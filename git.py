# Инициализация нового репозитория Git
git init

# Показывает статус проекта
git status

# Подготовить файлы к отправке
git add .

# Создать коммит с сообщением
git commit -m "Первый коммит"

# Связывает папку с репозиторием
git remote add origin https://github.com/lleeoleg/student-app2.git

# Проверить
git remote -v

# Отправить изменения в удаленный репозиторий
git push -u origin main

# Клонировать репозиторий на свой компьютер
git clone https://github.com/lleeoleg/-urrency-exchange-rates-project.git

####################
# Работа с ветками #
####################

# Просмотр всех веток
git branch

# Создание новой ветки
git branch название_ветки

# Переключение на другую ветку
git checkout название_ветки

# Создание и переключение на новую ветку
git checkout -b название_ветки 
