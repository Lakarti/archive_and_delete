Этот проект включает в себя набор функций для управления файлами в указанных директориях, включая удаление старых папок и создание архивов PDF-файлов.

## Функциональность

### 1. Конфигурация логирования

Функция `configure_logging` настраивает логирование для приложения, используя вращающийся файловый обработчик. Логи записываются в файл `log.txt` и включают временную метку, уровень логирования и сообщение.

### 2. Удаление старых папок

Функция `delete_old_folders` удаляет папки в указанной директории, которые старше заданного порога времени. Порог времени по умолчанию составляет 5 дней.

### 3. Создание архивов

Функция `create_archives` создает ZIP-архивы для PDF-файлов в указанной директории. Архивы организуются по дате последнего изменения файлов.

## Использование

1. Замените значения переменных `brightness_directory`, `example_directory` и `orders_directory` на фактические пути к директориям вашего проекта.

2. Вызовите функцию `configure_logging` один раз перед вызовом функций `delete_old_folders` и `create_archives`.

3. Вызовите функцию `delete_old_folders` для каждой директории, которую вы хотите проверить и очистить от старых папок.

4. Вызовите функцию `create_archives` для каждой директории, в которой вы хотите создать архивы PDF-файлов.

## Пример использования

```python
# Замените 'path/to/your/folder' на фактический путь к вашей основной директории
brightness_directory = 'path/to/your/folder'
example_directory = 'path/to/your/folder'
orders_directory = 'path/to/your/folder'

# Вызовите configure_logging один раз перед вызовом delete_old_folders и create_archives
configure_logging()

delete_old_folders(brightness_directory)
delete_old_folders(example_directory)
create_archives(orders_directory)
