
label s_morning_random:
    if s_scene1 == "False":
        $ renpy.jump('sm'+str(renpy.random.randint(1,3)))
    if s_scene1 == "True" and s_scene2 == "False":
        $ renpy.jump('sm'+str(renpy.random.randint(4,6)))
    if s_scene2 == "True" and s_scene3 == "False":
        $ renpy.jump('sm'+str(renpy.random.randint(7,9)))
    if s_scene3 == "True" and s_scene4 == "False":
        $ renpy.jump('sm'+str(renpy.random.randint(10,12)))
    if s_scene4 == "True" and s_scene5 == "False" and s_love == "False":
        $ renpy.jump('sm'+str(renpy.random.randint(13,15)))


    if s_scene6 == "True" and s_scene7 == "False":
        $ renpy.jump('sm'+str(renpy.random.randint(19,21)))
    if s_scene7 == "True":
        jump sm22
    if s_love == "True" and s_love1 == "False":
        $ renpy.jump('sm'+str(renpy.random.randint(23,25)))
    if s_love1 == "True" and s_love2 == "False":
        $ renpy.jump('sm'+str(renpy.random.randint(26,28)))
    if s_love2 == "True" and s_love3 == "False":
        $ renpy.jump('sm'+str(renpy.random.randint(29,31)))
    if s_love3 == "True":
        jump sm32
    return

label s_club_random:
    if s_scene1 == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(1,3)))
    if s_scene1 == "True" and s_scene2 == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(4,6)))
    if s_scene2 == "True" and s_scene3 == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(7,9)))
    if s_scene3 == "True" and s_scene4 == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(10,12)))
    if s_scene4 == "True" and s_scene5 == "False" and s_love == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(13,15)))
    if s_scene5 == "True" and s_scene6 == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(16,18)))
    if s_scene6 == "True" and s_scene7 == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(19,21)))
    if s_scene7 == "True":
        jump sc22
    if s_love == "True" and s_love1 == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(23,25)))
    if s_love1 == "True" and s_love2 == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(26,28)))
    if s_love2 == "True" and s_love3 == "False":
        $ renpy.jump('sc'+str(renpy.random.randint(29,31)))
    if s_love3 == "True":
        jump sc32
    return


label m_club_random:
    if m_scene1 == "True" and m_scene2 == "False":
        $ renpy.jump('mc'+str(renpy.random.randint(1,3)))
    if m_scene2 == "True" and m_scene3 == "False":
        $ renpy.jump('mc'+str(renpy.random.randint(4,6)))
    if m_scene3 == "True" and m_scene4 == "False":
        $ renpy.jump('mc'+str(renpy.random.randint(7,9)))
    if m_scene4 == "True" and m_scene5 == "False":
        $ renpy.jump('mc'+str(renpy.random.randint(10,12)))
    if m_scene5 == "True" and m_scene6 == "False" and m_love == "False":
        $ renpy.jump('mc'+str(renpy.random.randint(13,15)))
    if m_scene6 == "True":
        jump mc16
    if m_love == "True" and m_love1 == "False":
        $ renpy.jump('mc'+str(renpy.random.randint(17,19)))
    if m_love1 == "True":
        jump mc20
    return


label n_morning_random:
    if n_scene1 == "True" and n_scene2 == "False":
        $ renpy.jump('nm'+str(renpy.random.randint(1,3)))
    elif n_scene2 == "True" and n_scene3 == "False":
        $ renpy.jump('nm'+str(renpy.random.randint(4,6)))
    elif n_scene3 == "True" and n_scene4 == "False":
        $ renpy.jump('nm'+str(renpy.random.randint(7,9)))
    elif n_scene4 == "True" and n_scene5 == "False" and n_love == "False":
        $ renpy.jump('nm'+str(renpy.random.randint(10,12)))
    elif n_scene5 == "True" and n_scene6 == "False":
        $ renpy.jump('nm'+str(renpy.random.randint(13,15)))
    elif n_scene6 == "True":
        jump nm16
    elif n_love == "True" and n_love1 == "False":
        $ renpy.jump('nm'+str(renpy.random.randint(17,19)))
    elif n_love1 == "True" and n_love2 == "False":
        $ renpy.jump('nm'+str(renpy.random.randint(20,22)))
    elif n_love2 == "True" and n_love3 == "False":
        $ renpy.jump('nm'+str(renpy.random.randint(23,25)))
    elif n_love3 == "True":
        jump nm26
    return

