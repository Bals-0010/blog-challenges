"""
    Try to imagine a world in which you might have to stay home for 14 days at any given time. 
    Do you have enough TP to make it through?
    Although the number of squares per roll of TP varies significantly, 
    we'll assume each roll has 500 sheets, and the average person uses 57 sheets per day.

    Create a function that will receive a dictionary with two key/values:

    "people" ⁠— Number of people in the household.
    "tp" ⁠— Number of rolls.
    Return a statement telling the user if they need to buy more TP!
"""

def tp_checker(people_tp_dict):
    """
    Input: A dictionary with two key/values
    Output: Returns a statement telling the user if they need to buy more TP!
    """
    average_sheet_per_person = 57
    each_roll_has_sheets = 500
    tp_solution = int(people_tp_dict["tp"]* each_roll_has_sheets) // (people_tp_dict["people"]*average_sheet_per_person)
    
    if tp_solution<14:
        return "Your TP will only last " + str(tp_solution) + " days, buy more!"
    else:
        return "Your TP will last " + str(tp_solution) + " days, no need to buy panic!"

print(tp_checker({"people":4, "tp":1}))
     