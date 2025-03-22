class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
    
    def add_subscriber(self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify_subscribers(self, news):
        for subscriber in self.__subscribers:
            subscriber.update(news)

# 옵저버 인터페이스
from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, news):
        pass 

# concrete observer
class SMSSubscriber(Subscriber):
    def update(self, news):
        print(f"SMS: {news}")

class EmailSubscriber(Subscriber):
    def update(self, news):
        print(f"Email: {news}")

if __name__ == "__main__":
    news_publisher = NewsPublisher()
    sms_subscriber = SMSSubscriber()
    email_subscriber = EmailSubscriber()

    news_publisher.add_subscriber(sms_subscriber)
    news_publisher.add_subscriber(email_subscriber)

    news_publisher.notify_subscribers("뉴스입니다.")