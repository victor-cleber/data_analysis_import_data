
def import_files():
    print("Import files")


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
