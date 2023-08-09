## Условия домашки

‍Из-за наплыва пользователей стало появляться слишком много продуктов, и администратор лично не успевает их обрабатывать. 
Поэтому появилась необходимость проводить ручное модерирование продуктов, которые добавляются на платформу. 
Для этих целей было решено нанять модераторов.

#### Контекст: зачем решать подобные задачи?
Такая задача встречается разработчику на проектах любого уровня: от простого сайта до сложного личного кабинета 
государственной структуры. Именно поэтому важно научиться распределять права доступа пользователей 
по их ролям в веб-сервисе.

### Задание 1
Продолжаем работать с проектом. Создайте группу для роли модератора и опишите необходимые доступы:

- может отменять публикацию продукта,
- может менять описание любого продукта,
- может менять категорию любого продукта.

Недостающее поле признака публикации необходимо добавить таким образом, чтобы можно было определять статус продукта. 
Можно использовать 

    BooleanField
 со значением False по умолчанию или 

    CharField 
 с указанием вариантов значений (choises). При этом по умолчанию должен быть вариант, который не предполагает 
публикацию продукта.

### Задание 2
Реализуйте решение, которое проверит, что редактирование продукта доступно только его владельцу.

* ### Дополнительное задание
Выделите отдельную роль для пользователя контент-менеджера, который может управлять публикациями в блоге. 
Также не забудьте реализовать проверки на то, что обычный пользователь или модератор из другого отдела 
не сможет ничего изменить в разделе блога.




**********************************************************************************************************************

### NOTE:
для функционирования приложения необходимо создать в корне проекта файл .env в котором указать значения
переменных окружения:
- SECRET_KEY=
- DB_ENGINE=django.db.backends.postgresql
- DB_NAME=
- DB_USER=
- DB_PASSWORD=
- DB_HOST=
- DB_PORT=
- EMAIL_HOST=
- EMAIL_PORT=
- EMAIL_HOST_USER=
- EMAIL_HOST_PASSWORD=