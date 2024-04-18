import csv

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            # If value is a dictionary, flatten it recursively
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list) and all(isinstance(item, str) for item in v):
            # If value is a list of strings, treat it as separate columns
            for i, item in enumerate(v, start=1):
                items.append((f'{new_key}_course{i}', item))
        else:
            items.append((new_key, v))
    return dict(items)

# Original nested dictionary
student = {
    'personal_info': {
        'name': 'Alice',
        'age': 20,
        'contact_info': {
            'email': 'alice@example.com',
            'phone': '123-456-7890'
        }
    },
    'academic_info': {
        'major': 'Computer Science',
        'gpa': 3.5,
        'year': 3,
        'courses': {
            'fall': ['Data Structures', 'Algorithms'],
            'spring': ['Database Systems', 'Operating Systems'],
            'name': 'abcd'  # Added 'name' key under 'courses'
        }
    }
}

# Flatten the nested dictionary
flattened_student = flatten_dict(student)

# Write flattened data to a CSV file
csv_file = 'output.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(flattened_student.keys())
    writer.writerow(flattened_student.values())

print(f"Flattened data has been written to {csv_file}")