import re

html = open('d:/Git-Repos/infernum/index.html', encoding='utf-8').read()

subtitle_gone = 'profile-sub">' not in html
focus_gone = 'Wide area' not in html
role_gone = 'profile-kv-val">Designer' not in html

css_match = re.search(r'<style>(.*?)</style>', html, re.S)
css = css_match.group(1)
depth = sum(1 if c == '{' else -1 if c == '}' else 0 for c in css)
css_ok = depth == 0

print('subtitle gone:', subtitle_gone)
print('Focus gone:', focus_gone)
print('Role gone:', role_gone)
print('CSS balanced:', css_ok, '(depth=%d)' % depth)
