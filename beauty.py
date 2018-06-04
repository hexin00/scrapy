from bs4 import BeautifulSoup
import requests
import random
def save_img(img,img_extension):
    response = requests.get(img)
    with open('/root/py3/image/'+str(random.random())+img_extension, 'wb') as f:
        f.write(response.content)
        f.close()
def img_extension(str):
    img_extension = str[str.rfind('.'):]
    return img_extension
def save(http):
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "utf-8",
        "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Host": "beautyleg7.com",
        "Referer": "http://www.beautyleg7.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
    }
    response = requests.get(http, headers=header)

    # 查看响应内容，response.text 返回的是Unicode格式的数据
    html = response.content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    imgs = soup.select('.contents img')
    for i in imgs:
        jpg = img_extension(i['src'])
        save_img(i['src'],jpg)

def find_last_two(str):
    weizhi = str.rfind('/')
    weizhi2 = str[:weizhi]
    new = weizhi2.rfind('/')
    return str[new:weizhi+1]



def main(url):
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "utf-8",
        "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Host": "beautyleg7.com",
        "Referer": "http://www.beautyleg7.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
    }
    url = url

    response = requests.get(url[0], headers=header)
    html = response.content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    list = soup.select('.page li a')
    for a in list[3:-1]:
        url.append('http://www.beautyleg7.com/siwameitui' + find_last_two(url[0]) + a['href'])
    for url in url:
        save(url)
src = [['http://www.beautyleg7.com/siwameitui/201707/650.html']]

for s in src:
    main(s)