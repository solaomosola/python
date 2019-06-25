from urllib import request,parse,error
import xml.etree.ElementTree as ET
import json
lines = request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

for line in lines:
    words = line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1

print(counts)

data = '''
<hi>
<hello>
Good
</hello>
</hi>
'''
tree = ET.fromstring(data)
print(tree.find('hello').text)

jsonData = ''' 
{"name":"Chuck",
"phone":{
        "type":"intl",
        "number":"09090980888"
        },
"email":{
        "hide":"please"
}
}
'''
info = json.loads(jsonData)
print(info["phone"]["number"])