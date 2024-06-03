class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self,name,pet_type,owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}.")
        self.name = name
        self.pet_type = pet_type
        if isinstance(owner,Owner):
            owner.add_pet(self)
            self.owner = owner
        else:
            self.owner = {}    
        self.add_pet_to_all(self)

    @classmethod
    def add_pet_to_all(cls,pet):
        cls.all.append(pet)    


class Owner:
    def __init__(self, name):
        self.name = name
        self.pet_s = []

    def pets(self):
        return self.pet_s

    def add_pet(self, pet):
        if isinstance(pet,Pet):
            self.pet_s.append(pet)
            pet.owner = self
        else:
            raise Exception(f'{pet} is not of class Pet')

    def get_sorted_pets(self):
        return sorted(self.pet_s,key=lambda pet:pet.name)              
    pass

owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)
print(owner.get_sorted_pets())