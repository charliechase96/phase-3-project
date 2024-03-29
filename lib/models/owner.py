from db.database import CONN, CURSOR
import models.pet as pet_module

class Owner:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    # @property
    # def id(self):
    #     return self._id

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

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Owner instances """
        sql = """
            CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Owner instances """
        sql = """
            DROP TABLE IF EXISTS owners;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Owner instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO owners (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
    
    def delete(self):
        """ Delete the owner and all their associated pets from the database """
        # First, check if the owner exists
        sql_select = """
            SELECT id FROM owners WHERE id = ?
        """
        CURSOR.execute(sql_select, (self.id,))
        row = CURSOR.fetchone()

        if row:
            # If owner exists, first delete all pets belonging to this owner
            pet_module.Pet.delete_by_owner_id(self.id)

            # Then, delete the owner
            sql_delete = """
                DELETE FROM owners WHERE id = ?
            """
            CURSOR.execute(sql_delete, (self.id,))
            CONN.commit()

    @classmethod
    def create(cls, name):
        """ Initialize a new Owner instance and save the object to the database """
        owner = cls(name)
        owner.save()
        return owner

    @classmethod
    def get_all(cls):
        """ Retrieve all Owner instances from the database """
        sql = """
            SELECT * FROM owners WHERE name != ''
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        owners = []
        for row in rows:
            owner_id, owner_name = row[0], row[1]
            owner = cls(owner_name, owner_id)
            owners.append(owner)
        return owners
    
    @classmethod
    def delete_empty_names(cls):
        """ Delete records with empty names from the database """
        sql = """
            DELETE FROM owners WHERE name = ''
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def find_by_id(cls, owner_id):
        """ Find an Owner instance by ID """
        sql = """
            SELECT * FROM owners WHERE id = ?
        """
        CURSOR.execute(sql, (owner_id,))
        row = CURSOR.fetchone()
        if row:
            owner = cls(row[1], row[0])
            return owner
        else:
            return None
        
    @classmethod
    def find_by_name(cls, name):
        """ Find an Owner instance by name """
        sql = """
            SELECT * FROM owners WHERE name = ?
        """
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        if row:
            owner_id, owner_name = row[0], row[1]
            return cls(owner_name, owner_id)
        else:
            return None
        
    @classmethod
    def find_id_by_name(cls, name):
        """ Find owner ID by name """
        sql = """
            SELECT id FROM owners WHERE name = ?
        """
        CURSOR.execute(sql, (name,))
        row = CURSOR.fetchone()
        if row:
            return row[0]
        else:
            print("No owner found with the specified name.")
            return None