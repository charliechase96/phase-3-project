#!/usr/bin/env python3

import sys
from models.owner import Owner
from models.pet import Pet
from models.vaccine import Vaccine

def main():
    Owner.create_table()
    Pet.create_table()
    Vaccine.create_table()

    while True:
        print("\nMain Menu:")
        print("1. Create Owner")
        print("2. Delete Owner")
        print("3. Display All Owners")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':  # Create Owner
            name = input("Enter owner's name: ")
            try:
                owner = Owner.create(name)
                print(f"Owner '{owner.name}' created and placed at list number {owner.id}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':  # Delete Owner
            owner_id = input("Enter owner list number to delete: ")
            try:
                owner_id = int(owner_id)
                owner = Owner.find_by_id(owner_id)
                if owner:
                    owner.delete()
                    print(f"Owner '{owner.name}' at list number {owner_id} deleted successfully")
                else:
                    print(f"Owner at list number {owner_id} not found")
            except ValueError:
                print("Invalid owner list number")

        elif choice == '3':  # Display All Owners
            owners = Owner.get_all()
            if owners:
                print("\nOwners:")
                for owner in owners:
                    print(f"{owner.id}.) {owner.name}")

                owner_id_input = input("\nEnter owner list number to see pet information (or type 'back' to return to Main Menu): ")
                if owner_id_input.lower() == 'back':
                    continue

                try:
                    owner_id = int(owner_id_input)
                    owner = Owner.find_by_id(owner_id)
                    if owner:
                        pets = Pet.find_by_owner_id(owner_id)
                        if pets:
                            print(f"\nPets of {owner.name}:")
                            for pet in pets:
                                print(f"{pet.id}.) Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Birthdate: {pet.birthdate}")

                            while True:
                                print("\nPet Menu:")
                                print("1. Create New Pet")
                                print("2. Delete a Pet")
                                print("3. Display Pet Vaccines")
                                print("4. Back to Main Menu")
                                choice_pet_menu = input("\nEnter your choice: ")

                                if choice_pet_menu == '1':  # Create New Pet
                                    name = input("Enter pet's name: ")
                                    species = input("Enter pet's species: ")
                                    breed = input("Enter pet's breed: ")
                                    birthdate = input("Enter pet's birthdate (YYYY-MM-DD): ")
                                    try:
                                        pet = Pet.create(owner_id, name, species, breed, birthdate)
                                        print(f"Pet '{pet.name}' created and placed at list number {pet.id}")
                                    except ValueError as e:
                                        print(f"Error: {e}")

                                elif choice_pet_menu == '2':  # Delete a Pet
                                    pet_id = input("Enter pet list number to delete: ")
                                    try:
                                        pet_id = int(pet_id)
                                        pet = Pet.find_by_id(pet_id)
                                        if pet:
                                            pet.delete()
                                            print(f"Pet '{pet.name}' at list number {pet_id} deleted successfully")
                                        else:
                                            print(f"Pet at list number {pet_id} not found")
                                    except ValueError:
                                        print("Invalid pet list number")

                                elif choice_pet_menu == '3':  # Display Pet Vaccines
                                    pet_id_input = input("\nEnter pet list number to see vaccine information (or type 'back' to return to Pet Menu): ")
                                    if pet_id_input.lower() == 'back':
                                        continue

                                    try:
                                        pet_id = int(pet_id_input)
                                        pet = Pet.find_by_id(pet_id)
                                        if pet:
                                            vaccines = Vaccine.find_by_pet_id(pet_id)
                                            if vaccines:
                                                print(f"\nVaccines for {pet.name}:")
                                                for vaccine in vaccines:
                                                    print(f"{vaccine.id}.) Type: {vaccine.vaccine_type}, Date Administered: {vaccine.date_administered}, Next Due Date: {vaccine.next_due_date}")

                                                while True:
                                                    print("\nVaccine Menu:")
                                                    print("1. Add New Vaccine")
                                                    print("2. Delete Vaccine")
                                                    print("3. Back to Previous Menu")
                                                    choice_vaccine_menu = input("\nEnter your choice: ")

                                                    if choice_vaccine_menu == '1':  # Add New Vaccine
                                                        vaccine_type = input("Enter vaccine type: ")
                                                        date_administered = input("Enter date administered (YYYY-MM-DD): ")
                                                        next_due_date = input("Enter next due date (YYYY-MM-DD): ")
                                                        try:
                                                            vaccine = Vaccine.create(pet_id, vaccine_type, date_administered, next_due_date)
                                                            print(f"Vaccine '{vaccine.vaccine_type}' added successfully")
                                                        except ValueError as e:
                                                            print(f"Error: {e}")

                                                    elif choice_vaccine_menu == '2':  # Delete Vaccine
                                                        vaccine_id = input("Enter vaccine list number to delete: ")
                                                        try:
                                                            vaccine_id = int(vaccine_id)
                                                            vaccine = Vaccine.find_by_id(vaccine_id)
                                                            if vaccine:
                                                                vaccine.delete()
                                                                print(f"Vaccine '{vaccine.vaccine_type}' at list number {vaccine_id} deleted successfully")
                                                            else:
                                                                print(f"Vaccine at list number {vaccine_id} not found")
                                                        except ValueError:
                                                            print("Invalid vaccine list number")

                                                    elif choice_vaccine_menu == '3':  # Back to Previous Menu
                                                        break

                                                    else:
                                                        print("Invalid choice. Please enter a valid option.")

                                            else:
                                                print(f"No vaccines found for {pet.name}")
                                        else:
                                            print(f"No pet found at list number {pet_id}")
                                    except ValueError:
                                        print("Invalid pet list number")

                                elif choice_pet_menu == '4':  # Back to Main Menu
                                    print("Returning to Main Menu...")
                                    break

                                else:
                                    print("Invalid choice. Please enter a valid option.")

                        else:
                            print(f"No pets found for {owner.name}")
                    else:
                        print(f"No owner found at list number {owner_id}")
                except ValueError:
                    print("Invalid owner list number")
            else:
                print("No owners found")

        elif choice == '4':  # Exit
            print("Exiting program...")
            sys.exit()

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
