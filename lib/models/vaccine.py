class Vaccine:
    def __init__(self, vaccine_type, date_administered, next_due_date, pet_id=None, id=None):
        self.id = id
        self.vaccine_type = vaccine_type
        self.date_administered = date_administered
        self.next_due_date = next_due_date
        self.pet_id = pet_id

    def __repr__(self):
        return f"<Vaccine {self.id}: Type - {self.vaccine_type}, Administered - {self.date_administered}, Next Due - {self.next_due_date}, Pet ID - {self.pet_id}>"

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

    def update(self):
        """Update the table row corresponding to the current Vaccine instance."""
        sql = """
            UPDATE vaccines
            SET vaccine_type = ?, date_administered = ?, next_due_date = ?, pet_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.vaccine_type, self.date_administered, self.next_due_date, self.pet_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Vaccine instance"""
        sql = """
            DELETE FROM vaccines
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
