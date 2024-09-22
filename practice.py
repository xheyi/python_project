import logic as l


user_input = ""
while user_input != "exit":
    user_input = input(l.custom_message)
    month_and_unit = user_input.split(":")
    month_and_unit_dict = {"month": month_and_unit[0], "unit": month_and_unit[1]}
    l.validation_and_execution(month_and_unit_dict)
