import turtle
import sys
import time
import mysql.connector 
from CSVfunc import *
from SQLfunc import *
from loadingscreen import *
splash_screen(6)

print("RULES OF THE GAME:")
print("1.LOCAL PLAY RULES:")
print("USE W AND S KEYS TO MOVE THE PADDLE ON YOUR LEFT AND UP AND DOWN KEYS FOR THE PADDLE ON YOUR LEFT.","THE FIRST TO SCORE 10 WINS.",sep='\n')
print("2.RULES FOR ENDLESS MODE:")
print("USE UP AND DOWN KEYS TO MOVE YOUR PADDLE.","DONT WORRY,THE OTHER ONE WORKS ON IT OWN.","YOU WILL BE SCORED ON HOW MUCH TIME IT TOOK FOR THE PLAYER TO LOSE 5 POINTS.",sep='\n')
print("THE POINT OF THIS GAME IS NOT TO WIN BUT TO SURVIVE THE LONGEST.")
DBinit()
CREATE()

user_name = input("Enter player name :")
leader_input = int(input("Do you wish to see the current leaderboard?1/0:"))
if leader_input == 1:
    LEADERBOARD()
    input_user=int(input("Enter 1 for LOCAL PLAYERS , Enter 2 for SURVIVAL MODE: "))


    if input_user==1 :
        wn = turtle.Screen()
        wn.title("Pong")
        wn.bgcolor("blue")
        wn.setup(width=800, height=600)
        wn.tracer(0)


        #scorekeeping
        score_a=0
        score_b=0


        #paddle A
        paddle_a=turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("red")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350,0)



        #paddle b
        paddle_b=turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("red")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350,0)



        #ball
        ball=turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("black")
        ball.penup()
        ball.goto(0,0)
        ball.dx = 0.33
        ball.dy = 0.33

        #for scoring
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,260)
        pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24,"normal"))




        def paddle_a_up():
            y = paddle_a.ycor()
            y+=40
            paddle_a.sety(y)

        wn.listen()
        wn.onkeypress(paddle_a_up, "w")

        def paddle_a_down():
            y = paddle_a.ycor()
            y-=40
            paddle_a.sety(y)

        wn.listen()
        wn.onkeypress(paddle_a_down, "s")


        def paddle_b_up():
            y = paddle_b.ycor()
            y+=40
            paddle_b.sety(y)

        wn.listen()
        wn.onkeypress(paddle_b_up, "Up")

        def paddle_b_down():
            y = paddle_b.ycor()
            y-=40
            paddle_b.sety(y)

        wn.listen()
        wn.onkeypress(paddle_b_down, "Down")

        #Main game loop
        while True:
            wn.update()
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
            

            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy*=-1


            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy*=-1

            if ball.xcor() > 390:
                ball.goto(0,0)
                ball.dx*=-1
                score_a+=1
                pen.clear()
                pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24,"normal"))

            if ball.xcor() < -390:
                ball.goto(0,0)
                ball.dx*=-1
                score_b+=1
                pen.clear()
                pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24,"normal"))

            #for collision ball and paddle
            if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
                ball.setx(340)
                ball.dx *=-1    
            
            if ball.xcor() <-340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
                ball.setx(-340)
                ball.dx *=-1    
            
            if score_a == 10:
                
                congr=turtle.Turtle()
                congr.speed(0)
                congr.color("white")
                congr.penup()
                congr.hideturtle()
                congr.goto(0,0)
                congr.write("PLAYER A WINS", align="center", font=("Courier", 28,"bold"))
                sys.exit("Player A wins")

            if score_b == 10:
                
                congr=turtle.Turtle()
                congr.speed(0)
                congr.color("white")
                congr.penup()
                congr.hideturtle()
                congr.goto(0,0)
                congr.write("PLAYER B WINS", align="center", font=("Courier", 28,"bold"))
                sys.exit("Player B wins")


    if input_user==2 :
        init()
        #survival mode code
        start_time = time.time()#for scoring in this


        wn = turtle.Screen()
        wn.title("Pong")
        wn.bgcolor("blue")
        wn.setup(width=800, height=600)
        wn.tracer(0)


        #for keeping track of points of computer
        score_a=0
        


        #paddle A
        paddle_a=turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("red")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350,0)



        #paddle b
        paddle_b=turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("red")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350,0)



        #ball
        ball=turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("black")
        ball.penup()
        ball.goto(0,0)
        ball.dx = 0.36
        ball.dy = 0.36

        #for scoring
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,260)
        pen.write("POINTS LOST: 0", align="center", font=("Courier", 24,"normal"))

      

        def paddle_b_up():
            y = paddle_b.ycor()
            y+=40
            paddle_b.sety(y)

        wn.listen()
        wn.onkeypress(paddle_b_up, "Up")

        def paddle_b_down():
            y = paddle_b.ycor()
            y-=40
            paddle_b.sety(y)

        wn.listen()
        wn.onkeypress(paddle_b_down, "Down")

        def speed_up():
            if elapsed_time%5==0:
                ball.dx+=0.3
                ball.dy+=0.3

      
        #Main game loop
        while True:
            wn.update()
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
            paddle_a.sety(ball.ycor())
            
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy*=-1


            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy*=-1

            if ball.xcor() > 390:
                ball.goto(0,0)
                ball.dx*=-1
                score_a+=1
                pen.clear()
                pen.write("POINTS LOST: {}".format(score_a), align="center", font=("Courier", 24,"normal"))

            if ball.xcor() < -390:
                ball.goto(0,0)
                ball.dx*=-1
                score_b+=1
                pen.clear()
                pen.write("POINTS LOST: {}".format(score_a), align="center", font=("Courier", 24,"normal"))

            #for collision ball and paddle
            if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
                ball.setx(340)
                ball.dx *=-1    
            
            if ball.xcor() <-340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
                ball.setx(-340)
                ball.dx *=-1    
            
              #for calculating score in endless mode using time

            elapsed_time = time.time() - start_time 

            score = int(elapsed_time)#FOR DETERMINING HIGHSCORE(NEEDED)
        
            if score_a==5: # game end
                something(score)
                WRITE_SCORE(user_name,score)
                time=turtle.Turtle()
                time.speed(0)
                time.color("white")
                time.penup()
                time.hideturtle()
                time.goto(0,-260)
                time.write( "SCORE ACHIEVED: {} HIGHSCORE: {}".format( int(elapsed_time), getHighScore()) , align="center", font=("Courier", 20,"normal"))
                sys.exit()




            

