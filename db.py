class Database:
    def __init__(self, filename):
        self.f = open(filename,'rt')
        print(self.f.read())
