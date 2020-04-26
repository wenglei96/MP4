import os



# 删除下载的 .ts文件
def del_files(dir):
  path = dir
  for root , dirs, files in os.walk(path):
    for name in files:
      if name.endswith(".ts"):   #指定要删除的格式，这里是jpg 可以换成其他格式
        os.remove(os.path.join(root, name))
        print ("Delete File: " + os.path.join(root, name))

# test
# if __name__ == "__main__":
#   指定路径文件夹
#   path = 'F:\\PyDownload'
#   del_files(path)