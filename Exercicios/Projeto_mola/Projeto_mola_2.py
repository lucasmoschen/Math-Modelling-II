#Sistema Mola

#Constantes iniciais 

g = PVector(0,9.8) #aceleracao da gravidade
t = millis() #tempo inicial

k1 = 10.0 #constante da mola superior 
k2 = 10.0 #contante da mola inferior
c1 = 70.0 #comprimento da mola 1
c2 = 70.0 #comprimento da mola 2
m1 = 1.0 #massa do peso 1
m2 = 1.0 #massa do peso 2 

quadrado = PVector(400,233.33) #posição inicial do quadrado 
tamq = 20.0 #tamanho do quadrado

def setup():
    size(800,700)
    frameRate(60)
    
def draw():
    background(0)
    stroke(255)
    fill(128,0,0)
    rectMode(CENTER)
    quad(quadrado.x,quadrado.y,tamq)
