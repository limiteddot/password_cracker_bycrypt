import bcrypt


# Function to read words from a dictionary file
def read_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


# Function to hash a password using bcrypt
def hash_password(password):
    # Generate a salt using bcrypt's gensalt() function
    salt = bcrypt.gensalt()
    # Hash the password using the salt
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


# Function to crack a password hash using the dictionary
def crack_password(target_hash, dictionary):
    for word in dictionary:
        # Compare the hashed dictionary word with the target hash
        if bcrypt.checkpw(word.encode(), target_hash):
            return word
    return None


if __name__ == "__main__":
    # Example target hash (hashed version of a sample password)
    target_hash = b'$2b$12$D1evuoukI1fO76/HOyzqa.JLGkqG8WeRGzlB.09TG.1JRmQpe.e1e'
    dictionary_file = "dictionary.txt"

    # Read words from the dictionary file
    dictionary = read_dictionary(dictionary_file)

    # Attempt to crack the password using the dictionary
    cracked_password = crack_password(target_hash, dictionary)

    if cracked_password:
        print("The cracked password is:", cracked_password)
    else:
        print("Password is not in the dictionary")
