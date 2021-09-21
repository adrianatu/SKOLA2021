#Sula maksa 1.5 eiro (bez pvn) siers 3 eiro (bez pvn)
#Aprekini cik kopa ar pvn

PVN = 0.21

SulasCena = 1.5
SulaPVN = PVN * SulasCena


sieraCena = 3
sieraPVN = sieraCena * PVN


Kopejacena = sieraCena + SulasCena + SulaPVN + sieraPVN

print(Kopejacena)
