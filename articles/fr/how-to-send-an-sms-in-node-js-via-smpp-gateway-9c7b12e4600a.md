---
title: Comment envoyer un SMS en Node.js via une passerelle SMPP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T21:13:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-send-an-sms-in-node-js-via-smpp-gateway-9c7b12e4600a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XVSMVkKMUtd0tX_DzlhVbA.jpeg
tags:
- name: communication
  slug: communication
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: sms
  slug: sms
- name: 'tech '
  slug: tech
seo_title: Comment envoyer un SMS en Node.js via une passerelle SMPP
seo_desc: 'By Shailesh Shekhawat

  Introduction

  SMPP (Short Message Peer-to-Peer) is a protocol used by the telecommunications industry.
  It exchanges SMS messages between (SMSC) and ESME. SMSC acts as middleman to store
  the message and route it. ESME is the syste...'
---

Par Shailesh Shekhawat

### Introduction

SMPP (Short Message Peer-to-Peer) est un protocole utilisé par l'industrie des télécommunications. Il échange des messages SMS entre le SMSC (Short Message Service Center) et l'ESME (External Short Messaging Entity). Le SMSC agit comme intermédiaire pour stocker le message et le router. L'ESME est le système qui livre les SMS au SMSC.

Ce tutoriel vous aidera à envoyer des messages SMS en utilisant votre propre passerelle SMSC.

### **Prise en main**

#### **Où est utilisé SMPP ?**

SMPP est particulièrement adapté aux applications SMS à haut volume et à haut débit. Il présente les caractéristiques suivantes :

* Les connexions établies par le client avec le serveur sont persistantes et peuvent être maintenues ouvertes indéfiniment. Il n'y a pas de surcharge de connexion comme on peut le trouver avec des protocoles tels que HTTP qui utilisent des connexions transitoires.
* Les requêtes peuvent être émises par le client SMPP ainsi que par le serveur SMPP.
* Les requêtes sont traitées de manière asynchrone. Cela signifie que les requêtes peuvent être émises sans avoir à attendre d'abord les réponses aux requêtes précédentes.

#### **Comment l'utiliser**

Nous utiliserons Node.js [node-smpp](https://github.com/farhadi/node-smpp) pour l'implémentation.

Requêtes SMPP :

* **bind** : requête pour établir la session SMPP
* **submit_sm** : requêtes émises par le client pour envoyer des messages à un téléphone mobile
* **deliver_sm** : requêtes émises par le serveur pour transmettre des messages du téléphone mobile au client, y compris les accusés de réception
* **enquire_link** : requêtes émises à la fois par le serveur et le client pour maintenir la session SMPP active
* **unbind** : requête émise par le serveur ou le client pour terminer la session SMPP

#### **Comment cela fonctionne**

Une session SMPP doit être établie entre l'ESME (External Short Messaging Entities) et le Centre de Messages ou l'Entité de Routage SMPP, selon le cas.

Cette session est créée à l'aide d'un client SMPP qui communique avec un protocole SMPP. Il y a un échange continu de PDU SMPP (Protocol Data Units ou Paquets) pour garantir qu'une liaison/connexion appropriée est établie.

Le client SMPP prend en charge les SMS et les livre au serveur SMPP. Le serveur SMPP transmet également un **rapport de livraison** au client lorsqu'il y a un changement de statut pour un SMS.

Node.js nous aidera à atteindre un haut MPS (messages par seconde) car il effectue toutes les opérations d'I/O de manière asynchrone.

Traditionnellement, les opérations d'I/O s'exécutent soit de manière synchrone (bloquante), soit de manière asynchrone en créant des threads parallèles pour effectuer le travail.

Cette ancienne approche consomme beaucoup de mémoire et est notoirement difficile à programmer.

En revanche, lorsqu'une application Node doit effectuer une opération d'I/O, elle envoie une tâche asynchrone à la boucle d'événements, ainsi qu'une fonction de rappel. Elle continue ensuite à exécuter le reste de son programme.

Lorsque l'opération asynchrone est terminée, la boucle d'événements revient à la tâche pour exécuter son rappel.

#### **Mode de message "Stocker et Transférer"**

L'approche conventionnelle pour les SMS a été de stocker le message dans une zone de stockage SMSC (par exemple, une base de données de messages) avant de transférer le message pour livraison au destinataire SME. Avec ce modèle, le message reste stocké en toute sécurité jusqu'à ce que toutes les tentatives de livraison aient été faites par le SMSC. Ce mode de messagerie est communément appelé "stocker et transférer".

![Image](https://cdn-media-1.freecodecamp.org/images/l2qlTM5I7RaqA3ipp3oE-2PZR7zaXh5WZR7S)

### Étape 1 : Créer une session SMPP

Au début, nous devons créer une nouvelle session `smpp` avec une adresse IP et un port.

```js
const smpp = require('smpp');
const session = new smpp.Session({host: '0.0.0.0', port: 9500});
```

### Étape 2 : Lier le Transceiver

Dès qu'il se connecte, nous allons le lier à l'événement `connect` :

```js
let isConnected = false
session.on('connect', () => {
  isConnected = true;

  session.bind_transceiver({
      system_id: 'NOM_UTILISATEUR',
      password: 'MOT_DE_PASSE_UTILISATEUR',
      interface_version: 1,
      system_type: '380666000600',
      address_range: '+380666000600',
      addr_ton: 1,
      addr_npi: 1,
  }, (pdu) => {
    if (pdu.command_status == 0) {
        console.log('Liaison réussie')
    }

  })
})

session.on('close', () => {
  console.log('smpp est maintenant déconnecté') 
  
  if (isConnected) {        
    session.connect();    // reconnecter à nouveau
  }
})

session.on('error', error => { 
  console.log('erreur smpp', error)   
  isConnected = false;
});
```

### Étape 3 : Envoyer un SMS

Maintenant que nous sommes connectés, envoyons le SMS :

```js
function sendSMS(from, to, text) {
   from = `+${from}`  
   
// cela est très important, assurez-vous donc d'avoir inclus le signe + avant le code ISD pour envoyer un SMS
   
   to = `+${to}`
  
  session.submit_sm({
      source_addr:      from,
      destination_addr: to,
      short_message:    text
  }, function(pdu) {
      if (pdu.command_status == 0) {
          // Message envoyé avec succès
          console.log(pdu.message_id);
      }
  });
}
```

Maintenant, après l'envoi du SMS, le SMSC enverra le rapport de livraison indiquant que le message a été livré.

J'espère que vous trouverez ce tutoriel utile. N'hésitez pas à [me contacter](https://101node.io) si vous avez des **questions**.

#### **Pour aller plus loin :**

Si vous souhaitez en savoir plus sur SMPP, consultez : [http://opensmpp.org/specifications.html](http://opensmpp.org/specifications.html)

_N'hésitez pas à applaudir si vous avez trouvé cela utile !_

Suivez [Shailesh Shekhawat](https://www.freecodecamp.org/news/author/thatshailesh/) pour être notifié chaque fois que je publie un nouveau post.

_Publié à l'origine sur [101node.io](https://101node.io/blog/send-sms-in-node-js-via-smpp-gateway/) le 16 septembre 2018._