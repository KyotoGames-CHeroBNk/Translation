


label s_route:
    $ route_start = "True"
    $ s_route_begin = "True"
    $ renpy.jump_out_of_context(s_scene0)
label s_scene0:
    stop music fadeout 2.0
    scene bg spring2 with dissolve_scene_full
    pause 1.0
    play music t3
    scene bg club_day with wipeleft_scene
    call s_scene1 from _call_s_scene1_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    scene bg club_day with wipeleft_scene
    call s_scene2 from _call_s_scene2

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    scene bg club_day with wipeleft_scene
    call s_scene3 from _call_s_scene3_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    scene bg club_day with wipeleft_scene
    call s_scene4 from _call_s_scene4_1

    if s_love == "True":
        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call s_love1 from _call_s_love1_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call s_love2 from _call_s_love2_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call s_love3 from _call_s_love3_1
    else:
        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music t3
        scene bg club_day with wipeleft_scene
        call s_scene5 from _call_s_scene5_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music t3
        scene bg club_day with wipeleft_scene
        call s_scene6 from _call_s_scene6_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call s_scene7 from _call_s_scene7

    return


label m_route:
    $ route_start = "True"
    $ m_route_begin = "True"
    $ renpy.jump_out_of_context(m_scene0)
label m_scene0:
    stop music fadeout 2.0
    scene bg spring2 with dissolve_scene_full
    pause 1.0
    play music t3
    scene bg club_day with wipeleft_scene
    call m_scene1 from _call_m_scene1_2
    if m_end == "True":
        scene dark with dissolve_scene_full
        return

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music wefn
    scene bg kitchen with wipeleft_scene
    call m_scene2 from _call_m_scene2_1
    if m_end == "True":
        scene dark with dissolve_scene_full
        return

    stop music fadeout 2.0
    $ ath_lvl2 = "True"
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music wefn
    scene bg kitchen with wipeleft_scene
    call m_scene3 from _call_m_scene3_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg sat with open_eyes
    "Несколько дней спустя."
    play music wefn
    scene bg kitchen with wipeleft_scene
    call m_scene4 from _call_m_scene4_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music wefn
    call m_scene5 from _call_m_scene5_1

    if m_love == "True":
        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call m_love1 from _call_m_love1_1
    else:

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call m_scene6 from _call_m_scene6_1
    scene dark with dissolve_scene_full
    return


label n_route:
    $ route_start = "True"
    $ n_route_begin = "True"
    $ renpy.jump_out_of_context(n_scene0)
label n_scene0:
    stop music fadeout 2.0
    scene bg spring2 with dissolve_scene_full
    pause 1.0
    play music t3
    scene bg club_day with wipeleft_scene
    call n_scene1 from _call_n_scene1_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    scene bg club_day with wipeleft_scene
    call n_scene2 from _call_n_scene2_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    scene bg club_day with wipeleft_scene
    call n_scene3 from _call_n_scene3_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    scene bg club_day with wipeleft_scene
    call n_scene4 from _call_n_scene4_1

    if n_love == "True":
        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music wefn
        call n_love1 from _call_n_love1_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call n_love2 from _call_n_love2_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call n_love3 from _call_n_love3_1
    else:
        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music t3
        scene bg club_day with wipeleft_scene
        call n_scene5 from _call_n_scene5_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg mon with open_eyes
        "Несколько дней спустя."
        play music t2
        scene bg resday with wipeleft_scene
        call n_scene6 from _call_n_scene6_2
    scene dark with dissolve_scene_full
    return



label y_route:
    $ route_start = "True"
    $ y_route_begin = "True"
    $ renpy.jump_out_of_context(y_scene0)
label y_scene0:
    stop music fadeout 2.0
    scene bg spring2 with dissolve_scene_full
    pause 1.0
    play music t3
    scene bg club_day with wipeleft_scene
    call y_scene1 from _call_y_scene1_2

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music wefn
    scene bg kitchen with wipeleft_scene
    call y_scene2 from _call_y_scene2_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    scene bg club_day with wipeleft_scene
    call y_scene3 from _call_y_scene3

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    scene bg club_day with wipeleft_scene
    call y_scene4 from _call_y_scene4_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    scene bg club_day with wipeleft_scene
    call y_scene5 from _call_y_scene5_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music wefn
    scene bg kitchen with wipeleft_scene
    call y_scene6 from _call_y_scene6

    if y_love == "False":
        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music t3
        scene bg club_day with wipeleft_scene
        call y_scene7 from _call_y_scene7_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music wefn
        call y_scene8 from _call_y_scene8
    else:
        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        call y_love1 from _call_y_love1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call y_love2 from _call_y_love2
    scene dark with dissolve_scene_full
    return


label r_route:
    $ route_start = "True"
    $ r_route_begin = "True"
    $ renpy.jump_out_of_context(r_scene0)
