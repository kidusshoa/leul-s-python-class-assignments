import datetime

def is_valid_date(date_str):
    try:
        month, day, year = map(int, date_str.split('/'))
        datetime.date(year, month, day)
        return f"{date_str} is a valid date."
    except ValueError:
        return f"{date_str} is NOT a valid date."

# Example test cases
print(is_valid_date("5/24/1962"))  # Valid
print(is_valid_date("9/31/2000"))  # Invalid
