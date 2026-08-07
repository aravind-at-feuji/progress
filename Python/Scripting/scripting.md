# Python Scripting

## What is Scripting?

Scripting is the process of writing **scripts**—small programs that automate tasks, control software, or add functionality to existing applications.

Scripts are usually written in **scripting languages**, which are often **interpreted**, meaning they are run directly without requiring a separate compilation step.

---

## Common Scripting Languages

- **Python** – Automation, data analysis, and web development.
- **JavaScript** – Adds interactivity to websites.
- **Bash** – Automates tasks in Linux and macOS terminals.
- **PowerShell** – Automates tasks in Windows.
- **PHP** – Server-side web scripting.

---

# Python Scripting

Python scripting is the process of writing Python programs (called **scripts**) to automate tasks, process data, or control other software.

A Python script is typically saved with the **`.py`** extension and executed by the **Python interpreter**.

---

## Example

The following script lists all files and folders in the current directory.

```python
import os

folder = "."

for filename in os.listdir(folder):
    print(filename)
```
---

## Output

The output will display the names of all files and folders in the current directory, for example:

```text
Example.py
scripting.md
```

---
