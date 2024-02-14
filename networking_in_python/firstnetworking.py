import urllib.request

p=input("paste an Urll link you want to access : ")

try:
    r=urllib.request.urlopen("https://"+p)
    content=r.read()
    r.close()
except urllib.error.HTTPError:
    print(">>>>! entered URLL is notfound !<<<<")
    exit()
f=open("python.html",'wb')
f.write(content)
f.close()


# download image
urllib.request.urlretrieve("https://i.pinimg.com/originals/31/b2/3b/31b23ba6a051a0abc69c7c65a0a26552.jpg","image.png")