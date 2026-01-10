---
title: Comment écraser les fichiers locaux avec Git Pull
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T23:03:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-override-local-files-with-git-pull
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9db8740569d1a4ca3947.jpg
tags:
- name: Git
  slug: git
- name: toothbrush
  slug: toothbrush
seo_title: Comment écraser les fichiers locaux avec Git Pull
seo_desc: 'When do you need to overwrite local files?

  If you feel the need to discard all your local changes and just reset/overwrite
  everything with a copy from the remote branch, then you should follow this guide.

  Important: If you have any local changes, the...'
---

# **Quand avez-vous besoin d'écraser les fichiers locaux ?**

Si vous ressentez le besoin d'abandonner toutes vos modifications locales et de simplement tout réinitialiser/écraser avec une copie de la branche distante, alors vous devriez suivre ce guide.

Important : Si vous avez des modifications locales, elles seront perdues. Avec ou sans l'option `--hard`, tous les commits locaux qui n'ont pas été poussés seront perdus.

Si vous avez des fichiers qui ne sont pas suivis par Git (par exemple, du contenu utilisateur téléchargé), ces fichiers ne seront pas affectés.

## **Le workflow d'écrasement :**

Pour écraser vos fichiers locaux, faites :

```text
git fetch --all
git reset --hard <remote>/<branch_name>
```

Par exemple :

```text
git fetch --all
git reset --hard origin/master
```

## **Comment cela fonctionne :**

`git fetch` télécharge la dernière version depuis la branche distante sans essayer de fusionner ou de rebaser quoi que ce soit.

Ensuite, `git reset` réinitialise la branche master à ce que vous venez de télécharger. L'option `--hard` modifie tous les fichiers dans votre arborescence de travail pour qu'ils correspondent aux fichiers dans `origin/master`.

## **Informations supplémentaires :**

Il est utile de noter qu'il est possible de conserver les commits locaux actuels en créant une branche à partir de `master` ou de la branche sur laquelle vous souhaitez travailler avant de réinitialiser :

Par exemple :

```text
git checkout master
git branch nouvelle-branche-pour-sauvegarder-les-commits-actuels
git fetch --all
git reset --hard origin/master
```

Après cela, tous les anciens commits seront conservés dans `nouvelle-branche-pour-sauvegarder-les-commits-actuels`. Les modifications non validées (même indexées) seront perdues. Assurez-vous de mettre de côté et de valider tout ce dont vous avez besoin.

### Attribution :

_Cet article est basé sur une question Stack Overflow <a href='http://stackoverflow.com/questions/1125968/force-git-to-overwrite-local-files-on-pull/8888015#8888015' target='_blank' rel='nofollow'>ici_