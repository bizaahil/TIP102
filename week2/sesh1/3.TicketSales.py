def total_sales(ticket_sales):
    total = 0

    for ticket in ticket_sales.values():
        total += ticket

    return total



ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))