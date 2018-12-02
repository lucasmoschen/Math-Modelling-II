#Sistema Mola

#Constantes iniciais 

g = PVector(0.0,9.8) #aceleracao da gravidade
t = millis() #tempo inicial
dt = millis()/1000.0

#constantes em relação aos pesos e às molas

k1 = 6.0 #constante da mola superior 
k2 = 6.0 #contante da mola inferior
c1 = 60.0 #comprimento da mola 1
c2 = 60.0 #comprimento da mola 2
m1 = 5.0 #massa do peso 1
m2 = 5.0 #massa do peso 2
k = 0.0 #constante de retardo

quadrado = PVector(400.0,233.33) #posição inicial do quadrado 
tamq = 30.0 #tamanho do quadrado
tamc = 35.0 #diametro circunferencia

#vetores Peso
P1 = g.copy()
P1.mult(m1)
P2 = g.copy()
P2.mult(m2)

#vetores velocidade inicial
v1 = PVector(0.0,0.0)
v2 = PVector(0.0,0.0)

def setup():
    size(800,700) 
    frameRate(60)
    
entrada = 'noMouse'
    
def draw():
    background(0)
    textSize(32)
    fill(255)
    text("Sistema de duas molas",220,130)
    if mousePressed:
        global entrada
        entrada = 0 
        if mouseButton == LEFT:
            global r1
            r1 = PVector.sub(PVector(mouseX,mouseY),quadrado)
        elif mouseButton == RIGHT:
            global r2
            r2 = PVector.sub(PVector(mouseX,mouseY),quadrado)
    else:
        if entrada == 'noMouse':
            r1 = r1_inicial(g,m1,m2,k1,c1)
            r2 = r2_inicial(g,m2,k2,c2)
#calcula a deformação da mola 1
    d1 = r1.mag() - c1
#Força mola 1
    Fm1 = r1.copy()
    tamanho = Fm1.mag()
    Fm1.div(tamanho)
    Fm1.mult(-k1 * d1)
#calcula vetor r12
    r12 = PVector.sub(r2,r1)
#calcula a deformação da mola 2
    d2 =  r12.mag() - c2
    Fm2 = r12.copy()
    tamanho2 = Fm2.mag()
    Fm2.div(tamanho2)
    Fm2.mult(-k2*d2)
#calcula as forças de retardo
    global v1, v2
    Fr1 = v1.copy()
    Fr1.mult(-k)
    Fr2 = v2.copy()
    Fr2.mult(-k)
#calcula Forças resultantes
    F1 = P1.copy()
    F1.sub(Fm2)
    F1.add(Fm1)
    F1.add(Fr1)
    F2 = P2.copy()
    F2.add(Fm2)
    F2.add(Fr2)
#calcula as acelerações    
    a1 = F1.copy()
    a1.div(m1)
    a2 = F2.copy()
    a2.div(m2)
    
#Método de Euler
    global dt
    v1_0 = v1.copy()
    v1 = a1.copy()
    v1.mult(dt)
    v1.add(v1_0)
    
    v2_0 = v2.copy()
    v2 = a2.copy()
    v2.mult(dt)
    v2.add(v2_0)
    
    dr1 = v1.copy()
    dr1.mult(dt)
    dr2 = v2.copy()
    dr2.mult(dt)
    r1.add(dr1)
    r2.add(dr2)
    
    s1 = r1.copy()
    s1.add(quadrado)
    s2 = r2.copy()
    s2.add(quadrado)

#itera t
    global t
    dt = (millis() - t) / 1000.0
    t = millis()
    
#desenho do quadrado
    stroke(255)
    fill(200,0,0)
    rectMode(CENTER)
    rect(quadrado.x,quadrado.y,tamq,tamq)
    
