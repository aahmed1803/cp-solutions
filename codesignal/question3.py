"""
Your task is to develop a library book circulation tracker.

You are given a sequence of operations that represent activities in a library. Each operation is one of three types: acquisition, checkout, or reclassify. Operations are provided in the following format:

["acquisition", "<book category>", "<quantity>", "<price>"] 
    – the library acquires <quantity> books of <book category>, each valued at <price> for insurance purposes.
["checkout", "<book category>", "<quantity>"]
    – patrons borrow <quantity> books of <book category>. If books of the specified category have different insurance values, the least valuable ones should be checked out first. It is guaranteed that the library will always have enough books to fulfill all checkout requests.
["reclassify", "<book category>", "<quantity>", "<original price>", "<new price>"] 
    – the library reclassifies <quantity> books of <book category> to a more valuable edition. It is guaranteed that there are <quantity> books of the specified category with the <original price> value.
Your function should calculate the total insurance value of all books checked out after processing the entire sequence of operations. Return an array representing the insurance value of books for each checkout operation.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(operations.length2) will fit within the execution time limit.

Example

For

operations = [
  ["acquisition", "fiction", "2", "100"],
  ["acquisition", "reference", "3", "60"],
  ["checkout", "fiction", "1"],
  ["checkout", "reference", "1"],
  ["reclassify", "reference", "1", "60", "100"],
  ["checkout", "reference", "1"],
  ["checkout", "reference", "1"]
]
the output should be

solution(operations) = [100, 60, 60, 100]
Let's analyze the operations:

["acquisition", "fiction", "2", "100"] - the library acquires 2 fiction books, each valued at 100.
["acquisition", "reference", "3", "60"] - the library acquires 3 reference books, each valued at 60.
["checkout", "fiction", "1"] - a patron checks out 1 fiction book valued at 100, so the insurance value is 1 × 100 = 100.
["checkout", "reference", "1"] - a patron checks out 1 reference book valued at 60, so the insurance value is 1 × 60 = 60.
["reclassify", "reference", "1", "60", "100"] - one reference book is reclassified and its value becomes 100.
["checkout", "reference", "1"] - a patron checks out 1 reference book. There are 2 reference books in the library with values of 60 and 100, and the one with the value of 60 should be checked out first, so the insurance value is 1 × 60 = 60.
["checkout", "reference", "1"] - a patron checks out 1 reference book. There is 1 reference book in the library with the value of 100, so the insurance value is 1 × 100 = 100.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.string operations

An array of strings, where each element represents one of 3 types of operations described above - acquisition, checkout, or reclassify.
Each <book category> only consists of alphanumeric characters - English letters and digits.
Each <price> and <quantity> are string representations of integers which are between 0 and 2000.

Guaranteed constraints:
1 ≤ operations.length ≤ 100,
3 ≤ operations[i].length ≤ 5.

[output] array.integer

An array of integers representing insurance values from each checkout operation.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

"""

def solution(operations):
    prices = [] 
    inventory = {}  
    
    for op in operations:
        if op[0] == "acquisition":
            category = op[1]
            quantity = int(op[2])
            price = int(op[3])
            if category not in inventory:
                inventory[category] = []
            inventory[category].extend([price] * quantity)
            inventory[category].sort()
        
        elif op[0] == "checkout":
            category = op[1]
            quantity = int(op[2])
            books = inventory.get(category, [])
            remove = books[:quantity]
            total = sum(remove)
            inventory[category] = books[quantity:]
            prices.append(total)
        
        elif op[0] == "reclassify":
            category = op[1]
            quantity = int(op[2])
            original = int(op[3])
            new_price = int(op[4])
            
            books = inventory[category]
            
            changed = 0
            for i in range(len(books)):
                if books[i] == original and changed < quantity:
                    books[i] = new_price
                    changed += 1
            books.sort()
    
    return prices


def library_books_circulation_tracker():

    expected_output = [ 227250, 72250, 22250, 4750, 1000, 123312, 280600, 750, 24552, 8075, 129600, 660826, 6732, 657400, 83317]
    operations = [ 
            ["acquisition", "XwGq", "1427", "250"], 
            ["checkout", "XwGq", "909"],
            ["checkout", "XwGq", "289"],
            ["reclassify", "XwGq", "85", "250", "275"],
            ["reclassify", "XwGq", "72", "275", "303"],
            ["reclassify", "XwGq", "16", "303", "334"],
            ["checkout", "XwGq", "89"],
            ["reclassify", "XwGq", "22", "250", "275"],
            ["reclassify", "XwGq", "4", "275", "303"],
            ["acquisition", "zBRUlMJ", "610", "610"],
            ["acquisition", "sqmGgIyZH", "1988", "168"],
            ["checkout", "XwGq", "19"],
            ["checkout", "XwGq", "4"],
            ["checkout", "sqmGgIyZH", "734"],
            ["checkout", "zBRUlMJ", "460"],
            ["acquisition", "SH3", "1609", "540"],
            ["reclassify", "sqmGgIyZH", "1160", "168", "185"],
            ["acquisition", "0", "156", "396"],
            ["checkout", "XwGq", "3"],
            ["checkout", "0", "62"],
            ["acquisition", "XUwLAtN9Xb", "1313", "450"],
            ["checkout", "XwGq", "30"],
            ["acquisition", "XMdtFT5udp", "1631", "612"],
            ["acquisition", "SH3", "302", "655"],
            ["acquisition", "XUwLAtN9Xb", "984", "808"],
            ["checkout", "XUwLAtN9Xb", "288"],
            ["checkout", "XUwLAtN9Xb", "1272"],
            ["reclassify", "XwGq", "8", "275", "303"],
            ["reclassify", "sqmGgIyZH", "695", "185", "204"],
            ["acquisition", "XUwLAtN9Xb", "184", "556"],
            ["acquisition", "JhLshiFgDh", "1864", "75"],
            ["checkout", "0", "17"],
            ["checkout", "XUwLAtN9Xb", "871"],
            ["acquisition", "ek4f27", "1105", "814"],
            ["checkout", "sqmGgIyZH", "459"]
        ]
    
    output = solution(operations)
    print(output)
    assert output == expected_output
    
    
    expected_output =  [100, 60, 60, 100]
    operations = [
            ["acquisition", "fiction", "2", "100"],
            ["acquisition", "reference", "3", "60"],
            ["checkout", "fiction", "1"],
            ["checkout", "reference", "1"],
            ["reclassify", "reference", "1", "60", "100"],
            ["checkout", "reference", "1"],
            ["checkout", "reference", "1"]
        ]
    
    output = solution(operations)
    print(output)
    assert output == expected_output

library_books_circulation_tracker()
    