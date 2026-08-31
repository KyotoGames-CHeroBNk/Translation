#This is a copy of credits.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Import the datetime library for using time
init python:
    import datetime

#This defines the CGs that disappear after a few seconds
#These are the colored CGs used for scene cgs
image credits_cg1:
    "images/cg/credits/1.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "mod_assets/mc2_cg1.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "mod_assets/m_cg1.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

#These are the grayed out CGs for unseen cgs
image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    size(640, 360)
    8.6
    "images/menu/notfound.png"

#This defines the CGs that don't fade for a "perfect ending"
image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size(640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size(640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size(640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size(640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size(640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size(640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size(640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size(640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size(640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size(640, 360)

#DDLC Logo
image credits_logo:
    "mod_assets/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

#Team Salvato logo
image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

#This styles the different text in the credits
style credits_header:
    font "gui/font/v_CCBellyLaugh.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/comic.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/Adventure.ttf"
    color "#fff"
    size 40
    text_align 0.5
    outlines []

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)

#These are the animations applied to the make the credits and images scroll
transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

#This defines the Karaoke for Monika's singing
image mcredits_1a:
    ypos credits_ypos
    xoffset -205
    "black"
    10.33
    Text("День за днём,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -35
    "black"
    11.75
    Text("строю мир в голове,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 170
    "black"
    13.76
    Text("где будем лишь мы с тобой.", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -226
    "black"
    19.45
    Text("На листе пером выведу стих,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -10
    "black"
    20.9
    Text("в котором ты здесь,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 225
    "black"
    23.27
    Text("со мной.", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("Тёмной лужей чернила вдруг стали,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    xoffset -5
    "black"
    32.9
    Text("Просто пиши -- дай им стать большой рекой!", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("В мире, где миллионы решений,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -145
    "black"
    42.0
    Text("Куда же плыть вместе", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 85
    "black"
    43.47
    Text("с нею за мечтой?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("Какой же путь вместе нас сведет с тобой?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4)

#Glitchy images
image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

#Start for the actual credits scene
label credits:
    #Disable player interactions
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    #Start Monika's spoken dialogue
    play music sign_of_hope

    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat

    jump credits2

#This is where the credits scroll starts=======================================================================================================================================
label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    $ consolehistory = []
    $ starttime = datetime.datetime.now()
    pause 9.12
    #Each CG is shown. If it's unseen gray it out, if it's not a perfect ending
    #make each image get deleted after a few seconds
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    #show image ("credits_cg1" + lockedtext) at credits_scroll_right as credits_image_1
    show image ("credits_cg1") at credits_scroll_right as credits_image_1

    #Actual names for the credits
    show credits_header "Концепция и дизайн игры" at credits_text_scroll_left as credits_header_1
    show credits_text "Dan Salvato\nGuyBread" at credits_text_scroll_left as credits_text_1

    ##The rest of the sections follow this same pattern
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.") from _call_updateconsole_1
    else:
        call updateconsole_clearall("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.") from _call_updateconsole_clearall
    show image ("credits_cg2") at credits_scroll_left as credits_image_2
    show credits_header "Художник по персонажам" at credits_text_scroll_right as credits_header_2
    show credits_text "Satchely\nBlackRabbitArtworks\nKutabare" at credits_text_scroll_right as credits_text_2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.") from _call_updateconsole_2
    else:
        call updateconsole_clearall("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.") from _call_updateconsole_clearall_1
    show image ("credits_cg3") at credits_scroll_right as credits_image_1
    show credits_header "Художник по фонам" at credits_text_scroll_left as credits_header_1
    show credits_text "Velinquent\nCyrke\nMinikle" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.") from _call_updateconsole_3
    else:
        call updateconsole_clearall("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.") from _call_updateconsole_clearall_2
    show image ("credits_cg4") at credits_scroll_left as credits_image_2
    show credits_header "Автор сценария" at credits_text_scroll_right as credits_header_2
    show credits_text "Dan Salvato\nGuyBread" at credits_text_scroll_right as credits_text_2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.") from _call_updateconsole_4
    else:
        call updateconsole_clearall("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.") from _call_updateconsole_clearall_3
    show image ("credits_cg5") at credits_scroll_right as credits_image_1
    show credits_header "Композитор" at credits_text_scroll_left as credits_header_1
    show credits_text "Dan Salvato" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.") from _call_updateconsole_5
    else:
        call updateconsole_clearall("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.") from _call_updateconsole_clearall_4
    show image ("credits_cg6") at credits_scroll_left as credits_image_2
    show credits_header "Вычитка" at credits_text_scroll_right as credits_header_2
    show credits_text "Yog Dzewa\nStormlord\nCaptain Crown" at credits_text_scroll_right as credits_text_2
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.") from _call_updateconsole_6
    else:
        call updateconsole_clearall("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.") from _call_updateconsole_clearall_5
    show image ("credits_cg7") at credits_scroll_right as credits_image_1
    show credits_header "Редактирование/Кодирование" at credits_text_scroll_left as credits_header_1
    show credits_text "GuyBread" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.") from _call_updateconsole_7
    else:
        call updateconsole_clearall("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.") from _call_updateconsole_clearall_6
    show image ("credits_cg8") at credits_scroll_left as credits_image_2
    show credits_header "Особая благодарность" at credits_text_scroll_right as credits_header_2
    show credits_text "Discord Playtesters" at credits_text_scroll_right as credits_text_2
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.") from _call_updateconsole_8
    else:
        call updateconsole_clearall("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.") from _call_updateconsole_clearall_7
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show image ("credits_cg9") at credits_scroll_right as credits_image_1
    show credits_header "Особая благодарность" at credits_text_scroll_left as credits_header_1
    show credits_text "Yog Dzewa\nKutabare" at credits_text_scroll_left as credits_text_1
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/r_cg1.png\")", "r_cg1.png deleted successfully.") from _call_updateconsole_9
    else:
        call updateconsole_clearall("os.remove(\"images/cg/r_cg1.png\")", "r_cg1.png deleted successfully.") from _call_updateconsole_clearall_8
    show image ("credits_cg10") at credits_scroll_left as credits_image_2
    show credits_header "Особая благодарность" at credits_text_scroll_right as credits_header_2
    show credits_text "The Dokis\nKiba\n[player]" at credits_text_scroll_right as credits_text_2
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.") from _call_updateconsole_10
    else:
        call updateconsole_clearall("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.") from _call_updateconsole_clearall_9
    pause 5.0
    stop music fadeout 2.0
    scene dark
    with dissolve_scene_full
    if r_love3 == "True" or m_love1 == "True" or s_love3 == "True" or n_love3 == "True" or y_love2 == "True":
        jump final_day
        return
    else:
        return
