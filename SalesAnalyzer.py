import csv

def calculate_total_sales(filename):
    # This function reads a CSV file and calculates the total sales.
    # It assumes the CSV has 'product_name', 'price', 'quantity' columns.
    
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            total = 0.0
            
            for row_num, row in enumerate(csv_reader, start=2):  # Start at 2 (row 1 is header)
                try:
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    total += price * quantity
                except ValueError as ve:
                    print(f"Error in row {row_num}: Invalid data format. Price must be a valid number and quantity must be an integer.")
                    print(f"  Row data: {row}")
                    print(f"  Details: {ve}")
                    continue
            
            return total
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file path and try again.")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def find_top_product(filename):
    # This function identifies the product with the highest total revenue (price * quantity).
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            top_product = None
            top_revenue = 0.0
            
            for row_num, row in enumerate(csv_reader, start=2):
                try:
                    product_name = row.get('product_name', 'Unknown')
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    revenue = price * quantity
                    
                    if revenue > top_revenue:
                        top_revenue = revenue
                        top_product = {
                            'name': product_name,
                            'price': price,
                            'quantity': quantity,
                            'revenue': revenue
                        }
                except ValueError as ve:
                    print(f"Error in row {row_num}: Invalid data format. Skipping this row.")
                    continue
            
            return top_product
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file path and try again.")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

if __name__ == "__main__":
    sales_data_file = 'sales_data.csv'
    
    # Calculate total sales
    print("="*50)
    total_sales = calculate_total_sales(sales_data_file)
    
    if total_sales is not None:
        print(f"Total Sales from {sales_data_file}: ${total_sales:.2f}")
    else:
        print("Unable to calculate total sales due to errors.")
    
    # Find and display top-selling product
    print("="*50)
    top_product = find_top_product(sales_data_file)
    
    if top_product is not None:
        print(f"\nTop-Selling Product by Revenue:")
        print(f"  Product: {top_product['name']}")
        print(f"  Unit Price: ${top_product['price']:.2f}")
        print(f"  Quantity Sold: {top_product['quantity']}")
        print(f"  Total Revenue: ${top_product['revenue']:.2f}")
    else:
        print("Unable to find top-selling product due to errors.")
    print("="*50)