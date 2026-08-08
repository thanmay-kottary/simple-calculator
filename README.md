🧮 Simple Python Calculator
--
A simple command-line calculator built using Python.

I created this project while learning the basics of Python. The idea was to make a small calculator that can do more than just addition and subtraction, while also giving me some practice with functions, loops, conditions, user input, and basic error handling.

It's a simple project, but it helped me understand how different parts of a Python program can work together.

---

✨ What Can It Do?
-
The calculator currently supports 7 different operations:

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 📊 Percentage
- √ Square Root
- 🔢 Power

There is also an Exit option if you want to stop using the calculator.

After completing a calculation, you can choose whether you want to perform another calculation or exit the program.

---

🖥️ How It Works
-
When you start the program, you'll see a simple menu:

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
-
You simply enter the number corresponding to the operation you want.

For example:

Enter choice : 1
Enter first number: 25
Enter second number: 15

The sum is: 40.0

After that, the calculator asks:

Do you want to perform another calculation? (yes/no):

You can type "yes" to continue or "no" to exit.

---

📌 Operations
-
1. Addition

Adds two numbers together.

25 + 15 = 40


2. Subtraction

Subtracts the second number from the first.

25 - 15 = 10


3. Multiplication

Multiplies two numbers.

25 × 15 = 375


4. Division

Divides the first number by the second.

25 ÷ 5 = 5

The program also checks if the denominator is zero before performing division.


5. Percentage

Calculates the percentage of a part compared to a whole.

Part = 25
Whole = 100

Percentage = 25%

The program also checks that the whole value is not zero.


6. Square Root

Finds the square root of a number.

√25 = 5

The program checks for negative numbers before calculating the square root.


7. Power

Raises a number to a specified power.

2³ = 8

---

🛠️ Technologies Used
-

- Python 3
- Command Line / Terminal

No external libraries are required to run this project.

---

📂 Project Structure
-
The project is intentionally kept simple:

Simple-Python-Calculator/
- │
- ├── simcalculator.py
- └── README.md

"simcalculator.py"

This is the main Python file containing the calculator program and all of its operations.

"README.md"

This file explains the project, how it works, and how to run it.

---

🚀 How to Run the Project
-

1. Clone the repository

Open your terminal and run:

git clone YOUR_REPOSITORY_URL

Replace "YOUR_REPOSITORY_URL" with the URL of your GitHub repository.


2. Open the project folder

cd Simple-Python-Calculator


3. Run the Python file

python simcalculator.py

Depending on your system, you may need to use:

python3 simcalculator.py

---

💡 What I Learned From This Project
-

Even though this is a small project, I used several important Python concepts while building it.

Functions

Each mathematical operation is written as its own function.

For example:

def add(x, y):
    return x + y

This makes the code easier to understand and keeps each operation separate.

Conditional Statements

The program uses "if", "elif", and "else" statements to decide which operation the user selected.

Loops

The calculator uses a loop so the user can perform multiple calculations without restarting the program.

User Input

The program takes numbers and choices directly from the user through the terminal.

Basic Error Handling

The calculator includes checks for situations such as attempting to divide by zero or finding the square root of a negative number.

---

🎯 Why I Made This
-

I wanted to build something small that I could actually run and use while learning Python.

Instead of only following tutorials and writing individual examples, I wanted to put some of the concepts I was learning together into one working program.

This calculator is one of my early Python projects, and I plan to improve it as I learn more.

---

🔮 Possible Future Improvements
-

There are several things I could add to this project in the future:
- [ ] Improve input validation
- [ ] Handle invalid text input more safely
- [ ] Add a calculation history
- [ ] Add more mathematical operations
- [ ] Improve the command-line interface
- [ ] Add a graphical user interface (GUI)
- [ ] Organize the project into multiple files
- [ ] Add automated tests
- [ ] Improve the error messages
- [ ] Add more user-friendly formatting

---

🤝 Contributions
-

This is mainly a learning project, but suggestions and improvements are welcome.
If you notice something that could be improved, feel free to open an issue or create a pull request.

---

📄 License
-
This project is open for learning and experimentation.
You are welcome to explore the code and use it as a reference for learning basic Python programming.

---

👨‍💻 About the Project
-
This calculator is a beginner-level Python project created to practice programming fundamentals.
More projects will be added as I continue learning and improving my programming skills.

⭐ If you found this project useful or interesting, feel free to give the repository a star!
-
