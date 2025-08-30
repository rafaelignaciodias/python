import os

# places = []
places = [
    {"name": "name 1", "category": "category 1", "active": False},
    {"name": "name 3", "category": "category 2", "active": False},
    {"name": "name 3", "category": "category 3", "active": True},
]


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
            change_place_status()
        else:
            finish_app()

    except ValueError as e:
        invalid_option()
        return


def register_place():
    show_subtitles("register place")

    place_name = input("\nplace name: ")
    place_category = input("\nplace category: ")
    place_active = False

    places.append(
        {"name": place_name, "category": place_category, "active": place_active}
    )
    print(f"\nplace {place_name} registered.")

    return_menu()


def list_place():
    show_subtitles("list place")
    print()

    for place in places:
        place_name = place["name"]
        place_category = place["category"]
        place_active = place["active"]
        print(
            f"name: {place_name} - category: {place_category} - active: {place_active}"
        )

    return_menu()


def change_place_status():
    show_subtitles("change place status")
    print()

    place_name = input("\nplace name: ")
    is_place_found = False

    for place in places:
        if place_name == place["name"]:
            place["active"] = not place["active"]
            is_place_found = True
            break

    if not is_place_found:
        print("place not found")

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
    input("press enter to return ")
    main()


def main():
    os.system("clear")
    show_header()
    show_menu()
    choose_menu_option()


if __name__ == "__main__":
    main()
