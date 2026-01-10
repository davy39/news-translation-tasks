---
title: Comment utiliser Dependabot pour maintenir votre environnement à jour
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-18T22:28:59.000Z'
originalURL: https://freecodecamp.org/news/using-dependabot-to-keep-your-environment-up-to-date
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/zhang-kenny-2CeWChQ7AD8-unsplash.jpg
tags:
- name: dependency management
  slug: dependency-management
- name: npm
  slug: npm
seo_title: Comment utiliser Dependabot pour maintenir votre environnement à jour
seo_desc: 'By Leonardo Faria

  Adding dependencies to a project often helps you not reinvent the wheel. But at
  the same time it can cause issues in many different aspects of the project:


  Versioning: sometimes dependencies can require specific versions of other d...'
---

Par Leonardo Faria

Ajouter des dépendances à un projet aide souvent à ne pas réinventer la roue. Mais en même temps, cela peut causer des problèmes dans de nombreux aspects du projet :

* Versioning : parfois, les dépendances peuvent nécessiter des versions spécifiques d'autres dépendances, ce qui peut causer des problèmes dans votre application.
* Bundling : vous devez faire attention à ne pas vous retrouver avec trop de code supplémentaire qui alourdira vos bundles.
* Mise à jour : JavaScript évolue rapidement, et si vous ne mettez pas régulièrement à jour les packages, vous jouerez à Jenga dans le futur.

Il existe différents outils pour couvrir la tâche de mise à jour des dépendances, comme [Dependencies.io](https://dependencies.io), [Snyk](https://snyk.io/) et [Dependabot](https://dependabot.com/). Comme j'utilise Dependabot depuis un certain temps, j'ai décidé d'écrire sur mon expérience.

Dependabot est un outil acquis par GitHub il y a un an qui vérifie les fichiers de dépendances de différents langages (Ruby, JavaScript, Python, PHP, Elixir, pour n'en nommer que quelques-uns) et trouve de nouvelles versions des bibliothèques que vous utilisez dans votre projet. Voici l'installation :

![Capture d'écran de Dependabot](https://leonardofaria.net/wp-content/uploads/2020/05/dependabot.jpg)

Les mises à jour quotidiennes peuvent être accablantes, et je pense que les mises à jour hebdomadaires ont un meilleur rapport coût/bénéfice. De plus, je m'assigne les Pull Requests pour recevoir des notifications dès qu'elles sont ouvertes.

## Comment utiliser Dependabot efficacement

Dependabot inclut, dans chaque PR, des notes de version, des changelogs, des liens de commit et des détails de vulnérabilité lorsque disponibles. Cela est utile car vous pouvez consulter les informations et décider de continuer ou non.

Cependant, en tant que programmeurs pragmatiques, nous voulons nous assurer que les choses ne casseront pas. Les détails de la PR sont importants, mais plus que cela, nous voulons une simulation de tous (ou presque tous) les livrables que le projet possède.

![Intégration CI](https://leonardofaria.net/wp-content/uploads/2020/05/semaphore.jpg)

Cette capture d'écran montre ce qui se passe chaque fois qu'une PR est ouverte dans la bibliothèque de composants du codebase de mon travail.

* **Tests (Jest / Bundle)** : la tâche Jest testera les composants React tandis que la tâche Bundle simulera les commandes de bundling que nous exécutons lorsque nous voulons mettre à jour le package dans le registre NPM.
* **Linters (Stylesheets / JavaScript)** : les fichiers de stylesheet suivent une configuration personnalisée de sass-lint et le code JS suit une série de règles ESLint. Si une PR introduit une nouvelle version d'un linter avec de nouvelles règles, nous pourrons le capturer.
* **Cypress (Screenshot Testing / Accessibility Testing)** : si un nouveau package introduit des changements qui peuvent être reflétés dans l'apparence des composants, Cypress capturera la différence, prendra une capture d'écran et la stockera dans S3. Comme Cypress a besoin d'une version live du site de documentation, nous couvrons également le processus de build Gatsby.

Avec toutes ces étapes, il est très peu probable qu'un package externe casse notre branche master. Merci à mon collègue Grant Lee qui travaille également sur ce projet.

_Aussi publié sur [mon blog](https://bit.ly/2ZhD9GC). Si vous aimez ce contenu, suivez-moi sur [Twitter](https://twitter.com/leozera) et [GitHub](https://github.com/leonardofaria). Photo de couverture par [Zhang Kenny](https://unsplash.com/@kennyzhang29?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/dependency-tree?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_