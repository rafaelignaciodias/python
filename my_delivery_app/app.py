import os

places = []


def show_header():
    print("""
    ███╗░░░███╗██╗░░░██╗██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗░█████╗░██████╗░██████╗░
    ████╗░████║╚██╗░██╔╝██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗
    ██╔████╔██║░╚████╔╝░██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░███████║██████╔╝██████╔╝
    ██║╚██╔╝██║░░╚██╔╝░░██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░██╔══██║██╔═══╝░██╔═══╝░
    ██║░╚═╝░██║░░░██║░░░██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░██║░░██║██║░░░░░██║░░░░░
    ╚═╝░░░░░╚═╝░░░╚═╝░░░╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░      
    """)


def show_menu():
    print("1. register place")
    print("2. list place")
    print("3. enable place")
    print("4. exit\n")


def choose_menu_option():
    try:
        option = int(input("choose an option: "))
        if option == 1:
            register_place()
        elif option == 2:
            list_place()
        elif option == 3:
            print("enable place")
        else:
            finish_app()

    except ValueError as e:
        invalid_option()
        return


def register_place():
    show_subtitles("register place")

    place_name = input("\nplace name: ")
    places.append(place_name)
    print(f"\nplace {place_name} registered.")

    return_menu()


def list_place():
    show_subtitles("list place")
    print()

    for place in places:
        print(place)

    return_menu()


def invalid_option():
    print("you chose an invalid option\n")

    return_menu()


def finish_app():
    show_subtitles("finishing my delivery app")


def show_subtitles(title):
    os.system("clear")
    print(title)


def return_menu():
    input("press enter to return")
    main()


def main():
    os.system("clear")
    show_header()
    show_menu()
    choose_menu_option()


if __name__ == "__main__":
    main()
