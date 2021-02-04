from urllib  import request
import zipfile

def d(n,s,t):
    print(f"Downloading... {'%0.8f'%((n*s/t)*100)}%")

#p,_ = request.urlretrieve("https://aka.ms/resourcepacktemplate", "res.zip", d)

p = "res.zip"

with zipfile.ZipFile(p) as zf:
    zf.extract("texts/zh_CN.lang", "catch/")

with open("catch/texts/zh_CN.lang", encoding='utf8') as f:
    o = open("data/zh_CN.lang", "w", encoding='utf8')
    o.write(f.read())
    f.close()
    o.close()
