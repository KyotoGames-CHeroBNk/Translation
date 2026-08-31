
label int_level:
    if int_lvl1 == "False":
        "Уровень интеллекта повысился с 'Осведомлённого' до 'Информированного.'"
        $ i_appeal = i_appeal - 15
        $ int_lvl1 = "True"
        return
    if int_lvl1 == "True" and int_lvl2 == "False":
        "Уровень интеллекта повысился с 'Информированного' до 'Эксперта.'"
        $ i_appeal = i_appeal - 15
        $ int_lvl2 = "True"
        return
    if int_lvl2 == "True" and int_lvl3 == "False":
        "Уровень интеллекта повысился с 'Эксперта' до 'Гения.'"
        $ i_appeal = i_appeal - 15
        $ int_lvl3 = "True"
        return
    else:
        return

label soc_level:
    if soc_lvl1 == "False":
        "Общительность повысилась с 'Замкнутой' до 'Базовой.'"
        $ c_appeal = c_appeal - 15
        $ soc_lvl1 = "True"
        return
    if soc_lvl1 == "True" and soc_lvl2 == "False":
        "Общительность повысилась с 'Базовой' до 'Скорректированной.'"
        $ c_appeal = c_appeal - 15
        $ soc_lvl2 = "True"
        return
    if soc_lvl2 == "True" and soc_lvl3 == "False":
        "Общительность повысилась с 'Скорректированной' до 'Адаптированной.'"
        $ c_appeal = c_appeal - 15
        $ soc_lvl3 = "True"
        return
    else:
        return

label ath_level:
    if ath_lvl1 == "False":
        "Физическая подготовка повысилась с 'Средней' до 'Упорной.'"
        $ a_appeal = a_appeal - 15
        $ ath_lvl1 = "True"
        return
    if ath_lvl1 == "True" and ath_lvl2 == "False":
        "Физическая подготовка повысилась с 'Упорной' до 'Подтянутой.'"
        $ a_appeal = a_appeal - 15
        $ ath_lvl2 = "True"
        return
    if ath_lvl2 == "True" and ath_lvl3 == "False":
        "Физическая подготовка повысилась с 'Подтянутой' до 'Тренированной.'"
        $ a_appeal = a_appeal - 15
        $ ath_lvl3 = "True"
        return
    else:
        return


