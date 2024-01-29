import sys

def lookup_team_player_in_directory(roster, name):
    if name in roster:
        return roster[name]
    else:
        return "N/A"

def add_player_to_team_directory(roster, name, stats):
    if name in roster:
        print(f"Error: {name} is already in the roster.")
        return roster
    else:
        roster[name] = stats
        return roster

def delete_player_from_directory(roster, name):
    if name not in roster:
        print(f"Error: {name} is not in the roster.")
        return roster
    else:
        del roster[name]
        return roster

def main():
    # initial roster
    brave_roster = {
        "Austin Riley": "AB: 615, R: 90, H: 168, HR: 38, AVG: 0.273",
        "Ronald Acuna": "AB: 467, R: 71, H: 124, HR: 15, AVG: 0.266",
    }

    # display menu and get user input
    while True:
        print("\nMenu:")
        print("1. Look up a player's stats")
        print("2. Add a player to the roster")
        print("3. Remove a player from the roster")
        print("4. Quit")

        choice = input("Enter your selection (1-4): ")

        if choice == "1":
            name = input("Enter the player's name: ")
            stats = lookup_team_player_in_directory(brave_roster, name)
            print(f"\n{name}: {stats}")
        elif choice == "2":
            name = input("Enter the player's name: ")
            stats = input("Enter the player's stats: ")
            brave_roster = add_player_to_team_directory(brave_roster, name, stats)
            print("\nUpdated roster:")
            for name, stats in brave_roster.items():
                print(f"{name}: {stats}")
        elif choice == "3":
            name = input("Enter the player's name: ")
            brave_roster = delete_player_from_directory(brave_roster, name)
            print("\nUpdated roster:")
            for name, stats in brave_roster.items():
                print(f"{name}: {stats}")
        elif choice == "4":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
