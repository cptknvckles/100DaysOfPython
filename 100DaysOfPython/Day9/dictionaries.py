#Deep dive into dictionaries
#{key:value}
#example {"Leon": "German Shepard", "Odin": "German Shepard", "Clifford": "Big Red Dog"}
dog_dict = {
    "GSD" : "Leon",
    "Big Red Dog" : "Clifford",
    "Retreiver" : "Rusty"
}
#userSearch = input("What key are you looking for? ")
# for i in dog_dict[1] : 
#     i = userSearch
#     print(i)
# print(dog_dict["GSD"])
#add to the dictionary
# dog_dict["Shitzu"] = "Greggory"
# print(dog_dict)
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
        "country" : "France", 
        "cities_visited" : ["Paris", "Cafe", "Baguette"],
        "times_visited" : 12
    },
    {
        "country" : "USA", 
        "cities_visited" : ["Milwaukee", "Chicago", "Maine", "Cranton"],
        "times_visited" : 89
    }
]

print(travel_log[1]["times_visited"])

