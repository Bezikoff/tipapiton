import math


a110 =input()
if a110 == '1.1':
    class Robot:
        def perform_actions(self):
            print("Робот совершает случайные действия")

        def freeze(self):
            print("Робот бездействует")


    robot = Robot()

    robot.perform_actions()
    robot.perform_actions()
    robot.freeze()
elif a110 == '1.2':
    class Player:
        spec = 'warrior'

        def change_specialization(self):
            if self.spec == 'warrior':
                self.spec = 'thief'
            elif self.spec == 'thief':
                self.spec = 'magician'
            else:
                self.spec = 'warrior'

        def print_specialization(self):
            print(self.spec)

    player = Player()

    player.change_specialization()
    player.change_specialization()
    player.print_specialization()

    player.change_specialization()
    player.print_specialization()
elif a110=='1.3':
    class MusicDevice:
        volume = 0
        def increase_volume(self):
            if self.volume < 10:
                self.volume+=1
        def decrease_volume(self):
            if self.volume > 0:
                self.volume -=1
        def make_volume(self, a):
            if a>10:
                self.volume = 10
            elif a < 0:
                self.volume = 0
            else:
                self.volume = a

    music_device = MusicDevice()

    music_device.increase_volume()
    print(music_device.volume)

    music_device.make_volume(13)
    print(music_device.volume)

    for i in range(1000):
        music_device.decrease_volume()
    print(music_device.volume)
elif a110=='2.1':
    class Rectangle:
        def __init__(self, width, height):
            global r
            if width < 0:
                width = 0
            if height < 0:
                height = 0
            self.weight = width
            self.height = height
            self.oreo = width * height
            self.perimetro = width * 2 + height * 2
            if width == height:
                self.is_sqvara = True
            else:
                self.is_sqvara = False
            if math.pow((self.weight**2+self.height**2), 1/2) <= r*2:
                self.yes = True
            else:
                self.yes = False

        def is_in_circle(self):
            return self.yes
            
        def area(self):
            return self.oreo
        
        def perimeter(self):
            return self.perimetro

        def is_square(self):
            return self.is_sqvara

    rec = Rectangle(5, 3)

    print(rec.area())
    print(rec.perimeter())

    if not rec.is_square():
        rec.weight, rec.height = (
            max(rec.weight, rec.height),
            max(rec.weight, rec.height)
        )
    print(rec.area())
    print(rec.perimeter())

    r = 1
    while not rec.is_in_circle():
        r += 1
    print(r)
