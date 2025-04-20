import random
import string
import json

def generate_secure_password(password_length=12):
    valid_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(valid_chars) for _ in range(password_length))

def create_user_profile():
    names_list = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah"]
    surnames_list = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones"]
    
    full_name = f"{random.choice(names_list)} {random.choice(surnames_list)}"
    user_age = random.randint(18, 80)
    user_email = f"{full_name.lower().replace(' ', '.')}@example.com"
    user_password = generate_secure_password()
    
    return {
        "full_name": full_name,
        "age": user_age,
        "email": user_email,
        "password": user_password
    }

def handle_user_data(file_name="user_data.json"):
    profile_data = create_user_profile()
    
    with open(file_name, 'w') as data_file:
        json.dump(profile_data, data_file, indent=4)
    
    with open(file_name, 'r') as data_file:
        loaded_profile = json.load(data_file)
        print(json.dumps(loaded_profile, indent=4))

if __name__ == "__main__":
    handle_user_data()
