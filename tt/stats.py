import sqlite3
import pandas as pd

def stats():
        conn = sqlite3.connect('C:\\Users\\jakak\Dokumenti\\Automation\\Time-Tracker\\TimeTracker.db')
        cur = conn.cursor()
        df = pd.read_sql_query('SELECT project from TrackingTime GROUP By project;', conn)

        print("\n" \
                        "Your projects:\n" \
                        f"{df.to_string(header=False)} \n")

        not_selected = True
                
        while not_selected:
                try:
                        project_id = int(input("Please select a project, you want to see stats to: "))
                        
                        if df.last_valid_index() >= project_id:
                                break
                        else:
                                print("ID is out of range. Please try again with a different ID.")
                except:
                        print("Error: Input was not an integer! \n")

                

        project = df.iloc[project_id ,0]

        df = pd.read_sql_query(f'SELECT start_time AS "Start Time", end_time AS "End Time", working_time AS "Hours Worked" FROM TrackingTime WHERE project = "{project}"', conn)
        
        print(f"\n\n {project}: \n", df)
        
        total_hours = 0

        for i in range(len(df)):
                total_hours += df.iloc[i, 2] if df.iloc[i, 2] else 0


        print(f'Total working hours: {round(total_hours, 2)} hrs \n')


if __name__ == "__main__":
        stats()