class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self.pets.append(pet)
        else:
            print("Invalid pet object.")

    def display_info(self):
        print("Owner:", self.name)
        print("Pets:")
        for pet in self.pets:
            pet.display_info()
