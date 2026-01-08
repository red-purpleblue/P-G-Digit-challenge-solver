P&G / Aon Digit Challenge Solver 

A Python-based utility designed to solve the Digit Challenge (interactive equation puzzles) commonly found in P&G (Procter & Gamble) and Aon (cut-e) online assessments.

🚀 Features

Fast Solving: Instantly finds the correct digits (1-9) to complete the equation.

Smart Parsing: Automatically detects operators and target numbers from simple shorthand input (e.g., xx-125).

Rule Compliance: Adheres to standard assessment rules (non-repeating digits, standard mathematical precedence).

Lightweight: No external dependencies required (uses standard Python libraries).

🛠️ Requirements  Python 3.x

📖 How to Use

Run the script: python solver.py 

Input Format: Type the operators followed by the target number. 

? + ? x ? = 24 -> Input: +x24

? x ? x ? - ? = 125 -> Input: xx-125 (or **-125)

Get Solution: The script will output the correct sequence of numbers.

Example Output: ✅ Solution: 2x7x9-1=125

⚠️ Disclaimer 

This tool is for educational and practice purposes only. Please ensure you comply with the terms and conditions of any assessment you undertake.
