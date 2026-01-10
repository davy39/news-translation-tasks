---
title: 5 astuces npm pour booster votre productivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-29T14:05:16.000Z'
originalURL: https://freecodecamp.org/news/5-npm-tips-and-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Being-Agile-Kanban-VS-Scrum--4-.png
tags:
- name: npm
  slug: npm
- name: Productivity
  slug: productivity
seo_title: 5 astuces npm pour booster votre productivité
seo_desc: 'By Niall Maher

  While this article will likely boost your productivity, at the very least it will
  also impress some of your colleagues with your new skills. People will now perceive
  you as smarter and potentially more interesting. ?

  I''ve kept away fro...'
---

Par Niall Maher

Bien que cet article boostera probablement votre productivité, il impressionnera au moins certains de vos collègues avec vos nouvelles compétences. Les gens vous percevront désormais comme plus intelligent et potentiellement plus intéressant. ?

J'ai évité les raccourcis évidents et j'ai essayé de partager des informations que vous ne connaissez probablement pas.

Si vous préférez la version vidéo, regardez-la ci-dessous. Si vous aimez lire, alors faites défiler, mon ami... ?

%[https://youtu.be/EVT39ggmoM8]

## 1. Lister les scripts disponibles

Pour vérifier facilement tous les scripts disponibles dans un projet, exécutez simplement :

```
npm run
```

Cela vous donne une belle sortie montrant les commandes comme ceci :

![sortie npm run](https://res.cloudinary.com/practicaldev/image/fetch/s--_LPtQBgD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/HMIzHx7.png)

## 2. Lister les packages installés

```
npm list
```

Cela nous montre probablement trop d'informations car nous voyons les dépendances de nos dépendances...

![sortie npm list](https://res.cloudinary.com/practicaldev/image/fetch/s--kz7Rq87p--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/axrlVAi.png)

Utilisez `--depth` pour limiter la profondeur de votre recherche

```
npm list --depth=0
```

Et voici la sortie lorsque vous limitez la profondeur :

![sortie npm list --depth=0](https://res.cloudinary.com/practicaldev/image/fetch/s--u3jK9MGv--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/oS5z6Lw.png)

## 3. Ouvrir la page d'accueil ou le dépôt d'un package

J'aime vraiment cette fonctionnalité car vous pouvez rapidement obtenir la documentation des packages.

Pour ouvrir automatiquement la page d'accueil du package, vous pouvez exécuter :

```
npm home NOM_DU_PACKAGE
```

Pour ouvrir le dépôt, vous pouvez simplement exécuter :

```
npm repo NOM_DU_PACKAGE
```

C'est super pratique pour ne pas avoir à chercher sur Google les pages de documentation ou npm et pour accéder rapidement aux informations dont vous avez besoin sur les packages que vous ne connaissez pas.

## 4. Afficher toutes les versions disponibles pour un package

Pour obtenir la dernière version d'un package, nous pouvons exécuter :

```
npm v react version
```

![sortie npm v react version](https://res.cloudinary.com/practicaldev/image/fetch/s--iRvAhOEz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/UsPEWEl.png)

Ou pour toutes les versions, nous devons simplement mettre "version" au pluriel.

```
npm v react versions
```

Nous obtenons ensuite une belle sortie de toutes les versions disponibles, ce qui est super pratique si vous voulez vérifier ce qui est nouveau/ancien ou s'il y a des versions alpha à essayer.

Voici un extrait de la sortie de l'exécution de `npm v react versions` :

![sortie npm v react versions](https://res.cloudinary.com/practicaldev/image/fetch/s--PcoUrUC---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/bFY7uNf.png)

## 5. Rechercher les packages obsolètes

La commande `outdated` vérifie le registre npm pour voir si l'un de vos packages est obsolète. Elle affiche un petit tableau dans votre ligne de commande montrant la version actuelle, la version souhaitée et la dernière version.

```
npm outdated
```

Si vous voyez les packages en rouge comme dans mon exemple, cela signifie qu'il y a des vulnérabilités majeures et qu'ils doivent être mis à jour. Comme vous pouvez le voir dans ce projet de 4 ans, tout est d'un beau rouge sain...

![sortie npm outdated sur un ancien projet](https://res.cloudinary.com/practicaldev/image/fetch/s--6WBx9bX3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.imgur.com/uwZUxfO.jpg)

Si vous voulez des versions différentes de votre version actuelle, vous pouvez exécuter `npm update` pour mettre à jour ces packages en toute sécurité.

Je pense qu'une meilleure façon de mettre à jour et de vérifier les éléments obsolètes est d'exécuter la commande `npm audit`, car elle donne beaucoup plus de détails. Je ne l'ai pas incluse comme astuce car elle nous crie toujours dessus pour l'exécuter dans la console lorsque nous installons des dépendances.

## Astuce bonus pour Visual Studio Code ! ?

Beaucoup de gens ne le savent pas, mais vous pouvez exécuter vos scripts directement depuis Visual Studio Code avec leur belle interface.

Cherchez "NPM Scripts" en bas à gauche de votre panneau.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/TiTJeqh.png)
_[Affichage de l'onglet npm scripts dans Visual Studio Code](https://i.imgur.com/TiTJeqh.png)_

Vous pouvez ouvrir vos scripts à partir d'ici et simplement appuyer sur l'icône de lecture pour les lancer. J'aime cela car c'est une méthode claire et facile pour les personnes qui ne sont peut-être pas très familières avec _npm_.

Si vous ne voyez pas cela, assurez-vous qu'il est activé dans vos paramètres. ?

---

[Suivez-moi sur Twitter](https://twitter.com/nialljoemaher)

Abonnez-vous sur [Codú Community](https://www.youtube.com/c/Cod%C3%BACommunity)