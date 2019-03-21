import json


kb = json.load(open('kb.json'))
kbid = 'https://en.wikipedia.org/wiki/HMS_Romney_(1708)'
article = kb[kbid]['article']
print(article)
links = kb[kbid]['links']
print(links)
