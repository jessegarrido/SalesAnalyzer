def calculate_total_sales(filename):
def find_top_selling_product(filename):
import csv

class SalesAnalyzer:
    """
    A class to analyze sales data from a CSV file.
    
    The analyzer reads sales data and provides methods to calculate total sales
    and identify the top-selling product by revenue. It assumes the CSV file has
    'product_name', 'price', and 'quantity' columns.
    """
    def __init__(self, filename):
        """
        Initialize the SalesAnalyzer with a CSV filename.
        
        Args:
            filename (str): The path to the CSV file containing sales data.
        """
        self.filename = filename
        self.data = None

    def load_data(self):
        """
        Load and parse data from the CSV file.
        
        Reads the CSV file and stores valid rows as a list of dictionaries.
        Handles FileNotFoundError and prints an error message if the file
        doesn't exist.
        
        Returns:
            bool: True if data was loaded successfully, False otherwise.
        """
        try:
            with open(self.filename, mode='r') as file:
                csv_reader = csv.DictReader(file)
                self.data = list(csv_reader)
                return True
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
            print("Please ensure the file exists in the specified location.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")
            return False

    def calculate_total_sales(self):
        """
        Calculate the total sales from loaded data.
        
        Iterates through all data rows and calculates the sum of (price * quantity)
        for each product. Handles ValueError for invalid numeric values and
        continues processing remaining rows.
        
        Returns:
            float: The total sales amount, or None if data hasn't been loaded
                   or an error occurs.
        """
        if self.data is None:
            print("Error: Data not loaded. Call load_data() first.")
            return None
        total = 0.0
        for row_num, row in enumerate(self.data, start=2):  # start=2 to account for header
            try:
                price = float(row['price'])
                quantity = int(row['quantity'])
                total += price * quantity
            except ValueError as e:
                print(f"Error in row {row_num}: Invalid price or quantity value. {row}")
                print(f"Details: {e}")
                continue
            except KeyError as e:
                print(f"Error in row {row_num}: Missing required column {e}")
                continue
        return total

    def find_top_product(self):
        """
        Identify the top-selling product by total revenue.
        
        Calculates revenue (price * quantity) for each product and returns
        the product with the highest total revenue. Handles ValueError for
        invalid numeric values and continues processing remaining rows.
        
        Returns:
            tuple: A tuple of (product_name, revenue) for the top product,
                   or None if data hasn't been loaded, no valid products exist,
                   or an error occurs.
        """
        if self.data is None:
            print("Error: Data not loaded. Call load_data() first.")
            return None
        max_revenue = 0.0
        top_product = None
        for row_num, row in enumerate(self.data, start=2):  # start=2 to account for header
            try:
                product_name = row['product_name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                revenue = price * quantity
                if revenue > max_revenue:
                    max_revenue = revenue
                    top_product = (product_name, revenue)
            except ValueError as e:
                print(f"Error in row {row_num}: Invalid price or quantity value. {row}")
                print(f"Details: {e}")
                continue
            except KeyError as e:
                print(f"Error in row {row_num}: Missing required column {e}")
                continue
        return top_product

if __name__ == "__main__":
    sales_data_file = 'sales_data.csv'
    analyzer = SalesAnalyzer(sales_data_file)
    # Load data
    if not analyzer.load_data():
        print("Failed to load sales data. Exiting.")
        exit(1)
    # Calculate total sales
    print("=" * 50)
    total_sales = analyzer.calculate_total_sales()
    if total_sales is not None:
        print(f"Total sales from {sales_data_file}: ${total_sales:,.2f}")
    else:
        print("Unable to calculate total sales due to errors.")
    # Find top-selling product
    print("\n" + "=" * 50)
    top_product = analyzer.find_top_product()
    if top_product is not None:
        product_name, revenue = top_product
        print(f"Top-selling product: {product_name}")
        print(f"Total revenue: ${revenue:,.2f}")
    else:
        print("Unable to find top-selling product due to errors.")
    print("=" * 50)