label book1:
    if ch1_book12 == "True":
        "Снова я погружаюсь в пучину отчаяния под названием «Игра в убийство»."
        "Каждый персонаж так детально проработан, что убийцей может оказаться кто угодно."
        "У всех есть свои мотивы и причины для избирательной расправы."
        "Моя первая догадка об убийце развеялась, когда этого персонажа нашли повешенным в комнате общежития."
        "Атмосфера безысходности затягивает всё сильнее, и я не могу оторваться."
        "Странно, но автор явно провёл исследование — я узнаю о психических расстройствах, вызванных стрессом."
        $ ch1_book12 = "False"
        $ ch1_book13 = "True"
        $ i_appeal = i_appeal + 2
        "--Интеллект увеличен на 2--"
        if i_appeal >= 15:
            call int_level from _call_int_level_4
        return
    if ch1_book13 == "True":
        "Сюжет накаляется, но одновременно становится мрачнее."
        "С каждой новой жертвой нарастает ужас, а круг подозреваемых сужается."
        "Мой второй кандидат в убийцы тоже оказался невиновным."
        "Обнаружив подброшенные фото её мужа с любовницей, она не выдержала."
        "В отчаянии она взяла кухонный нож, предназначенный для самообороны, и заколола себя."
        "...{i}Похоже, я плохо разбираюсь в людях."
        "Из тринадцати осталось шестеро, но личность убийцы остаётся загадкой."
        "Странным образом я изучаю уязвимые точки человеческого тела."
        $ ch1_book13 = "False"
        $ ch1_book14 = "True"
        $ i_appeal = i_appeal + 2
        "--Интеллект увеличен на 2--"
        if i_appeal >= 15:
            call int_level from _call_int_level_5
        return
    if ch1_book14 == "True":
        "Приближаясь к финалу, я ловлю себя на том, что читаю всё быстрее и быстрее по мере приближения конца."
        "Мой любимый персонаж, саркастичный, но в то же время надежный, оказывается одним из четырех последних выживших."
        "Учитывая, что их осталось так мало, очевидно, что всё относятся друг к другу с большим подозрением."
        "Тем не менее, даже при таком недоверии все они сходятся во мнении, что происходит что-то странное. Что-то, отличное от случайных убийств."
        "А именно, это беспокойство возникает после того, как обнаруживается ещё один труп, обугленный до хрустящей корочки и не поддающийся идентификации."
        "Сбитые с толку тем, что теперь, по-видимому, насчитывается в общей сложности четырнадцать тел, считая живых и мертвых, выжившие заключают временное перемирие."
        "Объединившись и пройдя по своим следам, они обнаруживают, что труп, относящийся ко второй причинно-следственной связи, исчез."
        "Благодаря их совместным навыкам расследования они обнаруживают, что личность убийцы на самом деле совпадает с личностью пропавшего трупа."
        "Как только грандиозный план раскрыт, появляется убийца. Как и ожидалось, это тот же человек, который был 'убит' в начале истории."
        "Признавшись, что она использовала двойника, чтобы инсценировать свою смерть, и сожгла труп, чтобы посеять недоверие среди выживших..."
        "Убийца продолжает маниакально разглагольствовать об экстазе, который является \"полным отчаянием\"."
        "Устав от её безумных игр, четверо выживших восстают и побеждают её."
        "Дочитывая последнюю страницу, я испытываю невероятное удовлетворение."
        $ y_diss = "False"
        $ ch1_book14 = "False"
        $ ch1_book15 = "True"
        $ i_appeal = i_appeal + 2
        "--Интеллект увеличен на 2--"
        if i_appeal >= 15:
            call int_level from _call_int_level
        return


label morning_standard1:
    menu:
        "С кем пойти?"
        "Сайори":

            scene bg resday with wipeleft_scene
            call s_morning_random from _call_s_morning_random
            $ s_appeal = s_appeal + 3
            if s_appeal >= 10:
                "Кажется, скоро у нас будет шанс сблизиться."
                if s_out == "True":
                    "Может, поговорим после школы?"
                if s_weekend == "True":
                    "Встретимся на выходных?"
        "Киба":

            scene bg resday with wipeleft_scene
            call k_morning_random from _call_k_morning_random
            $ k_appeal = k_appeal + 3
            if k_appeal >= 10:
                "Чувствую, Киба скоро захочет проводить со мной время."
    return

label morning_standard2:
    menu:
        "С кем идти в школу?"

        "Сайори" if s_mad == "False":
            scene bg resday with wipeleft_scene
            call s_morning_random from _call_s_morning_random_1
            $ s_appeal = s_appeal + 3
            if soc_lvl1 == "True":
                $ s_appeal = s_appeal + 1
            if soc_lvl2 == "True":
                $ s_appeal = s_appeal + 1
            if soc_lvl3 == "True":
                $ s_appeal = s_appeal + 1
            if s_appeal >= 10:
                "Чувствую, скоро мы сможем стать ближе."
                if s_out == "True":
                    "Может, поговорим после уроков?"
                if s_weekend == "True":
                    "Встретимся на выходных?"
        "Киба":

            scene bg resday with wipeleft_scene
            call k_morning_random from _call_k_morning_random_1
            $ k_appeal = k_appeal + 3
            if soc_lvl1 == "True":
                $ k_appeal = k_appeal + 1
            if soc_lvl2 == "True":
                $ k_appeal = k_appeal + 1
            if soc_lvl3 == "True":
                $ k_appeal = k_appeal + 1
            if k_appeal >= 10:
                "Кажется, Киба захочет встретиться."
                if k_out == "True":
                    "Наверное, зайдёт после школы."
                if k_weekend == "True":
                    "Может, напишет на выходных."

        "Нацуки" if n_scene1 == "True":
            if n_scene5 == "True" and n_appeal >=10 and n_scene6 == "False":
                scene bg resday with wipeleft_scene
                call n_scene6 from _call_n_scene6_1
            else:
                scene bg resday with wipeleft_scene
                call n_morning_random from _call_n_morning_random
                $ n_appeal = n_appeal + 3
                if soc_lvl1 == "True":
                    $ n_appeal = n_appeal + 1
                if soc_lvl2 == "True":
                    $ n_appeal = n_appeal + 1
                if soc_lvl3 == "True":
                    $ n_appeal = n_appeal + 1
                if n_appeal >=10:
                    "Возможно, наши отношения улучшатся."
                    if n_out == "True":
                        "Может, встретимся после школы?"
                    if n_weekend:
                        "Интересно, захочет ли она общаться на выходных?"
    return


