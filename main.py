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
    # --- القراء (Getters) ---
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
        return self.c_hel >= 0


    # -------------------------  (setter) ---------------------------


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

    # def attck (self :object,target :object ) :
    #     if self._ap >= 3 :
    #         target.c_hel
    #         damage = self.atk - target.ar
            
    #         if damage < 0: damage = 0
            
    #         target.c_hel -= damage
    #         print(f"{self.name} deals {damage} damage to {target.name}")
    #         self._ap -= 3
    #     else : 
    #         print("mo ap point to use this action")













class Card(Hero):
    def __init__(self, id, name, cost, atk, ar, max_hel):
        super().__init__(id, name, atk, ar, max_hel)
        
        self._cost = cost

    # --- القراء (Getters) ---
    @property
    def cost(self):
        return self._cost

    # --- المعدلون (Setters) ---
    @cost.setter
    def cost(self, value):
        self._cost = value
    




 






mon1 = Card(1, "goblin", cost=3, atk=5, ar=2, max_hel=20)
mon2 = Card(2, "Dragon", cost=7, atk=15, ar=3, max_hel=30)
hero1= Hero(3, "Knight", atk=3, ar=3, max_hel=100)
hero2 = Hero(4, "Knight", atk=3, ar=3,  max_hel=100)


print(mon1.__dict__)
print(mon2.__dict__)
print(hero1.__dict__)
print(hero2.__dict__)

mon1.Battck(mon2)
mon1.Battck(mon2)



print(mon1.__dict__)
print(mon2.__dict__)


# add deak 
while hero1.is_alive and hero2.is_alive :
    turn = 0 
    hero1.ap = hero1.ap + turn
    while hero1.ap > 0 :
        action = input("play")


        ...




    while hero1.ap > 0 :

        ...


    turn += 1 



    # x=input()
    # if x == "1" : 
    #     pass

    # hero1.ap,hero2.ap += 3