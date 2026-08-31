
label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer


    $ s_name = "Сайори"
    $ m_name = "Моника"
    $ n_name = "Нацуки"
    $ y_name = "Юри"
    $ k_name = "Киба"
    $ r_name = "Рикка"
    $ i_name = "Инт"
    $ c_name = "Соц"
    $ a_name = "Атл"
    $ e_name = "Опыт"
    $ h_name = "Харуна"
    $ z_name = "???"



    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.example_seen:
        call page_one from _call_page_one_1
    else:
        call page_one from _call_page_one

    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
