from django.db import models


class BAccount(models.Model):


    def __init__(self, acctcode, emplcode, clcode,  created_at, amount,state, mov_cont,acc_pass):
        self.acctcode = acctcode
        self.emplcode = emplcode
        self.clcode = clcode
        self.created_at = created_at
        self.amount = amount
        self.state = state
        self.mov_cont = mov_cont
        self.acc_pass = acc_pass
        

    @staticmethod
    def insert( acctcode, emplcode, clcode,created_at,amount, state, mov_cont,acc_pass):

        return BAccount.collection.insert_one({
           
            'acctcode': acctcode,
            'emplcode': emplcode,
            'clcode': clcode,
            'created_at': created_at,
            'amount': amount,
            'state': state,
            'mov_cont':mov_cont,
            'acc_pass':acc_pass
        })
        
    def add_card(self, card):
      
       pass

    def display_cards(self):
   
        return [card.card_number for card in self.cards]