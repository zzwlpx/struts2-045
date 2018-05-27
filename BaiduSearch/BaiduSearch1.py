#encoding: utf-8
#采集SERP搜索结果标题
import urllib2
import sys
import loggerbaidu
from bs4 import BeautifulSoup

#获取title和url
def GetTitleUrl(url,res_title,res_url,bShowRes):
  try:
    ##获取Html源码
    req = urllib2.Request(url)
    response= urllib2.urlopen(req,None,2)#设置超时时间
    data = response.read()#.decode('utf-8','ignore')
    response.close()
    ##提取搜索结果SERP的标题和链接
    soup = BeautifulSoup(''.join(data),'lxml')
    num = 0
    for i in soup.findAll("h3"):
      num += 1
      temp_title = i.a.text.encode("gbk")
      temp_url = i.a.get('href')
      response = urllib2.urlopen(temp_url)
      realurl = response.geturl()
      if bShowRes==1:
          loggerbaidu.log.info(realurl)
      res_title.append(temp_title)
      res_url.append(realurl)
  except:
      pass
  return (res_title,res_url)

###########Main Func###########
if __name__ == "__main__":
  keyword = raw_input("Search Content: ")
  keyword = keyword.replace(" ","+")
  searchnum = raw_input("Search Pages: ")
  res_title = []
  res_url = []
  mode = raw_input("Show By Pages(1) Or All(2)?: ")
  if mode == '1':
      ShowRes_Mode = 1
  elif mode == '2':
      ShowRes_Mode = 2
  else:
      loggerbaidu.loger.debug("ShowMode error!")
      sys.exit()
  start = raw_input("10 per page,From page: ")
  if start.strip() == '':
      start = 0
  else:
      start = int(start)
  #ShowRes_Mode = 2    #1: 分页显示；2：最后直接显示
  for i in range(start,int(searchnum)+start):
    if ShowRes_Mode==1:
        print("第%s页内容：".decode("utf8").encode("gbk") %(str(int(i))))
    '''
    wd：搜索关键字
    rn：每页显示10条结果
    pn：第几条开始
    '''
    url = "http://www.baidu.com/s?wd="+keyword+"&rn=10&pn="+str(int(i)*10)
    (res_title,res_url) = GetTitleUrl(url,res_title,res_url,ShowRes_Mode)
  if ShowRes_Mode == 2:
      for i in range(len(res_url)):
        loggerbaidu.log.info(res_url[i])


