from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from asset.models import userhostlist
from .magicpackpet import SendMagicPacket

# Create your views here.
def PowerOn(request):
    if request.method== 'GET':
        return render(request,'wol/addhost.html')

def Index(request):
    if request.method == 'GET':
       return render(request, 'wol/index.html')

    if request.method == 'POST':
       username= request.POST['username']
       hostname= request.POST['hostname']
       #host= get_object_or_404(userhostlist , hostname=hostname)
       #host=userhostlist.objects.get(hostname='zhoubin')
       host= userhostlist.objects.filter(hostname=hostname)
       if host:
           try :
               ret = SendMagicPacket(host.ip,host.mac)
               return HttpResponse(ret)

           except :
               return HttpResponse('发送失败')
       else:
           user= get_object_or_404(userhostlist, username=username)
           if user:
               ret= SendMagicPacket(user.ip,user.mac)
               return HttpResponse(ret)
    return  HttpResponse("用户名或主机不正解")




