from db.database import CONN, CURSOR

class Pet:
    def __init__(self, name, species, breed, birthdate, owner_id=None, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.breed = breed
        self.birthdate = birthdate
        self.owner_id = owner_id

    def __repr__(self):
        return f"<Pet {self.id}: {self.name}, {self.species}, {self.breed}, {self.birthdate}, Owner ID: {self.owner_id}>"

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
