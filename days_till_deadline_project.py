import datetime

goal_and_deadline = input("enter your goal with a deadline separated by colon.\n")
g_and_d = goal_and_deadline.split(":")

goal = g_and_d[0]
deadline = g_and_d[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
current_date = datetime.datetime.now()

time_till_deadline = deadline_date - current_date

print(f"the number of days left till your goal: {goal} is {time_till_deadline.days} days or {time_till_deadline.days * 24} hours")