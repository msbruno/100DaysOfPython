class EmailSender:
    def send(self, content:str):
        print("Sending by email. Content: {}".format(content))
        
class FileRepository:
    def get_content(self)->str:
        return "From file."

class SendContentToSubscribersUseCase:
    def __init__(self) -> None:
        self.__repo = FileRepository()
        self.__sender = EmailSender()

    def send(self):
        content = FileRepository().get_content()
        EmailSender().send(content)
   
        
use_case = SendContentToSubscribersUseCase()
use_case.send()
