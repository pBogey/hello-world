"""
Normalization
08.08.2019
Bogdan Prădatu
"""

print("\n********** Unicode Normalization **********\n")

s1 = "café"
s2 = "cafe\u0301"
print("s1:",s1,"\ns2:",s2)
print("s1 == s2:", s1==s2)
print("len(s1):",len(s1),"\nlen(s2):",len(s2))

from unicodedata import normalize

## the first argument for normalize can be: NFC, NFD, NFKC, NFKD
## Normalization Form C (NFC) composes the code points to produce the shortest
## equivalent string, while NFD decomposes, expanding composed characters
## into base characters and separate combining characters
print("\t****** Normalize NFC *****")
## Western keyboards usually generate composed characters,
## so text typed by users will be in NFC by default
print("s1 NFC form:",normalize('NFC',s1),"\tlen(s1):",len(normalize('NFC',s1)))
print("s2 NFC form:",normalize('NFC',s2),"\tlen(s2):",len(normalize('NFC',s2)))
print("\t****** Normalize NFD *****")
print("s1 NFD form:",normalize('NFD',s1),"\tlen(s1):",len(normalize('NFD',s1)))
print("s2 NFD form:",normalize('NFD',s2),"\tlen(s2):",len(normalize('NFD',s2)))
print("\t****** Normalize NFKC *****")
print("s1 NFKC form:",normalize('NFKC',s1),"\tlen(s1):",len(normalize('NFKC',s1)))
print("s2 NFKC form:",normalize('NFKC',s2),"\tlen(s2):",len(normalize('NFKC',s2)))
print("\t****** Normalize NFKD *****")
print("s1 NFKD form:",normalize('NFKD',s1),"\tlen(s1):",len(normalize('NFKD',s1)))
print("s2 NFKD form:",normalize('NFKD',s2),"\tlen(s2):",len(normalize('NFKD',s2)))

## NFKC and NFKD—the letter K stands for “compatibility.” These are stronger
## forms of normalization, affecting the so-called “compatibility characters.”
## Although one goal of Unicode is to have a single “canonical” code point for
## each character, some characters appear more than once for compatibility
## with preexisting standards.
print("\n\t****** Compatibility ****** \n")
from unicodedata import name
micro = "\u00b5"
mu = "\u03bc"
print("micro:",micro,"\tname:",name(micro),"\nmu:",mu,"\t\tname:",name(mu))
print("micro == mu:", micro == mu)
print("micro(NFKC):",normalize('NFKC',micro))
print("mu(NFKC):",normalize('NFKC',mu))
print("micro(NFC) == mu(NFC)",normalize('NFC',micro)==normalize('NFC',mu))
print("micro(NFKC) == mu(NFKC)",normalize('NFKC',micro)==normalize('NFKC',mu))

## NFKC and NFKD normalization should be applied with care and
## only in special cases—e.g., search and indexing—and not for permanent
## storage, because these transformations cause data loss.

print("\n\t**********\t\n")
ohm = "\u2126"
omega = normalize('NFC',ohm)

print("ohm:", ohm,"\nomega:",omega)
print("ohm == omega:",ohm==omega)
print("name(ohm):",name(ohm))
print("name(omega):",name(omega))

print("\n\t ***** Case Folding *****\n")
## Case folding is essentially converting all text to lowercase,
## with some additional transformations.
micro_c = micro.casefold()
mu_c = micro.casefold()
print("micro:",micro,"\tname:",name(micro),"\nmu:",mu,"\t\tname:",name(mu))
print("micro_c:",micro_c,"\tname:",name(micro_c),
      "\nmu_c:",mu_c,"\tname:",name(mu_c))
print("micro_c == mu_c:",micro_c==mu_c)
