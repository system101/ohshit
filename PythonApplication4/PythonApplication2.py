import turtle
class Hanoi(object):
    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            disk1 = Disk("d"+str(i),0,i*150,20,(n-i)*30)
            self.startp.pushdisk(disk1)
    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)
    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)
    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)
class Disk(object):
    def __init__(self,name,y,x,h,w):
        self.name = name
        self.x = x
        self.y = y-80
        self.h = h
        self.w = w
        self.c = "blue"
    def showdisk(self):
        turtle.pu()
        turtle.goto(self.x,self.y)
        turtle.pd()
        turtle.color(self.c,self.c)
        turtle.begin_fill()
        turtle.goto(self.x+(self.w/2),self.y)
        turtle.goto(self.x+(self.w/2),self.y-self.h)
        turtle.goto(self.x-(self.w/2),self.y-self.h)
        turtle.goto(self.x-(self.w/2),self.y)
        turtle.goto(self.x,self.y)
        turtle.end_fill()
        turtle.pu()
        return 0
    def newpos(self,x1,y1):
        self.x = x1
        self.y = y1
        return 0
    def cleardisk(self):
        turtle.pu()
        turtle.goto(self.x,self.y)
        turtle.pd()
        turtle.color("white","white")
        turtle.begin_fill()
        turtle.goto(self.x+(self.w/2),self.y)
        turtle.goto(self.x+(self.w/2),self.y-self.h)
        turtle.goto(self.x-(self.w/2),self.y-self.h)
        turtle.goto(self.x-(self.w/2),self.y)
        turtle.goto(self.x,self.y)
        turtle.end_fill()
        turtle.pu()
        turtle.pu()
        turtle.goto(self.x,self.y)
        turtle.pd()
        turtle.color("red","red")
        turtle.begin_fill()
        turtle.goto(self.x+(10/2),self.y)
        turtle.goto(self.x+(10/2),self.y-self.h)
        turtle.goto(self.x-(10/2),self.y-self.h)
        turtle.goto(self.x-(10/2),self.y)
        turtle.goto(self.x,self.y)
        turtle.end_fill()
        turtle.pu()
        return 0
class Pole(object):
    def __init__(self,name,x,y):
        self.name = name
        self.stack = []
        self.top = 0
        self.x = x
        self.y = y
        self.t = 10
        self.l = 100
        self.c = "red"
    def showpole(self):
        turtle.pu()
        turtle.goto(self.x,self.y)
        turtle.pd()
        turtle.color(self.c,self.c)
        turtle.begin_fill()
        turtle.goto(self.x+(self.t/2),self.y)
        turtle.goto(self.x+(self.t/2),self.y-self.l)
        turtle.goto(self.x-(self.t/2),self.y-self.l)
        turtle.goto(self.x-(self.t/2),self.y)
        turtle.goto(self.x,self.y)
        turtle.end_fill()
        turtle.pu()
        return 0
    def pushdisk(self,disk):
        disk.newpos(self.x,self.top+self.y-self.l+20)
        self.stack.append(disk)
        self.top += 20
        disk.showdisk()
        return 0
    def popdisk(self):
        disk = self.stack.pop()
        disk.cleardisk()
        disk.newpos(self.x,self.top+self.y-self.l+20)
        self.top -= 20
        return disk
h = Hanoi()
h.solve()
turtle.mainloop()