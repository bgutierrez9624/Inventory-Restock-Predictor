# Restock Predictor for a Grocery Store

#Add function to calculate remaining inventory days based on stock and sales rate

def calculate_days_left(current_stock, avg_daily_sales):
    """
    if avg_daily_sales <= 0:
        return None
    return current_stock / avg_daily_sales

#Add function to determine restock status based on remaining inventory days

    def get_restock_status(days_left, reorder_threshold):
    """
    Returns the restock recommendation based on days left.
    """
    if days_left is None:
        return "No sales data"
    elif days_left <= reorder_threshold:
        return "RESTOCK NOW"
    elif days_left <= reorder_threshold + 2:
        return "Restock soon"
    else:
        return "Stock is okay"

#Add main function to collect inventory data and calculate restock status

def main():
    print("=== Grocery Store Restock Predictor ===")

    inventory = []

    try:
        num_items = int(input("How many products do you want to enter? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(num_items):
        print(f"\nEntering product #{i + 1}")

        product_name = input("Product name: ")

        try:
            current_stock = int(input("Current stock: "))
            avg_daily_sales = float(input("Average daily sales: "))
            reorder_threshold = int(input("Reorder threshold (days): "))
        except ValueError:
            print("Invalid input. Please enter numbers for stock, sales, and threshold.")
            return

        days_left = calculate_days_left(current_stock, avg_daily_sales)
        status = get_restock_status(days_left, reorder_threshold)

        inventory.append({
            "name": product_name,
            "current_stock": current_stock,
            "avg_daily_sales": avg_daily_sales,
            "days_left": days_left,
            "status": status
        })

#Add report output and restock alert summary for inventory

print("\n=== Restock Report ===")
    for item in inventory:
        print(f"\nProduct: {item['name']}")
        print(f"Current Stock: {item['current_stock']}")
        print(f"Average Daily Sales: {item['avg_daily_sales']}")

        if item["days_left"] is None:
            print("Days Left: No sales data")
        else:
            print(f"Days Left: {item['days_left']:.1f}")

        print(f"Status: {item['status']}")

    print("\n=== Items That Need Attention ===")
    found_attention = False

    for item in inventory:
        if item["status"] in ["RESTOCK NOW", "Restock soon"]:
            found_attention = True
            print(f"- {item['name']}: {item['status']}")

    if not found_attention:
        print("All items are stocked well.")


if __name__ == "__main__":
    main()
