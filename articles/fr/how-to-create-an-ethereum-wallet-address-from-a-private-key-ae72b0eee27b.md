---
title: Comment créer une adresse de portefeuille Ethereum à partir d'une clé privée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-31T16:35:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-ethereum-wallet-address-from-a-private-key-ae72b0eee27b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qWiAHdbuyJspr67HahgDYw.png
tags:
- name: Cryptocurrency
  slug: cryptocurrency
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Comment créer une adresse de portefeuille Ethereum à partir d'une clé privée
seo_desc: 'By Timur Badretdinov

  In the first article of this series, we generated a bitcoin private key: 60cf347dbc59d31c1358c8e5cf5e45b822ab85b79cb32a9f3d98184779a9efc2.

  Here, we’ll use that key to get the public address and then the Ethereum wallet
  address of...'
---

Par Timur Badretdinov

Dans [le premier article](https://www.freecodecamp.org/news/how-to-generate-your-very-own-bitcoin-private-key-7ad0f4936e6c/) de cette série, nous avons généré une clé privée bitcoin : `60cf347dbc59d31c1358c8e5cf5e45b822ab85b79cb32a9f3d98184779a9efc2`.

Ici, nous utiliserons cette clé pour obtenir l'adresse publique puis l'adresse du portefeuille Ethereum de cette clé privée.

La création de l'adresse de portefeuille Bitcoin à partir de la clé privée est un peu compliquée. Ici, le processus sera beaucoup plus simple. Nous devons appliquer une fonction de hachage pour obtenir la clé publique et une autre pour obtenir l'adresse.

Alors, commençons.

### Clé publique

Cette partie est presque identique à ce que nous avons discuté dans [l'article sur Bitcoin](https://www.freecodecamp.org/news/how-to-create-a-bitcoin-wallet-address-from-a-private-key-eca3ddd9c05f/), donc si vous l'avez lu, vous pouvez la sauter (sauf si vous avez besoin d'un rappel).

La première chose que nous devons faire est d'appliquer l'ECDSA, ou Elliptic Curve Digital Signature Algorithm, à notre clé privée. Une courbe elliptique est une courbe définie par l'équation `y² = x³ + ax + b` avec des `a` et `b` choisis. Il existe toute une famille de telles courbes qui sont largement connues et utilisées. Bitcoin utilise la courbe **secp256k1**. Si vous souhaitez en savoir plus sur la cryptographie à courbe elliptique, je vous renvoie à [cet article](https://hackernoon.com/what-is-the-math-behind-elliptic-curve-cryptography-f61b25253da3).

Ethereum utilise la même courbe elliptique, **secp256k1**, donc le processus pour obtenir la clé publique est identique dans les deux cryptomonnaies.

En appliquant l'ECDSA à la clé privée, nous obtenons un entier de 64 octets, qui est deux entiers de 32 octets représentant X et Y du point sur la courbe elliptique, concatenés ensemble.

Pour notre exemple, nous avons obtenu `1e7bcc70c72770dbb72fea022e8a6d07f814d2ebe4de9ae3f7af75bf706902a7b73ff919898c836396a6b0c96812c3213b99372050853bd1678da0ead14487d7`.

En Python, cela ressemblerait à ceci :

```python
private_key_bytes = codecs.decode(private_key, 'hex')
# Obtenir la clé publique ECDSA
key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
key_bytes = key.to_string()
key_hex = codecs.encode(key_bytes, 'hex')
```

Remarque : comme vous pouvez le voir dans le code ci-dessus, j'ai utilisé une méthode du module `ecdsa` et j'ai décodé la clé privée en utilisant `codecs`. Cela est plus pertinent pour Python et moins pour l'algorithme lui-même, mais je vais expliquer ce que nous faisons ici pour éviter toute confusion.

En Python, il existe au moins deux classes qui peuvent contenir les clés privées et publiques : "str" et "bytes". La première est une chaîne de caractères et la seconde est un tableau d'octets. Les méthodes cryptographiques en Python fonctionnent avec la classe "bytes", en la prenant comme entrée et en la retournant comme résultat.

Maintenant, il y a un petit piège : une chaîne de caractères, par exemple, `4f3c` n'est pas égale au tableau d'octets `4f3c`. Elle est plutôt égale au tableau d'octets avec deux éléments, `O<`. Et c'est ce que fait la méthode `codecs.decode` : elle convertit une chaîne de caractères en un tableau d'octets. Cela sera le même pour toutes les manipulations cryptographiques que nous ferons dans cet article.

### Adresse de portefeuille

Une fois que nous avons obtenu la clé publique, nous pouvons calculer l'adresse. Maintenant, contrairement à Bitcoin, Ethereum a les mêmes adresses sur le réseau principal et tous les réseaux de test. Les utilisateurs spécifient le réseau qu'ils veulent utiliser plus tard dans le processus lorsqu'ils créent et signent une transaction.

Pour créer une adresse à partir de la clé publique, tout ce que nous devons faire est d'appliquer Keccak-256 à la clé et ensuite prendre les 20 derniers octets du résultat. Et c'est tout. Aucune autre fonction de hachage, pas de Base58 ou toute autre conversion. La seule chose dont vous avez besoin est d'ajouter '0x' au début de l'adresse.

Voici le code Python :

```python
public_key_bytes = codecs.decode(public_key, 'hex')
keccak_hash = keccak.new(digest_bits=256)
keccak_hash.update(public_key_bytes)
keccak_digest = keccak_hash.hexdigest()
# Prendre les 20 derniers octets
wallet_len = 40
wallet = '0x' + keccak_digest[-wallet_len:]
```

### Somme de contrôle

Maintenant, comme vous vous en souvenez peut-être, Bitcoin crée la somme de contrôle en hachant la clé publique et en prenant les 4 premiers octets du résultat. Cela est vrai pour toutes les adresses Bitcoin, donc vous ne pouvez pas obtenir une adresse valide sans ajouter les octets de somme de contrôle.

Dans Ethereum, ce n'est pas ainsi que les choses fonctionnent. Initialement, il n'y avait aucun mécanisme de somme de contrôle pour valider l'intégrité de la clé. Cependant, en 2016, Vitalik Buterin [a introduit](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md) un mécanisme de somme de contrôle, qui a depuis été adopté par les portefeuilles et les échanges.

L'ajout d'une somme de contrôle à l'adresse de portefeuille Ethereum la rend sensible à la casse.

Tout d'abord, vous devez obtenir le hachage Keccak-256 de l'adresse. Notez que cette adresse doit être passée à la fonction de hachage sans la partie `0x`.

Ensuite, vous itérez sur les caractères de l'adresse initiale. Si le _i_ème octet du hachage est supérieur ou égal à 8, vous convertissez le _i_ème caractère de l'adresse en majuscule, sinon vous le laissez en minuscule.

Enfin, vous ajoutez `0x` au début de la chaîne résultante. L'adresse de somme de contrôle est la même que l'adresse initiale si vous ignorez la casse. Mais les lettres majuscules permettent à quiconque de vérifier que l'adresse est effectivement valide. Vous pouvez trouver l'algorithme de validation de la somme de contrôle sur la [page liée ici](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md).

Comme vous le lirez dans la proposition, pour ce schéma de somme de contrôle,

> "en moyenne, il y aura 15 bits de vérification par adresse, et la probabilité nette qu'une adresse générée aléatoirement, si elle est mal tapée, passe accidentellement une vérification est de 0,0247 %."

Et voici le code pour ajouter une somme de contrôle à l'adresse Ethereum :

```
checksum = '0x'
# Supprimer '0x' de l'adresse
address = address[2:]
address_byte_array = address.encode('utf-8')
keccak_hash = keccak.new(digest_bits=256)
keccak_hash.update(address_byte_array)
keccak_digest = keccak_hash.hexdigest()
for i in range(len(address)):
    address_char = address[i]
    keccak_char = keccak_digest[i]
    if int(keccak_char, 16) >= 8:
        checksum += address_char.upper()
    else:
        checksum += str(address_char)
```

### Conclusion

Comme vous pouvez le voir, créer une adresse pour Ethereum est beaucoup plus simple que pour Bitcoin. Tout ce que nous devons faire est d'appliquer l'ECDSA à la clé publique, puis appliquer Keccak-256, et enfin prendre les 20 derniers octets de ce hachage.

![Image](https://cdn-media-1.freecodecamp.org/images/ftvp6XOxQG9VoczsAV0Nh8YvrdKrafRJYbMt)

Si vous voulez jouer avec le code, je l'ai publié sur le [dépôt GitHub](https://github.com/Destiner/blocksmith).

Je crée un cours sur les cryptomonnaies ici sur freeCodeCamp News. La [première partie](https://medium.com/longcaller/blockchain-explained-2b26b28657ca) est une description détaillée de la blockchain.

Je publie également des pensées aléatoires sur la crypto sur [Twitter](https://twitter.com/DestinerX), donc vous pourriez vouloir y jeter un coup d'œil.