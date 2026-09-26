# ============================================================
# DokiNameSwap UPDATE 1 - v4.2
# MAS 0.12.19 / Ren'Py 6.99.12.4.2187
#
# UPDATE:
# - Sayori crash -> Check sound / Wait restored
# - Sayori door scene
# - Door knock system
# - 5 knock limit
# - Sayori sad transition
# - Natsuki special sprite
# - Yuri / Natsuki / Sayori Easter eggs
# - Change My Name preserved
# - Monika hidden while Doki is active
# - Natsuki 5th-question dialogue is NORMAL TEXT
# ============================================================


# ============================================================
# IMAGES
# ============================================================

image dns_sayori_happy = im.Scale(
    "submods/DokiNameSwap_v1.0.0_FIXED/DokiNameSwap/images/sayoridesk_happy.png",
    1260,
    720
)

image dns_sayori_sad = im.Scale(
    "submods/DokiNameSwap_v1.0.0_FIXED/DokiNameSwap/images/sayoridesk_sad.png",
    1260,
    720
)

image dns_yuri = im.Scale(
    "submods/DokiNameSwap_v1.0.0_FIXED/DokiNameSwap/images/yuridesk.png",
    1260,
    720
)

image dns_natsuki = im.Scale(
    "submods/DokiNameSwap_v1.0.0_FIXED/DokiNameSwap/images/natsukidesk.png",
    1260,
    720
)

# CORRECT SPECIAL NATSUKI IMAGE
image dns_natsuki_special = im.Scale(
    "submods/DokiNameSwap_v1.0.0_FIXED/DokiNameSwap/images/natsukidesk-n.png",
    1260,
    720
)


# ============================================================
# SAYORI DOOR
# ============================================================

image dns_door = im.Scale(
    "mod_assets/door.png",
    1260,
    720
)


# ============================================================
# EASTER EGG IMAGES
# ============================================================

image dns_ee_sayori = im.Scale(
    "mod_assets/ee_sayori.png",
    1260,
    720
)

image dns_ee_yuri = im.Scale(
    "mod_assets/yuricreepy.png",
    1260,
    720
)

image dns_ee_natsuki = im.Scale(
    "mod_assets/natsukicreepy.png",
    1260,
    720
)


# ============================================================
# CHARACTERS
# ============================================================

define dns_s = Character("Sayori")
define dns_y = Character("Yuri")
define dns_n = Character("Natsuki")
define dns_p = Character("[persistent.playername]")


# ============================================================
# VARIABLES
# ============================================================

default dns_current_name = ""
default dns_name_input = ""

default dns_active_doki = ""
default dns_doki_visible = False

default dns_easter_egg_active = False
default dns_sayori_event_running = False

default dns_sayori_ee_done = False
default dns_yuri_ee_done = False
default dns_natsuki_ee_done = False

default dns_where_monika_count = 0
default dns_yuri_truth_count = 0
default dns_natsuki_read_count = 0

default dns_sayori_sad_visible = False
default dns_natsuki_special_visible = False
default dns_sayori_knock_count = 0


# ============================================================
# MONIKA SLIDE
# ============================================================

transform dns_monika_slide:

    xalign -0.8

    linear 1.0 xalign 0.5


# ============================================================
# KEEP MONIKA HIDDEN
# ============================================================

init python:

    def dns_keep_monika_hidden():

        if (
            store.dns_doki_visible
            or store.dns_easter_egg_active
            or store.dns_sayori_event_running
        ):

            try:
                renpy.hide("monika")
            except:
                pass


# ============================================================
# CHARACTER DISPLAY
# ============================================================

screen dns_character_display():

    if dns_doki_visible and dns_active_doki == "sayori":

        if dns_sayori_sad_visible:

            add "dns_sayori_sad"

        else:

            add "dns_sayori_happy"


    elif dns_doki_visible and dns_active_doki == "yuri":

        add "dns_yuri"


    elif dns_doki_visible and dns_active_doki == "natsuki":

        if dns_natsuki_special_visible:

            add "dns_natsuki_special"

        else:

            add "dns_natsuki"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

