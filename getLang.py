from urllib  import request
import zipfile

def d(n,s,t):
    print(f"Downloading... {'%0.8f'%((n*s/t)*100)}%")

#p,_ = request.urlretrieve("https://aka.ms/resourcepacktemplate", "res.zip", d)

p = "res.zip"

with zipfile.ZipFile(p) as zf:
    print(zf.namelist())
    zf.extract("texts/zh_CN.lang", "data/")
