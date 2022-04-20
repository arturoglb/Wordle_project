import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt')


