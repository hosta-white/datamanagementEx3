import random

# Function to simulate a coin toss
def toss_coin():
    return random.choice(["Heads", "Tails"])

# Variables to count the number of heads and tails
heads_count = 0
tails_count = 0

# Simulate three rounds of coin tossing
print("Tossing a coin...")
for round in range(1, 4):
    result = toss_coin()
    if result == "Heads":
        heads_count += 1
    else:
        tails_count += 1
    print(f"Round {round}: {result}")

# Print the final count of heads and tails
print(f"Heads: {heads_count}, Tails: {tails_count}")
if heads_count > tails_count:
    print("You won!")
else:
    print("You lost!")