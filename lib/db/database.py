import sqlite3

DB_FILE = "pet_vaccines.db"
CONN = sqlite3.connect(DB_FILE)
CURSOR = CONN.cursor()

def create_tables():
    CURSOR.execute('''CREATE TABLE IF NOT EXISTS pets
                 (name TEXT PRIMARY KEY,
                  species TEXT,
                  breed TEXT,
                  birthdate TEXT)''')
    CURSOR.execute('''CREATE TABLE IF NOT EXISTS vaccinations
                 (pet_name TEXT,
                  vaccine_type TEXT,
                  date_administered TEXT,
                  next_due_date TEXT,
                  FOREIGN KEY (pet_name) REFERENCES pets(name))''')
    CONN.commit()
    CONN.close()

def add_pet(name, species, breed, birthdate):
    try:
        CURSOR.execute("INSERT INTO pets VALUES (?, ?, ?, ?)", (name, species, breed, birthdate))
        CONN.commit()
        print("Pet added successfully.")
    except sqlite3.IntegrityError:
        print("Pet with the same name already exists.")
    finally:
        CONN.close()

def record_vaccination(pet_name, vaccine_type, date_administered, next_due_date):
    CURSOR.execute("INSERT INTO vaccinations VALUES (?, ?, ?, ?)", (pet_name, vaccine_type, date_administered, next_due_date))
    CONN.commit()
    CONN.close()

def display_pet_info(name):
    CURSOR.execute("SELECT * FROM pets WHERE name=?", (name,))
    pet = CURSOR.fetchone()
    if pet:
        print("Pet Info:")
        print("Name:", pet[0])
        print("Species:", pet[1])
        print("Breed:", pet[2])
        print("Birthdate:", pet[3])
        print("Vaccination History:")
        CURSOR.execute("SELECT * FROM vaccinations WHERE pet_name=?", (name,))
        vaccinations = CURSOR.fetchall()
        if vaccinations:
            for i, v in enumerate(vaccinations, 1):
                print(f"{i}. Vaccine Type: {v[1]}, Administered: {v[2]}, Next Due: {v[3]}")
        else:
            print("No vaccination records found.")
    else:
        print("Pet not found.")
    CONN.close()
