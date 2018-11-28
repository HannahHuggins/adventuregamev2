from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not configured")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):

    quips = [
        "You became a coopian you sucka",
        "Your Mum needs a comma",
        "You died you dickhead",
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print("-" * 10)
        print(dedent("""
        The coopians of Planet coop have invaded your workplace and annihilated your
        colleagues. You have been forced to adopt their way of life and their 
        confusing agile principles. You mission is to remain as introverted as possible,
        to avoid turning into a coopian. 
        
        The project manager is a tall, green-haired alien with horns protruding from his 
        forehead. He screams "stand up!" and you watch as the other coopians flock to join him.
        
        Do you:
        
        Join them, hide, or pretend as if nothing has happened? 
        """))

        choice = input("> ")

        if choice == "join":
            return 'death'
        elif choice == "hide":
            print(dedent("""
            You hide under your desk like a coward, listening out for the signs of 
            footsteps. 
            The manager walks around the corner and glares at you. You avert your eyes and
            start humming a song under your breath. He sighs and turns away. You will never be a true coopian.
            """))
            return 'device_lab'
        elif choice == "pretend":
            print(dedent("""
            You follow the horde into the auditorium and see that they are taking part in a satanic ritual
            known as a "retro". You look on in horror as they all share ideas and "take part." You don't know
            where to look.
            """))
            return 'auditorium'
        else:
            print("Please try again.")
            return 'central_corridor'


class DeviceLab(Scene):

    def enter(self):
        print(dedent("""
        You emerge from under your desk and run to the device lab, scanning the rows of desks for any sign
        of the coopians. 
        You fling open the door to the lab and grab the nearest ipad to use as a weapon.
        You see a coopian walk towards you and whap them in the side of the head with apples latest device.
        "You'll never convert me!" You shout.
        """))
        return 'fight'


class Auditorium(Scene):

    def enter(self):
        print(dedent("""
        After what feels like a week (2 hours in coopian time), they start to leave the auditorium.
        You breathe a sign of relief, you could feel your resolve breaking.
        "They're not so bad" you find yourself thinking.
        All of a sudden, the green haired project manager is behind you.
        "What did you think of the session?" He asked with a friendly smile.
        You scramble for something to say.
         """))
        return 'awkward'


class Fight(Scene):

    def enter(self):
        print(dedent("""
        You sprint to the door of the device room, to find that it's locked. Panic rises in your throat
        as you claw at the door. You notice a keypad on the side of the door. The passcode is 3 digits, but you
        can't remember what it is. You remember being told that if you input the code incorrectly 10 times the door
        will remain shut and the alarms will sound, giving away your position.
        """))

        code = randint(1,5)
        guess = int(input("> "))
        guesses = 0

        while guess != code and guesses < 9:
            print("Try again!")
            guesses += 1
            guess = int(input())
            if guess < code:
                print("Guess higher!")
            elif guess > code:
                print("Guess lower!")
        if guesses == 9:
            return 'death'
        elif guess == code:
            print(dedent("""
            You grab an iphone in each hand, and connect the charger cables to them, using them as nunchucks.
                They whistle as they swing through the air, knocking out the remaining coopians.
                You survived!
            
            """))
            return 'last_scene'


class Awkward(Scene):

    def enter(self):
        print(dedent("""
        "It was great." You whisper, sweat forming on your brow. He senses your hesitation and moves closer.
        His red eyes pierce yours, and smoke starts billowing out of his dragon-like nose. 
        You run to the device lab, knowing that this is your only hope.
        """))
        return 'fight'


class TheEnd(Scene):

    def enter(self):
        print("You have finished the game!")
        exit(0)


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'death': Death(),
        'device_lab': DeviceLab(),
        'auditorium': Auditorium(),
        'fight': Fight(),
        'awkward': Awkward(),
        'last_scene': TheEnd(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