label n_club_random:
    if n_scene1 == "False":
        $ renpy.jump('nc'+str(renpy.random.randint(1,3)))
    if n_scene1 == "True" and n_scene2 == "False":
        $ renpy.jump('nc'+str(renpy.random.randint(4,6)))
    if n_scene2 == "True" and n_scene3 == "False":
        $ renpy.jump('nc'+str(renpy.random.randint(7,9)))
    if n_scene3 == "True" and n_scene4 == "False":
        $ renpy.jump('nc'+str(renpy.random.randint(10,12)))
    if n_scene4 == "True" and n_scene5 == "False" and n_love == "False":
        $ renpy.jump('nc'+str(renpy.random.randint(13,15)))
    if n_scene5 == "True" and n_scene6 == "False":
        $ renpy.jump('nc'+str(renpy.random.randint(16,18)))
    if n_scene6 == "True":
        jump nc19
    if n_love == "True" and n_love1 == "False":
        $ renpy.jump('nc'+str(renpy.random.randint(20,22)))
    if n_love1 == "True" and n_love2 == "False":
        $ renpy.jump('nc'+str(renpy.random.randint(23,25)))
    if n_love2 == "True" and n_love3 == "False":
        $ renpy.jump('nc'+str(renpy.random.randint(26,28)))
    if n_love3 == "True":
        jump nc29
    return


label y_lunch_random:
    if y_scene1 == "True" and y_scene2 == "False":
        $ renpy.jump('yl'+str(renpy.random.randint(1,3)))
    if y_scene2 == "True" and y_scene3 == "False":
        $ renpy.jump('yl'+str(renpy.random.randint(1,3)))
    if y_scene3 == "True" and y_scene4 == "False":
        $ renpy.jump('yl'+str(renpy.random.randint(4,6)))
    if y_scene4 == "True" and y_scene5 == "False":
        $ renpy.jump('yl'+str(renpy.random.randint(7,9)))
    if y_scene5 == "True" and y_scene6 == "False":
        $ renpy.jump('yl'+str(renpy.random.randint(10,12)))
    if y_scene6 == "True" and y_scene7 == "False" and y_love == "False":
        $ renpy.jump('yl'+str(renpy.random.randint(10,12)))
    if y_scene7 == "True" and y_scene8 == "False":
        $ renpy.jump('yl'+str(renpy.random.randint(13,15)))
    if y_scene8 == "True":
        jump yl16
    if y_love == "True" and y_love1 == "False":
        $ renpy.jump('yl'+str(renpy.random.randint(17,19)))
    if y_love1 == "True" and y_love2 == "False":
        $ renpy.jump('yl'+str(renpy.random.randint(20,22)))
    if y_love2 == "True":
        jump yl23
    return

