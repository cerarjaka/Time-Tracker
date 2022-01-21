from datetime import datetime, timedelta
import sqlite3
import pandas as pd

def end():
        conn = sqlite3.connect('C:\\Users\\jakak\Dokumenti\\Automation\\Time-Tracker\\TimeTracker.db')
        cur = conn.cursor()

        # get last entry and check if end_time is null
        df = pd.read_sql_query("SELECT * FROM TrackingTime Order by id DESC LIMIT 1;", conn)
        id, start_time, end_time = df.iloc[0, 0], df.iloc[0, 1], df.iloc[0, 2]

        if not end_time:
                # end_time is not set
                cur.execute(f"UPDATE TrackingTime SET end_time = datetime('now') WHERE id = {id}")
                conn.commit()

                df = pd.read_sql_query("SELECT * FROM TrackingTime Order by id DESC LIMIT 1;", conn)
                id, start_time, end_time = df.iloc[0, 0], df.iloc[0, 1], df.iloc[0, 2]

                start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
                end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

                delta = round(abs(end_time - start_time).total_seconds() / 3600, 2)

                cur.execute(f"UPDATE TrackingTime SET working_time = {delta} WHERE id = {id}")
                conn.commit()

                print(f"Today you worked: {delta} hrs")
                
        else:
                # end_time is set return error message
                print("You do not have a TimeTracker running.")



if __name__ == "__main__":
        end()