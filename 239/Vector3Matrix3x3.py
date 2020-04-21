# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:22:19 2020

@author: Nikita
"""

import math
class Vector3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '({:.2f}, {:.2f}, {:.2f})'.format(self.x,self.y,self.z)
    def len(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    def norm(self):
        if self.x == self.y == self.z == 0:
            return Vector3(0,0,0)
        else:
            d = math.sqrt(self.x**2+self.y**2+self.z**2)
            return Vector3(self.x/d,self.y/d,self.z/d)
    def xR(self,R):
        return Vector3(self.x*R,self.y*R,self.z*R)
    def plusV(self,v2):
        return Vector3(self.x+v2.x,self.y+v2.y,self.z+v2.z)
    def minusV(self,v2):
        return Vector3(self.x-v2.x,self.y-v2.y,self.z-v2.z)
    def dotV(self,v2):
        return self.x*v2.x+self.y*v2.y+self.z*v2.z
    def xV(self,v2):
        x = self.y*v2.z-v2.y*self.z
        y = self.x*v2.z-v2.x*self.z
        z = self.x*v2.y-v2.x*self.y
        return Vector3(x,-y,z)
    
class Matrix3x3:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return '({},\n {},\n {})'.format(self.a,self.b,self.c)   
    def I():
        return Matrix3x3(Vector3(1,0,0),Vector3(0,1,0),Vector3(0,0,1))  
    def xR(self,R):
        return Matrix3x3(self.a.xR(R),self.b.xR(R),self.c.xR(R))
    def plusM(self,M):
        return Matrix3x3(self.a.plusV(M.a),self.b.plusV(M.b),self.c.plusV(M.c))
    def minusM(self,M):
        return Matrix3x3(self.a.minusV(M.a),self.b.minusV(M.b),self.c.minusV(M.c))
    def xV(self,v):
        return Vector3(self.a.dotV(v),self.b.dotV(v),self.c.dotV(v))
    def xM(self,M):
        return Matrix3x3(Vector3(self.a.dotV(Vector3(M.a.x,M.b.x,M.c.x)),self.a.dotV(Vector3(M.a.y,M.b.y,M.c.y)),self.a.dotV(Vector3(M.a.z,M.b.z,M.c.z))),\
                         Vector3(self.b.dotV(Vector3(M.a.x,M.b.x,M.c.x)),self.b.dotV(Vector3(M.a.y,M.b.y,M.c.y)),self.b.dotV(Vector3(M.a.z,M.b.z,M.c.z))),\
                         Vector3(self.c.dotV(Vector3(M.a.x,M.b.x,M.c.x)),self.c.dotV(Vector3(M.a.y,M.b.y,M.c.y)),self.c.dotV(Vector3(M.a.z,M.b.z,M.c.z))))
    def MRot(v,fi):
        S = Matrix3x3(Vector3(0,v.z,-v.y),Vector3(-v.z,0,v.x),Vector3(v.y,-v.x,0)) 
        t1 = S.xR(math.sin(fi)) 
        I = Matrix3x3.I()
        l = t1.plusM(I)
        S2 = S.xM(S) 
        fi2 = 1 - math.cos(fi)
        r = S2.xR(fi2)
        return l.plusM(r)
        