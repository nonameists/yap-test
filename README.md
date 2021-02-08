# yap-test
Test task for backend tests developer

## Необходимо написать тесты, проверяющие решение студента, и дающие подсказки в случае ошибки.

Что предоставляет платформа для тестов:
- Решение студента импортируется в тестовый модуль, соответственно все переменные студента доступны в нем. 
- `user_code` — переменная, в которой в виде строки хранится весь код студента.
- `output` — stdout работы файла с кодом студента (все его `print()`) в виде строки.
- в тестовом модуле можно импортировать разные библиотеки, например `re`, а также пользоваться любыми фишками языка python.


Тест должен проверить правильность конечного решения студента, а также шаги, которые к этому решению привели.  
Описание найденной ошибки(assert message) должно подсказывать что не так сделал студент. 

Часто бывает, что студенты изменяют или удаляют исходные переменные, которые мы им даем в прекоде, что потом часто заводит их в тупик.  
Сама проверка происходит, используя `assert` и текстовое сообщения студенту.

`assert False, 'Вы ошиблись в выводе на экран'`

В файлах с задачами выложен прекод (который мы отдаем студентам) и авторское решение, по которому пишутся тесты.  

## Список файлов

- `precode.py` — прекод для студента
- `author.py` — эталонное решение
- `test.py` — напишите ваш тест в этом файле

#### Удачи!