label r_scene0:
    stop music fadeout 2.0
    scene bg spring2 with dissolve_scene_full
    pause 1.0
    call r_scene1 from _call_r_scene1_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    call r_scene2 from _call_r_scene2_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    call r_scene3 from _call_r_scene3_1

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg sat with open_eyes
    "Несколько дней спустя."
    play music wefn
    scene bg kitchen with wipeleft_scene
    call r_scene4 from _call_r_scene4

    stop music fadeout 2.0
    scene dark with dissolve_scene_full
    pause 0.5
    scene bg spring2 with open_eyes
    "Несколько дней спустя."
    play music t3
    call r_scene5 from _call_r_scene5_1

    if r_love == "False":
        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music t3
        scene bg track with wipeleft_scene
        call r_scene6 from _call_r_scene6_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call r_scene7 from _call_r_scene7
    else:
        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music t3
        scene bg track with wipeleft_scene
        call r_love1 from _call_r_love1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call r_love2 from _call_r_love2_1

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg sat with open_eyes
        "Несколько дней спустя."
        play music wefn
        scene bg kitchen with wipeleft_scene
        call r_love3 from _call_r_love3

        stop music fadeout 2.0
        scene dark with dissolve_scene_full
        pause 0.5
        scene bg spring2 with open_eyes
        "Несколько дней спустя."
        play music t8
        scene bg track with wipeleft_scene
        call r_love4 from _call_r_love4
    scene dark with dissolve_scene_full
    return


label k_app:
    "Киба: Установить Ноль"
    scene bg resday with open_eyes
    play music t2
    call km1 from _call_km1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km2 from _call_km2
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km3 from _call_km3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    play music t8
    call kl1 from _call_kl1
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    call kl2 from _call_kl2
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    call kl3 from _call_kl3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Киба: Установить Один"
    scene bg resday with open_eyes
    play music t2
    call km4 from _call_km4
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km5 from _call_km5
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km6 from _call_km6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    play music t8
    call kl4 from _call_kl4
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    call kl5 from _call_kl5
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    call kl6 from _call_kl6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Киба: Установить Два"
    scene bg resday with open_eyes
    play music t2
    call km7 from _call_km7
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km8 from _call_km8_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km9 from _call_km9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    play music t8
    call kl7 from _call_kl7
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    call kl9 from _call_kl9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Киба: Установить Три"
    scene bg resday with open_eyes
    play music t2
    call km10 from _call_km10
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km11 from _call_km11_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km12 from _call_km12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    play music t8
    call kl10 from _call_kl10
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    call kl12 from _call_kl12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Киба: Установить Четыре"
    scene bg resday with open_eyes
    play music t2
    call km13 from _call_km13
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km14 from _call_km14
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call km15 from _call_km15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    play music t8
    call kl13 from _call_kl13
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    call kl14 from _call_kl14
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    call kl15 from _call_kl15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Киба: После Очистки Дружбы"
    scene bg resday with open_eyes
    play music t2
    call km16 from _call_km16
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg courtyard with open_eyes
    play music t8
    call kl16 from _call_kl16
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    return

label m_app:
    "Моника: Установить Один"
    scene bg club_day with open_eyes
    play music t3
    call mc1 from _call_mc1
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc2 from _call_mc2
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc3 from _call_mc3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Моника: Установить Два"
    scene bg club_day with open_eyes
    play music t3
    call mc4 from _call_mc4
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc5 from _call_mc5
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc6 from _call_mc6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Моника: Установить Три"
    scene bg club_day with open_eyes
    play music t3
    call mc7 from _call_mc7
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc8 from _call_mc8
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc9 from _call_mc9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Моника: Установить Четыре"
    scene bg club_day with open_eyes
    play music t3
    call mc10 from _call_mc10
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc11 from _call_mc11
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc12 from _call_mc12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Моника: Установить Пять"
    scene bg club_day with open_eyes
    play music t3
    call mc13 from _call_mc13
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc14 from _call_mc14_1
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc15 from _call_mc15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Моника: После Очистки Дружбы"
    scene bg club_day with open_eyes
    play music t3
    call mc16 from _call_mc16
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Моника: Установить Дату Один"
    scene bg club_day with open_eyes
    play music t3
    call mc17 from _call_mc17
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc18 from _call_mc18
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call mc19 from _call_mc19
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Моника: После Очистки Даты"
    scene bg club_day with open_eyes
    play music t3
    call mc20 from _call_mc20
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    return

