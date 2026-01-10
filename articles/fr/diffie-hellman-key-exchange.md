---
title: 'Diffie-Hellman : L''algorithme de génie derrière la communication réseau sécurisée'
subtitle: ''
author: David Karolyi
co_authors: []
series: null
date: '2020-05-11T18:53:11.000Z'
originalURL: https://freecodecamp.org/news/diffie-hellman-key-exchange
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b21740569d1a4ca29e4.jpg
tags:
- name: algorithms
  slug: algorithms
- name: computer network
  slug: computer-network
- name: Cryptography
  slug: cryptography
- name: cybersecurity
  slug: cybersecurity
- name: JavaScript
  slug: javascript
seo_title: 'Diffie-Hellman : L''algorithme de génie derrière la communication réseau
  sécurisée'
seo_desc: 'Let''s start with a quick thought experiment.

  You have a network of 3 computers, used by Alice, Bob, and Charlie. All 3 participants
  can send messages, but just in a way that all other clients who connected to the
  network can read it. This is the only...'
---

Commençons par une petite expérience de pensée.

Vous avez un réseau de 3 ordinateurs, utilisés par Alice, Bob et Charlie. Les 3 participants peuvent envoyer des messages, mais seulement de manière à ce que tous les autres clients connectés au réseau puissent les lire. C'est la seule forme de communication possible entre les participants.

Si Alice envoie un message à travers les fils, Bob et Charlie le reçoivent tous les deux. En d'autres termes, Alice ne peut pas envoyer un message direct à Bob sans que Charlie le reçoive également.

Mais Alice veut envoyer un message confidentiel à Bob et ne veut pas que Charlie puisse le lire.

Cela semble impossible avec ces règles strictes, n'est-ce pas ? La belle chose est que ce problème a été résolu en 1976 par Whitfield Diffie et Martin Hellman.

C'est une version simplifiée du monde réel, mais nous sommes confrontés au même problème lorsque nous communiquons à travers le plus grand réseau qui ait jamais existé.

Habituellement, vous n'êtes pas directement connecté à Internet, mais vous faites partie d'un réseau local plus petit, appelé Ethernet.

Ce réseau plus petit peut être filaire ou sans fil (Wi-Fi), mais le concept de base reste le même. Si vous envoyez un signal à travers le réseau, ce signal peut être lu par tous les autres clients connectés au même réseau.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/network-ethernet.png)

Une fois que vous émettez un message au serveur de votre banque avec les informations de votre carte de crédit, tous les autres clients du réseau local recevront le message, y compris le routeur. Il le transmettra ensuite au serveur réel de la banque. Tous les autres clients ignoreront le message.

Mais que se passe-t-il s'il y a un client malveillant dans le réseau qui ne va pas ignorer vos messages confidentiels, mais les lire à la place ? Comment est-il possible que vous ayez encore de l'argent sur votre compte bancaire ?

## Chiffrement

Il est assez clair à ce stade que nous devons utiliser une sorte de chiffrement pour nous assurer que le message est lisible pour Alice et Bob, mais complètement incompréhensible pour Charlie.

Le chiffrement des informations est effectué par un algorithme de chiffrement, qui prend une clé (par exemple une chaîne de caractères) et renvoie une valeur chiffrée, appelée texte chiffré. Le texte chiffré est simplement une chaîne de caractères qui semble complètement aléatoire.

Il est important que la valeur chiffrée (texte chiffré) ne puisse être déchiffrée qu'avec la clé d'origine. Cela s'appelle un algorithme à clé symétrique parce que vous avez besoin de la même clé pour déchiffrer le message que celle avec laquelle il a été chiffré. Il existe également des algorithmes à clé asymétrique, mais nous n'en avons pas besoin pour l'instant.

Pour faciliter la compréhension de cela, voici un algorithme de chiffrement factice implémenté en JavaScript :

```javascript
function encrypt(message, key) {
    return message.split("").map(character => {
        const characterAsciiCode = character.charCodeAt(0)
    	return String.fromCharCode(characterAsciiCode+key.length)
    }).join("");
}
```

