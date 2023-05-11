import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_user_choice(self):
        """Prompt the user for their choice and return it."""
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
        if user_choice.lower() not in self.choices:
            print("Invalid choice. Please try again.")
            return self.get_user_choice()
        return user_choice.lower()

    def get_computer_choice(self):
        """Generate and return the computer's choice."""
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        """Determine and announce the winner."""
        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
            print(f"Congratulations! {user_choice} beats {computer_choice}. You win!")
        else:
            print(f"Sorry, {computer_choice} beats {user_choice}. You lose.")

    def main(self):
        """Main game loop."""
        print("Welcome to Rock, Paper, Scissors!")
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            self.determine_winner(user_choice, computer_choice)

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                print("Thanks for playing! Goodbye.")
                break

if __name__ == "__main__":
    game = RockPaperScissors()
    game.main()

