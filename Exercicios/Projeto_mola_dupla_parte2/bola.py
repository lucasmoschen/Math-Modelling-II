# coding: utf8

import random as ran

class Bolas:
    
    def __init__(self,largura,comprimento,tamc,p,g):
        self.tamc = tamc
        self.posb = PVector(
            ran.uniform((p+self.tamc)/2,(largura-p/2-self.tamc/2)),
            ran.uniform((p+self.tamc)/2,(comprimento-p/2-self.tamc/2))
        )
        self.vb = PVector(ran.uniform(300,400),ran.uniform(300,400))
        self.m = ran.uniform(5,15)
        self.g = g
        self.peso = self.m*self.g #calcula força peso da bola 1
        self.ab = 0
        self.epg = 0
        self.ec = 0
        
    def energy(self,p):
        self.epg = self.m*self.g.mag()*(700-self.posb.y-p/2)
        self.ec = 1.0/2.0*self.m*(self.vb.mag())**2
        
    
    def calculus_aceleration(self,k):
        Frb = (-k)*self.vb #calcula força de retardo
        Fb = self.peso + Frb #calcula força resultante
        ab = (1/self.m)*Fb
        return ab
    
    def metodo_euler(self,vb,ab,dt):
        vb_0 = self.vb.copy()
        self.vb = ab.copy()
        self.vb.mult(dt)
        self.vb.add(vb_0)       
        drb = self.vb.copy()
        drb.mult(dt)
        self.posb.add(drb)
        return self.posb
        
    def calculus_posicion(self,k,dt):
        self.ab = self.calculus_aceleration(k)
        self.posb = self.metodo_euler(self.vb,self.ab,dt)
        return self.posb
    
    def draw_balls(self,k,dt):
        self.posb = self.calculus_posicion(k,dt)
        fill(50,60,90)
        ellipse(self.posb.x,self.posb.y,self.tamc,self.tamc)
        
            
    
        
