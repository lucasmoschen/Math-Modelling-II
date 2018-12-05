import random as ran
from comparing import Compare
from bola import Bolas
from collision import Collision 
from spring import Spring 
from masses import Masses

################ Sistema Mola ####################

################## Parte II ######################

#Constantes iniciais 

g = PVector(0.0,98.0) #aceleracao da gravidade
t = millis() #tempo inicial
dt = millis()/1000.0


largura,comprimento,p = 800,700,100.0 # tamanho de largura, comprimento e de duas paredes paralelas
e = 1 # tamanho espessura mola

#constantes em relação aos pesos e às molas

k1,k2 = 20.0,20.0 #constantes das molas superior e inferior 
c1,c2 = 60.0,60.0 #comprimento das molas
m1,m2 = 5.0,5.0 #massa do pesos
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

#Variáveis do cálculo da energia

t0 = millis() #tempo inicial do retardo na atualização da energia
inicio = True
epg = 0
ec = 0
epe = 0
et = 0

#Variáveis das bolas aleatórias
bola1,b1 = False,False ##ambas servem para uso específico
resb1_wall_ant = False
resb1_quad_ant = False
resb1_both_1_ant = False
resb1_both_2_ant = False
bola2,b2 = False,False ##ambas servem para uso específico
resb2_wall_ant = False
resb2_quad_ant = False
resb2_both_1_ant = False
resb2_both_2_ant = False
resb2_both_b1_ant = False
bola3,b3 = False,False ##ambas servem para uso específico
resb3_wall_ant = False
resb3_quad_ant = False
resb3_both_1_ant = False
resb3_both_2_ant = False
resb3_both_b1_ant = False
resb3_both_b2_ant = False

def setup():
    global masses, spring
    size(largura,comprimento) 
    frameRate(60)
    spring = Spring()
    masses = Masses(g, m1, m2, k1, k2, c1, c2, r, quadrado, dt, tamc, k)
    
entrada = 'noMouse'
    
def draw():
    global masses, spring, dt, t
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
            masses.r1 = PVector.sub(PVector(mouseX,mouseY),quadrado)
        elif mouseButton == RIGHT:
            masses.r2 = PVector.sub(PVector(mouseX,mouseY),quadrado)
    else:
        if entrada == 'noMouse':
            masses.__init__(g, m1, m2, k1, k2, c1, c2, r, quadrado, dt, tamc, k)
    
    masses.dt = dt
    s1, s2, v1, v2, r1, r12, r2, d1, d2 = masses.calculations()
    
    dt = (millis() - t) / 1000.0
    t = millis()
    
#desenho de pesos e molas     

    spring.draw_spring(r1, quadrado, s1)
    spring.draw_spring(r12, s1, s2)
    masses.draw_masses(e)    
        
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
    
    
    ### Mas o que acontece se colidir? 
    
    #Parede
    
    global res_wall_1_ant,res_wall_2_ant 
    if res_wall_1[0] and not res_wall_1_ant:
        colisao = Collision(m1,v1)
        masses.v1 = colisao.walls(res_wall_1)        
    if res_wall_2[0] and not res_wall_2_ant:
        colisao = Collision(m2,v2)
        masses.v2 = colisao.walls(res_wall_2)            
    res_wall_1_ant = res_wall_1[0]
    res_wall_2_ant = res_wall_2[0]
    
    #entre as massas
            
    global res_both_ant                        
    if res_both[0] and not res_both_ant:
        colisao = Collision(m1,v1)
        vels = colisao.circle(s1,s2,m2,v2,r)
        masses.v1 = vels[0]
        masses.v2 = vels[1]      
    res_both_ant = res_both[0]
    
    #quadrado
    
    global res_1_ant, res_2_ant
    
    if res_1[0] and not res_1_ant:
        colisao = Collision(m1,v1)
        masses.v1 = colisao.square(res_1,s1,quadrado,tamq)
    if res_2[0] and not res_2_ant:
        colisao = Collision(m2,v2)
        masses.v2 = colisao.square(res_2,s2,quadrado,tamq)        
    res_1_ant = res_1[0]
    res_2_ant = res_2[0]
    
