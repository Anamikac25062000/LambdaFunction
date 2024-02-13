#Write a Python program to extract year, month, date and time using Lambda. 
# Sample Output: 
# 2020-01-15 09:03:32.744178 
# 2020 
# 1 
# 15 
# 09:03:32.744178 

from datetime import datetime

extract_info = lambda timestamp: (
    timestamp.year,
    timestamp.month,
    timestamp.day,
    timestamp.strftime("%H:%M:%S.%f")
)
sample_timestamp = "2020-01-15 09:03:32.744178"

formatted_timestamp = datetime.strptime(sample_timestamp, "%Y-%m-%d %H:%M:%S.%f")

year, month, day, time = extract_info(formatted_timestamp)

print(sample_timestamp)
print(year)
print(month)
print(day)
print(time)
