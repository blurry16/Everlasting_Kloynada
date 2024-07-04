init:

    # Dev mode 
    $ config.developer = True # False

    # Custom Characters (Text)
    $ ml = Character (u'Мельник', color="#BBDEF0", what_color="E2C778")
    $ k4 = Character (u'Кулич', color="#95f542", what_color="E2C778")
    $ vs = Character (u'Вика', color="#bf42f5", what_color="E2C778")
    $ si = Character (u'Славик', color="#ef9e08", what_color="E2C778")
    $ dn = Character (u'Денис', color="#eb6734", what_color="E2C778")
    $ kl = Character (u'Кирилл', color="#3440eb", what_color="E2C778")
    $ ms = Character (u'Максим', color="#fc0307", what_color="E2C778")
    $ wj = Character (u'Вожатая', color="#00fd0d", what_color="E2C778")
    $ rm = Character (u'Рома', color="#E9D758", what_color="E2C778")
    $ ng = Character (u'Никита Г.', color="6DA9E4", what_color="E2C778")

    # Custom Images (p.s custom sprites probably will be in another comment)
    image discord = "mods/Everlasting_Kloynada/materials/images/discord1.jpg"
    image khata = "mods/Everlasting_Kloynada/materials/images/khata1.jpg"
    image vanna11 = "mods/Everlasting_Kloynada/materials/images/vanna11.jpg"
    image basgolova = "mods/Everlasting_Kloynada/materials/images/basgolova.jpg"
    image dota_opening = "mods/Everlasting_Kloynada/materials/images/dota2_opening.jpg"
    image dota_menu_sf = "mods/Everlasting_Kloynada/materials/images/dota_menu_sf.jpg"
    image dota_tournament_roshan = "mods/Everlasting_Kloynada/materials/images/dota_tournament_roshan.jpg"
    image basgolova_bw = "mods/Everlasting_Kloynada/materials/images/basgolova_4b_version.jpg"
    image dota_training ="mods/Everlasting_Kloynada/materials/images/dota_training.jpg"
    image busvk_not_good_weather = "mods/Everlasting_Kloynada/materials/images/bus_vk_bad_weather.jpg"
    image melnik_house_outside_day = "mods/Everlasting_Kloynada/materials/images/melnik_house_outside_day.jpg"
    image melnik_house_inside_day = "mods/Everlasting_Kloynada/materials/images/melnik_house_inside_day.jpg"
    image melnik_house_inside_night = "mods/Everlasting_Kloynada/materials/images/melnik_house_inside_night.jpg"
    image in_dinning_hall_sunset = "mods/Everlasting_Kloynada/materials/images/in_stolovaya_sunset.jpg"
    image ext_house_of_un_sunset = "mods/Everlasting_Kloynada/materials/images/ext_house_of_un_sunset.jpg"
    image int_melnik_house_without_light = "mods/Everlasting_Kloynada/materials/images/int_melnik_house_without_light.jpg"
    image me_on_a_bed_melnik = "mods/Everlasting_Kloynada/materials/images/me_on_a_bed_melnik.jpg"
    image ext_melnik_house_night = "mods/Everlasting_Kloynada/materials/images/ext_melnik_house_night.jpg"
    image bg ext_camp_entrance_sunset = "mods/Everlasting_Kloynada/materials/images/ext_camp_entrance_sunset.jpg"
    image bg int_clubs_sunset = "mods/Everlasting_Kloynada/materials/images/int_clubs_sunset.jpg"
    image bg ext_clubs_sunset = "mods/Everlasting_Kloynada/materials/images/ext_clubs_sunset.jpg"
    image cg psglgdhavelost = "mods/Everlasting_Kloynada/materials/images/PSGLGDhavelost.jpg"
    image cg psglgdhavelostbw = "mods/Everlasting_Kloynada/materials/images/PSGLGDhavelostBW.jpg"
    image bg ext_loot_room_day = "mods/Everlating_Kloynada/materials/images/ext_loot_room_day.jpg"

    $ NOTHING_PATH = "mods/Everlasting_Kloynada/nothing.png"

    # holy fuck
    image ml normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Everlasting_Kloynada/materials/sprites/ml_normal_pioneer.png',
        (0, 0), NOTHING_PATH), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Everlasting_Kloynada/materials/sprites/ml_normal_pioneer.png',
        (0, 0), NOTHING_PATH), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/Everlasting_Kloynada/materials/sprites/ml_normal_pioneer.png', (0, 0), NOTHING_PATH)
    )
    image ml normal pioneer su = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Everlasting_Kloynada/materials/sprites/ml_normal_pioneer_su.png',
        (0, 0), NOTHING_PATH), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Everlasting_Kloynada/materials/sprites/ml_normal_pioneer_su.png',
        (0, 0), NOTHING_PATH), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/Everlasting_Kloynada/materials/sprites/ml_normal_pioneer_su.png', (0, 0), NOTHING_PATH)
    )
    
    image k4 normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Everlasting_Kloynada/materials/sprites/k4_normal_pioneer.png',
        (0, 0), NOTHING_PATH), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/Everlasting_Kloynada/materials/sprites/k4_normal_pioneer.png',
        (0, 0), NOTHING_PATH), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/Everlasting_Kloynada/materials/sprites/k4_normal_pioneer.png', (0, 0), NOTHING_PATH)
    )
    
    # Custom Music
    $ lvvp = "mods/Everlasting_Kloynada/materials/music/neksyusha1.mp3"
    $ slava_song = "mods/Everlasting_Kloynada/materials/music/slavas_song.mp3"
     
    # Custom Sounds(loop sounds there are too)
    $ join_discord = "mods/Everlasting_Kloynada/materials/sounds/user_join_ds.mp3"
    $ disconnect_ds = "mods/Everlasting_Kloynada/materials/sounds/user_disconnect_ds.mp3"
    $ bumer_sound = "mods/Everlasting_Kloynada/materials/sounds/bumer_sound.mp3"
    $ slap_sound = "mods/Everlasting_Kloynada/materials/sounds/slap1.mp3"
    $ flashbang_sound = "mods/Everlasting_Kloynada/materials/sounds/flashbang.explode1.mp3"
    $ condition_sound = "mods/Everlasting_Kloynada/materials/sounds/condition_sound.mp3"
    $ condition_sound_on = "mods/Everlasting_Kloynada/materials/sounds/condition_sound_on.mp3"
    $ flag_sound = "mods/Everlasting_Kloynada/materials/sounds/flag_sfx.mp3"
    $ flag_sound_upped = "mods/Everlasting_Kloynada/materials/sounds/flag_sfx_upped.mp3"
    $ two_ball_kicks = "mods/Everlasting_Kloynada/materials/sounds/2_ball_kicks.mp3"
    $ four_ball_kicks = "mods/Everlasting_Kloynada/materials/sounds/4_ball_kicks.mp3"        
    $ five_ball_kicks = "mods/Everlasting_Kloynada/materials/sounds/5_ball_kicks.mp3"        
    
    # Scores
    $ si_score = 0
    $ ml_score = 0
    $ k4_score = 0
    $ vs_score = 0
    $ dn_score = 0
    $ kl_score = 0
    $ ms_score = 0
    $ rm_score = 0

init 0 python:
    from os import path

    MOD_ID = "kloynada_prolog_start"
    MOD_NAME = "Бесконечная Клоунада"
    COLOR_SPRITES = False # True

    mods[MOD_ID] = MOD_NAME

    for file in renpy.list_files():
        if MOD_ID in file:
            file_name = path.splitext(path.basename(file))[0]
            file_split = file.split("/")

            if file.endswith((".png", ".jpg")):
                if "sprites" in file_split:
                    renpy.image(
                        file_name,
                        ConditionSwitch(
                            "persistent.sprite_time == 'sunset'",
                            im.MatrixColor(
                                file,
                                im.matrix.tint(0.94, 0.82, 1.0)
                            ),
                            "persistent.sprite_time == 'night'",
                            im.MatrixColor(
                                file,
                                im.matrix.tint(0.63, 0.78, 0.82)
                            ),
                            True,
                            file
                        )
                    )
                else:
                    renpy.image(file_name, file)
            elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file

