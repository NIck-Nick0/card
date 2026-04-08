import random
import os

class Hero: 
    def __init__(self, id, name, atk, ar, max_hel ):
        self._id = id
        self._name = name
        self._atk = atk
        self._ar = ar
        self._max_hel = max_hel
        self._c_hel = max_hel
        self._ex = True
        self._ap =3

        self._hand = []
        self._deck = []  
        self._field = []
    # ---  (Getters) ---


    @property
    def hand(self): return self._hand

    @property
    def id(self): return self._id

    @property
    def name(self): return self._name

    @property
    def atk(self): return self._atk

    @property
    def ar(self): return self._ar

    @property
    def c_hel(self): return self._c_hel
    
    @property
    def max_hel(self): return self._max_hel
    
    @property
    def ex(self): return self._ex
    
    @property
    def ap(self): return self._ap

    @property
    def is_alive(self):
        return self.c_hel > 0
    
    @property
    def field(self):
        return self._field


    # -------------------------  (setter)   ---------------------------


    @atk.setter
    def atk(self, value):
        self._atk = value

    @ar.setter
    def ar(self, value):
        self._ar = value

    @c_hel.setter
    def c_hel(self, value): 
        self._c_hel = value

    @max_hel.setter
    def max_hel(self, value): 
        self._max_hel = value


    @ap.setter
    def ap(self, value): 
        self._ap = value

    def Battck (self :object,target :object ) :
        if self._ap >= 3 :
            target.c_hel
            damage = self.atk - target.ar
            
            if damage < 0: damage = 0
            
            target.c_hel -= damage
            print(f"{self.name} deals {damage} damage to {target.name}")
            self._ap -= 3
        else : 
            print("mo ap point to use this action")




    def load_deck(self, cards_list):
        self._deck = cards_list.copy() 
        random.shuffle(self._deck)
    
    def draw_card(self):
        if len(self._deck) > 0:
          
            new_card = self._deck.pop() 
            self._hand.append(new_card)
            print(f"🃏  Draw card : {new_card.name}")
        else:
            print(f"⚠️   Emety deck ")


    def summon_card(self, index):  
        if 0 <= index < len(self._hand):
            card = self._hand[index]
            if self.ap >= card.cost:
                self.ap -= card.cost
                self._field.append(card) 
                self._hand.pop(index)    
                print(f"⚔️ {self.name} summoned {card.name} to the field!")
            else:
                print(f"❌ Not enough AP! (Required: {card.cost})")
        else:
            print("⚠️ Invalid card index!" )       


class Card(Hero):
    def __init__(self, id, name, cost, atk, ar, max_hel):
        super().__init__(id, name, atk, ar, max_hel)
        
        self._cost = cost

    @property
    def cost(self):
        return self._cost

   
    @cost.setter
    def cost(self, value):
        self._cost = value
    


def show_field(hero1, hero2):
    print(f"\n" + "="*60)
    print(f"🏟️  BATTLEFIELD STATE")
    
    print(f"[{hero2.name}] Units: ", end="")
    if not hero2.field: print("None", end="")
    for i, u in enumerate(hero2.field):
        print(f" | ID:{i} {u.name}[HP:{u.c_hel}|AR:{u.ar}|ATK:{u.atk}] ", end="")
    
    print(f"\n" + "-"*15 + " VS " + "-"*15)
    
    print(f"[{hero1.name}] Units: ", end="")
    if not hero1.field: print("None", end="")
    for i, u in enumerate(hero1.field):
        print(f" | ID:{i} {u.name}[HP:{u.c_hel}|AR:{u.ar}|ATK:{u.atk}] ", end="")
    print("\n" + "="*60)








hero1= Hero(3, "Knight", atk=6, ar=3, max_hel=100)
hero2 = Hero(4, "Knight", atk=6, ar=3,  max_hel=100)






c1 = Card(101, "Slayer", cost=1, atk=8, ar=1, max_hel=10)
c2 = Card(102, "Berserker", cost=2, atk=12, ar=0, max_hel=15)
c3 = Card(103, "Assassin", cost=2, atk=15, ar=1, max_hel=8)
c4 = Card(104, "Fire Mage", cost=3, atk=18, ar=2, max_hel=20)
c5 = Card(105, "Dragon Kin", cost=4, atk=25, ar=4, max_hel=30)
c6 = Card(106, "Giant", cost=5, atk=35, ar=5, max_hel=50)

# ---  (Tanks) ---
c7 = Card(107, "Shield Bearer", cost=1, atk=2, ar=5, max_hel=15)
c8 = Card(108, "Iron Golem", cost=3, atk=5, ar=10, max_hel=40)
c9 = Card(109, "Royal Guard", cost=2, atk=6, ar=6, max_hel=25)
c10 = Card(110, "Castle Wall", cost=4, atk=0, ar=15, max_hel=60)

# --- (Balanced) ---
c11 = Card(111, "Knight apprentice", cost=1, atk=5, ar=2, max_hel=12)
c12 = Card(112, "Viking Warrior", cost=2, atk=9, ar=3, max_hel=20)
c13 = Card(113, "Samurai", cost=3, atk=14, ar=4, max_hel=25)
c14 = Card(114, "Paladin", cost=4, atk=12, ar=8, max_hel=35)

