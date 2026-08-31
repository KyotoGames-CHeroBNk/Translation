#This is a copy of definitions.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for Definitions
#This section defines stuff for the game: sprite poses for the girls, music, and backgrounds
#If you plan on adding new content, pop them over down there and mimic the appropriate lines!
define persistent.demo = False
define persistent.steam = False
define config.developer = False #Change this flag to True to enable dev tools

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)


#Music
#The Music section is where you can reference existing DDLC audio

#You'll see this in some existing scripts as command 'play music [t1]' for example
#For easier reference, there are comments next to it so you can go DJ on the mod :)
define audio.t1 = "<loop 22.073>bgm/1.ogg"  #Main theme (title)


define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"

#Theseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee----------------------------------------------
define audio.htpg = "mod_assets/HTPG.ogg"
define audio.wefn = "<loop 0>mod_assets/Were_fine.ogg"
define audio.ddsl = "<loop 0>mod_assets/ddsl.ogg"
define audio.spook = "<loop 0.500>mod_assets/spook.ogg"
define audio.happy1 = "<loop 0>mod_assets/happy.ogg"
define audio.alarm = "<loop 0>mod_assets/alarm.ogg"
define audio.ohno = "mod_assets/ohno.mp3"
define audio.sad1 = "mod_assets/sad1.ogg"
define audio.sad2 = "mod_assets/sad2.mp3"
define audio.bell = "mod_assets/bell.ogg"
define audio.knock = "mod_assets/knock.ogg"
define audio.shower = "<loop 0>mod_assets/shower.ogg"
define audio.ring = "<loop 10.000>mod_assets/ring.ogg"
define audio.badp1 = "mod_assets/badp1.ogg"
define audio.badp2 = "mod_assets/badp2.ogg"
define audio.badp3 = "mod_assets/badp3.ogg"
define audio.piano_full = "mod_assets/piano_full.ogg"
define audio.wedig = "<loop 25.000>mod_assets/wedig.ogg"
define audio.hided = "mod_assets/hide.ogg"
define audio.coffee = "mod_assets/coffee.ogg"
define audio.spook2 = "mod_assets/spook2.ogg"
define audio.piano_room = "mod_assets/piano_room.ogg"
define audio.sad1 = "<loop 0>mod_assets/sad1.ogg"
define audio.rain = "mod_assets/rain.mp3"
define audio.sign_of_hope = "mod_assets/sign_of_hope.mp3"

define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems...... 'Okay Everyone~!'
#Hey Mod team, our themes aren't defined here in the original script.
#Did some reading around and there was this + "_character" reference elsewhere.
#Anyhow, I'll try 'defining' them and see if it works!

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" #I'm the only one with pianos x3
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" #Hxppy Thoughts with Ukelele & Snapping~!
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" #Was it always cute on purpose?
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" #Fancy harps and instruments!

#Yeah, Monika... that should be good.
#So, take it from her and if you want to define music, make sure it exists in the appropriate folder
#Define its "audio.name" and see how it goes! (this should always be .ogg too, I think)


define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"


define audio.m1 = "<loop 0>bgm/m1.ogg" #Monika and her spaceroom music
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" #Monika music post-deletion

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.fall2 = "sfx/fall2.ogg"
define audio.gnid = "sfx/gnid.ogg"
define audio.punch = "mod_assets/punch.ogg"



# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg resday = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"
image bg park = "mod_assets/park.png"
image bg split3 = "mod_assets/split3.png"
image bg bathroom_past = "mod_assets/bathroom_past.png"
image bg bathroom = "mod_assets/bathroom.png"
#image bg park = "mod_assets/park.png" ------------------------------------------------------------------------------------------------------------------------------------
image bg fastfood = "mod_assets/fastfood.png"
image bg city2_day = "mod_assets/city2_day.png"
image bg park_day = "mod_assets/park_day.png"
image bg shrine_night = "mod_assets/shrine_night.png"
image bg shrine_nightp = "mod_assets/shrine_nightp.png"
image bg shrine_eve = "mod_assets/shrine_eve.png"
image bg mon = "mod_assets/monday.png"
image bg tues = "mod_assets/tuesday.png"
image bg wed = "mod_assets/wednesday.png"
image bg thur = "mod_assets/thursday.png"
image bg fri = "mod_assets/friday.png"
image bg sat = "mod_assets/saturday.png"
image bg sun = "mod_assets/sunday.png"
image bg city3 = "mod_assets/city3.png"
image bg house_evening = "mod_assets/house_evening.png"
image bg spring = "mod_assets/spring.png"
image bg spring2 = "mod_assets/spring2.png"
image bg spring3 = "mod_assets/spring3.png"
image bg living_evening = "mod_assets/living_evening.png"
image bg m_darkroom = "mod_assets/m_darkroom.png"
image bg living_dark = "mod_assets/living_dark.png"
image bg bed_dark = "mod_assets/bed_dark.png"
image bg bathroom = "mod_assets/bathroom.png"
image bg res_evening = "mod_assets/res_evening.png"
image bg door_m = "mod_assets/door_m.png"
image bg door_n = "mod_assets/door_n.png"
image bg living_day = "mod_assets/living_day.png"
image bg school = "mod_assets/school.png"
image bg kitchen_100 = "mod_assets/kitchen_100.png"
image bg res2 = "mod_assets/res2.png"
image bg house2 = "mod_assets/house2.png"
image bg house1 = "mod_assets/house1.png"
image bg bedroom2 = "mod_assets/bedroom2.png"
image bg resn = "mod_assets/resn.png"
image bg stars = "mod_assets/stars.png"
image bg housen = "mod_assets/housen.png"
image bg bathroom2 = "mod_assets/bathroom2.png"
image bg hall2 = "mod_assets/hall2.png"
image bg kitchen2 = "mod_assets/kitchen2.png"
image bg ph = "mod_assets/placeholder.png"
image bg courtyard = "mod_assets/courtyard.png"
image bg courtyard_past = "mod_assets/courtyard_past.png"
image bg split = "mod_assets/split.png"
image bg split4 = "mod_assets/split4.png"
image bg split5 = "mod_assets/split5.png"
image bg split6 = "mod_assets/split6.png"
image bg split7 = "mod_assets/split7.png"
image bg split8 = "mod_assets/split8.png"
image bg split9 = "mod_assets/split9.png"
image bg split10 = "mod_assets/split10.png"
image bg split11 = "mod_assets/split11.png"
image bg split12 = "mod_assets/split12.png"
image bg club_past = "mod_assets/club-past.png"
image bg corridor_past = "mod_assets/corridor_past.png"
image bg resp = "mod_assets/resp.png"
image bg m_bedroom = "mod_assets/m_bedroom.png"
image bg m_bedroom_eve = "mod_assets/m_bedroom_eve.png"
image bg city = "mod_assets/city.png"
image bg city2 = "mod_assets/city2.png"
image bg cafe = "mod_assets/cafe.png"
image bg cafe_eve = "mod_assets/cafe_eve.png"
image bg cafe_night = "mod_assets/cafe_night.png"
image bg cafe2 = "mod_assets/cafe2.png"
image bg split2 = "mod_assets/split2.png"
image bg bathroom20 = "mod_assets/bathroom20.png"
image bg creditbg = "mod_assets/creditbg.png"
image bg resr = "mod_assets/resr.png"
image mc_sticker1 = "mod_assets/mc_chibi1.png"
image mc_sticker2 = "mod_assets/mc_chibi2.png"
image r_sticker1 = "mod_assets/r_sticker1.png"
image r_sticker2 = "mod_assets/r_sticker2.png"
image s_cg3 = "mod_assets/s_cg3.png"
image s_cg4 = "mod_assets/s_cg4.png"
image n_sticker10 = "gui/poemgame/n_sticker_1.png"
image n_sticker20 = "gui/poemgame/n_sticker_2.png"
image s_sticker1 = "gui/poemgame/s_sticker_1.png"
image s_sticker2 = "gui/poemgame/s_sticker_2.png"
image m_sticker1 = "mod_assets/m_sticker1.png"
image m_sticker2 = "mod_assets/m_sticker2.png"
image bg kitchenp = "mod_assets/kitchenpast.png"
image bg class_rain = "mod_assets/class_rain.png"
image bg track = "mod_assets/track.png"
image bg office = "mod_assets/office.png"
image bg hall3 = "mod_assets/hall3.png"
image bg club_rain = "mod_assets/club_rain.png"
image bg locker_room = "mod_assets/locker_room.png"
image bg track_evening = "mod_assets/track_evening.png"
image bg grocery = "mod_assets/grocery.png"
image bg date_eve = "mod_assets/date_eve.png"
image bg date_day = "mod_assets/date_day.png"
image bg ent_rain = "mod_assets/ent_rain.png"
image bg ent = "mod_assets/ent.png"
image bg s_bathroom = "mod_assets/s_bathroom.png"
image bg home_ec = "mod_assets/home_ec.png"
image bg stairs = "mod_assets/stairs.png"
image bg bookstore = "mod_assets/bookstore.png"
image bg library = "mod_assets/library.png"
image bg city4 = "mod_assets/city4.png"
image bg city5 = "mod_assets/city5.png"
image bg water1_day = "mod_assets/water1_day.png"
image bg water2_day = "mod_assets/water2_day.png"
image bg water2_eve = "mod_assets/water2_eve.png"
image bg water2_past = "mod_assets/water2_past.png"
image bg mall = "mod_assets/mall.png"
image bg store = "mod_assets/store.png"
image bg h_bedroomp = "mod_assets/h_bedroomp.png"
image bg y_kitchen_day = "mod_assets/y_kitchen_day.png"
image bg y_kitchen_eve = "mod_assets/y_kitchen_eve.png"
image bg y_bedroom = "mod_assets/y_bedroom.png"
image bg y_bedroom_eve = "mod_assets/y_bedroom_eve.png"
image bg bedroom_past = "mod_assets/bedroom_past.png"
image bg living_past = "mod_assets/living_past.png"
image bg kitchen3 = "mod_assets/kitchen3.png"
image bg cafe3 = "mod_assets/cafe3.png"
image bg s_bed2 = "mod_assets/s_bed2.png"
image bg street_day = "mod_assets/street_day.png"

image mom = im.Composite((960, 960), (0, 0), "mod_assets/mom.png")
image dad = im.Composite((960, 960), (0, 0), "mod_assets/dad.png")
image sill1 = im.Composite((960, 960), (0, 0), "mod_assets/sill1.png")
image sill2 = im.Composite((960, 960), (0, 0), "mod_assets/sill2.png")
image sill3 = im.Composite((960, 960), (0, 0), "mod_assets/sill3.png")


image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")


#Coding Jazz:
default m_day = "False"
default n_day = "False"
default s_day = "False"
default y_day = "False"
default r_day = "False"
default k_day = "False"

default n_final_appeal = "False"
#default m_final_appeal = "False"
#default s_final_appeal = "False"
#default y_final_appeal = "False"
#default r_final_appeal = "False"
#default k_final_appeal = "False"

default met_club = "False"
default met_rikka = "False"
default stats_list = "False"


default rain = "False"
default gtext = glitchtext(6)

define s_route = "s_route"
default s_route_begin = "False"

define m_route = "m_route"
default m_route_begin = "False"