label n_app:
    "Нацуки: Установить Ноль"
    scene bg club_day with open_eyes
    play music t3
    call nc1 from _call_nc1
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc2 from _call_nc2
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc3 from _call_nc3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: Установить Один"
    scene bg resday with open_eyes
    play music t2
    call nm1 from _call_nm1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm2 from _call_nm2
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm3 from _call_nm3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call nc4 from _call_nc4
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc5 from _call_nc5
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc6 from _call_nc6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: Установить Два"
    scene bg resday with open_eyes
    play music t2
    call nm4 from _call_nm4
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm5 from _call_nm5_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm6 from _call_nm6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call nc7 from _call_nc7
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc9 from _call_nc9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: Установить Три"
    scene bg resday with open_eyes
    play music t2
    call nm7 from _call_nm7
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm8 from _call_nm8_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm9 from _call_nm9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call nc10 from _call_nc10
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc12 from _call_nc12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: Установить Четыре"
    scene bg resday with open_eyes
    play music t2
    call nm10 from _call_nm10
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm11 from _call_nm11_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm12 from _call_nm12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call nc13 from _call_nc13
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc15 from _call_nc15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: Установить Пять"
    scene bg resday with open_eyes
    play music t2
    call nm13 from _call_nm13
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm14 from _call_nm14_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm15 from _call_nm15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call nc16 from _call_nc16
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc18 from _call_nc18
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: После Очистки Дружбы"
    scene bg resday with open_eyes
    play music t2
    call nm16 from _call_nm16
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc19 from _call_nc19
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: Установить Дату Один"
    scene bg resday with open_eyes
    play music t2
    call nm17 from _call_nm17
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm18 from _call_nm18_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm19 from _call_nm19
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call nc20 from _call_nc20
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc22 from _call_nc22
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: Установить Дату Два"
    scene bg resday with open_eyes
    play music t2
    call nm20 from _call_nm20
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm21 from _call_nm21_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm22 from _call_nm22
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call nc23 from _call_nc23
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc25 from _call_nc25
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: Установить Дату Три"
    scene bg resday with open_eyes
    play music t2
    call nm23 from _call_nm23
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm24 from _call_nm24_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call nm25 from _call_nm25
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call nc26 from _call_nc26
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call nc28 from _call_nc28
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Нацуки: После Очистки Даты"
    scene bg resday with open_eyes
    play music t2
    call nm26 from _call_nm26
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call nc29 from _call_nc29
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    return

label r_app:
    "Рикка: Установить Ноль"
    scene bg track with open_eyes
    play music t8
    call rc1 from _call_rc1
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc2 from _call_rc2
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc3 from _call_rc3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: Установить Один"
    scene bg track with open_eyes
    play music t8
    call rc4 from _call_rc4
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc5 from _call_rc5
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc6 from _call_rc6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: Установить Два"
    scene bg track with open_eyes
    play music t8
    call rc7 from _call_rc7
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc8 from _call_rc8
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc9 from _call_rc9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    play music wefn
    call r_lunch2 from _call_r_lunch2_1
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5


    "Рикка: Установить Три"
    scene bg track with open_eyes
    play music t8
    call rc10 from _call_rc10
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc11 from _call_rc11
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc12 from _call_rc12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: Установить Четыре"
    scene bg track with open_eyes
    play music t8
    call rc13 from _call_rc13
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc14 from _call_rc14
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc15 from _call_rc15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: Установить Пять"
    scene bg track with open_eyes
    play music t8
    call rc16 from _call_rc16
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc17 from _call_rc17
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc18 from _call_rc18
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: Установить Шесть"
    scene bg track with open_eyes
    play music t8
    call rc19 from _call_rc19
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc20 from _call_rc20
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc21 from _call_rc21
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: После Очистки Дружбы"
    scene bg track with open_eyes
    play music t8
    call rc22 from _call_rc22
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: Установить Дату Один"
    scene bg track with open_eyes
    play music t8
    call rc23 from _call_rc23
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc24 from _call_rc24
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc25 from _call_rc25
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg stairs with open_eyes
    play music wefn
    call rl24 from _call_rl24
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: Установить Дату Два"
    scene bg track with open_eyes
    play music t8
    call rc26 from _call_rc26
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc27 from _call_rc27
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc28 from _call_rc28
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: Установить Дату Три"
    scene bg track with open_eyes
    play music t8
    call rc29 from _call_rc29
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc30 from _call_rc30
    scene dark with close_eyes
    pause 0.5
    scene bg track with open_eyes
    call rc31 from _call_rc31
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Рикка: После Очистки Даты"
    scene bg track with open_eyes
    play music t8
    call rc32 from _call_rc32
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg stairs with open_eyes
    play music wefn
    call rl32 from _call_rl32
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    return

