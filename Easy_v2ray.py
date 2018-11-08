import json
import requests
import subprocess
import os
import tkinter
import webbrowser

mveid = ''
mapikey = ''


#弹出搬瓦工购买教程
def btn1click():
    webbrowser.open('https://atrandys.com/2018/266.html', new=2, autoraise=True)

#保存参数
def btn2click():
    global mveid, mapikey
    mveid = veid.get()
    mapikey = apikey.get()
    savedict = [mveid,mapikey]
    f = open('config.txt', 'w')
    f.write(str(savedict))
    f.close()
    text.insert('insert','√参数已保存到config.txt文件\n')

#获取保存的配置
def getconfig():
    global mveid,mapikey
    f = open('config.txt', 'r')
    a = f.read()
    if len(a) > 0:
        getdict = eval(a)
        mveid = getdict[0]
        mapikey = getdict[1]
        f.close()

#重新安装系统
def reinstallos():
    global mveid, mapikey
    stopurl = 'https://api.64clouds.com/v1/stop?veid=' + mveid +'&api_key=' + mapikey
    response = requests.post(stopurl)
    resjson = response.text
    resdict = json.loads(resjson)
    if resdict['error'] == 0:
        reinsurl = 'https://api.64clouds.com/v1/reinstallOS?os=centos-7-x86_64-bbr&veid='+mveid + '&api_key='+mapikey
        reinsresp = requests.post(reinsurl)
        reinsresj = reinsresp.text
        reinsdict = json.loads(reinsresj)
        if reinsdict['error'] == 0:
            text.insert('insert','√重装系统命令执行成功，重装系统需要大概5分钟，请耐心等待后进入步骤④,root密码变更为：'+ reinsdict['rootPassword'] + '，ssh端口为:' + str(reinsdict['sshPort'])+'\n')
        else:
            text.insert('insert','×重装系统命令执行失败，请稍后重试\n')
    else:
        text.insert('insert','×停止VPS失败，请稍后重试\n')

#安装Prov脚本
def installprov():
    global mveid, mapikey
    insprov = 'https://api.64clouds.com/v1/basicShell/exec?command=curl -O https://raw.githubusercontent.com/yobabyshark/proV/master/config_v2ray.sh %26%26 chmod %2Bx config_v2ray.sh %26%26 ./config_v2ray.sh&veid=' + mveid +'&api_key=' + mapikey
    insresp = requests.post(insprov)
    insresj = insresp.text
    insdict = json.loads(insresj)
    if insdict['error'] == 0:
        text.insert('insert', '√安装命令已执行，请稍等几分钟查看客户端配置参数\n')
    else:
        text.insert('insert', '×prov安装脚本未正确运行，请稍后重试\n')


#获取prov的配置参数
def getprovconfig():
    global mveid, mapikey
    getprovurl = 'https://api.64clouds.com/v1/basicShell/exec?command=cat /etc/v2ray/myconfig.json&veid=' + mveid +'&api_key=' + mapikey
    getresp = requests.post(getprovurl)
    getresj = getresp.text
    getdict = json.loads(getresj)
    text.delete(1.0,20.0)
    text.insert('insert',getdict['message']+'\n')

#打开客户端
def openprov():
    mydir = os.getcwd()
    subprocess.Popen([mydir+'\\proV_win_64\\v2rayN.exe'])
    text.insert('insert', '√prov客户端已打开，在电脑右下角任务栏中查看\n')



#打开客户端配置教程
def btn6click():
    webbrowser.open('https://atrandys.com/2018/271.html', new=2, autoraise=True)

#执行从本地文件获得保存的参数
getconfig()

#主体窗口配置
window = tkinter.Tk()
#title
window.title('Easy_v2ray - Based on Bandwagon')
window.iconbitmap('./src/easyprov.ico')
#设置窗口居中
xlocation = (window.winfo_screenwidth() - 1000)/2
ylocation = (window.winfo_screenheight() - 700)/2
window.geometry('1000x700+%s+%s'%(int(xlocation),int(ylocation)))

#顶部标题
titlestr = 'Easy_v2ray 适用win7/8/10 64位'
title = tkinter.Label(window,text=titlestr,font=('微软雅黑',12,'bold'),fg='#4FB17D')
title.place(x=50,y=10,width=240,height=50)

