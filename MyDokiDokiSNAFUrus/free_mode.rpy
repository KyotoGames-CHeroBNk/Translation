

label free_mode:
    scene bg sat with open_eyes
    pause 1.5
    play music wefn
    scene bg kitchen with wipeleft_scene
    "Хотя многие студенты предпочитают спать в субботние утренние часы, я уже встал и принял душ к 8 утра."
    "На протяжении завтрака в моей голове крутятся мысли о том, как провести этот выходной."
    call weekend2 from _call_weekend2_7

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 1.5


    scene bg sun with open_eyes
    pause 1.5
    play music wefn
    scene bg kitchen with wipeleft_scene
    "Несмотря на то что воскресенье для многих считается \"днем отдыха\", я не собираюсь сидеть без дела следующие двенадцать часов."
    mc "Сейчас посмотрим, раз я закончил завтрак--"
    call weekend2 from _call_weekend2_8

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 1.0

    menu:
        "Перейти к финальной встрече клуба?"
        "Да.":

            scene dark with dissolve_scene_full
            pause 1.0
            jump club_final
        "Нет.":

            scene dark with dissolve_scene_full


    scene bg mon with open_eyes
    pause 1.5
    play music t2
    scene bg kitchen with wipeleft_scene
    $ midterms = "True"
    "После завтрака и сборов школьных принадлежностей, мне остается только решить--"
    call morning_standard2 from _call_morning_standard2_2

    stop music fadeout 2.0
    scene bg spring2 with dissolve_scene_full
    pause 1.5
    scene bg club_day with wipeleft_scene
    play music t3
    "Все уже занимаются своими делами, когда я вхожу в клубное помещение."
    call club_standard2 from _call_club_standard2_6

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 1.5


    scene bg tues with open_eyes
    pause 1.5
    scene bg class_day with dissolve_scene_full
    play music t8
    "Занятия проходят привычно и довольно скучно, оставляя меня в размышлениях--"
    call lunch_standard1 from _call_lunch_standard1_2

    stop music fadeout 2.0
    scene bg spring2 with wipeleft_scene
    pause 1.5
    scene bg class_day with wipeleft_scene
    play music t3
    "Звонит финальный звонок, и я остаюсь решать, куда пойти теперь."
    menu:
        "Наверное, неплохая идея--"
        "Посетить Литературный Клуб.":

            scene bg club_day with wipeleft_scene
            "Девочки заняты своими делами, когда я вхожу в комнату и кладу свои вещи."
            call club_standard2 from _call_club_standard2_7
        "Посетить Команду по Легкой Атлетике.":

            scene bg track with wipeleft_scene
            "Другие бегуны и менеджер команды уже собрались у дорожки к тому времени, как я переодеваюсь и выхожу на улицу."
            call track_menu from _call_track_menu

    stop music fadeout 2.0
    scene bg spring3 with wipeleft_scene
    pause 1.5
    scene bg kitchen with wipeleft_scene
    play music wefn
    "Не имея особых дел, у меня остается много свободного времени после приезда домой."
    call ass from _call_ass_4

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 1.0



    scene bg wed with open_eyes
    pause 1.5
    scene bg class_day with dissolve_scene_full
    play music t3
    "С очередным длинным учебным днем позади, мне остается только подумать о--"
    menu:
        "Куда мне пойти?"
        "Литературный Клуб.":

            scene bg club_day with wipeleft_scene
            "Как это стало привычным, мое появление в клубной комнате вызывает немного внимания у остальных членов."
            call club_standard2 from _call_club_standard2_8
        "Тренировка по Легкой Атлетике.":

            scene bg track with wipeleft_scene
            "Некоторые другие студенты третьего года вежливо здороваются со мной, когда я выхожу на улицу..."
            "Что ощущается неловко, так как все их имена до сих пор абсолютно незнакомы мне."
            call track_menu from _call_track_menu_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 1.0
    menu:
        "Перейти к финальной встрече клуба?"
        "Да.":

            scene dark with dissolve_scene_full
            pause 1.0
            jump club_final
        "Нет.":

            scene dark with dissolve_scene_full


    scene bg thur with open_eyes
    pause 1.5
    scene bg class_day with dissolve_scene_full
    play music t8
    "Скоро настает время обеда, и мне нужно решать--"
    call lunch_standard1 from _call_lunch_standard1_3

    stop music fadeout 2.0
    scene bg spring2 with wipeleft_scene
    pause 1.5
    scene bg class_day with wipeleft_scene
    play music t3
    "Мои одноклассники сразу же выходят из комнаты после финального звонка, оставляя меня одного размышлять о--"
    menu:
        "Куда мне пойти?"
        "Литературный Клуб.":

            scene bg club_day with wipeleft_scene
            "Все так заняты своими делами, что моё появление в клубной комнате в основном остается незамеченным."
            mc "{i}Ну что ж..."
            call club_standard2 from _call_club_standard2_9
        "Тренировка по Легкой Атлетике.":

            scene bg track with wipeleft_scene
            "Взгляд на тренера Таку, стоящего над несколькими измученными первокурсниками, быстро привлекает мое внимание."
            mc "{i}Похоже, все его \"интенсивные тренировки\" за последние два дня действительно подействовали на них."
            mc "..."
            mc "Ну что ж. Быть первокурсником - это нелегко."
            call track_menu from _call_track_menu_2

    stop music fadeout 2.0
    scene bg spring3 with wipeleft_scene
    pause 1.5
    scene bg kitchen with wipeleft_scene
    play music wefn
    "После прогулки домой меня ждет пустой и непретязательный дом."
    mc "Все дела были сделаны вчера, так что у меня есть свободное время."
    call ass from _call_ass_5

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 1.5


    scene bg fri with open_eyes
    pause 1.5
    play music t2
    scene bg kitchen with wipeleft_scene
    mc "Уже пятница, а? Интересно, не захотят ли другие поехать вместе?"
    mc "Если да..."
    call morning_standard2 from _call_morning_standard2_3

    stop music fadeout 2.0
    scene bg spring2 with dissolve_scene_full
    pause 1.5
    scene bg club_day with wipeleft_scene
    play music t3
    "Все в клубе в приподнятом настроении из-за предстоящих выходных."
    "Даже завсегдатай-книголюб и \"совершенно не безответственный\" президент клуба выглядят более радостными, чем обычно."
    call club_standard2 from _call_club_standard2_10

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 1.5

    jump free_mode
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