# --- (Early Game) ---
c15 = Card(115, "Goblin", cost=1, atk=4, ar=1, max_hel=8)
c16 = Card(116, "Wolf", cost=1, atk=6, ar=0, max_hel=10)
c17 = Card(117, "Skeleton", cost=1, atk=5, ar=1, max_hel=7)

# ---(Legendary/Boss) ---
c18 = Card(118, "Dark Lord", cost=5, atk=40, ar=10, max_hel=100)
c19 = Card(119, "Archangel", cost=5, atk=30, ar=15, max_hel=80)
c20 = Card(120, "Void Beast", cost=4, atk=22, ar=6, max_hel=45)

all_cards = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, 
             c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]



def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')












# game 
def main():

    hero1.load_deck(all_cards)
    hero2.load_deck(all_cards)

    print ("player one :-")
    for _ in range(3):
        hero1.draw_card()
    print()
    print ("player two :-")
    for _ in range(3):
        hero2.draw_card()


    # turn = 0
    turn = 1

    while hero1.is_alive and hero2.is_alive:

        

        hero1.ap = 3 + turn  
        hero1.draw_card()    
        
        while hero1.ap > 0:
            clear_screen()
            print(f"\n>>> {hero1.name}'s Turn (P1) | ❤️ HP: {hero1.c_hel} | ✨ AP: {hero1.ap}")
            
            show_field(hero1, hero2)
            print("\nYour Hand:")
            for i, card in enumerate(hero1.hand):
                print(f"  [{i}] {card.name} (Cost:{card.cost} | ATK:{card.atk} | HP:{card.c_hel} | AR:{card.ar})")
            
            action = input("\nAction (Index:Summon, a:HeroAtk, u:UnitAtk, e:End): ").strip().lower()

            if action == "a":
                hero1.Battck(hero2)
                
            elif action == "e":
                hero1.ap = 0
                print(f"--- {hero1.name} ended the turn ---")
                break
                
            elif action == "u":
                if len(hero1.field) > 0:
                    try:
                        u_idx = int(input("Select YOUR unit index to attack: "))
                        if 0 <= u_idx < len(hero1.field):
                            attacker = hero1.field[u_idx]
                            target_choice = input("Attack Enemy Hero (h) or Enemy Unit (Index)? ").strip().lower()
                            
                            if target_choice == 'h':
                                attacker.Battck(hero2)
                            elif target_choice.isdigit():
                                t_idx = int(target_choice)
                                if 0 <= t_idx < len(hero2.field):
                                    victim = hero2.field[t_idx]
                                    attacker.Battck(victim)
                                    if victim.c_hel <= 0:
                                        print(f"💀 {victim.name} has been destroyed!")
                                        hero2.field.pop(t_idx)
                    except (ValueError, IndexError):
                        print("⚠️ Invalid input or index!")
                else:
                    print("❌ No units on field to attack with!")

            elif action.isdigit():
                idx = int(action)
                hero1.summon_card(idx)
            
            if not hero2.is_alive: 
                print(f"\n🏆 {hero1.name} IS THE VICTOR!")
                break

        if not hero2.is_alive: break












    
        hero2.ap = 3 + turn
        hero2.draw_card()
        
        while hero2.ap > 0:
            clear_screen()
            print(f"\n>>> {hero2.name}'s Turn (P2) | ❤️ HP: {hero2.c_hel} | ✨ AP: {hero2.ap}")
            
            show_field(hero2, hero1) 
            print("\nYour Hand:")
            for i, card in enumerate(hero2.hand):
                print(f"  [{i}] {card.name} (Cost:{card.cost} | ATK:{card.atk} | HP:{card.c_hel} | AR:{card.ar})")
                
            action = input("\nAction (Index:Summon, a:HeroAtk, u:UnitAtk, e:End): ").strip().lower()

            if action == "a":
                hero2.Battck(hero1)
            elif action == "e":
                hero2.ap = 0
                break
            elif action == "u":
                if len(hero2.field) > 0:
                    try:
                        u_idx = int(input("Select YOUR unit index to attack: "))
                        if 0 <= u_idx < len(hero2.field):
                            attacker = hero2.field[u_idx]
                            target_choice = input("Attack Enemy Hero (h) or Enemy Unit (Index)? ").strip().lower()
                            
                            if target_choice == 'h':
                                attacker.Battck(hero1)
                            elif target_choice.isdigit():
                                t_idx = int(target_choice)
                                if 0 <= t_idx < len(hero1.field):
                                    victim = hero1.field[t_idx]
                                    attacker.Battck(victim)
                                    if victim.c_hel <= 0:
                                        print(f"💀 {victim.name} has been destroyed!")
                                        hero1.field.pop(t_idx)
                    except (ValueError, IndexError):
                        print("⚠️ Invalid input or index!")
                else:
                    print("❌ No units on field to attack with!")

            elif action.isdigit():
                idx = int(action)
                hero2.summon_card(idx)

            if not hero1.is_alive:
                print(f"\n🏆 {hero2.name} IS THE VICTOR!")
                break

        turn += 1


if __name__ == "__main__":
    main()




        

