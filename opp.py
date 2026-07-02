from datetime import datetime


# class Handle:
#     def __init__(self,brand,spec ,coo):
#         self.brand =brand
#         self.spec = spec
#         self.coo =coo
    
# class Make:
#     def __init__(self,country,year):
#         self.country = country
#         self.year= year

# make = Make("china",2025)
# handle = Handle('asus','amd',make)

# print(handle.coo.country)
# print(handle.coo.year)


class person:
    user_count = 0
    def __init__(self,name,email,password=0):
        self._name = name
        self._email = email
        self._password = password
        person.user_count+=1
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,newEmail):
        if '@' in newEmail:
            self._email = newEmail
    
    



    
    # def getName(self):
    #     print(datetime.now())
       
    #     return self._name
    
    # def setName(self,name):
    #     self._name = name
    
    
    # def setEmail(self,newEmail):
    #    if '@' in newEmail:
    #        self._email = newEmail
        

    # def getEmail(self):
    
    #     return self._email
    
    # def sayHello(self,user):
    #     print(f"sending to {user.name}, hi {user.name} from {self.name}")

p1 = person("Shen","shen@qq.com")
p1.email= "nonononono"
p2= person("dandan","dd@df.com")
p2.email= "nonononono"

print(p1.email)
print(person.user_count)

# p = person("shen",100)
# p1 = person('dan',99)
# p.sayHello(p1)


class vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year =year

    def info(self):
        print(f'{self.brand}-{self.year}')

    def start(self):
        print("start")

    def stop(self):
        print("stop")



class car(vehicle):
    def __init__(self,brand,year,wheel):
        super().__init__(brand, year)
        self.wheel =wheel

class moto(vehicle):
    def __init__(self,brand,year,engine):
        super().__init__(brand,year)
        self.engine = engine

c =car('toyota','2029',4)
print(c.__dict__)


from abc import ABC,abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self,message:str):
        pass




class EmailService(NotificationService):
    def send_notification(self,message):
        print(f'sending email {message}')


class MobileService(NotificationService):
    def send_notification(self,message:str):
        print(f'sending text message {message}')

        


class Order:
    def __init__(self,notificationService:NotificationService):
        self.notificationService = notificationService
    def create(self):
        self.notificationService.send_notification("sending now!")

order = Order(EmailService())
order.create()















# class payment_abs(ABC):
#     @abstractmethod

#     def pay(self,aount:float):
#         pass
    



# class paypalPayment(payment_abs):
#     def pay(self,amount):
#         print(f'paypal payment is {amount}')

# class creditCardPayment(payment_abs):
#     def pay(self,amount):
#         print(f'credit card payment {amount}')



# def checkOut(payment:payment_abs,amount:float):
#     payment.pay(amount)


# checkOut(paypalPayment(),100)
# checkOut(creditCardPayment(),200)




# class primarySkill(ABC):
#     @abstractmethod
#     def skillName(self,skill:str):
#         print(f'skill is {skill}')



# class DPS(primarySkill):
#     def skillName(self,skill):
#         print(f'dps -> {skill} ')


# class HEALER(primarySkill):
#     def skillName(self,skill):
#         print(f'healer ->{skill}')



# class OUTPUT:
#     def output(skill:primarySkill,input:str):
#         skill.skillName(input)

# k = OUTPUT
# k.output(DPS(),"emp")



class bankAccount:
    def __init__(self,balance):
        self._balance =balance

    def deposit(self,amount:int):
        if amount >= 10000:
            print("report to IRS")
            return
        self._balance +=amount

    def withdraw(self,amount):
        if self._balance<amount:
            print("insufficent amount")
            return 
        
        if self._balance >=amount:
            self._balance-=amount


    def checkBalance(self):
        return self._balance
    

    def transfer(self,other_account,amount):
        if self._balance<amount:
            print("not enough money")
            return
        
        self._balance-=amount
        other_account._balance+=amount

        



account1 = bankAccount(100)
print(account1.checkBalance())

account1.deposit(1000)
print(account1.checkBalance())

account1.deposit(99999)
print(account1.checkBalance())

account2 = bankAccount(10)
print(account2.checkBalance())

account1.transfer(account2,50)
print(account2.checkBalance())



#composition

class Boss:
    def __init__(self,hp,skill,loot,ai):
        self.hp =hp
        self.skill =skill
        self.loot=loot
        self.ai =ai

# class DragonBoss(Boss):
#     def __init__(self):
#         super().__init__(
#             hp=500,
#             ai=AggressiveAI(),
#             skills=[FireBreath()],
#             loot=DragonLoot()
        # )

# 解耦 Coupling
# 👉 你学到：不要直接改别人数据
class player:
    def __init__(self):
        self.attack_power =10

    def attack(self,boss):
        boss.take_damage(self.attack_power)

        # boss.hp ❌
        # boss.take_damage() ✔

class Boss:
    def __init__(self):
        self.hp=100
    def take_damage(self,damage):
        self.hp-=damage
        print(f"Boss 受到 {damage} 伤害，剩余 HP = {self.hp}")





#factory. 只需要创建对象 输出就好

class Sword:
    def __init__(self):
        self.damage=10

class Bow:
    def __init__(self):
        self.damage =7

class weaponFactory:
    def createWeapon(self,weapon_type):
        if weapon_type =='sword':
            return Sword()
        
        elif weapon_type =="bow":
            return Bow()
        

factory =weaponFactory()
weapon =factory.createWeapon('sword')
print(weapon.damage)



#strategy


# class smallHeal:
#     def __init__(self):
#         self.heal=10

# class bigHeal:
#     def __init__(self):
#         self.heal=25

