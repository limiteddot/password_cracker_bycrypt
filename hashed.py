import bcrypt

# Plain text password that you want to hash
plain_text_password = "PassWord"

# Hash the password using bcrypt
# bcrypt.gensalt() generates a random salt
# bcrypt.hashpw() combines the salt and the plaintext password to produce the bcrypt hash
hashed_password = bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt())

# Print the hashed password
print("Hashed Password:", hashed_password.decode())
