#Deep dive into dictionaries
#{key:value}
#example {"Leon": "German Shepard", "Odin": "German Shepard", "Clifford": "Big Red Dog"}
dog_dict = {
    "GSD" : "Leon",
    "Big Red Dog" : "Clifford",
    "Retreiver" : "Rusty"
}
dog_dict["Shitzu"] = "Greggory"
def entry_search():
    userSearch = input("What breed are you looking for?: ")
    if userSearch in dog_dict:
        name = dog_dict[userSearch]
        print(f"We found a match with {userSearch}")
        print(f"Name(s) on file for {userSearch}'s: {name}")
        search_again = input("Want to search again?(Y/n): ").lower()
        if search_again == "y":
            entry_search()
        else:
            print("Goodbye")
    else:
        print(f"No records match {userSearch}")
        search_again = input("Want to search again?(Y/n): ").lower()
        if search_again == "y":
            entry_search()
        else:
            print("Goodbye")
entry_search()


#add to the dictionary
#print(dog_dict)
#wipe existing dict
# dog_dict = {}
# print(dog_dict)
#edit an item in a dict
# dog_dict["GSD"] = "Odin"
# print(dog_dict["GSD"])
#loop through a dict
#--------------------------------------------------#
# Nesting lists in Dict, and Nesting Dicts in Dict #
#__________________________________________________#

travel_blog = {
    "France" : ["Paris", "Cafe", "Baguette"], #nested list
    "Germany" : "Berlin",
    "USA" : {
        "cities_visited" : ["Milwaukee", "Chicago", "Maine", "Cranton"], "total_visits" : 13
        }
}
# print(travel_blog["USA"])
#nesting a dict inside a list
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#at first i tried travel_log[0][country] = country live and you learn right
def add_new_country(country, int, cities):
    travel_log.append(
        {
            "country" : country,
            "visits" : int,
            "cities" : cities
        }
    )
    

add_new_country("Russia", 2, ["Moscow", "St.Peter"])
#print(travel_log)

