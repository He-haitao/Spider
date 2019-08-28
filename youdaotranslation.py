import urllib.request
import urllib.parse
import json
import time
#ctrl+]缩进，ctrl+[取消缩进
while True:
    content = input('请输入需要翻译的内容(输入q!退出程序)： ')
    if content == 'q!':
        break
    
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    date={}

    date['i']=content
    date['from']='AUTO'
    date['to']= 'AUTO'
    date['smartresult']='dict'
    date['client']='fanyideskweb'
    date['salt']='1533087768209'
    date['sign']= 'c9b051aae2d852af3c4d6e7237fa97b2'
    date['doctype']='json'
    date['version']='2.1'
    date['keyfrom']='fanyi.web'
    date['action']='FY_BY_REALTIME'
    date['typoResult']='false'
    date = urllib.parse.urlencode(date).encode('utf-8')
    
    #隐藏 添加header  法1：

    head ={}
    '''
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    '''
    #req.headers会返回上面的内容


    req = urllib.request.Request(url,date,head)
    #隐藏 添加header 法2：
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print("翻译结果为: %s" % (target['translateResult'][0][0]['tgt']))

    time.sleep(2)
