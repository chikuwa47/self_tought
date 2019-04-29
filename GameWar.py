#! /usr/bin/env python3
# GameWar.py - トランプゲーム「戦争」

from random import shuffle

class Card:
    suits = ['spades', 'hearts', 'diamonds', 'clubs']

    # index番号とカード番号を合わせるため、初めの２つをNoneにしている
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9',
              '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, v, s):
        """suit and value should be integers
        スート（マーク）も値も整数値です。"""
        self.value = v
        self.suit = s

    # ２枚のカードを比べ、優劣を決める
    def __lt__(self, c2):  # __lt__か__gt__関数どちらかあればOKみたい
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

#    def __gt__(self, c2):
#        if self.value > c2.value:
#            return True
#        if self.value == c2.value:
#            return self.suit > c2.suit
#        return False
    
    def __repr__(self):  # カードの表示を　ハートの３　みたいに変更
        v = self.values[self.value] + ' of ' + \
            self.suits[self.suit]
        return v


class Deck:
    def __init__(self):  # カードを56枚self.cardsに代入し、シャッフル
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()  # self.cardsリストの最後からカードを抜く。.pop()の　カッコに何も指定しなければ、リストの最後の値を取得する。

class Player:
    def __init__(self, name):
        self.wins = 0  # 勝利数
        self.card = None  # 引いた(drawした)カード
        self.name = name  # プレイヤーの名前


class Game:
    def __init__(self):
        name1 = input('プレーヤー１の名前: ')
        name2 = input('プレーヤー２の名前: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = f'このラウンドは {winner.name} が勝ちました'
        print(w)

    def print_draw(self, p1, p2):
        d = f'{p1.name} は {p1.card}、 {p2.name} は {p2.card} を引きました'
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print('戦争を始めます')
        while len(cards) >= 2:
            m = 'q で終了、それ以外のキーでプレイ'
            response = input(m)
            if response == 'q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:  # カードの優劣を判断
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)
        if win == '引き分け':
            print('引き分け')
        else:
            print(f'ゲーム終了、 {win} の勝利です！')
            print(f"'勝利数' {self.p1.name} : {self.p1.wins}回, {self.p2.name} : {self.p2.wins}回")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return '引き分け'

game = Game()
game.play_game()



