def docfile(name):
    f = open(name, "r")
    data = f.readlines()
    f.close()
    D_data = {}
    for i in data:
        vt = i.find("|")
        if vt == -1:
            key = ""
            value = list(map(int,i.split()))
        else:
            key = i[:vt].strip()
            value = list(map(int,i[vt+1:].split()))
        D_data[key] = value
    return D_data

def vtmax(L):
    vt = None
    for i in range(len(L)):
        if vt == None or L[vt] < L[i]:
            vt = i
    return vt

def minimax(key,chieusau,b_max,root):
    L = data[key]
    if root:
        L_kq = []
        for i in range(len(L)):
            if chieusau != 1:
                nhanh = minimax(str(i),chieusau - 1,not b_max,False)
            else:
                nhanh = L[i]
            L_kq.append(nhanh)
        print(L_kq)
        return vtmax(L_kq)
    else:
        kq = None
        for i in range(len(L)):
            if chieusau != 1:
                nhanh = minimax(key + " " + str(i),chieusau - 1,not b_max,False)
            else:
                nhanh = L[i]
            if b_max:
                if kq == None or nhanh > kq:
                    kq = nhanh
            else:
                if kq == None or nhanh < kq:
                    kq = nhanh
        return kq

data = docfile("minimax2.txt")
import time
tg = round(time.time()*1000)
print(minimax("",2,True,True))
tg0 = round(time.time()*1000)
print(tg0 - tg)