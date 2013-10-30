from tasks.sqlite_task import SQLiteTask


class SQLiteCreateTask(SQLiteTask):

    def run(self, connection):
        connection.executescript("""
            CREATE TABLE devices (
                id integer  PRIMARY KEY AUTOINCREMENT DEFAULT NULL,
                name Varchar(255),
                serial_no Varchar(255)
            );

            CREATE TABLE data (
                id integer  PRIMARY KEY AUTOINCREMENT DEFAULT NULL,
                device_id integer  REFERENCES devices(id) ON DELETE CASCADE,
                timestamp Timestamp DEFAULT NULL,
                voltage integer,
                current integer,
                "power" integer,
                spike Boolean,
                dip Boolean,
                failure Boolean
            );

            CREATE TABLE actions (
                id integer  PRIMARY KEY AUTOINCREMENT DEFAULT NULL,
                action integer,
                info TEXT
            );
       """)
