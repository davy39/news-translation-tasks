---
title: Lister les branches Git – Comment afficher tous les noms de branches locales
  et distantes
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-29T17:55:45.000Z'
originalURL: https://freecodecamp.org/news/git-list-branches-how-to-show-all-remote-and-local-branch-names
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/magnolia-trees-gffa46356f_1920.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Lister les branches Git – Comment afficher tous les noms de branches locales
  et distantes
seo_desc: "Git is a version control system used by software developers to track changes\
  \ in applications and collaborate on projects. \nOne feature that makes Git more\
  \ dynamic is branches. Developers working on a project can work in different branches\
  \ before merg..."
---

Git est un système de contrôle de version utilisé par les développeurs de logiciels pour suivre les modifications dans les applications et collaborer sur des projets. 

Une fonctionnalité qui rend Git plus dynamique est l'utilisation des branches. Les développeurs travaillant sur un projet peuvent travailler dans différentes branches avant de fusionner leurs modifications avec le code d'origine ou la branche principale.

Parfois, vous souhaiterez peut-être voir les branches que vous et d'autres collaborateurs avez créées. C'est ce que je vais vous montrer comment faire dans cet article.

## Comment afficher tous les noms de branches locales et distantes

Pour voir les noms des branches locales, ouvrez votre terminal et exécutez `git branch` :
![ss-1-4](https://www.freecodecamp.org/news/content/images/2022/03/ss-1-4.png)

**N.B.** la branche locale actuelle sera marquée d'un astérisque. De plus, si vous utilisez Git bash ou Ubuntu sur WSL comme terminal, la branche locale actuelle sera mise en évidence en vert.

Pour voir tous les noms des branches distantes, exécutez `git branch -r` :
![ss-2-4](https://www.freecodecamp.org/news/content/images/2022/03/ss-2-4.png)

Pour voir toutes les branches locales et distantes, exécutez `git branch -a` :
![ss3](https://www.freecodecamp.org/news/content/images/2022/03/ss3.png)

Vous pouvez voir des informations détaillées telles que les branches locales ou distantes utilisées, les IDs de commit et les messages de commit en exécutant `git branch -vv` ou `git branch -vva` :
![ss4](https://www.freecodecamp.org/news/content/images/2022/03/ss4.png)

## Conclusion

Cet article vous a montré comment lister les branches tout en travaillant avec Git.

Être capable de lister les branches Git d'un projet peut vous aider à en savoir plus sur le projet et à savoir sur quoi travaillent les membres de votre équipe.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec d'autres personnes qui pourraient en avoir besoin.

Merci de votre lecture.