from mysql.connector import MySQLConnection, Error
from datetime import date
import sys
import csv
import os


def get_database_details():
    print("Import files")
    print("Inform the database IP: ")
    database_ip = input()
    print("Inform the database Name: ")
    database_name = input()
    print("Inform the database user: ")
    database_user = input()
    print("Inform the database password: ")
    database_password = input()
    return database_ip, database_name, database_user, database_password


def import_files():
    # establishing  the connection
    db_details = get_database_details
    conn = MySQLConnection(
        user='vcleber',
        password='795641',
        host='192.168.1.83',
        database="casestudy1"
    )

    # creating a cursor object using the cursor() method
    cursor = conn.cursor()


def get_csv_files():
    csv_files = None
    print("Inform where the files (.csv) are: ")
    path = input()
    dir_list = os.listdir(path)
    for x in dir_list:
        if x.endswith(".csv"):
            print(x)
            csv_files = path + "\\" + x
    print(csv_files)
    return csv_files


def show_logs():
    print("Show Logs")


def show_number_of_imported_records():
    print("Show number of imported records")


def show_file_details():
    print("Show file details")


def main():
    print("Main method")


def main_menu():
    opt = None
    while opt != 0:
        print("Select your option:")
        print("1 - Import files")
        print("2 - Show logs")
        print("3 - Show number of imported records")
        print("4 - Show file details")  # file | qtd_records |
        print("0 - Exit")
        option = input()
        try:
            opt = int(option)
            if opt == 1:
                import_files()
                #variavel = get_database_details()
                # print(type(variavel))
            elif opt == 2:
                show_logs()
            elif opt == 3:
                show_number_of_imported_records()
            elif opt == 4:
                show_file_details()
            elif opt == 0:
                print("Thank you.")
                break
            else:
                print(f"option {opt} out of the range. Try again!")
                opt = None
        except:
            print(f"Option {option} is invalid. Try again!")


if __name__ == '__main__':
    main_menu()
