def greedy_coin_change():
    """
    Solves the Coin Change Problem using the Greedy Algorithm.
    The coin list is sorted from largest to smallest before processing.
    """
    print("=========================================================")
    print("🪙 1. Greedy Coin Change Program")
    print("=========================================================")
    try:
        # --- User Input ---
        amount = int(input("Enter the amount of money: ").strip())
        
        coins_input = input("Input list of values coins (e.g.: 1000 500 200 100 50): ")
        coins = [int(x) for x in coins_input.split()]
        
        # Instruction: Sort coin from big to small
        coins.sort(reverse=True) 
        
        if not coins or amount < 0:
            print("❌ Invalid input. Please check the amount and coin values.")
            return

        # --- Greedy Processing ---
        remaining_amount = amount
        coin_combination = {}
        total_coins = 0

        print(f"\nProcessing Change for {amount}. Sorted Coins: {coins}")

        for coin in coins:
            if remaining_amount >= coin:
                # Calculate how many times this coin can be used
                count = remaining_amount // coin 
                
                # Update tracking variables
                coin_combination[coin] = count
                total_coins += count
                
                # Subtract the used amount and update remainder
                remaining_amount %= coin 
                
            if remaining_amount == 0:
                break

        # --- Output ---
        print("\n✅ Program Output:")
        print(f"Combination coins used: {coin_combination}")
        print(f"Total number of coins: {total_coins}")
        
        if remaining_amount > 0:
            print(f"⚠️ Note: Could not make exact change. Remaining amount: {remaining_amount}")
        
    except ValueError:
        print("❌ Invalid input. Please ensure amount and coins are valid integers.")

if __name__ == "__main__":
    greedy_coin_change()
    