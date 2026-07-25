def main_menu():
    print("-" * 30)
    print("========KIDUS GRAND HOTEL🏩=========")
    print("-" * 30)
    print("WELCOME💐")
    print("=Main Menu=")
    print("1. Add Room")
    print("2. View Room")
    print("3. Remove Room")
    print("4. Book Room")
    print("5. Cancel Reservation")
    print("6. View Reservation")
    print("7. Search Customer")
    print("8. Hotel Statstics")
    print("9. Exit❌")

    choice = int(input("Enter your choice: "))
    return choice


def add_room():
    room_number = int(input("Enter a room number: "))