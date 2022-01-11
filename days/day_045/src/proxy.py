from abc import ABC, abstractmethod
'''
Proxy
Intent:
  "Provide a surrogate or placeholder for another object to control access to it."
'''
class TelevisionOperations(ABC):
    @abstractmethod
    def volume_up(self):
        pass
    
    @abstractmethod
    def volume_down(self):
        pass


class TelevisionAPI(TelevisionOperations):
    
    def volume_up(self):
        print("Volume up")
    
    def volume_down(self):
        print("Volume down")

    
class RemoteControlProxy(TelevisionOperations):

    def __init__(self, tv:TelevisionAPI) -> None:
        self.__tv = tv
    
    def volume_up(self):
        print("sending command volume up.")
        self.__tv.volume_up()
    
    def volume_down(self):
        print("sending command volume down.")
        self.__tv.volume_up()


def client_operations():
    tv = TelevisionAPI()
    proxy = RemoteControlProxy(tv)
    proxy.volume_up()
    proxy.volume_down()

client_operations()
