# Python file for starting the timetracker
import sqlite3
import pandas as pd

def start():
        conn = sqlite3.connect('C:\\Users\\jakak\Dokumenti\\Automation\\Time-Tracker\\TimeTracker.db')
        cur = conn.cursor()

        df = pd.read_sql_query("SELECT * FROM TrackingTime Order by id DESC LIMIT 1;", conn)
        
        
        end_time = df.iloc[0, 2] if len(df) > 0 else True

        if not end_time:
                print("Error: You cannot have two Trackers running at the same time!")
                return

        # ask if user wants to continue on existing project
        continue_exist_proj = input("Do you want to continue on an existing project? (y or n) : ")

        if continue_exist_proj.lower() == 'y':
                # retrieve projects
                avpr_df = pd.read_sql_query('SELECT project from TrackingTime GROUP By project;', conn)
                print("\n" \
                        "Your projects:\n" \
                        f"{avpr_df.to_string(header=False)} \n")

                not_selected = True
                
                while not_selected:
                        project_id = int(input("Please select a project by entering its id: "))
                        
                        if avpr_df.last_valid_index() >= project_id:
                                break
                        else:
                                print("ID is out of range. Please try again with a different ID.")

                project = avpr_df.iloc[project_id ,0]
        else:
                project = input("What should your project be called? : ")
        
        # now we got the project name
        # next we will create record of starting time and
        cur.execute("INSERT INTO TrackingTime (start_time, project) VALUES (datetime('now'), ?)", (project,))
        conn.commit()

if __name__ == "__main__":
       start()