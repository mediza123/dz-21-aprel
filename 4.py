import random
from array import array
from datetime import datetime, timedelta

def generate_random_dates(total=10):
    today = datetime.now()
    five_years_ago = today - timedelta(days=5*365)
    
    date_sequence = array('d')
    for _ in range(total):
        random_days = random.randint(0, (today - five_years_ago).days)
        random_date = (five_years_ago + timedelta(days=random_days)).date()
        date_sequence.append(random_date.toordinal())
    
    return date_sequence

def show_date_gaps(date_records):
    for i in range(len(date_records) - 1):
        first_moment = datetime.fromordinal(int(date_records[i])).date()
        second_moment = datetime.fromordinal(int(date_records[i+1])).date()
        gap = abs((second_moment - first_moment).days)
        print(f"Интервал между {first_moment} и {second_moment}: {gap} суток")

if __name__ == "__main__":
    date_collection = generate_random_dates()
    show_date_gaps(date_collection)
