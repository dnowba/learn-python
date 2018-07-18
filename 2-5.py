import time
import urllib.request
def get_price():
    page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
    text=page.read().decode("utf8")
    price=text.find('>$')
    start=price+2
    end=start+4
    totalprice=float(text[start:end])
    return(totalprice)

print("You want the price immediately?")
question = input("Y/N:")
yesno = str(question)
if yesno == "Y":
    print(get_price())
else:
    container=get_price()
    while container > 5:
        get_price()
        container=get_price()
        #debug
        print(container)
    print(container)
print("Here's the price")