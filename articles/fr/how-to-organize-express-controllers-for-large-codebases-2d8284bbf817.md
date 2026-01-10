---
title: Comment organiser les contrôleurs Express pour les grandes bases de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T22:46:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-organize-express-controllers-for-large-codebases-2d8284bbf817
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rZynfm9hux013-uclDjBfA.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment organiser les contrôleurs Express pour les grandes bases de code
seo_desc: 'By Alexandre Levacher

  Three years ago, I started developing an Express.js API for a company. I wondered
  what could be the best controllers architecture to stay organized as the codebase
  grows.

  Influenced by Sails or Rails and by my research, I came t...'
---

Par Alexandre Levacher

Il y a trois ans, j'ai commencé à développer une API Express.js pour une entreprise. Je me demandais quelle pourrait être la meilleure architecture de contrôleurs pour rester organisé à mesure que la base de code grandit.

Influencé par Sails ou Rails et par mes recherches, j'ai créé mon propre système. Je ne voulais pas surcharger mon projet en utilisant un framework complet comme Sails, mais plutôt choisir des dépendances plus légères lorsque nécessaire.

J'ai donc créé un système d'organisation pour les contrôleurs de l'application que j'ai associé à un chargeur fait maison. Depuis, j'ai amélioré les deux grâce à l'expérience acquise en l'implémentant sur d'autres projets.

Aujourd'hui, je suis suffisamment confiant avec cette méthode pour la partager, car les résultats sont convaincants.

D'après ce que je sais, elle est utilisée par quelques grandes entreprises. Elle simplifie l'intégration des nouveaux développeurs car elle rend la base de code plus facile à lire.

✅ Voici comment mettre en place une architecture de contrôleurs propre.

### **La Structure**

Si vous n'anticipez pas la croissance de votre application, vous aurez rapidement une base de code désorganisée. J'ai conçu la méthode d'organisation pour qu'elle soit largement compatible, ce qui signifie que, un jour, vous ne serez pas bloqué dans un cas d'utilisation que vous ne pouvez pas résoudre avec cette méthode.

#### Configurez votre arborescence de fichiers

* Regroupez les routes dans des contrôleurs
* Créez des dossiers pour chaque contrôleur
* Créez un fichier de routage dans chaque contrôleur qui décrit le **chemin** de chaque route, la **méthode à appeler**, son **middleware** éventuellement associé et le **niveau de restriction**.
* Créez un fichier pour chaque action du contrôleur qui contient la **méthode à exécuter** et les **middlewares**.
* Créez un **fichier de spécification** pour les tests

Voyons à quoi cela ressemble.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4b15NCcOkq9zjfQcS8bEdg.png)
_? Exemple de structure de contrôleurs_

**N'ayez pas peur de créer beaucoup de fichiers**. Cela ne ralentit pas le développement et rend votre base de code soignée et aérée. ✨

### **Chargez vos routes**

Pour faire fonctionner les choses selon la structure définie ci-dessus, nous devons utiliser un chargeur simple que j'ai créé : [Lumie](https://github.com/Alex-Levacher/Lumie). Il parcourra vos contrôleurs, lira les fichiers de définition et chargera vos routes.

C'est un petit package, vous pouvez consulter le code source sur [GitHub](https://github.com/Alex-Levacher/Lumie).

#### Fichiers de routage

Ils ont été conçus pour être faciles à lire. Le but est de pouvoir identifier les méthodes à mettre à jour en développement en jetant un rapide coup d'œil dans vos fichiers **.routing**. Dans l'exemple suivant, trois routes seront créées :

* [ PUT ] **/user**
* [ GET ] **/user**
* [ GET ] **/user/reset-password**

Vous vous demandez pourquoi les routes sont préférées avec « **user** » bien que cela ne soit pas décrit dans la définition de routage. Lumie utilise le nom du dossier dans lequel se trouve le fichier de routage pour préfixer les routes.

Ici, nous sommes dans `controllers/user/user.routing.js`. Si le dossier `user` avait été dans un sous-dossier `admin`, par exemple, les routes auraient été préférées par `admin/user`.

Notez que vous pouvez passer un champ `path` optionnel à la définition de routage afin qu'il soit utilisé à la place de celui par défaut.

#### Actions et Middlewares

Comme vous pouvez le voir ci-dessus, chaque configuration de route a une méthode d'action qui n'est rien de plus que la logique à exécuter lorsque nous appelons votre route API. Je recommande de garder dans un fichier : **une méthode d'action** et **son middleware associé optionnel**.

#### Restrictions

Pour chaque configuration de route, vous choisirez le niveau de restriction associé. La valeur du niveau sera passée à la fonction de restriction que vous créerez pour faire fonctionner Lumie. Voir [comment initialiser Lumie](https://github.com/Alex-Levacher/Lumie#%EF%B8%8F-configuration) avec votre propre fonction de restriction.

Cela devrait être juste une fonction qui retourne un middleware express classique.

### Conclusion

J'utilise cette méthode depuis un certain temps. J'aime avoir ce genre de framework opinionné à suivre lorsque je développe. À la fin de la journée, cela m'aide à garder une base de code propre et à ne pas prendre de raccourcis comme écrire trop de logique dans un seul fichier ou définir une route dans un fichier inapproprié.

Merci d'avoir lu. Dites-moi dans les commentaires ce que vous pensez de l'organisation des contrôleurs de cette manière.

Si vous avez trouvé cet article utile, laissez quelques ? ?