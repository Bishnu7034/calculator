Electric_bill = float(input("Enter the electricity bill amount: "))
House_rent = float(input("enter the rent: "))
cook = float(input("enter the amount given to cook"))
water_bill = float(input("enter the water bill"))
tenants = int(input("enter the number of tenants: "))
total_amount_per_head = (Electric_bill+House_rent+cook+water_bill+tenants)//tenants
print(f"each person will pay {total_amount_per_head}")
