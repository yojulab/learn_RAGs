# 사용자의 나이를 입력받아 성인 여부 판단하는 프로그램
import os

def is_adult(age):
    # Get threshold from environment variable or use default 20
    adult_threshold = int(os.environ.get('ADULT_THRESHOLD', 20))
    # Ensure age is treated as a number
    age = int(age)
    if age >= adult_threshold:
        return True
    else:
        return False

def test_with_examples():
    """Test the program with example ages"""
    example_ages = [15, 20, 25, 18, 21]
    
    print("\n===== Testing with example data =====")
    # Get the current threshold for reference
    adult_threshold = int(os.environ.get('ADULT_THRESHOLD', 20))
    print(f"Current adult threshold: {adult_threshold}\n")
    
    for age in example_ages:
        result = "adult" if is_adult(age) else "not an adult"
        print(f"Age {age}: {result}")
    print("===================================\n")

def main():
    try:
        # Add option to run with example data
        mode = input("Press 'E' to run examples or any other key to enter your age: ").strip().upper()
        
        if mode == 'E':
            test_with_examples()
            return
            
        # Explicitly convert input to integer
        age_input = input("Enter your age: ")
        age = int(age_input)
        
        if is_adult(age):
            print(f"You are an adult. Age: {age}")
        else:
            print(f"You are not an adult. Age: {age}")
    except ValueError:
        print("Please enter a valid age (number).")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
