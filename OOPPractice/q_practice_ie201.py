"""
Add necessary code before the indicated line so that `Run()` function returns the following string as output:

This family has 3 men and 2 women members. Ages of the children are 10 12 15

All your code should be written as classes in accordance with object-oriented principles. Use polymorphism as much as possible.

# Your code will be inserted before this line.

def Run():
	Family = FAMILY()
    M = MOTHER() 
    F = FATHER()
	S1 = SON(10)
    D = DAUGHTER(12) 
    S2 = SON(15)
    Family.AddMember(M)
    Family.AddMember(F)
    Family.AddMember(S1)
    Family.AddMember(D)
    Family.AddMember(S2)
	Family.Print()

print(Run())

"""
class FAMILY():

    def __init__(self):
        self.FamilyMembers = []

    def AddMember(self, member):
        self.FamilyMembers.append(member)

    # Public Function
    def Print(self):
        men = 0
        women = 0
        ages = []
        for member in self.FamilyMembers:
            if member.gender == "M":
                men += 1
            elif member.gender == "W":
                women += 1
        
            if hasattr(member, "age"): # Checks whether this member has an age attribute or not
                ages.append(member.age)

        print(f"This family has {men} men and {women} women members. Ages of the children are {' '.join(ages)}")


class FamilyMember():
    def __init__(self, gender=None):
        self.gender = gender

# Genders in Family Members
class MEN(FamilyMember):
    def __init__(self):
        super().__init__(gender = "M")
class WOMEN(FamilyMember):
    def __init__(self):
        super().__init__(gender = "W")

# Women in Family Members
class DAUGHTER(WOMEN):
    def __init__(self, age):
        super().__init__()
        self.age = str(age)

class MOTHER(WOMEN):
    pass
    # Python automatically does the code above so dont need to write it
    """
    def __init__(self):
        super().__init__()
    """

# Men in Family Members
class SON(MEN):
    def __init__(self, age):
        super().__init__()
        self.age = str(age)

class FATHER(MEN):
    pass
    # Python automatically does the code above so dont need to write it
    """
    def __init__(self):
        super().__init__()
    """
    
def Run():
    Family = FAMILY()
    M = MOTHER() 
    F = FATHER()
    S1 = SON(10)
    D = DAUGHTER(12) 
    S2 = SON(15)

    Family.AddMember(M)
    Family.AddMember(F)
    Family.AddMember(S1)
    Family.AddMember(D)
    Family.AddMember(S2)
    Family.Print()

Run()