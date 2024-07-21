# Run pip show countryinfo to check library version
# Run pip list to see the version of every library in our PC
# This program will return info of the country selected from the user input
# This is a simple program, everything is in the library

# Run python.exe -m pip install --upgrade pip --user to upgrade pip tool
# This Python version (3.12) did not had countryinfo installed which cause the problem
# Run pip install countryinfo --user to solve the problem

from countryinfo import CountryInfo

name_of_country = input("Enter your country: ")

country = CountryInfo(name_of_country)

print(f"Official Name: {country.name()}")
print(f"Capital: {country.capital()}")
print(f"Population: {country.population()}")
print(f"Area: {country.area()} square kilometers")
print(f"Region: {country.region()}")
print(f"Borders: {', '.join(country.borders())}")
print(f"Timezones: {', '.join(country.timezones())}")
print(f"Calling Code: {', '.join(country.calling_codes())}")
print(f"Currency: {country.currencies()}")
print(f"Language: {', '.join(country.languages())}")