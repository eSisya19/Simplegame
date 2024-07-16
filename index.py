import streamlit as st
import random

# List of simpler, common words for the hangman game
WORDS = [
    "apple", "banana", "orange", "grape", "melon", "berry", "peach", "pear", "plum", "mango",
    "chair", "table", "sofa", "bed", "lamp", "shelf", "desk", "stool", "drawer", "couch",
    "dog", "cat", "fish", "bird", "horse", "cow", "sheep", "goat", "pig", "duck",
    "car", "bike", "bus", "train", "plane", "boat", "ship", "truck", "scooter", "taxi",
    "red", "blue", "green", "yellow", "black", "white", "pink", "purple", "brown", "orange",
    "sun", "moon", "star", "cloud", "rain", "snow", "wind", "storm", "lightning", "thunder",
    "happy", "sad", "angry", "excited", "bored", "tired", "scared", "brave", "shy", "proud"
]

# Function to initialize the game
def initialize_game():
    word = random.choice(WORDS)
    return word, ["_"] * len(word), [], 6  # word, guessed_word, guessed_letters, attempts_left

# Function to update the guessed word
def update_guessed_word(word, guessed_word, guessed_letters):
    for i, letter in enumerate(word):
        if letter in guessed_letters:
            guessed_word[i] = letter
    return guessed_word

# Streamlit application
def hangman_game():
    st.title("Hangman Game")

    if "game_state" not in st.session_state:
        st.session_state.game_state = initialize_game()

    word, guessed_word, guessed_letters, attempts_left = st.session_state.game_state

    st.write("Word to guess: " + " ".join(guessed_word))
    st.write(f"Attempts left: {attempts_left}")

    guess = st.text_input("Enter a letter:", max_chars=1).lower()

    if st.button("Guess"):
        if guess in guessed_letters:
            st.warning("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            guessed_word = update_guessed_word(word, guessed_word, guessed_letters)
            st.session_state.game_state = (word, guessed_word, guessed_letters, attempts_left)
        else:
            guessed_letters.append(guess)
            attempts_left -= 1
            st.session_state.game_state = (word, guessed_word, guessed_letters, attempts_left)

        if "_" not in guessed_word:
            st.success("Congratulations! You guessed the word: " + word)
            st.session_state.game_state = initialize_game()
        elif attempts_left == 0:
            st.error("Game Over! The word was: " + word)
            st.session_state.game_state = initialize_game()

    st.write("Guessed letters: " + ", ".join(guessed_letters))

if __name__ == "__main__":
    hangman_game()


# Footer
st.markdown("""<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 20%;
    background-color: cyan;
    color: black;
    text-align: center;
}
</style>
<div class="footer">
    <p>Developed by Eddie</p>
</div>
""", unsafe_allow_html=True)
