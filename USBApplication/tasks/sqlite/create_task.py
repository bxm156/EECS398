from tasks.sqlite_task import SQLiteTask


class SQLiteCreateTask(SQLiteTask):
    """
    TODO: Add
    "device_id" integer  REFERENCES devices(ROWID) ON DELETE CASCADE,
    if there is time
    """
    def run(self, connection):
        connection.executescript("""
            CREATE TABLE IF NOT EXISTS devices (
                name Varchar(255),
                serial_no Varchar(255)
            );

            CREATE TABLE IF NOT EXISTS data (
                "flags" INTEGER,
                "epoch" Timestamp,
                "voltage" REAL,
                "current" REAL,
                "period" REAL,
                "active_power" REAL,
                "reactive_power" REAL,
                "apparent_power" REAL,
                "phase_angle" REAL,
                "power_factor" REAL
            );

            CREATE TABLE IF NOT EXISTS actions (
                action integer,
                info TEXT
            );
       """)
