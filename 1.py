import random
import string
from pathlib import Path

def generate_random_filename(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length)) + '.txt'

def create_random_files(directory, count=10):
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)  
    
    files = []
    for _ in range(count):
        filename = generate_random_filename()
        file_path = dir_path / filename
        file_path.touch() 
        files.append(file_path)
    
    return files
