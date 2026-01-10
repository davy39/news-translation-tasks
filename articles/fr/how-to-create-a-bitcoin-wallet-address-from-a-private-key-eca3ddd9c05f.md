---
title: Comment créer une adresse de portefeuille Bitcoin à partir d'une clé privée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T15:35:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-bitcoin-wallet-address-from-a-private-key-eca3ddd9c05f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yrGW1KubP_JKLR1CVg074g.png
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
seo_title: Comment créer une adresse de portefeuille Bitcoin à partir d'une clé privée
seo_desc: 'By Timur Badretdinov

  In the previous article, we looked at different methods to generate a private key.
  Whatever method you choose, you’ll end up with 32 bytes of data. Here’s the one
  that we got at the end of that article:

  60cf347dbc59d31c1358c8e5cf...'
---

Par Timur Badretdinov

Dans [l'article précédent](https://www.freecodecamp.org/news/how-to-generate-your-very-own-bitcoin-private-key-7ad0f4936e6c/), nous avons examiné différentes méthodes pour générer une clé privée. Quelle que soit la méthode que vous choisissez, vous finirez avec 32 octets de données. Voici celle que nous avons obtenue à la fin de cet article :

`60cf347dbc59d31c1358c8e5cf5e45b822ab85b79cb32a9f3d98184779a9efc2`

Nous utiliserons cette clé privée tout au long de l'article pour dériver à la fois une clé publique et l'adresse pour le portefeuille Bitcoin.

Ce que nous voulons faire, c'est appliquer une série de conversions à la clé privée pour obtenir une clé publique et ensuite une adresse de portefeuille. La plupart de ces conversions sont appelées fonctions de hachage. Ces fonctions de hachage sont des conversions à sens unique qui ne peuvent pas être inversées. Nous n'entrerons pas dans les mécanismes des fonctions elles-mêmes — il existe de nombreux articles qui couvrent cela. Au lieu de cela, nous examinerons comment l'utilisation de ces fonctions dans le bon ordre peut vous mener à l'adresse de portefeuille Bitcoin que vous pouvez utiliser.

### Cryptographie à Courbe Elliptique

La première chose que nous devons faire est d'appliquer l'ECDSA ou Elliptic Curve Digital Signature Algorithm à notre clé privée. Une courbe elliptique est une courbe définie par l'équation `y² = x³ + ax + b` avec un `a` et un `b` choisis. Il existe toute une famille de telles courbes qui sont largement connues et utilisées. Bitcoin utilise la courbe **secp256k1**. Si vous souhaitez en savoir plus sur la cryptographie à courbe elliptique, je vous renvoie à [cet article](https://hackernoon.com/what-is-the-math-behind-elliptic-curve-cryptography-f61b25253da3).

En appliquant l'ECDSA à la clé privée, nous obtenons un entier de 64 octets. Cela consiste en deux entiers de 32 octets qui représentent les coordonnées X et Y du point sur la courbe elliptique, concaténés ensemble.

Pour notre exemple, nous avons obtenu : `1e7bcc70c72770dbb72fea022e8a6d07f814d2ebe4de9ae3f7af75bf706902a7b73ff919898c836396a6b0c96812c3213b99372050853bd1678da0ead14487d7`.

En Python, cela ressemblerait à ceci :

```python
public_key_bytes = codecs.decode(public_key, 'hex')
# Exécuter SHA-256 pour la clé publique
sha256_bpk = hashlib.sha256(public_key_bytes)
sha256_bpk_digest = sha256_bpk.digest()
# Exécuter RIPEMD-160 pour le SHA-256
ripemd160_bpk = hashlib.new('ripemd160')
ripemd160_bpk.update(sha256_bpk_digest)
ripemd160_bpk_digest = ripemd160_bpk.digest()
ripemd160_bpk_hex = codecs.encode(ripemd160_bpk_digest, 'hex')
```

Note : comme vous pouvez le voir dans le code, avant d'utiliser une méthode du module `ecdsa`, j'ai décodé la clé privée en utilisant `codecs`. Cela est plus pertinent pour Python et moins pour l'algorithme lui-même, mais je vais expliquer ce que nous faisons ici pour éviter toute confusion.

En Python, il existe au moins deux classes qui peuvent conserver les clés privées et publiques : "str" et "bytes". La première est une chaîne de caractères et la seconde est un tableau d'octets. Les méthodes cryptographiques en Python fonctionnent avec la classe "bytes", en la prenant comme entrée et en la retournant comme résultat.

Maintenant, il y a un petit piège : une chaîne de caractères, par exemple, `4f3c` n'est pas égale au tableau d'octets `4f3c`, elle est égale au tableau d'octets avec deux éléments, `O<`. Et c'est ce que fait la méthode `codecs.decode` : elle convertit une chaîne de caractères en un tableau d'octets. Cela sera le même pour toutes les manipulations cryptographiques que nous ferons dans cet article.

### Clé publique

Une fois que nous avons terminé avec l'ECDSA, tout ce que nous devons faire est d'ajouter les octets `0x04` au début de notre clé publique. Le résultat est une clé publique complète de Bitcoin, qui est égale à : `041e7bcc70c72770dbb72fea022e8a6d07f814d2ebe4de9ae3f7af75bf706902a7b73ff919898c836396a6b0c96812c3213b99372050853bd1678da0ead14487d7` pour nous.

### Clé publique compressée

Mais nous pouvons faire mieux. Comme vous vous en souvenez peut-être, la clé publique est un point (X, Y) sur la courbe. Nous connaissons la courbe, et pour chaque X, il n'y a que deux Y qui définissent le point qui se trouve sur cette courbe. Alors pourquoi garder Y ? Au lieu de cela, gardons X et le signe de Y. Plus tard, nous pouvons dériver Y à partir de cela si nécessaire.

Les détails sont les suivants : nous prenons X de la clé publique ECDSA. Maintenant, nous ajoutons `0x02` si le dernier octet de Y est pair, et l'octet `0x03` si le dernier octet est impair.

Dans notre cas, le dernier octet est impair, donc nous ajoutons `0x03` pour obtenir la clé publique compressée : `031e7bcc70c72770dbb72fea022e8a6d07f814d2ebe4de9ae3f7af75bf706902a7`. Cette clé contient les mêmes informations, mais elle est presque deux fois plus courte que la clé non compressée. Cool !

Auparavant, les logiciels de portefeuille utilisaient des versions longues et complètes des clés publiques, mais maintenant, la plupart d'entre eux sont passés aux clés compressées.

### Chiffrement de la clé publique

À partir de maintenant, nous devons créer une adresse de portefeuille. Quelle que soit la méthode d'obtention de la clé publique que vous choisissez, elle passe par la même procédure. Évidemment, les adresses seront différentes. Dans cet article, nous utiliserons la version compressée.

Ce que nous devons faire ici, c'est appliquer SHA-256 à la clé publique, puis appliquer RIPEMD-160 au résultat. L'ordre est important.

SHA-256 et RIPEMD-160 sont deux fonctions de hachage, et encore une fois, nous n'entrerons pas dans les détails de leur fonctionnement. Ce qui compte, c'est que nous avons maintenant un entier de 160 bits, qui sera utilisé pour des modifications ultérieures. Appelons cela une clé publique chiffrée. Pour notre exemple, la clé publique chiffrée est `453233600a96384bb8d73d400984117ac84d7e8b`.

![Image](https://cdn-media-1.freecodecamp.org/images/9Fj7FyUVc7zLwLodE7JvoHXfY81g6DndArUd)

Voici comment nous chiffrons la clé publique en Python :

```
public_key_bytes = codecs.decode(public_key, 'hex')# Exécuter SHA-256 pour la clé publiquesha256_bpk = hashlib.sha256(public_key_bytes)sha256_bpk_digest = sha256_bpk.digest()# Exécuter RIPEMD-160 pour le SHA-256ripemd160_bpk = hashlib.new('ripemd160')ripemd160_bpk.update(sha256_bpk_digest)ripemd160_bpk_digest = ripemd160_bpk.digest()ripemd160_bpk_hex = codecs.encode(ripemd160_bpk_digest, 'hex')
```

### Ajout de l'octet de réseau

Bitcoin a deux réseaux, main et test. Le réseau principal est celui que toutes les personnes utilisent pour transférer les pièces. Le réseau de test a été créé — vous l'avez deviné — pour tester de nouvelles fonctionnalités et logiciels.

Nous voulons générer une adresse pour l'utiliser sur le mainnet, donc nous devons ajouter les octets `0x00` à la clé publique chiffrée. Le résultat est `00453233600a96384bb8d73d400984117ac84d7e8b`. Pour le testnet, ce serait les octets `0x6f`.

### Somme de contrôle

Maintenant, nous devons calculer la somme de contrôle de notre clé mainnet. L'idée de la somme de contrôle est de s'assurer que les données (dans notre cas, la clé) n'ont pas été corrompues pendant la transmission. Le logiciel de portefeuille doit vérifier la somme de contrôle et marquer l'adresse comme invalide si la somme de contrôle ne correspond pas.

Pour calculer la somme de contrôle de la clé, nous devons appliquer SHA-256 deux fois, puis prendre les 4 premiers octets du résultat. Pour notre exemple, le double SHA-256 est `512f43c48517a75e58a7ec4c554ecd1a8f9603c891b46325006abf39c5c6b995` et donc la somme de contrôle est `512f43c4` (notez que 4 octets correspondent à 8 chiffres hexadécimaux).

![Image](https://cdn-media-1.freecodecamp.org/images/rcb40Z2plVojizglRqDG3Y4fIxy1m77Gsnnu)

Le code pour calculer une somme de contrôle d'adresse est le suivant :

```python
# Double SHA256 pour obtenir la somme de contrôle
sha256_nbpk = hashlib.sha256(network_bitcoin_public_key_bytes)
sha256_nbpk_digest = sha256_nbpk.digest()
sha256_2_nbpk = hashlib.sha256(sha256_nbpk_digest)
sha256_2_nbpk_digest = sha256_2_nbpk.digest()
sha256_2_hex = codecs.encode(sha256_2_nbpk_digest, 'hex')
checksum = sha256_2_hex[:8]
```

### Obtention de l'adresse

Enfin, pour créer une adresse, nous concaténons simplement la clé mainnet et la somme de contrôle. Cela donne `00453233600a96384bb8d73d400984117ac84d7e8b512f43c4` pour notre exemple.

C'est tout ! C'est l'adresse de portefeuille pour la clé privée au début de l'article.

Mais vous pouvez remarquer que quelque chose ne va pas. Vous avez probablement vu quelques adresses Bitcoin et elles ne ressemblaient pas à cela. Eh bien, la raison est qu'elles sont encodées avec [Base58](https://en.wikipedia.org/wiki/Base58). C'est un peu étrange.

Voici l'algorithme pour convertir une adresse hexadécimale en adresse Base58 :

```python
def base58(address_hex):
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    b58_string = ''
    # Obtenir le nombre de zéros de tête
    leading_zeros = len(address_hex) - len(address_hex.lstrip('0'))
    # Convertir hex en décimal
    address_int = int(address_hex, 16)
    # Ajouter des chiffres au début de la chaîne
    while address_int > 0:
        digit = address_int % 58
        digit_char = alphabet[digit]
        b58_string = digit_char + b58_string
        address_int //= 58
    # Ajouter '1' pour chaque 2 zéros de tête
    ones = leading_zeros // 2
    for one in range(ones):
        b58_string = '1' + b58_string
    return b58_string
```

Ce que nous obtenons est `17JsmEygbbEUEpvt4PFtYaTeSqfb9ki1F1`, une adresse de portefeuille Bitcoin compressée.

![Image](https://cdn-media-1.freecodecamp.org/images/saUvqNSzw5b7ATtpSh3RUMS3WwEeBFVNU9m8)

### Conclusion

Le processus de génération de la clé de portefeuille peut être divisé en quatre étapes :

* création d'une clé publique avec ECDSA
* chiffrement de la clé avec SHA-256 et RIPEMD-160
* calcul de la somme de contrôle avec double SHA-256
* encodage de la clé avec Base58.

Selon la forme de la clé publique (complète ou compressée), nous obtenons différentes adresses, mais les deux sont parfaitement valides.

Voici l'algorithme complet pour la clé publique non compressée :

![Image](https://cdn-media-1.freecodecamp.org/images/r1G799LERTJzPvyfibbkVdRpJDzMbgPRbmmu)

Si vous voulez jouer avec le code, je l'ai publié dans le [dépôt Github](https://github.com/Destiner/blocksmith).

Je crée un cours sur les cryptomonnaies ici sur freeCodeCamp News. La [première partie](https://medium.com/longcaller/blockchain-explained-2b26b28657ca) est une description détaillée de la blockchain.

Je publie également des pensées aléatoires sur la crypto sur [Twitter](https://twitter.com/DestinerX), alors vous pourriez vouloir y jeter un coup d'œil.