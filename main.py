class Student:
    # [assignment] Skeleton class. Add your code here
    name =""
    age = 35 # class attribute
    tracks = []
    score = 0.00

    # Instantiation
    def __init__(self, name = "Adedayo", age=35, tracks=["Full stack", "Frontend", "Backend"], score=0.00):
        self.name = name # instance attribute
        self.age = age
        self.tracks = tracks
        self.score = score
        pass

    def change_name(self, name): # class method
        self.name = name

    def change_age(self, age): # class method
        self.age = int(age)
        # print ("Student's tracks are ", self.age)

    def add_track(self, tracks): # class method
        self.tracks.append(tracks)
        # print ("Student's tracks are ", self.tracks)
    
    def set_score(self, score):
         self.score = float(score)
         # self.score = round( self.score, 2)
         # self.score = float("{0:.2f}". format(self.score))
        
    def get_score(self): # class method
        print ("Student's score is ", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()