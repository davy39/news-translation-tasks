---
title: Comment architecturer une DApp en utilisant Nuxt.js et Nebulas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-14T19:15:59.000Z'
originalURL: https://freecodecamp.org/news/architecting-dapp-using-nuxt-js-nebulas-fc00712ae341
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1LSHpbDThueykKQQeCkAug.png
tags:
- name: Blockchain
  slug: blockchain
- name: decentralized apps
  slug: decentralized-apps
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment architecturer une DApp en utilisant Nuxt.js et Nebulas
seo_desc: 'By Honey Thakuria

  There is ever-increasing interest in and demand for Decentralized application (DApp)
  development. Therefore, I have decided to come up with a tutorial to help you get
  started with developing & architecting a modular DApp. We’ll use ...'
---

Par Honey Thakuria

Il y a un intérêt et une demande toujours croissants pour le développement d'applications décentralisées (DApp). Par conséquent, j'ai décidé de proposer un tutoriel pour vous aider à commencer à développer et à architecturer une DApp modulaire. Nous utiliserons l'un des langages les plus populaires et largement adoptés du 21e siècle : JavaScript.

Nous travaillerons avec les technologies suivantes dans ce tutoriel :

1. [**Nebulas**](https://nebulas.io/) : une plateforme BlockChain qui nous permet d'écrire des Smart Contracts en JavaScript. Inscrivez-vous [**ici**](https://incentive.nebulas.io/signup.html?invite=1L9eA) pour obtenir le bénéfice de parrainage.
2. [**Nuxt.JS**](https://nuxtjs.org/) : un framework construit sur **Vue.JS**.
3. [**NebPay**](https://github.com/nebulasio/nebPay) : API JavaScript de paiement Nebulas. Pour PC et mobile.
4. [**WebExtensionWallet**](https://github.com/nebulasio/WebExtensionWallet) : Utilisé pour interagir avec le Smart Contract à des fins de paiement.

Je vais expliquer le processus de création de DApp à l'aide d'une DApp existante, [Distributed Stories](http://distributedstoriesupdated.s3-website-eu-west-1.amazonaws.com/). Elle a été qualifiée pour la nouvelle récompense DApp de la saison 1 du programme d'incitation sur la [**plateforme Nebulas**](https://nebulas.io/).

Vous pouvez trouver le code source du frontend de la DAapp [ici](https://github.com/honey93/distributed_stories). Le code du Smart Contract peut être trouvé dans les PayloadData [ici](https://explorer.nebulas.io/#/tx/63cede0eabc488c093064cc37a14ec8c991ac96d39be93db378802313c4486ef).

Il n'est pas toujours suffisant de savoir créer une simple application de liste de tâches. Parfois, nous devons aussi comprendre comment architecturer de grandes applications modulaires.

En me concentrant sur une telle application, je vais vous donner un aperçu de haut niveau de la structuration d'une grande DApp modulaire en utilisant Nuxt.js et Nebulas. Vous pouvez approfondir en explorant et en déboguant le code partagé ci-dessus.

#### Que allons-nous construire ?

Nous allons créer une plateforme de collaboration pour des **histoires**/**poèmes** courts, Distributed Stories. Elle permettra à un utilisateur de créer une nouvelle histoire en ajoutant une ligne à une histoire existante et de partager l'histoire sur Twitter. Voici un lien de démonstration [ici](http://distributedstoriesupdated.s3-website-eu-west-1.amazonaws.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/FkrFJyNuZvkesZjjHSR7KB5JPfBGkrPxnMKP)

Je vais expliquer le **Smart Contract** et l'**Architecture Frontend** dans les lignes suivantes.

### **Le [Code du Smart Contract](https://explorer.nebulas.io/#/tx/63cede0eabc488c093064cc37a14ec8c991ac96d39be93db378802313c4486ef)**

Le Frontend de la DApp communique avec le SmartContract afin de récupérer et d'écrire les données. C'est ensuite la plateforme BlockChain qui synchronise ces données de contrat intelligent sur plusieurs nœuds afin de répondre aux besoins de décentralisation et de sécurité. Ce processus de synchronisation prend un peu de temps, et c'est pourquoi le processus d'écriture coûte du temps et de l'argent sous forme de NAS.

#### **Initialisation** de l'**Histoire**

Dans la section ci-dessous, je vais vous expliquer la partie du contrat intelligent qui définit l'objet Story :

```
"use strict";
/*
Constructeur Story qui créera l'histoire en fournissant les champs nécessaires récupérés depuis le frontend en utilisant l'API nebpay expliquée à la fin de ce blog :
*/

var Story = function(text, image_url) {
    this.title = text;
    this.address = Blockchain.transaction.from;
    this.hash = Blockchain.transaction.hash;
    this.image_url = image_url;
    this.lines = [];
    this.votes = [];
};
/*  
La fonction init est utilisée une fois lors du déploiement du contrat intelligent pour 
initialiser les paramètres si nécessaire :  
*/
Story.prototype = {
    init: function() {

    }
};
```

Comme mentionné ci-dessus, chaque histoire aura les champs suivants, parmi lesquels text et image_url doivent être fournis comme argument par l'utilisateur. Pour le champ Address, le hash peut être obtenu en utilisant les API BlockChain expliquées en profondeur [**ici**](https://medium.com/nebulasio/how-to-build-a-dapp-on-nebulas-part-2-5424789f7417).

#### **Structure de données** et **Stockage** utilisés dans la DApp

Le module de stockage permet le stockage de données sur Nebulas. Il permet le stockage permanent des variables de données sur Nebulas lorsqu'un paiement est effectué. Vous pouvez lire plus en profondeur à ce sujet [ici](https://medium.com/nebulasio/how-to-build-a-dapp-on-nebulas-part-2-5424789f7417).

```
/*
Avec l'aide du module de stockage, nous définissons les maps suivantes et la propriété d'index, qui nous aideront à suivre les données multidimensionnelles obtenues des utilisateurs. Nebulas recommande la capture de plusieurs points de données, ce qui peut aider à améliorer le classement et la fonction de recherche de Nebulas.
*/
var Data = function() {
    LocalContractStorage.defineMapProperty(this, "favourite_stories");
    LocalContractStorage.defineMapProperty(this, "my_stories");
    LocalContractStorage.defineProperty(this, "s_index");
    LocalContractStorage.defineMapProperty(this, "stories_data");
};
```

#### **Sauvegarde** et **Récupération** de l'Histoire

Maintenant, nous allons examiner deux des fonctions les plus importantes utilisées pour écrire et obtenir l'histoire sur la plateforme à l'aide du constructeur Story et du stockage déclaré dans le constructeur Data ci-dessus.

```
/*
La map stories_data contiendra chaque histoire stockée contre son index unique sur le module de stockage de la plateforme.
Chaque index d'histoire ajouté par un utilisateur particulier sera stocké dans une map my_stories, sous la forme d'un tableau.
*/

Data.prototype = {
     
/* 
Initialisation de l'index sur le Smart Contract. Dès que les gens continueront à ajouter une nouvelle histoire, s_index continuera à augmenter. 
*/
 
init: function () {
        this.s_index = new BigNumber(1);
      },
save_story: function (name, image_url) {
var id = this.s_index;
if (name.length > 25) {
          throw new Error("Erreur de longueur de l'histoire");
        }
if (name == "") {
          throw new Error("Titre de l'histoire vide");
        }
var story = new Story(name, image_url);
this.stories_data.put(new BigNumber(id).toNumber(), JSON.stringify(story));
var my_stories_local = this.my_stories.get(Blockchain.transaction.from) || [];
my_stories_local.push(this.s_index);
this.my_stories.put(Blockchain.transaction.from, my_stories_local);
this.s_index = new BigNumber(id).plus(1);
},
      
/* 
La méthode get_stories sera utilisée pour récupérer toutes les histoires stockées sur la plateforme.
*/
get_stories: function () {
        
        var stories = [];
        var total = new BigNumber(this.s_index).toNumber();
        for (let i = 1; i < total; i++) {
          stories.push(JSON.parse(this.stories_data.get(i)));
        }
        return stories;
},
    
/* 
Les fonctions restantes peuvent être trouvées dans le code du Smart Contract ici.
*/
};
module.exports = Data;
```

Cela complète les principales parties du Smart Contract. Dans la section suivante, je vais expliquer la structure du code Frontend dans Nuxt.js.

### **Conception de l'Architecture Frontend**

À mesure que le projet grandit et que de nouvelles fonctionnalités sont ajoutées, une architecture correcte mise en place dès le début peut nous aider à atteindre notre objectif en facilitant le débogage.

L'approche ci-dessous est une bonne façon de procéder :

```
/*
Allez dans le répertoire racine dans le code source ici et trouvez les fichiers mentionnés ci-dessous. Cette architecture aide à créer une grande application/modulaire App/Dapp.
*/
pages/
 
 about / index.vue  : Page statique À propos de nous
 
 contact / index.vue : Page statique Contactez-nous
 
 create / index.vue : Page pour créer l'histoire.
 
 favourite / index.vue : Les histoires que vous avez aimées seront ici.
 
 mystory / index.vue : Page Mes Histoires.
 
 index.vue / index.vue : Page Toutes les Histoires

store/
 index.js : Code Vuex utilisé pour faire des appels API au Smart Contract
 
 neb_init.js : Importation de nebpay et initialisation de l'adresse du Smart Contract     
               ici, qui est utilisée dans toute l'application.
layouts/
 default.vue: Chaque page suit une architecture où l'en-tête et   
              le pied de page sont les mêmes. Donc, configuration de l' 
              architecture par défaut ici.
components/
 
 Header.vue: Composant d'en-tête qui est utilisé dans default.vue
 Footer.cue: Composant de pied de page qui est utilisé dans default.vue
 ....
```

#### Faire des appels API au Smart Contract

Je vais expliquer l'un des appels API en utilisant **nebpay** pour interagir avec le Smart Contract et obtenir toutes les données des histoires pour la page d'accueil.

Initialisez Nebpay, pour être utilisé dans toute l'application dans **store/neb_init.js** :

```
import * as NebPay from 'nebpay.js';
/*
L'adresse du contrat peut être obtenue après avoir déployé le code sur la plateforme Nebulas en utilisant leur Web Wallet.
Il doit s'agir de l'adresse Mainnet.
*/
var contractAddress = "n1pQHv...................Pm1";
var nebPay = new NebPay();
export { contractAddress, nebPay, result,NebPay };
```

Le code de l'**appel API** suivant peut être trouvé dans le fichier **store/index.js** :

```
/*
Les API de nebPay peuvent être utilisées pour interagir avec le Smart Contract et l'extension Chrome pour effectuer des opérations de lecture et d'écriture. Plus de détails sur les API de nebpay peuvent être trouvés ici.
*/
call: (store) => {
// les arguments doivent être envoyés dans le format ci-dessous.
var args = "[]";
nebPay.simulateCall(contractAddress, 0, "get_stories", args, {
 listener: function (data) {
  if (data.result != null) {
    store.commit("all_data", JSON.parse(data.result));
  }
 }
});
}
```

Le code ci-dessus est appelé depuis **component/Allstories.vue**.

```
/*
Dès que le composant Allstories est monté, il déclenche l'action call mentionnée dans les lignes ci-dessus, qui remplit ensuite le tableau all_data du magasin Vuex et est rendu dans le composant All Stories.
*/
mounted() {
  this.$store.dispatch("call");
}
```

Ainsi, vous pouvez explorer chaque section dans le code source et comprendre l'architecture complète de la DApp.

J'espère que ce tutoriel vous a aidé à commencer avec le développement de DApp. Pour toute question, n'hésitez pas à me contacter.