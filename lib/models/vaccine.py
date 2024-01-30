from db.database import CONN, CURSOR
from datetime import datetime

class Vaccine:
    def __init__(self, vaccine_type, date_administered, next_due_date, pet_id=None, id=None):
        self._id = id
        self._vaccine_type = vaccine_type
        self._date_administered = date_administered
        self._next_due_date = next_due_date
        self._pet_id = pet_id

    @property
    def id(self):
        return self._id

    @property
    def vaccine_type(self):
        return self._vaccine_type

    @vaccine_type.setter
    def vaccine_type(self, value):
        if not value:
            raise ValueError("Vaccine type cannot be empty.")
        if len(value) > 25:  # Maximum length
            raise ValueError("Vaccine type is too long.")
        self._vaccine_type = value

    @property
    def date_administered(self):
        return self._date_administered

    @date_administered.setter
    def date_administered(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')  # Check if the date string matches the format YYYY-MM-DD
        except ValueError:
            raise ValueError("Date administered should be in YYYY-MM-DD format.")
        self._date_administered = value

    @property
    def next_due_date(self):
        return self._next_due_date

    @next_due_date.setter
    def next_due_date(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')  # Check if the date string matches the format YYYY-MM-DD
        except ValueError:
            raise ValueError("Next due date should be in YYYY-MM-DD format.")
        self._next_due_date = value

    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        # Check if the pet_id exists in the database
        sql = """
            SELECT id FROM pets WHERE id = ?
        """
        CURSOR.execute(sql, (value,))
        row = CURSOR.fetchone()
        if not row:
            raise ValueError("Pet with the specified ID does not exist.")

        self._pet_id = value

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Vaccine instances """
        sql = """
            CREATE TABLE IF NOT EXISTS vaccines (
            id INTEGER PRIMARY KEY,
            vaccine_type TEXT,
            date_administered TEXT,
            next_due_date TEXT,
            pet_id INTEGER,
            FOREIGN KEY (pet_id) REFERENCES pets(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Vaccine instances """
        sql = """
            DROP TABLE IF EXISTS vaccines;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the attributes of the current Vaccine instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO vaccines (vaccine_type, date_administered, next_due_date, pet_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.vaccine_type, self.date_administered, self.next_due_date, self.pet_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, vaccine_type, date_administered, next_due_date, pet_id):
        """ Initialize a new Vaccine instance and save the object to the database """
        vaccine = cls(vaccine_type, date_administered, next_due_date, pet_id)
        vaccine.save()
        return vaccine

    @classmethod
    def get_all(cls):
        """ Retrieve all Vaccine instances from the database """
        sql = """
            SELECT * FROM vaccines
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        vaccines = []
        for row in rows:
            vaccine = cls(row[1], row[2], row[3], row[4], row[0])
            vaccines.append(vaccine)
        return vaccines

    @classmethod
    def find_by_id(cls, vaccine_id):
        """ Find a Vaccine instance by ID """
        sql = """
            SELECT * FROM vaccines WHERE id = ?
        """
        CURSOR.execute(sql, (vaccine_id,))
        row = CURSOR.fetchone()
        if row:
            vaccine = cls(row[1], row[2], row[3], row[4], row[0])
            return vaccine
        else:
            return None
