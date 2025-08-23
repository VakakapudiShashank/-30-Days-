# Day 5: Tuples & Sets — Unique Item Tracker

def unique_item_tracker():
    print("=== Unique Item Tracker ===")
    
    items = set()  
    while True:
        item = input("Enter an item (or type 'done' to finish): ").strip()
        
        if item.lower() == "done":
            break
        
        if item in items:
            print(f"'{item}' is already in the tracker ❌")
        else:
            items.add(item)
            print(f"'{item}' added ✅")
    
    items_tuple = tuple(items)
    print("\n📋 Final Unique Items (Tuple):", items_tuple)


if __name__ == "__main__":
    unique_item_tracker()