label s_app:
    "Сайори: Установить Ноль"
    scene bg resday with open_eyes
    play music t2
    call sm1 from _call_sm1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm2 from _call_sm2
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm3 from _call_sm3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc1 from _call_sc1
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc2 from _call_sc2
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc3 from _call_sc3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: Установить Один"
    scene bg resday with open_eyes
    play music t2
    call sm4 from _call_sm4
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm5 from _call_sm5
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm6 from _call_sm6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc4 from _call_sc4
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc5 from _call_sc5
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc6 from _call_sc6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: Установить Два"
    scene bg resday with open_eyes
    play music t2
    call sm7 from _call_sm7
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm8 from _call_sm8_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm9 from _call_sm9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc7 from _call_sc7
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc9 from _call_sc9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: Установить Три"
    scene bg resday with open_eyes
    play music t2
    call sm10 from _call_sm10
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm11 from _call_sm11_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm12 from _call_sm12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc10 from _call_sc10
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc12 from _call_sc12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: Установить Четыре"
    scene bg resday with open_eyes
    play music t2
    call sm13 from _call_sm13
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm14 from _call_sm14_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm15 from _call_sm15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc13 from _call_sc13
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc15 from _call_sc15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: Установить Пять"
    scene bg club_day with open_eyes
    play music t3
    call sc16 from _call_sc16
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc17 from _call_sc17
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc18 from _call_sc18
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: Установить Шесть"
    scene bg resday with open_eyes
    play music t2
    call sm19 from _call_sm19
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm20 from _call_sm20_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm21 from _call_sm21
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc19 from _call_sc19
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc21 from _call_sc21
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: После Очистки Дружбы"
    scene bg resday with open_eyes
    play music t2
    call sm22 from _call_sm22
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc22 from _call_sc22
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: Установить Дату Один"
    scene bg resday with open_eyes
    play music t2
    call sm23 from _call_sm23
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm24 from _call_sm24_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm25 from _call_sm25
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc23 from _call_sc23
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc25 from _call_sc25
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: Установить Дату Два"
    scene bg resday with open_eyes
    play music t2
    call sm26 from _call_sm26
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm27 from _call_sm27_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm28 from _call_sm28
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc26 from _call_sc26
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc28 from _call_sc28
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: Установить Дату Три"
    scene bg resday with open_eyes
    play music t2
    call sm29 from _call_sm29
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm30 from _call_sm30_1
    scene dark with close_eyes
    pause 0.5
    scene bg resday with open_eyes
    call sm31 from _call_sm31
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call sc29 from _call_sc29
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc31 from _call_sc31
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Сайори: После Очистки Даты"
    scene bg resday with open_eyes
    play music t2
    call sm32 from _call_sm32
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call sc32 from _call_sc32
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    return

label y_app:
    "Юри: Установить Один"
    scene bg class_day with open_eyes
    play music t8
    call yl1 from _call_yl1
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl2 from _call_yl2
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl3 from _call_yl3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call yc1 from _call_yc1
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call yc2 from _call_yc2
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call yc3 from _call_yc3
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Юри: Установить Два"
    scene bg class_day with open_eyes
    play music t8
    call yl4 from _call_yl4
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl5 from _call_yl5
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl6 from _call_yl6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call yc4 from _call_yc4
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call yc5 from _call_yc5
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call yc6 from _call_yc6
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Юри: Установить Три"
    scene bg class_day with open_eyes
    play music t8
    call yl7 from _call_yl7
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl8 from _call_yl8_1
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl9 from _call_yl9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call yc7 from _call_yc7
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call yc9 from _call_yc9
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Юри: Установить Четыре"
    scene bg class_day with open_eyes
    play music t8
    call yl10 from _call_yl10
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl11 from _call_yl11_1
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl12 from _call_yl12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call yc10 from _call_yc10
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call yc12 from _call_yc12
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Юри: Установить Пять"
    scene bg class_day with open_eyes
    play music t8
    call yl13 from _call_yl13
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl14 from _call_yl14_1
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl15 from _call_yl15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call yc13 from _call_yc13
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call yc15 from _call_yc15
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Юри: После Очистки Дружбы"
    scene bg class_day with open_eyes
    play music t8
    call yl16 from _call_yl16
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call yc16 from _call_yc16
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Юри: Установить Дату Один"
    scene bg class_day with open_eyes
    play music t8
    call yl17 from _call_yl17
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl18 from _call_yl18_1
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl19 from _call_yl19
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call yc17 from _call_yc17
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call yc19 from _call_yc19
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Юри: Установить Дату Два"
    scene bg class_day with open_eyes
    play music t8
    call yl20 from _call_yl20
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl21 from _call_yl21_1
    scene dark with close_eyes
    pause 0.5
    scene bg class_day with open_eyes
    call yl22 from _call_yl22
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call yc20 from _call_yc20
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    call yc22 from _call_yc22
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5

    "Юри: После Очистки Даты"
    scene bg class_day with open_eyes
    play music t8
    call yl23 from _call_yl23
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    scene bg club_day with open_eyes
    play music t3
    call yc23 from _call_yc23
    stop music fadeout 2.0
    scene dark with close_eyes
    pause 0.5
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
