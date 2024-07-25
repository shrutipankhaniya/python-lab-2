# main.py

import calculator1

def main():
    a = 10
    b = 5
    total = 100
    part = 50
    
    print(f"Addition of {a} and {b} is: {calculator1.add(a, b)}")
    print(f"Subtraction of {b} from {a} is: {calculator1.subtract(a, b)}")
    print(f"Multiplication of {a} and {b} is: {calculator1.multiply(a, b)}")
    print(f"Division of {a} by {b} is: {calculator1.divide(a, b)}")
    print(f"Percentage of {part} out of {total} is: {calculator1.percentage(total, part)}%")

if __name__ == "__main__":
    main()
