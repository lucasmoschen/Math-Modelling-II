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
m1 = 0.5 #massa do peso 1
m2 = 0.5 #massa do peso 2

quadrado = PVector(400.0,233.33) #posição inicial do quadrado 
tamq = 20.0 #tamanho do quadrado

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
    global dt
    background(0)
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
    K1 = [0]*4
    K2 = [0]*4
    d1 = r1.mag() - c1
    p1 = PVector(0.0,0.0)
    p2 = PVector(0.0,0.0)
    for i in range(4):
    #Força mola 1
        Fm1 = r1.copy()
        tamanho = Fm1.mag()
        Fm1.div(tamanho)
        if i == 0:
            Fm1.mult(-k1 * d1)
        elif i == 1 or i ==2:
            Fm1.mult(-k1 * (d1+(K1[i-1]*dt/2).mag())*dt)
        elif i == 3:
            Fm1.mult(-k1 * (d1+(K1[2]*dt).mag())*dt)
    #calcula vetor r12
        r12 = PVector.sub(r2,r1)
    #calcula a deformação da mola 2
        d2 =  r12.mag() - c2
        Fm2 = r12.copy()
        tamanho2 = Fm2.mag()
        Fm2.div(tamanho2)
        if i == 0:
            Fm2.mult(-k2 * d2)
        elif i == 1 or i ==2:
            Fm2.mult(-k2 * (d2+(K2[i-1]*dt/2).mag())*dt)
        elif i == 3:
            Fm2.mult(-k2 * (d2+(K2[2]*dt).mag())*dt)
    #calcula Forças resultantes
        F1 = P1.copy()
        F1.sub(Fm2)
        F1.add(Fm1)
        F2 = P2.copy()
        F2.add(Fm2)
    #calcula as acelerações    
        a1 = F1.copy()
        a1.div(m1)
        a2 = F2.copy()
        a2.div(m2)
        K1[i] = a1.copy()
        K2[i] = a2.copy()
        p1.add(K1[i])
        p2.add(K2[i])
    
#Método de Euler
    global v1,v2

    v1_0 = v1.copy()
    v1 = p1.copy()
    v1.mult(dt/6)
    v1.add(v1_0)
    
    v2_0 = v2.copy()
    v2 = p2.copy()
    v2.mult(dt/6)
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
    
#desenho de pesos e molas
    stroke(0,200,0)
    line(quadrado.x,quadrado.y,s1.x,s1.y)
    stroke(0,0,200)
    line(s1.x,s1.y,s2.x,s2.y)
    stroke(255)
    fill(128,128,0)
    ellipse(s1.x,s1.y,tamq,tamq)
    fill(0,128,128)
    ellipse(s2.x,s2.y,tamq,tamq)
    fill(200,0,0)
    rectMode(CENTER)
    rect(quadrado.x,quadrado.y,tamq,tamq)

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

def keyPressed():
    global entrada
    entrada = 'noMouse'
    global v1,v2
    v1 = PVector(0.0,0.0)
    v2 = PVector(0.0,0.0)
