class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = ''):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        """pet_type getter"""
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        """pet_type setter"""
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise TypeError('pet_type must be in PET_TYPES')
        
    @property
    def owner(self):
        """owner property"""
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        """owner setter method"""
        if isinstance(owner, Owner):
            self._owner = owner
        else:
            raise TypeError('owner must be of Owner type')


class Owner:

    def __init__(self, name):
        self.name = name
        #self.owners_pets = []

    def pets(self):
        return [p for p in Pet.all if p.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError('pet must be of Pet type')

    def get_sorted_pets(self):
        return [p for p in sorted(self.pets(), key = lambda p: p.name) ]