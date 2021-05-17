# SecEmailApi

Данный файл представляет собой модуль для работы c API https://www.1secmail.com/api/

# Функции:

```python
from api import Email

# Получаем список почт.

emails = Email.get_email(3)  # Result: ['w4qave00g@1secmail.org', 'vygj9g@1secmail.com', 'qix5yn6ec@xojxe.com']

# Проверяем, есть ли сообщения на почте. Возвращает пустой список если нету писем

messages = Email.check_mailbox(emails[0]) # Result: [{'id': 190556001, 'from': 'adolf_githuber@rambler.com', 'subject': '123', 'date': '2021-05-17 13:39:01'}] 

# Получаем подробную информациб о письме по  его id

message = Email.fetching_message(email[0], 190556001) # Result: {'id': 190556001, 'from': 'adolf_githuber@rambler.com', 'subject': '123', 'date': '2021-05-17 13:39:01', 'attachments': [], 'body': '', 'textBody': '\n\xa0\nПроверка\n\xa0\n--\nАртём Сапгиров', 'htmlBody': ''}

# Получаем фаил из письма

file = Email.attachment_download(email[0], 190556001, 'FILE_NAME') # Возвращает файл

# Echo функция, ожидает входящее письмо, и возвращает полное его содержимое
	
message = Email.message_handler(email[0]) # Result: {'id': 190556001, 'from': 'adolf_githuber@rambler.com', 'subject': '123', 'date': '2021-05-17 13:39:01', 'attachments': [], 'body': '', 'textBody': '\n\xa0\nПроверка\n\xa0\n--\nАртём Сапгиров', 'htmlBody': ''}
	
```

