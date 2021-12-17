class Repository:

    def get_content(self)->str:
        raise Exception("Method Not Implemented.")

class Sender:

    def send(self, content:str):
        raise Exception("Method Not Implemented.")

class FileRepository(Repository):

    def get_content(self)->str:
        return "From file."

class EmailSender(Sender):

    def send(self, content:str):
        print("Sending by email. Content: {}".format(content))

class SendContentToSubscribersUseCase:

    def __init__(self, repo:Repository, sender:Sender) -> None:
        self.__repo:Repository = repo
        self.__sender:Sender = sender

    def send(self):
        content = self.__repo.get_content()
        self.__sender.send(content)

use_case = SendContentToSubscribersUseCase(FileRepository(), EmailSender())
use_case.send()
