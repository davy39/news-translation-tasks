---
title: Comment la blockchain fonctionne-t-elle vraiment ? J'ai construit une app pour
  vous le montrer.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-04T19:39:31.000Z'
originalURL: https://freecodecamp.org/news/how-does-blockchain-really-work-i-built-an-app-to-show-you-6b70cd4caf7d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y3c_hIqCuiDH4x-8dObVyg.png
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment la blockchain fonctionne-t-elle vraiment ? J'ai construit une app
  pour vous le montrer.
seo_desc: 'By Sean Han

  According to Wikipedia, a blockchain is:


  A distributed database that is used to maintain a continuously growing list of records,
  called blocks.


  That sounds nice, but how does it work?

  To illustrate a blockchain, we will use an open sour...'
---

Par Sean Han

Selon Wikipedia, une blockchain est :

> Une base de données distribuée utilisée pour maintenir une liste continuellement croissante d'enregistrements, appelés _blocs_.

Cela semble bien, mais comment cela fonctionne-t-il ?

Pour illustrer une blockchain, nous utiliserons une interface en ligne de commande open source appelée [Blockchain CLI](https://github.com/seanseany/blockchain-cli).

J'ai également construit une [version basée sur le navigateur de ceci ici](http://blockchaindemo.io/).

![Image](https://cdn-media-1.freecodecamp.org/images/zSZrnGuYhLmiKeazyIjY-TyzCTcZBjBZoQ1x)

### Installation de la version en ligne de commande

Si ce n'est pas déjà fait, installez [Node.js](https://nodejs.org/download/).

Ensuite, exécutez les commandes suivantes dans votre terminal :

```bash
# Clonez ce dépôt
$ git clone https://github.com/seanseany/blockchain-cli

# Allez dans le dépôt
$ cd blockchain-cli

# Installez les dépendances
$ npm install

# Exécutez l'application
$ npm start
```

Vous devriez voir `? Bienvenue dans Blockchain CLI!` et une invite `blockchain →` prête à accepter des commandes.

### À quoi ressemble un bloc ?

Pour voir votre blockchain actuelle, entrez `blockchain` ou `bc` dans l'invite de commande. Vous devriez voir un bloc comme dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/EJwQgibxDMqIpDvroRN-k5R4CWR5ZZj6-vIw)
_Un bloc sur la blockchain_

* **Index (Bloc #)** : Quel bloc est-ce ? (Le bloc Genesis a l'index 0)
* **Hash** : Le bloc est-il valide ?
* **Hash précédent** : Le bloc précédent est-il valide ?
* **Horodatage** : Quand le bloc a-t-il été ajouté ?
* **Données** : Quelles informations sont stockées sur le bloc ?
* **Nonce** : Combien d'itérations avons-nous effectuées avant de trouver un bloc valide ?

#### Bloc Genesis

Chaque blockchain commence par le `Bloc Genesis`. Comme vous le verrez plus tard, chaque bloc de la blockchain dépend du bloc précédent. Ainsi, le bloc Genesis est nécessaire pour miner notre premier bloc.

### Que se passe-t-il lorsqu'un nouveau bloc est miné ?

![Image](https://cdn-media-1.freecodecamp.org/images/p0XcmG5w3eBvkxEejjPVd99nNBCzUqrhdxbQ)

Minons notre premier bloc. Entrez `mine freeCodeCamp❤️` dans l'invite.

La blockchain regarde le dernier bloc de la blockchain pour l'index et le hash précédent. Dans ce cas, le bloc Genesis est le dernier bloc.

* **Index** : 0+1 = 1
* **Hash précédent** : 0000018035a828da0…
* **Horodatage** : Quand le bloc est ajouté
* **Données** : freeCodeCamp❤️
* **Hash** : ??
* **Nonce** : ??

### Comment le hash est-il calculé ?

Une **valeur de hash** est une **valeur** numérique de longueur fixe qui identifie de manière unique des données.

Le hash est calculé en prenant l'index, le hash du bloc précédent, l'horodatage, les données du bloc et le nonce comme entrée.

```js
CryptoJS.SHA256(index + previousHash + timestamp + data + nonce)
```

L'algorithme SHA256 calculera un hash unique, étant donné ces entrées. Les mêmes entrées retourneront toujours le même hash.

#### Avez-vous remarqué les quatre 0 initiaux dans le hash du bloc ?

Les quatre 0 initiaux sont une exigence minimale pour un hash valide. Le nombre de 0 initiaux requis est appelé **difficulté**.

```js
function isValidHashDifficulty(hash, difficulty) {
  for (var i = 0, b = hash.length; i < b; i ++) {
      if (hash[i] !== '0') {
          break;
      }
  }
  return i >= difficulty;
}
```

Ceci est également connu sous le nom de [système de preuve de travail](https://en.wikipedia.org/wiki/Proof-of-work_system).

### Qu'est-ce qu'un nonce ?

Un nonce est un nombre utilisé pour trouver un hash valide.

```js
let nonce = 0;
let hash;
let input;

while(!isValidHashDifficulty(hash)) {     
  nonce = nonce + 1;
  input = index + previousHash + timestamp + data + nonce;
  hash = CryptoJS.SHA256(input)
}
```

Le nonce itère jusqu'à ce que le hash soit valide. Dans notre cas, un hash valide a au moins quatre 0 initiaux. Le processus de recherche d'un nonce qui correspond à un hash valide est le **minage**.

À mesure que la difficulté **augmente**, le nombre de hashes valides possibles **diminue**. Avec moins de hashes valides possibles, il faut plus de puissance de traitement pour trouver un hash valide.

### Pourquoi est-ce important ?

Cela compte parce que cela maintient la blockchain immuable.

Si nous avons la blockchain suivante A → B → C, et que quelqu'un veut changer les données du Bloc A. Voici ce qui se passe :

1. Les données changent sur le Bloc A.
2. Le hash du Bloc A change parce que les données sont utilisées pour calculer le hash.
3. Le Bloc A devient invalide parce que son hash n'a plus quatre 0 initiaux.
4. Le hash du Bloc B change parce que le hash du Bloc A était utilisé pour calculer le hash du Bloc B.
5. Le Bloc B devient invalide parce que son hash n'a plus quatre 0 initiaux.
6. Le hash du Bloc C change parce que le hash du Bloc B était utilisé pour calculer le hash du Bloc C.
7. Le Bloc C devient invalide parce que son hash n'a plus quatre 0 initiaux.

La seule façon de muter un bloc serait de miner à nouveau le bloc, et tous les blocs suivants. Puisque de nouveaux blocs sont toujours ajoutés, il est presque impossible de muter la blockchain.

J'espère que ce tutoriel vous a été utile !

Si vous souhaitez essayer une version web de la démonstration, rendez-vous sur [http://blockchaindemo.io](http://blockchaindemo.io)