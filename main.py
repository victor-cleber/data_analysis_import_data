from mysql.connector import MySQLConnection, Error
from datetime import date
import sys
import csv
import os

# import sleep to show output for some time period
from time import sleep
# import only system from os
from os import system, name

database_ip = None
database_name = None
database_user = None
database_password = None
csv_path = None
csv_files = None

# define our clear function


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_database_details():
    print("Inform the database")
    print("IP: ")
    database_ip = input()
    print("Name: ")
    database_name = input()
    print("User: ")
    database_user = input()
    print("Inform the database Password: ")
    database_password = input()


def test_database_connection():
    result = False
    try:
        conn = MySQLConnection(
            user=database_user,
            password=database_password,
            host=database_ip,
            database=database_name
        )
        # creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Executing a MYSQL function using the execute() method
        cursor.execute('SELECT DATABASE()')

        # Fetch a single row using fetchone() method
        data = cursor.fetchone()
        print("Connection established to ", data)
        result = True
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        # Closing the connection
        cursor.close()
        conn.close()
        print("ok")
    return result


def file_was_already_imported():
    # open log file
    # check if csv was already imported
    return True


def import_files():
    # establishing  the connection
    db_details = get_database_details
    conn = MySQLConnection(
        user='vcleber',
        password='795641',
        host='192.168.1.83',
        database="casestudy1"
    )


def get_csv_files():
    csv_files = None
    csv_path = input("Inform where the files (.csv) are: ")
    dir_list = os.listdir(csv_path)
    for x in dir_list:
        if x.endswith(".csv"):
            print(x)
            csv_files = csv_path + "\\" + x
        else:
            print(
                f"There are no .csv files in this folder [{csv_path}]. Please, try again!")
    print(csv_files)
    return csv_files


def show_logs():
    print("Show Logs")


def show_number_of_imported_records():
    print("Show number of imported records")


def show_file_details():
    print("Show file details")


def main_menu():
    opt = None
    while opt != 0:
        print("Select your option:")
        print()
        print("1 - Configure your database connection")
        print("2 - Load your csv files")
        print("3 - Import data")
        print("4 - Show logs")
        print("5 - Show number of imported records")
        print("6 - Show file details")  # file | qtd_records |
        print("0 - Exit")
        option = input()
        try:
            opt = int(option)
            if opt == 1:
                import_files(dbDetails, csv_files)
            elif opt == 2:
                get_csv_files()
            elif opt == 3:
                # import_files()
                get_csv_files()
                variavel = get_database_details()
                print(type(variavel))  # <class 'tuple'>
            elif opt == 4:
                show_logs()
            elif opt == 5:
                show_number_of_imported_records()
            elif opt == 6:
                show_file_details()
            elif opt == 0:
                print("Thank you.")
                # break
                sys.exit
            else:
                print(f"option {opt} out of the range. Try again!")
                opt = None
                time.sleep(1)
        except Exception as ex:
            #print(f"Option {option} is invalid. Try again!")
            print(f"Error: {ex}")


def main():
    print()
    print("************DATABASE IMPORT SYSTEM**************")
    print()
    print("Before we start, please: ")
    get_database_details()

    if (test_database_connection() == False):
        print("Something went wrong, please try again!")
        sys.exit()
    else:
        csv_files = get_csv_files()
    main_menu()


if __name__ == '__main__':
    main()
