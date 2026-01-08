import itertools
import re
import sys

def solve_puzzle():
    print("="*40)
    print("宝洁/Aon Digit Challenge Solver")
    print("Format example: xx-125 (means ? x ? x ? - ? = 125)")
    print("Supported: + - x * / ÷")
    print("Input 'q' to exit")
    print("="*40)

    while True:
        try:
            # 1. Get user input
            user_input = input("\nEnter puzzle (e.g., xx-125): ").strip().lower()
            
            if user_input == 'q':
                print("Exiting program.")
                break
            
            if not user_input:
                continue

            # 2. Parse input: separate operators and target number
            # Match non-digits as operators, digits as result
            match = re.match(r'([+\-*x/÷]+)(\d+)', user_input)
            
            if not match:
                print("❌ Format error! Please input operators followed by the number (e.g., +*20)")
                continue

            ops_input = match.group(1)
            target = int(match.group(2))
            
            # Convert user input symbols to Python operators
            # x -> *, ÷ -> /
            py_ops = []
            display_ops = []
            for char in ops_input:
                if char == 'x' or char == '*':
                    py_ops.append('*')
                    display_ops.append('x')
                elif char == '÷' or char == '/':
                    py_ops.append('/')
                    display_ops.append('÷')
                else:
                    py_ops.append(char)
                    display_ops.append(char)

            # Number of variables = number of operators + 1
            num_vars = len(py_ops) + 1
            
            print(f"🔍 Searching for {num_vars} non-repeating digits (1-9) where '{''.join(display_ops)}' equals {target}...")

            found = False
            
            # 3. Generate permutations (non-repeating combinations of 1-9)
            # itertools.permutations ensures unique digits in each set
            digits = range(1, 10)
            
            for nums in itertools.permutations(digits, num_vars):
                # Construct arithmetic expression string
                # Example: nums=(2,7,9,1), ops=['*','*','-'] -> expression "2*7*9-1"
                expression = str(nums[0])
                display_expr = str(nums[0])
                
                valid_calc = True
                
                for i, op in enumerate(py_ops):
                    # Special check for division: divisor cannot be 0 (though range starts at 1, good for safety)
                    if op == '/' and nums[i+1] == 0:
                        valid_calc = False
                        break
                    
                    expression += op + str(nums[i+1])
                    display_expr += display_ops[i] + str(nums[i+1])
                
                if not valid_calc:
                    continue

                # 4. Calculate and verify
                try:
                    # Note: Aon/P&G tests usually follow standard math precedence (MDAS)
                    # Python's eval() handles this correctly
                    result = eval(expression)
                    
                    # Compare floating point numbers with a small tolerance
                    if abs(result - target) < 0.0001:
                        print(f"✅ Solution: {display_expr}={target}")
                        found = True
                        break # Stop after finding the first solution
                            
                except ZeroDivisionError:
                    continue

            if not found:
                print("⚠️ No solution found (Please check input or if the puzzle requires repeating digits)")

        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    solve_puzzle()
