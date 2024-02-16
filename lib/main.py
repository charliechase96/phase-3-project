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
                print(f"\nOwner '{owner.name}' created successfully\n")
            except ValueError as e:
                print(f"\nError: {e}\n")

        elif choice == '2':  # Delete Owner
            owner_id = input("\nEnter owner list number to delete: ")
            try:
                owner_id = int(owner_id)
                owner = Owner.find_by_id(owner_id)
                if owner:
                    owner.delete()
                    print(f"\nOwner '{owner.name}' deleted successfully\n")
                else:
                    print(f"\nOwner not found\n")
            except ValueError:
                print("\nInvalid owner list number\n")

        elif choice == '3':  # Display All Owners
            owners = Owner.get_all()
            if owners:
                print("\nOwners:")
                for owner in owners:
                    print(owner.name)
                print()

                owner_choice = input("Now displaying all pet owners. Enter name of owner to display pet options for that owner. Enter 'back' to return to the main menu.\n\nEnter owner's name: ")

                if owner_choice.lower() == 'back':
                    continue

                selected_owner = Owner.find_by_name(owner_choice)
                if not selected_owner:
                    print("\nOwner not found. Please enter a valid owner's name.\n")
                    continue

                while True:
                    print("\nPet Menu:")
                    print("1. Create Pet")
                    print("2. Delete Pet")
                    print("3. Display All Pets for Selected Owner")
                    print("4. Display All Pets for All Owners")
                    print("5. Back to Previous Menu")

                    print(f"\nNow displaying the pet options for '{selected_owner.name}'. Enter a menu option number to navigate through the available pet options.\n")

                    pet_choice = input("Enter your choice: ")

                    if pet_choice == '1':  # Create Pet
                        name = input("\nEnter pet's name: ")
                        species = input("Enter pet's species: ")
                        breed = input("Enter pet's breed: ")
                        birthdate = input("Enter pet's birthdate (YYYY-MM-DD): ")
                        try:
                            pet = Pet.create(name, species, breed, birthdate, selected_owner.id)
                            print(f"\nPet '{pet.name}' created for owner '{selected_owner.name}'\n")
                        except ValueError as e:
                            print(f"\nError: {e}\n")

                    elif pet_choice == '2':  # Delete Pet
                        pet_name = input("\nEnter pet name to delete: ")
                        try:
                            pet = Pet.find_by_name_owner(pet_name, selected_owner.id)
                            if pet:
                                pet.delete()
                                print(f"\nPet '{pet_name}' deleted successfully\n")
                            else:
                                print(f"\nPet '{pet_name}' not found for owner '{selected_owner.name}'\n")
                        except ValueError:
                            print("\nInvalid pet name\n")

                    elif pet_choice == '3':  # Display All Pets for Selected Owner
                        pets = Pet.find_by_owner_name(selected_owner.name)
                        if pets:
                            print(f"\nPets for owner '{selected_owner.name}':")
                            for pet in pets:
                                print(f"Name: {pet.name}, Species: {pet.species}, Breed: {pet.breed}, Birthdate: {pet.birthdate}")
                            print()

                            pet_name_choice = input(f"Now displaying all pets for owner named {selected_owner.name}. Enter pet name to display vaccine options for that pet. Enter 'back' to return to the previous menu.\n\nEnter your choice: ")

                            if pet_name_choice.lower() == 'back':
                                continue

                            selected_pet = Pet.find_by_name_and_owner_id(pet_name_choice, selected_owner.id)
                            if not selected_pet:
                                print("\nPet not found. Please enter a valid pet's name.\n")
                                continue

                            while True:
                                print("\nVaccine Menu:")
                                print("1. Create Vaccine")
                                print("2. Delete Vaccine")
                                print("3. Display All Vaccines for Selected Pet")
                                print("4. Display All Vaccines for All Pets")
                                print("5. Back to Previous Menu")

                                print(f"\nNow displaying the vaccine options for '{selected_pet.name}'. Enter a menu option number to navigate through the available vaccine options.\n")

                                vaccine_choice = input("Enter your choice: ")

                                if vaccine_choice == '1':  # Create Vaccine
                                    vaccine_type = input("\nEnter vaccine type: ")
                                    date_administered = input("Enter date administered (YYYY-MM-DD): ")
                                    next_due_date = input("Enter next due date (YYYY-MM-DD): ")
                                    try:
                                        vaccine = Vaccine.create(vaccine_type, date_administered, next_due_date, selected_pet.id)
                                        print(f"\nVaccine added for pet '{selected_pet.name}'\n")
                                    except ValueError as e:
                                        print(f"\nError: {e}\n")

                                elif vaccine_choice == '2':  # Delete Vaccine
                                    vaccine_name = input("\nEnter vaccine name to delete: ")
                                    try:
                                        vaccine = Vaccine.find_by_name_pet(vaccine_name, selected_pet.id)
                                        if vaccine:
                                            vaccine.delete()
                                            print(f"\nVaccine '{vaccine_name}' deleted successfully\n")
                                        else:
                                            print(f"\nVaccine '{vaccine_name}' not found for pet '{selected_pet.name}'\n")
                                    except ValueError:
                                        print("\nInvalid vaccine name\n")

                                elif vaccine_choice == '3':  # Display All Vaccines for Selected Pet
                                    vaccines = Vaccine.find_by_pet_name(selected_pet.name)
                                    if vaccines:
                                        print(f"\nVaccines for pet '{selected_pet.name}':")
                                        for vaccine in vaccines:
                                            print(f"Type: {vaccine.vaccine_type}, Date Administered: {vaccine.date_administered}, Next Due Date: {vaccine.next_due_date}")
                                        print()

                                        input(f"\nNow displaying all vaccines for pet named {selected_pet.name}. Enter 'back' to return to the previous menu.\n\nEnter your choice: ")

                                    else:
                                        print(f"\nNo vaccines found for pet '{selected_pet.name}'\n")
                                
                                elif vaccine_choice == '4':  # Display All Vaccines for All Pets
                                    all_vaccines = Vaccine.get_all_with_pets()
                                    if all_vaccines:
                                        print("\nAll Vaccines for All Pets:")
                                        for vaccine, pet_name in all_vaccines:
                                            print(f"Pet: {pet_name}; Vaccine: {vaccine.vaccine_type}, Date Administered: {vaccine.date_administered}, Next Due Date: {vaccine.next_due_date}")
                                        print()

                                        input(f"\nNow displaying all vaccines for all pets. Enter 'back' to return to the previous menu.\n\nEnter your choice: ")

                                    else:
                                        print("\nNo vaccines found in the database.\n")

                                elif vaccine_choice == '5':  # Back to Previous Menu
                                    print("\nReturning to Previous Menu...\n")
                                    break

                                else:
                                    print("\nInvalid choice. Please enter a valid option.\n")

                        else:
                            print(f"\nNo pets found for owner '{selected_owner.name}'\n")

                    elif pet_choice == '4':  # Display All Pets for All Owners
                        all_pets = Pet.get_all_with_owners()
                        if all_pets:
                            print("\nAll Pets:")
                            for pet, owner in all_pets:
                                print(f"Pet: {pet.name}; Owner: {owner.name}")
                            print()

                            pet_name_selection = input("Enter the name of a pet to view vaccine options, or type 'back' to return to the previous menu.\n\nEnter your choice: ")

                            if pet_name_selection.lower() == 'back':
                                continue

                            selected_pet = Pet.find_by_name(pet_name_selection)
                            if selected_pet:
                                while True:
                                    print("\nVaccine Menu:")
                                    print("1. Create Vaccine")
                                    print("2. Delete Vaccine")
                                    print("3. Display All Vaccines for Selected Pet")
                                    print("4. Display All Vaccines for All Pets")
                                    print("5. Back to Previous Menu")

                                    vaccine_choice = input(f"\nEnter your choice for pet '{selected_pet.name}': ")

                                    if vaccine_choice == '1':  # Create Vaccine
                                        vaccine_type = input("\nEnter vaccine type: ")
                                        date_administered = input("Enter date administered (YYYY-MM-DD): ")
                                        next_due_date = input("Enter next due date (YYYY-MM-DD): ")
                                        try:
                                            vaccine = Vaccine.create(vaccine_type, date_administered, next_due_date, selected_pet.id)
                                            print(f"\nVaccine added for pet '{selected_pet.name}'\n")
                                        except ValueError as e:
                                            print(f"\nError: {e}\n")

                                    elif vaccine_choice == '2':  # Delete Vaccine
                                        vaccine_name = input("\nEnter vaccine name to delete: ")
                                        try:
                                            vaccine = Vaccine.find_by_name_pet(vaccine_name, selected_pet.id)
                                            if vaccine:
                                                vaccine.delete()
                                                print(f"\nVaccine '{vaccine_name}' deleted successfully\n")
                                            else:
                                                print(f"\nVaccine '{vaccine_name}' not found for pet '{selected_pet.name}'\n")
                                        except ValueError:
                                            print("\nInvalid vaccine name\n")

                                    elif vaccine_choice == '3':  # Display All Vaccines for Selected Pet
                                        vaccines = Vaccine.find_by_pet_name(selected_pet.name)
                                        if vaccines:
                                            print(f"\nVaccines for pet '{selected_pet.name}':")
                                            for vaccine in vaccines:
                                                print(f"Type: {vaccine.vaccine_type}, Date Administered: {vaccine.date_administered}, Next Due Date: {vaccine.next_due_date}")
                                            print()

                                            input(f"\nNow displaying all vaccines for pet named {selected_pet.name}. Enter 'back' to return to the previous menu.\n\nEnter your choice: ")

                                        else:
                                            print(f"\nNo vaccines found for pet '{selected_pet.name}'\n")

                                    elif vaccine_choice == '4':  # Display All Vaccines for All Pets
                                        all_vaccines = Vaccine.get_all_with_pets()
                                        if all_vaccines:
                                            print("\nAll Vaccines for All Pets:")
                                            for vaccine, pet_name in all_vaccines:
                                                print(f"Pet: {pet_name}; Vaccine: {vaccine.vaccine_type}, Date Administered: {vaccine.date_administered}, Next Due Date: {vaccine.next_due_date}")
                                            print()

                                            input(f"\nNow displaying all vaccines for all pets. Enter 'back' to return to the previous menu.\n\nEnter your choice: ")

                                        else:
                                            print("\nNo vaccines found in the database.\n")

                                    elif vaccine_choice == '5':  # Back to Previous Menu
                                        break  # Exit the vaccine menu

                                    else:
                                        print("\nInvalid choice. Please enter a valid option.\n")

                            else:
                                print("\nPet not found. Please enter a valid pet's name.\n")

                        else:
                            print("\nNo pets found in the database.\n")


                    elif pet_choice == '5':  # Back to Previous Menu
                        print("\nReturning to Previous Menu...\n")
                        break

                    else:
                        print("\nInvalid choice. Please enter a valid option.\n")

            else:
                print("\nNo owners found\n")

        elif choice == '4':  # Exit
            print("\nExiting program...\n")
            sys.exit()

        else:
            print("\nInvalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()