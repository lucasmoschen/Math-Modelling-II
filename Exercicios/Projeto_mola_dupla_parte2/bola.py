# coding: utf8

class Bolas:

    def __init__(self,largura,comprimento,tamc,p,g,m1,dt):
        import random as ran
        self.posb = PVector(
            ran.uniform((p+tamc)/2,(largura-p/2-tamc/2)),
            ran.uniform((p+tamc)/2,(comprimento-p/2-tamc/2))
        )
        self.vb = PVector(ran.uniform(10,40),ran.uniform(10,40))
        self.peso = m1*g #calcula força peso da bola 1
        self.m1 = m1
        self.ab = 0
        self.dt = dt
    
    def calculus_aceleration(self,k):
        Frb = (-k)*self.vb #calcula força de retardo
        Fb = self.peso + Frb #calcula força resultante
        ab = (1/self.m1)*Fb
        return ab
    
    def metodo_euler(self,vb,ab):
        vb_0 = vb.copy()
        vb = ab.copy()
        vb.mult(self.dt)
        vb.add(vb_0)       
        drb = vb.copy()
        drb.mult(self.dt)
        self.posb.add(drb)
        return self.posb
        
    def calculus_posicion(self,k):
        self.ab = self.calculus_aceleration(k)
        self.posb = self.metodo_euler(self.vb,self.ab)
        return self.posb
            
    
        