Dans cette fonction, j'ai mappé chaque caractère à un autre caractère basé sur la longueur de la clé donnée.

Chaque caractère a une représentation entière, appelée code ASCII. Il existe un dictionnaire qui contient tous les caractères avec leur code, appelé la table ASCII. Nous avons donc incrémenté cet entier par la longueur de la clé :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-13.png)
_Mappage des caractères_

Le déchiffrement du texte chiffré est assez similaire. Mais au lieu d'une addition, nous soustrayons la longueur de la clé de chaque caractère dans le texte chiffré, afin de retrouver le message original.

```javascript
function decrypt(cipher, key) {
    return cipher.split("").map(character => {
        const characterAsciiCode = character.charCodeAt(0)
    	return String.fromCharCode(characterAsciiCode-key.length)
    }).join("");
}
```

Enfin, voici le chiffrement factice en action :

```javascript
const message = "Hi Bob, here is a confidential message!";
const key = "password";

const cipher = encrypt(message, key);
console.log("Message chiffré :", cipher);
// Message chiffré : Pq(Jwj4(pmzm(q{(i(kwvnqlmv|qit(um{{iom)

const decryptedMessage = decrypt(cipher, key);
console.log("Message déchiffré :", decryptedMessage);
// Message déchiffré : Hi Bob, here is a confidential message!
```

Nous avons appliqué un certain degré de chiffrement au message, mais cet algorithme n'était utile qu'à des fins de démonstration, pour avoir une idée de la manière dont les algorithmes de chiffrement à clé symétrique se comportent.

Il y a quelques problèmes avec cette implémentation, en plus de la mauvaise gestion des cas particuliers et des types de paramètres.

Tout d'abord, toute clé de 8 caractères peut déchiffrer le message qui a été chiffré avec la clé "password". Nous voulons qu'un algorithme de chiffrement ne puisse déchiffrer un message que si nous lui donnons la même clé que celle avec laquelle le message a été chiffré. Une serrure de porte qui peut être ouverte par toute autre clé n'est pas très utile.

Deuxièmement, la logique est trop simple - chaque caractère est décalé de la même quantité dans la table ASCII, ce qui est trop prévisible. Nous avons besoin de quelque chose de plus complexe pour rendre plus difficile la découverte du message sans la clé.

Troisièmement, il n'y a pas de longueur minimale pour la clé. Les algorithmes modernes fonctionnent avec des clés d'au moins 128 bits de long (~16 caractères). Cela augmente considérablement le nombre de clés possibles, et donc la sécurité du chiffrement.

Enfin, il faut trop peu de temps pour chiffrer ou déchiffrer le message. C'est un problème parce qu'il ne faut pas trop de temps pour essayer toutes les clés possibles et craquer le message chiffré.

Cela va de pair avec la longueur de la clé : Un algorithme est sécurisé si, en tant qu'attaquant, je veux trouver la clé, alors je dois essayer un grand nombre de combinaisons de clés et il faut un temps relativement long pour essayer une seule combinaison.

Il existe une large gamme d'algorithmes de chiffrement symétrique qui ont abordé toutes ces revendications, souvent utilisés ensemble pour trouver un bon ratio de vitesse et de sécurité pour chaque situation.

