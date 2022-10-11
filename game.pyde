def setup():
    fullScreen()
    background(255)
    
circle_y_pos = 500
circle_x_pos = 100
circle_y_vel = 0
circle_size = 50
score = 0
lose = False
start = False
line_speed = 11
line_1_1xpos = 1920
line_1_2xpos = 1920
line_1_1ypos = 270
line_1_2ypos = 800
line_r = 255 
line_g = 255
line_b = 0

def draw(): 
    global circle_y_pos, circle_x_pos, circle_y_vel, circle_size, score, lose, line_speed, line_1_1xpos, line_1_2xpos, line_1_1ypos, line_1_2ypos, line_r, line_g, line_b, start
    background(255)
    strokeWeight(2)
    stroke(0)
    fill(random(0,255),random(0,255),random(0,255))
    circle(circle_x_pos,circle_y_pos,circle_size)     #player
    
    if (keyPressed == True and key == ' ') and (lose == True):  #resets game if you lose, don't have to close and reopen
        circle_y_pos = 500
        circle_x_pos = 100
        circle_y_vel = 0
        circle_size = 50
        score = 0
        lose = False
        line_speed = 11
        line_1_1xpos = 1920
        line_1_2xpos = 1920
        line_1_1ypos = 270
        line_1_2ypos = 800
        line_r = 255 
        line_g = 255
        line_b = 0
        
    if (keyPressed == True and key == ' ') and (start == False):  #starts game
        start = True 
    
    if (circle_y_pos > 1055): #lose if touch bottom
        circle_y_pos = 1055
        circle_y_vel = 0
        lose = True
        
    if (circle_y_pos < 25): #lose if touch top
        circle_y_pos = 25
        circle_y_vel = 0
        lose = True
        
    if (circle_y_pos > line_1_1ypos) and (circle_y_pos < line_1_2ypos) and (line_1_1xpos > 75) and (line_1_1xpos < 125):  #touch line
        lose = True
        
            
    if (lose == True):
        text("you losed, press space to restart",870,540) #lose message
        
    if (start == False):
        text("welcome to No Touch Line Game, press space to bounce ball" + '\n' + "if you touch the lines or the top or bottom you fail, press space to start",200,400)  #start message
   
    textSize(50)
    text(score,190,61)
    fill(0)
    text("Score:",50,60) #score counter
    
    if (lose == False) and (start == True):
        line_1_1xpos -= line_speed #line move thing
        line_1_2xpos -= line_speed 
        line_speed += 0.01
        circle_y_vel += 0.7           #player falling 
        circle_y_pos += circle_y_vel
        if (keyPressed == True and key == ' '): #move player up
            circle_y_vel -= 5
            
            if(circle_y_vel < -10): #player speed limit
                circle_y_vel = -10
    
        strokeWeight(20) 
        stroke(line_r,line_g,line_b)
        line(line_1_1xpos, line_1_1ypos, line_1_2xpos, line_1_2ypos)
        
    if (line_1_1xpos < 0):  #sets line to the right side
        line_1_1xpos = 1920
        line_1_2xpos = 1920
        score += 1
        line_1_1ypos = random(0,540)
        line_1_2ypos = random(540,1080) #sets random line size
        if (line_1_1ypos < 250) and (line_1_2ypos > 850):
            line_1_1ypos += 150
        line_r = random(0,255) #sets random line colour
        line_g = random(0,255)
        line_b = random(0,255)
