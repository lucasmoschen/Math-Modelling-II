g = 9.8 #aceleração da gravidade
vt = 20.0 #velocidade inicial
#oldt = millis()/1000.0

def setup():
    size(600,600)

def draw():
    global g,vt,oldt
    t = millis()/1000.0
    #dt = t - oldt
    #oldt = t

    y = vt*t - 1/2*g*(t**2)
        
    background(255)
    stroke(0)
    fill(0)
    ellipse(300,600 - y,20, 20)
