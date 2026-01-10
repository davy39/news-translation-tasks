---
title: Déploiement d'une application Node/Express Mongo en production sur AWS — Une
  réflexion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-25T10:51:35.000Z'
originalURL: https://freecodecamp.org/news/deploying-a-production-node-express-mongo-app-to-aws-a-reflection-8982894289c6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8Seydglu0RAQqkvQ7kIGCQ.jpeg
tags:
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Déploiement d'une application Node/Express Mongo en production sur AWS
  — Une réflexion
seo_desc: 'By Jared Nutt

  Lessons learned deploying a production web application in AWS

  Background

  This is not a code-based tutorial. It consists of all the things I wish I knew before
  I started the project and the steps I took that worked out pretty well. It fo...'
---

Par Jared Nutt

#### Leçons apprises lors du déploiement d'une application web en production sur AWS

### Contexte

Ce n'est pas un tutoriel basé sur du code. Il contient toutes les choses que j'aurais aimé savoir avant de commencer le projet et les étapes que j'ai suivies et qui ont bien fonctionné. Il suit le développement d'une application web Node.js en production créée avec le framework Express qui a été déployée sur Amazon Web Services (AWS).

Le tutoriel complet est disponible [ici](https://medium.freecodecamp.org/how-to-deploy-a-node-js-app-to-the-aws-elastic-beanstalk-f150899ed977).

# Développer un plan est crucial

Il existe des livres entiers sur le développement de plans, donc je ne vais pas m'étendre sur ce sujet ici. Ayez simplement un plan, quel qu'il soit.

# Vous ne vous accordez jamais assez de temps

Peu importe que la tâche soit simple ou complexe. Je n'ai jamais estimé correctement le temps qu'une tâche donnée prendrait. J'imagine qu'à force de le faire, je vais m'améliorer dans l'estimation des délais.

Une chose qui peut aider est de définir un calendrier réaliste qui vous donne suffisamment de marge pour vous ajuster si nécessaire.

# Déployez sur le serveur dès le début

Il y a un vieux dicton de développeur qui dit quelque chose comme : « Développez toujours dans un environnement identique à votre environnement de déploiement. » C'est pour cela que des choses comme les environnements virtuels existent. C'est un conseil avisé.

Aujourd'hui, il est si facile de simplement prendre un générateur (comme [express generator](https://www.npmjs.com/package/express-generator) ou [create-react-app](https://www.npmjs.com/package/create-react-app)), de faire `yarn install` et d'écrire tout notre code localement. C'est génial pour le développement, mais ce que j'ai appris sur le dernier projet, c'est que si vous attendez le déploiement jusqu'à la fin, vous serez surpris par le nombre de choses qui « devraient fonctionner » mais qui ne fonctionnent pas.

Pour ce projet, j'ai choisi de déployer l'application de manière incrémentielle pendant que je la construisais. Cela a permis de s'assurer que ce que je construisais allait fonctionner sur l'environnement sur lequel je vais la déployer. De plus, cela a économisé beaucoup de temps lorsque le moment du déploiement réel est arrivé.

# La communication avec le client est essentielle

Je fais la plupart de mon travail seul, donc parfois je trouve que les solutions que j'ai trouvées ne sont pas toujours compréhensibles pour la personne qui va les utiliser. Il est incroyablement important d'obtenir l'adhésion du client. En fait, si vous pouvez les amener à avoir l'idée, ils vont l'**adorer**, je vous le promets. Rien ne rend un humain plus heureux que d'être écouté.

## À part - J'ai eu de la chance avec un client VRAIMENT bon

Ce n'est pas tant une leçon, qu'un rappel de l'importance de bien choisir vos clients. Je sais que cela semble impossible, et franchement, lorsque vous commencez, il est très difficile d'être sélectif sur vos emplois. Cependant, j'ai accepté des emplois auparavant qui se sont transformés en cauchemars parce que j'ai ignoré les signes.

Des phrases comme « Nous en avons besoin le plus tôt possible » sont un bon indicateur que le client va sous-estimer votre valeur.

# Prévoyez l'échec

![Image](https://cdn-media-1.freecodecamp.org/images/1*CY8CSJcXBrmMZjuZ0SKU7w.png?q=20)
_Les bugs sont inévitables_

Je pense que parfois nous regardons des applications établies comme Facebook ou Instagram et nous essayons d'atteindre cet objectif avec nos applications Version 1.0. Cela est impossible pour deux raisons :

1. La croissance appropriée d'une application nécessite l'apport des utilisateurs. Pensez-vous qu'Instagram avait prévu d'ajouter des stories dans leur version 1.0 ? Bien sûr que non, ils ont attendu que Snapchat le fasse d'abord puis les ont copiés. ?
2. Si vous attendez qu'elle soit parfaite, elle ne sera jamais terminée.

Ce que je veux dire, c'est de faire de votre mieux, mais ne vous attardez pas à écrire la fonction parfaite. Faites-la fonctionner, et améliorez-la au fur et à mesure.

De plus, sachant que les choses vont échouer, assurez-vous de gérer correctement vos erreurs. L'utilisateur doit savoir si quelque chose ne va pas, même s'il ne peut rien y faire.

# L'importance des tests utilisateurs

Ne **pas** envoyer un lien au client et dire : « Allez voir ça », si vous prévoyez de quitter votre ordinateur dans un avenir proche. J'ai fait l'erreur de le faire et j'ai ensuite été bombardé de messages en une heure, alors que j'essayais de déjeuner. À moins, bien sûr, que vous n'aimiez les bugs avec votre sushi. Pas toujours la solution.

Cela peut vous sembler évident, mais cela ne signifie pas que c'est évident pour les autres. Beaucoup de petites choses qui sont devenues des bugs étaient dues à une mauvaise UX ou UI. J'ai tenu pour acquis que je savais exactement ce qui devait se passer parce que j'avais écrit la chose. Je ne dis pas que vous pouvez tout prévoir, mais soyez conscient que vous devrez ajuster certaines de vos mises en page pour que tout le monde sache ce que vous voulez qu'ils fassent.

J'avais initialement prévu seulement deux semaines pour les tests bêta. Une pour tester, une pour corriger. Ce n'est pas assez de temps. J'ai fini par avoir une semaine de tests bêta partie un, une semaine de nettoyage, puis une autre semaine de tests bêta, suivie d'une autre semaine de nettoyage.

# Ne vous attachez pas au produit

Cet idéal est motivé par mon expérience en design graphique. Si nous nous accrochons à un design parce que nous l'aimons vraiment, nous allons ignorer tous les retours des utilisateurs (ce qui compte vraiment) et ne jamais changer. C'est la même chose avec la construction d'une application.

Créer quelque chose à partir de rien est, comme son nom l'indique, un acte créatif. Vous prenez beaucoup de décisions sur la façon dont vous pensez qu'un utilisateur interagira avec la chose que vous construisez. Ne pensez pas que vous savez mieux que l'utilisateur — vous ne savez pas.

# Amusez-vous

Il n'y a aucune raison pour que vous ne puissiez pas apprécier ce que vous faites. Cela ne veut pas dire que ce ne sera pas incroyablement frustrant, mais essayez de l'apprécier autant que possible.

# Apprenez quelque chose

Les délais sont des délais, mais si vous pouvez incorporer une nouvelle chose dans votre stack, faites-le. Vous serez un bien meilleur développeur ensuite.

Mon plus grand défi pour ce projet était AWS. J'ai passé beaucoup d'heures à me familiariser avec AWS. Mais maintenant, j'ai cette expérience à mon actif pour le prochain emploi. Il aurait été si facile de simplement la déployer sur Heroku et d'en rester là, mais ce n'est pas la meilleure option pour un certain nombre de raisons.

# Poussez pour ce MVP

Au moment où j'écris ces lignes, j'ai encore environ 20 problèmes ouverts sur le projet. S'attendre à terminer chaque élément pour la version 1.0 est irréaliste. Poussez toujours pour le produit minimum viable (MVP) initialement. La priorisation est la clé pour déterminer ce qui compte vraiment dans un projet.

**Exemple :** L'un des problèmes ouverts que j'ai est que le padding n'est pas correct sur la navigation. Est-ce un problème critique ? Non. Peut-il attendre que toutes les fonctionnalités principales soient terminées pour le corriger ? Oui.

Donc, je ne l'ai pas encore corrigé. Cependant, j'ai exprimé cela au client et ils sont d'accord avec cela.

# Les choses que je ferai différemment la prochaine fois

## Tests unitaires

Je n'avais rien fait avec les tests avant ce projet, donc je n'ai pas fait de tests unitaires pour ce projet. Grosse erreur. J'ai fini par devoir intégrer des tests après avoir déjà construit la chose.

Les tests unitaires aident pour les points suivants :

1. Chaque fois que j'ajoutais une nouvelle fonctionnalité ou que je changeais quelque chose, je devais tout tester **manuellement**. Pas bon.
2. Cela maintient un niveau de fonctionnalité et vous permet également de réaliser certains défauts de votre code. Écrire délibérément des tests qui échoueront aide à identifier les problèmes dans le code.

Je suggère fortement le cours TDD de [FunFunFunction](https://www.youtube.com/watch?v=Eu35xM76kKY) pour commencer.

**Petite parenthèse :** Si vous utilisez le générateur express, il n'exporte pas le serveur.

Si vous voulez tester le serveur avec Mocha, vous devez l'exporter à la fin du fichier `bin/www`.

```javascript
module.exports = server;
```

## Obtenez une vue plus approfondie de chaque fonctionnalité dès le début

J'ai fait une liste de toutes les fonctionnalités lorsque j'ai commencé, mais je n'ai pas fait une analyse approfondie au début pour voir comment j'allais réellement les implémenter. Si je l'avais fait, j'aurais probablement pu mieux estimer mon temps.

# Petites choses que j'ai apprises

## Vous pouvez accéder à la caméra avec une entrée HTML — Bienvenue en 2018

Cependant, cela ne fonctionne pas sur les pages non sécurisées sous iOS.

## Le téléchargement et le redimensionnement de fichiers est un casse-tête

Le tutoriel que j'ai suivi montrait la méthode pour sauvegarder localement, mais je voulais utiliser AWS S3. Pour être honnête, la méthode que j'ai mise en place n'est pas idéale, donc j'espère pouvoir mieux m'en occuper à l'avenir.

## AWS ne vous permet pas de créer des certificats SSL si vous êtes un nouveau compte

Il s'avère qu'AWS est assez pointilleux sur les nouveaux comptes. Le représentant du service client a dit que c'était pour empêcher les nouveaux comptes d'accumuler des factures énormes, ce qui, je suppose, a du sens. Dans tous les cas, c'est assez ennuyeux lorsque vous essayez de lancer une application et que vous ne pouvez pas obtenir votre certificat SSL.

**Note de côté :** si vous utilisez AWS pour l'hébergement, leur gestionnaire de certificats est incroyablement facile.

## Hébergement de la base de données Mongo

J'ai choisi [mLab](http://mlab.com/) pour héberger ma base de données mongo pour un certain nombre de raisons :

1. Je voulais des sauvegardes sans avoir à gérer les sauvegardes. mLab le fait pour vous.
2. Je ne voulais pas dépenser une tonne d'argent (ou plutôt je ne voulais pas que mon client dépense une tonne d'argent). Ils coûtent 10 $ par gigaoctet.
3. De plus, ils permettent l'hébergement sur AWS. Donc dans mon esprit, ce sera plus rapide. Je doute que ce soit le cas, mais c'est l'intention qui compte, n'est-ce pas ?

## Prettier

Prettier est un sauveur de vie. Cependant, il entre souvent en conflit avec mon ESLint. Pour une chose, il supprime toujours mes parenthèses autour des fonctions à paramètre unique. Ce qui signifie : `(var) => {}`

vs

`var => {}`

## Illustrator continuait à créer des favicons qui faisaient 1000 x 1001 pixels

Il s'avère que si vous n'arrangez pas les plans de travail sur la grille de pixels, cela va les désaligner. L'utilisation de la fonction d'arrangement automatique des plans de travail résoudra ce problème. Plus d'informations [ici](https://www.reddit.com/r/AdobeIllustrator/comments/3dqadd/1_pixel_off_when_exporting_artboards_to_png/).

# Construire pour l'échec est important

Plus j'avançais avec d'autres personnes utilisant l'application, plus je devais ajuster ma base de données et mes vues. Cela signifiait casser des choses qui fonctionnaient auparavant.

Il est difficile de tout prévoir, mais j'ai pris l'habitude de m'attendre à ce qu'il n'y ait pas de données et de les gérer.

**Exemple :** J'ai changé la façon dont je stockais les images. C'était dans un champ appelé 'documentation'. Lorsque j'ai changé la façon dont je les stockais, je l'ai également changé dans la vue, mais cela a cassé les anciennes entrées.

J'ai résolu ce problème en vérifiant d'abord s'il y avait quelque chose. Et s'il y avait quelque chose, j'exécutais une logique.

# Résumé

Ce n'est pas tout ce que j'ai appris, mais j'espère que certaines de ces choses seront utiles à quelqu'un. Si vous avez des questions, contactez-moi.

Je ne peux pas partager le code de ce projet car il est pour un client. Cependant, je suis heureux d'approfondir l'un des points de cet article si vous avez des questions.

**Bon codage !**