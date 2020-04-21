import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y        
    def __str__(self):
        if abs(self.x) == 0:
            self.x = 0
        if abs(self.y) == 0:
            self.y = 0
        return '({:.2f}, {:.2f})'.format(self.x,self.y)
    def distanceTo(self, p2):
        return math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2)

class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        if self.A < 0:
            A = '-{:.2f}'.format(abs(self.A))
        else:
            A = '{:.2f}'.format(abs(self.A))
        if self.B < 0:
            B = '- {:.2f}'.format(abs(self.B))
        else:
            B = '+ {:.2f}'.format(abs(self.B))            
        if self.C < 0:
            C = '- {:.2f}'.format(abs(self.C))
        else:
            C = '+ {:.2f}'.format(abs(self.C))            

        return A+'x '+B+'y '+C+' = 0'
    
    def nearPoint(self, Point):
        k2 = self.B/self.A
        c2 = Point.y - k2*Point.x
        l2 = Line(-k2,1,-c2)
        return self.intersection(l2)   
    
    def oneSide(self,p1,p2):
        l2 = self.fromCoord(p1.x, p1.y, p2.x, p2.y)
        p3 = self.intersection(l2)
        if abs(p1.x - p3.x)<0.001 or abs(p2.x - p3.x)<0.001  or abs(p1.y - p3.y)<0.001  or abs(p2.y - p3.y)<0.0001:
            return True
        if (p1.x > p3.x and p2.x < p3.x) or (p1.y > p3.y and p2.y < p3.y):
            return False
        else:
            return True
        
    def isParallel(self, l2):
        l0 = self.A*l2.B
        l1 = self.B*l2.A
        return abs(l1-l0) <= 0.001
    
    def intersection(self, l2):
        if self.B == 0:
            a = 0
            c = 0
        else: 
            a = -self.A/self.B
            c = -self.C/self.B
        if l2.B == 0:
            b = 0
            d = 0
        else:
            b = -l2.A/l2.B
            d = -l2.C/l2.B
        if self.isParallel(l2) == False:
            x = (d - c)/(a - b)
            y = (a*d - b*c)/(a - b)
            return Point(x,y)
        else:
            return None
    
    def normalize(self):
        if abs(self.A) == 0:
            self.A = 0
        if abs(self.B) == 0:
            self.B = 0
        if abs(self.C) == 0:
            self.C = 0
        if self.C != 0:
            self.A = self.A/self.C
            self.B = self.B/self.C
            self.C = 1
        elif self.A != 0:
            self.B = self.B/self.A
            self.A = 1
        else:
            self.B = 1
        return self.__str__()
    
    def perpendicularLine(self, Point):        
        a = self.B/self.A
        c = (self.B/self.A)*Point.x - Point.y
        return Line(a, -1, -c)
    
    def parallelLine(self, Point):
        l2 = self.perpendicularLine(Point)
        a  = l2.B/l2.A
        c = (l2.B/l2.A)*Point.x - Point.y
        return Line(a, -1, -c)
    
    def projectionLength(self, p1, p2):
        l1 = self.perpendicularLine(p1)
        p11 = self.intersection(l1)
        l2 = self.perpendicularLine(p2)
        p22 = self.intersection(l2)
        return math.sqrt((p22.x-p11.x)**2+(p22.y-p11.y)**2)
    
    def middlePoint(self, p1):
        l1 = self.perpendicularLine(p1)
        p2 = self.intersection(l1)  
        if p1.x > p2.x:
            dx = p1.x+p2.x
        elif p2.x > p1.x:
            dx = p2.x+p1.x
        else:
            dx = 0
        if p1.y > p2.y:
            dy = p1.y+p2.y
        elif p2.y > p1.y:
            dy = p2.y+p1.y
        else:
            dy = 0
        return Point(dx/2,dy/2)      

    def symmetricPoint(self, p1):
        l1 = self.perpendicularLine(p1)
        p2 = self.intersection(l1) 
        if p2.x > p1.x:
            x = p2.x + p2.x - p1.x
        elif p2.x < p1.x:
            x = p2.x - (p1.x - p2.x)
        else:
            x = p1.x
        if p2.y > p1.y:
            y = p2.y + p2.y - p1.y
        elif p2.y < p1.y:
            y = p2.y - (p1.y - p2.y)
        else:
            y = p1.y
        return Point(x,y)
    
    def insideTreug(self,p1):
        l2 = self.fromCoord(0,0,p1.x,p1.y)
        p2 = self.intersection(l2)
        ly = self.fromCoord(0,0,0,1)
        lx = self.fromCoord(0,0,1,0)
        px = self.intersection(lx)
        py = self.intersection(ly)
        l = math.sqrt((p1.x)**2+(p1.y)**2)
        r = math.sqrt((p2.x)**2+(p2.y)**2)
        if p2.x == 0 and p2.y == 0: 
            return False
        elif (px.x > 0 and py.y > 0) and (p1.x >= 0 and p1.y >= 0) and (p2.x >= 0 and p2.y >= 0) and (l <= r):
            return True
        elif (px.x < 0 and py.y > 0) and (p1.x <= 0 and p1.y >= 0) and (p2.x <= 0 and p2.y >= 0) and (l <= r): 
            return True
        elif (px.x < 0 and py.y < 0) and (p1.x <= 0 and p1.y <= 0) and (p2.x <= 0 and p2.y <= 0) and (l <= r): 
            return True
        elif (px.x > 0 and py.y < 0) and (p1.x >= 0 and p1.y <= 0) and (p2.x >= 0 and p2.y <= 0) and (l <= r): 
            return True
        else:
            return l2



        
    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1-y2, x2-x1, x1*y2-x2*y1)

    def distanceToZero(self):
        if math.sqrt(self.A*self.A + self.B*self.B) == 0:
            return 0
        else:    
            return abs(self.C) / math.sqrt(self.A*self.A + self.B*self.B)    
    
    def distanceToPoint(self, Point):
        if math.sqrt(self.A*self.A + self.B*self.B) == 0:
            return 0
        else:    
            return abs(self.A*Point.x + self.B*Point.y + self.C) / math.sqrt(self.A*self.A + self.B*self.B)
    
