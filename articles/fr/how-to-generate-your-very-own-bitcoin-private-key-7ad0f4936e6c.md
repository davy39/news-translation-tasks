---
title: Comment générer votre propre clé privée Bitcoin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-29T00:40:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-your-very-own-bitcoin-private-key-7ad0f4936e6c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6pWGbFF9kCmlGSra6Kmh-w.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: Cryptocurrency
  slug: cryptocurrency
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Comment générer votre propre clé privée Bitcoin
seo_desc: 'By Timur Badretdinov

  In cryptocurrencies, a private key allows a user to gain access to their wallet.
  The person who holds the private key fully controls the coins in that wallet. For
  this reason, you should keep it secret. And if you really want to ...'
---

Par Timur Badretdinov

Dans les cryptomonnaies, une clé privée permet à un utilisateur d'accéder à son portefeuille. La personne qui détient la clé privée contrôle pleinement les pièces dans ce portefeuille. Pour cette raison, vous devez la garder secrète. Et si vous souhaitez vraiment générer la clé vous-même, il est judicieux de le faire de manière sécurisée.

Ici, je vais fournir une introduction aux clés privées et vous montrer comment vous pouvez générer votre propre clé en utilisant diverses fonctions cryptographiques. Je vais fournir une description de l'algorithme et du code en Python.

### Dois-je générer une clé privée ?

La plupart du temps, vous n'en avez pas besoin. Par exemple, si vous utilisez un portefeuille web comme Coinbase ou Blockchain.info, ils créent et gèrent la clé privée pour vous. Il en va de même pour les exchanges.

Les portefeuilles mobiles et de bureau génèrent généralement également une clé privée pour vous, bien qu'ils puissent avoir l'option de créer un portefeuille à partir de votre propre clé privée.

Alors pourquoi la générer quand même ? Voici les raisons que j'ai :

* Vous voulez vous assurer que personne ne connaît la clé
* Vous voulez simplement en apprendre davantage sur la cryptographie et la génération de nombres aléatoires (RNG)

### Qu'est-ce qu'une clé privée exactement ?

Formellement, une clé privée pour Bitcoin (et de nombreuses autres cryptomonnaies) est une série de 32 octets. Maintenant, il existe de nombreuses façons d'enregistrer ces octets. Cela peut être une chaîne de 256 uns et zéros (32 * 8 = 256) ou 100 lancers de dés. Cela peut être une chaîne binaire, une chaîne Base64, une [clé WIF](https://en.bitcoin.it/wiki/Wallet_import_format), une [phrase mnémonique](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), ou enfin, une chaîne hexadécimale. Pour nos besoins, nous utiliserons une chaîne hexadécimale de 64 caractères.

