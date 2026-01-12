# Simple Deal or no Deal style game with cases as a list. 
import random

# ---------- HELPER FUNCTION ----------
def get_valid_case(prompt, num_cases, opened, player_case):
    while True:
        user_input = input(prompt)

        # Check if input is numeric
        if not user_input.isdigit():
            print("Please enter a number.")
            continue

        choice = int(user_input) - 1

        # Check range
        if choice < 0 or choice >= num_cases:
            print("Number out of range.")
            continue

        # Prevent choosing own case
        if choice == player_case:
            print("You cannot choose your own case.")
            continue

        # Prevent reopening cases
        if opened[choice]:
            print("That case is already opened.")
            continue

        return choice


# ---------- GAME SETUP ----------
cases = [
    0.10, 1, 5, 10, 50,
    100, 200, 300,
    400, 500, 750,
    1000, 5000, 10000,
    50000, 100000, 200000,
    300000, 400000, 500000, 750000, 1000000
]

num_cases = len(cases)

# Simple shuffle (MicroPython-safe)
for i in range(num_cases):
    j = random.randint(0, num_cases - 1)
    cases[i], cases[j] = cases[j], cases[i]

opened = [False] * num_cases

print("🎲 DEAL OR NO DEAL 🎲")
print("Choose from 22 briefcases (1–22)")

# ---------- PLAYER CHOOSES CASE ----------
while True:
    user_input = input("Select your case: ")

    if not user_input.isdigit():
        print("Please enter a number.")
        continue

    player_case = int(user_input) - 1

    if 0 <= player_case < num_cases:
        break

    print("Number out of range.")

print("You chose case", player_case + 1)

# ---------- ROUND STRUCTURE ----------
rounds = [6, 5, 4, 3, 2, 1]


# ---------- GAME LOOP ----------
for round_num in range(len(rounds)):
    print("\n--- ROUND", round_num + 1, "---")

    for _ in range(rounds[round_num]):
        choice = get_valid_case(
            "Open a case: ",
            num_cases,
            opened,
            player_case
        )

        opened[choice] = True
        print("Case", choice + 1, "contained $", cases[choice])

    # ---------- BANKER OFFER ----------
    total = 0
    count = 0

    for i in range(num_cases):
        if not opened[i] and i != player_case:
            total += cases[i]
            count += 1

    offer = total // count
    print("\n💼 BANKER OFFER: $", offer)

    decision = input("Deal or No Deal? (d/n): ").lower()

    if decision == "d":
        print("\n✅ DEAL!")
        print("You won $", offer)
        print("Your case contained $", cases[player_case])
        break
else:
    # ---------- FINAL REVEAL ----------
    print("\n🎉 FINAL CASE 🎉")
    print("Your case contained $", cases[player_case])
