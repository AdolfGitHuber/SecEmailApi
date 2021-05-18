import requests
from time import sleep


class Email:
    def __init__(self):
        self.api_url = "https://www.1secmail.com/api/v1/"

    def get_email(self, count: int = 1) -> dict:
        """
        :param count: How many email addresses you need
        :return: Array with email addresses
        """
        return requests.get(
            f'{self.api_url}?action=genRandomMailbox&count={count}').json()

    def check_mailbox(self, email: str) -> dict:
        """
        :param email: Email address
        :return: Dict:
        id	Message id
        from	Sender email address
        subject	Subject
        date	Receive date
        """
        email_data = email.split('@')
        return requests.get(f'{self.api_url}?action=getMessages&'
                            f'login={email_data[0]}&'
                            f'domain={email_data[1]}').json()

    def fetching_message(self, email: str, message_id: int) -> dict:
        """
        :param email: Email address
        :param message_id: message_id. Takes from func check_mailbox
        :return: Dict:
            id	Message id
            from	Sender email address
            subject	Subject
            date	Receive date
            attachments	Attachments list
            body	Message body (html if exists, text otherwise)
            textBody	Message body (text)
            htmlBody	Message body (html)
        """
        email_data = email.split('@')
        return requests.get(f'{self.api_url}?action=readMessage&'
                            f'login={email_data[0]}&domain={email_data[1]}&'
                            f'id={message_id}').json()

    def attachment_download(self, email: str, message_id: int,
                            file: str) -> requests.Response:
        """
        :param email: Email address
        :param message_id: message_id. Takes from func check_mailbox
        :param file: filename of attachment
        :return: file
        """
        email_data = email.split('@')
        return requests.get(f'{self.api_url}?action=download&'
                            f'login={email_data[0]}&domain={email_data[1]}&'
                            f'id={message_id}&file={file}')

    def message_handler(self, email: str) -> dict:
        """
        :param email:  Email address
        :return: Dict:
            id	Message id
            from	Sender email address
            subject	Subject
            date	Receive date
            attachments	Attachments list
            body	Message body (html if exists, text otherwise)
            textBody	Message body (text)
            htmlBody	Message body (html)
        """
        while len(self.check_mailbox(email)) == len(self.check_mailbox(email)):
            sleep(1)
        return self.fetching_message(email,
                                     self.check_mailbox(email)[-1]['id'])