Les algorithmes à clé symétrique les plus populaires sont [Twofish](http://en.wikipedia.org/wiki/Twofish), [Serpent](http://en.wikipedia.org/wiki/Serpent_%28cipher%29), [AES](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard) ([Rijndael](http://en.wikipedia.org/wiki/Rijndael)), [Blowfish](http://en.wikipedia.org/wiki/Blowfish_%28cipher%29), [CAST5](http://en.wikipedia.org/wiki/CAST5), [RC4](http://en.wikipedia.org/wiki/RC4), [TDES](http://en.wikipedia.org/wiki/Triple_DES), et [IDEA](http://en.wikipedia.org/wiki/International_Data_Encryption_Algorithm).

Si vous voulez en savoir plus sur la cryptographie en général, consultez [cette conférence](https://www.youtube.com/watch?v=cqgtdkURzTE).

## Échange de clés

Il semble que nous ayons réduit l'espace du problème original. Avec le chiffrement, nous pouvons créer un message qui est significatif pour les parties qui sont éligibles pour lire l'information, mais qui est illisible pour les autres.

Lorsque Alice veut écrire un message confidentiel, elle choisirait une clé et chiffrerait son message avec celle-ci et enverrait le texte chiffré à travers les fils. Bob et Charlie recevraient tous les deux le message chiffré, mais aucun d'eux ne pourrait l'interpréter sans la clé d'Alice.

Maintenant, la seule question à répondre est de savoir comment Alice et Bob peuvent trouver une clé commune simplement en communiquant à travers le réseau et empêcher Charlie de découvrir cette même clé.

Si Alice envoie sa clé directement à travers les fils, Charlie l'intercepterait et serait capable de déchiffrer tous les messages d'Alice. Donc ce n'est pas une solution. Cela s'appelle le problème d'échange de clés en informatique.

### Échange de clés Diffie-Hellman

Cet algorithme cool fournit un moyen de générer une clé partagée entre deux personnes de telle manière que la clé ne peut pas être vue en observant la communication.

En premier lieu, nous dirons qu'il existe un nombre premier énorme, connu de tous les participants, c'est une information publique. Nous l'appelons **"p" ou modulus**.

Il existe également un autre nombre public appelé **"g" ou base**, qui est inférieur à **p**.

Ne vous inquiétez pas de la manière dont ces nombres sont générés. Pour simplifier, disons simplement qu'Alice choisit un très grand nombre premier (**p**) et un nombre qui est considérablement inférieur à **p**. Elle les envoie ensuite à travers les fils sans aucun chiffrement, de sorte que tous les participants connaîtront ces nombres.

**Exemple :** Pour comprendre cela à travers un exemple, nous utiliserons de petits nombres. Disons **p=23** et **g=5**.

En deuxième lieu, Alice (**a**) et Bob (**b**) choisiront tous les deux un nombre secret, qu'ils ne diront à personne, il vit simplement localement dans leurs ordinateurs.

**Exemple :** Disons qu'Alice a choisi 4 (**a=4**), et Bob a choisi 3 (**b=3**).

Ensuite, ils feront quelques calculs sur leurs nombres secrets, ils calculeront :

1. la base (**g**) à la puissance de leur nombre secret,
2. et prendront le modulo du nombre calculé par **p**.
3. Appelons le résultat **A** (pour Alice) et **B** (pour Bob).

Le modulo est une simple déclaration mathématique, et nous l'utilisons pour trouver le reste après avoir divisé un nombre par un autre. Voici un exemple : **23 mod 4 = 3**, parce que 23/4 est 5 et il reste 3.

Peut-être est-il plus facile de voir tout cela en code :

```javascript
// base
const g = 5;
// modulus
const p = 23;

// Le nombre choisi aléatoirement par Alice
const a = 4;
// La valeur calculée par Alice
const A = Math.pow(g, a)%p;

// Faire de même pour Bob
const b = 3;
const B = Math.pow(g, b)%p;

console.log("Valeur calculée par Alice (A) :", A);
// Valeur calculée par Alice (A) : 4
console.log("Valeur calculée par Bob (B) :", B);
// Valeur calculée par Bob (B) : 10
```

Maintenant, Alice et Bob enverront leurs valeurs calculées (**A**, **B**) à travers le réseau, de sorte que tous les participants les connaîtront.

En dernière étape, Alice et Bob prendront les valeurs calculées de l'autre et feront ce qui suit :

1. Alice prendra la valeur calculée de Bob (**B**) à la puissance de son nombre secret (**a**),
2. et calculera le modulo de ce nombre par **p** et appellera le résultat **s** (secret).
3. Bob fera de même mais avec la valeur calculée d'Alice (**A**), et son nombre secret (**b**).

À ce stade, ils ont réussi à générer un secret commun (**s**), même si c'est difficile à voir pour l'instant. Nous explorerons cela plus en détail dans un instant.

En code :

```javascript
// Alice calcule le secret commun
const secretOfAlice = Math.pow(B, a)%p;
console.log("Secret calculé par Alice :", secretOfAlice);
// Secret calculé par Alice : 18

// Bob calculera
const secretOfBob = Math.pow(A, b)%p;
console.log("Secret calculé par Bob :", secretOfBob);
// Secret calculé par Bob : 18
```

Comme vous pouvez le voir, Alice et Bob ont tous les deux obtenu le nombre 18, qu'ils peuvent utiliser comme clé pour chiffrer les messages. Cela semble magique à ce stade, mais ce n'est que des mathématiques.

Voyons pourquoi ils ont obtenu le même nombre en décomposant les calculs en éléments élémentaires :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-09-at-12.11.18.png)
_Le processus sous forme d'équation_

Dans la dernière étape, nous avons utilisé une [identité arithmétique modulo](https://en.wikipedia.org/wiki/Modulo_operation#Properties_(identities)) et ses propriétés distributives pour simplifier les déclarations modulo imbriquées.

Ainsi, Alice et Bob ont la même clé, mais voyons ce que Charlie a vu de tout cela. Nous savons que **p** et **g** sont des nombres publics, disponibles pour tout le monde.

Nous savons également qu'Alice et Bob ont envoyé leurs valeurs calculées (**A**, **B**) à travers le réseau, donc cela peut également être capté par Charlie.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-09-at-20.12.35.png)
_Perspective de Charlie_

Charlie connaît presque tous les paramètres de cette équation, seuls **a** et **b** restent cachés. Pour rester dans l'exemple, s'il sait que **A** est 4 et **p** est 23, **g** à la puissance de **a** peut être 4, 27, 50, 73, ... et une infinité d'autres nombres qui résultent en 4 dans l'espace modulo.

Il sait également que seul un sous-ensemble de ces nombres sont des options possibles parce que tous les nombres ne sont pas une exponentielle de 5 (**g**), mais cela reste un nombre infini d'options à essayer.

Cela ne semble pas très sécurisé avec de petits nombres. Mais au début, j'ai dit que **p** est un nombre vraiment grand, souvent de 2000 ou 4000 bits de long. Cela rend presque impossible de deviner la valeur de **a** ou **b** dans le monde réel.

La clé commune qu'Alice et Bob possèdent tous les deux ne peut être générée qu'en connaissant **a** ou **b**, en plus des informations qui ont circulé à travers le réseau.

Si vous êtes plus visuel, voici un grand diagramme qui montre tout ce processus en mélangeant des seaux de peinture au lieu de nombres.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Diffie-Hellman_Key_Exchange.svg)
_source : [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)_

Ici, **p** et **g** sont des constantes partagées représentées par la peinture jaune "Peinture commune". Les nombres secrets d'Alice et Bob (**a**, **b**) sont des "Couleurs secrètes", et "Secret commun" est ce que nous avons appelé **s**.

C'est une grande analogie car elle représente l'irréversibilité de l'opération modulo. Comme les peintures mélangées ne peuvent pas être démélangées en leurs composants originaux, le résultat d'une opération modulo ne peut pas être inversé.

## Résumé

Maintenant, le problème original peut être résolu en chiffrant les messages à l'aide d'une clé partagée, qui a été échangée avec l'algorithme Diffie-Hellman.

Avec cela, Alice et Bob peuvent communiquer de manière sécurisée, et Charlie ne peut pas lire leurs messages même s'il fait partie du même réseau.

Merci d'avoir lu jusqu'ici ! J'espère que vous avez tiré quelque chose de valeur de cet article et que vous avez compris certaines parties de ce flux de communication intéressant.

Si cela a été difficile de suivre les mathématiques de cette explication, [ici](https://www.youtube.com/watch?v=NmM9HA2MQGI) se trouve une excellente vidéo pour vous aider à comprendre l'algorithme sans mathématiques, d'un niveau supérieur.

Si vous avez aimé cet article, vous voudrez peut-être me suivre sur [Twitter](https://twitter.com/karolyidav) pour trouver d'autres ressources passionnantes sur la programmation et le développement logiciel.