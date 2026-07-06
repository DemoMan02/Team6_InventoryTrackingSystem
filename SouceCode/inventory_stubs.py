"""
========================================
INVENTORY TRACKING SYSTEM - Function Stubs
========================================
Project Name  : Inventory Tracking System
Team Number   : Group 6
Team Members  : Ronny Espinosa (Project Manager)
                Melissa Granville (Documentation Manager)
                Antoine Lara (GitHub Coordinator)
Course        : Introduction to Programming COP1047C-2265-6449
Date          : July 5, 2026
 
Description:
    This file contains function stubs for the Inventory Tracking System.
    A function stub is an empty function that shows the name, purpose,
    and structure of each feature without any working code inside.
    Full implementation will be added in Phase 3.
 
Records       : 25 Inventory Records
Data Fields   : Item ID, Item Name, Inventory Status
Status Values : In Stock | Low Stock | Out of Stock
========================================
"""
 
# ----------------------------------------
# CONSTANTS
# These values never change in the program
# ----------------------------------------
 
MAX_RECORDS = 25                         # Maximum number of inventory records allowed
 
STATUS_IN_STOCK     = "In Stock"         # Item has plenty of stock
STATUS_LOW_STOCK    = "Low Stock"        # Item is running low
STATUS_OUT_OF_STOCK = "Out of Stock"     # Item has no stock remaining
 
VALID_STATUSES = [STATUS_IN_STOCK, STATUS_LOW_STOCK, STATUS_OUT_OF_STOCK]
 
 
# ----------------------------------------
# FUNCTION STUBS
# ----------------------------------------
 
 
def add_record(records):
    """
    Add a new inventory item to the system.
 
    This function will ask the user to enter:
        - Item ID   (example: "INV-001")
        - Item Name (example: "Water Bottle")
        - Status    (In Stock / Low Stock / Out of Stock)
 
    It will then save the new item to the records list.
    The system can hold a maximum of 25 records.
 
    Parameters:
        records (list): The current list of inventory items.
 
    Returns:
        list: The updated list with the new item added.
 
    Author : Ronny Espinosa
    Status : Stub - Implementation pending Phase 3
    """
    # TODO: Implementation in Phase 3
    pass
 
 
def search_record(records, search_term):
    """
    Search for an inventory item by Item ID or Item Name.
 
    This function will look through all records and find any item
    that matches what the user typed. The search will work even
    if the user types only part of the name.
 
    Parameters:
        records (list): The current list of inventory items.
        search_term (str): The Item ID or Item Name to search for.
 
    Returns:
        list: A list of items that match the search.
              Returns an empty list if nothing is found.
 
    Author : Melissa Granville
    Status : Stub - Implementation pending Phase 3
    """
    # TODO: Implementation in Phase 3
    pass
 
 
def display_records(records):
    """
    Display all inventory records on the screen.
 
    This function will print all 25 inventory items in a
    neat and organized table format showing:
        - Item ID
        - Item Name
        - Inventory Status
 
    If there are no records yet, it will show a message
    telling the user that the inventory is empty.
 
    Parameters:
        records (list): The current list of inventory items.
 
    Returns:
        None: This function only prints to the screen.
 
    Author : Antoine Lara
    Status : Stub - Implementation pending Phase 3
    """
    # TODO: Implementation in Phase 3
    pass
 
 
def update_status(records, record_id, new_status):
    """
    Update the inventory status of an existing item.
 
    This function will find the item with the matching Item ID
    and change its status to the new value entered by the user.
 
    Valid status values are:
        - "In Stock"
        - "Low Stock"
        - "Out of Stock"
 
    Parameters:
        records (list): The current list of inventory items.
        record_id (str): The Item ID of the item to update.
        new_status (str): The new status to assign to the item.
 
    Returns:
        list: The updated list with the new status applied.
 
    Author : Ronny Espinosa
    Status : Stub - Implementation pending Phase 3
    """
    # TODO: Implementation in Phase 3
    pass
 
 
def generate_report(records):
    """
    Generate a summary report of all inventory items.
 
    This function will count how many items fall into each
    status category and display a full summary report showing:
        - Total number of items.
        - Number of items In Stock.
        - Number of items Low Stock.
        - Number of items Out of Stock.
 
    Parameters:
        records (list): The current list of inventory items.
 
    Returns:
        dict: A dictionary with the following summary numbers:
              {
                  "total_items"  : total count of all 25 records,
                  "in_stock"     : count of In Stock items,
                  "low_stock"    : count of Low Stock items,
                  "out_of_stock" : count of Out of Stock items,
              }
 
    Author : Melissa Granville
    Status : Stub - Implementation pending Phase 3
    """
    # TODO: Implementation in Phase 3
    pass
 
 
def exit_program():
    """
    Exit the Inventory Tracking System.
 
    This function will display a goodbye message and
    then close the program when the user is done.
 
    Parameters:
        None
 
    Returns:
        None
 
    Author : Antoine Lara
    Status : Stub - Implementation pending Phase 3
    """
    # This line already works - it prints the goodbye message
    print("Thank you for using the Inventory Tracking System. Goodbye!")
 
    # TODO: Add any final cleanup steps in Phase 3
    pass
 
 
def main_menu():
    """
    Display the main menu and handle user choices.
 
    This function will show the user a numbered list of options
    and ask them to pick one. It will keep showing the menu
    after each action until the user chooses to exit.
 
    Menu Options:
        1. Add Inventory Record.
        2. Search Inventory Record.
        3. Display All Records.
        4. Update Inventory Status.
        5. Generate Summary Report.
        6. Exit Program.
 
    Parameters:
        None
 
    Returns:
        None: Keeps looping until the user selects Exit.
 
    Author : Ronny Espinosa
    Status : Stub - Implementation pending Phase 3
    """
    # TODO: Implementation in Phase 3
    pass
 
 
# ----------------------------------------
# PROGRAM ENTRY POINT
# This is where the program starts running
# ----------------------------------------
 
if __name__ == "__main__":
    # TODO: Create the records list and call main_menu() in Phase 3
    pass
