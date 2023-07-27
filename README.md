Условия домашки

Контекст: зачем решать подобные задачи

Фреймворк Django существует довольно давно и обзавелся за это время большим количеством инструментов автоматизации, 
в том числе для реализации расширения стандартного механизма CRUD.

Популярность магазина значительно выросла. В связи с этим продакт-менеджер предложил добавить возможность пользователям 
заполнять карточки продуктов и при этом расширить функционал веб-приложения.

Критерий выполнения заданий
Результат всего задания залейте в GitHub и сдайте в виде ссылки на репозиторий.

Задание 1
Продолжаем работать с проектом из предыдущего домашнего задания. Для модели продуктов реализуйте механизм CRUD, 
задействовав модуль 

django.forms
.

Условия для пользователей:

могут создавать новые продукты;
не могут загружать запрещенные продукты на платформу.
Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, 
чтобы нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.

Задание 2
Добавьте новую модель «Версия», которая должна содержать следующие поля:

продукт,
номер версии,
название версии,
признак текущей версии.
При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

Задание 3
Для формы работы с продуктом добавьте реализацию работы с формсетами для версий продукта. При этом версия может быть 
внесена только в существующий продукт.

Все созданные формы нужно стилизовать так, чтобы они были в единой стилистике оформления всей платформы. Для этого 
можно воспользоваться методом 

__init__
 либо самостоятельно изучить пакет crispy-forms: https://pypi.org/project/django-crispy-forms/.

* Дополнительное задание
В один момент времени может быть только одна активная версия продукта, поэтому при изменении версий необходимо 
проверять, что пользователь в качестве активной версии указал только одну. В случае возникновения ошибки вернуть 
сообщение пользователю и попросить выбрать только одну активную версию.

Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.

**********************************************************************************************************************

NOTE:
для функционирования приложения необходимо создать в корне проекта файл .env в котором указать значения
переменных окружения:
SECRET_KEY=
DB_ENGINE=django.db.backends.postgresql
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=