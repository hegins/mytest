from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from asset.models import userhostlist
from .magicpackpet import SendMagicPacket
from .form import addHostForm

# Create your views here.
def PowerOn(request):
    if request.method == 'GET':
        return render(request,'wol/addhost.html')

def Index(request):
    error=[]
    if request.method == 'GET':
       return render(request, 'wol/index.html',{'error':error})

    if request.method == 'POST':
       username= request.POST['username']
       hostname= request.POST['hostname']
       #host= get_object_or_404(userhostlist,hostname=hostname )
      # host=userhostlist.objects.get(hostname=hostname)
       host= userhostlist.objects.filter(hostname=hostname)
       if host:
          try :
               host = userhostlist.objects.get(hostname=hostname)
               print(host.ip,host.mac)
               ret = SendMagicPacket(host.ip,host.mac)
               return HttpResponse(ret)
          except :
               error.append('发送失败')
               return render(request,'wol/index.html',{'error':error})
       else:
           #user= get_object_or_404(userhostlist, username=username)
           user=userhostlist.objects.filter(username=username)
           if user:
               user=userhostlist.objects.get(username=username)
               ret= SendMagicPacket(user.ip,user.mac)
               return HttpResponse(ret)
           else:
                error.append('用户名或主机不存在')
    return  render(request,'wol/index.html',{'error':error})

def AddHost(request):
    if request.method == 'POST':
        try:
            userhostlist.objects.create(ip=request.POST['ip'])
        except :
            return  HttpResponse("添加失败")
        return HttpResponse('添加成功')

    return render(request,'addhost.html')


def AddServer(request):
    return render(request,'wol/addserver.html')




