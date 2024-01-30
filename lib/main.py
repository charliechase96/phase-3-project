#!/usr/bin/env python3

import sys
from models.owner import Owner
from models.pet import Pet
from models.vaccine import Vaccine

# Function to display menu
def display_menu():
    print("\nWelcome to Pet Vaccination Tracker!")
    print("1. Owners Menu")
    print("2. Pets Menu")
    print("3. Vaccines Menu")
    print("4. Exit")

# Function to display owner menu
def display_owner_menu():
    print("\nOwners Menu:")
    print("1. Create Owner")
    print("2. Delete Owner")
    print("3. Display All Owners")
    print("4. Find Owner by Name")
    print("5. Exit to Main Menu")

# Function to display pet menu
def display_pet_menu():
    print("\nPets Menu:")
    print("1. Create Pet")
    print("2. Delete Pet")
    print("3. Display All Pets")
    print("4. Find Pet by Name")
    print("5. Find Pets by Owner ID")
    print("6. Exit to Main Menu")

# Function to display vaccine menu
def display_vaccine_menu():
    print("\nVaccines Menu:")
    print("1. Create Vaccine")
    print("2. Delete Vaccine")
    print("3. Display All Vaccines")
    print("4. Find Vaccine by Type")
    print("5. Find Vaccines by Pet ID")
    print("6. Exit to Main Menu")

# Function to handle owner operations
def handle_owner_operations(option):
    if option == '1':  # Create Owner
        name = input("Enter owner's name: ")
        try:
            owner = Owner.create(name)
            print(f"Owner '{owner.name}' created with ID {owner.id}")
        except ValueError as e:
            print(f"Error: {e}")
    elif option == '2':  # Delete Owner
        owner_id = input("Enter owner ID to delete: ")
        try:
            owner_id = int(owner_id)
            owner = Owner.find_by_id(owner_id)
            if owner:
                owner.delete()
                print(f"Owner '{owner.name}' with ID {owner_id} deleted successfully")
            else:
                print(f"Owner with ID {owner_id} not found")
        except ValueError:
            print("Invalid owner ID")
    elif option == '3':  # Display All Owners
        owners = Owner.get_all()
        if owners:
            print("Owners:")
            for owner in owners:
                print(f"ID: {owner.id}, Name: {owner.name}")
        else:
            print("No owners found")
    elif option == '4':  # Find Owner by Name
        name = input("Enter owner's name to find: ")
        owner = Owner.find_by_name(name)
        if owner:
            print(f"Owner found - ID: {owner.id}, Name: {owner.name}")
        else:
            print(f"No owner found with name '{name}'")

# Function to handle pet operations
def handle_pet_operations(option):
    if option == '1':  # Create Pet
        name = input("Enter pet's name: ")
        species = input("Enter pet's species: ")
        breed = input("Enter pet's breed: ")
        birthdate = input("Enter pet's birthdate (YYYY-MM-DD): ")
        owner_id = input("Enter owner's ID for the pet: ")
        try:
            owner_id = int(owner_id)
            pet = Pet.create(name, species, breed, birthdate, owner_id)
            print(f"Pet '{pet.name}' created with ID {pet.id}")
        except ValueError as e:
            print(f"Error: {e}")
    elif option == '2':  # Delete Pet
        pet_id = input("Enter pet ID to delete: ")
        try:
            pet_id = int(pet_id)
            pet = Pet.find_by_id(pet_id)
            if pet:
                pet.delete()
                print(f"Pet '{pet.name}' with ID {pet_id} deleted successfully")
            else:
                print(f"Pet with ID {pet_id} not found")
        except ValueError:
            print("Invalid pet ID")
    elif option == '3':  # Display All Pets
        pets = Pet.get_all()
        if pets:
            print("Pets:")
            for pet in pets:
                print(f"ID: {pet.id}, Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Birthdate: {pet.birthdate}, Owner ID: {pet.owner_id}")
        else:
            print("No pets found")
    elif option == '4':  # Find Pet by Name
        name = input("Enter pet's name to find: ")
        pet = Pet.find_by_name(name)
        if pet:
            print(f"Pet found - ID: {pet.id}, Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Birthdate: {pet.birthdate}, Owner ID: {pet.owner_id}")
        else:
            print(f"No pet found with name '{name}'")
    elif option == '5':  # Find Pets by Owner ID
        owner_id = input("Enter owner ID to find pets: ")
        try:
            owner_id = int(owner_id)
            pets = Pet.find_by_owner_id(owner_id)
            if pets:
                print(f"Pets belonging to owner with ID {owner_id}:")
                for pet in pets:
                    print(f"ID: {pet.id}, Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Birthdate: {pet.birthdate}, Owner ID: {pet.owner_id}")
            else:
                print(f"No pets found for owner with ID {owner_id}")
        except ValueError:
            print("Invalid owner ID")

