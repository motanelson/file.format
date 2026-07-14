import struct
import math
def openw(names:str):
    return open(names,"bw")


def closew(f1):
    f1.close()


def writesS(f1,s:str):
    f1.write(s.encode())


def writesf(f1,f):
    f1.write(struct.pack('<f',f))

def writesi(f1,i):
    f1.write(struct.pack('<i',i))

print("\033c\033[47;30m\nwrite")

f1=openw("my.bin")
writesS(f1,"hello\n")
writesi(f1,int(128))
writesf(f1,math.pi)

closew(f1)

