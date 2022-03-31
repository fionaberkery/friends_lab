def get_name(person):
    return person["name"] 

def get_favourite_tv_show(tv_show):
    return tv_show["favourites"]["tv_show"]
    
def likes_to_eat(person,food_to_find):
    found_food = False
    for food in person["favourites"]["snacks"]:
        if food == food_to_find:
            found_food = True
    return found_food

def add_friend(person, friend):
    person["friends"].append(friend)


        