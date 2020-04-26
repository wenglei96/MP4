# url解析 vip视频播放地址的模块 做url加密的
from urllib import parse
import tkinter.messagebox as msgbox # TK 如果出现错误会返回一个消息
import tkinter as tk # 做桌面编程的
import webbrowser # 控制浏览器的
import re # 正则表达式

from 视频下载 import web
from 视频下载 import main


class APP:
    # 魔术方法
    # 初始化用的
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = '视频播放下载助手'

        # 软件名
        self.root = tk.Tk(className=self.title)

        # vip视频播放地址 StringVar() 定义字符串变量
        self.url = tk.StringVar()

        # 定义选择哪个播放源
        self.v = tk.IntVar()

        # 默认为1
        self.v.set(2)

        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        frame_4 = tk.Frame(self.root)
        frame_5 = tk.Frame(self.root)

        # 控件内容设置
        bb = tk.Label(frame_1, text='版本: 1.0  qq:153242015', padx=10, pady=10)
        group = tk.Label(frame_2, text='暂时只有一个视频通道：', padx=10, pady=10)
        tb  = tk.Radiobutton(frame_3, text='一号通道', variable=self.v, value=1, width=10, height=3)
        lable = tk.Label(frame_5, text='请输入视频连接：')



        # 输入框声明
        # entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        TV1 = tk.Button(frame_4, text='腾讯视频', font=('楷体', 12), fg='Purple', width=2, height=1, command=web.TV1)
        TV2 = tk.Button(frame_4, text='爱奇艺视频', font=('楷体', 12), fg='Purple', width=2, height=1, command=web.TV2)

        entry = tk.Entry(frame_5, textvariable=self.url, highlightthickness=1, width=35)
        play = tk.Button(frame_5, text='播放', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)
        down = tk.Button(frame_5, text='下载', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_down)

        # 控件布局 显示控件在你的软件上
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
        frame_5.pack()

        # 确定控件的位置 wow 行 column 列
        bb.grid(row=0, column=0)
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        lable.grid(row=0, column=0)
        entry.grid(row=0, column=1)

        # ipadx x方向的外部填充 ipady y方向的内部填充
        play.grid(row=0, column=3, ipadx=10, ipady=10)
        down.grid(row=0, column=4, ipadx=10, ipady=10)
        TV1.grid(row=0, column=3, ipadx=30, ipady=10)
        TV2.grid(row=0, column=4, ipadx=30, ipady=10)


    def video_play(self):
        # 视频解析网站地址
        port = 'https://jx.618g.com/?url='
        # 正则表达式判定是否为合法连接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            # 拿到用户输入的视频网址
            ip = self.url.get()
            # 视频连接解密
            ips = parse.quote_plus(ip)
            # 用浏览器打开网址
            webbrowser.open(port + ips)
        else:
            msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')

    def video_down(self):
        # 视频解析网站地址
        port = 'https://jx.618g.com/?url='
        # 正则表达式判定是否为合法连接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):

            # 拿到用户输入的视频网址
            ip = self.url.get()
            # 视频连接解密
            ips = parse.quote_plus(ip)
            xy = main.main_(port + ips)
            if xy == 'successful':
                msgbox.showerror(title='下载成功', message='下载成功！！！继续或关闭')
            else:
                msgbox.showerror(title='下载失败', message='下载失败！！请重新尝试')
        else:
            msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')



    # 启动GUI程序的函数
    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()


if __name__ == "__main__":
    app = APP()
    app.loop()