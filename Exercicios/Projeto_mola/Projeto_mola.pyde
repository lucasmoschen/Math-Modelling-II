#Sistema Mola

#Constantes iniciais 

g = 9.8 #aceleracao da gravidade
t = 0.0 #tempo inicial

k1 = 100.0 #constante da mola superior 
k2 = 100.0 #contante da mola inferior
c1 = 70.0 #comprimento da mola 1
c2 = 70.0 #comprimento da mola 2
m1 = 1.0 #massa do peso 1
m2 = 1.0 #massa do peso 2 

xq = 400
yq = 233.33
tamq = 20.0

#posicao de repouso

x0_1 = 400.0
y0_1 = (m1+m2)*g/k1 
x0_2 = 400.0
y0_2 = m2*g/k2 

def setup():
    size(800,700) #define tamanho da tela
    frameRate(60)
    
def draw():
#base, inalterável
    stroke(255) #define cor branca das linhas
    background(0) #a cada iteração, zera tudo
    fill(128,0,0)
    rectMode(CENTER)
    rect(xq,yq,tamq,tamq) # é base que sustenta
    
#cálculos
    global t #diz que t é global, para utilizar t = 0 como variavel local. 
    y1 = 0
    y2 = (y0_2 - m2*g/k2)*cos(((k2/m2)**(0.5))*t) + m2*g/k2 #itera y2.
    
#desenhos dos pesos e molas, alteráveis.
    fill(0,128,0) 
    ellipse(x0_1,y0_1 + c1 + yq + tamq,tamq,tamq) #desenha o peso 1
    fill(0,0,128)
    ellipse(x0_2,y2 + c2 + c1 + yq + tamq,tamq,tamq) #desenha o peso 2
    stroke(128,128,0)
    line(xq,yq,x0_1,y0_1 + c1 + yq + tamq) #desenha a mola 1
    stroke(0,128,128)
    line(x0_1,y0_1 + c1 + yq + tamq,x0_2,y2 + c2 + c1 + yq + tamq) #desenha a mola 2

#itera t
    t = t + 0.01

def mousePressed(): #se o mouse for pressionado
    if mouseButton == RIGHT:
        y0_1 = mouseY - (c1 + yq + tamq)
        global y0_1 
    elif mouseButton == LEFT:
        y0_2 = mouseY - (c2 + c1 + yq + tamq)
        global y0_2
    t = 0.0 #zera o cronometro
    global t #globaliza os valores
    loop()

def keyPressed():
    x0_1 = 400.0
    y0_1 = (m1+m2)*g/k1 
    x0_2 = 400.0
    y0_2 = m2*g/k2
    t = 0.0
    global x0_1,x0_2,y0_1,y0_2
    loop() #volta no draw, para ele ter loop


        


    

  
    

    
