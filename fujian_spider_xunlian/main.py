import time
import requests
from processing_img.processing_img import get_img

cookies = {
    'csrftoken': 'wKWcRKvFsb5WfPNNmdQtpj7fDO2HpHvUEnZIPwnphMvGcOtFA0Umb1hMTkS6qQ4H',
    'sessionid': '3qzbf7q9kcu9ulv20qz6w4ijajj4znv0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'image/avif,image/webp,*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'close',
}
id = 0
import os
path=r'img_library/'
if not os.path.exists(path):
    os.makedirs(r'img_library/')
while id!=100:
    id+=1
    print("-----------------------\n爬取第%d张图片"%id)
    response = requests.get('http://www.ccgp-fujian.gov.cn/noticeverifycode/', cookies=cookies, headers=headers)
    name = '%d_img_%d' % (id,int(time.time()))
    f=open('img_library/'+name+'.png','wb')
    f.write(response.content)
    f.close()
    get_img(name)