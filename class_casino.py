from decouple import config
import emoji
from logic_casino import GameLogic


class Casino:
    def __init__(self):
        self.my_money = config('MY_MONEY', cast=int)
        self.logic = GameLogic()

    def start(self):
        while True:
            print(emoji.emojize('Ваш баланс ' + str(self.my_money) + ':heavy_dollar_sign:'))
            word = int(input('Введите число от 1 до 30: '))
            price = int(input('Ваша ставка: '))
            if price > self.my_money:
                print(emoji.emojize(f':cross_mark:Ваша ставка превышает ваш баланс: {self.my_money}:cross_mark:'))
                continue

            result = self.logic.Game(price, word)
            self.my_money += result
            if result > 0:
                print(emoji.emojize(f'Результат: ::fireworks:Вы выйграли: {result}:dollar_banknote:'))
            else:
                print(emoji.emojize(f'Результат: Вы проиграли: {result}:face_with_crossed-out_eyes:'))
                print(emoji.emojize(f"Ваш баланс: {self.my_money}:heavy_dollar_sign:"))

            play = input(emoji.emojize("Хотите продолжить играть? :check_mark_button:'ДА' или :cross_mark:'НЕТ':  "))
            if self.my_money <= 0:
                print(emoji.emojize(f':cross_mark:Игра закончена ваш баланс равняется {self.my_money} :cross_mark:'))
                break
            if play.lower() == 'да':
                print(emoji.emojize(':four_leaf_clover:Отлично пусть удача благоволит вам:four_leaf_clover:'))
                continue
            elif play.lower() == 'нет':
                print(emoji.emojize(f':smiling_face_with_open_hands:Ваш баланс составляет: {self.my_money}' '\n'
                                    'Приходите когда будете готовы и попытайте удачу снова:smiling_face_with_open_hands:'))
                break



