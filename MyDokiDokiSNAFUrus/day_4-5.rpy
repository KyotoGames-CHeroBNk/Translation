label day_four:

    scene bg sat
    with open_eyes
    pause 1.5

    "--Суббота, 9 апреля--"

    scene bg kitchen with wipeleft_scene
    play music wefn

    "Зайдя на кухню рано утром, я размышляю, чем заняться в свой выходной день."
    "За пределами домашних дел, школьных заданий и еды, по утрам и вечерам субботы и воскресенья у меня обычно бывает избыток свободного времени."
    call screen dialog("Настало время выходных!\n\nВ течение времени, проведённого в клубе, будут дни, когда вам нечем заняться, кроме как остаться дома.\nНе беспокойтесь, потому что эти моменты — отличный шанс повысить свои характеристики!\nПовышение характеристик в свободные дни происходит быстрее, чем обычно, чтобы ускорить ваш рост.\nК тому же, в зависимости от степени близости с Доки, вы можете получить специальные сцены в воскресенье!", ok_action=Return())
    mc "Сегодня может быть хорошим шансом дочитать ту книгу."
    mc "С другой стороны, погода на улице ожидается приятной и прохладной до позднего вечера. Можно выйти и размяться."
    "...{i}с тех пор, как я присоединился к клубу, я не занимался никакими формальными упражнениями."

    call weekend2 from _call_weekend2_2

    scene dark with dissolve_scene_full
    pause 1.0
    stop music fadeout 2.0

    scene bg sun with open_eyes
    pause 1.5

    "--Воскресенье, 10 апреля--"

    scene bg kitchen with wipeleft_scene
    play music wefn
    $ c_appeal = 0
    "После обычной рутины — душа и завтрак, — я снова размышляю, как провести своё свободное время."
    "В отличие от вчера, кажется, что выбор стал больше."
    "Мой телефон зазвонил в кармане, пока я сидел за кухонным столом."
    "{i}Входящий звонок от: Сайори"
    stop music fadeout 2.0
    mc "Алло."
    scene bg split2
    show sayori 2bx at t33
    with wiperight
    play music t2
    s "Привет, [player]!"
    show sayori 2ba
    mc "Привет, Сайори. Тебе что-то нужно?"
    s 2bx "Мама хочет, чтобы я сходила за продуктами, и я подумала, не хочешь ли ты пойти со мной!?"
    show sayori 2ba
    mc "Покупки продуктов, да?"
    menu:
        "Сайори хочет, чтобы я присоединился к ней. Я должен..."
        "Принять":

            $ s_appeal = s_appeal + 5
            mc "Конечно. Мне тоже нужно пару вещей."
            s 4bx "Отлично! Давай встретимся у твоего дома через минуту."
            mc "Звучит хорошо."
            scene bg kitchen
            hide sayori
            with wipeleft
            stop music fadeout 2.0
            "Я слышу, как она хихикает, прежде чем повесить трубку, и начинаю готовиться к выходу."
            call sshopping_1 from _call_sshopping_1
            jump day_six
        "Отказать":


            mc "Извини, Сайори, у меня сегодня есть другие дела. Может, в следующий раз."
            s 4bh "О-О, ладно..."
            s "Тогда в другой раз."
            show sayori 4bg
            mc "Увидимся завтра."
            s 4bk "Хорошо, увидимся."
            stop music fadeout 2.0
            scene bg kitchen
            hide sayori
            with wipeleft
            "Сайори звучит разочарованной, когда вешает трубку."
            mc "Теперь тогда..."
            play music wefn
            call weekend2 from _call_weekend2_3

    stop music fadeout 2.0
    scene dark
    with dissolve_scene_full
    pause 1.0

    jump day_six
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
