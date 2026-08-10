# Simple Python Calculator

A beginner-friendly command-line calculator built with Python.

This is one of my first Python projects. I built it while learning programming fundamentals and wanted to turn what I was learning into a small, working application.

The calculator supports basic mathematical operations and includes simple checks for common errors such as division by zero and invalid square-root inputs.

---

## Features

The calculator currently supports:

| Operation      | Description                                                |
| -------------- | ---------------------------------------------------------- |
| Addition       | Adds two numbers                                           |
| Subtraction    | Finds the difference between two numbers                   |
| Multiplication | Multiplies two numbers                                     |
| Division       | Divides one number by another                              |
| Percentage     | Calculates the percentage of one value compared to another |
| Square Root    | Calculates the square root of a number                     |
| Power          | Raises a number to a specified power                       |

The program also lets you perform multiple calculations in one session.

---

## How It Works

When the program starts, it displays a menu:

```text
Welcome to the calculator program!

Select operation to perform:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Percentage
6. Square Root
7. Power
8. Exit
```

You select an operation by entering its number.

For example:

```text
Enter choice : 1
Enter first number: 25
Enter second number: 15

The sum is: 40.0
```

After each calculation, the program asks whether you want to continue:

```text
Do you want to perform another calculation? (yes/no):
```

Enter `yes` to continue or `no` to exit.

---

## Error Handling

I added some basic checks to make the calculator safer to use.

The program handles cases such as:

* Division by zero
* Percentage calculations with a zero whole value
* Square roots of negative numbers
* Invalid operation choices

For example, the division function checks whether the second number is zero before performing the calculation.

The square-root function also checks for negative numbers before calculating the result.

---

## Technologies Used

* **Python 3**
* **Command Line / Terminal**

No external libraries are required to run the project.

---

## Getting Started

### Prerequisites

You need **Python 3** installed on your computer.

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with the URL of this repository.

### 2. Open the project directory

```bash
cd Simple-Python-Calculator
```

### 3. Run the calculator

```bash
python simcalculator.py
```

On some systems, use:

```bash
python3 simcalculator.py
```

---

## Project Structure

```text
Simple-Python-Calculator/
│
├── simcalculator.py
└── README.md
```

### `simcalculator.py`

Contains the calculator functions, menu, user input, calculations, and program flow.

### `README.md`

Contains information about the project, how to run it, the available operations, and what I learned while building it.

---

## What I Learned

This project helped me practice several important Python concepts.

### Functions

I created separate functions for each mathematical operation.

For example:

```python
def add(x, y):
    return x + y
```

Keeping each operation in its own function makes the code easier to understand and maintain.

### Conditional Statements

I used `if`, `elif`, and `else` statements to determine which operation the user selected.

### Loops

A loop keeps the calculator running so the user can perform multiple calculations without starting the program again.

### User Input

The program takes operation choices and numbers directly from the terminal.

### Basic Error Handling

I learned how to check for common problems before performing certain calculations, such as division by zero and negative square-root inputs.

---

## Why I Built This

I wanted to start building actual programs instead of only practicing individual Python concepts.

A calculator seemed like a good first project because it allowed me to combine several things I was learning into one application.

It is a simple project, but it gave me a better understanding of how different parts of a Python program work together.

---

## Future Improvements

There are several things I would like to improve as I learn more Python:

* [ ] Improve input validation
* [ ] Handle invalid text input more safely
* [ ] Add calculation history
* [ ] Add more mathematical operations
* [ ] Improve the command-line interface
* [ ] Add a graphical user interface
* [ ] Organize the project into multiple files
* [ ] Add automated tests
* [ ] Improve error messages
* [ ] Add better output formatting

These improvements are planned ideas rather than features currently included in the project.

---

## Contributing

This is mainly a learning project, but feedback and suggestions are welcome.

If you find something that could be improved, feel free to open an issue or submit a pull request.

---

## License

This project is intended for learning and experimentation.

You are welcome to explore the code and use it as a reference while learning basic Python programming.

---

## About

This project represents one of my early steps into Python programming.

I'm using small projects like this to strengthen my fundamentals and gradually move toward building larger and more useful applications.

More projects and improvements will be added as I continue learning.

---

## Support

If you found the project useful or interesting, consider giving the repository a star.

Thanks for checking it out.

