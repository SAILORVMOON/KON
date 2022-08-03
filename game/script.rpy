# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define ritsu = Character('Рицу', color="#a77327")
define mio = Character('Мио', color="#343436")
define tsumugi = Character('Цумуги')
define yui = Character('Юи')
define adzusa = Character('Адзуса')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg first

    show ritsu normal

    ritsu "ММММММММИИИИИИИИИИИОООООООООООО"

    ritsu "Давай вступим в клуб!!!"

    hide ritsu

    show mio normal

    mio "Вступим в клуб?"

    hide mio

    show ritsu normal

    ritsu "В клуб лёгкой музыки...\nКЕЙ-ОН!!!"

    hide ritsu

    show mio normal

    mio "Но я хотела вступить в научный клуб..."

    mio "И заявление написала"

    hide mio

    show ritsu normal

    "*РВЁТ ЗАЯВЛЕНИЕ*"

    mio "АААААААААААААААААААААААААА!!!"

    return


label first:
    show ritsu normal