# class Priest:
#     def healStrategy(self,heal_type):
#         if heal_type =='smallheal':
#             return smallHeal()
        
#         if heal_type =='bigheal':
#             return bigHeal()
        

# p = Priest()
# healing=p.healStrategy('bigheal')
# # print(healing.heal)
        

  

class smallHeal:
    def heal(self):
        print("10 hp healing")

class bigHeal:
    def heal(self):
        print("25 hp healing")

class Priest:
    def __init__(self, skill_type_heal):
        self.skill_type_heal = skill_type_heal

    def heal(self):
        self.skill_type_heal.heal()

p=Priest(bigHeal())
p.heal()

print("------------------------------------------------\n\n\n\n\n\n\n\n\n")


# Player
#  ├── Weapon
#  ├── AttackStrategy
#  └── HP

# Boss
#  ├── AI
#  └── HP

# WeaponFactory

# Battle


class Weapon:
    def __init__(self,name,damage):
        self.name =name
        self.damage= damage

class Sword(Weapon):
    def __init__(self,name,damage):
        super().__init__(name,damage)
     

class Bow(Weapon):
      def __init__(self,name,damage):
        super().__init__(name,damage)
     


class weaponFactory:
    def create_weapon(self,weapon_type):
        if weapon_type == 'sword':
            return Sword("sword",15)
        elif weapon_type == 'bow':
            return Bow("bow",20)


factory = weaponFactory()
weapon = factory.create_weapon('bow')
print(weapon.damage)



print("------------------------------------------------\n\n\n\n\n\n\n\n\n")


# class Character:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

#     def take_damage(self, damage):
#         self.hp -= damage
#         print(f"{self.name} takes {damage} damage")
#         print(f"{self.name} HP: {self.hp}")

#     def show_status(self):
#         print(f"{self.name} HP: {self.hp}")


# class Weapon:
#     def __init__(self, name, damage):
#         self.name = name
#         self.damage = damage


# class Player(Character):
#     def __init__(self, name, hp, weapon):
#         super().__init__(name, hp)
#         self.weapon = weapon

#     def attack(self, target):
#         print(f"{self.name} attacks {target.name} with {self.weapon.name}")
#         target.take_damage(self.weapon.damage)


# class Monster(Character):
#     def __init__(self, name, hp, damage):
#         super().__init__(name, hp)
#         self.damage = damage

#     def attack(self, target):
#         print(f"{self.name} attacks {target.name}")
#         target.take_damage(self.damage)


# # =====================
# # 游戏开始
# # =====================

# sword = Weapon("Sword", 15)

# player = Player("Hero", 100, sword)
# monster = Monster("Slime", 50, 8)

# print("===== Battle Start =====\n")

# round_num = 1

# while player.hp > 0 and monster.hp > 0 and round_num <= 5:
#     print(f"--- Round {round_num} ---")

#     # 玩家攻击
#     player.attack(monster)

#     if monster.hp <= 0:
#         print(f"\n{player.name} wins!")
#         break

#     # 怪物攻击
#     monster.attack(player)

#     if player.hp <= 0:
#         print(f"\n{monster.name} wins!")
#         break

#     print("")
#     round_num += 1

# print("\n===== Battle End =====")





class Account:
    def __init__(self, name,balance):
        self.name =name
        self.balance=balance
    

    def deposit (self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        if self.balance < amount:
            print("not enough moneys")
            return
        else:
            self.balance-=amount
       
 
    
    def show_balance(self):
        print(f"{self.name} {self.balance}")

    
  
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def show_all_accounts(self):
        for account in self.accounts:
            account.show_balance()

    # def find_account(self,account_name):
    #     for i in self.accounts:
    #         if i.name == account_name:
    #             i.show_balance()
    #             return 
    #     return None
                

    def find_account(self,account_name):
        for i in self.accounts:
            if i.name == account_name:
                i.show_balance()
                return
        
        return None
    
    def find_account_for_transfer(self,account_name):
        for i in self.accounts:
            if i.name == account_name:
                return i
        return None
    


    
    def transfer(self,a,b,amount):
        from_A = self.find_account_for_transfer(a)
        to_B = self.find_account_for_transfer(b)

        if not from_A or not to_B:
            print("something is wrong")
            return
        
        if from_A.balance <amount:
            print("not enough")
            return
        
        from_A.withdraw(amount)
        to_B.deposit(amount)

        print(f"{a} to {b} transfer {amount} done!!")



        



bank= Bank()

a1 = Account("shen",500)
a2 = Account("dandan",300)

bank.add_account(a1)
bank.add_account(a2)

a1.show_balance()
a2.show_balance()

a1.deposit(50)
a1.show_balance()


a2.show_balance()


bank.find_account('shen')
bank.find_account('dandan')


bank.transfer('shen','dandan',100)

a1.show_balance()
a2.show_balance()



import sys
x =1000
y=x
print(id(x) == id(y))
print(type(id))
print(sys.getrefcount(a1))


def add(a,b):
    return a+b



def sub(a:int,b:int)->int:
    return a-b

print(int.__mro__) #method resolution order
      
# x = [42,12]
# print(isinstance(x, int))     
# print(isinstance(x, float))
# print(isinstance(x[1],int))


lst = [1,2,3,4,5,6,7,8,'shenhaiqi']
def has__string(lst):
    for i in lst:
        if isinstance('shenhaiqi',str):
            return True
    return False

# print(has__string(lst))


lst2 = [1,3,5,6,7,8,'hi']

def has_int(lst):
    for i in lst:
        if isinstance(i,int):
            return True
    return False


def has_int2(lst):
    for i in lst:
        if not isinstance(i,int):
            return False
    return True

print(has_int2(lst2))

