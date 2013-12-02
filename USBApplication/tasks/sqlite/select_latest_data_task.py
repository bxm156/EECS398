from tasks.sqlite.select_task import SQLiteSelectTask


class SQLiteSelectLatestDataTask(SQLiteSelectTask):

    query = "SELECT flags, epoch, voltage, current, period, active_power, reactive_power, apparent_power, phase_angle, power_factor FROM data ORDER BY ROWID DESC LIMIT 1"