init python:

    def dns_get_player_name():

        try:
            return persistent.playername
        except:
            return ""


    def dns_hide_custom_sprites():

        try:
            renpy.hide("dns_sayori_happy")
        except:
            pass

        try:
            renpy.hide("dns_sayori_sad")
        except:
            pass

        try:
            renpy.hide("dns_yuri")
        except:
            pass

        try:
            renpy.hide("dns_natsuki")
        except:
            pass

        try:
            renpy.hide("dns_natsuki_special")
        except:
            pass


    def dns_reset_route_counters():

        store.dns_where_monika_count = 0
        store.dns_yuri_truth_count = 0
        store.dns_natsuki_read_count = 0


    def dns_reset_visual_states():

        store.dns_sayori_sad_visible = False
        store.dns_natsuki_special_visible = False
        store.dns_sayori_knock_count = 0


    def dns_reset_easter_egg_state():

        store.dns_easter_egg_active = False
        store.dns_sayori_event_running = False

        store.dns_sayori_ee_done = False
        store.dns_yuri_ee_done = False
        store.dns_natsuki_ee_done = False

        dns_reset_route_counters()
        dns_reset_visual_states()


    def dns_set_character_from_name(name):

        name = name.strip().lower()

        store.dns_current_name = name

        dns_reset_easter_egg_state()

        dns_hide_custom_sprites()


        if name == "sayori":

            store.dns_active_doki = "sayori"
            store.dns_doki_visible = True

            try:
                renpy.hide("monika")
            except:
                pass


        elif name == "yuri":

            store.dns_active_doki = "yuri"
            store.dns_doki_visible = True

            try:
                renpy.hide("monika")
            except:
                pass


        elif name == "natsuki":

            store.dns_active_doki = "natsuki"
            store.dns_doki_visible = True

            try:
                renpy.hide("monika")
            except:
                pass


        else:

            store.dns_active_doki = ""
            store.dns_doki_visible = False


        renpy.restart_interaction()


    def dns_finish_easter_egg():

        store.dns_doki_visible = False
        store.dns_easter_egg_active = False
        store.dns_sayori_event_running = False

        dns_hide_custom_sprites()

        try:
            renpy.show(
                "monika",
                at_list=[dns_monika_slide]
            )
        except:
            pass

        renpy.restart_interaction()


# ============================================================
# TALK FUNCTIONS
# ============================================================

init python:

    def dns_talk_sayori():

        dns_keep_monika_hidden()

        renpy.call("dns_sayori_talk")


    def dns_talk_yuri():

        dns_keep_monika_hidden()

        renpy.call("dns_yuri_talk")


    def dns_talk_natsuki():

        dns_keep_monika_hidden()

        renpy.call("dns_natsuki_talk")


    def dns_open_name_change():

        renpy.call("dns_change_name")


# ============================================================
# OVERLAY
# ============================================================

screen dns_name_swap_overlay():

    timer 0.20 repeat True action Function(
        dns_keep_monika_hidden
    )

    use dns_character_display


    if dns_active_doki == "sayori":

        if dns_doki_visible:

            if not dns_sayori_event_running:

                textbutton "Talk to Sayori":

                    xpos 0.76
                    ypos 0.82

                    action Function(dns_talk_sayori)


    if dns_active_doki == "yuri":

        if dns_doki_visible:

            if not dns_sayori_event_running:

                textbutton "Talk to Yuri":

                    xpos 0.76
                    ypos 0.82

                    action Function(dns_talk_yuri)


    if dns_active_doki == "natsuki":

        if dns_doki_visible:

            if not dns_sayori_event_running:

                textbutton "Talk to Natsuki":

                    xpos 0.76
                    ypos 0.82

                    action Function(dns_talk_natsuki)


    if not dns_sayori_event_running:

        textbutton "Change My Name":

            xpos 0.76
            ypos 0.90

            action Function(dns_open_name_change)


# ============================================================
# CHANGE NAME SCREEN
# ============================================================

screen dns_change_name_screen():

    modal True

    frame:

        xalign 0.5
        yalign 0.5

        vbox:

            spacing 15

            text "Change My Name"

            input:

                value VariableInputValue(
                    "dns_name_input"
                )

                length 30

                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_- "


            textbutton "Confirm":

                action [

                    Function(
                        lambda: dns_set_character_from_name(
                            dns_name_input
                        )
                    ),

                    Hide(
                        "dns_change_name_screen"
                    )

                ]


            textbutton "Cancel":

                action Hide(
                    "dns_change_name_screen"
                )


# ============================================================
# CHANGE NAME LABEL
# ============================================================

label dns_change_name:

    $ dns_name_input = dns_get_player_name()

    call screen dns_change_name_screen

    return


# ============================================================
# SAYORI TALK
# ============================================================

