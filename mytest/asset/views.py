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

def server_manage(request):
    print('aaa')
    if request.method=='GET':
        id=request.GET.get('id')
        server=get_object_or_404(serverlist,pk=id)
        edit=request.GET['edit']
        delete=request.GET['delete']
        if edit:
            form=ServerListForm(instance=server)
            return render(request,'servermanage.html',{"form":form, "action":'edit'})

        if delete:
            server.delete()
            return HttpResponseRedirect(reverse(server_list))
        else:
            pass

    if request.method=='POST':
        serverhost = get_object_or_404(serverlist, pk=id)
        id=request.POST.get('id')
        print(id)
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