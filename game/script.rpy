# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define sounds = ["audio/Voices/voice_bloodiey.ogg","audio/Voices/voice_alice.ogg","audio/Voices/voice_kenia.ogg","audio/Voices/voice_camacho.ogg"]
init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[0]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v
    def type_sound_Alice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[1]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
           


        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
        
    def type_sound_kenia(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[2]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            
           


        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def type_sound_camacho(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            snd = sounds[3]
            renpy.sound.play(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
            renpy.sound.queue(snd)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

# El juego comienza aquí.

# define hugo = Character("hugo",color="#00FBFE",callback=type_sound)
define ButterPie = Character("ButterPie",color="#f600fe",callback=type_sound_Alice)
define Bloodine = Character("Bloodine",color="#b9d6ff",callback=type_sound_kenia)
# define camacho = Character("camacho",color="#73ff00",callback=type_sound_camacho)
define Bloodiey = Character("Bloodiey",color="#0011ff",callback=type_sound)
label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene bg subconsincious

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show bloodiey happy

    # Presenta las líneas del diálogo.
    play music "audio/gallery.mp3"
    Bloodiey "Hola Amigo!"
    Bloodiey "Bienvenido al plano multiversal"
    Bloodiey "Aca puedes hacer lo que quieras"
    Bloodiey "Asegurate de no romper las reglas cosmicas!"
    Bloodiey "Quieres leerlas?"
    menu:
        "Si":
            jump ReadCosmicRules
        "No":
            jump skip_Cosmic_rules

    label skip_Cosmic_rules:
        Bloodiey "Vale Comprendo"
        jump afterCosmicRules

    label ReadCosmicRules:
        Bloodiey "Vale pues Empezemos por lo basico"
        Bloodiey "Numero 1:"
        Bloodiey "No Alterar el orden con tus acciones"
        Bloodiey "Basicamente No mates a Nadie"
        Bloodiey "Numero 2:"
        Bloodiey "No puedes accedar a todos los universos"
        Bloodiey "Sobre todo aquellos que sean aterradores"
        Bloodiey "En caso De entrar en uno salga inmediatamente"
        Bloodiey "Y esas son todas"
        jump afterCosmicRules

    label afterCosmicRules: 
    Bloodiey "Bueno sigamos"
    Bloodiey "¿Estas Listo para entrar al Multiverso?"
    Bloodiey "¡Por que yo si lo estoy!"

    scene bg secrethouse

    "parece que estan en un cuarto"
    "Asi que va a ser complicado"
    
    # Here starts the Hub shit Maybe
    
    call screen multiversalGate

    # Finaliza el juego:

    return
