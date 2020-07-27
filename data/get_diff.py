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
diff = open('data/sweetwinter/zh_CN.sweetwinter.lang').read()
diff_mine = open('data/zh_PC.diff.lang').read()

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
    for k in lang_map:
        lang_list.append(k+'='+lang_map[k])
    lang_str = '\n'.join(lang_list)
    return lang_str

source_map = loadLang(source)
diff_map = loadLang(diff)
diff_map_mine = loadLang(diff_mine)

output_map={}

for k in diff_map:
    if source_map.get(k,'') != diff_map.get(k,''):
        output_map[k] = diff_map.get(k,'') + '\n##' + source_map.get(k, '') + '|' + diff_map_mine.get(k, '')

with open('data/sweetwinter/zh_CN.diff.sweetwinter.lang','w') as f:
    f.write(exportLang(output_map))
    f.close()