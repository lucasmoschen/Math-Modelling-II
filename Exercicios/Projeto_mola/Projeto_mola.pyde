#Sistema Mola

#Constantes iniciais 

g = 9.8 #aceleracao da gravidade
t = millis() #tempo inicial

k1 = 10.0 #constante da mola superior 
k2 = 10.0 #contante da mola inferior
c1 = 70.0 #comprimento da mola 1
c2 = 70.0 #comprimento da mola 2
m1 = 1.0 #massa do peso 1
m2 = 1.0 #massa do peso 2 

xq = 400 #posição inicial do quadrado 
yq = 233.33
tamq = 20.0 #tamanho do quadrado

#posicao de repouso

x0_1 = 0.0
y0_1 = (m1+m2)*g/k1 
x0_2 = 0.0
y0_2 = m2*g/k2

def setup():
    size(800,700) #define tamanho da tela
    frameRate(60)
    noLoop()
    
def draw():
#base, inalterável
    stroke(255) #define cor branca das linhas
    background(0) #a cada iteração, zera tudo
    fill(128,0,0)
    rectMode(CENTER)
    rect(xq,yq,tamq,tamq) # é base que sustenta
 
    
#itera t
    global t
    t = (millis() - t) / 1000.0

    
#cálculos
    global y1, y2
    
    y2 = (y0_2 - m2*g/k2)*cos(((k2/m2)**(0.5))*t) + m2*g/k2 #itera y2.
    y1 = (y0_1 - (m1 + m2) * g / k1) * cos((k2 / m2)**0.5 * t) + k2/k1*y2 + g*m1/k1 #itera y1

        
    
#desenhos dos pesos e molas, alteráveis.
    fill(0,128,0) 
    ellipse(x0_1 + xq,y1 + c1 + yq,tamq,tamq) #desenha o peso 1
    fill(0,0,128)
    ellipse(x0_2 + xq, y2 + c2 + y1 + c1 + yq,tamq,tamq) #desenha o peso 2
    stroke(128,128,0)
    line(xq,yq,x0_1 + xq, y1 + c1 + yq) #desenha a mola 1
    stroke(0,128,128)
    line(x0_1 + xq,y1 + c1 + yq,x0_2 + xq,y1 + y2 + c2 + c1 + yq) #desenha a mola 2


def mousePressed(): #se o mouse for pressionado
    if mouseButton == RIGHT:
        y0_1 = mouseY - (c1 + yq)
        global y0_1 
    elif mouseButton == LEFT:
        y0_2 = mouseY - (c2 + c1 + yq + y1)
        global y0_2
    global t #globaliza os valores
    t = millis() #zera o cronometro

def keyPressed():
    global x0_1,x0_2,y0_1,y0_2
    x0_1 = 0.0
    y0_1 = (m1+m2)*g/k1 
    x0_2 = 0.0
    y0_2 = m2*g/k2
    t = millis()


        


    

  
    

    
