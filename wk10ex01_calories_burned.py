"""
Filename: wk10ex01_calories_burned.py
Description: A multi-session calorie tracker program that calculates per-session 
             and total calories consumed using helper functions and dynamic lists.
Author: Precious Arellano
Date: 2026
"""

def calculate_session_total(calories_list):
    """
    Helper function to sum calories for a single session.
    
    Parameters:
        calories_list (list): A list of integers representing calories from meals.
        
    Returns:
        int: The total calories for the session.
    """
    return sum(calories_list)


def main():
    print("=== Multi-Session Calorie Tracker ===")
    
    # Prompt the user for total number of sessions to log
    try:
        total_sessions = int(input("Enter the total number of sessions to track: "))
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
        return

    session_totals = []  # List to store per-session calorie sums
    overall_total = 0    # Accumulator for total calories across all sessions

    # Process each session sequentially
    for session_num in range(1, total_sessions + 1):
        print(f"\n--- Processing Session {session_num} ---")
        current_session_calories = []
        
        while True:
            meal_input = input("Enter meal calories (or type 'done' to finish session): ").strip()
            
            if meal_input.lower() == 'done':
                break
            
            # Convert input to integer and append to session list
            try:
                calories = int(meal_input)
                if calories < 0:
                    print("Calorie values cannot be negative. Try again.")
                    continue
                current_session_calories.append(calories)
            except ValueError:
                print("Invalid entry. Please enter a numerical value or 'done'.")

        # Calculate session total using the helper function
        session_total = calculate_session_total(current_session_calories)
        session_totals.append(session_total)
        
        # Update total accumulator
        overall_total += session_total
        print(f"Total calories for Session {session_num}: {session_total}")

    # Display final summary results
    print("\n================ SUMMARY ================")
    for i, total in enumerate(session_totals, start=1):
        print(f"Session {i} Total: {total} calories")
    print(f"Overall Total Calories Consumed: {overall_total} calories")
    print("=========================================")

if __name__ == "__main__":
    main()
