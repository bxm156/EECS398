from tasks.sqlite.select_task import SQLiteSelectTask


class SQLiteSelectDataSinceTask(SQLiteSelectTask):

    query = "SELECT epoch, voltage, current, period, active_power, reactive_power, apparent_power, phase_angle, power_factor FROM data WHERE epoch > :since_time ORDER BY epoch ASC, ROWID ASC"
