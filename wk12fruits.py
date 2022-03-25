def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    # Reverse and print the fruit_list list.
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    # Append "orange" to the end of the fruit_list and
    # print the list.
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")

    # Find where "apple" is located in the fruit_list and insert
    # "cherry" before "apple" in the list and print the list.
    locate = fruit_list.index('apple')
    fruit_list.insert(locate, "cherry")
    print(f"insert cherry: {fruit_list}")

    # Remove "banana" from the fruit_list and print the list.
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    # Pop (remove) the last element from the fruit_list
    # and print the popped element and the list.
    last = fruit_list.pop()
    print(f"pop {last}: {fruit_list}")

    # Sort and print the fruit_list.
    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    # Clear and print the fruit_list.
    fruit_list.clear()
    print(f"cleared: {fruit_list}")

main()