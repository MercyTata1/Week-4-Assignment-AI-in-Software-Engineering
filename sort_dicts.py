def sort_dicts_manual(data, key):
    """Sorts a list of dictionaries by a specified key."""
    return sorted(data, key=lambda x: x[key])

# Example usage:
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by age
sorted_people = sort_dicts_manual(people, "age")
print(sorted_people)