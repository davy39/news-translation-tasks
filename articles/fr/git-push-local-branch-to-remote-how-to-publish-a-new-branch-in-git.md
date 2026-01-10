---
title: Git Push Local Branch to Remote – Comment publier une nouvelle branche dans
  Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-09T20:36:25.000Z'
originalURL: https://freecodecamp.org/news/git-push-local-branch-to-remote-how-to-publish-a-new-branch-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/code-5290465_1920.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Git Push Local Branch to Remote – Comment publier une nouvelle branche
  dans Git
seo_desc: "Git branches let you add new features without tampering with the live version\
  \ of your projects. And if you work in a team, different developers might have unique\
  \ branches they work on. \nIn the long run, you'll have to push those independent\
  \ branches ..."
---

Les branches Git vous permettent d'ajouter de nouvelles fonctionnalités sans altérer la version live de vos projets. Et si vous travaillez en équipe, différents développeurs peuvent avoir des branches uniques sur lesquelles ils travaillent. 

À long terme, vous devrez pousser ces branches indépendantes vers un serveur distant. Par exemple, GitHub, GitLab, et autres.

Dans cet article, je vais vous montrer comment pousser une branche locale git vers un serveur distant. Peu importe que vous n'ayez pas encore poussé du tout. Vous avez peut-être déjà poussé votre branche principale et souhaitez pousser une autre branche. Je vais vous montrer tout depuis le début.

## Comment pousser la branche principale vers le distant
Si vous voulez pousser la branche principale vers le distant, il est possible que ce soit la première fois que vous poussez. Avant d'essayer de pousser vers le distant, assurez-vous d'avoir exécuté ces commandes :
- `git init` pour initialiser un dépôt local
- `git add .` pour ajouter tous vos fichiers au dépôt local
- `git commit -m 'message de commit'` pour sauvegarder les modifications apportées à ces fichiers

![ss1-2](https://www.freecodecamp.org/news/content/images/2022/09/ss1-2.png)

Pour pousser le dépôt principal, vous devez d'abord ajouter le serveur distant à Git en exécutant `git remote add <url>`.

Pour confirmer que le distant a été ajouté, exécutez `git remote -v` :

![ss2-2](https://www.freecodecamp.org/news/content/images/2022/09/ss2-2.png) 

Pour enfin pousser le dépôt, exécutez `git push -u origin <nom-de-la-branche>`
("main" est le nom de cette branche pour moi). Cela pourrait être master ou Main pour vous. Initialement, c'était "master", donc j'ai exécuté `git branch -M main` pour le changer. 

Si vous n'avez pas configuré Git pour utiliser un assistant d'identification, vous serez invité à entrer votre nom d'utilisateur GitHub et votre PAT (jeton d'accès personnel) :

![ss3-2](https://www.freecodecamp.org/news/content/images/2022/09/ss3-2.png) 

C'est ainsi que vous poussez la branche principale pour la première fois.

## Comment pousser une nouvelle branche vers le distant
Si vous avez une autre branche sur laquelle vous avez travaillé et que vous souhaitez pousser vers le distant, vous utiliserez toujours la commande `git push`, mais de manière légèrement différente.

Pour rappel, pour créer une nouvelle branche, vous exécutez `git branch nom-de-la-branche`. Et pour basculer vers cette branche afin de pouvoir y travailler, vous devez exécuter `git switch nom-de-la-branche` ou `git checkout nom-de-la-branche`.

Pour pousser la branche vers le serveur distant, exécutez `git push -u origin <nom-de-la-branche>`. Dans mon cas, le nom de cette branche est `bug-fixes`. Donc, je dois exécuter `git push -u origin bug-fixes` :

![ss4-2](https://www.freecodecamp.org/news/content/images/2022/09/ss4-2.png) 

Pour confirmer que la branche a été poussée, rendez-vous sur GitHub et cliquez sur le menu déroulant des branches. Vous devriez voir la branche là-bas :

![ss5-2](https://www.freecodecamp.org/news/content/images/2022/09/ss5-2.png)

## Conclusion
Cet article vous a montré comment pousser une nouvelle branche vers le distant. En plus de cela, nous avons également vu comment vous pourriez pousser vers un serveur distant pour la première fois.

Si vous voulez en savoir plus sur git, consultez d'autres [articles freeCodeCamp sur Git et GitHub](https://www.freecodecamp.org/news/tag/git/).