label dns_sayori_talk:

    $ dns_keep_monika_hidden()


    if dns_sayori_ee_done:
        return


    if dns_sayori_event_running:
        return


    dns_s "Hey! What do you wanna talk about?"


    menu:

        "Are you hurt?":

            dns_s "Hurt?"

            dns_s "No, I'm okay!"

            return


        "How are you feeling?":

            dns_s "I'm feeling pretty good!"

            dns_s "A little confused sometimes..."

            dns_s "But I'm okay."

            return


        "Do you miss the Literature Club?":

            dns_s "The Literature Club..."

            dns_s "Yeah."

            dns_s "I miss everyone."

            return


        "Do you remember everyone?":

            dns_s "Of course I do!"

            dns_s "Yuri..."

            dns_s "Natsuki..."

            dns_s "Monika..."

            dns_s "And you."

            return


        "What do you think of the room?":

            dns_s "It's nice!"

            dns_s "Although..."

            dns_s "Sometimes it feels a little too quiet."

            return


        "Do you want to talk about something else?":

            dns_s "Sure!"

            return


        "Are you hiding something?":

            dns_s "Hiding something?"

            dns_s "Me?"

            dns_s "Nooo..."

            return


        "Do you like being here?":

            dns_s "I do!"

            return


        "Can I ask you something?":

            dns_s "Of course!"

            return


        "Where's Monika?":

            $ dns_where_monika_count += 1


            if dns_where_monika_count == 1:

                dns_s "She's probably around somewhere!"

                return


            elif dns_where_monika_count == 2:

                dns_s "You really miss Monika, huh?"

                return


            elif dns_where_monika_count == 3:

                dns_s "You REALLY wanna know where she is..."

                return


            elif dns_where_monika_count == 4:

                dns_s "Okay..."

                dns_s "That's the fourth time."

                return


            else:

                $ dns_sayori_event_running = True
                $ dns_sayori_sad_visible = True

                dns_s "..."

                dns_s "I have to do something. Be right back!"


                $ dns_sayori_sad_visible = False
                $ dns_doki_visible = False
                $ dns_easter_egg_active = True


                pause 5.0


                play sound "mod_assets/crash.ogg"

                pause 8.0

                stop sound


                menu:

                    "Go check the sound":

                        call dns_sayori_door


                    "Wait":

                        dns_s "..."

                        dns_s "Maybe I should just keep waiting."

                        pause 10.0

                        dns_s "If you're not ready..."

                        dns_s "This button has been made just for you!"


                        $ dns_set_character_from_name(
                            dns_get_player_name()
                        )


                return


        "Never mind.":

            dns_s "Okay!"

            return


# ============================================================
# SAYORI DOOR
# ============================================================

label dns_sayori_door:

    $ dns_doki_visible = False
    $ dns_easter_egg_active = True
    $ dns_sayori_event_running = True

    $ dns_hide_custom_sprites()


    scene dns_door

    with None


    dns_p "I didn't remember a door being here?"


    $ dns_sayori_knock_count = 0


    jump dns_sayori_door_menu


label dns_sayori_door_menu:

    menu:

        "Open the door gently":

            jump dns_sayori_open_door


        "Knock" if dns_sayori_knock_count < 5:

            jump dns_sayori_knock


        "Wait":

            $ dns_set_character_from_name(
                dns_get_player_name()
            )

            return


# ============================================================
# DOOR KNOCK
# ============================================================

label dns_sayori_knock:

    $ dns_sayori_knock_count += 1


    play sound "mod_assets/knocking on wood.ogg"

    pause 3.0

    stop sound


    if dns_sayori_knock_count < 5:

        dns_p "..."


    else:

        dns_p "There's no answer."


    jump dns_sayori_door_menu


# ============================================================
# OPEN DOOR
# ============================================================

label dns_sayori_open_door:

    scene black

    with None

    pause 4.0


    show dns_ee_sayori

    with None

    pause 7.0


    hide dns_ee_sayori


    $ dns_sayori_ee_done = True
    $ dns_finish_easter_egg()


    pause 1.0


    m "Ahh.. Let's just ignore that. Anyways.. where was I?"


    return


# ============================================================
# YURI
# ============================================================

label dns_yuri_talk:

    $ dns_keep_monika_hidden()


    if dns_yuri_ee_done:
        return


    dns_y "Hello."


    menu:

        "How are you feeling?":

            dns_y "I'm doing alright."

            return


        "What are you reading?":

            dns_y "I've been reading a few different things."

            return


        "Do you still write poetry?":

            dns_y "Of course."

            return


        "Do you like tea?":

            dns_y "Very much."

            return


        "More questions...":

            menu:

                "Do you miss the Literature Club?":

                    dns_y "I do."

                    return


                "What's your favorite thing about reading?":

                    dns_y "Being able to completely disappear into another world."

                    return


                "Do you ever feel lonely here?":

                    dns_y "Sometimes."

                    return


                "What do you think about Monika?":

                    dns_y "Monika..."

                    dns_y "She's complicated."

                    return


                "Back.":

                    return


        "Tell me the truth.":

            $ dns_yuri_truth_count += 1


            if dns_yuri_truth_count < 5:

                dns_y "You really want to know?"

                return


            else:

                $ dns_sayori_event_running = True
                $ dns_easter_egg_active = True
                $ dns_doki_visible = False


                dns_y "You really want to see the truth?"


                menu:

                    "Just tell me it":

                        dns_y "..."

                        dns_y "Alright."

                        dns_y "You asked for it."


                        scene black

                        with None


                        play sound "mod_assets/yuri_horror.ogg" loop

                        pause 8.0

                        stop sound


                        show dns_ee_yuri

                        pause 7.0

                        hide dns_ee_yuri


                        $ dns_yuri_ee_done = True
                        $ dns_yuri_truth_count = 0


                        $ dns_finish_easter_egg()


                        pause 1.0


                        m "You weren't supposed to see that..."


                    "Nevermind":

                        dns_y "..."

                        dns_y "Thanks for not asking the truth."


                        $ dns_set_character_from_name(
                            dns_get_player_name()
                        )


                return


        "Never mind.":

            dns_y "That's alright."

            return


