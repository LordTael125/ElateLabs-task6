from pathlib import Path
# Simulated password
target_password = "letmein"


def load_wordlist(file_path):
    with open(file_path, 'r', encoding='latin-1') as f:
        return [line.strip() for line in f]

def dictionary_attack(target, wordlist):
    for attempt, word in enumerate(wordlist, 1):
        if word == target:
            print(f"[+] Password found: {word}")
            print(f"[+] Attempts: {attempt}")
            return word
    print("[-] Password not found in dictionary.")
    return None


# Get the directory of the current script
script_dir = Path(__file__).resolve().parent

# Build full path to dictionary file
dictionary_path = script_dir / "dictionary.txt"

# Sample dictionary list
dictionary = load_wordlist(dictionary_path)

# Run the attack
dictionary_attack(target_password, dictionary)