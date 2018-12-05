# coding: utf8

class Masses:
    
    def __init__(self, g, m1, m2, k1, k2, c1, c2, r, quadrado, dt, tamc, k):
        self.v1 = PVector(0.0, 0.0)
        self.v2 = PVector(0.0, 0.0)
        self.g = g
        self.m1 = m1
        self.m2 = m2
        self.P1 = g.copy()
        self.P1.mult(m1)
        self.P2 = g.copy()
        self.P2.mult(m2)
        self.k1 = k1
        self.k2 = k2
        self.c1 = c1
        self.c2 = c1
        self.r = r
        self.quadrado = quadrado
        self.dt = dt
        self.tamc = tamc
        self.k = k
                
        self.r1 = g*(m1 + m2)/k1 + PVector(0,c1)        
        self.r2 = g*(m2/k2 + (m1 + m2)/k1) + PVector(0,c2+c1)
        
    def calculations(self):
        d1 = self.r1.mag() - self.c1
    #Força mola 1
        Fm1 = self.r1.copy()
        tamanho = Fm1.mag()
        Fm1.div(tamanho)
        Fm1.mult(-self.k1 * d1)
    #calcula vetor r12
        r12 = PVector.sub(self.r2,self.r1)
    #calcula a deformação da mola 2
        d2 =  r12.mag() - self.c2
        Fm2 = r12.copy()
        tamanho2 = Fm2.mag()
        Fm2.div(tamanho2)
        Fm2.mult(-self.k2*d2)
    #calcula as forças de retardo
        Fr1 = self.v1.copy()
        Fr1.mult(-self.k)
        Fr2 = self.v2.copy()
        Fr2.mult(-self.k)
    #calcula Forças resultantes
        F1 = self.P1.copy()
        F1.sub(Fm2)
        F1.add(Fm1)
        F1.add(Fr1)
        F2 = self.P2.copy()
        F2.add(Fm2)
        F2.add(Fr2)
    #calcula as acelerações    
        a1 = F1.copy()
        a1.div(self.m1)
        a2 = F2.copy()
        a2.div(self.m2)
        
        self.euler(a1, a2)
        
        return self.s1, self.s2, self.v1, self.v2, self.r1, r12, self.r2, d1, d2
                
    def euler(self, a1, a2):        
        v1_0 = self.v1.copy()
        self.v1 = a1.copy()
        self.v1.mult(self.dt)
        self.v1.add(v1_0)
        
        v2_0 = self.v2.copy()
        self.v2 = a2.copy()
        self.v2.mult(self.dt)
        self.v2.add(v2_0)
        
        dr1 = self.v1.copy()
        dr1.mult(self.dt)
        dr2 = self.v2.copy()
        dr2.mult(self.dt)
        self.r1.add(dr1)
        self.r2.add(dr2)
        
        self.s1 = self.r1.copy()
        self.s1.add(self.quadrado)
        self.s2 = self.r2.copy()
        self.s2.add(self.quadrado)
        
    def draw_masses(self, e):
        strokeWeight(e)
        stroke(255)
        fill(128, 128, 0)
        ellipse(self.s1.x, self.s1.y, self.tamc, self.tamc)
        fill(0, 128, 128)
        ellipse(self.s2.x, self.s2.y, self.tamc, self.tamc)