define n_route = "n_route"
default n_route_begin = "False"

define y_route = "y_route"
default y_route_begin = "False"

define r_route = "r_route"
default r_route_begin = "False"

define s_scene0 = "s_scene0"
define n_scene0 = "n_scene0"
define m_scene0 = "m_scene0"
define y_scene0 = "y_scene0"
define r_scene0 = "r_scene0"

default y_carry = "False"
default n_carry = "False"
default m_carry2 = "False"
default cram = "False"

default ch1_book12 = "False"
default n_start = "False"
default admission = "False"
default p_girls = "False"
default cut_hand = "False"
default ch1_chibi = "False"
default chibi2 = "False"
default akiba_trip = "False"
default golden_track = "False"
default golden_club = "False"
default golden_week_end = "False"
default midterms = "False"

default n_casual = "False"

default a_date = "False"
default y_date = "False"
default s_date = "False"
default n_date = "False"
default m_date = "False"
default r_date = "False"

default ch1_scene = "False"
default s_shopping = "False"
default s_scene1 = "False"
default s_scene2 = "False"
default s_scene3 = "False"
default s_scene4 = "False"
default s_scene5 = "False"
default s_mad = "False"
default m_help = "False"
default s_scene6 = "False"
default s_scene7 = "False"
default s_love = "False"
default s_love1 = "False"
default s_love2 = "False"
default s_love3 = "False"

default y_out = "False"
default y_weekend = "False"
default m_out = "False"
default m_weekend = "False"
default n_out = "False"
default n_weekend = "False"
default s_out = "False"
default s_weekend = "False"
default r_out = "False"
default r_weekend = "False"
default k_out = "False"
default k_weekend = "False"

default y_sunday1 = "False"
default y_scene1 = "False"
default y_scene2 = "False"
default y_scene3 = "False"
default y_scene4 = "False"
default y_scene5 = "False"
default y_scene6 = "False"
default y_scene7 = "False"
default y_scene8 = "False"
default y_love = "False"
default y_love1 = "False"
default y_love2 = "False"

default n_scene1 = "False"
default n_scene2 = "False"
default n_scene3 = "False"
default n_scene4 = "False"
default n_scene5 = "False"
default n_scene6 = "False"
default n_love = "False"
default n_love1 = "False"
default n_love2 = "False"
default n_love3 = "False"
default n_lunch = "False"
default n_sunday1 = "False"

default m_end = "False"
default m_scene1 = "False"
default m_scene2 = "False"
default m_scene3 = "False"
default m_scene4 = "False"
default m_scene5 = "False"
default m_scene6 = "False"
default m_love = "False"
default m_love1 = "False"
default m_love2 = "False"
default m_love3 = "False"

default r_lunch1 = "False"
default r_lunch2 = "False"
default r_long_date = "False"
default r_date_set = "False"
default r_route = "False"
default r_scene1 = "False"
default r_scene2 = "False"
default r_scene3 = "False"
default r_scene4 = "False"
default r_scene5 = "False"
default r_scene6 = "False"
default r_scene7 = "False"
default r_scene8 = "False"
default r_love = "False"
default r_love1 = "False"
default r_love2 = "False"
default r_love3 = "False"
default r_love4 = "False"
default rc15 = "False"

default k_scene1 = "False"
default k_scene2 = "False"
default k_scene3 = "False"
default k_scene4 = "False"
default k_scene5 = "False"
default k_scene6 = "False"

default d_scene1 = "False"
default d_scene2 = "False"
default d_scene3 = "False"

default ch1_book11 = "False"
default ch1_book12 = "False"
default ch1_book13 = "False"
default ch1_book14 = "False"
default ch1_book15 = "False"
default int_lvl1 = "False"
default int_lvl2 = "False"
default int_lvl3 = "False"
default int_lvl4 = "False"
default soc_lvl1 = "False"
default soc_lvl2 = "False"
default soc_lvl3 = "False"
default soc_lvl4 = "False"
default ath_lvl1 = "False"
default ath_lvl2 = "False"
default ath_lvl3 = "False"
default ath_lvl4 = "False"

default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0
default k_appeal = 0
default r_appeal = 0
default d_appeal = 0

default i_appeal = 0
default a_appeal = 0
default c_appeal = 0

default route_start = "False"
default persistent.message = "False"
default persistent.end = "False"

#------------------------------------------------From hereon, the girl's bodies are defined along with their heads.
#-----------------------------------------here's reference for the left half------the right half--------the head
# Sayori
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

image sayori 1ba2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/a2.png")
image sayori 2ba2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/a2.png")
image sayori 3ba2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/a2.png")
image sayori 4ba2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/a2.png")

image sayori 1k2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/k2.png")
image sayori 2k2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/k2.png")
image sayori 3k2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/k2.png")
image sayori 4k2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/k2.png")

image sayori 1bk2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/k2.png")
image sayori 2bk2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/k2.png")
image sayori 3bk2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/k2.png")
image sayori 4bk2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/k2.png")

image sayori 1b2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/b2.png")
image sayori 2b2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/b2.png")
image sayori 3b2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/b2.png")
image sayori 4b2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/b2.png")

image sayori 1g2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/g2.png")
image sayori 2g2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/g2.png")
image sayori 3g2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/g2.png")
image sayori 4g2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/g2.png")
image sayori 1bg2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/g2.png")
image sayori 2bg2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/g2.png")
image sayori 3bg2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/g2.png")
image sayori 4bg2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/g2.png")

image sayori 1bb2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/b2.png")
image sayori 2bb2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/b2.png")
image sayori 3bb2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/b2.png")
image sayori 4bb2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/b2.png")

image sayori 1t2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/t2.png")
image sayori 2t2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/t2.png")
image sayori 3t2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/t2.png")
image sayori 4t2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/t2.png")

image sayori 1bt2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/t2.png")
image sayori 2bt2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/t2.png")
image sayori 3bt2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/t2.png")
image sayori 4bt2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/t2.png")

image sayori 1d2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/d2.png")
image sayori 2d2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/d2.png")
image sayori 3d2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/d2.png")
image sayori 4d2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/d2.png")
image sayori 1bd2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/d2.png")
image sayori 2bd2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/d2.png")
image sayori 3bd2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/d2.png")
image sayori 4bd2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/d2.png")

image sayori 1g3 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sg3.png")
image sayori 2g3 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sg3.png")
image sayori 3g3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sg3.png")
image sayori 4g3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sg3.png")
image sayori 1bg3 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sg3.png")
image sayori 2bg3 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sg3.png")
image sayori 3bg3 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sg3.png")
image sayori 4bg3 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sg3.png")

image sayori 1h2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sh2.png")
image sayori 2h2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sh2.png")
image sayori 3h2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sh2.png")
image sayori 4h2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sh2.png")
image sayori 1bh2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sh2.png")
image sayori 2bh2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sh2.png")
image sayori 3bh2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sh2.png")
image sayori 4bh2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sh2.png")

image sayori 1k3 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/k3.png")
image sayori 2k3 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/k3.png")
image sayori 3k3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/k3.png")
image sayori 4k3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/k3.png")
image sayori 1bk3 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/k3.png")
image sayori 2bk3 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/k3.png")
image sayori 3bk3 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/k3.png")
image sayori 4bk3 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/k3.png")

image sayori 1l2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sl2.png")
image sayori 2l2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sl2.png")
image sayori 3l2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sl2.png")
image sayori 4l2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sl2.png")
image sayori 1bl2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sl2.png")
image sayori 2bl2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sl2.png")
image sayori 3bl2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sl2.png")
image sayori 4bl2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sl2.png")

image sayori 1m2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sm2.png")
image sayori 2m2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sm2.png")
image sayori 3m2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sm2.png")
image sayori 4m2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sm2.png")
image sayori 1bm2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sm2.png")
image sayori 2bm2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sm2.png")
image sayori 3bm2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sm2.png")
image sayori 4bm2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sm2.png")

image sayori 1q2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sq2.png")
image sayori 2q2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sq2.png")
image sayori 3q2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/sq2.png")
image sayori 4q2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/sq2.png")
image sayori 1bq2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sq2.png")
image sayori 2bq2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sq2.png")
image sayori 3bq2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/sq2.png")
image sayori 4bq2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/sq2.png")
image sayori 1cq2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sq2.png")
image sayori 2cq2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sq2.png")
image sayori 3cq2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sq2.png")
image sayori 4cq2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sq2.png")

image sayori 1s2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/ss2.png")
image sayori 2s2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/ss2.png")
image sayori 3s2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/ss2.png")
image sayori 4s2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/ss2.png")
image sayori 1bs2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/ss2.png")
image sayori 2bs2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/ss2.png")
image sayori 3bs2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/ss2.png")
image sayori 4bs2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/ss2.png")

image sayori 1u2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/u2.png")
image sayori 2u2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/u2.png")
image sayori 3u2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "mod_assets/u2.png")
image sayori 4u2 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/u2.png")
image sayori 1bu2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/u2.png")
image sayori 2bu2 = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/u2.png")
image sayori 3bu2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/u2.png")
image sayori 4bu2 = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/u2.png")
#
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 5ba = im.Composite((960, 960), (0, 0), "mod_assets/5ba.png")
image sayori 5bb2 = im.Composite((960, 960), (0, 0), "mod_assets/5bb2.png")
image sayori 5bc = im.Composite((960, 960), (0, 0), "mod_assets/5bc.png")
image sayori 5bd = im.Composite((960, 960), (0, 0), "mod_assets/5bd.png")

image sayori 5ca = im.Composite((960, 960), (0, 0), "mod_assets/sc/5ca.png")
image sayori 5cb = im.Composite((960, 960), (0, 0), "mod_assets/sc/5cb.png")
image sayori 5cc = im.Composite((960, 960), (0, 0), "mod_assets/sc/5cc.png")
image sayori 5cd = im.Composite((960, 960), (0, 0), "mod_assets/sc/5cd.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")
image sayori 1bz = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "mod_assets/z.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")
image sayori 4bz = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "mod_assets/z1.png")
image sayori 4z1 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "mod_assets/z1.png")

image sayori 1ch2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sh2.png")
image sayori 2ch2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sh2.png")
image sayori 3ch2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sh2.png")
image sayori 4ch2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sh2.png")

image sayori 1ca = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/a.png")
image sayori 1cb = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/b.png")
image sayori 1cb2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/b2.png")
image sayori 1cc = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/c.png")
image sayori 1cd = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/d.png")
image sayori 1cd2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/d2.png")
image sayori 1ce = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/e.png")
image sayori 1cf = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/f.png")
image sayori 1cg = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/g.png")
image sayori 1cg2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/g2.png")
image sayori 1cg3 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sg3.png")
image sayori 1ch = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/h.png")
image sayori 1ci = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/i.png")
image sayori 1cj = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/j.png")
image sayori 1ck = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/k.png")
image sayori 1ck2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/k2.png")
image sayori 1ck3 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/k3.png")
image sayori 1cl = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/l.png")
image sayori 1cl2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sl2.png")
image sayori 1cm = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/m.png")
image sayori 1cm2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sm2.png")
image sayori 1cn = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/n.png")
image sayori 1co = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/o.png")
image sayori 1cp = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/p.png")
image sayori 1cq = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/q.png")
image sayori 1cr = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/r.png")
image sayori 1cs = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/s.png")
image sayori 1cs2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/s2.png")
image sayori 1ct = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/t.png")
image sayori 1ct2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/t2.png")
image sayori 1cu = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/u.png")
image sayori 1cu2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/u2.png")
image sayori 1cv = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/v.png")
image sayori 1cw = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/w.png")
image sayori 1cx = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/x.png")
image sayori 1cy = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/y.png")
image sayori 1cz1 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/z1.png")

