---
title: Gestion du chiffrement front-end avec OpenPGP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-17T04:10:48.000Z'
originalURL: https://freecodecamp.org/news/handling-front-end-encryption-using-openpgp-3b0462bf5876
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HMRjFON6A7nGDlvrf7auIw.png
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Gestion du chiffrement front-end avec OpenPGP
seo_desc: 'By Mateja Trifunovski

  In a world where privacy is being constantly invaded, people tend to start to care
  about it. Private messaging platforms are becoming more and more popular. They should
  be, because privacy does matter.

  This article will be about...'
---

Par Mateja Trifunovski

Dans un monde où la vie privée est constamment envahie, les gens commencent à s'en soucier. Les plateformes de messagerie privée deviennent de plus en plus populaires. Elles devraient l'être, car la vie privée est importante.

Cet article traitera du chiffrement de bout en bout des e-mails. Mon expérience vient de la construction d'un système d'e-mail décentralisé et chiffré de bout en bout appelé [**Lemon Email**](https://lemon.email/). Le chiffrement des e-mails peut s'appliquer à pratiquement n'importe quel système, en utilisant les mêmes algorithmes cryptographiques ou similaires.

### Qu'est-ce que le chiffrement front-end ?

L'idée de base est que pour préserver la confidentialité des données, nous devons les rendre illisibles pour les éventuels intrus. La meilleure façon de le faire est de les chiffrer à la source, c'est-à-dire côté client. Nous devons nous assurer que même si les données sont interceptées en cours de route vers le serveur ou une base de données, il est impossible de distinguer ce que représente ce morceau de données.

### **Comment faire ?**

Nous utiliserons un système cryptographique appelé [Cryptographie à clé publique](https://en.wikipedia.org/wiki/Public-key_cryptography), également connu sous le nom de cryptographie asymétrique. Pour l'implémentation réelle, nous utiliserons une bibliothèque open source [OpenPGP.js](https://github.com/openpgpjs/openpgpjs). L'implémentation sera très simple, omettant tout code back-end pour des raisons de simplicité.

#### Génération des clés

La première étape consiste à générer nos clés privée et publique que nous utiliserons pour chiffrer/déchiffrer nos e-mails. Dans l'extrait de code ci-dessous, nous ajoutons quelques options comme la longueur de la clé. La longueur de la clé déterminera la force de la clé ainsi que le temps nécessaire pour la générer. Nous ajoutons également une **phrase secrète** spécifiée par l'utilisateur, utilisée pour verrouiller la clé privée.

```js
let keyOptions = {
    numBits: 2048,
    passphrase: "secret-passphrase"
    // vous obtiendriez normalement la phrase secrète à partir d'un champ de saisie
};

let user = {};

openpgp.generateKey(keyOptions)
    .then((key) => {
        user.privateKey = key.privateKeyArmored;
        user.publicKey = key.publicKeyArmored;
    });
```

La **phrase secrète** est très importante car la clé privée ne peut pas être utilisée sans elle. C'est la seule chose qui empêche les autres d'utiliser la clé privée. Cela est utile car nous stockons généralement notre clé privée dans un stockage persistant, tel qu'une base de données, où quelqu'un peut la voir. La phrase secrète doit être uniquement mémorisée côté client, dans la mémoire de l'utilisateur.

#### Chiffrement d'un message

Après avoir créé nos clés, pour que les utilisateurs puissent échanger des messages, nous avons besoin d'au moins deux utilisateurs. Pour simplifier, disons qu'un autre utilisateur a créé ses clés quelque part et que nous avons maintenant deux utilisateurs.

Dans ce scénario, un utilisateur nommé Bob envoie un message à John. Si nous voulons que seul John puisse lire le message, nous obtenons la **clé publique** de John et l'utilisons pour chiffrer le message complet. Plus tard, John pourra lire le message en utilisant sa **clé privée**.

```js
// Bob{} (Utilisateur 1), John{} (Utilisateur 2)
const email = {
    subject: "Bonjour John, je suis Bob !",
    body: "Message secret"
}

const options = {
    data: JSON.stringify(email),
    // Ici, nous utilisons la clé publique de John pour le chiffrement
    publicKeys:  openpgp.key.readArmored(John.publicKey).keys
};

let messageForJohn = "";
openpgp.encrypt(options)
    .then((cipherText)=>{
         messageForJohn = cipherText.data;
    });
```

La variable `messageForJohn` qui contient la valeur chiffrée de l'e-mail qui ressemble maintenant à l'extrait ci-dessous.

```js
-----BEGIN PGP MESSAGE-----
Version: OpenPGP.js v2.5.4
Comment: http://openpgpjs.org

0mgBCFDGPx2Bz+cETU+PtCjKSzgB+U4pVvEakBlEdBHFnccqfSBI8+A1DCns
s1cOKrMtJ5SfZaYSlxdO+982UqgH8NEV5/+ZLn8OCx+/ppff4EIuN0ZuN4ps
LkbeHL93oA8Ja/rKGJp+kg==
=bf0/
-----END PGP MESSAGE-----
```

#### **Déchiffrement d'un message**

Maintenant que nous avons le contenu du message chiffré, nous devons le déchiffrer pour que John puisse enfin voir son message. Maintenant, tout ce dont nous avons besoin est la **phrase secrète** de John ("john-passphrase") et sa **clé privée**.

```js
// John {} (Utilisateur 2) 
let privateKey = openpgp.key.readArmored(John.privateKey).keys[0];

if (privateKey.decrypt("john-passphrase")) {
    openpgp.decrypt({
        privateKey: privateKey,
        message: openpgp.message.readArmored(messageForJohn)
    })
    .then((decryptedData) => {
        decryptedData = JSON.parse(decryptedData.data);
        console.log(decryptedData);
    })
}
```

Le message de John a été déchiffré et il peut maintenant le lire. Si tout s'est bien passé, cela devrait ressembler à ceci.

```json
{
  "subject": "Bonjour John, je suis Bob !",
  "body": "Message secret"
}
```

#### Étapes suivantes

Ceci était une brève démonstration de la façon dont deux utilisateurs peuvent communiquer de manière privée. Vous pouvez l'étendre selon vos souhaits. Essayez de stocker les clés publiques et privées dans une base de données, et créez un système de connexion qui nécessite qu'un utilisateur entre une phrase secrète en plus du nom d'utilisateur et du mot de passe habituels. Vous pourriez également essayer d'utiliser d'autres bibliothèques de chiffrement comme [crypto-js](https://github.com/brix/crypto-js), amusez-vous simplement avec !

### Mises en garde

Au début, vous pourriez penser, "pourquoi tout n'est-il pas chiffré ?" Eh bien, il y a quelques inconvénients qui accompagnent le chiffrement.

Les clients comme les navigateurs deviennent de plus en plus performants. N'ayant qu'un seul thread principal, l'écran peut geler lors de travaux intensifs comme la génération de clés, ou le déchiffrement de grandes quantités de données. Bien sûr, avec les web workers et les futures mises à jour de performance, cela pourrait devenir une norme.

De plus, certaines fonctionnalités comme la recherche peuvent devenir assez délicates, car vous ne pouvez pas facilement rechercher dans des données chiffrées. Mais avec de nouvelles technologies comme [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API), nous pourrions même voir une recherche entièrement front-end bientôt.

### **Conclusion**

J'ai créé un exemple montrant le chiffrement de base d'un e-mail fictif à ce [Lien Github](https://github.com/Matko95/front-end-encryption-example). N'hésitez pas à jeter un coup d'œil au code et à jouer avec !