label y_club_random:
    if y_scene1 == "True" and y_scene2 == "False":
        $ renpy.jump('yc'+str(renpy.random.randint(1,3)))
    if y_scene2 == "True" and y_scene3 == "False":
        $ renpy.jump('yc'+str(renpy.random.randint(1,3)))
    if y_scene3 == "True" and y_scene4 == "False":
        $ renpy.jump('yc'+str(renpy.random.randint(4,6)))
    if y_scene4 == "True" and y_scene5 == "False":
        $ renpy.jump('yc'+str(renpy.random.randint(7,9)))
    if y_scene5 == "True" and y_scene6 == "False":
        $ renpy.jump('yc'+str(renpy.random.randint(10,12)))
    if y_scene6 == "True" and y_scene7 == "False" and y_love == "False":
        $ renpy.jump('yc'+str(renpy.random.randint(10,12)))
    if y_scene7 == "True" and y_scene8 == "False":
        $ renpy.jump('yc'+str(renpy.random.randint(13,15)))
    if y_scene8 == "True":
        jump yc16
    if y_love == "True" and y_love1 == "False":
        $ renpy.jump('yc'+str(renpy.random.randint(17,19)))
    if y_love1 == "True" and y_love2 == "False":
        $ renpy.jump('yc'+str(renpy.random.randint(20,22)))
    if y_love2 == "True":
        jump yc23
    return



label r_club_random:
    if r_scene1 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(1,3)))
    if r_scene1 == "True" and r_scene2 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(4,6)))
    if r_scene2 == "True" and r_scene3 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(7,9)))
    if r_scene3 == "True" and r_scene4 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(10,12)))
    if r_scene4 == "True" and r_scene5 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(13,15)))
    if r_scene5 == "True" and r_scene6 == "False" and r_love == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(16,18)))
    if r_scene6 == "True" and r_scene7 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(19,21)))
    if r_scene7 == "True":
        jump rc22
    if r_love == "True" and r_love1 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(23,25)))
    if r_love1 == "True" and r_love2 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(26,28)))
    if r_love2 == "True" and r_love3 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(26,28)))
    if r_love3 == "True" and r_love4 == "False":
        $ renpy.jump('rc'+str(renpy.random.randint(29,31)))
    if r_love4 == "True":
        jump rc32
    return

label r_lunch_random:
    if r_scene2 == "True" and r_scene3 == "False":
        jump rl8
    if r_scene3 == "True" and r_scene4 == "False":
        jump rl11
    if r_scene4 == "True" and r_scene5 == "False":
        jump rl14
    if r_scene5 == "True" and r_scene6 == "False" and r_love == "False":
        jump rl17
    if r_scene6 == "True" and r_scene7 == "False":
        jump rl20
    if r_scene7 == "True":
        jump rl22
    if r_love == "True" and r_love1 == "False":
        jump rl24
    if r_love1 == "True" and r_love2 == "False":
        jump rl27
    if r_love2 == "True" and r_love3 == "False":
        jump rl27
    if r_love3 == "True" and r_love4 == "False":
        jump rl30
    if r_love4 == "True":
        jump rl32
    return


label k_morning_random:
    if k_scene1 == "False":
        $ renpy.jump('km'+str(renpy.random.randint(1,3)))
    if k_scene1 == "True" and k_scene2 == "False":
        $ renpy.jump('km'+str(renpy.random.randint(4,6)))
    if k_scene2 == "True" and k_scene3 == "False":
        $ renpy.jump('km'+str(renpy.random.randint(7,9)))
    if k_scene3 == "True" and k_scene4 == "False":
        $ renpy.jump('km'+str(renpy.random.randint(10,12)))
    if k_scene4 == "True" and k_scene5 == "False":
        $ renpy.jump('km'+str(renpy.random.randint(13,15)))
    if k_scene5 == "True":
        jump km16
    return

label k_lunch_random:
    if k_scene1 == "False":
        $ renpy.jump('kl'+str(renpy.random.randint(1,3)))
    if k_scene1 == "True" and k_scene2 == "False":
        $ renpy.jump('kl'+str(renpy.random.randint(4,6)))
    if k_scene2 == "True" and k_scene3 == "False":
        $ renpy.jump('kl'+str(renpy.random.randint(7,9)))
    if k_scene3 == "True" and k_scene4 == "False":
        $ renpy.jump('kl'+str(renpy.random.randint(10,12)))
    if k_scene4 == "True" and k_scene5 == "False":
        $ renpy.jump('kl'+str(renpy.random.randint(13,15)))
    if k_scene5 == "True":
        jump kl16
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