label lunch_standard1:
    menu:
        "С кем пообедать?"
        "Киба":

            play music t8
            if k_appeal >= 10 and k_day == "False" and k_out == "False" and k_weekend == "False":
                scene bg courtyard with wipeleft_scene
                call k_code_in from _call_k_code_in
            elif k_day == "False":
                call k_lunch_random from _call_k_lunch_random
                $ k_appeal = k_appeal + 3
                if soc_lvl1 == "True":
                    $ k_appeal = k_appeal + 1
                if soc_lvl2 == "True":
                    $ k_appeal = k_appeal + 1
                if soc_lvl3 == "True":
                    $ k_appeal = k_appeal + 1
                if k_appeal >= 10:
                    "Киба, кажется, хочет чаще видеться."
                    if k_out == "True":
                        "Вероятно, зайдёт после занятий."
                    if k_weekend == "True":
                        "Может, предложит встретиться на выходных."
        "Юри" if y_scene1 == "True":
            scene bg class_day with wipeleft_scene
            play music t8
            pause 0.5
            call y_lunch_random from _call_y_lunch_random
            $ y_appeal = y_appeal + 3
            if int_lvl1 == "True":
                $ y_appeal = y_appeal + 1
            if int_lvl2 == "True":
                $ y_appeal = y_appeal + 1
            if int_lvl3 == "True":
                $ y_appeal = y_appeal + 1
            if y_scene2 == "False":
                "Мы общаемся, но прогресс будет только после школьного разговора."
                "Всё же чувствую, что мы стали ближе."
            if y_appeal >=10 and y_scene2 == "True":
                "Скоро Юри станет немного открытее."
                if y_out == "True":
                    "Может, поговорим после школы?"
                if y_weekend == "True":
                    "Интересно, согласится ли она на встречу в выходные?"
        "Рикка" if r_lunch1 == "True":
            if r_lunch2 == "False":
                play music t8
                scene bg class_day with wipeleft_scene
                call r_lunch2 from _call_r_lunch2
            if r_lunch2 == "True":
                play music t8
                scene bg stairs with wipeleft_scene
                call r_lunch_random from _call_r_lunch_random
                if r_appeal >= 10:
                    "Кажется, Рикка скоро начнёт \"баловать\" сэмпая."
                    if r_out == "True":
                        "Интересно, позовёт ли после школы?"
                    if r_weekend == "True":
                        "Надеюсь, хотя бы дождётся выходных."
    $ k_day = "False"
    return


