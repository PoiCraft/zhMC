import json
import datetime
import pytz
import hashlib
import sys

m = hashlib.md5()

class NothingChangedException(Exception):
    pass

info = json.loads(open('manifest.json').read())
version = '.'.join([str(v) for v in info['header']['version']])
time = datetime.datetime.now(pytz.timezone('UTC')).strftime('%Y-%m-%d %H:%M:%S')

source = open('data/zh_CN.lang').read()
diff = open('data/zh_PC.diff.lang').read()
sweetwinter = open('data/sweetwinter/zh_CN.sweetwinter.lang').read()
sweetwinter_keys = open('data/sweetwinter/zh_CN.sweetwinter.txt').read().splitlines()

sign_str = diff.encode(encoding='utf-8') + sweetwinter.encode(encoding='utf-8')
m.update(sign_str)
sign = f'Sign: {m.hexdigest()}'

sign_old = open('texts/zh_PC.lang').read().splitlines()[0]

print(sign_old,sign)
if ('#'+sign) == sign_old:
    print('Nothing Changed')
    sys.exit()

extra = [
        sign,
        'Github: https://github.com/PoiCraft/zhMC',
        f'Version: {version}',
        f'BuildAt: {time} UTC'
        ]

def loadLang(lang_str):
    lang_map = {}
    lang_list = lang_str.splitlines()
    for lang_w in lang_list:
        if len(lang_w) == 0:
            continue
        if (lang_w[0] == '#' or lang_w[0] == ' '):
            continue
        lang_d = lang_w.split('=')
        if len(lang_d) < 2:
            continue
        if not '.' in lang_d[0]:
            continue
        lang_map[lang_d[0]] = lang_d[1]
    return lang_map

def exportLang(lang_map):
    lang_list=[]
    for v in extra:
        lang_list.append('#'+v)
    for k in lang_map:
        lang_list.append(k+'='+lang_map[k])
    lang_str = '\n'.join(lang_list)
    return lang_str

source_map = loadLang(source)
diff_map = loadLang(diff)
sweetwinter_map = loadLang(sweetwinter)

for k in diff_map:
    print(k+':'+source_map[k]+' -> '+diff_map[k])
    source_map[k]=diff_map[k]

for k in sweetwinter_keys:
    print('Thank Coolapk@甜冬SweetWinter')
    print(k+':'+source_map[k]+' -> '+sweetwinter_map[k])
    source_map[k]=sweetwinter_map[k]

with open('texts/zh_PC.lang','w') as f:
    f.write(exportLang(source_map))
    f.close()
        
