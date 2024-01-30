from db.database import CONN, CURSOR
from datetime import datetime

class Pet:
    def __init__(self, name, species, breed, birthdate, owner_id, id=None):
        self._id = id
        self._name = name
        self._species = species
        self._breed = breed
        self._birthdate = birthdate
        self._owner_id = owner_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        if len(value) > 25:  # Maximum length
            raise ValueError("Name is too long.")
        self._name = value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if not value:
            raise ValueError("Species cannot be empty.")
        if len(value) > 25:  # Maximum length
            raise ValueError("Species is too long.")
        self._species = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if not value:
            raise ValueError("Breed cannot be empty.")
        if len(value) > 25:  # Maximum length
            raise ValueError("Breed is too long.")
        self._breed = value

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')  # Check if the date string matches the format YYYY-MM-DD
        except ValueError:
            raise ValueError("Birthdate should be in YYYY-MM-DD format.")

        self._birthdate = value

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        # Check if the owner_id exists in the database
        sql = """
            SELECT id FROM owners WHERE id = ?
        """
        CURSOR.execute(sql, (value,))
        row = CURSOR.fetchone()
        if not row:
            raise ValueError("Owner with the specified ID does not exist.")

        self._owner_id = value

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Pet instances """
        sql = """
            CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            breed TEXT,
            birthdate TEXT,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owners(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Pet instances """
        sql = """
            DROP TABLE IF EXISTS pets;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the attributes of the current Pet instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO pets (name, species, breed, birthdate, owner_id)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.species, self.breed, self.birthdate, self.owner_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, species, breed, birthdate, owner_id):
        """ Initialize a new Pet instance and save the object to the database """
        pet = cls(name, species, breed, birthdate, owner_id)
        pet.save()
        return pet

    @classmethod
    def get_all(cls):
        """ Retrieve all Pet instances from the database """
        sql = """
            SELECT * FROM pets
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        pets = []
        for row in rows:
            pet = cls(row[1], row[2], row[3], row[4], row[5], row[0])
            pets.append(pet)
        return pets

    @classmethod
    def find_by_id(cls, pet_id):
        """ Find a Pet instance by ID """
        sql = """
            SELECT * FROM pets WHERE id = ?
        """
        CURSOR.execute(sql, (pet_id,))
        row = CURSOR.fetchone()
        if row:
            pet = cls(row[1], row[2], row[3], row[4], row[5], row[0])
            return pet
        else:
            return None
