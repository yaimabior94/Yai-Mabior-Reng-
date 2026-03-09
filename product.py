class Product:
    """
    Represents a product in an online shop.
    """
    def __init__(self, product_id: str, name: str, price: float, stock: int, category: str):
        # Using private attributes for encapsulation
        self._product_id = product_id
        self._name = name
        self._category = category
        
        # Using setters for initialization to ensure validation rules are applied
        self.price = price  
        self.stock = stock  

    # --- Properties (Encapsulation) ---

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def category(self) -> str:
        return self._category

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, value: int):
        if value < 0:
            raise ValueError("Stock cannot be negative.")
        self._stock = value

    # --- Methods ---

    def add_stock(self, quantity: int) -> None:
        """Increases the quantity of the product in inventory."""
        if quantity <= 0:
            raise ValueError("Quantity to add must be strictly positive.")
        self.stock += quantity
        print(f"Added {quantity} units. New stock for '{self.name}': {self.stock}")

    def check_stock_availability(self, quantity: int = 1) -> bool:
        """Verifies if a product is available in the requested quantity."""
        if quantity <= 0:
            raise ValueError("Quantity to check must be strictly positive.")
        return self.stock >= quantity

    def sell_product(self, quantity: int = 1) -> None:
        """Reduces the stock when a product is sold."""
        if quantity <= 0:
            raise ValueError("Quantity to sell must be strictly positive.")
        
        # Prevent sale if stock is insufficient
        if self.check_stock_availability(quantity):
            self.stock -= quantity
            print(f"Successfully sold {quantity} units of '{self.name}'. Remaining stock: {self.stock}")
        else:
            print(f"Error: Insufficient stock to sell {quantity} units of '{self.name}'. Current stock: {self.stock}")

    def apply_discount(self, percentage: float) -> None:
        """Applies a percentage discount to the product price."""
        if not (0 <= percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        discount_amount = self.price * (percentage / 100.0)
        self.price -= discount_amount
        print(f"Applied {percentage}% discount. New price for '{self.name}': ${self.price:.2f}")

    def display_details(self) -> None:
        """Shows all product information."""
        print("-" * 35)
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Category   : {self.category}")
        print(f"Price      : ${self.price:.2f}")
        print(f"Stock      : {self.stock} units")
        print("-" * 35)


def main():
    """Demonstrates example usage of the Product class."""
    try:
        # 1. Create a product
        print("--- Creating a New Product ---")
        laptop = Product(
            product_id="P1001", 
            name="Gaming Laptop", 
            price=1200.00, 
            stock=10, 
            category="Electronics"
        )
        laptop.display_details()

        # 2. Add stock
        print("\n--- Adding Stock ---")
        laptop.add_stock(5)

        # 3. Apply discount
        print("\n--- Applying Discount ---")
        laptop.apply_discount(10)  # 10% discount

        # 4. Sell a product (successful)
        print("\n--- Selling Product ---")
        laptop.sell_product(3)

        # Attempt to sell more than available (will fail due to check_stock_availability)
        print("\n--- Selling Product (Exceeding Stock) ---")
        laptop.sell_product(15)

        # 5. Display updated product details
        print("\n--- Final Product Details ---")
        laptop.display_details()

    except ValueError as e:
        print(f"Validation Error: {e}")

if __name__ == "__main__":
    main()
