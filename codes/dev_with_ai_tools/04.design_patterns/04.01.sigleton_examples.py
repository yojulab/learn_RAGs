# 싱글톤 클래스 생성
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, value):
        self.value = value

# 싱글톤 클래스 테스트
if __name__ == "__main__":
    singleton1 = Singleton("첫 번째")
    singleton2 = Singleton("두 번째")
    
    print(singleton1.value)  # 출력: 두 번째
    print(singleton2.value)  # 출력: 두 번째
    print(singleton1 is singleton2)  # 출력: True
    print(id(singleton1), id(singleton2))  # 출력: 동일한 ID
    print(singleton1 == singleton2)  # 출력: True