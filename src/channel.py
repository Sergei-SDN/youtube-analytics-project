import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    # api_key:str = os.getenv('YT_API_KEY')
    api_key = 'AIzaSyAt8mAr2lJQ163Dn4 - TdTJONAprKrjwV7s'



    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.channel_id = channel_id

        self.channel_data_response = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        self.title: str = self.channel_data_response['items'][0]['snippet']['title']
        self.channel_description: str = self.channel_data_response['items'][0]['snippet']['description']
        self.url: str = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count: int = int(self.channel_data_response['items'][0]['statistics']['subscriberCount'])
        self.video_count: int = int(self.channel_data_response['items'][0]['statistics']['videoCount'])
        self.view_count: int = int(self.channel_data_response['items'][0]['statistics']['viewCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel_data = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel_data, indent=4, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """возвращает объект для работы с YouTube API"""

        return build('youtube', 'v3', developerKey=cls.api_key)

    def to_json(self, filename):
        """сохраняет в файл значения атрибутов"""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.channel_data_response, file, ensure_ascii=False)

    def __str__(self):
        """отображение информации об объекте класса для пользователей"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """сложение классов"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """вычитание классов"""
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        """сравнение классов 'больше'"""
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """сравнение классов 'больше или равно'"""
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        """сравнение классов 'меньше'"""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """сравнение классов 'меньше или равно'"""
        return self.subscriber_count <= other.subscriber_count