import urllib.request
import os
import base64,re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    
    return html
def get_page(url):
    html = url_open(url).decode('utf-8')
    
    a = html.find('current-comment-page')+23
    b = html.find(']',a)
    return html[a:b]
    
def find_imgs(page_url):
    html = url_open(page_url).decode('utf-8')
    img_addrs=[]
      
    res = re.findall('<span class="img-hash">([^<]+)', html)
     
    for item in res:
        link = 'http:' + str(base64.b64decode(item), 'utf-8')
        img_addrs.append(link)
        #print(link)

    #print(type(res))
    return img_addrs
        
    '''
    #一下图片都被加密了，无法直接得到源码
    while a != -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])      
        else:
            b=a+9
            
        a = html.find('img src=',b)
    '''
    
def save_imgs(img_addrs,folder='ooxx'):
    for i in img_addrs:
        filename = i.split('/')[-1]
        img = url_open(i)
        with open(filename,'wb') as f:
            f.write(img)
        

def download_mm(folder='ooxx',pages=2):
    os.mkdir(folder)
    os.chdir(folder)
    url = 'http://jandan.net/ooxx/'

    page_num = int(get_page(url))
    

    for i in range(pages):
        page_num -= i
    page_url = url + 'page-'+ str(page_num)+'#comments'
    img_addrs = find_imgs(page_url)
    save_imgs(img_addrs,folder)
        

if __name__ == '__main__':
    download_mm()