label club_standard1:
    menu:
        "Поговорить с Сайори"
        "Сайори":

            scene bg club_day with wipeleft_scene
            if s_appeal >= 10 and s_day == "False" and s_out == "False" and s_weekend == "False":
                call s_code_in from _call_s_code_in
            elif s_day == "False":
                call s_club_random from _call_s_club_random
                $ s_appeal = s_appeal + 3
                if soc_lvl1 == "True":
                    $ s_appeal = s_appeal + 1
                if soc_lvl2 == "True":
                    $ s_appeal = s_appeal + 1
                if soc_lvl3 == "True":
                    $ s_appeal = s_appeal + 1
                if s_appeal >= 10:
                    "Скоро будет шанс укрепить наши отношения."
                    if s_out == "True":
                        "Может, поговорим после уроков?"
                    if s_weekend == "True":
                        "Встретимся на выходных?"
        "Вернуть книгу Юри" if ch1_book15 == "True" and y_scene1 == "False":
            scene bg club_day with wipeleft_scene
            call y_scene1 from _call_y_scene1
        "Поговорить с Юри" if y_scene1 == "True":
            scene bg club_day with wipeleft_scene
            if y_appeal >= 10 and y_scene2 == "True" and y_day == "False" and y_out == "False" and y_weekend == "False":
                call y_code_in from _call_y_code_in_2
            elif y_day == "False":
                call y_club_random from _call_y_club_random_4
                $ y_appeal = y_appeal + 3
                if int_lvl1 == "True":
                    $ y_appeal = y_appeal + 1
                if int_lvl2 == "True":
                    $ y_appeal = y_appeal + 1
                if int_lvl3 == "True":
                    $ y_appeal = y_appeal + 1
                if y_scene2 == "False":
                    "Мы общаемся, но прогресс будет только после разговора."
                    "Всё же мы стали немного ближе."
                if y_appeal >=10 and y_scene2 == "True":
                    "Скоро Юри станет открытее."
                    if y_out == "True":
                        "Может, поговорим после школы?"
                    if y_weekend == "True":
                        "Интересно, согласится ли на встречу в выходные?"
        "Поговорить с Нацуки":
            scene bg club_day with wipeleft_scene
            if n_appeal >= 10 and n_day == "False" and n_out == "False" and n_weekend == "False":
                call n_code_in from _call_n_code_in
            elif n_day == "False":
                call n_club_random from _call_n_club_random_1
                $ n_appeal = n_appeal + 3
                if soc_lvl1 == "True":
                    $ n_appeal = n_appeal + 1
                if soc_lvl2 == "True":
                    $ n_appeal = n_appeal + 1
                if soc_lvl3 == "True":
                    $ n_appeal = n_appeal + 1
                if n_appeal >= 10:
                    "Возможно, улучшим отношения."
                    if n_out == "True":
                        "Может, встретимся после школы?"
                    if n_weekend:
                        "Интересно, захочет ли общаться на выходных?"
        "Читать" if ch1_book15 == "False":
            mc "Самое время прочесть ещё пару глав книги от Юри."
            scene bg club_day with wipeleft_scene
            call book1 from _call_book1_2
        "Учиться":
            scene bg club_day with wipeleft_scene
            call study1 from _call_study1
    $ n_day = "False"
    $ m_day = "False"
    $ s_day = "False"
    $ y_day = "False"
    return

