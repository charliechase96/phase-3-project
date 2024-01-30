#!/usr/bin/env python3

from models.owner import Owner
from models.pet import Pet
from models.vaccine import Vaccine
from db import database

# Function to display menu and get user choice
def display_menu():
    print("\nMenu:")
    print("1. Manage Owners")
    print("2. Manage Pets")
    print("3. Manage Vaccines")
    print("4. Exit")
    return input("Enter your choice: ").strip()

# Function to handle owner management
def manage_owners():
    while True:
        print("\nOwner Management:")
        print("1. Add Owner")
        print("2. Delete Owner")
        print("3. Display All Owners")
        print("4. View Owner's Pets")
        print("5. Find Owner by Name")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter owner name: ").strip()
            owner = Owner(name)
            owners.append(owner)
            print(f"Owner '{name}' added successfully.")
        elif choice == '2':
            name = input("Enter owner name to delete: ").strip()
            for owner in owners:
                if owner.name == name:
                    owners.remove(owner)
                    print(f"Owner '{name}' deleted successfully.")
                    break
            else:
                print(f"Owner '{name}' not found.")
        elif choice == '3':
            print("\nAll Owners:")
            for owner in owners:
                print(owner.name)
        elif choice == '4':
            name = input("Enter owner name to view pets: ").strip()
            for owner in owners:
                if owner.name == name:
                    owner.display_info()
                    break
            else:
                print(f"Owner '{name}' not found.")
        elif choice == '5':
            name = input("Enter owner name to find: ").strip()
            for owner in owners:
                if owner.name == name:
                    print("Owner found:")
                    print(owner.name)
                    break
            else:
                print(f"Owner '{name}' not found.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle pet management
def manage_pets():
    while True:
        print("\nPet Management:")
        print("1. Add Pet")
        print("2. Delete Pet")
        print("3. Display All Pets")
        print("4. View Pet's Vaccines")
        print("5. Find Pet by Name")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            owner_name = input("Enter owner name for the pet: ").strip()
            owner = next((owner for owner in owners if owner.name == owner_name), None)
            if owner:
                name = input("Enter pet name: ").strip()
                species = input("Enter species: ").strip()
                breed = input("Enter breed: ").strip()
                birthdate = input("Enter birthdate (YYYY-MM-DD): ").strip()
                pet = Pet(name, species, breed, birthdate)
                owner.add_pet(pet)
                database.add_pet(name, species, breed, birthdate)
                print(f"Pet '{name}' added successfully.")
            else:
                print(f"Owner '{owner_name}' not found.")
        elif choice == '2':
            pet_name = input("Enter pet name to delete: ").strip()
            for owner in owners:
                for pet in owner.pets:
                    if pet.name == pet_name:
                        owner.pets.remove(pet)
                        database.delete_pet(pet_name)
                        print(f"Pet '{pet_name}' deleted successfully.")
                        break
                else:
                    continue
                break
            else:
                print(f"Pet '{pet_name}' not found.")
        elif choice == '3':
            print("\nAll Pets:")
            for owner in owners:
                for pet in owner.pets:
                    print(f"{pet.name} (Owner: {owner.name})")
        elif choice == '4':
            pet_name = input("Enter pet name to view vaccines: ").strip()
            for owner in owners:
                for pet in owner.pets:
                    if pet.name == pet_name:
                        pet.display_info()
                        break
                else:
                    continue
                break
            else:
                print(f"Pet '{pet_name}' not found.")
        elif choice == '5':
            pet_name = input("Enter pet name to find: ").strip()
            for owner in owners:
                for pet in owner.pets:
                    if pet.name == pet_name:
                        print("Pet found:")
                        print(pet.name)
                        print("Owner:", owner.name)
                        break
                else:
                    continue
                break
            else:
                print(f"Pet '{pet_name}' not found.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle vaccine management
def manage_vaccines():
    while True:
        print("\nVaccine Management:")
        print("1. Add Vaccine")
        print("2. Delete Vaccine")
        print("3. Display All Vaccines")
        print("4. Find Vaccine by Type")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            pet_name = input("Enter pet name for the vaccine: ").strip()
            owner = next((owner for owner in owners if any(pet.name == pet_name for pet in owner.pets)), None)
            if owner:
                vaccine_type = input("Enter vaccine type: ").strip()
                date_administered = input("Enter date administered (YYYY-MM-DD): ").strip()
                next_due_date = input("Enter next due date (YYYY-MM-DD): ").strip()
                vaccine = Vaccine(vaccine_type, date_administered, next_due_date)
                for pet in owner.pets:
                    if pet.name == pet_name:
                        pet.add_vaccination(vaccine)
                        database.record_vaccination(pet_name, vaccine_type, date_administered, next_due_date)
                        print("Vaccine added successfully.")
                        break
            else:
                print(f"Pet '{pet_name}' not found.")
        elif choice == '2':
            pet_name = input("Enter pet name for the vaccine to delete: ").strip()
            owner = next((owner for owner in owners if any(pet.name == pet_name for pet in owner.pets)), None)
            if owner:
                vaccine_type = input("Enter vaccine type to delete: ").strip()
                for pet in owner.pets:
                    if pet.name == pet_name:
                        for vaccine in pet.vaccinations:
                            if vaccine.vaccine_type == vaccine_type:
                                pet.vaccinations.remove(vaccine)
                                database.delete_vaccination(pet_name, vaccine_type)
                                print("Vaccine deleted successfully.")
                                break
                        else:
                            print(f"Vaccine '{vaccine_type}' not found for pet '{pet_name}'.")
                        break
            else:
                print(f"Pet '{pet_name}' not found.")
        elif choice == '3':
            print("\nAll Vaccines:")
            for owner in owners:
                for pet in owner.pets:
                    for vaccine in pet.vaccinations:
                        print(f"Pet: {pet.name} (Owner: {owner.name}), Vaccine Type: {vaccine.vaccine_type}")
        elif choice == '4':
            vaccine_type = input("Enter vaccine type to find: ").strip()
            found = False
            for owner in owners:
                for pet in owner.pets:
                    for vaccine in pet.vaccinations:
                        if vaccine.vaccine_type == vaccine_type:
                            print("Vaccine found:")
                            print(f"Pet: {pet.name} (Owner: {owner.name}), Vaccine Type: {vaccine.vaccine_type}")
                            found = True
            if not found:
                print(f"Vaccine '{vaccine_type}' not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    global owners
    owners = []

    database.create_tables()

    while True:
        choice = display_menu()

        if choice == '1':
            manage_owners()
        elif choice == '2':
            manage_pets()
        elif choice == '3':
            manage_vaccines()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
