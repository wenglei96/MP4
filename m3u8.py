
import os
import requests
from bs4 import  BeautifulSoup

# 用于m3u8数据解析

def m3u8_(url):
    #url ='https://jx.618g.com/?url=https://v.qq.com/x/cover/gfmdwy050xqp85e.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    re = requests.get(url,headers=headers)
    #print('加密视频地址响应值：',re.status_code)

    # 加密视频播放地址信息解析,获取 m3u8 地址信息
    s = BeautifulSoup(re.content, 'html.parser')
    #视频名称
    titles = s.find('title').text
    t = titles.split(' ')
    title = ''
    for aa in t:
        title += aa
    print('视频名称',title)
    src = s.find('div',class_='player').find('iframe')
    #print(src)
    m3u8 =src.get('src')
    m3u8_url = (m3u8.split('='))[1]
    #print(m3u8_url)


    # 加密视频地址解析
    r = requests.get(m3u8_url)
    r.encoding='utf-8'
    print('m3u8响应值',r.status_code)
    #print(r.text)

    # 合成带有hls的m3u8地址
    #https://youku.cdn7-okzy.com/20200114/16664_9145d65f/1000k/hls/index.m3u8
    if r.text.split('\n')[-1] == '':
        hls_mark = r.text.split('\n')[-2] # 以防\n结尾
    else:
        hls_mark = r.text.split('\n')[-1]
    url_m3u8_hls = m3u8_url.replace('index.m3u8',hls_mark)
    print('hls的m3u8地址',url_m3u8_hls)


    # 带有hls的m3u8文件中获得的是ts信息
    # 包括ts文件名称，以及该文件的持续时间
    m3u8s = requests.get(url_m3u8_hls)

    # 这个文件有用，先保存一下
    file_m3u8s = url_m3u8_hls.split('/')[-1]
    with open(file_m3u8s,'wb') as f:
        f.write(m3u8s.content)

    #获取 .ts数据
    # iter_lines得到的是bytesstring
    text_bytes = list(m3u8s.iter_lines())
    # 转化成正常string
    text_string = [i.decode('utf-8') for i in text_bytes]
    #print(text_string)

    # 筛选以.ts结尾的行
    # 有些情况下可能是以其他格式的文件，比如png，下载后修改后缀即可
    # ts_name = [i for i in text_string if i.endswith('.ts')]
    ts_name = [i for i in text_string if not i.startswith('#')]
    pt =(url_m3u8_hls.split('index.m3u8'))[0]+ts_name[0]

    print('首个.ts文件',pt)
    print(pt[0:-7])
    print('.ts文件个数',len(ts_name))

    m3u8_ss ={
        'm3u8_hls':pt,
        'gs':len(ts_name),
        'title':title
    }
    return  m3u8_ss



# if __name__ == '__main__':
#     a =m3u8_()
#     print(a['m3u8_hls'])
#     print(a['gs'])