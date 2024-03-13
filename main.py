import random
from ursina import *
# window
window.borderless = False
window.title = 'Name'
# movement
render = False
# y
y = 0
# count
count_1 = 0
# movement
movement = True
# time
time = 0
# player
def update():
    global count, render, floor, y, count_1, movement, time
    # camera
    camera.y = player.y + 6
    if camera.y < 0 + 6:
        camera.y = 0
    # render
    if render == True:
        player.y += 1
        y += 1
        count_1 += 1
        # color change
        fc = color.rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if fc == player.color:
            fc = color.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            for z in range(8):
                for x in range(8):
                    floor = Floor(position=(x, y, z))
                    floor.color = fc
                    R = random.randint(0, 11)
                    if R == 1 and count == 0:
                        count += 1
                        floor.color = color.red
                        floor.collider = 'box'
    # time
    time += 1
    print(time)
    if time == 250:
        movement = False
        for z in range(9):
            for x in range(9):
                floor = Floor(position=(x, y, z))
                floor.color = color.black
    # hit info
    hit_info = player.intersects()
    if hit_info.hit:
        time = -1
        count = 0
        render = True
    if count_1 > 0:
        count_1 = 0
        render = False
    # movement
    if movement == True:
        # up and dow
        if held_keys['w']:
            player.z += 0.1
        if held_keys['s']:
            player.z -= 0.1
        # eds for up and down
        if player.z > 8:
            movement = False
        if player.z < 0:
            movement = False
        # side to side
        if held_keys['d']:
            player.x += 0.1
        if held_keys['a']:
            player.x -= 0.1
        # eds for the sides
        if player.x > 8:
            movement = False
        if player.x < -1:
            movement = False
    else:
        player.y -= 1
    # end game
    def input(key):
        if key == 'left mouse down':
            Ursina = quit()
    if player.y < -1:
        end_game = Text(text= 'End game', position = (-0.6,0), scale = 10)
        button = Button(model = 'cube', scale = (0.5,0.1), position = (0,-0.4), text = 'Exit Game')
        button.on_click = input
# red chance
count = 0
# app
app = Ursina()
# floor
class Floor(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            position = position,
            model = 'cube',
            texture = 'white_cube'
        )

# player
player = Entity(model = 'cube', position = (4,1,4), color = color.red, collider = 'box')
# floor
# color change
fc = color.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
if fc == player.color:
    fc = color.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
else:
    for z in range(8):
        for x in range(8):
            floor = Floor(position=(x, y, z))
            floor.color = fc
            R = random.randint(0, 11)
            if R == 1 and count == 0:
                count += 1
                floor.color = color.red
                floor.collider = 'box'
# camera
camera.position = (3.7,0,-20)
camera.rotation_x = 10
app.run()