label club_standard2:
    menu:
        "Предположу, что могу использовать встречу для..."
        "Поговорить с Сайори":

            scene bg club_day with wipeleft_scene
            if s_appeal >= 10 and s_day == "False" and s_out == "False" and s_weekend == "False":
                call s_code_in from _call_s_code_in_1
            elif s_day == "False":
                call s_club_random from _call_s_club_random_1
                $ s_appeal = s_appeal + 3
                if soc_lvl1 == "True":
                    $ s_appeal = s_appeal + 1
                if soc_lvl2 == "True":
                    $ s_appeal = s_appeal + 1
                if soc_lvl3 == "True":
                    $ s_appeal = s_appeal + 1
                if s_appeal >= 10:
                    "Чувствую, скоро будет шанс сблизиться."
                    if s_out == "True":
                        "Может, поговорим после уроков?"
                    if s_weekend == "True":
                        "Встретимся на выходных?"
        "Вернуть книгу Юри" if ch1_book15 == "True" and y_scene1 == "False":
            scene bg club_day with wipeleft_scene
            call y_scene1 from _call_y_scene1_1
        "Поговорить с Юри" if y_scene1 == "True":
            scene bg club_day with wipeleft_scene
            if y_appeal >= 10 and y_scene2 == "True" and y_day == "False" and y_out == "False" and y_weekend == "False":
                call y_code_in from _call_y_code_in_2
            elif y_day == "False":
                call y_club_random from _call_y_club_random_4
                $ y_appeal = y_appeal + 3
                if int_lvl1 == "True":
                    $ y_appeal = y_appeal + 1
                if int_lvl2 == "True":
                    $ y_appeal = y_appeal + 1
                if int_lvl3 == "True":
                    $ y_appeal = y_appeal + 1
                if y_scene2 == "False":
                    "Общаемся нормально, но прогресс будет после разговора."
                    "Всё же стали немного ближе."
                if y_appeal >=10 and y_scene2 == "True":
                    "Скоро Юри станет открытее."
                    if y_out == "True":
                        "Может, поговорим после школы?"
                    if y_weekend == "True":
                        "Согласится ли на встречу в выходные?"
        "Поговорить с Нацуки":
            scene bg club_day with wipeleft_scene
            if n_appeal >= 10 and n_day == "False" and n_out == "False" and n_weekend == "False":
                call n_code_in from _call_n_code_in_1
            elif n_day == "False":
                call n_club_random from _call_n_club_random_2
                $ n_appeal = n_appeal + 3
                if soc_lvl1 == "True":
                    $ n_appeal = n_appeal + 1
                if soc_lvl2 == "True":
                    $ n_appeal = n_appeal + 1
                if soc_lvl3 == "True":
                    $ n_appeal = n_appeal + 1
                if n_appeal >= 10:
                    "Возможно, улучшим отношения."
                    if n_out == "True":
                        "Может, встретимся после школы?"
                    if n_weekend == "True":
                        "Захочет ли общаться на выходных?"
        "Поговорить с Моникой ({i}Инт. Ур. 2, Общ. Ур. 1{/i})" if m_scene1 == "False":
            if int_lvl2 == "True" and soc_lvl1 == "True":
                scene bg club_day with wipeleft_scene
                call m_scene1 from _call_m_scene1_1
            else:
                "Ещё не готов к такому уровню сложности."
                call club_standard2 from _call_club_standard2
        "Поговорить с Моникой" if m_scene1 == "True" and m_end == "False":
            scene bg club_day with wipeleft_scene
            call m_club_random from _call_m_club_random
            $ m_appeal = m_appeal + 3
            if soc_lvl1 == "True" and ath_lvl1 == "True" and int_lvl1 == "True":
                $ m_appeal = m_appeal + 1
            if soc_lvl2 == "True" and ath_lvl2 == "True" and int_lvl2 == "True":
                $ m_appeal = m_appeal + 1
            if soc_lvl3 == "True" and ath_lvl3 == "True" and int_lvl3 == "True":
                $ m_appeal = m_appeal + 1
            if m_appeal >= 10:
                "Моника, кажется, хочет копнуть глубже."
                if m_out == "True" and m_scene2 == "True":
                    "Придёт ли после школы снова?"
                if m_weekend == "True":
                    "Может предложить встречу на выходных."
        "Читать" if ch1_book15 == "False":
            mc "Самое время дочитать пару глав книги от Юри."
            scene bg club_day with wipeleft_scene
            call book1 from _call_book1_3
        "Учиться":
            scene bg club_day with wipeleft_scene
            call study1 from _call_study1_1

    $ n_day = "False"
    $ s_day = "False"
    $ y_day = "False"
    return


