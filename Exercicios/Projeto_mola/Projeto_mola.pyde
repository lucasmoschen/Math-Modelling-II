#Sistema Mola

g = 10 #aceleracao da gravidade
k = 1 #constante da mola
x_quad = 375 #posicao inicial do retangulo
y_quad = 100
m = 30 #massa do objeto
x0 = 400 #posicao inicial circulo
y0 = 300

def setup():
    size(800,600)

def draw():
    global x_quad,y_quad,x0
    if mousePressed:
        background(0)
        fill(128,0,0)
        rect(x_quad,y_quad,50,50)
        fill(0,128,0)
        ellipse(x0,mouseY,50,50)
        line(x_quad+25,y_quad+25,x0,mouseY)
        y1 = mouseY
    t = millis()/1000.0
    if 
    y = (y1 - (g*m/k))*cos(((k/m)**(0.5))*t)
    background(0)
    fill(128,0,0)
    rect(x_quad,y_quad,50,50)
    fill(0,128,0)
    ellipse(x0,y,50,50)
    line(x_quad+25,y_quad+25,x0,y)

    

  
    

    
