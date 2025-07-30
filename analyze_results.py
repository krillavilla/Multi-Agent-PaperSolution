import pandas as pd
import re

# Read test results
df = pd.read_csv('test_results.csv')
print('Total orders processed:', len(df) - 1)

# Extract order details from response column
total_revenue = 0
item_counts = {}
item_quantities = {}

for response in df['response'][1:]:  # Skip header
    if 'Order confirmed' in str(response):
        # Extract total amount using regex
        price_match = re.search(r'\$([0-9]+\.?[0-9]*)', response)
        if price_match:
            amount = float(price_match.group(1))
            total_revenue += amount
        
        # Extract quantity and item name
        qty_match = re.search(r'(\d+) units of ([^f]+) for', response)
        if qty_match:
            quantity = int(qty_match.group(1))
            item_name = qty_match.group(2).strip()
            item_counts[item_name] = item_counts.get(item_name, 0) + 1
            item_quantities[item_name] = item_quantities.get(item_name, 0) + quantity

print(f'Total revenue: ${total_revenue:.2f}')
print(f'Cash balance shown: ${df["cash_balance"].iloc[-1]:.2f}')

print('\nTop selling items by order frequency:')
sorted_items = sorted(item_counts.items(), key=lambda x: x[1], reverse=True)
for item, count in sorted_items[:3]:
    total_qty = item_quantities.get(item, 0)
    print(f'  {item}: {count} orders, {total_qty} total units')
