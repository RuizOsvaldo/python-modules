"""
Create a single player Pong game
"""
from Ball import Ball
from Paddle import Paddle

def setup():
    global started
    started = False
    
    # 1. Set the size of your window to at least width = 800, height = 600
    size(800,600)
    
    # 2. Make a global ball variable
    #global ball
    global ball
    
    # 3. Initialize your ball variable to a new Ball(x)
    #ball = Ball(width/2)
    ball = Ball(width/2)
    
    # 4. Make a global paddle variable
    global paddle
    
    # 5. Initialize your paddle variable to a new Paddle(x)
    paddle = Paddle(width/2)

    
def draw():
    if not started:
        textSize(32)
        fill(0)
        text("Press 's' to start", width/3, height/2)
        return
    
    # 6. Use the background() function to set the background color.
    #    background(0) will set a classic black background
    #    Do you see your background color?
    background(0)

    # 7. Call the ball object's update() and draw() methods.
    #    Do you see the ball moving on the screen?
    ball.update()
    ball.draw()

    # 8. Call the paddle object's update() and draw() methods.
    #    Do you see the paddle on the screen?
    paddle.update()
    paddle.draw()

    # 9. Finish the code in keyPressed() and keyReleased() first!
    
    
    # 12. Call the ball object's collision(paddle) method and pass the
    #     paddle object as an input variable.
    #     Does the ball bounce off the paddel?
    ball.collision(paddle)
    # 12. End the game when the ball goes below the bottom of the screen.
    #     You can use noLoop() to freeze the game and text() to print text
    #     on the screen.

    # 13. Figure out how to add a score to the game so every bounce off
    #     the paddle increases the player socre

    # *EXTRA*
    # Can you figure out how to make a 2 player pong game with paddles on
    # the left and right on the screen?

def keyPressed():
    if key == 's':
        global started
        started = True 
    elif key == CODED:
        pass
        
        # 10. Change paddle.x_speed when the 'keyCode' variable is
        #     equal to LEFT or RIGHT.
        #     Does the paddle move?
        if keyCode == LEFT:
            paddle.x_speed = -15
            pass
        if keyCode == RIGHT:
            paddle.x_speed = 15


def keyReleased():
    if key == CODED:
        pass
        
        # 11. Set paddle.x_speed to 0 when the LEFT or RIGHT arrow keys are released.
        #     Does the paddle stop when the keys are released?
        if keyCode == LEFT or keyCode == RIGHT:
            paddle.x_speed = 0
            
