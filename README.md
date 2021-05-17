# SecEmailApi

Данный файл представляет собой модуль для работы c API https://www.1secmail.com/api/

# Функционал:
  
1. Получаем почту(ы)
"""
from api import Email

emails = Email.get_email(3) # Возвращает список из 3-ех почт.
print(emails)

Result: ['w4qave00g@1secmail.org', 'vygj9g@1secmail.com', 'qix5yn6ec@xojxe.com']
"""
