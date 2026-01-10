---
title: Comment pousser un commit vide dans Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-10T21:04:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-push-an-empty-commit-with-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Push.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment pousser un commit vide dans Git
seo_desc: 'By Chaitanya Prabuddha

  In this article, we will discuss how to push a commit in Git without making any
  changes.

  Git makes this process of pushing an empty commit super simple. It''s like pushing
  a regular commit, except that you add the --allow-empty ...'
---

Par Chaitanya Prabuddha

Dans cet article, nous allons discuter de la façon de pousser un commit dans Git sans apporter de modifications.

Git rend ce processus de poussée d'un commit vide super simple. C'est comme pousser un commit régulier, sauf que vous ajoutez le drapeau `--allow-empty`.

```
git commit --allow-empty -m "Empty-Commit"
```

Vous devrez maintenant pousser cela vers le dépôt principal. Pour ce faire, vous pouvez utiliser cette commande :

```
git push origin main
```

Vous pouvez voir que le commit a été poussé vers votre branche sans aucun changement après avoir exécuté les commandes ci-dessus.

### Pourquoi auriez-vous besoin de pousser un commit vide ?

Il est possible que vous deviez démarrer une build sans apporter de modifications à votre projet. Ou vous ne pourrez peut-être pas initier manuellement la build. La seule méthode pour démarrer la build est d'utiliser Git. Vous pouvez démarrer votre build sans apporter de modifications au projet en poussant un commit vide.

**C'est tout ! N'est-ce pas si simple ? 🤳**

J'écris également régulièrement dans ma newsletter. Vous pouvez vous inscrire directement ici. **👋👋**

<iframe src="https://thelearners.substack.com/embed" height="100"></iframe>