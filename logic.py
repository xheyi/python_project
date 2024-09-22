days_in_month = 30


def days_to_unit(num_of_days, unit):
    if unit == "days" or "day":
        return f"{num_of_days} months has {num_of_days * days_in_month} {unit}"
    if unit == "hours":
        return f"{num_of_days} months has {num_of_days * days_in_month * 24} {unit}"
    if unit == "minutes":
        return f"{num_of_days} months has {num_of_days * days_in_month * 24 * 60} {unit}"
    else:
        return "we dont calculate for this unit."


def validation_and_execution(month_and_unit_dict):

    try:
        ready_input = int(month_and_unit_dict["month"])
        if ready_input > 0:
            result = days_to_unit(ready_input, month_and_unit_dict["unit"])
            print(result)
        elif ready_input == 0:
            print("we dont calculate for zero.")
        else:
            print("you have entered a negative number.")
    except ValueError:
        print("you have entered an invalid input.")


custom_message = "give me a number of months and a unit to convert convert it to\n"