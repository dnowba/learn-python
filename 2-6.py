import urllib.request

def send_to_twitter():
    msg= "TEST123"
    password_manager=urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API","https://api.twitter.com/1.1/statuses","dnowba","DNOWBA0109")
    http_handler=urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener=urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params=urllib.parse.urlencode({'statue':msg}).encode(encoding="utf8")
    resp=urllib.request.urlopen("https://api.twitter.com/1.1/statuses/update.json",params)
    resp.read()
send_to_twitter()
