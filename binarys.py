import struct
import math
def openw(names:str):
    return open(names,"bw")

def openr(names:str):
    return open(names,"br")

def openr(names:str):
    return open(names,"ba")


def closew(f1):
    f1.close()


def writesS(f1,s:str):
    f1.write(s.encode())


def writesf(f1,f):
    f1.write(struct.pack('<f',f))

def writesi(f1,i:int):
    f1.write(struct.pack('<i',i))

def readsS(f1,s:str,i:int):
    r=f1.read(i)
    a=r.decode()

def readsf(f1):
    r=f1.read(4)
    ff=struct.unpack('<f',r)
    return ff

def writesi(f1):
    r=f1.write(4)
    ii=struct.pack('<i',r)
    return ii

print("\033c\033[47;30m\nwrite")
r="hello\n"
rr=len(r)
f1=openw("my.bin")
writesS(f1,"hello\n")
writesi(f1,128)
writesf(f1,math.pi)
f1=openr("my.bin")
print(readsS(f1,rr))
print(readsi(f1))
print(readsf(f1))

closew(f1)

