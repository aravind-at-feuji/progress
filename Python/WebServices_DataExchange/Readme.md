# REST/Web Services, Data Parsing & CSV Handling in Python

## Overview

This repository contains notes and examples related to:

- REST/Web Services concepts
- JSON parsing
- XML parsing
- CSV parsing in Python
- Common issues and solutions while working with Python CSV modules

These concepts are commonly used in backend development, API integration, data processing, and automation.

---

# 1. REST / Web Services

## What is REST?

REST (Representational State Transfer) is an architectural style used to build web services that allow applications to communicate over HTTP.

REST APIs use standard HTTP methods:

| Method | Purpose |
|--------|---------|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Update existing data |
| DELETE | Remove data |

Example:

```

GET [https://api.example.com/employees/101](https://api.example.com/employees/101)

````

Response:

```json
{
  "id": 101,
  "name": "John",
  "department": "IT"
}
````

---

# 2. JSON Parsing

## What is JSON?

JSON (JavaScript Object Notation) is a lightweight format used for exchanging data between applications.

Example:

```json
{
  "name": "Alice",
  "age": 25,
  "city": "New York"
}
```

Python JSON parsing example:

```python
import json

data = '{"name":"Alice","age":25}'

parsed_data = json.loads(data)

print(parsed_data["name"])
```

Output:

```
Alice
```

---

# 3. XML Parsing

## What is XML?

XML (eXtensible Markup Language) stores data using custom tags.

Example:

```xml
<Employee>
    <Id>101</Id>
    <Name>John</Name>
    <Department>IT</Department>
</Employee>
```

Common XML parsers:

* DOM Parser
* SAX Parser
* ElementTree

Python example:

```python
import xml.etree.ElementTree as ET

tree = ET.parse("employee.xml")

root = tree.getroot()

for child in root:
    print(child.tag, child.text)
```

---

# 4. CSV Parsing in Python

## What is CSV?

CSV (Comma-Separated Values) stores data in tabular format.

Example:

```csv
id,name,department
101,John,IT
102,Alice,HR
```

---

## Reading CSV Using csv Module

Python provides a built-in `csv` module.

Example:

```python
import csv

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```
['id', 'name', 'department']
['101', 'John', 'IT']
['102', 'Alice', 'HR']
```

---

## Reading CSV Using DictReader

`DictReader` converts rows into dictionaries.

Example:

```python
import csv

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
```

Output:

```
John
Alice
```

---

## Writing CSV Data

Example:

```python
import csv

with open("employees.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        ["ID", "Name", "Department"]
    )

    writer.writerow(
        [101, "John", "IT"]
    )
```

---

# Libraries Used

## Built-in Python Libraries

* csv
* json
* xml.etree.ElementTree

## External Libraries

Install pandas:

```bash
pip install pandas
```

Example:

```python
import pandas as pd

df = pd.read_csv("employees.csv")

print(df)
```
