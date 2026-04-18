from time import sleep
from random import randint 
import json

class Character:
    def __init__(self, name, weapon, armor, hp):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.hp = hp

class Hero(Character):
    def __init__(self, name, weapon, armor, hp, money):
        super().__init__(name, weapon, armor, hp)
        self.money = money 
        self.inventory = [] 

     #ИНВЕНТАРЬ
    def inventory_manager(self):
        while True:
            c =  int(input('нажми 1 для полного списка предметов \nнажми 2 если хочешь что-то экипировать или съесть хилку \nнажми 3 чтобы выйти из инвентаря: '))
            print('--------------------------------------------------')  
            if c == 1:
                self.show_hero_stats()
                self.show_hero_inventory()
                
            elif c == 2:
                self.equip()

            elif c == 3:
                break    
            else:
                print('нет действия под таким номером!')
                print('--------------------------------------------------')           
    
    def show_hero_inventory(self):
        m = 1
        for i in self.inventory:
            print(f"{m}.{i}")
            m += 1
        print('--------------------------------------------------')
    
    def show_hero_stats(self):
        print(f"HP:{self.hp}\nденьги:{self.money}\nоружие:{self.weapon}\nброня:{self.armor}")
        print('--------------------------------------------------')

    def equip(self):
        self.show_hero_inventory()
        n = int(input('выбери предмет, который хочешь экипировать или съесть: '))
        print('--------------------------------------------------')
        if n > len(self.inventory) or n < 1:
            print('в списке нету предмета с таким номером')
        else:
            if isinstance(self.inventory[n - 1], Weapon):
                self.inventory.append(self.weapon)
                self.weapon = self.inventory.pop(n - 1)

            elif isinstance(self.inventory[n - 1], Armor):
                self.inventory.append(self.armor)
                self.armor = self.inventory.pop(n - 1)

            elif isinstance(self.inventory[n - 1], Healings):
                self.hp += self.inventory[n - 1].heal
                self.inventory.pop(n - 1)
                print(f'вы восполнили своё здровье на {self.inventory[n - 1].heal} едениц ')
                print('--------------------------------------------------')
            

        
        

    

class Weapon:
    def __init__(self, name, dmg, price):
        self.name = name
        self.dmg = dmg
        self.price = price
    
    def __str__(self):
        return f"Название: {self.name}| урон: {self.dmg}| цена: {self.price}"
    

class Armor:
    def __init__(self, name, df, price):
        self.name = name
        self.df = df
        self.price = price

    def __str__(self):
        return f"Название: {self.name}| защита: {self.df}| Цена: {self.price}"
    

class Healings:
    def __init__(self, name, heal, price):
        self.name = name
        self.heal = heal
        self.price = price

    def __str__(self):
        return f"Название: {self.name}| +хп: {self.heal}| Цена: {self.price}"


class Shop:
    def __init__(self, name, inventory, money):
        self.name = name
        self.inventory = inventory
        self.money = money
        
    def trader_manager(self, hero):
        while True:
            c = int(input('ты зашел в магазин, нажми 1 если хочешь что-то купить\nнажми 2 если хочешь что-то продать\nнажми 3 чтобы уйти из магазина: '))
            print('--------------------------------------------------')
            if c == 1:
                self.buy_item(hero)
            elif c == 2:
                self.sell_item(hero)
            elif c == 3:
                break 
        
    #ПОКУПКА
    def buy_item(self, hero):
        self.show_inventory()
        u = int(input("Укажи номер пердмета: "))
        if u > len(self.inventory) or u < 1:
            print('такого предмета нет в списке')
            print('--------------------------------------------------')
            return
        
        r = hero.money - self.inventory[u - 1].price
        if r < 0:                                                                          
            print('неодостаточно средств')
            print('--------------------------------------------------')       
        else:    
            if not isinstance(self.inventory[u - 1], Healings):
                item = self.inventory.pop(u - 1)
            else:
                item = self.inventory[u - 1] 
            hero.money -= item.price     
            hero.inventory.append(item)   
            print(f"ты купил {item.name} за {item.price} монет и у тебя осталось {hero.money}")
            print('--------------------------------------------------')
            

    #ПРОДАЖА       
    def sell_item(self, hero):
        if hero.inventory == []:
            print('кажется предметов у тебя нет, нечего тебе продавать!')
            print('--------------------------------------------------')
            return
        hero.show_hero_inventory()
        u = int(input("Укажи номер пердмета: "))
        if u > len(hero.inventory) or u < len(hero.inventory):
            print('такого предмета нет в списке')
            print('--------------------------------------------------')
            return
        y = self.money - hero.inventory[u - 1].price                           
        if y < 0:
            print("кажется у торговца нет денег чтобы купить этот предмет")
            print('--------------------------------------------------')
        
        else:
            self.money -= hero.inventory[u - 1].price
            item = hero.inventory.pop(u - 1)
            self.inventory.append(item)
            hero.money += item.price 
            print(f'ты продал торговцу {item.name} за {item.price} монет, и твой баланс теперь {hero.money}')
      

    def show_inventory(self):
        m = 1
        
        for i in self.inventory:
            print(f"{m}.{i}")
            m += 1

        
    


