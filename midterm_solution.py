#Function to handle the sports tracker
def intramurals_tracker():

    # Ask section name
    section_name = input("Enter class section name: ")
    while section_name == "" or section_name == " ":
        print("Invalid input!")
        section_name = input("Enter class section name: ")

    # Ask coordinator name
    coordinator_name = input("Enter coordinator name: ")
    while coordinator_name == "" or coordinator_name == " ":
        print("Invalid input!")
        coordinator_name = input("Enter coordinator name: ")

    # Sports list
    sports_list = [
        ["Basketball", "Team"],
        ["Volleyball", "Team"],
        ["Badminton", "Individual"],
        ["Chess", "Individual"],
        ["Table Tennis", "Individual"]
    ]

    # Display sports events
    print("\n==========================================")
    print("   INTRAMURALS -- SPORTS EVENTS")
    print("==========================================")

    for i in range(len(sports_list)):
        print(f"{i+1}. {sports_list[i][0]:13} [{sports_list[i][1]}]")

    total_points = 0
    games = []

    # Accept 4 game entries
    for game_num in range(1, 5):

        print(f"\n--- GAME {game_num} ---")

        while True:
            sport_input = input("Sport number (0 to skip): ")

            if sport_input == "0":
                sport_number = 0
                break
            elif sport_input == "1":
                sport_number = 1
                break
            elif sport_input == "2":
                sport_number = 2
                break
            elif sport_input == "3":
                sport_number = 3
                break
            elif sport_input == "4":
                sport_number = 4
                break
            elif sport_input == "5":
                sport_number = 5
                break
            else:
                print("Invalid number!")

        if sport_number == 0:
            continue

        # FIXED OPONENT VALIDATION (NO strip, NO replace)
        while True:
            opponent = input("Opposing section: ")

            if opponent == "":
                print("Invalid input!")
            elif opponent == " ":
                print("Invalid input!")
            elif opponent == '"':
                print("Invalid input!")
            else:
                break

        # Result input validation
        result = input("Result (W/L): ")
        while result != "W" and result != "L":
            print("Invalid letter!")
            result = input("Result (W/L): ")

        # Points system
        if result == "W":
            points = 3
            status = "WIN"
        else:
            points = 0
            status = "LOSS"

        total_points += points

        # Save game
        games.append([
            sports_list[sport_number - 1][0],
            sports_list[sport_number - 1][1],
            opponent,
            status,
            points
        ])

    # Determine standing
    if total_points >= 9:
        standing = "GOLD CONTENDER"
    elif total_points >= 6:
        standing = "SILVER PUSH"
    else:
        standing = "KEEP FIGHTING!"

    # Output board
    print("\n=============================================")
    print(f"   {section_name} -- GAME RESULTS BOARD")
    print("=============================================")
    print("Coordinator :", coordinator_name)
    print("---------------------------------------------")

    for idx in range(len(games)):
        print(f"[{idx+1}] {games[idx][0]:13} [{games[idx][1]}]")
        print(f"    vs {games[idx][2]} | Result: {games[idx][3]:4} | Points: {games[idx][4]}")
        print()

    print("---------------------------------------------")
    print("Total Points :", total_points)
    print("Standing     :", standing)
    print("=============================================")


# Run program
intramurals_tracker()
