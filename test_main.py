import pytest
from main import Hero, Card 

def test_hero_init():
    knight = Hero(1, "Knight", 10, 5, 100)
    assert knight.name == "Knight"
    assert knight.c_hel == 100
    assert knight.ap == 3
    assert len(knight.hand) == 0
    assert len(knight.field) == 0

def test_draw_card():
    hero = Hero(1, "Hero", 10, 5, 100)
    cards = [Card(101, "Slayer", 1, 8, 1, 10)]
    hero.load_deck(cards)
    
    hero.draw_card()
    assert len(hero.hand) == 1
    assert hero.hand[0].name == "Slayer"
    
    hero.draw_card()
    assert len(hero.hand) == 1 

def test_summon_card():
    hero = Hero(1, "Hero", 10, 5, 100)
    hero.ap = 5
    card = Card(101, "Slayer", 3, 8, 1, 10)
    hero._hand.append(card) 
    
    hero.summon_card(0)
    assert hero.ap == 2 
    assert len(hero.field) == 1
    assert len(hero.hand) == 0

def test_summon_no_ap():
    hero = Hero(1, "Hero", 10, 5, 100)
    hero.ap = 1
    card = Card(101, "Mage", 3, 10, 1, 20)
    hero._hand.append(card)
    
    hero.summon_card(0)
    assert hero.ap == 1 

    assert len(hero.field) == 0 
# 4. اختبار منطق الهجوم (Battle Logic)
def test_attack_damage():
    attacker = Hero(1, "Attacker", 20, 0, 100)
    target = Hero(2, "Target", 0, 5, 100) 
    
    attacker.Battck(target)
    assert target.c_hel == 85

def test_attack_min_damage():
    attacker = Hero(1, "Weakling", 2, 0, 100)
    target = Hero(2, "Tank", 0, 10, 100) 
    
    attacker.Battck(target)
    assert target.c_hel == 100

def test_is_alive():
    hero = Hero(1, "Ghost", 10, 0, 10)
    assert hero.is_alive == True
    
    hero.c_hel = 0
    assert hero.is_alive == False
    
    hero.c_hel = -5
    assert hero.is_alive == False