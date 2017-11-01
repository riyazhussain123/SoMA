import facebook
f=open("/opt/somaaccesstoken")
gapitoken=f.read().strip()
graph = facebook.GraphAPI(gapitoken)
