from abc import ABC, abstractmethod

class TextComponent(ABC):
    """텍스트 컴포넌트의 인터페이스"""
    
    @abstractmethod
    def render(self) -> str:
        """텍스트를 렌더링하는 메서드"""
        pass


class PlainText(TextComponent):
    """기본 텍스트 구현체"""
    
    def __init__(self, text: str):
        self.text = text
    
    def render(self) -> str:
        return self.text


class TextDecorator(TextComponent):
    """텍스트 데코레이터 추상 클래스"""
    
    def __init__(self, component: TextComponent):
        self.component = component
    
    @abstractmethod
    def render(self) -> str:
        pass


class BoldDecorator(TextDecorator):
    """텍스트를 굵게 표시하는 데코레이터"""
    
    def render(self) -> str:
        return f"<b>{self.component.render()}</b>"


class ItalicDecorator(TextDecorator):
    """텍스트를 이탤릭체로 표시하는 데코레이터"""
    
    def render(self) -> str:
        return f"<i>{self.component.render()}</i>"


class UnderlineDecorator(TextDecorator):
    """텍스트에 밑줄을 추가하는 데코레이터"""
    
    def render(self) -> str:
        return f"<u>{self.component.render()}</u>"


class ColorDecorator(TextDecorator):
    """텍스트에 색상을 입히는 데코레이터"""
    
    def __init__(self, component: TextComponent, color: str):
        super().__init__(component)
        self.color = color
    
    def render(self) -> str:
        return f"<span style='color:{self.color}'>{self.component.render()}</span>"


# 클라이언트 코드 예제
if __name__ == "__main__":
    # 기본 텍스트
    plain_text = PlainText("Hello, Decorator Pattern!")
    print("일반 텍스트:", plain_text.render())
    
    # 굵은 텍스트
    bold_text = BoldDecorator(plain_text)
    print("굵은 텍스트:", bold_text.render())
    
    # 이탤릭 텍스트
    italic_text = ItalicDecorator(plain_text)
    print("이탤릭 텍스트:", italic_text.render())
    
    # 여러 데코레이터 조합 - 굵은 이탤릭 텍스트
    bold_italic_text = BoldDecorator(ItalicDecorator(plain_text))
    print("굵은 이탤릭 텍스트:", bold_italic_text.render())
    
    # 더 복잡한 조합 - 빨간색 굵은 밑줄 텍스트
    complex_text = ColorDecorator(
        BoldDecorator(
            UnderlineDecorator(
                PlainText("복잡한 데코레이션")
            )
        ), 
        "red"
    )
    print("복잡한 데코레이션:", complex_text.render())
    
    # 런타임에 동적으로 꾸미기
    print("\n동적 데코레이션 예제:")
    text = PlainText("동적 스타일 적용")
    
    # 사용자 입력에 따라 스타일 적용 시뮬레이션
    styles = ["bold", "italic", "underline", "color:blue"]
    
    for style in styles:
        if style == "bold":
            text = BoldDecorator(text)
        elif style == "italic":
            text = ItalicDecorator(text)
        elif style == "underline":
            text = UnderlineDecorator(text)
        elif style.startswith("color:"):
            color = style.split(":")[1]
            text = ColorDecorator(text, color)
    
    print("최종 결과:", text.render())
    print("HTML 출력:", text.render())