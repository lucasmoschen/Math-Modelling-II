# coding: utf8

class Spring:
    
    def draw_spring(self, r, quadrado, s):
        stroke(128) #Cor cinza
        strokeWeight(4) #Maior espessura
        
        pedaco = r.copy() / 10 #Vetor tamanho do pedaco, 1/10 do tamanho da mola
        line(quadrado.x, quadrado.y, quadrado.x + pedaco.x * 2, quadrado.y + pedaco.y * 2) #Primeira linha
        line(s.x - pedaco.x * 2, s.y - pedaco.y * 2, s.x, s.y) #Última linha
        
        #Inicia com x e y anteriores
        x_anterior = quadrado.x + pedaco.x * 2
        y_anterior = quadrado.y + pedaco.y * 2
        
        i = 0    
        for j in range(3, 8, 2):
            lado = PVector(-pedaco.y, pedaco.x)
            lado = lado/lado.mag()*15
            line(x_anterior, y_anterior, quadrado.x + pedaco.x * j + lado.x * (-1)**i, quadrado.y + pedaco.y * j + lado.y * (-1)**i)
            x_anterior = quadrado.x + pedaco.x * j + lado.x * (-1)**i
            y_anterior = quadrado.y + pedaco.y * j + lado.y * (-1)**i
            i += 1
        
        line(x_anterior, y_anterior, s.x - pedaco.x * 2, s.y - pedaco.y * 2)
