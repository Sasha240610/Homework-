import re
import requests
from collections import defaultdict

# Функція для зчитування та обробки даних

def read_data_from_github(url):
    pattern = r"username: (?P<username>\w+), email: (?P<email>[\w@.]+), date_connected: (?P<date_connected>\d{2}/\d{2}/\d{4} \d{2}:\d{2}), ip: (?P<ip>[.\d]+), connection_duration: (?P<duration>[\d:]+)"
    data = []
    response = requests.get(url)
    if response.status_code == 200:
        for line in response.text.splitlines():
            match = re.match(pattern, line)
            if match:
                data.append(match.groupdict())
    else:
        print("Error fetching data from GitHub:", response.status_code)
    return data

# Завдання 1: Період статистики
def get_date_range(data):
    dates = [entry['date_connected'].split(' ')[0] for entry in data]
    return [min(dates), max(dates)]

# Завдання 2: Унікальні користувачі
def count_unique_users(data):
    users = {entry['username'] for entry in data}
    return len(users)

# Завдання 3: Кількість підключень для кожного користувача
def count_user_connections(data):
    connections = defaultdict(int)
    for entry in data:
        connections[entry['username']] += 1
    return dict(connections)

# Завдання 4: Унікальні IP для кожного користувача
def unique_ips_per_user(data):
    ips = defaultdict(set)
    for entry in data:
        ips[entry['username']].add(entry['ip'])
    return {user: list(ip_set) for user, ip_set in ips.items()}

# Завдання 5: Кількість унікальних IP для кожного користувача
def count_unique_ips_per_user(data):
    unique_ips = unique_ips_per_user(data)
    return {user: len(ips) for user, ips in unique_ips.items()}

# Завдання 6: Загальний час підключення в секундах для кожного користувача
def total_connection_time(data):
    def time_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds

    durations = defaultdict(int)
    for entry in data:
        durations[entry['username']] += time_to_seconds(entry['duration'])
    return dict(durations)

# Основний блок
url = 'https://raw.githubusercontent.com/VolodymyrZontov/LIT_python_intro/main/Homeworks/test_logs.txt'
data = read_data_from_github(url)

# Результати
date_range = get_date_range(data)
unique_users = count_unique_users(data)
user_connections = count_user_connections(data)
unique_ips = unique_ips_per_user(data)
unique_ip_counts = count_unique_ips_per_user(data)
total_durations = total_connection_time(data)

# Виведення результатів
print("1. Період статистики:", date_range)
print("2. Кількість унікальних користувачів:", unique_users)
print("3. Кількість підключень для кожного користувача:", user_connections)
print("4. Унікальні IP для кожного користувача:", unique_ips)
print("5. Кількість унікальних IP для кожного користувача:", unique_ip_counts)
print("6. Загальний час підключення в секундах:", total_durations)
