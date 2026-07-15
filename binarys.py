import struct
import math
def openw(names:str):
    return open(names,"bw")

def openr(names:str):
    return open(names,"br")

def opena(names:str):
    return open(names,"ba")


def closew(f1):
    f1.close()


def writesS(f1,s:str):
    f1.write(s.encode())


def writesf(f1,f):
    f1.write(struct.pack('<f',f))

def writesi(f1,i:int):
    f1.write(struct.pack('<i',i))

def readsS(f1,i:int):
    r=f1.read(i)
    a=r.decode()
    return a

def readsf(f1):
    r=f1.read(4)
    ff=struct.unpack('<f',r)
    return ff[0]

def readsi(f1):
    r=f1.read(4)
    ii=struct.unpack('<i',r)
    return ii[0]

def writesb(f1,c):
    f1.write(bytearray(c))
    
def writesf(f1,f):
    f1.write(struct.pack('<f',f)) 

def writesh(f1,i:int):
    f1.write(struct.pack('>H',i))
   
def savesS(f1,s:str):
    writesb(f1,[1])
    writesh(f1,len(s)+1)
    ss=s+"\x00"
    writesS(f1,ss)

def savesm(f1,ar):
    for a in ar:
        savesS(f1,a)


def savesSBs(f1,ar):
    writesb(f1,[1])
    writesh(f1,len(ar)+1)
    ar.append(0)
    writesb(f1,ar)

print("\033c\033[47;30m\nwrite")
r="hello world....\n"
rr=len(r)
f1=openw("my.bin")
savesm(f1,["hello world...","hi there...","java hello..."])
savesSBs(f1,[0,1,2,3,4,5,6,7,8,9,0])
closew(f1)

