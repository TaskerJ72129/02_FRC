# import libraries
import pandas

# ---- Functions go here ----

# Checks that the user has entered yes / no to a question
def yes_no(question):

    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
                              "The component name can't be "
                              "blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity:",
                                 "The amount must be a whole number more than 0",
                                 int)
        else:
            quantity = 1

        price = num_check("How much for a single item? $",
                          "The price must be a number <more than 0>",
                          float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)


    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity']\
                            * expense_frame['Price']

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

def profit_goal(total_costs):

    # Initialise variables and error messages
    error = "Please enter a valid profit goal\n"

    valid = False 
    while not valid:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%) ")
        
        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]