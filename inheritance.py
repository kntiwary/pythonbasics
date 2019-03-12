



class Animal:
    def __init__(self):
        print("Animal is ready")


    def whoIsThis(self):
        print("This is Animal")

    def swim(self):
        print("Swim Faster")

class Bird:
    def __init__(self):
        print("Bird is ready")


    def whoIsThis(self):
        print("This is Bird")

    def swim(self):
        print("Swim Faster")

class Penguim(Animal,Bird):
    def __init__(self):
        super().__init__()
        print("Penguim is ready")

    #
    # def whoIsThis(self):
    #     print("Penguim")

    def run(self):
        print("Run Faster")

peggy = Penguim()
peggy.whoIsThis()


