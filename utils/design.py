def pretty_table(data, cell_sep=' | ', header_separator=True) -> str:
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [str(data[row][col]) for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)

    lines = []

    for i, row in enumerate(range(rows)):
        result = []
        for col in range(cols):
            item = str(data[row][col]).rjust(col_width[col])
            result.append(item)

        lines.append(cell_sep.join(result))

        if i == 0 and header_separator:
            lines.append(separator)

    return '\n'.join(lines)


def text_help():
    text = """add - Создать новую задачу. Введите описание задачи которую вы хотите создать вторым аргументом.
    list {todo, in-progress, done} - Отображение ваших задач, оставьте второй аргумент пустым если хотите отобразить все задачи
    update - Обновить описание вашей задачи, вторым аргументом введие id, а третьим новое описание
    delete - Удаляет вашу задачу, введите вторым аргументом id вашей задачи
    mark-in-progress - Отметить вашу задачу как в прогрессе, вторым аргументом передается id
    mark-done - Отметить вашу задачу как выполненную, вторым аргументом передается id"""
    return text