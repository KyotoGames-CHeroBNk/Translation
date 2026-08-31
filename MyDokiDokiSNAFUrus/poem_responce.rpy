label poemresponse_start:
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day
            with wipeleft_scene
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5
    label poemresponse_start2:
        if persistent.playthrough == 2:
            $ pt = "2"
        else:
            $ pt = ""
        if poemsread == 0:
            $ menutext = "Кому мне показать своё стихотворение первым?"
        if poemsread < 3:
            $ menutext = "Кому мне показать своё стихотворение?"
        if poemsread == 3:
            $ menutext = "Ну, я думаю, что остается только..."

        menu:
            "[menutext]"

            "Сайори" if not s_readpoem and persistent.playthrough == 0:
                $ s_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "Мне всё ещё комфортнее всего показать своё стихотворение Сайори первой."
                call poemresponse_sayori from _call_poemresponse_sayori
            "Нацуки" if not n_readpoem:
                $ n_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "Я сказал Нацуки, что интересуюсь её стихами вчера."
                    "Вероятно, будет справедливо, если я поделюсь своим с ней первым."
                call poemresponse_natsuki from _call_poemresponse_natsuki
            "Юри" if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "После того, что только что произошло, я не могу не захотеть провести больше времени с Юри."
                call poemresponse_yuri from _call_poemresponse_yuri
            "Моника" if y_readpoem and s_readpoem and n_readpoem:
                $ m_readpoem = True
                if chapter == 1 and poemsread == 3:
                    "Я думаю, что остается только Моника."
                    "Вот и всё."
                call poemresponse_monika from _call_poemresponse_monika
        $ poemsread += 1
        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4):
            jump poemresponse_loop

    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return


label poemresponse_sayori:
    scene bg club_day
    show sayori 1a zorder 2 at t11
    with wipeleft_scene




label poemresponse_yuri:
    scene bg club_day
    show yuri 1a zorder 2 at t11
    with wipeleft_scene




label poemresponse_natsuki:
    scene bg club_day
    show natsuki 1c zorder 2 at t11
    with wipeleft_scene




label poemresponse_monika:
    scene bg club_day
    with wipeleft_scene
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
