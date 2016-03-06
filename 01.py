import cocos
from cocos.actions import Move
from pyglet.window import key
from pyglet.window.key import KeyStateHandler


class HelloWorld(cocos.layer.Layer):
    # Always call super in the constructor:

    def __init__(self):
        super(HelloWorld, self).__init__()
        # To display the text, we’ll create a Label. Keyword arguments are used to set the font, position and alignment of the label:
        label = cocos.text.Label('Hello, Fresher',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        # After defining the HelloWorld class, we need to initialize and create a window. To do this, we initialize the Director:
        label.do(cocos.actions.MoveBy((200, 0), duration=5))
        pass


def act_on_input(dt):
    if keys[key.SPACE]:
        grossini.do(cocos.actions.JumpBy((0, 0), 2, 1, 1))
        print('Space!')
    if keys[key.RIGHT]:
        grossini.do(cocos.actions.MoveBy((10,0),duration=0))
        #grossini.do(cocos.actions.JumpBy((30, 0), 10, 1, 0.5))
        print('right!')
    if keys[key.LEFT]:
        grossini.do(cocos.actions.MoveBy((-10,0),duration=0))
        print('Left')
    if keys[key.UP]:
        grossini.do(cocos.actions.MoveBy((0,10),duration=0))
        print('UP')
    if keys[key.DOWN]:
        grossini.do(cocos.actions.MoveBy((0,-10),duration=0))
        print('DOWN')


def on_key_press(self, symbol, modifiers):
    if symbol == key.LEFT:
        print('left pressed')
        grossini.scale += 0.1
        # self.player.velocity = -self.player.speed, 0


cocos.director.director.init(width=800, height=600, caption="Hello Fresher",
                             fullscreen=False)  # Then we create a HelloWorld instance:
hello_layer = HelloWorld()  # Then we create an Scene that contains the HelloWorld layer as a child:
main_scene = cocos.scene.Scene(hello_layer)
label = cocos.text.Label("Hello Fresher!", position=(5, 5))
main_scene.add(label)
# текстовая метка будет перемещаться вправо на 200 пикселей в течение 5 секунд

back = cocos.sprite.Sprite('zo02-800x600.png')
back.position = 400, 300
main_scene.add(back)

cooler1 = cocos.sprite.Sprite('cooler50x102.png')
cooler1.position = 50, 400
main_scene.add(cooler1)

cooler2 = cocos.sprite.Sprite('cooler50x102.png')
cooler2.position = 500, 200
main_scene.add(cooler2)
# cooler2.do(cocos.actions.JumpBy((0, 0), 5, 500, 1000))

wc1 = cocos.sprite.Sprite('wc80x80.png')
wc1.position = 230, 500
main_scene.add(wc1)

tent1 = cocos.sprite.Sprite('tent120x120.png')
tent1.position = 650, 490
main_scene.add(tent1)

grossini = cocos.sprite.Sprite('grossini.png')
# We place the sprite in the center of the screen. Default position is (0,0):
# grossini.position = 340,220
grossini.position = 49, 70
# We set the scale attribute to 3. This means that our sprite will be 3 times bigger. The default scale attribute is 1:
grossini.scale = 1
# grossini.do(cocos.actions.JumpBy((400, 400), 50, 40, 40))
main_scene.add(grossini)

keys = key.KeyStateHandler()
cocos.director.director.window.push_handlers(keys)
main_scene.schedule(act_on_input)

cocos.director.director.run(main_scene)  # And finally we run the scene:

# cocos.director.director.run(cocos.scene.Scene(HelloWorld()))# A shorter way to write the last 3 statements is this:
