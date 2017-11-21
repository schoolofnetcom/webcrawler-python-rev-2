import os
import requests
from lxml import html

print 'URL : '
url = raw_input()
print 'Lang: '
lang = raw_input()

if (lang == 'pt'):
	url = url + '/?ned=pt-BR_br&hl=pt-BR&gl=BR'
else:
	url = url + '/?ned=us&hl=en&gl=US'

print url

response = requests.get(url)
f = open('titles.txt', 'w')

# request ok
if (response.status_code == 200):
	print('Response OK!')

	page = html.fromstring(response.text)
	# text = page.cssselect('a.nuEeue.hzdq5d.ME7ew')[0].text
	for a in page.cssselect('a.nuEeue.hzdq5d.ME7ew'):
		f.write(a.text_content().encode('utf-8') + os.linesep)
		# print (a.text_content().encode('utf-8'))

	f.close()
else:
	print("Request failed!")