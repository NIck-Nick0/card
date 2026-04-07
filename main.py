class Hero: 
    def __init__(self, id, name, atk, ar, mr,max_hel, atkT="ad"):
        # المتغيرات الأساسية (التي تبدأ بـ _ لتعبر عن أنها خاصة)
        self._id = id
        self._name = name
        self._atk = atk
        self._ar = ar
        self._mr = mr
        self._max_hel = max_hel
        self._c_hel = max_hel
        self._atkT = atkT
        self._ex = True

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @property
    def ex(self):
        return self._ex

    @property
    def atk(self):
        return self._atk

    @property
    def ar(self):
        return self._ar

    @property
    def mr(self):
        return self._mr

    @property
    def c_hel(self):
        return self._c_hel
    
    @property
    def max_hel(self):
        return self._max_hel
    
    @property
    def atkT(self):
        return self._atkT

    # --- المعدلون (Setters) ---
    @cost.setter
    def cost(self, value):
        self._cost = value

    @atk.setter
    def atk(self, value):
        self._atk = value

    @ar.setter
    def ar(self, value):
        self._ar = value

    @mr.setter
    def mr(self, value):
        self._mr = value

    @c_hel.setter
    def max_hel(self, value):
        self._c_hel = value


    @max_hel.setter
    def max_hel(self, value):
        self._max_hel = value


    def attck (self :object,target :object ) :
        target._hel
        damage = self.atk - target.ar
        
        # لضمان أن الضرر لا يكون سالباً (يعالج الخصم)
        if damage < 0: damage = 0
        
        target.hel -= damage
        print(f"{self.name} deals {damage} damage to {target.name}")


# def __init__(self, id, name, cost, atk, ar, mr, hel, spell_power):
#         # استدعاء الـ __init__ الخاص بالكلاس الأب
#         super().__init__(id, name, cost, atk, ar, mr, hel)
#         self.spell_power = spell_power

class Card(Hero) :
    def __init__(self, id, name, cost, atk, ar, mr,max_hel, atkT="ad"):
        # المتغيرات الأساسية (التي تبدأ بـ _ لتعبر عن أنها خاصة)
        super().__init__(id, name, atk, ar, mr, max_hel)
        self._cost = cost
        
        self._atkT = atkT
        self._atkT = atkT

        self._ex = True

    # --- القراء (Getters) ---
    # @property
    # def id(self):
    #     return self._id

    # @property
    # def name(self):
    #     return self._name

    @property
    def cost(self):
        return self._cost

    @property
    def ex(self):
        return self._ex

    # @property
    # def atk(self):
    #     return self._atk

    # @property
    # def ar(self):
    #     return self._ar

    # @property
    # def mr(self):
    #     return self._mr

    # @property
    # def hel(self):
    #     return self._hel

    @property
    def atkT(self):
        return self._atkT

    # --- المعدلون (Setters) ---
    @cost.setter
    def cost(self, value):
        self._cost = value

    # @atk.setter
    # def atk(self, value):
    #     self._atk = value

    # @ar.setter
    # def ar(self, value):
    #     self._ar = value

    # @mr.setter
    # def mr(self, value):
    #     self._mr = value

    # @hel.setter
    # def hel(self, value):
    #     self._hel = value



    





















    def attak(self, n):
        if self._size - n < 0 :
                 raise ValueError

        self._size = self._size  - n
        return self._size  
















mon1 =Card(12,"stack",5,10,3,3,20)
print(mon1.cost)