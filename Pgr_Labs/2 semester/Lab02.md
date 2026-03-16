# 👾 Lab02: Project Setup 
> This laboratory work is implemented in the [Clockly](https://github.com/cyjiky/Clockly) repository.

## Task:

```text 
• Create a Git repository and initialize it with git init
• Add a .gitignore file for your programming language
• Set up a project configuration file (package.json, Cargo.toml, or pyproject.toml)
• Add authors and a license (use MIT or ISC if unsure)
• Split your code from Task 1 into multiple files to form a proper library
• Create a separate project to demonstrate how to use your library
• Link the example project to your library (use local dependencies)
• Write usage examples showing how to use all functionalities from Task 1
• Commit and push your code to GitHub

```

## Description
Clockly is a mobile calendar application. The project is designed to be an advanced alternative to Google Calendar, offering extended functionality such as custom summaries for selected timeframes, flexible configuration, and other additional features.

## Structure 

```text 
📁.                                 project folder
 ├── 📁 backend                     server-side logic
 |    ├── 📁 auth                   authentication & authorization
 |    ├── 📁 DTOs                   data transfer objects 
 |    ├── 📁 routers                api route definition
 |    ├── 📁 postgre                
 |    ├── 📁 services               logic layer
 |    |    ├── 📁 core services     
 |    |    ├── 📁 postgre service   
 |    |    └── 📁 redis             
 |    ├── 📁 utils                  shared helper functions
 |    ├── 📝 main.py                backend entry point
 |    ├── ⚙️ .env                   environment variables (excluded from git)
 |    ├── ⚙️ .gitignore             vcs ignore 
 |    ├── 🐳 Containerfile          backend container build 
 |    └── 📝 pyproject.toml         python dependencies & config
 ├── 📁 frontend                    client-side application (development has not started)
 |    ├── 📁 app                    application routing & pages
 |    ├── 📁 assets                 static files
 |    ├── 📁 components             reusable UI elements
 |    ├── 📁 constants              global constants & configurations
 |    ├── 📁 hooks                  custom state & lifecycle hooks
 |    ├── 📝 package.json           frontend dependencies & scripts
 |    ├── ⚙️ .env                   environment variables (excluded from git)
 |    ├── ⚙️ .gitignore             vcs ignore 
 |    └── 🐳 Containerfile          frontend container build 
 ├── 🐳 compose.yaml                docker compose orchestration
 ├── 📄LICENCE                      LICENCE
 └── 📍README.md                    project description 
```

## Execution Results

1. Added a ``.gitignore`` file to both parts of the project (backend and frontend)
2. For the backend, we chose to use ``pyproject.toml`` instead of ``requirements.txt.`` This decision is justified by the transition to modern Python packaging standards and more convenient dependency management
    - For the frontend, a separate ``package.json`` file was created to manage all necessary dependencies and libraries
3. The project is published under the ``MIT License``
4. Containers were created and configured to simplify launching the application. The naming convention (``Containerfile``) was chosen deliberately so that the configurations can be used not only with Docker but also with similar alternative tools, depending on user preference
5. A comprehensive [README](https://github.com/cyjiky/Clockly/blob/main/README.md) was written in the main repository, containing startup instructions and descriptions of the project architecture and structure
6. The project is being developed by two contributors ([@cyjiky](https://github.com/cyjiky) $\cdot$ [@yeghor](https://github.com/yeghor))

## Project status 
The project is currently under development

---

Ця лабораторна робота виконується в [Clockly](https://github.com/cyjiky/Clockly) репозиторії.

## Опис 

Clockly — це мобільний додаток-календар. Проект задуманий як просунутий аналог Google Calendar з розширеним функціоналом: кастомним підбиттям підсумків за вибраний проміжок часу, гнучким налаштуванням та іншими додатковими можливостями.

## Структура проекту  

```text 
📁.                                 project folder
 ├── 📁 backend                     server-side logic
 |    ├── 📁 auth                   authentication & authorization
 |    ├── 📁 DTOs                   data transfer objects 
 |    ├── 📁 routers                api route definition
 |    ├── 📁 postgre                
 |    ├── 📁 services               logic layer
 |    |    ├── 📁 core services     
 |    |    ├── 📁 postgre service   
 |    |    └── 📁 redis             
 |    ├── 📁 utils                  shared helper functions
 |    ├── 📝 main.py                backend entry point
 |    ├── ⚙️ .env                   environment variables (excluded from git)
 |    ├── ⚙️ .gitignore             vcs ignore 
 |    ├── 🐳 Containerfile          backend container build 
 |    └── 📝 pyproject.toml         python dependencies & config
 ├── 📁 frontend                    client-side application (development has not started)
 |    ├── 📁 app                    application routing & pages
 |    ├── 📁 assets                 static files
 |    ├── 📁 components             reusable UI elements
 |    ├── 📁 constants              global constants & configurations
 |    ├── 📁 hooks                  custom state & lifecycle hooks
 |    ├── 📝 package.json           frontend dependencies & scripts
 |    ├── ⚙️ .env                   environment variables (excluded from git)
 |    ├── ⚙️ .gitignore             vcs ignore 
 |    └── 🐳 Containerfile          frontend container build 
 ├── 🐳 compose.yaml                docker compose orchestration
 ├── 📄LICENCE                      LICENCE
 └── 📍README.md                    project description 
```


## Результати виконання

1. Додано ``.gitignore`` файл для всіх частин проекту (backend and frontend).
1. Добавлен ``.gitignore`` в обе части проекта (бэкенд и фронтенд)
2. У бекенд було обрано та узгоджено написання ``pyproject.toml`` замість ``requirements.txt``. Аргуменовано переходом на сучасні стандарти упаковки Python-проектів та зручнішим управлінням залежностями.
    - у фронтенді створено окремий файл ``package.json``, що містить у собі всі залежності та необхідні бібліотеки
3. Проект опублікований під ліцензією ``MIT License``
4. Також створені та налаштовані контейнери для спрощеного запуску програми (іменування аргументовані тим, щоб можливо було використовувати ці контейнери не тільки для Docker, а й схожих програм залежно від переваг)
5. Написаний докладний [README](https://github.com/cyjiky/Clockly/blob/main/README.md) в основному репозиторії з інструкцією для запуску, описом архітектури та структури проекту
6. Розробка здійснюється двома контриб'юторами ([@cyjiky](https://github.com/cyjiky) $\cdot$ [@yeghor](https://github.com/yeghor))

## Статус проекту 
Проєкт зараз перебуває на стадії розробки