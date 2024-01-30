class Pet:
    def __init__(self, name, species, breed, birthdate):
        self.name = name
        self.species = species
        self.breed = breed
        self.birthdate = birthdate
        self.vaccinations = []

    def add_vaccination(self, vaccine):
        if isinstance(vaccine, Vaccine):
            self.vaccinations.append(vaccine)
        else:
            print("Invalid vaccine object.")

    def display_info(self):
        print("Name:", self.name)
        print("Species:", self.species)
        print("Breed:", self.breed)
        print("Birthdate:", self.birthdate)
        print("\nVaccination History:")
        for i, v in enumerate(self.vaccinations, 1):
            print(f"{i}. Vaccine Type: {v.vaccine_type}, Administered: {v.date_administered}, Next Due: {v.next_due_date}")
