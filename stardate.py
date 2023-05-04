import datetime

def days_since_year_0(date):
    year_0 = datetime.date(1, 1, 1)
    delta = date - year_0
    return delta.days - 1  # Subtract 1 to account for the year 0 not existing in the Gregorian calendar

def stardate_from_date(date):
    days = days_since_year_0(date)
    stardate_units_per_day = 2.7378
    stardate = days * stardate_units_per_day
    return stardate

def current_century():
    today = datetime.date.today()
    return (today.year - 1) // 100 + 1  # Subtract 1 to account for the year 0 not existing in the Gregorian calendar

def format_stardate_with_century(stardate, century):
    stardate_str = f"{century}{stardate:07.1f}"
    return stardate_str

def current_stardate():
    today = datetime.date.today()
    return stardate_from_date(today)

if __name__ == "__main__":
    stardate = current_stardate()
    century = current_century()
    stardate_with_century = format_stardate_with_century(stardate, century)
    print(f"Current stardate (with century prefix): {stardate_with_century}")
