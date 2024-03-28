"""
CIS129 Programming Class
Pima Community College
Lab 7
George Blake
"""

# Constants designed to add sections by modifying here
SECTIONS = ['A', 'B', 'C']
SEAT_PRICES = {'A': 20, 'B': 15, 'C': 10}
SEAT_CAPACITIES = {'A': 300, 'B': 500, 'C': 200}

# Function to display welcome message
def display_welcome():
    print("Welcome to the Theater Ticket Sales System")
    print("Section Names:", ', '.join(SECTIONS))
    print("Seat Prices:", SEAT_PRICES)
    print("Seat Capacities:", SEAT_CAPACITIES)
    print()

# Function to get number of tickets sold for a section useing try except
def get_tickets_sold(section):
    while True:
        try:
            tickets = int(input(f"Enter number of tickets sold for section {section}: "))
            if tickets < 0:
                print("Please enter a non-negative number.")
            else:
                return tickets
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to calculate subtotal for a section
def calculate_subtotal(section, tickets_sold):
    return SEAT_PRICES[section] * tickets_sold

# Main function NOTE TO TEACHER I still had to put main last to get it to work
def main():
    display_welcome()
    total_income = 0
    section_totals = {}

    # Loop through each section
    for section in SECTIONS:
        tickets_sold = get_tickets_sold(section)
        while tickets_sold > SEAT_CAPACITIES[section]:
            print(f"Sorry, there are only {SEAT_CAPACITIES[section]} seats available in section {section}.")
            tickets_sold = get_tickets_sold(section)
        subtotal = calculate_subtotal(section, tickets_sold)
        total_income += subtotal
        section_totals[section] = subtotal
        print(f"Subtotal for section {section}: ${subtotal}")
        print(f"Total income so far: ${total_income}")
        print()

    # Display overall total and section totals
    print("Overall Total:")
    print("Total Income:", total_income)
    print("Section Totals:")
    for section, subtotal in section_totals.items():
        print(f"Section {section}: ${subtotal}")

# Call main function
if __name__ == "__main__":
    main()
