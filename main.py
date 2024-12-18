import pyxel

import pyxel

class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)

        pyxel.load("my_resource.pyxres")

        # Set the initial position of the square
        self.x = 15
        self.y = 55
        self.score = 0
        self.space_pressed = False

     
        # Set the initial position and velocity of the sprite
        self.sprite_x = 130
        self.sprite_y = 60
        self.sprite_dx = 0
        self.sprite_dy = 2

        

        # Start the game loop
        pyxel.run(self.update, self.draw)


    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        if pyxel.btn(pyxel.KEY_SPACE):
            self.space_pressed = True

        if self.space_pressed == True:
            self.x += 5
        if self.x > 160:
            self.x = 15
            self.space_pressed = False
            
        
        # Simple interaction: Increase score when square reaches top-left corner
        if self.x < 10 and self.y < 10:
            self.score += 1

        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy

        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 160:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1
            
        if abs(self.x - self.sprite_x) <= 10 and abs(self.y - self.sprite_y) <= 10:
            self.score += 1
            
    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(1)

        # Draw a square (color 9)
        # pyxel.rect(self.x, self.y, 10, 10, 9)
        pyxel.blt(0, 0, 2, 0, 0, 160, 120)
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)  # Draws a 16x16 sprite from bank 0
        pyxel.blt(self.sprite_x, self.sprite_y, 1, 0, 0, 16, 16, 0)  # Draws a 16x16 sprite from bank 1
        


        # Draw the moving sprite (color 11)
        #pyxel.circ(self.sprite_x, self.sprite_y, 5, 11)
        #pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        # Display a message when score is high
        if self.score >= 100:
            pyxel.text(35, 50, "You won the game!!", 8)

# Run the game
App()