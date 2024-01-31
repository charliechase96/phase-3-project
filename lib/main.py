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
            name = input("\nEnter owner's name: ")
            try:
                owner = Owner.create(name)
                print(f"\nOwner '{owner.name}' created and placed at list number {owner.id}\n")
            except ValueError as e:
                print(f"\nError: {e}\n")

        elif choice == '2':  # Delete Owner
            owner_id = input("\nEnter owner list number to delete: ")
            try:
                owner_id = int(owner_id)
                owner = Owner.find_by_id(owner_id)
                if owner:
                    owner.delete()
                    print(f"\nOwner '{owner.name}' at list number {owner_id} deleted successfully\n")
                else:
                    print(f"\nOwner at list number {owner_id} not found\n")
            except ValueError:
                print("\nInvalid owner list number\n")

        elif choice == '3':  # Display All Owners
            owners = Owner.get_all()
            if owners:
                print("\nOwners:")
                for owner in owners:
                    print(f"{owner.id}.) {owner.name}")
                print()

                owner_choice = input("Now displaying all pet owners. Enter list number for owner to display pet options for that owner. Enter 'back' to return to the main menu.\n\nEnter your choice: ")

                if owner_choice.lower() == 'back':
                    continue

                try:
                    owner_choice = int(owner_choice)
                    selected_owner = Owner.find_by_id(owner_choice)
                    if not selected_owner:
                        print("\nOwner not found. Please enter a valid list number.\n")
                        continue

                    while True:
                        print("\nPet Menu:")
                        print("1. Create Pet")
                        print("2. Delete Pet")
                        print("3. Display All Pets for Selected Owner")
                        print("4. Back to Previous Menu")

                        print(f"\nNow displaying the pet options for '{selected_owner.name}'. Enter a menu option number to navigate through the available pet options.\n")

                        pet_choice = input("Enter your choice: ")

                        if pet_choice == '1':  # Create Pet
                            name = input("\nEnter pet's name: ")
                            species = input("Enter pet's species: ")
                            breed = input("Enter pet's breed: ")
                            birthdate = input("Enter pet's birthdate (YYYY-MM-DD): ")
                            try:
                                pet = Pet.create(str(name), species, breed, birthdate, owner_choice)
                                print(f"\nPet '{pet.name}' created for owner '{selected_owner.name}'\n")
                            except ValueError as e:
                                print(f"\nError: {e}\n")

                        elif pet_choice == '2':  # Delete Pet
                            pet_id = input("\nEnter pet list number to delete: ")
                            try:
                                pet_id = int(pet_id)
                                pet = Pet.find_by_id(pet_id)
                                if pet:
                                    pet.delete()
                                    print(f"\nPet '{pet.name}' at list number {pet_id} deleted successfully\n")
                                else:
                                    print(f"\nPet not found at list number {pet_id}\n")
                            except ValueError:
                                print("\nInvalid pet list number\n")

                        elif pet_choice == '3':  # Display All Pets for Selected Owner
                            pets = Pet.find_by_owner_id(owner_choice)
                            if pets:
                                print(f"\nPets for owner '{selected_owner.name}':")
                                for pet in pets:
                                    print(f"{pet.id}.) Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Birthdate: {pet.birthdate}")
                                print()

                                pet_number_choice = input(f"Now displaying all pets for owner named {selected_owner.name}. Enter list number for pet to display vaccine options for that pet. Enter 'back' to return to the previous menu.\n\nEnter your choice: ")

                                if pet_number_choice.lower() == 'back':
                                    continue

                                try:
                                    pet_number_choice = int(pet_number_choice)
                                    selected_pet = Pet.find_by_id(pet_number_choice)
                                    if not selected_pet:
                                        print("\nPet not found. Please enter a valid list number.\n")
                                        continue

                                    while True:
                                        print("\nVaccine Menu:")
                                        print("1. Create Vaccine")
                                        print("2. Delete Vaccine")
                                        print("3. Display All Vaccines for Selected Pet")
                                        print("4. Back to Previous Menu")

                                        print(f"\nNow displaying the vaccine options for '{selected_pet.name}'. Enter a menu option number to navigate through the available vaccine options.\n")

                                        vaccine_choice = input("Enter your choice: ")

                                        if vaccine_choice == '1':  # Create Vaccine
                                            vaccine_type = input("\nEnter vaccine type: ")
                                            date_administered = input("Enter date administered (YYYY-MM-DD): ")
                                            next_due_date = input("Enter next due date (YYYY-MM-DD): ")
                                            try:
                                                vaccine = Vaccine.create(vaccine_type, date_administered, next_due_date, pet_number_choice)
                                                print(f"\nVaccine added for pet '{selected_pet.name}'\n")
                                            except ValueError as e:
                                                print(f"\nError: {e}\n")

                                        elif vaccine_choice == '2':  # Delete Vaccine
                                            vaccine_id = input("\nEnter vaccine list number to delete: ")
                                            try:
                                                vaccine_id = int(vaccine_id)
                                                vaccine = Vaccine.find_by_id(vaccine_id)
                                                if vaccine:
                                                    vaccine.delete()
                                                    print(f"\nVaccine at list number {vaccine_id} deleted successfully\n")
                                                else:
                                                    print(f"\nVaccine not found at list number {vaccine_id}\n")
                                            except ValueError:
                                                print("\nInvalid vaccine list number\n")

                                        elif vaccine_choice == '3':  # Display All Vaccines for Selected Pet
                                            vaccines = Vaccine.find_by_pet_id(pet_number_choice)
                                            if vaccines:
                                                print(f"\nVaccines for pet '{selected_pet.name}':")
                                                for vaccine in vaccines:
                                                    print(f"{vaccine.id}.) Type: {vaccine.vaccine_type}, Date Administered: {vaccine.date_administered}, Next Due Date: {vaccine.next_due_date}")
                                                print()

                                                input(f"\nNow displaying all vaccines for pet named {selected_pet.name}. Enter 'back' to return to the previous menu.\n\nEnter your choice: ")

                                            else:
                                                print(f"\nNo vaccines found for pet '{selected_pet.name}'\n")

                                        elif vaccine_choice == '4':  # Back to Previous Menu
                                            print("\nReturning to Previous Menu...\n")
                                            break

                                        else:
                                            print("\nInvalid choice. Please enter a valid option.\n")

                                except ValueError:
                                    print("\nInvalid pet list number\n")

                            else:
                                print(f"\nNo pets found for owner '{selected_owner.name}'\n")

                        elif pet_choice == '4':  # Back to Previous Menu
                            print("\nReturning to Previous Menu...\n")
                            break

                        else:
                            print("\nInvalid choice. Please enter a valid option.\n")

                except ValueError:
                    print("\nInvalid owner list number\n")

            else:
                print("\nNo owners found\n")

        elif choice == '4':  # Exit
            print("\nExiting program...\n")
            sys.exit()

        else:
            print("\nInvalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()