```python
# Retail Billing with Multiple Discount Rules

products = {
    "Laptop": ["Electronics", 50000, 18],
    "Mobile": ["Electronics", 20000, 18],
    "Shirt": ["Clothing", 1000, 5],
    "Rice": ["Groceries", 500, 0]
}

cart = []

n = int(input("Enter the number of different products: "))

# Process products
for i in range(n):

    print("\nAvailable Products:")
    for name in products:
        print(name, "- Rs.", products[name][1])

    product_name = input("Enter product name: ")

    if product_name not in products:
        print("Invalid product. Please try again.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    category = products[product_name][0]
    price = products[product_name][1]
    tax_rate = products[product_name][2]

    subtotal = price * quantity

    cart.append([
        product_name,
        category,
        price,
        quantity,
        subtotal,
        tax_rate
    ])

# Calculate total subtotal
subtotal = 0

for item in cart:
    subtotal += item[4]

# Determine discount percentage
if subtotal >= 5000:
    discount_rate = 10

elif subtotal >= 1000:
    discount_rate = 5

else:
    discount_rate = 0

# Apply maximum discount limit
discount = subtotal * discount_rate / 100

if discount > 1000:
    discount = 1000

# Calculate proportional discount, tax, and final cost
total_tax = 0
final_total = 0

print("\n================ ITEMIZED INVOICE ================")
print("Product       Qty   Price   Subtotal   Discount   Tax")

for item in cart:

    name = item[0]
    price = item[2]
    quantity = item[3]
    item_subtotal = item[4]
    tax_rate = item[5]

    # Distribute discount proportionally
    if subtotal > 0:
        item_discount = discount * item_subtotal / subtotal
    else:
        item_discount = 0

    taxable_amount = item_subtotal - item_discount

    # Calculate category-specific tax
    tax = taxable_amount * tax_rate / 100

    item_total = taxable_amount + tax

    total_tax += tax
    final_total += item_total

    print(
        name,
        quantity,
        price,
        round(item_subtotal, 2),
        round(item_discount, 2),
        round(tax, 2)
    )

print("--------------------------------------------------")
print("Subtotal: Rs.", round(subtotal, 2))
print("Discount Rate:", discount_rate, "%")
print("Total Discount: Rs.", round(discount, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Final Payable Amount: Rs.", round(final_total, 2))
print("==================================================")
```