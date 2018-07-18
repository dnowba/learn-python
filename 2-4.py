def get_price():
    import urllib.request
    page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
    text=page.read().decode("utf8")
    price=text.find('>$')
    start=price+2
    end=start+4
    return(text[start:end])
print(get_price())