class Card:
    def __init__(self, id, name, cost, atk, ar, mr, hel, atkT="ad"):
        # المتغيرات الأساسية (التي تبدأ بـ _ لتعبر عن أنها خاصة)
        self._id = id
        self._name = name
        self._cost = cost
        self._atk = atk
        self._ar = ar
        self._mr = mr
        self._hel = hel
        self._atkT = atkT
        self._ex = True

    # --- القراء (Getters) ---
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
    def hel(self):
        return self._hel

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

    @hel.setter
    def hel(self, value):
        self._hel = value



    

    def attak(self, n):
        if self._size - n < 0 :
                 raise ValueError

        self._size = self._size  - n
        return self._size  














mon1 =Card(12,"stack",5,10,3,3,20)
print(mon1.cost)