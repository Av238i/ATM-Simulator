PROJECT STATEMENT 

- Problem Statement:
Most people use ATMs regularly, but don't see the logic behind them- checking a PIN, limiting number of attempts, and validating an amount of money before moving it in or out of account. this project turns the same logic into a simple command-line program using basic concepts of python such as loops, variables, and conditionals.

- SCOPE:
Included
1. PIN based login with a limited number of attempts. Once all attempts are exhausted, the card gets blocked
2. Checking the account balance, depositing money, and withdrawing money
3. Basic validation, such as prevention of withdrawls exceeding the available balance

Not Included
1. A real bank account or database. The PIN and balance are predefined and reset whenever the program is run.
2. Graphic user interface, i.e., a GUI-based setup
3. Multiple accounts or users

- TARGET USERS:
1. Python beginners who wish to understand how loops, conditionals, and user inputs are combined to build a small, practical program
2. Anyone curious about how a simple ATM login and menu is implemented in code

- HIGH-LEVEL FEATURES:
1. Authentication: The user is given 3 attempts to enter the correct PIN. A hint is displayed after two incorrect attempts, and the card gets blocked after the third
2. Account Operations: User can check the balance in their account, deposit or withdraw money from it, with basic input validation from each operation
3. Menu-Driven Flow: The menu continues to appear until the user chooses the exit option