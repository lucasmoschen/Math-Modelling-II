def setup():
    size(800,600)

def draw():
    background(200,200,255,50)
    fill(200,200,0)
    ellipse(400,300,40,40)
    t = millis()/10000.0
    x = 200*cos(t) + 400
    y = 200*sin(t) + 300
    fill(0,0,100)
    ellipse(x,y,20,20)
