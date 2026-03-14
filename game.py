from classes import Weapon, Armor, Character, Hero, Room, Dungeon, Shop, Healings


bandages = Healings('бинты', 10, 6)
medkit = Healings('аптечка', 15, 13)
healing_potion = Healings('зелье здоровья', 30, 24)
kvas = Healings('квас', 50, 40)



slime_ball = Weapon('слайм', 2, 10)
rat_claws = Weapon('когти крыски', 4, 6)
fist = Weapon('кулаки', 2, 0)
stick = Weapon('палка', 4, 3)
sword = Weapon('меч', 15, 75)
purple_stick = Weapon('фиолетовая палка', 100, 9999)
knife = Weapon('нож', 10, 30)
wings_kfc = Weapon('крылышки ростикс со острым соусом', 6, 40)
bagget = Weapon('тёплый французкий багет', 5, 10)
integraly = Weapon('интегралы', 7, 60)
crocodile_theeth = Weapon('зубы крокодила', 17, 61)
alien_blaster = Weapon('инопрешеленский бластер', 20, 120)
gadzilla_lazer = Weapon('лазер годзиллы', 35, 200000000000)
toad_sword = Weapon('жабий меч', 35, 100)

none = Armor('нет брони', 0, 0)
rat_shkurka = Armor('шкурка крыски', 0.5, 3)
potato = Armor('мешок из под кортошки ', 2, 5)
leather = Armor('кожаная броня', 6, 50)
iron_armor = Armor('железная броня' , 10, 75)
kfc_bucket = Armor('ведро острых крылышек ростикис', 1, 40)
amongus = Armor('крутая броня', 30, 555)
meowl_feather = Armor('перо меовла', 99, 1000000000000)
beret = Armor('французкий берет', 5, 10)
oblozhka = Armor('обложка', 6, 45)
kozha_krokodila = Armor('кожа крокодила', 10, 60)
kozha_gadzilli = Armor('кожа годзиллы', 20, 2000000000000)



swordman = Character('мечник', sword, leather, 24)
meowl = Character('мяуовл', stick, meowl_feather, 2)
rat_larisa = Character('крыска лариска', rat_claws, rat_shkurka, 4)
slime = Character('обычный слизень', slime_ball, none, 5)
goblin = Character('гоблин', knife, none, 13)
boss_rostics = Character('босс роситкс', wings_kfc, kfc_bucket, 6 )
cheburek = Hero('чебурек с мясом', fist, potato, 100, 15)
oge = Character('экзамен ОГЭ', integraly, oblozhka, 20)
crocodile = Character('крокодил', crocodile_theeth, kozha_krokodila, 25)
alien = Character('иноплонетян', alien_blaster, none, 30)
gadzilla = Character('годзилла', gadzilla_lazer, kozha_gadzilli, 100)
zhabka_inventory = [beret,  bagget, knife, sword, toad_sword, leather, iron_armor ,purple_stick, amongus, bandages, medkit, healing_potion, kvas]
zhabka_stonks = Shop('жабка торговец', zhabka_inventory, 1000 )


dump = Room(rat_larisa)

common_room = Room(swordman)


slime_room = Room(slime)


goblin_room = Room(goblin)


rostics = Room(boss_rostics)


ekzamen = Room(oge)

boloto = Room(crocodile)

tarelka = Room(alien)

boss_room = Room(gadzilla)

spisok_komnat = [dump, slime_room, rostics, goblin_room, ekzamen, common_room, boloto, tarelka, boss_room]

epic_dungeon = Dungeon(spisok_komnat)

epic_dungeon.dungeon_manager(cheburek, zhabka_stonks)

  
      









awesome_room = Room(meowl)
# awesome_room.enter_room(the_thinker)


