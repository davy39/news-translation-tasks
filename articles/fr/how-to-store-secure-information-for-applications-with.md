---
title: Comment stocker des informations sécurisées pour les applications avec dotenv
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T22:31:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-store-secure-information-for-applications-with
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d38740569d1a4ca368d.jpg
tags:
- name: Application Security
  slug: application-security
- name: toothbrush
  slug: toothbrush
seo_title: Comment stocker des informations sécurisées pour les applications avec
  dotenv
seo_desc: This article is about saving username and password credentials information
  for secure database access on 3rd party sites such as mLab in your local testing
  environment. This lets you protect them from anyone looking at your public repository
  on a sit...
---

Cet article traite de la sauvegarde des informations d'identification de nom d'utilisateur et de mot de passe pour un accès sécurisé à la base de données sur des sites tiers tels que mLab dans votre environnement de test local. Cela vous permet de les protéger de toute personne consultant votre dépôt public sur un site comme github.

Les informations sécurisées ou privées ne doivent jamais être stockées dans votre code et poussées vers un dépôt. Cela est dû au fait qu'elles seraient exposées publiquement, ce qui met vos informations en danger. Cela vous expose également au risque de perdre l'accès à l'API ou à la base de données si quelqu'un utilise vos identifiants de manière frauduleuse.

[Cet article wiki](https://forum.freecodecamp.com/t/guide-for-using-mongodb-and-deploying-to-heroku/19347/3) discute de la manière de protéger vos identifiants en utilisant la commande export. Afin de rendre ces variables persistantes, vous avez deux choix. Cependant, les variables d'environnement définies de cette manière sont effacées à chaque redémarrage du shell, par exemple lorsque vous éteignez votre ordinateur et le redémarrez pour une nouvelle session de codage.

Vous devriez répéter toutes les étapes pour définir vos variables d'environnement à chaque fois que vous démarrez un nouveau shell de terminal. Cela signifie que vous devriez stocker vos identifiants dans un fichier texte quelque part, ou continuer à les rechercher dans votre compte tiers (comme mLab).

Faire cela à chaque fois que vous démarrez une nouvelle session devient fastidieux. Plutôt que de les stocker dans le code lui-même où il est facile de les trouver, je vais vous montrer une façon d'utiliser le fichier texte et d'importer vos identifiants.

Le premier choix est d'utiliser votre profil de shell et d'exporter ces variables à chaque fois que vous démarrez un nouveau terminal. Cependant, après quelques semaines de développement de nouvelles applications et projets, votre profil de shell serait encombré par une liste massive de variables dont vous n'aurez pas besoin à chaque session. Vous n'avez besoin des identifiants que pour l'application sur laquelle vous travaillez actuellement.

## **Nettoyer un dépôt git contenant des identifiants sécurisés**

Si vous avez déjà poussé votre dépôt vers github avec vos identifiants stockés dans la base de code, les supprimer et les pousser à nouveau ne servira à rien. Cela est dû au fait que vos identifiants sont stockés dans votre historique, qui est également visible par le public. Si c'est le cas, utilisez ces commandes pour réinitialiser votre dépôt git et effacer votre historique.

**Premièrement**, supprimez votre dépôt de github. Vous en créerez un nouveau lorsque nous serons prêts.

**Deuxièmement**, supprimez votre dépôt git local de votre répertoire de travail. Changez de répertoire pour votre répertoire de travail. Votre fichier de dépôt .git devrait se trouver ici.

ATTENTION : l'utilisation du drapeau -rf peut supprimer l'intégralité de votre disque dur si elle n'est pas utilisée correctement. J'utilise le drapeau -i, qui signifie interactif pour être certain que je suis DANS le bon répertoire. 

Après avoir trié quelques fichiers et être sûr à 100 % que je suis au bon endroit, j'annulerai cette commande et l'exécuterai à nouveau sans le drapeau -i. Faites ce avec quoi vous êtes le plus à l'aise, mais il est conseillé d'avoir une sauvegarde complète de votre ordinateur (dans plus d'un endroit) avant d'exécuter une commande -rm.

```text
cd <nom-du-projet>
rm -i -rf .git
```

**Troisièmement**, assurez-vous de mettre à jour votre fichier .gitignore pour inclure le fichier .env ainsi que tout autre dossier que vous souhaitez garder privé. Les fichiers IDE locaux tels que .idea/ si vous utilisez jetbrains par exemple, pourraient être dans ce fichier. Mon fichier .gitignore ressemble à ceci. Notez que vous pouvez ajouter un dossier ou un fichier ici avant qu'il ne soit créé sans causer d'erreurs.

`.gitignore`  
node_modules  
.env  
data/  
.idea/

**Enfin**, créez un nouveau dépôt. Maintenant, vous êtes prêt à continuer à créer votre fichier .env et à pousser votre dépôt en toute sécurité vers github et à garder vos identifiants en sécurité.

`git init`

## **Comment utiliser dotenv dans votre application locale**

C'est là que le module node dotenv peut aider. Pour utiliser dotenv, vous devez l'inclure dans votre code d'application. Appelez la fonction config() sur celui-ci qui récupère vos identifiants depuis un fichier stocké localement sur votre ordinateur. Ce fichier est nommé `.env`.

**Étape 1 :** Créez un fichier .env et stockez vos variables dedans  
`MONGOLAB_URI="mongodb://username:password@ds01316.mlab.com:1316/food"`

**Étape 2 :** Incluez dotenv dans votre application principale dans votre fichier principal `app.js` (ou quel que soit le nom que vous lui avez donné)  
`var dotenv = require('dotenv');`

**Étape 3 :** Appelez la fonction config sur votre variable. (notez que cela peut être fait en une seule ligne en chaînant, mais j'aime voir cela se produire comme une activité séparée).  
`dotenv.config();`

**Étape 4 :** Définissez votre URL mongodb en appelant vos variables de processus :  
`var url = process.env.MONGOLAB_URI;`

Cette solution garde votre code propre des identifiants sécurisés que vous ne souhaitez pas pousser vers un dépôt public, tout en gardant chaque application bien organisée et en gagnant du temps pendant le développement.

### **[Où définir les variables d'environnement dans Mac OS X](http://osxdaily.com/2015/07/28/set-enviornment-variables-mac-os-x/)**

En ligne de commande, les variables environnementales sont définies pour le shell actuel et sont héritées par toute commande ou processus en cours d'exécution. Elles peuvent déterminer tout, depuis le shell par défaut, le PATH, etc.