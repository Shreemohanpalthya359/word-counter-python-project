import re

def word_counter(text):
    """
    Count the frequency of each word in the given text.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    # Convert the text to lowercase to make the count case-insensitive
    text = text.lower()

    # Remove punctuation from the text
    text = re.sub(r'[^\w\s]', '', text)

    # Split the text into words
    words = text.split()

    # Create a dictionary to store word frequencies
    word_count = {}

    # Count the frequency of each word
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def display_word_count(word_count):
    """
    Display the word count results.

    Args:
        word_count (dict): A dictionary with words and their counts.
    """
    print("\nWord Count Results:")
    if word_count:
        for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            print(f"'{word}': {count}")
    else:
        print("No words found.")

def main():
    print("Welcome to the Word Counter!")
    print("Please enter a text to count the frequency of each word.")

    while True:
        try:
            # Take user input
            user_input = input("\nEnter your text here: ")

            # Validate input for non-empty content
            if not user_input.strip():
                raise ValueError("Input cannot be empty.")

            # Process the input and count words
            word_count = word_counter(user_input)

            # Display the results
            display_word_count(word_count)

            # Exit the loop after successful processing
            break

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
