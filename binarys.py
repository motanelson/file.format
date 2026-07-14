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
    writesh(f1,len(s))
    ss=s+"\x00"
    writesS(f1,ss)


print("\033c\033[47;30m\nwrite")
r="hello world....\n"
rr=len(r)
f1=openw("my.bin")
savesS(f1,r)
closew(f1)

