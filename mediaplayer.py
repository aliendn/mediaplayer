from abc import ABC, abstractmethod

class Media(ABC):

    @abstractmethod
    def play(self):
        pass

    def mylocation(self):
        my_media = self.play()
        loc = self.__class__.loc
        if "https://" in loc:
            result = f"{my_media.media_player()}"
        if "drive://" in loc:
            result = f"{my_media.media_player()}"            
        return result

class MediaPlayer1(Media):
    loc = ("https://") 

    def play(self):
        return MediaLocation1()


class MediaPlayer2(Media):
    loc = ("drive://") 

    def play(self):
        return MediaLocation2()

class Location(ABC):

    @abstractmethod
    def media_player(self):
        pass


class MediaLocation1(Location):

    def media_player(self):
        return 'in media ba web play shode ast'


class MediaLocation2(Location):

    def media_player(self):
        return 'in media ba goshi play shode ast'


def player(media: Media):
    print(f"{media.mylocation()}")


if __name__ == "__main__":
    print("music shoma play shod")
    player(MediaPlayer1())
    print("\n")

    print("music shoma play shod")
    player(MediaPlayer2())