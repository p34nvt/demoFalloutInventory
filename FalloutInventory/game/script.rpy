#text button style
style item:
    size 22
    color "#00dd00"
    hover_color "#44ff44"
    antialias False

init python:
    from time import sleep
#item detail variable
    indice = 0
#item filter variable
    filtro = 0
#short list of items
    filtrada = []
#details variables
    peso, valor, imagen, texto = "", "", "", ""
#item list
    itemlist = [
        {
            "name": "Stimpak",
            "category_id": 1,
            "description": "A healing item that restores health.",
            "weight": 0.1,
            "value": 30,
            "quantity": 3
        },
        {
            "name": "RadAway",
            "category_id": 1,
            "description": "A radiation removal item.",
            "weight": 0.2,
            "value": 75,
            "quantity": 2
        },
        {
            "name": "10mm Pistol",
            "category_id": 3,
            "description": "A semi-automatic handgun.",
            "weight": 1.5,
            "value": 200,
            "quantity": 1
        },
        {
            "name": "Hunting Rifle",
            "category_id": 3,
            "description": "A powerful bolt-action rifle.",
            "weight": 8.0,
            "value": 300,
            "quantity": 2
        },
        {
            "name": "Leather Armor",
            "category_id": 2,
            "description": "Basic protective clothing made of leather.",
            "weight": 10.0,
            "value": 100,
            "quantity": 1
        },
        {
            "name": "Power Armor",
            "category_id": 2,
            "description": "Advanced armored exoskeleton.",
            "weight": 30.0,
            "value": 3000,
            "quantity": 1
        },
        {
            "name": "Nuka-Cola",
            "category_id": 1,
            "description": "A popular carbonated beverage.",
            "weight": 0.5,
            "value": 10,
            "quantity": 10
        },
        {
            "name": "Buffout",
            "category_id": 1,
            "description": "A performance-enhancing drug.",
            "weight": 0.3,
            "value": 30,
            "quantity": 2
        },
        {
            "name": "Frag Grenade",
            "category_id": 3,
            "description": "An explosive device that causes high damage.",
            "weight": 0.5,
            "value": 100,
            "quantity": 2
        },
        {
            "name": "Plasma Rifle",
            "category_id": 3,
            "description": "An energy weapon that shoots superheated plasma.",
            "weight": 10.0,
            "value": 1500,
            "quantity": 1
        },
        {
            "name": "Metal Helmet",
            "category_id": 2,
            "description": "A protective headgear made of metal.",
            "weight": 2.0,
            "value": 75,
            "quantity": 1
        },
        {
            "name": "Psycho",
            "category_id": 1,
            "description": "A powerful combat-enhancing drug.",
            "weight": 0.2,
            "value": 25,
            "quantity": 3
        },
        {
            "name": "Machete",
            "category_id": 3,
            "description": "A sharp melee weapon with a curved blade.",
            "weight": 2.5,
            "value": 75,
            "quantity": 2
        },
        {
            "name": "Rad-X",
            "category_id": 1,
            "description": "A temporary radiation resistance item.",
            "weight": 0.3,
            "value": 30,
            "quantity": 3
        }
    ]

screen display_1():
    frame:
        background Solid("#002200")
        xsize 800
        ysize 600
        xpos 0.2
        ypos 0.05

    frame:
        background Solid("#002200")     # or use any semi-transparent image you like
        align (0.35, 0.5)
        
        side "c l":
            area (0, 0, 500, 300)

            viewport id "vp":

                draggable True
                mousewheel True
                arrowkeys True

                vbox:
                    python:
                        print(str(indice)+" "+str(len(filtrada)))
                        if filtro==0:
                            filtrada = []
                            filtrada = itemlist.copy()
                        else:
                            filtrada = []
                            for dicti in itemlist:
                                if filtro==dicti["category_id"]:
                                    filtrada.append(dicti)
                                    print(str(indice)+" "+str(len(filtrada)))
                                indice+=1
                            if indice>=len(filtrada):
                                indice=0
                    #end of python block
                    for dicti in filtrada:
                        $ name = dicti["name"]
                        $ qua = dicti["quantity"]
                        textbutton name + ' (' + str(qua) + ')':
                            text_style "item"
                            hovered Play("sound", "audio/click.wav")
                            action Call("setdetails", dicti)

            vbar value YScrollValue("vp")

#stats list
    frame:
        background Solid("#005500")
        xpos 0.65
        ypos 0.6

        vbox:
            text "weight [peso]kg" size 18 antialias False
            text "value $[valor]" size 18 antialias False

    image "images/trollface.jpg" xpos 0.55 ypos 0.2
    text texto size 14 xpos 0.5 ypos 0.55

    hbox:
        xalign 0.5
        yalign 0.1
        spacing 10
        textbutton "All" text_style "item" action SetVariable("filtro", 0)
        textbutton "Weapons" text_style "item" action SetVariable("filtro", 3)
        textbutton "Wareable" text_style "item" action SetVariable("filtro", 2)
        textbutton "Consumable" text_style "item" action SetVariable("filtro", 1)

#apply details variables
label setdetails(dicti):
    python:
        peso = dicti["weight"]
        valor = dicti["value"]
        #imagen = "image.jpg"
        texto = dicti["description"]
# The game starts here.
label start:
    scene desert
    #pause 0.05
    call screen display_1