label track_standard:
    scene bg track with wipeleft_scene
    "Все уже начали разминку, когда я прибываю."
    menu track_menu:
        mc "Что ж, приступим—"
        "Поговорить с Риккой":

            if r_appeal >= 10 and r_day == "False" and r_out == "False" and r_weekend == "False":
                call r_code_in from _call_r_code_in
            elif r_day == "False":
                call r_club_random from _call_r_club_random
                $ r_appeal = r_appeal + 3
                if ath_lvl1 == "True":
                    $ r_appeal = r_appeal + 1
                if ath_lvl2 == "True":
                    $ r_appeal = r_appeal + 1
                if ath_lvl3 == "True":
                    $ r_appeal = r_appeal + 1
                if r_appeal >= 10:
                    "Рикка, кажется, скоро начнёт \"баловать\" сэмпая."
                    if r_out == "True":
                        "Позовёт ли после тренировки?"
                    if r_weekend == "True":
                        "Хоть бы до выходных подождала."
        "Сосредоточиться на тренировке":

            "Встаю на дорожку рядом с другими бегунами и начинаю подготовку."
            scene dark with close_eyes
            "Час интенсивных упражнений пролетает незаметно до объявления окончания тренировки."
            "Ноги ноют, но чувствуется прогресс."
            $ a_appeal = a_appeal + 3
            "--Атлетика увеличен на 3--"
            if a_appeal >= 15:
                call ath_level from _call_ath_level_10
    $ r_day = "False"
    return


label ass:
    menu:
        "Как провести день?"

        "Читать" if ch1_book15 == "False":
            mc "Дочитаю пару глав книги от Юри."
            scene bg living_day with wipeleft_scene
            call book1 from _call_book1_4
        "Учиться":
            scene bg kitchen with wipeleft_scene
            call study2 from _call_study2
        "Пробежка":
            scene bg resn with dissolve_scene_full
            call running2 from _call_running2
        "Встретиться с Юри" if y_scene1 == "True" and y_scene2 == "False":
            scene bg kitchen with wipeleft_scene
            call y_scene2 from _call_y_scene2
        "Связаться с Юри" if y_appeal >= 10 and y_out == "True" and midterms == "True":
            scene bg kitchen with wipeleft_scene
            call y_code_out from _call_y_code_out
        "Связаться с Нацуки" if n_appeal >= 10 and n_out == "True" and midterms == "True":
            scene bg kitchen with wipeleft_scene
            call n_code_out from _call_n_code_out
        "Связаться с Моникой" if m_appeal >= 10 and m_out == "True" and m_end == "False":
            scene bg kitchen with wipeleft_scene
            call m_code_out from _call_m_code_out
        "Связаться с Сайори" if s_appeal >= 10 and s_out == "True" and midterms == "True":
            scene bg kitchen with wipeleft_scene
            call s_code_out from _call_s_code_out
        "Связаться с Риккой" if r_appeal >= 10 and r_out == "True":
            scene bg kitchen with wipeleft_scene
            call r_code_out from _call_r_code_out
        "Связаться с Кибой" if k_appeal >= 10 and k_out == "True":
            scene bg kitchen with wipeleft_scene
            call k_code_out from _call_k_code_out
    return


label weekend1:
    menu:
        "Как провести свободное время?"

        "Чтение" if ch1_book15 == "False":
            mc "Дочитаю книгу от Юри."
            call book1 from _call_book1_7
            if ch1_book15 == "False":
                call book1 from _call_book1_8
        "Учёба":

            call study3 from _call_study3
    return