#desenho de pesos e molas        
         
    stroke(128) #Cor cinza
    strokeWeight(4) #Maior espessura
    
    pedaco1 = r1.copy() #Vetor tamanho do pedaco
    pedaco1.div(10) #1/10 do tamanho da mola
    line(quadrado.x, quadrado.y, quadrado.x + pedaco1.x * 2, quadrado.y + pedaco1.y * 2) #Primeira linha
    line(s1.x - pedaco1.x * 2, s1.y - pedaco1.y * 2, s1.x, s1.y) #Última linha
    
    #Inicia com x e y anteriores
    x_anterior = quadrado.x + pedaco1.x * 2
    y_anterior = quadrado.y + pedaco1.y * 2
    
    i = 0    
    for pedaco in range(3, 8, 2):
        lado = PVector(-pedaco1.y, pedaco1.x)
        lado.div(lado.mag())
        lado.mult(15)
        line(x_anterior, y_anterior, quadrado.x + pedaco1.x * pedaco + lado.x * (-1)**i, quadrado.y + pedaco1.y * pedaco + lado.y * (-1)**i)
        x_anterior = quadrado.x + pedaco1.x * pedaco + lado.x * (-1)**i
        y_anterior = quadrado.y + pedaco1.y * pedaco + lado.y * (-1)**i
        i += 1
    
    line(x_anterior, y_anterior, s1.x - pedaco1.x * 2, s1.y - pedaco1.y * 2)
    
    pedaco2 = r12.copy() #Vetor tamanho do pedaco
    pedaco2.div(10) #1/10 do tamanho da mola
    line(s1.x, s1.y, s1.x + pedaco2.x * 2, s1.y + pedaco2.y * 2) #Primeira linha
    line(s2.x - pedaco2.x * 2, s2.y - pedaco2.y * 2, s2.x, s2.y) #Última linha
    
    #Inicia com x e y anteriores
    x_anterior = s1.x + pedaco2.x * 2
    y_anterior = s1.y + pedaco2.y * 2
    
    i = 0    
    for pedaco in range(3, 8, 2):
        lado = PVector(-pedaco2.y, pedaco2.x)
        lado.div(lado.mag())
        lado.mult(15)
        line(x_anterior, y_anterior, s1.x + pedaco2.x * pedaco + lado.x * (-1)**i, s1.y + pedaco2.y * pedaco + lado.y * (-1)**i)
        x_anterior = s1.x + pedaco2.x * pedaco + lado.x * (-1)**i
        y_anterior = s1.y + pedaco2.y * pedaco + lado.y * (-1)**i
        i += 1
    
    line(x_anterior, y_anterior, s2.x - pedaco2.x * 2, s2.y - pedaco2.y * 2)
    
    strokeWeight(1) #Espessura normal
    stroke(255)
    fill(128,128,0)
    ellipse(s1.x,s1.y,tamc,tamc)
    fill(0,128,128)
    ellipse(s2.x,s2.y,tamc,tamc)

#vetores posição inicial
def r1_inicial(g,m1,m2,k1,c1):
    r1 = g.copy()
    r1.mult((m1+m2)/k1)
    r1.add(PVector(0,c1))
    return r1
    
def r2_inicial(g,m2,k2,c2):
    r2 = g.copy()
    r2.mult(m2/k2+(m1+m2)/k1)
    r2.add(PVector(0,c2+c1))
    return r2

def collision_circles(s1,s2,tamc):
    if (s1-s2).mag() <= tamc:
        return True
    else:
        return False

def collision_quad(quadrado,tamq,tamc,vector):
    #compara nos primeiros 4 if e elifs com as retas e depois com a distância ao vértices
    #assim, ele basicamente compara com a curva de menor ditancia entre quadrado e centro do circulo 
    if (quadrado.x + tamq/2 + tamc/2) < vector.x: 
        return False
    elif (quadrado.x - tamq/2 - tamc/2) > vector.x:
        return False
    elif (quadrado.y + tamq/2 + tamc/2) < vector.y:
        return False
    elif (quadrado.y - tamq/2 - tamc/2)  > vector.y:
        return False
    elif dist(quadrado.x-tamq/2,quadrado.x-tamq/2, vector.x,vector.y) > tamc:
        return False
    elif dist(quadrado.x-tamq/2,quadrado.x+tamq/2, vector.x,vector.y) > tamc:
        return False 
    elif dist(quadrado.x+tamq/2,quadrado.x+tamq/2, vector.x,vector.y) > tamc:
        return False 
    elif dist(quadrado.x+tamq/2,quadrado.x-tamq/2, vector.x,vector.y) > tamc:
        return False
    else:
        return True
    
def keyPressed():
    global entrada
    entrada = 'noMouse'
    global v1,v2
    v1 = PVector(0.0,0.0)
    v2 = PVector(0.0,0.0)
