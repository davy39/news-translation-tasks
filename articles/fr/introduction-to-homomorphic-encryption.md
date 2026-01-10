---
title: Qu'est-ce que le chiffrement homomorphe ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-26T23:01:28.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-homomorphic-encryption
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Homomorphic-Encryption-3--1.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: encryption
  slug: encryption
seo_title: Qu'est-ce que le chiffrement homomorphe ?
seo_desc: "By Aris Zagakos\nIn this article we will discuss Homomorphic Encryption,\
  \ the problem that it solves, and the different types that exist. \nThen we will\
  \ write code in Python to show some of its capabilities in action.\nHere's what\
  \ we'll cover:\n\nWhat is H..."
---

Par Aris Zagakos

Dans cet article, nous allons discuter du chiffrement homomorphe, du problème qu'il résout et des différents types qui existent. 

Ensuite, nous allons écrire du code en Python pour montrer certaines de ses capacités en action.

## Voici ce que nous allons couvrir :

1. Qu'est-ce que le chiffrement homomorphe ?
2. Avantages du chiffrement homomorphe
3. Types de chiffrement homomorphe
4. Système cryptographique de Paillier
5. Conclusion et ressources pour en savoir plus

## Qu'est-ce que le chiffrement homomorphe ?

Le nom Homomorphe vient du terme algébrique Homomorphisme.

> "L'homomorphisme est une application qui préserve la structure entre deux structures algébriques de même type (comme deux groupes, deux anneaux ou deux espaces vectoriels)." (Source : Wikipedia<ins>)</ins>

Le `chiffrement homomorphe` est une forme de chiffrement qui permet aux utilisateurs d'effectuer des opérations binaires sur des données chiffrées sans jamais déchiffrer les données. 

Cette forme de chiffrement permet aux informations d'être chiffrées et externalisées vers des services/environnements cloud pour traitement, sans accéder aux données brutes.

## Avantages du chiffrement homomorphe

Dans le monde d'aujourd'hui, si nous voulons effectuer des calculs sur des données chiffrées telles que des opérations mathématiques, nous devons d'abord les déchiffrer. Ensuite, nous devons effectuer nos calculs, et enfin chiffrer à nouveau les données afin de les renvoyer.

Mais que se passe-t-il lorsque les données chiffrées sont très sensibles et que nous ne voulons pas que d'autres services y aient accès ? C'est là que le `chiffrement homomorphe` entre en jeu.

Un exemple plus pratique serait un système/service qui traite des informations médicales afin de diagnostiquer si un patient a une condition ou non.

Les données que nous partagerions incluent probablement des informations très sensibles sur les antécédents médicaux du patient. Il est donc important de s'assurer qu'elles ne seront pas accessibles à quiconque.

En utilisant le `chiffrement homomorphe`, le système/service peut effectuer les calculs nécessaires sur les données chiffrées, retournant le résultat du diagnostic sans connaître les informations traitées.

Le partage d'informations sensibles à travers différentes plateformes compromet notre vie privée. D'un autre côté, pouvoir modifier et effectuer des opérations sur des données tout en les gardant chiffrées assure la confidentialité des données.

## Types de chiffrement homomorphe

L'objectif du chiffrement homomorphe est le suivant : étant donné une entrée quelconque telle que `input := Enc(x1),...,Enc(xn)`, pour toute fonction arbitraire `f` qui applique un nombre infini d'additions ou de multiplications telles que `value := f(Enc(x1),...,Enc(xn))`, la valeur peut être calculée tandis que l'entrée est chiffrée.

Les opérations arithmétiques, à la fin de la journée, sont implémentées au niveau matériel (comme tout le reste) sous forme de circuits arithmétiques ou booléens. 

Les opérations que nous voulons effectuer sont l'addition homomorphe et la multiplication homomorphe. Les noms Addition et Multiplication sont donnés en raison du comportement similaire de l'addition binaire et de la multiplication binaire que les portes logiques XOR et AND ont respectivement. La combinaison de ces deux portes peut représenter toute fonction booléenne.

Les facteurs rendent la complexité variable en fonction du nombre et du type d'opérations.

En raison de ces restrictions et du problème de construction d'un algorithme de chiffrement entièrement homomorphe (prenant en charge à la fois l'addition homomorphe et la multiplication homomorphe), différentes méthodes ont été implémentées au fil du temps.

