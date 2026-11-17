"""把 gen.py 產生的 out/report.html 轉成網站頁面 r/<日期>.html，並更新 dates.json。
用法：python3 build_site.py <out/report.html> <YYYY-MM-DD> <repo 目錄>"""
import sys, re, json, os
src, D, repo = sys.argv[1], sys.argv[2], sys.argv[3]
h = open(src, encoding='utf-8').read()
st = re.search(r'<style>(.*?)</style>', h, re.S).group(1)
st = re.sub(r'@page\s*\{[^}]*\}', '', st).replace("font-family: 'Noto Sans CJK HK';", "font-family: 'Noto Sans TC','Noto Sans CJK HK','PingFang TC','Microsoft JhengHei',sans-serif;")
st = re.sub(r'(^|\})\s*body\s*\{', r'\1 .rep{', st)
body = re.search(r'<body>(.*)</body>', h, re.S).group(1)
os.makedirs(f'{repo}/r', exist_ok=True)
open(f'{repo}/r/{D}.html', 'w', encoding='utf-8').write(f'<style>{st}</style><div class="rep">{body}</div>')
p = f'{repo}/dates.json'
ds = json.load(open(p)) if os.path.exists(p) else []
ds = sorted(set(ds) | {D}, reverse=True)
json.dump(ds, open(p, 'w'))
print('ok', D, len(ds))
