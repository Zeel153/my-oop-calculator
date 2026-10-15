# OOP Calculator

**Course:** IS 218 – Introduction to Professional Programming  
**Student:** Zeel Patel  
**Project:** Object-Oriented Programming Calculator

## Project Overview

This project is a command-line calculator developed in Python using object-oriented programming (OOP) principles. It supports addition and subtraction, stores calculation history, and allows users to manage previous calculations.

The project was developed in six stages, starting with basic classes and methods and gradually introducing abstraction, inheritance, polymorphism, encapsulation, error handling, automated testing, and continuous integration.

## Features

- Add two numbers.
- Subtract two numbers.
- Display calculation history.
- Remove calculations from history.
- Handle invalid numeric input and removal requests.
- Display available commands.
- Exit the application.
- Run automated tests with pytest.
- Check test coverage using pytest-cov.
- Automatically test the project using GitHub Actions.

## Installation

### 1. Clone the repository

```powershell
git clone https://github.com/Zeel153/my-oop-calculator.git
cd my-oop-calculator
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Running the Calculator

Start the application using:

```powershell
python -m calculator
```

The calculator provides six commands:

| Command | Description |
|---|---|
| `add` | Adds two numbers |
| `subtract` | Subtracts the second number from the first |
| `history` | Displays previous calculations |
| `remove` | Removes a calculation using its displayed number |
| `help` | Shows available commands |
| `exit` | Closes the calculator |

### Example

```text
OOP Calculator

Type "help" for commands.
> add
First number: 4
Second number: 4
Result: 8
> exit
Goodbye!
```

## Project Structure

```text
my-oop-calculator/
├── .github/
│   └── workflows/
│       └── tests.yml
├── calculator/
│   ├── __init__.py
│   ├── __main__.py
│   ├── calculation.py
│   ├── cli.py
│   ├── history.py
│   └── operations.py
├── tests/
│   ├── __init__.py
│   ├── test_calculation.py
│   ├── test_cli.py
│   ├── test_history.py
│   └── test_operations.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Object-Oriented Programming Concepts

### Abstraction

The calculator uses an abstract `Calculation` class to define a common structure for calculation operations. This makes it easier to introduce additional operations while maintaining a consistent design.

### Inheritance

The `Add` and `Subtract` classes inherit from the shared `Calculation` class. This allows both operations to follow the same structure while providing their own calculation behavior.

### Polymorphism

Both addition and subtraction use the `calculate()` method. The result depends on which calculation object is being used. This demonstrates how different objects can respond to the same method call in different ways.

### Encapsulation

The `History` class manages stored calculations without exposing its internal list directly. This helps protect the collection from unwanted modifications and keeps history-related responsibilities in one place.

## Testing and Coverage

The project uses pytest for automated testing and pytest-cov for coverage analysis.

To run the tests:

```powershell
python -m pytest -v
```

To view line and branch coverage:

```powershell
python -m pytest --cov=calculator --cov-branch --cov-report=term-missing
```

The completed Stage 5 implementation achieved:

- **37 passing tests**
- **100% line coverage**
- **100% branch coverage**

The tests verify calculation results, independent objects, calculation history, command-line interactions, invalid input recovery, and other boundary conditions.

## Continuous Integration

GitHub Actions automatically runs the test suite whenever changes are pushed to the repository.

The workflow is configured in `.github/workflows/tests.yml`.

The project is tested using Python versions:

- Python 3.11
- Python 3.12
- Python 3.13
- Python 3.14

All four jobs passed successfully during Stage 6.

## Stage 6 — Design Reflection

### 1. How would I add multiplication?

I would create a new `Multiply` class that follows the same structure as `Add` and `Subtract`. It would inherit from the `Calculation` class and implement the `calculate()` method using multiplication.

I would also update the command-line interface to recognize a `multiply` command, add the command to the help menu, and write tests to verify positive numbers, negative numbers, and multiplication by zero.

The existing design would make this easier because each operation follows the same contract.

### 2. How could the same design work for email and text notifications?

A notification system could use a common abstract class with a `send()` method. Different classes, such as `EmailNotification` and `TextNotification`, could implement that method in their own ways.

Both classes would follow the same interface, but one would send an email while the other would send a text message.

This is similar to how `Add` and `Subtract` share a `calculate()` method but perform different operations.

### 3. Which OOP concepts transfer to another programming language?

Abstraction, inheritance, polymorphism, and encapsulation are concepts that can be used in many programming languages.

For example, I could apply the same calculator design in Java or C++, although the syntax would be different.

I would need to learn how each language handles abstract classes, constructors, inheritance, access modifiers, and exceptions. The overall design ideas would remain useful even when the programming language changes.

## What I Learned

This project helped me understand how object-oriented programming can make a program easier to organize and expand.

At first, I worked with simple calculation classes. Later, I learned how to create a shared structure for different operations, manage objects using a history class, and connect everything through a command-line interface.

I also learned why testing is important. By adding tests for invalid input and unusual situations, I could make the calculator more reliable.

GitHub Actions was another useful part of the assignment because it showed me how automated testing can verify a project in different Python environments.

Overall, this assignment gave me more practice with Python, object-oriented programming, pytest, Git, and GitHub.

## Repository

GitHub: https://github.com/Zeel153/my-oop-calculator