Les types les plus courants de chiffrement homomorphe sont :

* Chiffrement partiellement homomorphe (PHE)
* Chiffrement quelque peu homomorphe (SHE)
* Chiffrement entièrement homomorphe (FHE)

Le chiffrement partiellement homomorphe (PHE) permet de n'effectuer qu'une seule opération sur le texte chiffré un nombre infini de fois. Cette opération peut être uniquement l'addition ou uniquement la multiplication. 

Les algorithmes de chiffrement partiellement homomorphe sont plus faciles à concevoir et sont très utiles dans les applications qui utilisent une seule opération arithmétique.

Le chiffrement quelque peu homomorphe (SHE) permet d'effectuer à la fois l'addition et la multiplication, mais pour un nombre limité de fois. Cette limitation est évaluée à une certaine profondeur dans la logique du circuit. C'est une étape très importante pour atteindre le chiffrement entièrement homomorphe.

Le chiffrement entièrement homomorphe (FHE) permet d'effectuer à la fois l'addition et la multiplication sur le texte chiffré un nombre infini de fois, prenant en charge des calculs arbitraires sur des données chiffrées. 

Le principal problème avec le chiffrement entièrement homomorphe est le coût en termes d'efficacité, à la fois en termes de vitesse et d'exigences de stockage par rapport aux opérations en texte clair.

## Système cryptographique de Paillier

Le système cryptographique de Paillier a été inventé par Pascal Paillier en 1999. Il s'agit d'un schéma de chiffrement partiellement homomorphe (PHE) et additivement homomorphe. 

Il ne prend en charge que l'addition de deux textes chiffrés et non la multiplication entre eux. De plus, un nombre en texte clair peut être ajouté ou multiplié au texte chiffré.

Dans cet exemple, nous utilisons `python-paillier`, une bibliothèque Python pour le chiffrement partiellement homomorphe utilisant le système cryptographique de Paillier.

```python
from phe import paillier

num1 = 10
num2 = 20

pub_key, priv_key = paillier.generate_paillier_keypair()
cipher_num1, cipher_num2 = pub_key.encrypt(num1), pub_key.encrypt(num2)

# additionner deux nombres chiffrés ensemble
result = cipher_num1 + cipher_num2
result = priv_key.decrypt(result)
print("additionner deux nombres chiffrés ensemble :",result)

# ajouter un nombre chiffré à un nombre en texte clair
result = cipher_num1 + 5
result = priv_key.decrypt(result)
print("ajouter un nombre chiffré à un nombre :",result)

# multiplier un nombre chiffré par un nombre en texte clair
result = cipher_num1 * 10
result = priv_key.decrypt(result)
print("multiplier un nombre chiffré par un nombre :",result)

```

Dans l'exemple ci-dessus, nous avons généré une paire de clés, une clé publique et une clé privée. Ensuite, nous avons chiffré `num1` et `num2` avec la clé publique et effectué des opérations sur leurs textes chiffrés.

Tout d'abord, nous avons additionné les deux chiffres. Après cela, nous avons pris `cipher_num1` et ajouté un nombre en texte clair. Enfin, nous avons fait le même processus qu'avant, mais au lieu de l'addition, nous avons multiplié `cipher_num1` par un nombre en texte clair cette fois.

Le calcul de ces opérations a lieu tandis que les données sont chiffrées. De plus, nous pouvons vérifier l'intégrité du résultat à chaque fois en le déchiffrant à l'aide de la clé privée.

## Conclusion

Le chiffrement homomorphe (HE) semble être un rêve en matière de confidentialité et de protection des données. Mais ses performances médiocres et ses coûts élevés le maintiennent encore hors des applications commerciales/de production. 

Cependant, il y a eu de nombreuses améliorations en termes de vitesse ces derniers temps. Avec le rythme actuel, je crois qu'il sera adopté dans le monde entier au cours des prochaines années.

### Ressources

* [Homomorphisme](https://en.wikipedia.org/wiki/Homomorphism)
* [Chiffrement homomorphe](https://en.wikipedia.org/wiki/Homomorphic_encryption)
* [Système cryptographique de Paillier](https://en.wikipedia.org/wiki/Paillier_cryptosystem)
* [python-paillier](https://python-paillier.readthedocs.io/en/develop/)