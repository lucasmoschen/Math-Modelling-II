#Sistema Mola

g = 10.0 #aceleracao da gravidade
k = 1.0 #constante da mola
x_quad = 375 #posicao inicial do retangulo
y_quad = 100
m = 30.0 #massa do objeto
x0 = 400 #posicao inicial circulo
y0 = 300
t = 0.0
keyvalue = 0

def setup():
    size(800,1200)
    background(0)
    stroke(255)
    
def draw():
    background(0)
    global x_quad,y_quad,x0,g,m,k
    global t
    t = t + 0.1
    y = (y0 - (g*m/k))*cos(((k/m)**(0.5))*t) + 300
    fill(128,0,0)
    rect(x_quad,y_quad,50,50)
    fill(0,128,0)
    ellipse(x0,y,50,50)
    line(x_quad+25,y_quad+25,x0,y)

def mousePressed():
    y0 = mouseY
    t = 0.0
    global y0,t
    loop()

def keyPressed():
    if keyvalue == 0:
        y0 = 300
        t = 0.0
        global y0,t
        redraw()


        


    

  
    

    
