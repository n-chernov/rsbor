# coding=utf-8

# Use colors from https://sashat.me/2017/01/11/list-of-20-simple-distinct-colors/

colors_map = {
    'ул. Марата' : '#3cb44b', # green
    'Жемчужина' : '#0082c8', # blue
    'Кронштадт' : '#3cb44b', # green
    'Московский р-н' : '#ffe119', # yellow
    'Косыгина' : '#0082c8', # blue
    'Невский р-н, у ТЦ Смайл' : '#911eb4', # purple
    'Факел' : '#46f0f0', # cyan
    'Купчино' : '#000080', # navy
    'Обводный канал' : '#ffe119', # yellow
    'Кировский завод' : '#e6194b', # red
    'Кировский' : '#e6194b', # red
    'Петроградская' : '#0082c8', # blue
    'Обводный' : '#f58231', # orange
    'Иные возможности' : '#808080', # gray
    'Спасибо' : '#46f0f0', # cyan
    'Мужества' : '#3cb44b', # green
    'Пионерская' : '#000080', # navy
    'Полюстрово' : '#ffe119', # yellow
    'ул. Гороховая' : '#aaffc3', # mint
    'Александрино' : '#f58231', # orange
    'Ледовый' : '#3cb44b', # green
    'Красное село' : '#3cb44b', # green
    'Долгоозерная' : '#e6194b', # red
    'акция' : '#808080', # gray
    'пл. Мужества' : '#3cb44b', # green
    'Калининский р-н' : '#aaffc3', # mint
    'Красносельский' : '#911eb4', # purple
    'Озерки' : '#46f0f0', # cyan
    'Марата' : '#ffd8b1', # coral
    'Петергоф' : '#0082c8', # blue
    'Невский' : '#ffd8b1', # coral
    'В.О.' : '#f58231', # orange
}

def get_colors(name):
    try:
        return colors_map[name]
    except KeyError:
        print 'KeyError -', name