def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in cheeses:
            return food
    return None

# Example usage
if __name__ == "__main__":
    # Testing roll_call_dwarves
    roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])

    # Testing summon_captain_planet
    print(summon_captain_planet(["earth", "wind", "fire", "water", "heart"]))

    # Testing long_planeteer_calls
    print(long_planeteer_calls(["puff", "go", "two"]))
    print(long_planeteer_calls(["two", "go", "industrious", "bop"]))

    # Testing find_the_cheese
    print(find_the_cheese(["crackers", "gouda", "thyme"]))
    print(find_the_cheese(["tomato soup", "cheddar", "oyster crackers", "gouda"]))
    print(find_the_cheese(["garlic", "rosemary", "bread"]))
