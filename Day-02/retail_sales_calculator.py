print("\n WELCOME TO THE RETAIL SALES CALCULATOR\n")

productName=(input("Product: "))
selling_price=float(input("Selling price: "))
cost_price=float(input("Cost price: "))
unit_sold=int(input("Unit sold: "))

print(f"Product: {productName}")
print(f"Selling price: {selling_price}")
print(f"Cost price: {cost_price}")
print(f"Unit sold: {unit_sold}")

print("\n----SALES REPORT----\n")
total_revenue =selling_price * unit_sold
total_cost = cost_price * unit_sold
total_profit = total_revenue - total_cost
profit_margin=(total_profit/total_revenue) * 100

print(f"Product: {productName}")
print(f"Unit Sold: {unit_sold}")
print(f"Total revenue: R{total_revenue:.2f}")
print(f"Total cost: R{total_cost:.2f}")
print(f"Total profit: R{total_profit:.2f}")
print(f"Profit margin: {profit_margin:.2f}%")




