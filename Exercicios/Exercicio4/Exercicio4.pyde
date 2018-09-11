def setup():
    size(800,600)
    background(0,0,128)
    t = millis()/1000.0

def draw():
    fill(200)
    ellipse(400,80,60,60)
    #strokeWeight(2)
    #stroke(128,0,0)
    for i in range(600):
        t = millis()/1000
        fill(128,128,0)
        rect(400,600 - 30*t,20,40)
        fill(128,0,0)
        triangle(400, 600 - 30*t, 420, 600 - 30*t, 410, 560 - 30*t)
        if 580 - 30*t < 110:
            fill(255,0,0)
            ellipse(400,100,120,120)
            break
        
        

        
        
        
        
    
    

    
