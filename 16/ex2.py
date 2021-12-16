import sys
import functools
import operator
class Buf:
    def __init__(self, buf):
        self.buf = []
        for x in map(ord, buf):
            if x <= ord('9'):
                lk = x-ord('0')
            else:
                lk = x-ord('A')+10
            for _ in range(4):
                if int(lk) & 8 == 0:
                    self.buf.append("0")
                else:
                    self.buf.append("1")
                lk *= 2
        self.buf = "".join(self.buf)
        self.cur = 0
        self.N = len(self.buf)
    def readN(self, n):
        self.cur += n
        return int(self.buf[self.cur-n:self.cur], 2)
input = Buf(sys.stdin.read().strip())


class Msg:
    pass

class LitMsg(Msg):
    def __init__(self, buf, ver, type):
        self.ver = ver
        self.type = type
        self.val = 0
        while(True):
            x = buf.readN(5)
            self.val = (self.val<<4)+(x&0b01111)
            if x&0b10000 == 0:
                break
    def eval(self):
        return self.val

class OprMsg(Msg):
    def __init__(self, buf, ver, type):
        self.ver = ver
        self.type = type
        self.val = []
        if buf.readN(1) == 0:
            len = buf.readN(15)
            end = buf.cur+len
            while buf.cur < end:
                self.val.append(readMsg(buf).eval())
        else:
            len = buf.readN(11)
            for _ in range(len):
                self.val.append(readMsg(buf).eval())
    def eval(self):
        if self.type == 0:
            return sum(self.val)
        elif self.type == 1:
            return functools.reduce(operator.mul, self.val)
        elif self.type == 2:
            return min(self.val)
        elif self.type == 3:
            return max(self.val)
        elif self.type == 5:
            return 1 if self.val[0] > self.val[1] else 0
        elif self.type == 6:
            return 1 if self.val[0] < self.val[1] else 0
        elif self.type == 7:
            return 1 if self.val[0] == self.val[1] else 0
        assert False

def readMsg(buf):
    ver = buf.readN(3)
    type = buf.readN(3)
    if type == 4:
        return LitMsg(buf, ver, type)
    else:
        return OprMsg(buf, ver, type)
msg = []
while input.cur+6 < input.N:
    msg.append(readMsg(input))
print(msg[0].eval())
