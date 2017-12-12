from django.shortcuts import render,get_object_or_404
from .models import serverlist,userhostlist
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .form import ServerListForm

# Create your views here.
def server_list(request):
    user = request.user
    servers= serverlist.objects.all().order_by('id')
    paginator= Paginator(servers,10)

    try :
        page= int(request.GET.get('page','1'))
    except ValueError :
        page=1

    try :
        servers= paginator.page(page)
    except :
        servers= paginator.page(paginator.num_pages)

    return render(request, "serverlist.html", {'servers':servers, 'page':page, 'paginator':paginator})

def ServerManage(request,id=None,delete=None):
    if not id :     ##当前ID为空时，该请求是传统硬编码方式请求，需要手动获取参数值
        id = request.GET.get('id')
        delete=request.GET.get('delete')
    if request.method == 'GET':
       # id=request.GET['id']
        server=get_object_or_404(serverlist,pk=id)

        #delete=request.GET['delete']

        if delete:
            server.delete()
            return HttpResponseRedirect(reverse(server_list))
        else:
            form = ServerListForm(instance=server)
            return render(request, 'servermanage.html', {"form": form, "action": 'edit'})

    if request.method=='POST':
        serverhost = get_object_or_404(serverlist, pk=id)

        form= ServerListForm(request.POST,instance=serverhost)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(server_list))
    else:
        pass

def host_list(request):
    user = request.user
    hosts= userhostlist.objects.all().order_by('id')
    paginator = Paginator(hosts,10)

    try:
        page= int(request.GET.get('page','1'))
    except ValueError:
        page=1
    try:
        hostlist=paginator.page(page)
    except :
        hostlist=paginator.page(paginator.num_pages)
    return render(request,'userhostlist.html', {'hostlist':hostlist,'page':page,'paginator':paginator})

def PowerOn(request):
    if request.method == 'GET':
        return render(request,'addhost.html')

    if request.method == 'POST':
        return render(request,'addhost.html')
