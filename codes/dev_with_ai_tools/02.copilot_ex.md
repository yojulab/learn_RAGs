# 성인 여부 확인 프로그램 개발 과정

## 1. 초기 요구사항 정의

**프롬프트:**
```
사용자의 나이를 입력받아 성인 여부를 판단하는 파이썬 프로그램을 작성해주세요. 
환경 변수로 성인 기준 나이를 설정할 수 있도록 하고, 기본값은 20으로 설정해주세요.
```

## 2. 기본 코드 구현

이 프롬프트를 통해 기본적인 프로그램 구조가 생성되었습니다:

```python
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

def main():
    try:
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
```

## 3. 테스트 데이터 추가 요청

**프롬프트:**
```
예제 데이터 만들어 잘 동작하는지 확인
```

이 프롬프트를 통해 다양한 예제 나이로 프로그램을 테스트하는 기능이 추가되었습니다:

```python
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
```

그리고 사용자가 예제 테스트를 선택할 수 있도록 메인 함수가 수정되었습니다:

```python
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
```

## 4. 실행 방법 설명 요청

**프롬프트:**
```
실행 방법
```

이 프롬프트를 통해 다음과 같은 실행 방법 설명을 작성할 수 있었습니다:

```
실행 방법:

1. 기본 실행 (성인 기준 20세):
   python 11.copilot_ex.py
   
2. 환경 변수로 성인 기준 변경하여 실행 (예: 18세):
   Linux/Mac:
   ADULT_THRESHOLD=18 python 11.copilot_ex.py
   
   Windows (CMD):
   set ADULT_THRESHOLD=18
   python 11.copilot_ex.py
   
   Windows (PowerShell):
   $env:ADULT_THRESHOLD=18; python 11.copilot_ex.py

3. 실행 후:
   - 'E'를 입력하면 예제 데이터로 테스트
   - 다른 키를 입력하면 나이를 직접 입력하여 테스트
```

## 5. 배운 점

- 명확한 프롬프트를 작성하면 원하는 기능을 더 정확하게 구현할 수 있습니다.
- 기능을 단계별로 추가하는 것이 효과적입니다.
- 예제 데이터로 테스트하는 기능은 프로그램의 신뢰성을 높입니다.
- 실행 방법을 문서화하면 다른 사람들이 쉽게 프로그램을 사용할 수 있습니다.
- 환경 변수를 활용하면 코드 수정 없이 프로그램의 동작을 변경할 수 있습니다.