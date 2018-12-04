import random as ran
from comparing import Compare
from bola import Bolas
from collision import Collision 

################ Sistema Mola ####################

################## Parte II ######################

#Constantes iniciais 

g = PVector(0.0,98.0) #aceleracao da gravidade
t = millis() #tempo inicial
dt = millis()/1000.0

e = 1.0 #esperssura da linha
largura = 800
comprimento = 700
p = 100.0 #tamanho de duas paredes paralelas

#constantes em relação aos pesos e às molas

k1 = 20.0 #constante da mola superior 
k2 = 20.0 #contante da mola inferior
c1 = 60.0 #comprimento da mola 1
c2 = 60.0 #comprimento da mola 2
m1 = 5.0 #massa do peso 1
m2 = 5.0 #massa do peso 2
k = 0.1 #constante de retardo
r = ran.uniform(0.6,1) #coeficiente de restituição

#resultados iniciais para comparação 

res_both_ant = False
res_wall_1_ant = False
res_wall_2_ant = False
res_1_ant = False
res_2_ant = False

quadrado = PVector(largura/2.0,comprimento/3.0) #posição inicial do quadrado 
tamq = 30.0 #tamanho do quadrado
tamc = 40.0 #diametro circunferencia

#vetores Peso
P1 = g.copy()
P1.mult(m1)
P2 = g.copy()
P2.mult(m2)

#vetores velocidade inicial
v1 = PVector(0.0,0.0)
v2 = PVector(0.0,0.0)

#Variáveis do cálculo da energia

t0 = millis() #tempo inicial do retardo na atualização da energia
inicio = True
epg = 0
ec = 0
epe = 0
et = 0

#Variáveis das bolas aleatórias
bola1,b1 = False,False ##ambas servem para uso específico
resb_wall_ant = False
resb_quad_ant = False

def setup():
    size(largura,comprimento) 
    frameRate(60)
    
entrada = 'noMouse'
    
def draw():
    background(255)
    fill(0)
    rect(400,350,largura - p,comprimento - p)
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
    
    strokeWeight(e) #Espessura normal
    stroke(255)
    fill(128,128,0)
    ellipse(s1.x,s1.y,tamc,tamc)
    fill(0,128,128)
    ellipse(s2.x,s2.y,tamc,tamc)
    
        
    #desenho do quadrado
    fill(200,0,0)
    rectMode(CENTER)
    rect(quadrado.x,quadrado.y,tamq,tamq)
    
############# TRABALHO 2 #################

############### ENERGIA ##################
    
    global t0, inicio, epg, ec, epe, et
    
    if inicio or millis() - t0 > 200:
        inicio = False
        epg1 = m1*g.mag()*(comprimento - s1.y - p/2)
        epg2 = m2*g.mag()*(comprimento - s2.y - p/2)
        epg = epg1 + epg2
        
        ec1 = 1.0/2.0*m1*(v1.mag())**2
        ec2 = 1.0/2.0*m2*(v2.mag())**2    
        ec = ec1 + ec2
        
        epe1 = 1.0/2.0*k1*d1**2
        epe2 = 1.0/2.0*k2*d2**2
        epe = epe1 + epe2
        
        et = epg + ec + epe
        
        t0 = millis()
        
    fill(255)
    text("Epg = {0:.2f} u.t.".format(epg/1000), p/2 + 10, comprimento - p/2 - 115)
    text("Ec = {0:.2f} u.t.".format(ec/1000), p/2 + 10, comprimento - p/2 - 80)
    text("Epe = {0:.2f} u.t.".format(epe/1000), p/2 + 10, comprimento - p/2 - 45)
    text("E = {0:.2f} u.t.".format(et/1000), p/2 + 10, comprimento - p/2 - 10)
    
##########################################

############## COLISÃO ###################

    cmp = Compare()
    res_1 = cmp.col_quad(quadrado,tamq,tamc,s1) #analisa se o quadrado se chocou com a massa 1
    res_2 = cmp.col_quad(quadrado,tamq,tamc,s2) #analisa se o quadrado se chocou com a massa 2
    res_both = cmp.col_circ(s1,s2,tamc)  #analisa se as massas se chocaram
    res_wall_1 = cmp.col_walls(largura,comprimento,p,tamc,s1)
    res_wall_2 = cmp.col_walls(largura,comprimento,p,tamc,s2)
    
    
    ###Mas o que acontece se colidir? 
    
    #Parede
    
    global res_wall_1_ant,res_wall_2_ant 
    if res_wall_1[0] and not res_wall_1_ant:
        colisao = Collision(m1,v1)
        v = colisao.walls(res_wall_1)        
    if res_wall_2[0] and not res_wall_2_ant:
        colisao = Collision(m2,v2)
        v2 = colisao.walls(res_wall_2)            
    res_wall_1_ant = res_wall_1[0]
    res_wall_2_ant = res_wall_2[0]
    
    #entre as massas
            
    global res_both_ant                        
    if res_both[0] and not res_both_ant:
        colisao = Collision(m1,v1)
        vels = colisao.circle(s1,s2,m2,v2,r)
        v1 = vels[0]
        v2 = vels[1]      
    res_both_ant = res_both[0]
    
    #quadrado
    
    global res_1_ant, res_2_ant
    
    if res_1[0] and not res_1_ant:
        colisao = Collision(m1,v1)
        v1 = colisao.square(res_1,s1,quadrado,tamq)
    if res_2[0] and not res_2_ant:
        colisao = Collision(m2,v2)
        v2 = colisao.square(res_2,s2,quadrado,tamq)        
    res_1_ant = res_1[0]
    res_2_ant = res_2[0]
    
################## Para brincar ####################

    if bola1:
        global b1,resb_wall_ant,resb_quad_ant
        if b1 == False:
            b1 = Bolas(largura,comprimento,tamc,p,g,dt)
        posb1 = b1.calculus_posicion(k)
        fill(50,60,90)
        ellipse(posb1.x,posb1.y,tamc,tamc)
        resb_wall = cmp.col_walls(largura,comprimento,p,tamc,posb1)
        if resb_wall[0] and not resb_wall_ant:
            colisao = Collision(b1.m,b1.vb)
            b1.vb = colisao.walls(resb_wall)
        resb_wall_ant = resb_wall[0]
        
        resb_quad = cmp.col_quad(quadrado,tamq,tamc,posb1)
        if resb_quad[0] and not resb_quad_ant:
            colisao = Collision(b1.m,b1.vb)
            b1.vb = colisao.square(resb_quad,posb1,quadrado,tamq)
        resb_quad_ant = resb_quad[0]
        
        resb_both_1 = cmp.col_circ(s1,posb1,tamc)
        if resb_b:
            pass
        
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
    if key == 'a' or key == 'A':
        global bola1
        bola1 = True
    else:
        global entrada
        entrada = 'noMouse'
        global v1,v2
        v1 = PVector(0.0,0.0)
        v2 = PVector(0.0,0.0)
        global r
        r = ran.uniform(0.5,1) #coeficiente de restituição
