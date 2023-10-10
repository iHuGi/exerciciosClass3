
"""
1. Defina um nome de utilizador e uma palavra-passe válidos
2. Solicite ao utilizador que insira um nome de utilizador.
3. Use uma estrutura condicional para verificar se o nome de utilizador fornecido pelo utilizador é igual ao utilizador Valido.
4. Se o nome de utilizador estiver correto, solicite ao utilizador que insira a palavra-passe.
5. Use outra estrutura condicional para verificar se a palavra-passe fornecida pelo utilizador é igual à palavra Passe Valida.
6. Se a palavra-passe estiver correta, exiba uma mensagem de "Login bem-sucedido". Caso contrário, exiba uma mensagem de "Palavra-passe incorreta".
7. Se o nome de utilizador estiver incorreto, exiba uma mensagem de "Nome de utilizador incorreto".
"""

# VERSION 1
print("VERSION 1")
# Dummy data for the user dictionary
user_data = {
    'userID1': {'username': 'Hugo', 'email': 'Hugo@gmail.com', 'password': 'abc123*'},
    'userID2': {'username': 'André', 'email': 'André@gmail.com', 'password': 'abc123*'},
    'userID3': {'username': 'Pedro', 'email': 'Pedro@gmail.com', 'password': 'abc123*'},
    'userID4': {'username': 'Tânia', 'email': 'Tânia@gmail.com', 'password': 'abc123*'},
    'userID5': {'username': 'Luís', 'email': 'Luís@gmail.com', 'password': 'abc123*'}
}

try:
    # Ask the user for input
    username = input("Enter your username: ")
    
    # Check if the entered username exists in the dictionary
    for user_id, user_info in user_data.items():
        print(f"ID: {user_id}, Info for each ID: {user_info}") # DEBUG (Check if loop is returning values)
        if user_info['username'] == username:
            password = input("Enter your password: ")
            # Check if the entered password matches the stored password
            if password == user_info['password']:
                print("Logging in...")
                break
            else:
                raise ValueError("Invalid password")
    else:
        raise ValueError("Invalid username")
except ValueError as e:
    print(f"Login failed: {e}")


print("")


# VERSION 2 with extra security, in a ideal world the passwords are stored in a database and not here
print("VERSION 2")
import bcrypt
print(f" bcrypt version: {bcrypt.__version__}")


# bcrypt takes the string 'abc123*' and encodes it into bytes using UTF-8 encoding, 
# then generates a salt (a random value used in the hashing process) using bcrypt.gensalt(). 
# Finally, it computes the password hash using the bcrypt algorithm.

#.decode('utf-8'): After generating the password hash, 
# it decodes it from bytes back into a UTF-8 encoded string. 
# This is typically done to store the hash as a string in a database or file.

# Dummy data for the user dictionary
user_data = {
    'userID1': {'username': 'Hugo', 'email': 'Hugo@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')},
    'userID2': {'username': 'André', 'email': 'André@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')},
    'userID3': {'username': 'Pedro', 'email': 'Pedro@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')},
    'userID4': {'username': 'Tânia', 'email': 'Tânia@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')},
    'userID5': {'username': 'Luís', 'email': 'Luís@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')}
}

try:
    # Ask the user for input
    username = input("Enter your username: ")
    
    # Check if the entered username exists in the dictionary
    for user_id, user_info in user_data.items():
        if user_info['username'] == username:
            password = input("Enter your password: ")
            # Hash the entered password and check if it matches the stored password hash
            if bcrypt.checkpw(password.encode('utf-8'), user_info['password_hash'].encode('utf-8')):
                print("Logging in...")
                break
            else:
                raise ValueError("Invalid password")
    else:
        raise ValueError("Invalid username")
except ValueError as e:
    print(f"Login failed: {e}")


print("")


# VERSION 3, this is a simpler version
print("VERSION 3")
username_expected = 'Hugo'
password_expected = 'abc123*'

username = input("Enter your username: ")

if username == username_expected:
    password = input("Enter your password: ")
    if (password == password_expected):
        print("Logging in...")
    else:
        print("Invalid password")
else:
    print("Invalid username")


print("")


# VERSION 4, limit the number of attempts a user can insert a password
print("VERSION 4")
import bcrypt

# Dummy data for the user dictionary
user_data = {
    'userID1': {'username': 'Hugo', 'email': 'Hugo@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')},
    'userID2': {'username': 'André', 'email': 'André@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')},
    'userID3': {'username': 'Pedro', 'email': 'Pedro@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')},
    'userID4': {'username': 'Tânia', 'email': 'Tânia@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')},
    'userID5': {'username': 'Luís', 'email': 'Luís@gmail.com', 'password_hash': bcrypt.hashpw('abc123*'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')}
}

max_attempts = 5
tries = 0

while tries < max_attempts:
    try:
        # Ask the user for input
        username = input("Enter your username: ")
        
        # Check if the entered username exists in the dictionary
        for user_id, user_info in user_data.items():
            if user_info['username'] == username:
                password = input("Enter your password: ")
                # Check if the entered password matches the stored password
                if bcrypt.checkpw(password.encode('utf-8'), user_info['password_hash'].encode('utf-8')):
                    print("Logging in...")
                    break
                else:
                    raise ValueError("Invalid password")
        else:
            raise ValueError("Invalid username")
    except ValueError as e:
        if "Invalid password" == str(e):
            print(f"Login failed: {e}")
            tries += 1
            tries_left = max_attempts - tries
            if tries_left > 0:
                print(f"Invalid password. You have {tries_left} {'tries' if tries_left > 1 else 'try'} left.")
            else:
                max_attempts_reached = "You have exceeded the maximum number of attempts."
        else:
            print(f"Login failed: {e}")

print(f"Account blocked. Reason: {max_attempts_reached}")