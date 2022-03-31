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


def remove_friend(person,friend):
    person["friends"].remove(friend)

def total_money(money):
    total_money = 0

    for cash in money:
        total_money += cash["monies"]
        cash["monies"] = 0

    return total_money
        
def lend_money(lender, lendee, amount):
    lender["monies"] -= amount
    lendee["monies"] += amount


    
    
    

    
    