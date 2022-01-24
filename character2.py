#Xây dựng lớp Character mô hình hóa một nhân vật game mà mọi người thích:

#Tự định nghĩa danh sách các thuộc tính mà nhân vật có (ví dụ: sát thương, máu, giáp, …)
#Các phương thức phù hợp để truy cập/chỉnh sửa các thuộc tính đó
#Có phương thức attack(other_player) để tấn công nhân vật khác
#Bổ sung thêm các thuộc tính như mana, skill để mỗi 2 lần tấn công bình thường thì có thể tấn công bằng kỹ năng
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass 
class AWeapon():
    name = ''
    
    @abstractmethod
    def attack(self,damage):
        return damage
 
@dataclass
class Gun(AWeapon):
    def __post_init__(self):
        self.name = '🔫'
    def attack(self):
        return super().attack(10)

@dataclass
class Sword(AWeapon):
    def __post_init__(self):
        self.name = '🔪'
    def attack(self):
        return super().attack(3)

@dataclass
class Axe(AWeapon):
    def __post_init__(self):
        self.name = '🪓'
    def attack(self):
        return super().attack(5)
      
@dataclass
class Character:
    name:str
    weapon: AWeapon
    defense: int
    health: int
    mana: int
        
    def display(self):
        print('====={}====='.format(self.name))
        print('❤️  {}'.format(self.health))
        print('⚡ {}'.format(self.mana))
        
    def change_weapon(self, weapon: AWeapon):
        if type(self.weapon)!=type(weapon):
            self.weapon = weapon
            print('{} đổi vũ khí {}'.format(self.name, weapon.name))
        
    def attack(self, other: Character):
        damage = self.weapon.attack()
        isSkill = False
        
        if self.health<=0:
            return print('Chết rồi còn đòi đánh ai nữa?')
        
        if other.health > 0:
            #Nếu mana == 100 ==> sát thương x2
            if self.mana == 100:
                damage = damage*2 - other.defense
                self.mana = 0
                isSkill = True
            else:
                damage = damage - other.defense
                self.mana += 50
            
            if damage<0:
               damage = 0
            
            if other.health > damage:
                other.health -= damage
            else:
                other.health = 0
            
            if damage>0:
                print('{} {}  {}, gây {}💔 sát thương'.format(self.name,self.weapon.name*2 if isSkill else self.weapon.name, other.name, damage))
            else:
                print('{} {}  {}, nhưng không mất máu do thủ của {} to quá!'.format(self.name,self.weapon.name*2 if isSkill else self.weapon.name, other.name,other.name))
        else:
            print(other.name + " đã 💀🪦")
            
c1 = Character("Tú",Gun(),2,100,0)
c2 = Character("Hiếu",Sword(),5,100,0)

c1.attack(c2)
c2.attack(c1)
c1.attack(c2)
c1.change_weapon(Axe())
c2.attack(c1)
c1.attack(c2)
c2.change_weapon(Gun())
c2.attack(c1)
for i in range(10):
    c1.attack(c2)
    c2.attack(c1)

c1.display()
c2.display()