else:
    input_user=int(input("Enter 1 for LOCAL PLAYERS , Enter 2 for SURVIVAL MODE: "))


    if input_user==1 :
        wn = turtle.Screen()
        wn.title("Pong")
        wn.bgcolor("blue")
        wn.setup(width=800, height=600)
        wn.tracer(0)


        #scorekeeping
        score_a=0
        score_b=0


        #paddle A
        paddle_a=turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("red")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350,0)



        #paddle b
        paddle_b=turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("red")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350,0)



        #ball
        ball=turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("black")
        ball.penup()
        ball.goto(0,0)
        ball.dx = 0.33
        ball.dy = 0.33

        #for scoring
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,260)
        pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24,"normal"))




        def paddle_a_up():
            y = paddle_a.ycor()
            y+=40
            paddle_a.sety(y)

        wn.listen()
        wn.onkeypress(paddle_a_up, "w")

        def paddle_a_down():
            y = paddle_a.ycor()
            y-=40
            paddle_a.sety(y)

        wn.listen()
        wn.onkeypress(paddle_a_down, "s")


        def paddle_b_up():
            y = paddle_b.ycor()
            y+=40
            paddle_b.sety(y)

        wn.listen()
        wn.onkeypress(paddle_b_up, "Up")

        def paddle_b_down():
            y = paddle_b.ycor()
            y-=40
            paddle_b.sety(y)

        wn.listen()
        wn.onkeypress(paddle_b_down, "Down")

        #Main game loop
        while True:
            wn.update()
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
            

            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy*=-1


            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy*=-1

            if ball.xcor() > 390:
                ball.goto(0,0)
                ball.dx*=-1
                score_a+=1
                pen.clear()
                pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24,"normal"))

            if ball.xcor() < -390:
                ball.goto(0,0)
                ball.dx*=-1
                score_b+=1
                pen.clear()
                pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24,"normal"))

            #for collision ball and paddle
            if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
                ball.setx(340)
                ball.dx *=-1    
            
            if ball.xcor() <-340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
                ball.setx(-340)
                ball.dx *=-1    
            
            if score_a == 10:
                
                congr=turtle.Turtle()
                congr.speed(0)
                congr.color("white")
                congr.penup()
                congr.hideturtle()
                congr.goto(0,0)
                congr.write("PLAYER A WINS", align="center", font=("Courier", 28,"bold"))
                sys.exit("Player A wins")

            if score_b == 10:
                
                congr=turtle.Turtle()
                congr.speed(0)
                congr.color("white")
                congr.penup()
                congr.hideturtle()
                congr.goto(0,0)
                congr.write("PLAYER B WINS", align="center", font=("Courier", 28,"bold"))
                sys.exit("Player B wins")


    if input_user==2 :
        init()
        #survival mode code
        start_time = time.time()#for scoring in this


        wn = turtle.Screen()
        wn.title("Pong")
        wn.bgcolor("blue")
        wn.setup(width=800, height=600)
        wn.tracer(0)


        #for keeping track of points of computer
        score_a=0
        


        #paddle A
        paddle_a=turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("red")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350,0)



        #paddle b
        paddle_b=turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("red")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350,0)



        #ball
        ball=turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("black")
        ball.penup()
        ball.goto(0,0)
        ball.dx = 0.36
        ball.dy = 0.36

        #for scoring
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,260)
        pen.write("POINTS LOST: 0", align="center", font=("Courier", 24,"normal"))

      

        def paddle_b_up():
            y = paddle_b.ycor()
            y+=40
            paddle_b.sety(y)

        wn.listen()
        wn.onkeypress(paddle_b_up, "Up")

        def paddle_b_down():
            y = paddle_b.ycor()
            y-=40
            paddle_b.sety(y)

        wn.listen()
        wn.onkeypress(paddle_b_down, "Down")

        def speed_up():
            if elapsed_time%5==0:
                ball.dx+=0.3
                ball.dy+=0.3

      
        #Main game loop
        while True:
            wn.update()
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
            paddle_a.sety(ball.ycor())
            
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy*=-1


            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy*=-1

            if ball.xcor() > 390:
                ball.goto(0,0)
                ball.dx*=-1
                score_a+=1
                pen.clear()
                pen.write("POINTS LOST: {}".format(score_a), align="center", font=("Courier", 24,"normal"))

            if ball.xcor() < -390:
                ball.goto(0,0)
                ball.dx*=-1
                score_b+=1
                pen.clear()
                pen.write("POINTS LOST: {}".format(score_a), align="center", font=("Courier", 24,"normal"))

            #for collision ball and paddle
            if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
                ball.setx(340)
                ball.dx *=-1    
            
            if ball.xcor() <-340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
                ball.setx(-340)
                ball.dx *=-1    
            
              #for calculating score in endless mode using time

            elapsed_time = time.time() - start_time 

            score = int(elapsed_time)#FOR DETERMINING HIGHSCORE(NEEDED)
        
            if score_a==5: # game end
                something(score)
                WRITE_SCORE(user_name,score)
                time=turtle.Turtle()
                time.speed(0)
                time.color("white")
                time.penup()
                time.hideturtle()
                time.goto(0,-260)
                time.write( "SCORE ACHIEVED: {} HIGHSCORE: {}".format( int(elapsed_time), getHighScore()) , align="center", font=("Courier", 20,"normal"))
                sys.exit()




            
