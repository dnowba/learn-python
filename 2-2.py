import urllib.request
page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty/html")
text=page.read().decode("utf8")
price=text.find('$')
start=price+1
end=price+5
totalprice=text[start:end]
print(totalprice)