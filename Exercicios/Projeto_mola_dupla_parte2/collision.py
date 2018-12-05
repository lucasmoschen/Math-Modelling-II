# coding: utf8

    ###Mas o que acontece se colidir? 
    
    #Parede
    
class Collision:
    
    def __init__(self,m,v):
        self.m = m
        self.v = v

    def walls(self,res_wall): 
        if res_wall[1] == 1:   
            self.v.y = abs(self.v.y)
        elif res_wall[1] == 2:
            self.v.x = abs(self.v.x)*(-1)
        elif res_wall[1] == 3:
            self.v.y = abs(self.v.y)*(-1)
        elif res_wall[1] == 4:
            self.v.x = abs(self.v.x)    
            
        return self.v
    
    def circle(self,s1,s2,m2,v2,r):
        v_cm = (self.m*self.v + m2*v2)/(self.m+m2)
        u = s2 - s1
        v1_cm = self.v - v_cm   
        v2_cm = v2 - v_cm    
        # if s1.x < s2.x:
        #     if v1_cm.x > 0 or v2_cm.x < 0:
        #         collision = True
        #     else:
        #         collision = False
        # elif s1.x > s2.x:
        #     if v1_cm.x < 0 or v2_cm.x > 0:
        #         collision = True
        #     else:
        #         collision = False 
        # elif s1.y < s2.y:
        #     if v1_cm.y > 0 or v2_cm.y < 0:
        #         collision = True
        #     else:
        #         collision = False
        # elif s1.y > s2.y:
        #     if v1_cm.y < 0 or v2_cm.y > 0:
        #         collision = True
        #     else:
        #         collision = False
        # if collision:
        proj_v1_cm_u = (v1_cm.dot(u) / u.mag()**2) * u
        proj_v2_cm_u = (v2_cm.dot(u) / u.mag()**2) * u
        v1_cm = r*(v1_cm - 2*proj_v1_cm_u)
        v2_cm = r*(v2_cm - 2*proj_v2_cm_u)
        self.v = v1_cm + v_cm
        v2 = v2_cm + v_cm
        return [self.v,v2]
    
    def square(self,res,pos,quadrado,tamq):
        if res[1] == 1: 
            self.v.y = abs(self.v.y)*(-1)
        elif res[1] == 2:
            self.v.x = abs(self.v.x)
        elif res[1] == 3:
            self.v.y = abs(self.v.y)
        elif res[1] == 4:
            self.v.x = abs(self.v.x)*(-1) 
        else:
            if res[1] == 5:
                u = pos - PVector(quadrado.x + tamq/2, quadrado.y - tamq/2)
            elif res[1] == 6:
                u = pos - PVector(quadrado.x + tamq/2, quadrado.y + tamq/2)
            elif res[1] == 7:
                u = pos - PVector(quadrado.x - tamq/2, quadrado.y + tamq/2)
            else:
                u = pos - PVector(quadrado.x - tamq/2, quadrado.y - tamq/2)
            proj_v1_u = (self.v.dot(u) / u.mag()**2) * u
            self.v = self.v - 2*proj_v1_u
        return self.v
