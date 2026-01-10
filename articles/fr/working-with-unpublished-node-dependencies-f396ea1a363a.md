---
title: Comment travailler avec des dépendances Node non publiées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T20:58:22.000Z'
originalURL: https://freecodecamp.org/news/working-with-unpublished-node-dependencies-f396ea1a363a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0n0NX3rgHf2bzldy1uvmiQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment travailler avec des dépendances Node non publiées
seo_desc: 'By Santhosh Reddy

  If you are a Node.js developer, you have definitely ended up in a situation where
  you want to use an unfinished feature from another Node dependency.

  Let’s elaborate on this a bit. For example, your entire project is broken logicall...'
---

Par Santhosh Reddy

Si vous êtes un développeur Node.js, vous vous êtes définitivement retrouvé dans une situation où vous souhaitez utiliser une fonctionnalité inachevée d'une autre dépendance Node.

Élaborons un peu cela. Par exemple, votre projet entier est logiquement divisé en 4 modules npm. Un module, qui est le principal, dépend des 3 autres modules. Avec cette configuration, vous devrez peut-être modifier le code dans les sous-modules et vérifier s'il fonctionne bien avec votre module Node principal.

La manière la plus simple est de publier les modules sur npm. Utilisez les nouvelles versions dans votre module Node principal. Eh bien, l'inconvénient de cette approche est que si vous avez fait une erreur dans vos sous-modules, vous devez les republier et les utiliser en conséquence. Mais les choses ne s'arrêtent pas là. Vous devrez répéter cela jusqu'à ce que votre module Node principal soit stable. Un casse-tête. N'est-ce pas ? Je sais.

Alors, comment contourner ce problème ?

#### Utiliser npm link

Avec cette approche, vous pouvez travailler avec n'importe quelle dépendance Node si elles sont extraites à un endroit de votre machine locale. Tout ce que vous avez à faire est d'exécuter la commande suivante dans le dossier racine du package, qui est une dépendance pour votre module Node principal.

Alors, que fait cela ? Si vous avez travaillé sur des projets basés sur Node, vous savez qu'il y a un dossier **node_modules** qui contient vos dépendances installées. De même, il y a un dossier global pour les dépendances. La commande ci-dessus crée un lien symbolique pour le package dans lequel cette commande est exécutée. Vous devez exécuter cette commande à nouveau dans le package où vous souhaitez utiliser le code de dépendance avec le nom dans `package.json`.

Avec cela, toute modification que vous apportez à votre module Node de dépendance peut être utilisée directement sans avoir à réinstaller. Les 2 étapes ci-dessus peuvent être raccourcies avec la commande suivante.

```
npm link <chemin-relatif-vers-la-dependance>
```

#### Obtenir la source depuis GitHub

Maintenant, discutons d'un autre cas d'utilisation où ce n'est pas vous qui travaillez sur votre dépendance, mais un collègue. Et ils ne veulent pas publier le code tant qu'ils ne sont pas sûrs que la fonctionnalité est complète dans une certaine mesure.

Mais vous avez besoin du code de cette personne pour tester tout problème d'intégration en phase précoce. Je suppose que vous utilisez tous les deux le système de contrôle de version Git pour gérer votre code. Vous pouvez obtenir les modifications que votre collègue a poussées vers git avec le lien vers le code du dépôt comme suit dans votre fichier.

package.json

```
'package-name': git@github.com:<nom-du-depot>.git#<nom-de-la-branche>
```

Une fois que vous avez placé le chemin ci-dessus dans le fichier `package.json`, vous devez exécuter un `npm install` propre pour obtenir le dernier code depuis git.

J'espère que vous avez apprécié l'article. Si vous l'avez aimé, n'hésitez pas à applaudir et à le partager avec d'autres.

Commentez ci-dessous si vous avez une autre manière de travailler avec les dépendances Node.

_Publié à l'origine sur [humbleposts.com](http://humbleposts.com/working-with-unpublished-node-dependencies)._