# ============================================================
# NATSUKI
# ============================================================

label dns_natsuki_talk:

    $ dns_keep_monika_hidden()


    if dns_natsuki_ee_done:
        return


    dns_n "What?"


    menu:

        "How are you feeling?":

            dns_n "I'm fine."

            return


        "Do you still like baking?":

            dns_n "Obviously!"

            return


        "What's your favorite dessert?":

            dns_n "Cupcakes."

            return


        "Do you still read manga?":

            dns_n "Yeah!"

            return


        "More questions...":

            menu:

                "Do you miss the Literature Club?":

                    dns_n "..."

                    dns_n "Maybe."

                    return


                "What's your favorite manga?":

                    dns_n "I'm not telling you!"

                    return


                "Do you like being here?":

                    dns_n "It's okay."

                    return


                "What do you think about Monika?":

                    dns_n "Monika?"

                    dns_n "She's... Monika."

                    return


                "Back.":

                    return


        # ====================================================
        # SPECIAL NATSUKI QUESTION
        # ====================================================

        "Why didn't you come to read with me.":

            $ dns_natsuki_read_count += 1


            if dns_natsuki_read_count == 1:

                dns_n "You keep asking me that?"

                return


            elif dns_natsuki_read_count == 2:

                dns_n "Seriously?"

                return


            elif dns_natsuki_read_count == 3:

                dns_n "You haven't forgotten, have you?"

                return


            elif dns_natsuki_read_count == 4:

                dns_n "One more time..."

                return


            else:

                # =================================================
                # SPECIAL NATSUKI SPRITE
                # =================================================

                $ dns_natsuki_special_visible = True
                $ dns_doki_visible = True

                $ dns_keep_monika_hidden()


                # =================================================
                # NORMAL NATSUKI TEXT
                # =================================================

                dns_n "BUT YOU DIDN'T COME READING WITH ME!"


                menu:

                    "No you didn't come reading with me!":

                        $ dns_sayori_event_running = True
                        $ dns_easter_egg_active = True
                        $ dns_doki_visible = False


                        dns_n "..."

                        dns_n "So that's how it is.."


                        scene black

                        with None


                        play sound "mod_assets/natsuki_crack.ogg" loop

                        pause 8.0

                        stop sound


                        show dns_ee_natsuki

                        pause 7.0

                        hide dns_ee_natsuki


                        $ dns_natsuki_ee_done = True
                        $ dns_natsuki_read_count = 0


                        $ dns_finish_easter_egg()


                        pause 1.0


                        m "Oh.. well she's gone now!"


                    "Fine i admit it i didn't come reading with you":

                        dns_n "..."

                        dns_n "Thanks for telling the truth."


                        # Restore normal pink Natsuki.
                        $ dns_natsuki_special_visible = False
                        $ dns_natsuki_read_count = 0
                        $ dns_sayori_event_running = False
                        $ dns_easter_egg_active = False
                        $ dns_doki_visible = True

                        $ dns_keep_monika_hidden()


                return


        "Never mind.":

            dns_n "Whatever."

            return


# ============================================================
# INITIAL NAME DETECTION
# ============================================================

init python:

    try:

        dns_current_name = persistent.playername.strip().lower()

    except:

        dns_current_name = ""


    if dns_current_name == "sayori":

        dns_active_doki = "sayori"
        dns_doki_visible = True


    elif dns_current_name == "yuri":

        dns_active_doki = "yuri"
        dns_doki_visible = True


    elif dns_current_name == "natsuki":

        dns_active_doki = "natsuki"
        dns_doki_visible = True


    else:

        dns_active_doki = ""
        dns_doki_visible = False


# ============================================================
# OVERLAY REGISTRATION
# ============================================================

init python:

    if "dns_name_swap_overlay" not in config.overlay_screens:

        config.overlay_screens.append(
            "dns_name_swap_overlay"
        )