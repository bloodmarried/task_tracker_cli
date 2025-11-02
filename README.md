<h1>Task Tracker CLI</h1>
https://github.com/bloodmarried/task_tracker_cli
https://roadmap.sh/projects/task-tracker<br>
Данный проект предназначен исключительно для самоподготовки
<h2>Описание</h2>
Данная программа сочетает в себе все те реализации, описанные в задаче, а именно:<br>
<ol>
  <li>Создание задач</li>
  <li>Редактирование задач</li>
  <li>Просмотр задач</li>
  <li>Отметка задач "В процессе" и "Выполнено"</li>
</ol>
Параметры, применяемые в CLI позиционные, данные хранятся и редактируются в файле json и все без использования сторонних библиотек
<h2>Скачивание</h2>
<code>git clone https://github.com/bloodmarried/task_tracker_cli/</code>
<h2>Использование</h2>
Для создания новой задачи в командной строке введите следующее:<br><br>
<code>py task_cli.py add "Пробежать 100 киллометров"</code><br><br>
В консоли выведится id задачи, а в файле json создаст список данных<br>
Для редактирования задачи:<br><br>
<code>py task_cli.py update 1 "Приготовить торт"</code><br><br>
Для удаления задачи:<br><br>
<code>py task_cli.py delete 1</code><br><br>
Для просмотра задач:<br><br>
<code>py task_cli.py list done</code><br><br>
Важное уточнение, если вы второй аргумент оставите пустым, то вам высветятся все задачи, вторым аргументом вы можете написать "todo", "done", "in-progress".<br>
Для отметки задачи "in-progress":<br><br>
<code>py task_cli.py mark-in-progress 1</code><br><br>
А для "done":<br><br>
<code>py task_cli.py mark_done 1</code>

