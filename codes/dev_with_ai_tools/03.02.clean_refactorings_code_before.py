# 사람들의 평균 나이를 구하는 함수
def calculate_avg_age(people):
    total_age = 0
    for person in people:
        total_age += person['age']
    return total_age / len(people)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(10))
    print(factorial(0))
    print(factorial(-5))