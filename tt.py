import sys
from tt.start import start
from tt.end import end
from tt.stats import stats


def main():
        # list[0] is the file name
        #therfore arguments start at index = 1
        list_of_arguments = sys.argv

        if list_of_arguments[1] == "start":
                start()
        elif list_of_arguments[1] == "stop":
                end()
        elif list_of_arguments[1] == "stats":
                stats()
        else:
                print(f"Invalid Argument {list_of_arguments[1]}")


if __name__ == "__main__":
        main()