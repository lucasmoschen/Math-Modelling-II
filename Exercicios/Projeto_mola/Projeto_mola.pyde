#Sistema Mola

g = 10.0 #aceleracao da gravidade
k = 1.0 #constante da mola
x_quad = 375 #posicao inicial do retangulo
y_quad = 100
m = 30.0 #massa do peso
x0 = 400 #posicao inicial do peso
y0 = 300 #posicao inicial do peso, y0 = g*m/k 
t = 0.0 #tempo inicial

def setup():
    size(800,1200) #define tamanho da tela
    background(0) #define cor preta como fundo
    stroke(255) #define cor branca das linhas
    
def draw():
    background(0) #a cada iteração, zera tudo
    global x_quad,y_quad,x0,g,m,k #prga os valores a cima
    global t #diz que t é global
    t = t + 0.5 #itera t
    y = (y0 - (g*m/k))*cos(((k/m)**(0.5))*t) + 300 #itera y. O 300 é o y0 inicial
    fill(128,0,0) 
    rect(x_quad,y_quad,50,50) # é base que sustenta
    fill(0,128,0) 
    ellipse(x0,y,50,50) #desenha o peso
    line(x_quad+25,y_quad+25,x0,y) #deseha a mola

def mousePressed(): #se o mouse for pressionado
    y0 = mouseY #posição Y do mouse
    t = 0.0 #zera o cronometro
    global y0,t #globaliza os valores
    loop()

def keyPressed():
    y0 = 300 #volta ao valor inicial caso alguma tecla seja clicada
    t = 0.0
    global y0,t
    loop() #volta no draw, para ele ter loop


        


    

  
    

    
