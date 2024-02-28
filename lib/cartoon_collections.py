def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print(f'{i}. {dwarf}')
        i += 1

def summon_captain_planet(planeteer_calls):
    call_list = [f'{call.capitalize()}!' for call in planeteer_calls]
    return call_list

def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for cheese in cheese_types:
        if cheese in snacks:
            return cheese
    return None
