# Program to Calculate User's current age and month


current_year = 2023
birth_year = int(input('Enter your year of birth: '))
birth_month = int(input('Enter your month of birth (1-12): '))
current_month = 4  # assuming the current month is April

if birth_month > current_month:
    age_in_years = current_year - birth_year - 1
    age_in_months = 12 - birth_month + current_month
else:
    age_in_years = current_year - birth_year
    age_in_months = current_month - birth_month

print(f"You are {age_in_years} years and {age_in_months} months old.")