image sayori 2ca = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/a.png")
image sayori 2cb = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/b.png")
image sayori 2cb2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/b2.png")
image sayori 2cc = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/c.png")
image sayori 2cd = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/d.png")
image sayori 2cd2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/d2.png")
image sayori 2ce = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/e.png")
image sayori 2cf = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/f.png")
image sayori 2cg = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/g.png")
image sayori 2cg2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/g2.png")
image sayori 2cg3 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sg3.png")
image sayori 2ch = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/h.png")
image sayori 2ci = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/i.png")
image sayori 2cj = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/j.png")
image sayori 2ck = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/k.png")
image sayori 2ck2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/k2.png")
image sayori 2ck3 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/k3.png")
image sayori 2cl = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/l.png")
image sayori 2cl2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sl2.png")
image sayori 2cm = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/m.png")
image sayori 2cm2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sm2.png")
image sayori 2cn = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/n.png")
image sayori 2co = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/o.png")
image sayori 2cp = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/p.png")
image sayori 2cq = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/q.png")
image sayori 2cr = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/r.png")
image sayori 2cs = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/s.png")
image sayori 2cs2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/s2.png")
image sayori 2ct = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/t.png")
image sayori 2ct2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/t2.png")
image sayori 2cu = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/u.png")
image sayori 2cu2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/u2.png")
image sayori 2cv = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/v.png")
image sayori 2cw = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/w.png")
image sayori 2cx = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/x.png")
image sayori 2cy = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/y.png")
image sayori 2cz1 = im.Composite((960, 960), (0, 0), "mod_assets/sc/1l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/z1.png")

image sayori 3ca = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/a.png")
image sayori 3cb = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/b.png")
image sayori 3cb2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/b2.png")
image sayori 3cc = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/c.png")
image sayori 3cd = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/d.png")
image sayori 3cd2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/d2.png")
image sayori 3ce = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/e.png")
image sayori 3cf = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/f.png")
image sayori 3cg = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/g.png")
image sayori 3cg2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/g2.png")
image sayori 3cg3 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sg3.png")
image sayori 3ch = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/h.png")
image sayori 3ci = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/i.png")
image sayori 3cj = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/j.png")
image sayori 3ck = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/k.png")
image sayori 3ck2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/k2.png")
image sayori 3ck3 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/k3.png")
image sayori 3cl = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/l.png")
image sayori 3cl2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sl2.png")
image sayori 3cm = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/m.png")
image sayori 3cm2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/sm2.png")
image sayori 3cn = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/n.png")
image sayori 3co = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/o.png")
image sayori 3cp = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/p.png")
image sayori 3cq = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/q.png")
image sayori 3cr = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/r.png")
image sayori 3cs = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/s.png")
image sayori 3cs2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/s2.png")
image sayori 3ct = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/t.png")
image sayori 3ct2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/t2.png")
image sayori 3cu = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/u.png")
image sayori 3cu2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/u2.png")
image sayori 3cv = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/v.png")
image sayori 3cw = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/w.png")
image sayori 3cx = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/x.png")
image sayori 3cy = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "sayori/y.png")
image sayori 3cz1 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/1r.png", (0, 0), "mod_assets/z1.png")

image sayori 4ca = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/a.png")
image sayori 4cb = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/b.png")
image sayori 4cb2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/b2.png")
image sayori 4cc = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/c.png")
image sayori 4cd = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/d.png")
image sayori 4cd2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/d2.png")
image sayori 4ce = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/e.png")
image sayori 4cf = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/f.png")
image sayori 4cg = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/g.png")
image sayori 4cg2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/g2.png")
image sayori 4cg3 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sg3.png")
image sayori 4ch = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/h.png")
image sayori 4ci = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/i.png")
image sayori 4cj = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/j.png")
image sayori 4ck = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/k.png")
image sayori 4ck2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/k2.png")
image sayori 4ck3 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/k3.png")
image sayori 4cl = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/l.png")
image sayori 4cl2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sl2.png")
image sayori 4cm = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/m.png")
image sayori 4cm2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/sm2.png")
image sayori 4cn = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/n.png")
image sayori 4co = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/o.png")
image sayori 4cp = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/p.png")
image sayori 4cq = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/q.png")
image sayori 4cr = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/r.png")
image sayori 4cs = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/s.png")
image sayori 4cs2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/s2.png")
image sayori 4ct = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/t.png")
image sayori 4ct2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/t2.png")
image sayori 4cu = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/u.png")
image sayori 4cu2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/u2.png")
image sayori 4cv = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/v.png")
image sayori 4cw = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/w.png")
image sayori 4cx = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/x.png")
image sayori 4cy = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "sayori/y.png")
image sayori 4cz1 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2l.png", (0, 0), "mod_assets/sc/2r.png", (0, 0), "mod_assets/z1.png")

image sayori 3zy = im.Composite((960, 960), (0, 0), "mod_assets/sc/2zl.png", (0, 0), "mod_assets/sc/1zr.png", (0, 0), "sayori/y.png")
image sayori 3zl2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2zl.png", (0, 0), "mod_assets/sc/1zr.png", (0, 0), "mod_assets/sl2.png")
image sayori 4zp = im.Composite((960, 960), (0, 0), "mod_assets/sc/2zl.png", (0, 0), "mod_assets/sc/2zr.png", (0, 0), "sayori/p.png")
image sayori 4zm = im.Composite((960, 960), (0, 0), "mod_assets/sc/2zl.png", (0, 0), "mod_assets/sc/2zr.png", (0, 0), "sayori/m.png")
image sayori 4zg2 = im.Composite((960, 960), (0, 0), "mod_assets/sc/2zl.png", (0, 0), "mod_assets/sc/2zr.png", (0, 0), "mod_assets/g2.png")

image sayori 6a = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/a.png")
image sayori 6b = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/b.png")
image sayori 6b2 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/b2.png")
image sayori 6c = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/c.png")
image sayori 6d = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/d.png")
image sayori 6d2 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/d2.png")
image sayori 6e = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/e.png")
image sayori 6f = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/f.png")
image sayori 6g = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/g.png")
image sayori 6g2 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/g2.png")
image sayori 6g3 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/sg3.png")
image sayori 6h = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/h.png")
image sayori 6i = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/i.png")
image sayori 6j = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/j.png")
image sayori 6k = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/k.png")
image sayori 6k2 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/k2.png")
image sayori 6k3 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/k3.png")
image sayori 6l = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/l.png")
image sayori 6l2 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/sl2.png")
image sayori 6m = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/m.png")
image sayori 6m2 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/sm2.png")
image sayori 6n = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/n.png")
image sayori 6o = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/o.png")
image sayori 6p = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/p.png")
image sayori 6q = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/q.png")
image sayori 6r = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/r.png")
image sayori 6s = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/s.png")
image sayori 6s2 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/s2.png")
image sayori 6t = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/t.png")
image sayori 6t2 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/t2.png")
image sayori 6u = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/u.png")
image sayori 6u2 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/u2.png")
image sayori 6v = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/v.png")
image sayori 6w = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/w.png")
image sayori 6x = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/x.png")
image sayori 6y = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "sayori/y.png")
image sayori 6z1 = im.Composite((960, 960), (0, 0), "mod_assets/6rl.png", (0, 0), "mod_assets/z1.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki
image natsuki 1k2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/nk2.png")
image natsuki 2k2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/nk2.png")
image natsuki 3k2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/nk2.png")
image natsuki 4k2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/nk2.png")
image natsuki 5k2 = im.Composite((960, 960), (18, 22), "mod_assets/nk2.png", (0, 0), "natsuki/3.png")

image natsuki 1c2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/c2.png")
image natsuki 2c2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/c2.png")
image natsuki 3c2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/c2.png")
image natsuki 4c2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/c2.png")
image natsuki 5c2 = im.Composite((960, 960), (18, 22), "mod_assets/c2.png", (0, 0), "natsuki/3.png")
image natsuki 1bc2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/c2.png")
image natsuki 2bc2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/c2.png")
image natsuki 3bc2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/c2.png")
image natsuki 4bc2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/c2.png")
image natsuki 5bc2 = im.Composite((960, 960), (18, 22), "mod_assets/c2.png", (0, 0), "natsuki/3b.png")

image natsuki 1m2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/m2.png")
image natsuki 2m2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/m2.png")
image natsuki 3m2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/m2.png")
image natsuki 4m2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/m2.png")
image natsuki 5m2 = im.Composite((960, 960), (18, 22), "mod_assets/m2.png", (0, 0), "natsuki/3.png")

image natsuki 1g2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/ng2.png")
image natsuki 2g2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/ng2.png")
image natsuki 3g2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/ng2.png")
image natsuki 4g2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/ng2.png")
image natsuki 5g2 = im.Composite((960, 960), (18, 22), "mod_assets/ng2.png", (0, 0), "natsuki/3.png")

image natsuki 1bg2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/ng2.png")
image natsuki 2bg2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/ng2.png")
image natsuki 3bg2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/ng2.png")
image natsuki 4bg2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/ng2.png")
image natsuki 5bg2 = im.Composite((960, 960), (18, 22), "mod_assets/ng2.png", (0, 0), "natsuki/3b.png")

image natsuki 1g3 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/g3.png")
image natsuki 2g3 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/g3.png")
image natsuki 3g3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/g3.png")
image natsuki 4g3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/g3.png")
image natsuki 5g3 = im.Composite((960, 960), (18, 22), "mod_assets/g3.png", (0, 0), "natsuki/3.png")

image natsuki 1bg3 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/g3.png")
image natsuki 2bg3 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/g3.png")
image natsuki 3bg3 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/g3.png")
image natsuki 4bg3 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/g3.png")
image natsuki 5bg3 = im.Composite((960, 960), (18, 22), "mod_assets/g3.png", (0, 0), "natsuki/3b.png")

image natsuki 1n2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/n2.png")
image natsuki 2n2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/n2.png")
image natsuki 3n2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/n2.png")
image natsuki 4n2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/n2.png")
image natsuki 5n2 = im.Composite((960, 960), (18, 22), "mod_assets/n2.png", (0, 0), "natsuki/3.png")

image natsuki 1bn2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/n2.png")
image natsuki 2bn2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/n2.png")
image natsuki 3bn2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/n2.png")
image natsuki 4bn2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/n2.png")
image natsuki 5bn2 = im.Composite((960, 960), (18, 22), "mod_assets/n2.png", (0, 0), "natsuki/3b.png")

image natsuki 1x2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/x2.png")
image natsuki 2x2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/x2.png")
image natsuki 3x2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/x2.png")
image natsuki 4x2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/x2.png")
image natsuki 5x2 = im.Composite((960, 960), (18, 22), "mod_assets/x2.png", (0, 0), "natsuki/3.png")

image natsuki 1bx2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/x2.png")
image natsuki 2bx2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/x2.png")
image natsuki 3bx2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/x2.png")
image natsuki 4bx2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/x2.png")
image natsuki 5bx2 = im.Composite((960, 960), (18, 22), "mod_assets/x2.png", (0, 0), "natsuki/3b.png")

image natsuki 1bm2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/m2.png")
image natsuki 2bm2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/m2.png")
image natsuki 3bm2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/m2.png")
image natsuki 4bm2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/m2.png")
image natsuki 5bm2 = im.Composite((960, 960), (18, 22), "mod_assets/m2.png", (0, 0), "natsuki/3b.png")

image natsuki 6a = im.Composite((960, 960), (0, 0), "mod_assets/n_laugh.png")

image natsuki 1bk2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/nk2.png")
image natsuki 2bk2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/nk2.png")
image natsuki 3bk2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/nk2.png")
image natsuki 4bk2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/nk2.png")
image natsuki 5bk2 = im.Composite((960, 960), (18, 22), "mod_assets/nk2.png", (0, 0), "natsuki/3b.png")

image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 4s2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/s2.png")
image natsuki 3s2 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/s2.png")
image natsuki 2s2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "mod_assets/s2.png")
image natsuki 1s2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "mod_assets/s2.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5s2 = im.Composite((960, 960), (18, 22), "mod_assets/s2.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
#image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")


