import tkinter as tk
from PIL import Image, ImageTk

# Set up the main window
root = tk.Tk()
root.title("Space Invaders")
root.resizable(False, False)
root.geometry("800x600")

# Create the canvas for the game
canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()

# Load the spaceship image
spaceship_image = Image.open(
    r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0099__Day95_Pro_Portfolio_Project_Alien_Invaders__241001\NewProject\r00_env_START\r05\spaceship.png")
spaceship_image = spaceship_image.resize((40, 40), Image.Resampling.LANCZOS)  # Resize image to fit
spaceship_photo = ImageTk.PhotoImage(spaceship_image)

# Load the barrier image
barrier_image = Image.open(r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0099__Day95_Pro_Portfolio_Project_Alien_Invaders__241001\NewProject\r00_env_START\r05\barrier.png")  # Update with the correct path to your barrier image
barrier_image = barrier_image.resize((40, 40), Image.Resampling.LANCZOS)
barrier_photo = ImageTk.PhotoImage(barrier_image)

# Spaceship properties
spaceship_x = 380  # starting x position of the spaceship
spaceship_y = 550  # fixed y position (near the bottom of the window)
spaceship_speed = 20

# Create the spaceship using the image
spaceship = canvas.create_image(spaceship_x, spaceship_y, image=spaceship_photo, anchor="nw")

# Variable to keep track of the active bullet
active_bullet = None


# Function to move the spaceship left
def move_left(event):
    x1, y1 = canvas.coords(spaceship)
    if x1 > 0:
        canvas.move(spaceship, -spaceship_speed, 0)


# Function to move the spaceship right
def move_right(event):
    x1, y1 = canvas.coords(spaceship)
    if x1 < 760:  # Make sure spaceship doesn't move past the right edge of the screen
        canvas.move(spaceship, spaceship_speed, 0)


# Function to fire a bullet (only one active bullet at a time)
def fire_bullet(event):
    global active_bullet
    # If there's already an active bullet, do nothing
    if active_bullet is not None:
        return

    # Create a new bullet
    x1, y1 = canvas.coords(spaceship)
    bullet = canvas.create_rectangle(x1 + 20 - 2, y1 - 10, x1 + 20 + 2, y1, fill="red")
    active_bullet = bullet
    move_bullet()


# Function to move the active bullet
def move_bullet():
    global active_bullet
    if active_bullet is not None:
        canvas.move(active_bullet, 0, -10)
        bullet_coords = canvas.coords(active_bullet)

        # If the bullet goes off-screen, remove it
        if bullet_coords[1] < 0:
            canvas.delete(active_bullet)
            active_bullet = None  # Reset the active bullet variable

    # Continue moving the bullet until it goes off-screen or is deleted
    if active_bullet is not None:
        root.after(50, move_bullet)


# Function to create barriers
def create_barriers():
    barrier_y = spaceship_y - 150  # 150 pixels above the spaceship
    barrier_spacing = 160  # Evenly space the barriers horizontally

    # Create four barriers shifted 20 pixels to the left
    for i in range(4):
        barrier_x = 135 + i * barrier_spacing  # Shifted 20 pixels to the left from previous position
        canvas.create_image(barrier_x, barrier_y, image=barrier_photo, anchor="nw")


# Create barriers on the screen
create_barriers()

# Bind key events to spaceship movement and firing
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", fire_bullet)

# Start the game loop
root.mainloop()