#教程说明lable
toplablestr = '说明：软件基于搬瓦工服务器开发，请按步骤①教程在搬瓦工官网购买服务器，购买的服务器为您私人所有，本软件只是调用搬瓦工API，方便您安装prov。请按教程步骤逐步执行即可，重装系统和安装prov需要几分钟的时间，注意看输出信息。'
toplable = tkinter.Label(window,text=toplablestr,font=('微软雅黑',12),bg='#4FB17D',wraplength = 900)
toplable.place(x=50,y=80,width=900,height=80)

#步骤1
img1 = tkinter.PhotoImage(file = './src/1.png')
label_img1 = tkinter.Label(window, image = img1)
label_img1.place(x=60,y=180)
step1 = tkinter.Label(window,text='点击查看购买教程，购买并获取VEID和API Key。',font=('微软雅黑',10),wraplength = 160)
step1.place(x=20,y=260)
btn1 = tkinter.Button(window,text='查看购买教程',bg='#4FB17D',width=15,height=2,command=btn1click)
btn1.place(x=40,y=380)

#步骤2
img2 = tkinter.PhotoImage(file = './src/2.png')
label_img2 = tkinter.Label(window, image = img2)
label_img2.place(x=260,y=180)
step2 = tkinter.Label(window,text='将①中获得的参数填入点击保存参数，进入步骤③。',font=('微软雅黑',10),wraplength = 160)
step2.place(x=220,y=260)
veidstr = tkinter.Label(window,text='VEID:',font=('微软雅黑',10),width=15,height=1)
veidstr.place(x=170,y=310,)
veid = tkinter.Entry(window,width=20)
veid.insert(0,mveid)
veid.place(x=270,y=310,)
apikeystr = tkinter.Label(window,text='APIkey:',font=('微软雅黑',10),width=15,height=1)
apikeystr.place(x=170,y=340,)
apikey = tkinter.Entry(window,width=20)
apikey.insert(0,mapikey)
apikey.place(x=270,y=340,)
btn2 = tkinter.Button(window,text='保存参数',bg='#4FB17D',width=15,height=2,command=btn2click)
btn2.place(x=240,y=380)

#步骤3
img3 = tkinter.PhotoImage(file = './src/3.png')
label_img3 = tkinter.Label(window, image = img3)
label_img3.place(x=480,y=180)
step3 = tkinter.Label(window,text='点击重装系统，等待5分钟后进入步骤④。',font=('微软雅黑',10),wraplength = 160)
step3.place(x=440,y=260)
btn3 = tkinter.Button(window,text='重装系统',bg='#4FB17D',width=15,height=2,command=reinstallos)
btn3.place(x=460,y=380)

#步骤4
img4 = tkinter.PhotoImage(file = './src/4.png')
label_img4 = tkinter.Label(window, image = img4)
label_img4.place(x=680,y=180)
step4 = tkinter.Label(window,text='点击安装proV，等待2分钟点击查看配置参数，将参数复制保存好。',font=('微软雅黑',10),wraplength = 160)
step4.place(x=640,y=260)
btn4 = tkinter.Button(window,text='安装ProV',bg='#4FB17D',width=15,height=2,command=installprov)
btn4.place(x=660,y=380)
btn_a = tkinter.Button(window,text='查看配置参数',fg='#4FB17D',width=15,height=2,command=getprovconfig)
btn_a.place(x=660,y=440)

#步骤5
img5 = tkinter.PhotoImage(file = './src/5.png')
label_img5 = tkinter.Label(window, image = img5)
label_img5.place(x=864,y=180)
step5 = tkinter.Label(window,text='点击打开客户端，会打开客户端软件，然后查看客户端教程。',font=('微软雅黑',10),wraplength = 160)
step5.place(x=828,y=260)
btn5 = tkinter.Button(window,text='打开客户端',bg='#4FB17D',width=15,height=2,command=openprov)
btn5.place(x=848,y=380)
btn6 = tkinter.Button(window,text='查看客户端教程',fg='#4FB17D',width=15,height=2,command=btn6click)
btn6.place(x=848,y=440)

#输出title
titlestr = '输出信息'
title = tkinter.Label(window,text=titlestr,font=('微软雅黑',12,'bold'),fg='#000000')
title.place(x=20,y=470,width=120,height=20)

#输出信息
text = tkinter.Text(window,font=('微软雅黑',8),fg='#B42958')
text.place(x=50,y=500,width=900,height=190)
window.mainloop()

