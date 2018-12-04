# coding: utf8

class Compare:
    
    def __init__(self):
        pass
    
    def col_circ(self,s1,s2,tamc):
        if (s1-s2).mag() <= tamc:
            return [True]
        else:
            return [False]
    
    def col_quad(self,quadrado,tamq,tamc,circle):
        #compara nos primeiros 4 if e elifs com as retas e depois com a distância ao vértices
        #assim, ele basicamente compara com a curva de menor ditancia entre quadrado e centro do circulo 
        if (quadrado.y - tamq/2 - tamc/2)  > circle.y:
            return [False]
        elif (quadrado.x + tamq/2 + tamc/2) < circle.x:
            return [False]
        elif (quadrado.y + tamq/2 + tamc/2) < circle.y:
            return [False]
        elif (quadrado.x - tamq/2 - tamc/2) > circle.x:
            return [False]
        elif circle.x <= quadrado.x-tamq/2 and circle.y <= quadrado.y-tamq/2 and dist(quadrado.x-tamq/2 ,quadrado.y-tamq/2, circle.x,circle.y) > tamc/2:
            return [False]
        elif circle.x <= quadrado.x-tamq/2 and circle.y >= quadrado.y+tamq/2 and dist(quadrado.x-tamq/2 ,quadrado.y+tamq/2, circle.x,circle.y) > tamc/2:
            return [False] 
        elif circle.x >= quadrado.x+tamq/2 and circle.y >= quadrado.y+tamq/2 and dist(quadrado.x+tamq/2 ,quadrado.y+tamq/2, circle.x,circle.y) > tamc/2:
            return [False]
        elif circle.x >= quadrado.x+tamq/2 and circle.y <= quadrado.y-tamq/2 and dist(quadrado.x+tamq/2 ,quadrado.y-tamq/2, circle.x,circle.y) > tamc/2:
            return [False]
        else:
            if circle.x >= quadrado.x - tamq/2 and circle.x <= quadrado.x + tamq/2:
                if circle.y > quadrado.y:
                    area = 3
                else:
                    area = 1
            elif circle.y >= quadrado.y - tamq/2 and circle.y <= quadrado.y + tamq/2:
                if circle.x > quadrado.x:
                    area = 2
                else:
                    area = 4
            else:
                if circle.x > quadrado.x:
                    if circle.y < quadrado.y:
                        area = 5
                    else:
                        area = 6
                else:
                    if circle.y < quadrado.y:
                        area = 8
                    else:
                        area = 7                
            return [True, area]
        
    def walls(self,largura,comprimento,p,tamc,circle):
        if p/2 + tamc/2 >= circle.y:
            return [True, 1]
        elif largura - p/2 - tamc/2 <= circle.x:
            return [True, 2]
        elif comprimento - p/2 - tamc/2 <= circle.y:
            return [True, 3]
        elif p/2 + tamc/2 >= circle.x:
            return [True, 4]
        else:
            return [False]
