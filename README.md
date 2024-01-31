# Pet Vaccination Tracker CLI Project

The Pet Vaccination Tracker is a command-line interface (CLI) application built with Python that helps pet owners keep track of their pets' vaccinations. The CLI script **main.py** serves as the entry point to the application, providing users with various options to manage owners, pets, and vaccines.

## CLI Script (main.py)

The **main.py** script provides a user-friendly interface for interacting with the Pet Vaccination Tracker. Upon running the script, users are presented with a main menu that allows them to navigate through different options:

+ **Owners Menu:** Create, delete, display, and find owners by name.
+ **Pets Menu:** Create, delete, display, and find pets by name or owner ID.
+ **Vaccines Menu:** Create, delete, display, and find vaccines by type or pet ID.
+ **Exit:** Terminate the application.

Users can input their choices using the corresponding numerical options and follow the on-screen prompts to perform desired actions.

## Functions

### handle_owner_operations(option)

Handles operations related to owners, such as creating, deleting, displaying, and finding owners by name.

### handle_pet_operations(option)

Handles operations related to pets, such as creating, deleting, displaying, and finding pets by name or owner ID.

### handle_vaccine_operations(option)

Handles operations related to vaccines, such as creating, deleting, displaying, and finding vaccines by type or pet ID.

### display_menu()

Displays the main menu options to the user.

### display_owner_menu()

Displays the owner menu options to the user.

### display_pet_menu()

Displays the pet menu options to the user.

### display_vaccine_menu()

Displays the vaccine menu options to the user.

## Models

### Owner

Represents an owner of a pet. Includes attributes such as name and ID.

### Pet

Represents a pet. Includes attributes such as name, species, breed, birthdate, and owner ID.

### Vaccine

Represents a vaccine administered to a pet. Includes attributes such as type, date administered, next due date, and pet ID.

## Database

The Pet Vaccination Tracker uses an SQLite database to persist data. The database schema is defined in the **database.py** file, and tables for owners, pets, and vaccines are created upon initialization of the application. Each model class is mapped to its corresponding table in the database for seamless data management.