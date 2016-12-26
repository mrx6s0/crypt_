#!/usr/bin/env python
# -* coding: utf-8 -*- 

from random import choice

def gera_senha(tamanho):
        caracters = '~{}^=+()@#$%*¨&ABCDEFGHIJKLMNOPQRSTUVXZY0123456789abcdefghijlmnopqrstuwvxz'
        senha = ''
        for char in xrange(tamanho):
                senha += choice(caracters)
        return  senha

print gera_senha(18) 

