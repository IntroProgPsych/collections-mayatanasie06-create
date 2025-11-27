# https://www.w3schools.com/python/python_dictionaries.asp

#  You are given this dictionary:
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
#     "Spain": "Madrid"
# }
#
# Write a function get_capital(country, capitals_dict) that:
#   - returns the capital of the given country
#   - returns "Unknown" if the country is not in the dictionary
#
# Ask the user for a country name and print the returned value.
# 
# Write your code here:

country=input("country name:")
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid"
}
def get_capital(country,capitals):
    if country in capitals:
        return capitals[country]
    else:
        return("Unknown")
    
print(get_capital(country,capitals))