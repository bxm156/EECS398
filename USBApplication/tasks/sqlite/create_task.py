from tasks.sqlite_task import SQLiteTask


class SQLiteCreateTask(SQLiteTask):

    def run(self, connection):
        connection.executescript("""
            CREATE TABLE IF NOT EXISTS devices (
                id integer  PRIMARY KEY AUTOINCREMENT DEFAULT NULL,
                name Varchar(255),
                serial_no Varchar(255)
            );

            CREATE TABLE IF NOT EXISTS data (
                id integer  PRIMARY KEY AUTOINCREMENT DEFAULT NULL,
                device_id integer  REFERENCES devices(id) ON DELETE CASCADE,
                timestamp Timestamp DEFAULT NULL,
                voltage REAL,
                current REAL,
                "power" REAL,
                "frequency" REAL,
                spike Boolean,
                dip Boolean,
                failure Boolean
            );

            CREATE TABLE IF NOT EXISTS actions (
                id integer  PRIMARY KEY AUTOINCREMENT DEFAULT NULL,
                action integer,
                info TEXT
            );
       """)