label weekend2:
    menu:
        "Чем заняться?"

        "Чтение" if ch1_book15 == "False":
            mc "Возьмусь за книгу от Юри."
            scene bg living_day with wipeleft
            call book1 from _call_book1_9
            if ch1_book15 == "False":
                scene bg living_dark with dissolve_scene_full
                "Закончив все дела, я снова берусь за чтение."
                call book1 from _call_book1_10
            else:
                scene bg living_dark with dissolve_scene_full
                "Закончив книгу, повторяю учебные материалы."
                $ i_appeal = i_appeal + 3
                "--Интеллект увеличен на 3--"
                if i_appeal >= 15:
                    call int_level from _call_int_level_6
        "Учёба":

            call study3 from _call_study_1
        "Пробежка":
            scene bg door_m with wipeleft
            call running3 from _call_running3
        "Связаться с Юри" if y_appeal >= 10 and y_weekend == "True":
            scene bg kitchen with wipeleft_scene
            call y_code_weekend from _call_y_code_weekend
        "Связаться с Нацуки" if n_appeal >= 10 and n_weekend == "True":
            scene bg kitchen with wipeleft_scene
            call n_code_weekend from _call_n_code_weekend
        "Связаться с Моникой" if m_appeal >= 10 and m_weekend == "True":
            scene bg kitchen with wipeleft_scene
            call m_code_weekend from _call_m_code_weekend
        "Связаться с Сайори" if s_appeal >= 10 and s_weekend == "True":
            scene bg kitchen with wipeleft_scene
            call s_code_weekend from _call_s_code_weekend
        "Связаться с Риккой" if r_appeal >= 10 and r_weekend == "True":
            scene bg kitchen with wipeleft_scene
            call r_code_weekend from _call_r_code_weekend
        "Связаться с Кибой" if k_appeal >= 10 and k_weekend == "True":
            call k_code_weekend from _call_k_code_weekend
    return


label study1:
    "Тишина в клубе способствует учёбе."
    "Достаю конспекты и начинаю повторение."
    $ i_appeal = i_appeal + 3
    "--Интеллект увеличен на 3--"
    if i_appeal >= 15:
        call int_level from _call_int_level_7
    return

label study2:
    "...{i}вряд ли кто-то помешает."
    mc "Займусь учебой."
    "Раскладываю материалы на кухонном столе."
    $ i_appeal = i_appeal + 3
    "--Интеллект учеличен на 3--"
    if i_appeal >= 15:
        call int_level from _call_int_level_8
    return

label study3:
    mc "Потрачу выходной на учёбу."
    scene bg bedroom с wipeleft
    "После завтрака раскладываю учебники на столе."
    "Материал несложный, легко усваивается."
    $ i_appeal = i_appeal + 4
    "--Интеллект учеличен 4--"
    if i_appeal >= 15:
        call int_level from _call_int_level_9
    return

label running2:
    "Вечерний воздух идеален для пробежки."
    "Привычная боль в ногах после второго круга."
    $ a_appeal = a_appeal + 3
    "--Атлетика увеличен на 3--"
    if a_appeal >= 15:
        call ath_level from _call_ath_level_2
    mc "Пора возвращаться."
    mc "Не стоит задерживаться допоздна."
    return

label running3:
    mc "Утренняя и вечерняя пробежка — оптимальный график."
    $ renpy.call('run_weekend'+str(renpy.random.randint(1,2)))
    scene bg door_n with wipeleft_scene
    "Кровь пульсирует в натруженных ногах."
    $ a_appeal = a_appeal + 5
    "--Атлетика увеличен на 5--"
    if a_appeal >= 15:
        call ath_level from _call_ath_level_3
    "Принимаю душ и готовлюсь ко сну."
    return

label run_weekend1:
    scene bg resday с wipeleft_scene
    "Утреннее солнце греет, влажный воздух освежает."
    mc "Успею сделать круг до восьми."
    mc "Вечером сделаю ещё два."
    "Начинаю пробежку."
    scene dark with close_eyes
    "День проходит в рутинных делах."

label run_weekend2:
    scene bg resn with dissolve_scene_full
    "Ночная прохлада бодрит лучше утренней жары."
    return







    scene bg tues with open_eyes
    pause 1.5

    "--Вторник, 12 апреля--"


    scene bg spring with wipeleft_scene
    pause 1.5


    scene bg spring2 with wipeleft_scene
    pause 1.5


    scene bg spring3 with wipeleft_scene
    pause 1.5


    scene dark with dissolve_scene_full
    pause 1.0

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
