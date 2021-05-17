import requests
from time import sleep

def get_login(email: str):
    try:
        email = email.split('@')
    except Exception as Error:
        raise Error
    return email


class Email:
    @staticmethod
    def get_email(count=1):
        """
        :param count: How many email addresses you need
        :return: Array with email addresses
        """
        request = requests.get(f'https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={str(count)}').json()
        return request

    @staticmethod
    def check_mailbox(email: str):
        """
        :param email: Email address
        :return: Dict:
        id	Message id
        from	Sender email address
        subject	Subject
        date	Receive date
        """
        email = get_login(email)
        request = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={email[0]}&domain={email[1]}').json()
        return request

    @staticmethod
    def fetching_message(email: str, message_id: int):
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
        email = get_login(email)
        request = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={email[0]}&domain={email[1]}&id={str(message_id)}').json()
        return request

    @staticmethod
    def attachment_download(email: str, message_id: int, file: str):
        """
        :param email: Email address
        :param message_id: message_id. Takes from func check_mailbox
        :param file: filename of attachment
        :return: file
        """
        email = get_login(email)
        request = requests.get(f'https://www.1secmail.com/api/v1/?action=download&login={email[0]}&domain={email[1]}&id={str(message_id)}&file={file}')
        return request

    @staticmethod
    def message_handler(email: str):
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
        data = len(Email.check_mailbox(email))
        while len(Email.check_mailbox(email)) == data:
            sleep(1)
        return Email.fetching_message(email, Email.check_mailbox(email)[-1]['id'])
