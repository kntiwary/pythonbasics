class Parrot:
    def fly(self):
        print ("Parrot can fly")


class Penguim:
    def fly(self):
        print ("Penguim can fly")



def test_flight(bird):
    bird.fly()


peng = Penguim()
par = Parrot()

test_flight(par)

test_flight(peng)