![Image](https://cdn-media-1.freecodecamp.org/images/lyrhBKkIKdFsCCrBdSXnaRYJrwj67NUaMXNy)
_La même clé privée, écrite dans différents formats._

Pourquoi exactement 32 octets ? Excellente question ! Vous voyez, pour créer une clé publique à partir d'une clé privée, Bitcoin utilise l'**ECDSA**, ou Elliptic Curve Digital Signature Algorithm. Plus précisément, il utilise une courbe particulière appelée **secp256k1**.

Maintenant, cette courbe a un ordre de 256 bits, prend 256 bits en entrée et produit des entiers de 256 bits. Et 256 bits est exactement 32 octets. Donc, en d'autres termes, nous avons besoin de 32 octets de données pour alimenter cet algorithme de courbe.

Il y a une exigence supplémentaire pour la clé privée. Parce que nous utilisons ECDSA, la clé doit être positive et doit être inférieure à l'ordre de la courbe. L'ordre de secp256k1 est `FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141`, qui est assez grand : presque n'importe quel nombre de 32 octets sera plus petit que lui.

### Méthode naïve

Alors, comment générer un entier de 32 octets ? La première chose qui vient à l'esprit est d'utiliser une bibliothèque RNG dans votre langage de choix. Python fournit même une manière mignonne de générer juste assez de bits :

```python
import random
bits = random.getrandbits(256)
# 30848827712021293731208415302456569301499384654877289245795786476741155372082
bits_hex = hex(bits)
# 0x4433d156e8c53bf5b50af07aa95a29436f29a94e0ccc5d58df8e57bdc8583c32
private_key = bits_hex[2:]
# 4433d156e8c53bf5b50af07aa95a29436f29a94e0ccc5d58df8e57bdc8583c32
```

Cela semble bien, mais en réalité, ce n'est pas le cas. Vous voyez, les bibliothèques RNG normales ne sont pas destinées à la cryptographie, car elles ne sont pas très sécurisées. Elles génèrent des nombres basés sur une graine, et par défaut, la graine est l'heure actuelle. Ainsi, si vous savez approximativement quand j'ai généré les bits ci-dessus, tout ce que vous avez à faire est de forcer brutalement quelques variantes.

Lorsque vous générez une clé privée, vous voulez être extrêmement sécurisé. Rappelez-vous, si quelqu'un apprend la clé privée, il peut facilement voler toutes les pièces du portefeuille correspondant, et vous n'avez aucune chance de les récupérer.

Alors essayons de le faire de manière plus sécurisée.

### RNG cryptographiquement fort

En plus d'une méthode RNG standard, les langages de programmation fournissent généralement un RNG spécialement conçu pour les opérations cryptographiques. Cette méthode est généralement beaucoup plus sécurisée, car elle tire son entropie directement du système d'exploitation. Le résultat d'un tel RNG est beaucoup plus difficile à reproduire. Vous ne pouvez pas le faire en connaissant l'heure de génération ou en ayant la graine, car il n'y a pas de graine. Eh bien, au moins l'utilisateur n'entre pas de graine — plutôt, elle est créée par le programme.

En Python, le RNG cryptographiquement fort est implémenté dans le module `secrets`. Modifions le code ci-dessus pour rendre la génération de la clé privée sécurisée !

```python
import secrets
bits = secrets.randbits(256)
# 46518555179467323509970270980993648640987722172281263586388328188640792550961
bits_hex = hex(bits)
# 0x66d891b5ed7f51e5044be6a7ebe4e2eae32b960f5aa0883f7cc0ce4fd6921e31
private_key = bits_hex[2:]
# 66d891b5ed7f51e5044be6a7ebe4e2eae32b960f5aa0883f7cc0ce4fd6921e31
```

C'est incroyable. Je parie que vous ne pourriez pas reproduire cela, même avec accès à mon PC. Mais pouvons-nous aller plus loin ?

### Sites spécialisés

Il existe des sites qui génèrent des nombres aléatoires pour vous. Nous allons en considérer deux ici. L'un est [random.org](https://random.org), un générateur de nombres aléatoires à usage général bien connu. Un autre est [bitaddress.org](https://bitaddress.org), qui est conçu spécifiquement pour la génération de clés privées Bitcoin.

[random.org](https://random.org) peut-il nous aider à générer une clé ? Définitivement, car ils ont un [service](https://www.random.org/bytes) pour générer des octets aléatoires. Mais deux problèmes se posent ici. [Random.org](https://random.org) prétend être un générateur vraiment aléatoire, mais pouvez-vous lui faire confiance ? Pouvez-vous être sûr qu'il est vraiment aléatoire ? Pouvez-vous être sûr que le propriétaire n'enregistre pas tous les résultats de génération, surtout ceux qui ressemblent à des clés privées ? La réponse vous appartient. Oh, et vous ne pouvez pas l'exécuter localement, ce qui est un problème supplémentaire. Cette méthode n'est pas sécurisée à 100 %.

Maintenant, [bitaddress.org](https://bitaddress.org) est une toute autre histoire. Il est open source, donc vous pouvez voir ce qu'il y a sous le capot. Il est côté client, donc vous pouvez le télécharger et l'exécuter localement, même sans connexion Internet.

Alors, comment cela fonctionne-t-il ? Il vous utilise — oui, vous — comme source d'entropie. Il vous demande de déplacer votre souris ou de presser des touches aléatoires. Vous le faites assez longtemps pour rendre la reproduction des résultats infaisable.

![Image](https://cdn-media-1.freecodecamp.org/images/y5eDywvm3A2NMywdEk2u6pQYUORSP42gtWr2)
_Le processus de génération d'entropie en déplaçant la souris de manière aléatoire. Le grand bloc de symboles montre le pool._

Êtes-vous intéressé à voir comment [bitaddress.org](https://bitaddress.org) fonctionne ? À des fins éducatives, nous allons examiner son code et essayer de le reproduire en Python.

> _Note rapide : bitaddress.org vous donne la clé privée au format WIF compressé, qui est proche du [format WIF](https://en.bitcoin.it/wiki/Wallet_import_format) dont nous avons parlé auparavant. Pour nos besoins, nous allons faire en sorte que l'algorithme retourne une chaîne hexadécimale afin que nous puissions l'utiliser plus tard pour la génération d'une clé publique._

### Bitaddress : les spécificités

Bitaddress crée l'entropie sous deux formes : par le mouvement de la souris et par la pression des touches. Nous parlerons des deux, mais nous nous concentrerons sur les pressions de touches, car il est difficile d'implémenter le suivi de la souris dans la bibliothèque Python. Nous nous attendons à ce que l'utilisateur final tape des boutons jusqu'à ce que nous ayons assez d'entropie, puis nous générerons une clé.

Bitaddress fait trois choses. Il initialise un tableau d'octets, en essayant d'obtenir autant d'entropie que possible de votre ordinateur, il remplit le tableau avec l'entrée de l'utilisateur, puis il génère une clé privée.

Bitaddress utilise un tableau de 256 octets pour stocker l'entropie. Ce tableau est réécrit en cycles, donc lorsque le tableau est rempli pour la première fois, le pointeur revient à zéro, et le processus de remplissage recommence.

Le programme initialise un tableau avec 256 octets de [window.crypto](https://developer.mozilla.org/en-US/docs/Web/API/Window/crypto). Ensuite, il écrit un horodatage pour obtenir 4 octets supplémentaires d'entropie. Enfin, il obtient des données telles que la taille de l'écran, votre fuseau horaire, des informations sur les plugins du navigateur, votre locale, et plus encore. Cela lui donne 6 octets supplémentaires.

Après l'initialisation, le programme attend continuellement l'entrée de l'utilisateur pour réécrire les octets initiaux. Lorsque l'utilisateur déplace le curseur, le programme écrit la position du curseur. Lorsque l'utilisateur presse des boutons, le programme écrit le code du caractère du bouton pressé.

Enfin, bitaddress utilise l'entropie accumulée pour générer une clé privée. Il doit générer 32 octets. Pour cette tâche, bitaddress utilise un algorithme RNG appelé ARC4. Le programme initialise ARC4 avec l'heure actuelle et l'entropie collectée, puis obtient les octets un par un 32 fois.

Ceci est une simplification excessive de la manière dont le programme fonctionne, mais j'espère que vous comprenez l'idée. Vous pouvez consulter l'algorithme en détail sur [Github](https://github.com/pointbiz/bitaddress.org).

### Le faire vous-même

Pour nos besoins, nous allons construire une version plus simple de bitaddress. Premièrement, nous ne collecterons pas de données sur la machine et la localisation de l'utilisateur. Deuxièmement, nous entrerons l'entropie uniquement via du texte, car il est assez difficile de recevoir continuellement la position de la souris avec un script Python (consultez [PyAutoGUI](https://github.com/asweigart/pyautogui) si vous voulez le faire).

Cela nous amène à la spécification formelle de notre bibliothèque de générateur. Premièrement, elle initialisera un tableau d'octets avec un RNG cryptographique, puis elle remplira l'horodatage, et enfin elle remplira la chaîne créée par l'utilisateur. Après que le pool de graines soit rempli, la bibliothèque permettra au développeur de créer une clé. En fait, ils pourront créer autant de clés privées qu'ils le souhaitent, toutes sécurisées par l'entropie collectée.

#### Initialisation du pool

Ici, nous plaçons quelques octets d'un RNG cryptographique et un horodatage. `__seed_int` et `__seed_byte` sont deux méthodes auxiliaires qui insèrent l'entropie dans notre tableau de pool. Remarquez que nous utilisons `secrets`.

```python
def __init_pool(self):
    for i in range(self.POOL_SIZE):
        random_byte = secrets.randbits(8)
        self.__seed_byte(random_byte)
    time_int = int(time.time())
    self.__seed_int(time_int)
def __seed_int(self, n):
    self.__seed_byte(n)
    self.__seed_byte(n >> 8)
    self.__seed_byte(n >> 16)
    self.__seed_byte(n >> 24)
def __seed_byte(self, n):
    self.pool[self.pool_pointer] ^= n & 255
    self.pool_pointer += 1
    if self.pool_pointer >= self.POOL_SIZE:
        self.pool_pointer = 0
```

#### Ensemencement avec l'entrée

Ici, nous plaçons d'abord un horodatage, puis la chaîne d'entrée, caractère par caractère.

```
def seed_input(self, str_input):
    time_int = int(time.time())
    self.__seed_int(time_int)
    for char in str_input:
        char_code = ord(char)
        self.__seed_byte(char_code)
```

#### Génération de la clé privée

Cette partie peut sembler difficile, mais elle est en réalité très simple.

Premièrement, nous devons générer un nombre de 32 octets en utilisant notre pool. Malheureusement, nous ne pouvons pas simplement créer notre propre objet `random` et l'utiliser uniquement pour la génération de clés. Au lieu de cela, il y a un objet partagé qui est utilisé par tout code qui s'exécute dans un script.

Qu'est-ce que cela signifie pour nous ? Cela signifie qu'à tout moment, n'importe où dans le code, un simple `random.seed(0)` peut détruire toute notre entropie collectée. Nous ne voulons pas cela. Heureusement, Python fournit les méthodes `getstate` et `setstate`. Donc, pour sauvegarder notre entropie chaque fois que nous générons une clé, nous nous souvenons de l'état où nous nous sommes arrêtés et nous le définissons la prochaine fois que nous voulons créer une clé.

Deuxièmement, nous nous assurons simplement que notre clé est dans la plage (1, `CURVE_ORDER`). Il s'agit d'une exigence pour toutes les clés privées ECDSA. Le `CURVE_ORDER` est l'ordre de la courbe secp256k1, qui est `FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141`.

Enfin, pour plus de commodité, nous convertissons en hexadécimal et supprimons la partie '0x'.

```python
def generate_key(self):
    big_int = self.__generate_big_int()
    big_int = big_int % (self.CURVE_ORDER - 1) # key < curve order
    big_int = big_int + 1 # key > 0
    key = hex(big_int)[2:]
    return key
def __generate_big_int(self):
    if self.prng_state is None:
    seed = int.from_bytes(self.pool, byteorder='big', signed=False)
    random.seed(seed)
    self.prng_state = random.getstate()
    random.setstate(self.prng_state)
    big_int = random.getrandbits(self.KEY_BYTES * 8)
    self.prng_state = random.getstate()
    return big_int
```

#### En action

Essayons d'utiliser la bibliothèque. En fait, c'est vraiment simple : vous pouvez générer une clé privée en trois lignes de code !

```
kg = KeyGenerator()
kg.seed_input('Truly random string. I rolled a dice and got 4.')
kg.generate_key()
# 60cf347dbc59d31c1358c8e5cf5e45b822ab85b79cb32a9f3d98184779a9efc2
```

Vous pouvez le voir par vous-même. La clé est aléatoire et totalement valide. De plus, chaque fois que vous exécutez ce code, vous obtenez des résultats différents.

### Conclusion

Comme vous pouvez le voir, il existe de nombreuses façons de générer des clés privées. Elles diffèrent en simplicité et en sécurité.

Générer une clé privée n'est qu'une première étape. L'étape suivante consiste à extraire une clé publique et une adresse de portefeuille que vous pouvez utiliser pour recevoir des paiements. Le processus de génération d'un portefeuille diffère pour Bitcoin et Ethereum, et je prévois d'écrire deux autres articles sur ce sujet.

Si vous voulez jouer avec le code, je l'ai publié dans ce [dépôt Github](https://github.com/Destiner/blocksmith).

_Je crée un cours sur les cryptomonnaies ici sur freeCodeCamp News. La [première partie](https://medium.com/longcaller/blockchain-explained-2b26b28657ca) est une description détaillée de la blockchain._

_Je poste également des pensées aléatoires sur la crypto sur [Twitter](https://twitter.com/DestinerX), donc vous pourriez vouloir y jeter un coup d'œil._