image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bs2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/s2.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bs2 = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/s2.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bs2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "mod_assets/s2.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bs2 = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "mod_assets/s2.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs2 = im.Composite((960, 960), (18, 22), "mod_assets/s2.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 5a = im.Composite((960, 960), (0, 0), "mod_assets/5a.png")

#===================================================================================================================================================================
image yuri 1q2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/yq2.png")
image yuri 2q2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yq2.png")
image yuri 3q2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/yq2.png")
image yuri 1bq2 = im.Composite((960, 960), (0, 0), "mod_assets/yq2.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 2bq2 = im.Composite((960, 960), (0, 0), "mod_assets/yq2.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq2 = im.Composite((960, 960), (0, 0), "mod_assets/yq2.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 5q2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "mod_assets/yq2.png")
image yuri 6q2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "mod_assets/yq2.png")
image yuri 5bq2 = im.Composite((960, 960), (0, 0), "mod_assets/yq2.png", (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5br.png")
image yuri 6bq2 = im.Composite((960, 960), (0, 0), "mod_assets/yq2.png", (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5br.png")
image yuri 7bq2 = im.Composite((960, 960), (0, 0), "mod_assets/yq2.png", (0, 0), "yuri/1l.png", (0, 0), "mod_assets/7br.png")
image yuri 8bq2 = im.Composite((960, 960), (0, 0), "mod_assets/yq2.png", (0, 0), "yuri/2l.png", (0, 0), "mod_assets/7br.png")

image yuri 1w2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "mod_assets/w2.png")
image yuri 2w2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/w2.png")
image yuri 3w2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "mod_assets/w2.png")
image yuri 1bw2 = im.Composite((960, 960), (0, 0), "mod_assets/w2.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 2bw2 = im.Composite((960, 960), (0, 0), "mod_assets/w2.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw2 = im.Composite((960, 960), (0, 0), "mod_assets/w2.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 5w2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "mod_assets/w2.png")
image yuri 6w2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "mod_assets/w2.png")
image yuri 5bw2 = im.Composite((960, 960), (0, 0), "mod_assets/w2.png", (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5br.png")
image yuri 6bw2 = im.Composite((960, 960), (0, 0), "mod_assets/w2.png", (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5br.png")
image yuri 7bw2 = im.Composite((960, 960), (0, 0), "mod_assets/w2.png", (0, 0), "yuri/1l.png", (0, 0), "mod_assets/7br.png")
image yuri 8bw2 = im.Composite((960, 960), (0, 0), "mod_assets/w2.png", (0, 0), "yuri/2l.png", (0, 0), "mod_assets/7br.png")

image yuri 5a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/a.png")
image yuri 5b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/b.png")
image yuri 5c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/c.png")
image yuri 5d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/d.png")
image yuri 5e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/e.png")
image yuri 5f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/f.png")
image yuri 5g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/g.png")
image yuri 5h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/h.png")
image yuri 5i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/i.png")
image yuri 5j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/j.png")
image yuri 5k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/k.png")
image yuri 5l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/l.png")
image yuri 5m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/m.png")
image yuri 5n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/n.png")
image yuri 5o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/o.png")
image yuri 5p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/p.png")
image yuri 5q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/q.png")
image yuri 5r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/r.png")
image yuri 5s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/s.png")
image yuri 5t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/t.png")
image yuri 5u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/u.png")
image yuri 5v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/v.png")
image yuri 5w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/w.png")

image yuri 6a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/a.png")
image yuri 6b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/b.png")
image yuri 6c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/c.png")
image yuri 6d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/d.png")
image yuri 6e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/e.png")
image yuri 6f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/f.png")
image yuri 6g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/g.png")
image yuri 6h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/h.png")
image yuri 6i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/i.png")
image yuri 6j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/j.png")
image yuri 6k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/k.png")
image yuri 6l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/l.png")
image yuri 6m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/m.png")
image yuri 6n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/n.png")
image yuri 6o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/o.png")
image yuri 6p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/p.png")
image yuri 6q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/q.png")
image yuri 6r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/r.png")
image yuri 6s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/s.png")
image yuri 6t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/t.png")
image yuri 6u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/u.png")
image yuri 6v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/v.png")
image yuri 6w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "mod_assets/5r.png", (0, 0), "yuri/w.png")

image yuri 5ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")
image yuri 5bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/5br.png")

image yuri 6ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")
image yuri 6bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/5br.png")

image yuri 7ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")
image yuri 7bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "mod_assets/7br.png")

image yuri 8ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")
image yuri 8bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "mod_assets/7br.png")

#===================================================================================================================================================================

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")


image n_sticker2 = im.Composite((141, 159), (0, 0), "mod_assets/n_sticker2.png")
image n_sticker1 = im.Composite((141, 161), (0, 0), "mod_assets/n_sticker1.png")
image y_sticker1 = im.Composite((112, 161), (0, 0), "gui/poemgame/y_sticker_1.png")
image y_sticker2 = im.Composite((112, 161), (0, 0), "gui/poemgame/y_sticker_2.png")
image m_sticker10 = im.Composite((119, 168), (0, 0), "gui/poemgame/m_sticker_1.png")
image m_sticker20 = im.Composite((119, 168), (0, 0), "gui/poemgame/m_sticker_2.png")


image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

#------------------------------------------------Our beloved Monika only has her school uniform here, but that can change!

# Just Monika
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")
image monika 4s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/s.png")
image monika ghost = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/ghost.png")
#====================================================================================================================================================================
image monika 1mb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/mb.png")
image monika 2mb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/mb.png")
image monika 3mb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/mb.png")
image monika 4mb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/mb.png")

image monika 1ob = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/ob.png")
image monika 2ob = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/ob.png")
image monika 3ob = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/ob.png")
image monika 4ob = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/ob.png")

image monika 1s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/s.png")
image monika 2s = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/s.png")
image monika 3s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/s.png")
image monika 4s = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/s.png")

image monika 1bob = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/ob.png")
image monika 2bob = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/ob.png")
image monika 3bob = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/ob.png")
image monika 4bob = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/ob.png")

image monika 1pb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/pb.png")
image monika 2pb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/pb.png")
image monika 3pb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/pb.png")
image monika 4pb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/pb.png")

image monika 1q2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/q2.png")
image monika 2q2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/q2.png")
image monika 3q2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/q2.png")
image monika 4q2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/q2.png")

image monika 1bq2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/q2.png")
image monika 2bq2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/q2.png")
image monika 3bq2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/q2.png")
image monika 4bq2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/q2.png")

image monika 1h2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/h2.png")
image monika 2h2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/h2.png")
image monika 3h2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/h2.png")
image monika 4h2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/h2.png")

image monika 1bh2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/h2.png")
image monika 2bh2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/h2.png")
image monika 3bh2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/h2.png")
image monika 4bh2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/h2.png")

image monika 1i2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/i2.png")
image monika 2i2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/i2.png")
image monika 3i2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/i2.png")
image monika 4i2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/i2.png")

image monika 1bi2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/i2.png")
image monika 2bi2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/i2.png")
image monika 3bi2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/i2.png")
image monika 4bi2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/i2.png")

image monika 1l2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/l2.png")
image monika 2l2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/l2.png")
image monika 3l2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/l2.png")
image monika 4l2 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/l2.png")

image monika 1bl2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/l2.png")
image monika 2bl2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/l2.png")
image monika 3bl2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/l2.png")
image monika 4bl2 = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/l2.png")

image monika 1bpb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/pb.png")
image monika 2bpb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/pb.png")
image monika 3bpb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/pb.png")
image monika 4bpb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/pb.png")

image monika 1fs = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/fs.png")
image monika 2fs = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/fs.png")
image monika 3fs = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/fs.png")
image monika 4fs = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/fs.png")

image monika 1bfs = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/fs.png")
image monika 2bfs = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/fs.png")
image monika 3bfs = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/fs.png")
image monika 4bfs = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/fs.png")

image monika 1os = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/os.png")
image monika 2os = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/os.png")
image monika 3os = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/os.png")
image monika 4os = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/os.png")

image monika 1bos = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/os.png")
image monika 2bos = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/os.png")
image monika 3bos = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/os.png")
image monika 4bos = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/os.png")

image monika 1qs = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/qs.png")
image monika 2qs = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/qs.png")
image monika 3qs = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/qs.png")
image monika 4qs = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/qs.png")

image monika 1bqs = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/qs.png")
image monika 2bqs = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/qs.png")
image monika 3bqs = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/qs.png")
image monika 4bqs = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/qs.png")

image monika 1db = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/db.png")
image monika 2db = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/db.png")
image monika 3db = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/db.png")
image monika 4db = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/db.png")

image monika 1bdb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/db.png")
image monika 2bdb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/db.png")
image monika 3bdb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/db.png")
image monika 4bdb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/db.png")

image monika 1nb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/nb.png")
image monika 2nb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/nb.png")
image monika 3nb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/nb.png")
image monika 4nb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/nb.png")

image monika 1bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/nb.png")
image monika 2bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/nb.png")
image monika 3bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/nb.png")
image monika 4bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/nb.png")

image monika 1bs = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/s.png")
image monika 2bs = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/s.png")
image monika 3bs = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/s.png")
image monika 4bs = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/s.png")

image monika 1eb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/eb.png")
image monika 2eb = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/eb.png")
image monika 3eb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "mod_assets/eb.png")
image monika 4eb = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "mod_assets/eb.png")

image monika 1beb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/eb.png")
image monika 2beb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/eb.png")
image monika 3beb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/eb.png")
image monika 4beb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/eb.png")

image monika 4bp2 = im.Composite((960, 960), (0, 0), "mod_assets/2l_past.png", (0, 0), "mod_assets/2r_past.png", (0, 0), "mod_assets/b_past.png")
image monika 1kp = im.Composite((960, 960), (0, 0), "mod_assets/1l_past.png", (0, 0), "mod_assets/1r_past.png", (0, 0), "mod_assets/k_past.png")
image monika 1bp2 = im.Composite((960, 960), (0, 0), "mod_assets/1l_past.png", (0, 0), "mod_assets/1r_past.png", (0, 0), "mod_assets/b_past.png")
image monika 1dp = im.Composite((960, 960), (0, 0), "mod_assets/1l_past.png", (0, 0), "mod_assets/1r_past.png", (0, 0), "mod_assets/d_past.png")
image monika ghostp = im.Composite((960, 960), (0, 0), "mod_assets/1l_past.png", (0, 0), "mod_assets/1r_past.png", (0, 0), "mod_assets/ghostp.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

# Monika's House outfit======================================================================================================================================================

image monika 1ba = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/a.png")
image monika 1bb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/b.png")
image monika 1bc = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/c.png")
image monika 1bd = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/d.png")
image monika 1be = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/e.png")
image monika 1bf = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/f.png")
image monika 1bg = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/g.png")
image monika 1bh = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/h.png")
image monika 1bi = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/i.png")
image monika 1bj = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/j.png")
image monika 1bk = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/k.png")
image monika 1bl = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/l.png")
image monika 1bm = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/m.png")
image monika 1bn = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/n.png")
image monika 1bo = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/o.png")
image monika 1bp = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/p.png")
image monika 1bq = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/q.png")
image monika 1br = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/r.png")

image monika 3ba = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/a.png")
image monika 3bb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/b.png")
image monika 3bc = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/c.png")
image monika 3bd = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/d.png")
image monika 3be = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/e.png")
image monika 3bf = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/f.png")
image monika 3bg = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/g.png")
image monika 3bh = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/h.png")
image monika 3bi = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/i.png")
image monika 3bj = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/j.png")
image monika 3bk = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/k.png")
image monika 3bl = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/l.png")
image monika 3bm = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/m.png")
image monika 3bn = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/n.png")
image monika 3bo = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/o.png")
image monika 3bp = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/p.png")
image monika 3bq = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/q.png")
image monika 3br = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "monika/r.png")

image monika 2ba = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/a.png")
image monika 2bb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/b.png")
image monika 2bc = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/c.png")
image monika 2bd = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/d.png")
image monika 2be = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/e.png")
image monika 2bf = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/f.png")
image monika 2bg = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/g.png")
image monika 2bh = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/h.png")
image monika 2bi = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/i.png")
image monika 2bj = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/j.png")
image monika 2bk = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/k.png")
image monika 2bl = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/l.png")
image monika 2bm = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/m.png")
image monika 2bn = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/n.png")
image monika 2bo = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/o.png")
image monika 2bp = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/p.png")
image monika 2bq = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/q.png")
image monika 2br = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/r.png")

image monika 4ba = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/a.png")
image monika 4bb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/b.png")
image monika 4bc = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/c.png")
image monika 4bd = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/d.png")
image monika 4be = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/e.png")
image monika 4bf = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/f.png")
image monika 4bg = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/g.png")
image monika 4bh = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/h.png")
image monika 4bi = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/i.png")
image monika 4bj = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/j.png")
image monika 4bk = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/k.png")
image monika 4bl = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/l.png")
image monika 4bm = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/m.png")
image monika 4bn = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/n.png")
image monika 4bo = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/o.png")
image monika 4bp = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/p.png")
image monika 4bq = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/q.png")
image monika 4br = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "monika/r.png")

image monika 1bmb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/mb.png")
image monika 2bmb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/mb.png")
image monika 3bmb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/mb.png")
image monika 4bmb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/mb.png")

image monika 1bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/nb.png")
image monika 2bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_1l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/nb.png")
image monika 3bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_1r.png", (0, 0), "mod_assets/nb.png")
image monika 4bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/nb.png")

# Monika Summer Dress ====================================================================================================================

image monika 1ca = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/a.png")
image monika 1cb = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/b.png")
image monika 1cc = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/c.png")
image monika 1cd = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/d.png")
image monika 1ce = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/e.png")
image monika 1cf = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/f.png")
image monika 1cg = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/g.png")
image monika 1ch = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/h.png")
image monika 1ci = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/i.png")
image monika 1cj = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/j.png")
image monika 1ck = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/k.png")
image monika 1cl = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/l.png")
image monika 1cm = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/m.png")
image monika 1cn = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/n.png")
image monika 1co = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/o.png")
image monika 1cp = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/p.png")
image monika 1cq = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/q.png")
image monika 1cr = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/r.png")

image monika 3ca = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/a.png")
image monika 3cb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/b.png")
image monika 3cc = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/c.png")
image monika 3cd = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/d.png")
image monika 3ce = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/e.png")
image monika 3cf = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/f.png")
image monika 3cg = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/g.png")
image monika 3ch = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/h.png")
image monika 3ci = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/i.png")
image monika 3cj = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/j.png")
image monika 3ck = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/k.png")
image monika 3cl = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/l.png")
image monika 3cm = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/m.png")
image monika 3cn = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/n.png")
image monika 3co = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/o.png")
image monika 3cp = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/p.png")
image monika 3cq = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/q.png")
image monika 3cr = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "monika/r.png")

image monika 2ca = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/a.png")
image monika 2cb = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/b.png")
image monika 2cc = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/c.png")
image monika 2cd = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/d.png")
image monika 2ce = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/e.png")
image monika 2cf = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/f.png")
image monika 2cg = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/g.png")
image monika 2ch = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/h.png")
image monika 2ci = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/i.png")
image monika 2cj = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/j.png")
image monika 2ck = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/k.png")
image monika 2cl = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/l.png")
image monika 2cm = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/m.png")
image monika 2cn = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/n.png")
image monika 2co = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/o.png")
image monika 2cp = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/p.png")
image monika 2cq = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/q.png")
image monika 2cr = im.Composite((960, 960), (0, 0), "mod_assets/1cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/r.png")

image monika 4ca = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/a.png")
image monika 4cb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/b.png")
image monika 4cc = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/c.png")
image monika 4cd = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/d.png")
image monika 4ce = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/e.png")
image monika 4cf = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/f.png")
image monika 4cg = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/g.png")
image monika 4ch = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/h.png")
image monika 4ci = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/i.png")
image monika 4cj = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/j.png")
image monika 4ck = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/k.png")
image monika 4cl = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/l.png")
image monika 4cm = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/m.png")
image monika 4cn = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/n.png")
image monika 4co = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/o.png")
image monika 4cp = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/p.png")
image monika 4cq = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/q.png")
image monika 4cr = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "monika/r.png")

image monika 5ca = im.Composite((960, 960), (0, 0), "mod_assets/3a.png")
image monika 5cb = im.Composite((960, 960), (0, 0), "mod_assets/3b.png")

image monika 1cdb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/db.png")
image monika 2cdb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/db.png")
image monika 3cdb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/db.png")
image monika 4cdb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/db.png")

image monika 1ceb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/eb.png")
image monika 2ceb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/eb.png")
image monika 3ceb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/eb.png")
image monika 4ceb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/eb.png")

image monika 1cl2 = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/l2.png")
image monika 2cl2 = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/l2.png")
image monika 3cl2 = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/l2.png")
image monika 4cl2 = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/l2.png")

image monika 1cmb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/mb.png")
image monika 2cmb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/mb.png")
image monika 3cmb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/mb.png")
image monika 4cmb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/mb.png")

image monika 1cnb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/nb.png")
image monika 2cnb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/nb.png")
image monika 3cnb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/nb.png")
image monika 4cnb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/nb.png")

image monika 1cob = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/ob.png")
image monika 2cob = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/ob.png")
image monika 3cob = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/ob.png")
image monika 4cob = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/ob.png")

image monika 1cos = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/os.png")
image monika 2cos = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/os.png")
image monika 3cos = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/os.png")
image monika 4cos = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/os.png")

image monika 1cpb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/pb.png")
image monika 2cpb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/pb.png")
image monika 3cpb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/pb.png")
image monika 4cpb = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/pb.png")

image monika 1cq2 = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/q2.png")
image monika 2cq2 = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/q2.png")
image monika 3cq2 = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/q2.png")
image monika 4cq2 = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/q2.png")

image monika 1cqs = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/qs.png")
image monika 2cqs = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/qs.png")
image monika 3cqs = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/qs.png")
image monika 4cqs = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/qs.png")

image monika 1cob = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/ob.png")
image monika 2cob = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/ob.png")
image monika 3cob = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/1cr.png", (0, 0), "mod_assets/ob.png")
image monika 4cob = im.Composite((960, 960), (0, 0), "mod_assets/2cl.png", (0, 0), "mod_assets/2cr.png", (0, 0), "mod_assets/ob.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define h = DynamicCharacter('h_name', image='haruna', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Нац и Юри', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define sy = Character('Сай и Юри', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define sm = Character('Сай и Мони', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mn = Character('Мони и Нац', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mny = Character('Мон, Нац и Юри', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mcs = Character('Я и Сайори', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ns = Character('Сай и Нац', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

###### Persistent Variables ######
# These values are automatically loaded/saved on game start and exit.
# These exist across all saves

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None

###### Other global variables ######
# It's good practice to define global variables here, just so you know what you can call later

default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

#default allow_choice = False #==================================================================================================================

default s_name = "Сайори"
default m_name = "Моника"
default n_name = "Нацуки"
default y_name = "Юри"
default k_name = "Киба"
default r_name = "Рикка"

# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]
default k_poemappeal = [0, 0, 0]
default r_poemappeal = [0, 0, 0]
default d_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False
default k_readpoem = False
default r_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# Kiba's Sprite
define k = DynamicCharacter('k_name', image='kiba', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# image monika 4bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/nb.png")
image kiba 1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image kiba 1a = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image kiba 1b = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/b.png")
image kiba 1c = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/c.png")
image kiba 1d = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d.png")
image kiba 1d2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d2.png")
image kiba 1e = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/e.png")
image kiba 1f = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/f.png")
image kiba 1h = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/h.png")
image kiba 1i = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i.png")
image kiba 1i2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i2.png")
image kiba 1i3 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i3.png")
image kiba 1k = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/k.png")
image kiba 1l = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/l.png")
image kiba 1m = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/m.png")
image kiba 1n = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/n.png")
image kiba 1o = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/o.png")
image kiba 1p = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p.png")
image kiba 1p2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p2.png")
image kiba 1q = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/q.png")
image kiba 1r = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/r.png")
image kiba 1s = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/s.png")
image kiba 1t = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/t.png")
image kiba 1u = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/u.png")
image kiba 1v = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/v.png")
image kiba 1w = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/w.png")
image kiba 1x = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/x.png")
image kiba 1y = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/y.png")
image kiba 1z = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/z.png")

image kiba 1ba = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/a.png")
image kiba 1bb = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/b.png")
image kiba 1bc = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/c.png")
image kiba 1bd = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/d.png")
image kiba 1bd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/d2.png")
image kiba 1be = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/e.png")
image kiba 1bf = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/f.png")
image kiba 1bh = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/h.png")
image kiba 1bi = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/i.png")
image kiba 1bk = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/k.png")
image kiba 1bl = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/l.png")
image kiba 1bm = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/m.png")
image kiba 1bn = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/n.png")
image kiba 1bo = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/o.png")
image kiba 1bp = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/p.png")
image kiba 1bp2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/p2.png")
image kiba 1bq = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/q.png")
image kiba 1br = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/r.png")
image kiba 1bs = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/s.png")
image kiba 1bt = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/t.png")
image kiba 1bu = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/u.png")
image kiba 1bv = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/v.png")
image kiba 1bw = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/w.png")
image kiba 1bx = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/x.png")
image kiba 1by = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/y.png")
image kiba 1bz = im.Composite((960, 960), (0, 0), "mod_assets/mc/1bl.png", (0, 0), "mod_assets/mc/1br.png", (0, 0), "mod_assets/mc/z.png")

image kiba 2a = im.Composite((960, 960), (0, 0), "mod_assets/mc/2a.png")
image kiba 2a2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2a2.png")
image kiba 2b = im.Composite((960, 960), (0, 0), "mod_assets/mc/2b.png")
image kiba 2ba = im.Composite((960, 960), (0, 0), "mod_assets/mc/2ba.png")
image kiba 2ba2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2ba2.png")
image kiba 2bb = im.Composite((960, 960), (0, 0), "mod_assets/mc/2bb.png")
image kiba 5a = im.Composite((960, 960), (0, 0), "mod_assets/mc/5a.png")
image kiba 5b = im.Composite((960, 960), (0, 0), "mod_assets/mc/5b.png")
image kiba sill1 = im.Composite((960, 960), (0, 0), "mod_assets/sill1.png")
image kiba sill1a = im.Composite((960, 960), (0, 0), "mod_assets/sill1a.png")
image kiba sill1b = im.Composite((960, 960), (0, 0), "mod_assets/sill1b.png")
image kiba sill1c = im.Composite((960, 960), (0, 0), "mod_assets/sill1c.png")
image kiba sill2 = im.Composite((960, 960), (0, 0), "mod_assets/sill2.png")
image kiba sill3 = im.Composite((960, 960), (0, 0), "mod_assets/sill3.png")

image kiba 3a = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/a.png")
image kiba 3b = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/b.png")
image kiba 3c = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/c.png")
image kiba 3d = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/d.png")
image kiba 3d2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/d2.png")
image kiba 3e = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/e.png")
image kiba 3f = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/f.png")
image kiba 3g = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/g.png")
image kiba 3h = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/h.png")
image kiba 3i = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/i.png")
image kiba 3j = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/j.png")
image kiba 3k = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/k.png")
image kiba 3l = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/l.png")
image kiba 3m = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/m.png")
image kiba 3n = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/n.png")
image kiba 3o = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/o.png")
image kiba 3p = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/p.png")
image kiba 3q = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/q.png")
image kiba 3r = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/r.png")
image kiba 3s = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/s.png")
image kiba 3t = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/t.png")
image kiba 3u = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/u.png")
image kiba 3v = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/v.png")
image kiba 3w = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/w.png")
image kiba 3x = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/x.png")
image kiba 3y = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/y.png")
image kiba 3z = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/z.png")

image kiba 4a = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/a.png")
image kiba 4b = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/b.png")
image kiba 4c = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/c.png")
image kiba 4d = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/d.png")
image kiba 4d2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/d2.png")
image kiba 4e = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/e.png")
image kiba 4f = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/f.png")
image kiba 4g = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/g.png")
image kiba 4h = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/h.png")
image kiba 4i = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/i.png")
image kiba 4j = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/j.png")
image kiba 4k = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/k.png")
image kiba 4l = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/l.png")
image kiba 4m = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/m.png")
image kiba 4n = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/n.png")
image kiba 4o = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/o.png")
image kiba 4p = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/p.png")
image kiba 4q = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/q.png")
image kiba 4r = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/r.png")
image kiba 4s = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/s.png")
image kiba 4t = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/t.png")
image kiba 4u = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/u.png")
image kiba 4v = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/v.png")
image kiba 4w = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/w.png")
image kiba 4x = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/x.png")
image kiba 4y = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/y.png")
image kiba 4z = im.Composite((960, 960), (0, 0), "mod_assets/mc/4.png", (0, 0), "mod_assets/mc/z.png")


#Rikka's Sprite
define r = DynamicCharacter('r_name', image='rikka', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# image monika 4bnb = im.Composite((960, 960), (0, 0), "mod_assets/h1_2l.png", (0, 0), "mod_assets/h1_2r.png", (0, 0), "mod_assets/nb.png")
image rikka 1a = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/a.png")
image rikka 1b = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/b.png")
image rikka 1c = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/c.png")
image rikka 1d = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/d.png")
image rikka 1e = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/e.png")
image rikka 1f = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/f.png")
image rikka 1h = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/h.png")
image rikka 1i = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/i.png")
image rikka 1j = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/j.png")
image rikka 1k = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/k.png")
image rikka 1l = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/l.png")
image rikka 1m = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/m.png")
image rikka 1n = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/n.png")
image rikka 1o = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/o.png")
image rikka 1p = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/p.png")
image rikka 1q = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/q.png")
image rikka 1r = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/r.png")
image rikka 1s = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/s.png")
image rikka 1t = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/t.png")
image rikka 1u = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/u.png")
image rikka 1v = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/v.png")
image rikka 1w = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/w.png")
image rikka 1x = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/x.png")
image rikka 1y = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/y.png")
image rikka 1z = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/z.png")

image rikka 2a = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/a.png")
image rikka 2b = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/b.png")
image rikka 2c = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/c.png")
image rikka 2d = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/d.png")
image rikka 2e = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/e.png")
image rikka 2f = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/f.png")
image rikka 2h = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/h.png")
image rikka 2i = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/i.png")
image rikka 2j = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/j.png")
image rikka 2k = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/k.png")
image rikka 2l = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/l.png")
image rikka 2m = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/m.png")
image rikka 2n = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/n.png")
image rikka 2o = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/o.png")
image rikka 2p = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/p.png")
image rikka 2q = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/q.png")
image rikka 2r = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/r.png")
image rikka 2s = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/s.png")
image rikka 2t = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/t.png")
image rikka 2u = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/u.png")
image rikka 2v = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/v.png")
image rikka 2w = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/w.png")
image rikka 2x = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/x.png")
image rikka 2y = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/y.png")
image rikka 2z = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/z.png")

image rikka 3a = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/a.png")
image rikka 3b = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/b.png")
image rikka 3c = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/c.png")
image rikka 3d = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/d.png")
image rikka 3e = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/e.png")
image rikka 3f = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/f.png")
image rikka 3h = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/h.png")
image rikka 3i = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/i.png")
image rikka 3j = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/j.png")
image rikka 3k = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/k.png")
image rikka 3l = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/l.png")
image rikka 3m = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/m.png")
image rikka 3n = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/n.png")
image rikka 3o = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/o.png")
image rikka 3p = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/p.png")
image rikka 3q = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/q.png")
image rikka 3r = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/r.png")
image rikka 3s = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/s.png")
image rikka 3t = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/t.png")
image rikka 3u = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/u.png")
image rikka 3v = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/v.png")
image rikka 3w = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/w.png")
image rikka 3x = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/x.png")
image rikka 3y = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/y.png")
image rikka 3z = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/z.png")

image rikka 4a = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/a.png")
image rikka 4b = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/b.png")
image rikka 4c = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/c.png")
image rikka 4d = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/d.png")
image rikka 4e = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/e.png")
image rikka 4f = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/f.png")
image rikka 4h = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/h.png")
image rikka 4i = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/i.png")
image rikka 4j = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/j.png")
image rikka 4k = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/k.png")
image rikka 4l = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/l.png")
image rikka 4m = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/m.png")
image rikka 4n = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/n.png")
image rikka 4o = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/o.png")
image rikka 4p = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/p.png")
image rikka 4q = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/q.png")
image rikka 4r = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/r.png")
image rikka 4s = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/s.png")
image rikka 4t = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/t.png")
image rikka 4u = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/u.png")
image rikka 4v = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/v.png")
image rikka 4w = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/w.png")
image rikka 4x = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/x.png")
image rikka 4y = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/y.png")
image rikka 4z = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/z.png")

image rikka 5a = im.Composite((960, 960), (0, 0), "mod_assets/mc2/a.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5b = im.Composite((960, 960), (0, 0), "mod_assets/mc2/b.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5c = im.Composite((960, 960), (0, 0), "mod_assets/mc2/c.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5d = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5e = im.Composite((960, 960), (0, 0), "mod_assets/mc2/e.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5f = im.Composite((960, 960), (0, 0), "mod_assets/mc2/f.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5g = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5h = im.Composite((960, 960), (0, 0), "mod_assets/mc2/h.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5i = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5j = im.Composite((960, 960), (0, 0), "mod_assets/mc2/j.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5k = im.Composite((960, 960), (0, 0), "mod_assets/mc2/k.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5l = im.Composite((960, 960), (0, 0), "mod_assets/mc2/l.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5m = im.Composite((960, 960), (0, 0), "mod_assets/mc2/m.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5n = im.Composite((960, 960), (0, 0), "mod_assets/mc2/n.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5o = im.Composite((960, 960), (0, 0), "mod_assets/mc2/o.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5p = im.Composite((960, 960), (0, 0), "mod_assets/mc2/p.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5q = im.Composite((960, 960), (0, 0), "mod_assets/mc2/q.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5r = im.Composite((960, 960), (0, 0), "mod_assets/mc2/r.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5s = im.Composite((960, 960), (0, 0), "mod_assets/mc2/s.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5t = im.Composite((960, 960), (0, 0), "mod_assets/mc2/t.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5u = im.Composite((960, 960), (0, 0), "mod_assets/mc2/u.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5v = im.Composite((960, 960), (0, 0), "mod_assets/mc2/v.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5w = im.Composite((960, 960), (0, 0), "mod_assets/mc2/w.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5x = im.Composite((960, 960), (0, 0), "mod_assets/mc2/x.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5y = im.Composite((960, 960), (0, 0), "mod_assets/mc2/y.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 5z = im.Composite((960, 960), (0, 0), "mod_assets/mc2/z.png", (0, 0), "mod_assets/mc2/5.png")

image rikka 1ba = im.Composite((960, 960), (0, 0), "mod_assets/mc2/a.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bb = im.Composite((960, 960), (0, 0), "mod_assets/mc2/b.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bc = im.Composite((960, 960), (0, 0), "mod_assets/mc2/c.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bd = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1be = im.Composite((960, 960), (0, 0), "mod_assets/mc2/e.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bf = im.Composite((960, 960), (0, 0), "mod_assets/mc2/f.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bh = im.Composite((960, 960), (0, 0), "mod_assets/mc2/h.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bi = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bj = im.Composite((960, 960), (0, 0), "mod_assets/mc2/j.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bk = im.Composite((960, 960), (0, 0), "mod_assets/mc2/k.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bl = im.Composite((960, 960), (0, 0), "mod_assets/mc2/l.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bm = im.Composite((960, 960), (0, 0), "mod_assets/mc2/m.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bn = im.Composite((960, 960), (0, 0), "mod_assets/mc2/n.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bo = im.Composite((960, 960), (0, 0), "mod_assets/mc2/o.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bp = im.Composite((960, 960), (0, 0), "mod_assets/mc2/p.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bq = im.Composite((960, 960), (0, 0), "mod_assets/mc2/q.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1br = im.Composite((960, 960), (0, 0), "mod_assets/mc2/r.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bs = im.Composite((960, 960), (0, 0), "mod_assets/mc2/s.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bt = im.Composite((960, 960), (0, 0), "mod_assets/mc2/t.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bu = im.Composite((960, 960), (0, 0), "mod_assets/mc2/u.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bv = im.Composite((960, 960), (0, 0), "mod_assets/mc2/v.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bw = im.Composite((960, 960), (0, 0), "mod_assets/mc2/w.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bx = im.Composite((960, 960), (0, 0), "mod_assets/mc2/x.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1by = im.Composite((960, 960), (0, 0), "mod_assets/mc2/y.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 1bz = im.Composite((960, 960), (0, 0), "mod_assets/mc2/z.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png")

image rikka 3ba = im.Composite((960, 960), (0, 0), "mod_assets/mc2/a.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bb = im.Composite((960, 960), (0, 0), "mod_assets/mc2/b.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bc = im.Composite((960, 960), (0, 0), "mod_assets/mc2/c.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bd = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3be = im.Composite((960, 960), (0, 0), "mod_assets/mc2/e.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bf = im.Composite((960, 960), (0, 0), "mod_assets/mc2/f.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bh = im.Composite((960, 960), (0, 0), "mod_assets/mc2/h.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bi = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bj = im.Composite((960, 960), (0, 0), "mod_assets/mc2/j.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bk = im.Composite((960, 960), (0, 0), "mod_assets/mc2/k.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bl = im.Composite((960, 960), (0, 0), "mod_assets/mc2/l.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bm = im.Composite((960, 960), (0, 0), "mod_assets/mc2/m.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bn = im.Composite((960, 960), (0, 0), "mod_assets/mc2/n.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bo = im.Composite((960, 960), (0, 0), "mod_assets/mc2/o.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bp = im.Composite((960, 960), (0, 0), "mod_assets/mc2/p.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bq = im.Composite((960, 960), (0, 0), "mod_assets/mc2/q.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3br = im.Composite((960, 960), (0, 0), "mod_assets/mc2/r.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bs = im.Composite((960, 960), (0, 0), "mod_assets/mc2/s.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bt = im.Composite((960, 960), (0, 0), "mod_assets/mc2/t.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bu = im.Composite((960, 960), (0, 0), "mod_assets/mc2/u.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bv = im.Composite((960, 960), (0, 0), "mod_assets/mc2/v.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bw = im.Composite((960, 960), (0, 0), "mod_assets/mc2/w.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bx = im.Composite((960, 960), (0, 0), "mod_assets/mc2/x.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3by = im.Composite((960, 960), (0, 0), "mod_assets/mc2/y.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")
image rikka 3bz = im.Composite((960, 960), (0, 0), "mod_assets/mc2/z.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png")

image rikka 2ba = im.Composite((960, 960), (0, 0), "mod_assets/mc2/a.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bb = im.Composite((960, 960), (0, 0), "mod_assets/mc2/b.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bc = im.Composite((960, 960), (0, 0), "mod_assets/mc2/c.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bd = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2be = im.Composite((960, 960), (0, 0), "mod_assets/mc2/e.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bf = im.Composite((960, 960), (0, 0), "mod_assets/mc2/f.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bh = im.Composite((960, 960), (0, 0), "mod_assets/mc2/h.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bi = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bj = im.Composite((960, 960), (0, 0), "mod_assets/mc2/j.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bk = im.Composite((960, 960), (0, 0), "mod_assets/mc2/k.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bl = im.Composite((960, 960), (0, 0), "mod_assets/mc2/l.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bm = im.Composite((960, 960), (0, 0), "mod_assets/mc2/m.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bn = im.Composite((960, 960), (0, 0), "mod_assets/mc2/n.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bo = im.Composite((960, 960), (0, 0), "mod_assets/mc2/o.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bp = im.Composite((960, 960), (0, 0), "mod_assets/mc2/p.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bq = im.Composite((960, 960), (0, 0), "mod_assets/mc2/q.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2br = im.Composite((960, 960), (0, 0), "mod_assets/mc2/r.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bs = im.Composite((960, 960), (0, 0), "mod_assets/mc2/s.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bt = im.Composite((960, 960), (0, 0), "mod_assets/mc2/t.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bu = im.Composite((960, 960), (0, 0), "mod_assets/mc2/u.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bv = im.Composite((960, 960), (0, 0), "mod_assets/mc2/v.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bw = im.Composite((960, 960), (0, 0), "mod_assets/mc2/w.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bx = im.Composite((960, 960), (0, 0), "mod_assets/mc2/x.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2by = im.Composite((960, 960), (0, 0), "mod_assets/mc2/y.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 2bz = im.Composite((960, 960), (0, 0), "mod_assets/mc2/z.png", (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png")

image rikka 4ba = im.Composite((960, 960), (0, 0), "mod_assets/mc2/a.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bb = im.Composite((960, 960), (0, 0), "mod_assets/mc2/b.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bc = im.Composite((960, 960), (0, 0), "mod_assets/mc2/c.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bd = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4be = im.Composite((960, 960), (0, 0), "mod_assets/mc2/e.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bf = im.Composite((960, 960), (0, 0), "mod_assets/mc2/f.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bh = im.Composite((960, 960), (0, 0), "mod_assets/mc2/h.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bi = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bj = im.Composite((960, 960), (0, 0), "mod_assets/mc2/j.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bk = im.Composite((960, 960), (0, 0), "mod_assets/mc2/k.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bl = im.Composite((960, 960), (0, 0), "mod_assets/mc2/l.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bm = im.Composite((960, 960), (0, 0), "mod_assets/mc2/m.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bn = im.Composite((960, 960), (0, 0), "mod_assets/mc2/n.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bo = im.Composite((960, 960), (0, 0), "mod_assets/mc2/o.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bp = im.Composite((960, 960), (0, 0), "mod_assets/mc2/p.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bq = im.Composite((960, 960), (0, 0), "mod_assets/mc2/q.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4br = im.Composite((960, 960), (0, 0), "mod_assets/mc2/r.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bs = im.Composite((960, 960), (0, 0), "mod_assets/mc2/s.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bt = im.Composite((960, 960), (0, 0), "mod_assets/mc2/t.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bu = im.Composite((960, 960), (0, 0), "mod_assets/mc2/u.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bv = im.Composite((960, 960), (0, 0), "mod_assets/mc2/v.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bw = im.Composite((960, 960), (0, 0), "mod_assets/mc2/w.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bx = im.Composite((960, 960), (0, 0), "mod_assets/mc2/x.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4by = im.Composite((960, 960), (0, 0), "mod_assets/mc2/y.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")
image rikka 4bz = im.Composite((960, 960), (0, 0), "mod_assets/mc2/z.png", (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png")

image rikka 5ba = im.Composite((960, 960), (0, 0), "mod_assets/mc2/a.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bb = im.Composite((960, 960), (0, 0), "mod_assets/mc2/b.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bc = im.Composite((960, 960), (0, 0), "mod_assets/mc2/c.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bd = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5be = im.Composite((960, 960), (0, 0), "mod_assets/mc2/e.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bf = im.Composite((960, 960), (0, 0), "mod_assets/mc2/f.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bh = im.Composite((960, 960), (0, 0), "mod_assets/mc2/h.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bi = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bj = im.Composite((960, 960), (0, 0), "mod_assets/mc2/j.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bk = im.Composite((960, 960), (0, 0), "mod_assets/mc2/k.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bl = im.Composite((960, 960), (0, 0), "mod_assets/mc2/l.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bm = im.Composite((960, 960), (0, 0), "mod_assets/mc2/m.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bn = im.Composite((960, 960), (0, 0), "mod_assets/mc2/n.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bo = im.Composite((960, 960), (0, 0), "mod_assets/mc2/o.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bp = im.Composite((960, 960), (0, 0), "mod_assets/mc2/p.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bq = im.Composite((960, 960), (0, 0), "mod_assets/mc2/q.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5br = im.Composite((960, 960), (0, 0), "mod_assets/mc2/r.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bs = im.Composite((960, 960), (0, 0), "mod_assets/mc2/s.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bt = im.Composite((960, 960), (0, 0), "mod_assets/mc2/t.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bu = im.Composite((960, 960), (0, 0), "mod_assets/mc2/u.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bv = im.Composite((960, 960), (0, 0), "mod_assets/mc2/v.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bw = im.Composite((960, 960), (0, 0), "mod_assets/mc2/w.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bx = im.Composite((960, 960), (0, 0), "mod_assets/mc2/x.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5by = im.Composite((960, 960), (0, 0), "mod_assets/mc2/y.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 5bz = im.Composite((960, 960), (0, 0), "mod_assets/mc2/z.png", (0, 0), "mod_assets/mc2/5b.png")

image rikka 1ca = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/a.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cb = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/b.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cc = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/c.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cd = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/d.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1ce = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/e.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cf = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/f.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/g.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1ch = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/h.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1ci = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/i.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cj = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/j.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1ck = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/k.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cl = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/l.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cm = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/m.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cn = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/n.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1co = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/o.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cp = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/p.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cq = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/q.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cr = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/r.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cs = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/s.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1ct = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/t.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cu = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/u.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cv = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/v.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cw = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/w.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cx = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/x.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cy = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/y.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 1cz = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/z.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png")

image rikka 3ca = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/a.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cb = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/b.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cc = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/c.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cd = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/d.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3ce = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/e.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cf = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/f.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/g.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3ch = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/h.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3ci = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/i.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cj = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/j.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3ck = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/k.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cl = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/l.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cm = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/m.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cn = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/n.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3co = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/o.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cp = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/p.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cq = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/q.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cr = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/r.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cs = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/s.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3ct = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/t.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cu = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/u.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cv = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/v.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cw = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/w.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cx = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/x.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cy = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/y.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")
image rikka 3cz = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/z.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png")

image rikka 2ca = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/a.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cb = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/b.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cc = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/c.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cd = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/d.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2ce = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/e.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cf = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/f.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/g.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2ch = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/h.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2ci = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/i.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cj = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/j.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2ck = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/k.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cl = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/l.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cm = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/m.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cn = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/n.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2co = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/o.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cp = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/p.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cq = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/q.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cr = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/r.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cs = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/s.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2ct = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/t.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cu = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/u.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cv = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/v.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cw = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/w.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cx = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/x.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cy = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/y.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 2cz = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/z.png", (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png")

image rikka 4ca = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/a.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cb = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/b.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cc = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/c.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cd = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/d.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4ce = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/e.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cf = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/f.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/g.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4ch = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/h.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4ci = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/i.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cj = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/j.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4ck = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/k.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cl = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/l.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cm = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/m.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cn = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/n.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4co = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/o.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cp = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/p.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cq = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/q.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cr = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/r.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cs = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/s.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4ct = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/t.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cu = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/u.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cv = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/v.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cw = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/w.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cx = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/x.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cy = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/y.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")
image rikka 4cz = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/z.png", (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png")

image rikka 5ca = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/a.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cb = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/b.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cc = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/c.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cd = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/d.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5ce = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/e.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cf = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/f.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/g.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5ch = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/h.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5ci = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/i.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cj = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/j.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5ck = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/k.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cl = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/l.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cm = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/m.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cn = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/n.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5co = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/o.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cp = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/p.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cq = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/q.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cr = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/r.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cs = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/s.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5ct = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/t.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cu = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/u.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cv = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/v.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cw = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/w.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cx = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/x.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cy = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/y.png", (0, 0), "mod_assets/mc2c/5c.png")
image rikka 5cz = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/z.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1g = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/g.png")
image rikka 2g = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/g.png")
image rikka 3g = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/g.png")
image rikka 4g = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/g.png")

image rikka 1c2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/c2.png")
image rikka 2c2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/c2.png")
image rikka 3c2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/c2.png")
image rikka 4c2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/c2.png")
image rikka 5c2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/c2.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 1bc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/c2.png")
image rikka 2bc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/c2.png")
image rikka 3bc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/c2.png")
image rikka 4bc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/c2.png")
image rikka 5bc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/c2.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 1cc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/c2.png")
image rikka 2cc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/c2.png")
image rikka 3cc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/c2.png")
image rikka 4cc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/c2.png")
image rikka 5cc2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/c2.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1e2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/e2.png")
image rikka 2e2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/e2.png")
image rikka 3e2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/e2.png")
image rikka 4e2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/e2.png")
image rikka 5e2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/e2.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 1be2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/e2.png")
image rikka 2be2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/e2.png")
image rikka 3be2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/e2.png")
image rikka 4be2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/e2.png")
image rikka 5be2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/e2.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 1ce2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/e2.png")
image rikka 2ce2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/e2.png")
image rikka 3ce2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/e2.png")
image rikka 4ce2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/e2.png")
image rikka 5ce2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/e2.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1g2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/g2.png")
image rikka 2g2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/g2.png")
image rikka 3g2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/g2.png")
image rikka 4g2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/g2.png")
image rikka 5g2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g2.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 1bg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/g2.png")
image rikka 2bg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/g2.png")
image rikka 3bg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/g2.png")
image rikka 4bg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/g2.png")
image rikka 5bg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g2.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 1cg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/g2.png")
image rikka 2cg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/g2.png")
image rikka 3cg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/g2.png")
image rikka 4cg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/g2.png")
image rikka 5cg2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/g2.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1g3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/g3.png")
image rikka 2g3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/g3.png")
image rikka 3g3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/g3.png")
image rikka 4g3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/g3.png")
image rikka 5g3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g3.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 1bg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/g3.png")
image rikka 2bg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/g3.png")
image rikka 3bg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/g3.png")
image rikka 4bg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/g3.png")
image rikka 5bg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g3.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 1cg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/g3.png")
image rikka 2cg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/g3.png")
image rikka 3cg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/g3.png")
image rikka 4cg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/g3.png")
image rikka 5cg3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/g3.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1i2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/i2.png")
image rikka 2i2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/i2.png")
image rikka 3i2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/i2.png")
image rikka 4i2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/i2.png")
image rikka 5i2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i2.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 1bi2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/i2.png")
image rikka 2bi2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/i2.png")
image rikka 3bi2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/i2.png")
image rikka 4bi2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/i2.png")
image rikka 5bi2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i2.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 1ci2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/i2.png")
image rikka 2ci2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/i2.png")
image rikka 3ci2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/i2.png")
image rikka 4ci2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/i2.png")
image rikka 5ci2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/i2.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1i3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/i3.png")
image rikka 2i3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/i3.png")
image rikka 3i3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/i3.png")
image rikka 4i3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/i3.png")
image rikka 5i3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i3.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 1bi3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/i3.png")
image rikka 2bi3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/i3.png")
image rikka 3bi3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/i3.png")
image rikka 4bi3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/i3.png")
image rikka 5bi3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/i3.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 1ci3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/i3.png")
image rikka 2ci3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/i3.png")
image rikka 3ci3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/i3.png")
image rikka 4ci3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/i3.png")
image rikka 5ci3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/i3.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1d2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/d2.png")
image rikka 2d2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/d2.png")
image rikka 3d2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/d2.png")
image rikka 4d2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/d2.png")
image rikka 5d2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d2.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 1bd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/d2.png")
image rikka 2bd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/d2.png")
image rikka 3bd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/d2.png")
image rikka 4bd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/d2.png")
image rikka 5bd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d2.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 1cd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/d2.png")
image rikka 2cd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/d2.png")
image rikka 3cd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/d2.png")
image rikka 4cd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/d2.png")
image rikka 5cd2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/d2.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1d3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/d3.png")
image rikka 2d3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/d3.png")
image rikka 3d3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/d3.png")
image rikka 4d3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/d3.png")
image rikka 5d3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d3.png", (0, 0), "mod_assets/mc2/5.png")
image rikka 1bd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/d3.png")
image rikka 2bd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/d3.png")
image rikka 3bd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/d3.png")
image rikka 4bd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/d3.png")
image rikka 5bd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/d3.png", (0, 0), "mod_assets/mc2/5b.png")
image rikka 1cd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/d3.png")
image rikka 2cd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/d3.png")
image rikka 3cd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/d3.png")
image rikka 4cd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/d3.png")
image rikka 5cd3 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/d3.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1l2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/l2.png")
image rikka 2l2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/l2.png")
image rikka 3l2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/l2.png")
image rikka 4l2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/l2.png")
image rikka 5l2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/l2.png", (0, 0), "mod_assets/mc2/5.png")

image rikka 1z2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/z2.png")
image rikka 2z2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/z2.png")
image rikka 3z2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/1r.png", (0, 0), "mod_assets/mc2/z2.png")
image rikka 4z2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2l.png", (0, 0), "mod_assets/mc2/2r.png", (0, 0), "mod_assets/mc2/z2.png")
image rikka 5z2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/z2.png", (0, 0), "mod_assets/mc2/5.png")

image rikka 1bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/g.png")
image rikka 2bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/g.png")
image rikka 3bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/g.png")
image rikka 4bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/g.png")
image rikka 5bg = im.Composite((960, 960), (0, 0), "mod_assets/mc2/g.png", (0, 0), "mod_assets/mc2/5b.png")

image rikka 1bl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/l2.png")
image rikka 2bl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/l2.png")
image rikka 3bl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/l2.png")
image rikka 4bl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/l2.png")
image rikka 5bl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/l2.png", (0, 0), "mod_assets/mc2/5b.png")

image rikka 1bz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/z2.png")
image rikka 2bz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/1bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/z2.png")
image rikka 3bz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/1br.png", (0, 0), "mod_assets/mc2/z2.png")
image rikka 4bz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/2bl.png", (0, 0), "mod_assets/mc2/2br.png", (0, 0), "mod_assets/mc2/z2.png")
image rikka 5bz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2/z2.png", (0, 0), "mod_assets/mc2/5b.png")

image rikka 1cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/g.png")
image rikka 2cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/g.png")
image rikka 3cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/g.png")
image rikka 4cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/g.png")
image rikka 5cg = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/g.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1cl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/l2.png")
image rikka 2cl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/l2.png")
image rikka 3cl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/l2.png")
image rikka 4cl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/l2.png")
image rikka 5cl2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/l2.png", (0, 0), "mod_assets/mc2c/5c.png")

image rikka 1cz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/z2.png")
image rikka 2cz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/1cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/z2.png")
image rikka 3cz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/1cr.png", (0, 0), "mod_assets/mc2c/z2.png")
image rikka 4cz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/2cl.png", (0, 0), "mod_assets/mc2c/2cr.png", (0, 0), "mod_assets/mc2c/z2.png")
image rikka 5cz2 = im.Composite((960, 960), (0, 0), "mod_assets/mc2c/z2.png", (0, 0), "mod_assets/mc2c/5c.png")

#Haruna ==================================================================================================================================
image haruna 1b = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png")
image haruna 2b = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png")
image haruna 3b = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png")

image haruna 1ba = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/a.png")
image haruna 1bb = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/b.png",)
image haruna 1bc = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/c.png",)
image haruna 1bd = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/d.png",)
image haruna 1be = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/e.png",)
image haruna 1bf = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/f.png",)
image haruna 1bg = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/g.png",)
image haruna 1bh = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/h.png",)
image haruna 1bi = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/i.png",)
image haruna 1bj = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/j.png",)
image haruna 1bk = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/k.png",)
image haruna 1bl = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/l.png",)
image haruna 1bm = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/m.png",)
image haruna 1bn = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/n.png",)
image haruna 1bo = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/o.png",)
image haruna 1bp = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/p.png",)
image haruna 1bq = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/q.png",)
image haruna 1br = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/r.png",)
image haruna 1bs = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/s.png",)
image haruna 1bt = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/t.png",)
image haruna 1bu = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/u.png",)
image haruna 1bv = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/v.png",)
image haruna 1bw = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/w.png",)
image haruna 1bx = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/x.png",)
image haruna 1by = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/y.png",)
image haruna 1bz = im.Composite((960, 960), (0, 0), "mod_assets/haru/1b.png", (0, 0), "mod_assets/haru/z.png",)

image haruna 2ba = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/a.png",)
image haruna 2bb = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/b.png",)
image haruna 2bc = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/c.png",)
image haruna 2bd = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/d.png",)
image haruna 2be = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/e.png",)
image haruna 2bf = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/f.png",)
image haruna 2bg = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/g.png",)
image haruna 2bh = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/h.png",)
image haruna 2bi = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/i.png",)
image haruna 2bj = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/j.png",)
image haruna 2bk = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/k.png",)
image haruna 2bl = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/l.png",)
image haruna 2bm = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/m.png",)
image haruna 2bn = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/n.png",)
image haruna 2bo = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/o.png",)
image haruna 2bp = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/p.png",)
image haruna 2bq = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/q.png",)
image haruna 2br = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/r.png",)
image haruna 2bs = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/s.png",)
image haruna 2bt = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/t.png",)
image haruna 2bu = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/u.png",)
image haruna 2bv = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/v.png",)
image haruna 2bw = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/w.png",)
image haruna 2bx = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/x.png",)
image haruna 2by = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/y.png",)
image haruna 2bz = im.Composite((960, 960), (0, 0), "mod_assets/haru/2b.png", (0, 0), "mod_assets/haru/z.png",)

image haruna 3ba = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/a.png",)
image haruna 3bb = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/b.png",)
image haruna 3bc = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/c.png",)
image haruna 3bd = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/d.png",)
image haruna 3be = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/e.png",)
image haruna 3bf = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/f.png",)
image haruna 3bg = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/g.png",)
image haruna 3bh = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/h.png",)
image haruna 3bi = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/i.png",)
image haruna 3bj = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/j.png",)
image haruna 3bk = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/k.png",)
image haruna 3bl = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/l.png",)
image haruna 3bm = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/m.png",)
image haruna 3bn = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/n.png",)
image haruna 3bo = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/o.png",)
image haruna 3bp = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/p.png",)
image haruna 3bq = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/q.png",)
image haruna 3br = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/r.png",)
image haruna 3bs = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/s.png",)
image haruna 3bt = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/t.png",)
image haruna 3bu = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/u.png",)
image haruna 3bv = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/v.png",)
image haruna 3bw = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/w.png",)
image haruna 3bx = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/x.png",)
image haruna 3by = im.Composite((960, 960), (0, 0), "mod_assets/haru/3b.png", (0, 0), "mod_assets/haru/y.png",)

#
