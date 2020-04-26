from tkinter import *

'''
LabelFrame（）
在一个labelframe一个简单的容器构件。其主要目的是作为一个间隔或复杂的窗口布局容器.
该部件有一帧的功能，加上能够显示标签.
'''
root = Tk()

group = LabelFrame(root, text='选择你喜欢的语言', padx=5, pady=5)
group.pack(padx=10, pady=10)

LANGS = [
    ('python', 1),
    ('Per1', 2),
    ('Ruby', 3),
    ('Lua', 4)]
print(type(LANGS))
v = IntVar()
# v.set(1)

for lang, num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num)
    # fill=X设置和其父窗口一样宽, 可以使用 fill=X 属性
    b.pack(anchor=W)

mainloop()
