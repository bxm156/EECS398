from tasks.sqlite.select_task import SQLiteSelectTask


class SQLiteSelectDataTask(SQLiteSelectTask):

    query = "SELECT voltage, current, period, active_power, reactive_power, apparent_power, phase_angle, power_factor FROM data WHERE epoch >= :start_time AND epoch <= :end_time"