################## Para brincar ####################

    if bola1:
        global b1, resb1_wall_ant,resb1_quad_ant,resb1_both_1_ant, resb1_both_2_ant
        if not b1:
            b1 = Bolas(largura,comprimento,tamc,p,g)
        b1.draw_balls(k,dt)
        
        resb1_wall = cmp.col_walls(largura,comprimento,p,tamc,b1.posb)
        if resb1_wall[0] and not resb1_wall_ant:
            colisao = Collision(b1.m,b1.vb)
            b1.vb = colisao.walls(resb1_wall)
        resb1_wall_ant = resb1_wall[0]
        
        resb1_quad = cmp.col_quad(quadrado,tamq,tamc,b1.posb)
        if resb1_quad[0] and not resb1_quad_ant:
            colisao = Collision(b1.m,b1.vb)
            b1.vb = colisao.square(resb1_quad,b1.posb,quadrado,tamq)
        resb1_quad_ant = resb1_quad[0]
        
        resb1_both_1 = cmp.col_circ(s1,b1.posb,tamc)
        if resb1_both_1[0] and not resb1_both_1_ant:
            colisao = Collision(b1.m,b1.vb)
            vels = colisao.circle(b1.posb,s1,m1,v1,r)
            b1.vb = vels[0]
            masses.v1 = vels[1]
        resb1_both_1_ant = resb1_both_1[0]
        
        resb1_both_2 = cmp.col_circ(s2,b1.posb,tamc)
        if resb1_both_2[0] and not resb1_both_2_ant:
            colisao = Collision(b1.m,b1.vb)
            vels = colisao.circle(b1.posb,s2,m2,v2,r)
            b1.vb = vels[0]
            masses.v2 = vels[1]
        resb1_both_2_ant = resb1_both_2[0]

    if bola2:
        global b2,resb2_wall_ant,resb2_quad_ant,resb2_both_1_ant, resb2_both_2_ant,resb2_both_b1_ant
        if not b2:
            b2 = Bolas(largura,comprimento,tamc,p,g)
        b2.draw_balls(k,dt)

        resb2_wall = cmp.col_walls(largura,comprimento,p,tamc,b2.posb)
        if resb2_wall[0] and not resb2_wall_ant:
            colisao = Collision(b2.m,b2.vb)
            b2.vb = colisao.walls(resb2_wall)
        resb2_wall_ant = resb2_wall[0]
        
        resb2_quad = cmp.col_quad(quadrado,tamq,tamc,b2.posb)
        if resb2_quad[0] and not resb2_quad_ant:
            colisao = Collision(b2.m,b2.vb)
            b2.vb = colisao.square(resb2_quad,b2.posb,quadrado,tamq)
        resb2_quad_ant = resb2_quad[0]
        
        resb2_both_1 = cmp.col_circ(s1,b2.posb,tamc)
        if resb2_both_1[0] and not resb2_both_1_ant:
            colisao = Collision(b2.m,b2.vb)
            vels = colisao.circle(b2.posb,s1,m1,v1,r)
            b2.vb = vels[0]
            masses.v1 = vels[1]
        resb2_both_1_ant = resb2_both_1[0]
        
        resb2_both_2 = cmp.col_circ(s2,b2.posb,tamc)
        if resb2_both_2[0] and not resb2_both_2_ant:
            colisao = Collision(b2.m,b2.vb)
            vels = colisao.circle(b2.posb,s2,m2,v2,r)
            b2.vb = vels[0]
            masses.v2 = vels[1]
        resb2_both_2_ant = resb2_both_2[0]

        resb2_both_b1 = cmp.col_circ(b1.posb,b2.posb,tamc)
        if resb2_both_b1[0] and not resb2_both_b1_ant:
            colisao = Collision(b2.m,b2.vb)
            vels = colisao.circle(b2.posb,b1.posb,b1.m,b1.vb,r)
            b2.vb = vels[0]
            b1.vb = vels[1]
        resb2_both_b1_ant = resb2_both_b1[0]

    if bola3:
        global b3,resb3_wall_ant,resb3_quad_ant,resb3_both_1_ant, resb3_both_2_ant,resb3_both_b1_ant, resb3_both_b2_ant
        if not b3:
            b3 = Bolas(largura,comprimento,tamc,p,g)
        b3.draw_balls(k,dt)
        
        resb3_wall = cmp.col_walls(largura,comprimento,p,tamc,b3.posb)
        if resb3_wall[0] and not resb3_wall_ant:
            colisao = Collision(b3.m,b3.vb)
            b3.vb = colisao.walls(resb3_wall)
        resb3_wall_ant = resb3_wall[0]
        
        resb3_quad = cmp.col_quad(quadrado,tamq,tamc,b3.posb)
        if resb3_quad[0] and not resb3_quad_ant:
            colisao = Collision(b3.m,b3.vb)
            b3.vb = colisao.square(resb3_quad,b3.posb,quadrado,tamq)
        resb3_quad_ant = resb3_quad[0]
        
        resb3_both_1 = cmp.col_circ(s1,b3.posb,tamc)
        if resb3_both_1[0] and not resb3_both_1_ant:
            colisao = Collision(b3.m,b3.vb)
            vels = colisao.circle(b3.posb,s1,m1,v1,r)
            b3.vb = vels[0]
            masses.v1 = vels[1]
        resb3_both_1_ant = resb3_both_1[0]
        
        resb3_both_2 = cmp.col_circ(s2,b3.posb,tamc)
        if resb3_both_2[0] and not resb3_both_2_ant:
            colisao = Collision(b3.m,b3.vb)
            vels = colisao.circle(b3.posb,s2,m2,v2,r)
            b3.vb = vels[0]
            masses.v2 = vels[1]
        resb3_both_2_ant = resb3_both_2[0]
        
        resb3_both_b1 = cmp.col_circ(b1.posb,b3.posb,tamc)
        if resb3_both_b1[0] and not resb3_both_b1_ant:
            colisao = Collision(b3.m,b3.vb)
            vels = colisao.circle(b3.posb,b1.posb,b1.m,b1.vb,r)
            b3.vb = vels[0]
            b1.vb = vels[1]
        resb3_both_b1_ant = resb3_both_b1[0]
        
        resb3_both_b2 = cmp.col_circ(b2.posb,b3.posb,tamc)
        if resb3_both_b2[0] and not resb3_both_b2_ant:
            colisao = Collision(b3.m,b3.vb)
            vels = colisao.circle(b3.posb,b2.posb,b2.m,b2.vb,r)
            b3.vb = vels[0]
            b2.vb = vels[1]
        resb3_both_b2_ant = resb3_both_b2[0]
        
##########################################
        
def keyPressed():
    if key == 'a' or key == 'A':
        global bola1
        bola1 = True
    elif key == 'b' or key == 'B':
        global bola2
        bola2 = True
    elif key == 'c' or key == 'C':
        global bola3
        bola3 = True
    else:
        global entrada
        entrada = 'noMouse'
        global r,bola1,bola2,bola3,b1,b2,b3
        r = ran.uniform(0.6,1) #coeficiente de restituição
        bola1,bola2,bola3,b1,b2,b3 = False,False,False,False,False,False
