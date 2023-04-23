# Importing necessary modules
import csv
import os
import random

villagers_csv = "villagers.csv"
# Define the global variables
favorite_villagers = []


# Defining the main function
def main():
    # Clearing the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Animal Crossing Village Manager")

    print("1. Favorites: view villagers in your town")
    print("2. View: view a list of all villagers")
    print("3. Search: Search for a specific villager by name")
    print("4. Random: Generate a random villager")
    print("5. Information: More information about the program")
    print("6. Exit: Exit program")

    # Getting user input
    choice = input("Enter your choice: ")

    # Handling user input
    if choice == "1":
        view_favorite_villagers()
    elif choice == "2":
        view_villagers()
    elif choice == "3":
        search_villager()
    elif choice == "4":
        generate_random_villager()
    elif choice == "5":
        information()
    elif choice == "6":
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()


# Defining the add_villager function
def view_favorite_villagers():
    # Print favorite villager details
    if len(favorite_villagers) == 0:
        print("No favorite villagers found.")
    else:
        print("Name\tSpecies\t\tGender")
        print("----------------------------------------")
        for villager in favorite_villagers:
            print(f"{villager[0]}\t{villager[1]}\t\t{villager[2]}")

    # Ask user if they want to go back to main menu
    input("Press Enter to go back to main menu.")
    main()


# Defining the view_villagers function
def view_villagers():
    # Read villager details from CSV file
    with open(villagers_csv, "r", newline='') as file:
        reader = csv.reader(file)
        villagers = list(reader)

    # Print villager details
    if len(villagers) == 0:
        print("No villagers found.")
    else:
        print("Name\tSpecies\t\tGender")
        print("----------------------------------------")
        for index, villager in enumerate(villagers):
            print(f"{index + 1}. {villager[0]}\t{villager[1]}\t\t{villager[2]}")

    # Ask user if they want to add a villager to favorites or go back to main menu
    choice = input(
        "Enter the number of the villager you want to add to favorites, or press Enter to go back to main menu: ")
    if choice.isdigit() and int(choice) <= len(villagers):
        favorite_villagers.append(villagers[int(choice) - 1])
        print(f"{villagers[int(choice) - 1][0]} has been added to your favorites.")
        input("Press Enter to go back to main menu.")
        main()
    else:
        main()


# Defining the search_villager function
def search_villager():
    # Getting search query from user
    query = input("Enter villager name or species to search: ")

    # Searching for villager details in file
    with open(villagers_csv, "r", newline='') as file:
        reader = csv.reader(file)
        villagers = list(reader)
    search_results = []
    for villager in villagers:
        name, species, gender = villager.strip().split(",")
        if query.lower() in name.lower() or query.lower() in species.lower():
            search_results.append((name, species, gender))

    # Printing search results
    if len(search_results) == 0:
        print("No search results found.")
    else:
        print("Search Results")
        print("Name\tSpecies\t\tPersonality")
        print("----------------------------------------")
        for result in search_results:
            name, species, gender = result
            print(f"{name}\t{species}\t\t{gender}")

    # Asking user if they want to search again or go back to main menu
    choice = input("Do you want to search again or go back to main menu? (Y/main): ")
    if choice == "yes" or "Y" or "Yes":
        search_villager()
    else:
        main()


def information():
    print("CSV Sourced from: "
        "https://huggingface.co/datasets/osanseviero/kaggle-animal-crossing-new-horizons-nookplaza-dataset/blob/main/villagers.csv")
    print("© Lindsey Larvick, 2023")


def generate_random_villager():
    # Read villager details from CSV file
    with open(villagers_csv, "r", newline='') as file:
        reader = csv.reader(file)
        villagers = list(reader)

    # Generate a random villager
    random_villager = random.choice(villagers)

    # Print the random villager
    print(f"Name: {random_villager[0]}")
    print(f"Species: {random_villager[1]}")
    print(f"Gender: {random_villager[2]}")

    # Ask user if they want to go back to main menu
    input("Press Enter to go back to main menu.")
    main()


if __name__ == '__main__':
    main()
