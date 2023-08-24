f=open("demofile.py","a")
f.write("now the file has more content")
f.close()

f=open("demofile.py","r")
print(f.read())