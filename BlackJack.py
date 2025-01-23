import random

# Function to calculate the score
def calculate_score(card_list):
    score = sum(card_list)
    # Adjust Ace (11) to 1 if score exceeds 21
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

# Ask the user if they want to play
play_game = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
if play_game != "yes":
    print("Maybe next time!")
    exit()

# List of cards, where 11 represents an Ace
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Initialize hands
user_cards = [random.choice(cards) for _ in range(2)]
computer_cards = [random.choice(cards) for _ in range(2)]

# Display initial cards
print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
print(f"Computer's first card: {computer_cards[0]}")

# User's turn
while True:
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if user_should_deal == "y":
        user_cards.append(random.choice(cards))
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        if user_score > 21:
            print("You went over 21. You lose!")
            exit()
    else:
        break

# Computer's turn
while calculate_score(computer_cards) < 17:
    computer_cards.append(random.choice(cards))

# Final scores
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

# Determine winner
if user_score > 21:
    print("You went over. You lose!")
elif computer_score > 21 or user_score > computer_score:
    print("You win!")
elif user_score < computer_score:
    print("You lose!")
else:
    print("It's a draw!")
