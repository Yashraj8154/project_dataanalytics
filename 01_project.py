import csv
from datetime import datetime
from pathlib import Path


DATA_FILE = Path("prices.csv")


def create_file_if_needed():
    """Create the CSV and its headings the first time the program runs."""
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "item", "category", "price"])


def add_price():
    item = input("Item name: ").strip()
    category = input("Category: ").strip()

    if not item or not category:
        print("Item name and category cannot be empty.")
        return

    try:
        price = float(input("Price: "))
        if price < 0:
            print("Price cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid number for the price.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    with DATA_FILE.open("a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, item, category, f"{price:.2f}"])

    print("Price saved successfully.")


def read_prices():
    with DATA_FILE.open(newline="") as file:
        return list(csv.DictReader(file))


def show_prices():
    records = read_prices()
    if not records:
        print("No prices have been added yet.")
        return

    print("\nDate        Item                 Category             Price")
    print("-" * 63)
    for record in records:
        print(f"{record['date']:<11} {record['item']:<20} {record['category']:<20} Rs. {float(record['price']):.2f}")


def analyse_prices():
    records = read_prices()
    if not records:
        print("No prices are available to analyse.")
        return

    prices = [float(record["price"]) for record in records]
    highest = max(records, key=lambda record: float(record["price"]))
    lowest = min(records, key=lambda record: float(record["price"]))
    average = sum(prices) / len(prices)

    print("\nPrice Analysis")
    print("-" * 30)
    print(f"Number of entries: {len(records)}")
    print(f"Total spent: Rs. {sum(prices):.2f}")
    print(f"Average price: Rs. {average:.2f}")
    print(f"Highest price: {highest['item']} - Rs. {float(highest['price']):.2f}")
    print(f"Lowest price: {lowest['item']} - Rs. {float(lowest['price']):.2f}")


def main():
    create_file_if_needed()

    while True:
        print("\n--- Price Tracker ---")
        print("1. Add a price")
        print("2. View all prices")
        print("3. Analyse prices")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_price()
        elif choice == "2":
            show_prices()
        elif choice == "3":
            analyse_prices()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
