
def import_files():
    pass


def show_logs():
    pass


def show_number_of_imported_records():
    pass


def show_file_details():
    pass


def main():
    pass


def main_menu():
    opt = 5
    while opt != 0:
        print("Select your option:")
        print("1 - Import files")
        print("2 - Show logs")
        print("3 - Show number of imported records")
        print("4 - Show file details")  # file | qtd_records |
        print("0 - Exit")
        try:
            opt = int(input())
        except:
            print(f"Option {0} is invalid", opt)

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
        print(f"option {0} out of the range. Try again.", opt)


if __name__ == '__main__':
    main_menu()
