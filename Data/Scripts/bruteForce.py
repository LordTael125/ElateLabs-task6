import itertools
import string
import time

# Target password (for simulation)
target_password = "L34J"

# Character set to use (lowercase letters + digits)
charset = string.ascii_lowercase + string.digits + string.ascii_uppercase

# Max length of password to try
max_length = 4

def brute_force(target):
    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_str = ''.join(guess)
            attempts += 1
            if guess_str == target:
                elapsed = time.time() - start_time
                print(f"[+] Password found: {guess_str}")
                print(f"[+] Attempts: {attempts}")
                print(f"[+] Time taken: {elapsed:.2f} seconds")
                return guess_str

    print("[-] Password not found.")
    return None

# Run the brute force
brute_force(target_password)
