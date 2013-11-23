from tasks.sqlite.select_task import SQLiteSelectTask


class SQLiteSelectDataTask(SQLiteSelectTask):

    query = "SELECT voltage, current, power, frequency FROM data WHERE timestamp >= :start_time AND timestamp <= :end_time"
