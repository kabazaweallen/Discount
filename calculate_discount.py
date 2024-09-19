def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to be applied.

    Returns:
    - float: The final price after discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = (price * discount_percent) / 100
        # Calculate final price
        final_price = price - discount_amount
    else:
        # No discount applied
        final_price = price
    
    return final_price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the final price
    print(f"The final price after applying the discount is: {final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