# Function to handle vaccine operations
def handle_vaccine_operations(option):
    if option == '1':  # Create Vaccine
        vaccine_type = input("Enter vaccine type: ")
        date_administered = input("Enter date administered (YYYY-MM-DD): ")
        next_due_date = input("Enter next due date (YYYY-MM-DD): ")
        pet_id = input("Enter pet ID for the vaccine: ")
        try:
            pet_id = int(pet_id)
            vaccine = Vaccine.create(vaccine_type, date_administered, next_due_date, pet_id)
            print(f"Vaccine '{vaccine.vaccine_type}' created with ID {vaccine.id}")
        except ValueError as e:
            print(f"Error: {e}")
    elif option == '2':  # Delete Vaccine
        vaccine_id = input("Enter vaccine ID to delete: ")
        try:
            vaccine_id = int(vaccine_id)
            vaccine = Vaccine.find_by_id(vaccine_id)
            if vaccine:
                vaccine.delete()
                print(f"Vaccine '{vaccine.vaccine_type}' with ID {vaccine_id} deleted successfully")
            else:
                print(f"Vaccine with ID {vaccine_id} not found")
        except ValueError:
            print("Invalid vaccine ID")
    elif option == '3':  # Display All Vaccines
        vaccines = Vaccine.get_all()
        if vaccines:
            print("Vaccines:")
            for vaccine in vaccines:
                print(f"ID: {vaccine.id}, Type: {vaccine.vaccine_type}, Date Administered: {vaccine.date_administered}, Next Due Date: {vaccine.next_due_date}, Pet ID: {vaccine.pet_id}")
        else:
            print("No vaccines found")
    elif option == '4':  # Find Vaccine by Type
        vaccine_type = input("Enter vaccine type to find: ")
        vaccine = Vaccine.find_by_type(vaccine_type)
        if vaccine:
            print(f"Vaccine found - ID: {vaccine.id}, Type: {vaccine.vaccine_type}, Date Administered: {vaccine.date_administered}, Next Due Date: {vaccine.next_due_date}, Pet ID: {vaccine.pet_id}")
        else:
            print(f"No vaccine found with type '{vaccine_type}'")
    elif option == '5':  # Find Vaccines by Pet ID
        pet_id = input("Enter pet ID to find vaccines: ")
        try:
            pet_id = int(pet_id)
            vaccines = Vaccine.find_by_pet_id(pet_id)
            if vaccines:
                print(f"Vaccines for pet with ID {pet_id}:")
                for vaccine in vaccines:
                    print(f"ID: {vaccine.id}, Type: {vaccine.vaccine_type}, Date Administered: {vaccine.date_administered}, Next Due Date: {vaccine.next_due_date}, Pet ID: {vaccine.pet_id}")
            else:
                print(f"No vaccines found for pet with ID {pet_id}")
        except ValueError:
            print("Invalid pet ID")

# Main function to run the program
def main():
    Owner.create_table()
    Pet.create_table()
    Vaccine.create_table()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':  # Owners Menu
            while True:
                display_owner_menu()
                owner_choice = input("\nEnter your choice: ")
                if owner_choice == '5':
                    break
                handle_owner_operations(owner_choice)
        elif choice == '2':  # Pets Menu
            while True:
                display_pet_menu()
                pet_choice = input("\nEnter your choice: ")
                if pet_choice == '6':
                    break
                handle_pet_operations(pet_choice)
        elif choice == '3':  # Vaccines Menu
            while True:
                display_vaccine_menu()
                vaccine_choice = input("\nEnter your choice: ")
                if vaccine_choice == '6':
                    break
                handle_vaccine_operations(vaccine_choice)
        elif choice == '4':  # Exit
            print("Exiting program...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

