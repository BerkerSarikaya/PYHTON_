# there are strings on your lists
# try to write on your screen strings that just involved numbers

list1 = ["berker","berker321","321","333","454532","33berkers"]
for a in list1:
    try:
        a = int(a)
        print("a",a)
    except:
        print("error")
    print("blocks over")
