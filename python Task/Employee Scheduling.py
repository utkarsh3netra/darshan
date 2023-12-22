employees = [
    {"name": "Alice", "role": "Chef", "available_days": ["Monday", "Tuesday"]},
    {"name": "Bob", "role": "Waiter", "available_days": ["Monday", "Wednesday", "Friday"]},
    {"name": "Charlie", "role": "Manager", "available_days": ["Tuesday", "Thursday", "Saturday"]},
    {"name": "Diana", "role": "Chef", "available_days": ["Wednesday", "Thursday"]},
    {"name": "Edward", "role": "Waiter", "available_days": ["Tuesday", "Thursday", "Sunday"]},
    {"name": "Fiona", "role": "Manager", "available_days": ["Monday", "Friday", "Sunday"]},
    {"name": "George", "role": "Chef", "available_days": ["Friday", "Saturday", "Sunday"]},
    {"name": "Hannah", "role": "Waiter", "available_days": ["Monday", "Saturday"]},
    {"name": "Sarah", "role": "Manager", "available_days": ["Wednesday", "Thursday", "Saturday"]},
]
roles_needed = {
    "Monday": ["Chef", "Waiter", "Manager"],
    "Tuesday": ["Chef", "Waiter", "Manager"],
    "Wednesday": ["Chef", "Waiter", "Manager"],
    "Thursday": ["Chef", "Waiter", "Manager"],
    "Friday": ["Chef", "Waiter", "Manager"],
    "Saturday": ["Chef", "Waiter", "Manager"],
    "Sunday": ["Chef", "Waiter", "Manager"]
}
sechedule = {day: [] for day in roles_needed}
for day, roles in roles_needed.items():
    for role in roles:
        for employee in employees:
            if role == employee["role"] and day in employee["available_days"]:
                if employee["name"] not in sechedule:
                    sechedule[day].append(employee["name"])
                    break
print(sechedule)
for employee in sechedule.items():
    print(f"{day}:{employee}")
