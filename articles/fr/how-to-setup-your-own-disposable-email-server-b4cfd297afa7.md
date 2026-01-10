---
title: Comment installer votre propre serveur d'emails jetables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T09:39:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-your-own-disposable-email-server-b4cfd297afa7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*--gyEd4Bg3ZTAwGztCg8_Q.png
tags:
- name: email
  slug: email
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: Software Testing
  slug: software-testing
- name: 'tech '
  slug: tech
seo_title: Comment installer votre propre serveur d'emails jetables
seo_desc: 'By Oren Geva

  Disposable email services are online services that provide temporary email addresses
  for registering or signing up on websites that require email verification.

  The purpose of these services is that you can avoid exposing your own email a...'
---

Par Oren Geva

Les services d'emails jetables sont des services en ligne qui fournissent des adresses email temporaires pour s'inscrire ou s'enregistrer sur des sites web qui nécessitent une vérification par email.

Le but de ces services est de vous permettre d'éviter d'exposer votre propre adresse email à d'éventuels SPAM, surtout si vous n'avez besoin du service que pour une courte période.

Les services d'emails jetables sont également utiles dans le développement et les tests de logiciels, car de nombreux produits logiciels nécessitent eux-mêmes une vérification par email. L'utilisation d'adresses email réelles dans le contexte du développement ou des tests de logiciels est fastidieuse et ennuyeuse. De nombreuses équipes à travers le monde utilisent des services d'emails jetables temporaires pour tester leurs propres produits logiciels.

[AHEM - Ad Hoc Email](https://www.ahem.email) est l'un de ces services. Vous pouvez envoyer un email à une adresse @ahem.email et vérifier la boîte mail [AHEM](https://www.ahem.email) pour récupérer et lire l'email.

De nombreux services similaires tels que [Mailinator](http://www.mailinator.com/), [ThrowAwayMail](https://www.throwawaymail.com/), [Temp-Mail](https://temp-mail.org) et [Yopmail](http://www.yopmail.com) sont disponibles en ligne pour n'en nommer que quelques-uns.

Chacun a sa propre interprétation du thème, mais l'une des choses qui rend [AHEM](https://www.ahem.email) unique est que le code d'AHEM est [librement disponible sur GitHub](https://github.com/o4oren/Ad-Hoc-Email-Server) en open source, permettant à un utilisateur de télécharger et de configurer son propre serveur de mail temporaire.

Mais pourquoi quelqu'un voudrait-il configurer son propre serveur de mail jetable ? Dans le contexte des tests logiciels, bien qu'un service d'email jetable en ligne soit généralement suffisant, il peut arriver que vous souhaitiez héberger un serveur de mail temporaire sur site :

* Certaines organisations bloquent l'accès aux emails jetables, ou même simplement aux sites web inconnus
* Certains laboratoires de QA n'offrent pas d'accès à Internet externe
* Certains produits nécessitent plusieurs domaines de mail ou des domaines contrôlables testés

[AHEM](https://www.ahem.email) répond à tous ces besoins et plus encore.

Pour installer [AHEM](https://www.ahem.email), vous aurez besoin d'une machine Linux ou Windows avec des droits administratifs et Node.js version 8.9+ ainsi que MongoDB installé.

La configuration de Node.js, npm et MongoDB est hors du cadre de ce guide, mais si vous êtes perdu, des informations détaillées sur leur configuration peuvent être trouvées sur les pages de [téléchargement de Node.js](https://nodejs.org/en/download/) et de [téléchargement de MongoDB](https://www.mongodb.com/download-center/community).

### Installation d'AHEM

La section suivante détaille les étapes nécessaires pour installer et exécuter le serveur de mail jetable [AHEM](https://www.ahem.email). [AHEM](https://www.ahem.email) peut fonctionner sur n'importe quel système supportant Node.js.  
Ces étapes ont été réalisées et testées sur un serveur Ubuntu Linux et peuvent nécessiter des modifications mineures pour être compatibles avec d'autres systèmes.

#### **Installer Angular CLI**

[AHEM](https://www.ahem.email) utilise Angular pour sa livraison front-end, vous devrez donc installer angular-cli globalement :

```
npm install -g @angular/cli
```

#### Installer Concurrently

Concurrently est une bibliothèque JavaScript qui permet d'exécuter plusieurs scripts simultanément. Dans cette configuration, [AHEM](https://www.ahem.email) utilise Concurrently pour exécuter à la fois l'API backend node et le serveur email, et servir le front-end directement via angular-cli :

```
npm install -g concurrently
```

#### Cloner le dépôt GitHub AHEM

```
git clone https://github.com/o4oren/ahem-server.git
```

#### Installer les dépendances dans le dossier créé

```
cd ahem-servernpm install
```

#### Mettre à jour la configuration

Un fichier de configuration nommé properties.json est situé à la racine du projet. Modifiez-le selon vos préférences.

```
vim properties.json
```

Le fichier properties.json ressemblera à quelque chose comme ceci :

Voici une explication des paramètres dans le fichier properties :

* **serverBaseUri** - l'adresse de base de votre serveur API.
* **mongoConnectUrl** - l'URL de connexion à mongodb.   
Exemple : "mongodb://localhost:27017/ahem".
* **appListenPort** - le port sur lequel l'application node se lie.
* **smtpPort** - le port du serveur SMTP. Notez que par défaut, il est défini sur 2525 — cela est fait à des fins de test, car sur de nombreux systèmes, seul un compte système peut écouter sur le port 25. Pour recevoir des emails SMTP standard, changez cela en 25.
* **emailDeleteInterval** - Le temps en secondes entre les vérifications d'âge pour purger les anciens emails.
* **emailDeleteAge** - L'âge maximum en secondes au-delà duquel les emails seront supprimés.
* **allowedDomains** - Un tableau de domaines email autorisés. Ces domaines seront autorisés par le serveur en tant qu'entrées RCPT TO:. Cela empêche également le serveur d'agir comme un relais ouvert. Format : ["my.domain.com", "my.second-domain.com"].
* **customText** - Une chaîne html qui remplacera le texte par défaut dans la page d'accueil.
* **allowAutocomplete** - Si défini sur false, empêchera la complétion automatique des utilisateurs dans l'interface utilisateur.

#### **Construire le projet**

```
npm run build:ssr
```

Cela peut prendre un certain temps...

#### Exécuter AHEM

À ce stade, assurez-vous que votre serveur MongoDB est en cours d'exécution et que votre fichier properties.json a été configuré correctement.

La manière la plus simple d'exécuter AHEM est d'exécuter le projet avec la commande :

```
node ahem.js
```

Cette commande démarrera (par défaut) le serveur backend sur le port 3000 et le front-end s'exécutera sur le port 4200. Vous pourrez alors accéder à l'interface web [AHEM](https://www.ahem.email) à l'adresse [http://localhost:4200](http://localhost:4200).

Applaudissez ou étoilez le [dépôt GitHub](https://github.com/o4oren/Ad-Hoc-Email-Server) si vous trouvez cela utile !