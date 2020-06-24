source = open('data/zh_CN.lang').read()
diff = open('data/zh_PC.diff.lang').read()

def loadLang(lang_str):
    lang_map = {}
    lang_list = lang_str.splitlines()
    for lang_w in lang_list:
        if len(lang_w) == 0:
            continue
        if (lang_w[0] == '#' or lang_w[0] == ' '):
            continue
        lang_d = lang_w.split('=')
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

for k in diff_map:
    print(k+':'+source_map[k]+' -> '+diff_map[k])
    source_map[k]=diff_map[k]

with open('texts/zh_PC.lang','w') as f:
    f.write(exportLang(source_map))
    f.close()
        
