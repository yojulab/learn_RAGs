from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def save(self):
        pass

class PdfDocument(Document):
    def save(self):
        print("PDF로 저장")

class WordDocument(Document):
    def save(self):
        print("Word로 저장")

# 팩토리 메서드 패턴 적용
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass
    
    def operation(self):
        # 팩토리 메서드를 이용해 객체 생성
        document = self.create_document()
        # 생성된 객체 사용
        document.save()

class PdfDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PdfDocument()

class WordDocumentCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()

# 클라이언트 코드 예제
if __name__ == "__main__":
    print("PDF 문서 생성:")
    pdf_creator = PdfDocumentCreator()
    pdf_document = pdf_creator.operation()

    print("\nWord 문서 생성:")
    word_creator = WordDocumentCreator()
    word_document = word_creator.operation()