"""output_utils.py
1. **`format_output(data)`**:
    - Purpose: Convert analysis data into a human-readable or structured format suitable for display or export.
    - Parameters:
        - `data`: The raw data to format.

3. **`save_to_csv(data, filename)`**:
    - Purpose: Export the provided data to a CSV file.
    - Parameters:
        - `data`: The data to export.
        - `filename`: The name of the CSV file to save.

4. **`load_from_csv(filename)`**:
    - Purpose: Load data from a CSV file for further analysis.
    - Parameters:
        - `filename`: The name of the CSV file to load.
"""

import csv
from typing import List, Dict, Union


def format_output(data: Union[Dict, List[Dict]]) -> str:
    """
    Convert analysis data into a human-readable or structured format.

    Parameters:
    - data: The raw data to format.

    Returns:
    - A formatted string representation of the data.
    """
    # Handle different data types
    if isinstance(data, dict):
        formatted_data = "\n".join([f"{key}: {value}" for key, value in data.items()])
    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
        headers = data[0].keys()
        formatted_data = "\n".join(
            [", ".join([str(item[header]) for header in headers]) for item in data]
        )
    else:
        formatted_data = str(data)

    return formatted_data


def save_to_csv(data: List[Dict], filename: str) -> None:
    """
    Export the provided data to a CSV file.

    Parameters:
    - data: The data to export.
    - filename: The name of the CSV file to save.
    """
    with open(filename, "w", newline="") as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


def load_from_csv(filename: str) -> List[Dict]:
    """
    Load data from a CSV file for further analysis.

    Parameters:
    - filename: The name of the CSV file to load.

    Returns:
    - A list of dictionaries representing the loaded data.
    """
    data = []

    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    return data


# Test functions
if __name__ == "__main__":
    sample_data = [
        {"name": "John", "age": "25", "city": "New York"},
        {"name": "Anna", "age": "28", "city": "London"},
        {"name": "Mike", "age": "23", "city": "San Francisco"},
    ]

    print(format_output(sample_data))

    save_to_csv(sample_data, "test.csv")
    loaded_data = load_from_csv("test.csv")
    print(loaded_data)
