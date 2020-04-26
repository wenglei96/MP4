import requests
import os
import time
from multiprocessing import Pool
from 视频下载 import m3u8
from 视频下载 import delete
from 视频下载 import dirbc

def run(i,m3u8_hls,dir):
    ##  拼接 .ts 文件
    url = m3u8_hls+'%04d.ts'%i
    print("开始下载："+url)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    r = requests.get(url, headers = headers,stream=True,timeout=600)
    ts = dir+url[-7:]
    with open(ts,'wb') as f:
        f.write(r.content)
        f.close()


def merge(t,cmd):
    time.sleep(t)
    res=os.popen(cmd)
    print(res.read())

def main_(m3u8_url):
    dir = dirbc.dir()
    m3u8s = m3u8.m3u8_(m3u8_url)
    # 创建进程池，执行10个任务
    pool = Pool(32)
    for i in range(m3u8s['gs']):
        pool.apply_async(run, (i,m3u8s['m3u8_hls'])) #执行任务
    pool.close()
    pool.join()
    #调用合并
    a ='copy /b '+dir+'*.ts '+dir+'new.mp4'
    #merge(5,"copy /b F:\\PyDownload\\*.ts F:\\PyDownload\\new.mp4")
    merge(5,a)
    #删除 .ts文件
    delete.del_files(dir)
    print('ok！处理完成')
    return 'successful'


# if __name__ == '__main__':
#
#     m3u8s = m3u8.m3u8_()
#
#     # 创建进程池，执行10个任务
#     pool = Pool(32)
#     for i in range(m3u8s['gs']):
#         pool.apply_async(run, (i,m3u8s['m3u8_hls'])) #执行任务
#     pool.close()
#     pool.join()
#     #调用合并
#     merge(5,"copy /b F:\\PyDownload\\*.ts F:\\PyDownload\\new.mp4")
#     #删除 .ts文件
#     delete.del_files()
#     print('ok！处理完成')