class Room:
    def __init__(self, enemy):
        self.enemy = enemy    

    #ВХОД В КОМНАТЫ
    def enter_room(self, hero):
        print('ты зашел в крутую комнату и в ней ты встретил', self.enemy.name)
        while True:
            try:
                answer = int(input('напиши 1, чтобы начать схватку, или напиши 2, чтобы заныть: '))
                print('--------------------------------------------------')
                if answer == 1:
                    self.start_fight(hero)
                    break
                elif answer == 2:
                    self.zanit(hero)
                    break
            except ValueError:
                print('надо ввести число 1 или 2')
            

    
    #БОЁВКА
    def start_fight(self, hero:Hero):
        while hero.hp > 0 and self.enemy.hp > 0:
            damage = hero.weapon.dmg - self.enemy.armor.df
            if damage < 0:
                damage = 0
            self.enemy.hp -= damage
            if self.enemy.hp < 0:
                self.enemy.hp = 0
            print(f'вы нанесли {damage}, урона и у противника осталось {self.enemy.hp} здоровья')
            if self.enemy.hp < 1:
                print('--------------------------------------------------')
                print('вы победили!')
                self.get_reward(hero)
                break

            sleep(1.5)           
            en_damage = (self.enemy.weapon.dmg - hero.armor.df)
            if en_damage < 0:
                print('атака противника не нанесла вам урона')
            else:
                hero.hp -= en_damage
                if hero.hp < 0:
                    hero.hp = 0
                print(f'вам нанесли {en_damage}, и у вас осталось {hero.hp} здоровья')
                

    #ПОЛУЧЕНИЕ НАГРАДЫ ПОСЛЕ МАХАЧА
    def get_reward(self, hero):
        g = randint(1, 100)
        if g > 0 and g <= 49:
            if  self.enemy.armor.name != 'нет брони':
                hero.inventory.append(self.enemy.armor)
                print(f'после победы над противником вы нашли и забрали себе: {self.enemy.armor.name}')
                print('--------------------------------------------------')  
            else:
                print('похоже что на противнике не было ничего такого, что можно использовать как броню')
         
        elif g >= 50 and g < 99:
            hero.inventory.append(self.enemy.weapon)
            print(f'после победы над противником вы нашли и забрали себе: {self.enemy.weapon.name}')
            print('--------------------------------------------------')  
        
        elif g == 99 or g == 100:
            print('тебе очень повезло ты нашел 500 монет!')
            hero.money += 500
            

    
    
    
            
            

      
    #ЗАНЫТЬ
    def zanit(self, hero: Hero):
        print('Ты поныл и заплатил 30, чтобы откупится от драки. Гуляй')
        if hero.money < 30:
            print('похоже денях у тебя нет. ну тогда держи 80 урона')
            hero.hp -= 80

        elif hero.money >= 30:
            print('Ты поныл и заплатил 30, чтобы откупится от драки. Гуляй')
            hero.money -= 30



class Dungeon:
    def __init__(self, rooms, hero, trader):
        self.rooms = rooms
        self.hero = hero
        self.trader = trader
        self.current_room = 0
        
    
    def next_room(self, hero):               
        self.rooms[self.current_room].enter_room(hero)
        self.current_room += 1

    def dungeon_manager(self):
        while True:
            c =  int(input('напиши 1, если хочешь зайти в следующую комнату \nнапиши 2, чтобы зайти в магазин \nнапиши 3, чтобы зайти в инвентарь: '))
            print('--------------------------------------------------')

            if c == 1:       
                self.next_room(self.hero)
            elif c == 2:
                self.trader.trader_manager(self.hero)                
            elif c == 3:
                self.hero.inventory_manager()
            elif c == 4:
                self.save_data()
            elif c == 5:
                self.load_data()
            else:
                print('нет действия под таким номером')

            if self.current_room == len(self.rooms):
                print('Поздравляю с проходением игры!')
                break          

            if self.hero.hp <= 0:
                print('Вы проиграли!')
                break

    def save_data(self):
        with open("save.json", "w", encoding="utf-8") as file:
            json.dump(self.hero, file, ensure_ascii=False, indent=4)

    def load_data(self):
        pass
        

            