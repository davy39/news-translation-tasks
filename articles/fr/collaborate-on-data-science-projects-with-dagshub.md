---
title: Comment collaborer sur des projets de data science avec DAGsHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T19:13:20.000Z'
originalURL: https://freecodecamp.org/news/collaborate-on-data-science-projects-with-dagshub
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/dagshub-storage.png
tags:
- name: Data Science
  slug: data-science
- name: version control
  slug: version-control
seo_title: Comment collaborer sur des projets de data science avec DAGsHub
seo_desc: 'By Linda Ikechukwu

  For software engineering teams, tools like Git and remote Git clients like GitHub,
  GitLab, and BitBucket have made collaboration easy and uncomplicated.

  They let different developers in different locations work on and contribute to...'
---

Par Linda Ikechukwu

Pour les équipes d'ingénierie logicielle, des outils comme Git et des clients Git distants comme GitHub, GitLab et BitBucket ont rendu la collaboration facile et sans complications.

Ils permettent à différents développeurs dans différents endroits de travailler et de contribuer au même projet de manière transparente. Cette capacité à collaborer facilement sur des projets a favorisé le développement de l'écosystème massif des logiciels/librairies open source.

Malheureusement, on ne peut pas en dire autant des équipes de data science. Même les équipes de data science les plus compétentes manquent encore de meilleures pratiques pour organiser leurs projets et collaborer efficacement.

Le domaine de la data science est une combinaison d'ingénierie logicielle et de recherche, c'est-à-dire du code + des ensembles de données, des modèles entraînés et des encodages de labels. Tout comme il est élémentaire de contrôler l'historique des versions et de collaborer à distance sur du code avec quelques commandes git, les data scientists devraient pouvoir parcourir, prévisualiser, partager, forker et fusionner des données et des modèles avec facilité.

Deux choses doivent être en place pour faciliter la collaboration à distance : le contrôle de version et le stockage central distant.

Tout comme Git permet aux ingénieurs logiciels de naviguer en toute sécurité entre différentes versions de leur code, les data scientists doivent contrôler non seulement différentes versions de leur code, mais aussi différentes versions de leurs données.

Ils doivent également être capables de suivre ce qu'ils ont fait pour atteindre un état particulier pour une version particulière et également être capables de reproduire le même état lorsque nécessaire.

Alors, quelles sont les solutions possibles ?

## Option 1 : Utiliser Git pour le contrôle de version dans les projets de data science

Vous pourriez déjà vous demander – ne pouvons-nous pas simplement utiliser Git ? Le problème est que Git a une limite de taille de fichier de 100 Mo. Cela ne serait pas suffisant pour des projets de data science sérieux qui ont parfois des fichiers de données qui atteignent des gigaoctets.

Une solution serait d'ajouter [Git LFS](https://www.atlassian.com/git/tutorials/git-lfs) (Large File Storage) au mélange.

Git LFS est une extension git pour gérer la restriction de taille de fichier dans Git. Il le fait en créant un fichier pointeur dans lequel il stocke des références aux grands fichiers de données. Ces grands fichiers seront stockés ailleurs – soit dans le cache local Git LFS, soit sur un serveur distant comme [GitHub](https://docs.github.com/en/github/managing-large-files/collaboration-with-git-large-file-storage) ou [Gitlab](https://docs.gitlab.com/ee/topics/git/lfs/).

Pourtant, cela ne serait pas suffisant. Git LFS limite toujours la taille des fichiers (environ 2 Go) et n'est pas une solution complète pour la data science. Il ne fournit pas d'informations utiles sur ce qui a changé pour les versions de grands fichiers (uniquement les changements basés sur le texte dans le fichier pointeur). Vous n'aurez également pas accès aux visualisations ou aux graphiques avant et après.

Git LFS ne supporte pas non plus les diffs hors de la boîte, il est donc assez difficile d'examiner la différence entre les versions successives d'un fichier.

## Option 2 : Utiliser DVC pour le contrôle de version dans les projets de data science

Une meilleure option est d'utiliser [DVC](https://dvc.org/). DVC, qui signifie data version control, est essentiellement comme Git mais a été conçu spécialement pour les données.

Et la syntaxe de DVC est similaire à celle de Git ! Donc, si vous connaissez déjà Git, apprendre DVC ne sera pas difficile. DVC suit facilement les grands fichiers – ce qui rend la réutilisabilité et la reproductibilité un jeu d'enfant.

Avec DVC, vous pouvez :

* suivre et sauvegarder des données et des modèles de machine learning de la même manière que vous capturez du code
* créer et basculer entre différentes versions de données et de modèles de ML facilement
* comprendre comment les ensembles de données et les artefacts de ML ont été construits en premier lieu
* comparer les métriques de modèles entre les expériences
* adopter des outils d'ingénierie et des meilleures pratiques dans les projets de data science

Mais DVC ne facilite que le contrôle de version localement. Pour le configurer pour la collaboration à distance, vous devez le connecter à un [stockage distant](https://dvc.org/doc/command-reference/remote#description). Le problème est que la configuration de ce stockage cloud est tout simplement trop compliquée.

Prenons Amazon S3, par exemple. Vous devrez fournir votre carte de crédit, installer l'outil AWS CLI, créer un utilisateur IAM, attribuer les permissions correctes (que la plupart des gens ne réussissent généralement pas du premier coup), et ainsi de suite.

C'est tout simplement trop compliqué. Ce niveau de friction peut décourager les gens de contribuer au projet – ce qui est le but même de la collaboration à distance.

Les choses devraient être aussi simples que créer un compte et faire un Git push. Le contrôle d'accès devrait également être géré automatiquement.

Et c'est là que DagsHub Storage intervient.

## Option 3 : Utiliser DVC + DAGsHub Storage pour le contrôle de version et la collaboration à distance

[DAGsHub Storage](https://dagshub.com/docs/reference/onboard_storage/) est une alternative (et gratuite) DVC remote qui ne nécessite aucune configuration. Il s'agit d'un nouvel outil des créateurs de DAGsHub, une plateforme web pour le contrôle de version des données et la collaboration pour les data scientists et les ingénieurs en machine learning (DAGsHub est à DVC ce que Github est à Git).

Avec DAGsHub storage, vous n'avez pas à subir le stress de la configuration de quoi que ce soit. Cela fonctionne de la même manière que l'ajout d'un Git remote.

Lorsque vous créez un dépôt sur DagsHub, il vous fournit automatiquement une URL DVC remote. Avec cette URL, vous pouvez rapidement pousser et tirer des données en utilisant vos identifiants DAGsHub existants (via l'authentification basique HTTPS).

Cela signifie également que le partage du travail avec des utilisateurs non-DVC est beaucoup plus facile, car il n'y a pas de configuration cloud requise de leur côté. N'est-ce pas bien mieux ?

Pour connecter DAGsHub Storage comme votre stockage distant, vous devez créer un compte sur DAGsHub et créer un projet. Vous pouvez le faire soit en créant un projet à partir de zéro, soit en vous connectant à un projet existant sur une autre plateforme comme Github ou Bitbucket, et [configurer DVC pour le versionnement local des données](https://dagshub.com/docs/experiment-tutorial/2-data-versioning/).


![Image](https://lh5.googleusercontent.com/pptgXgKjG8tKKl1edmThDD-fsvmckeNcOTo5lBlT3bnexEr_JgQWvaHd6z0OkLdvBF9EG5fHDnnvsRuCBppijm4QbkEJFalBGdCs-QdRnaPQFa7buMwmI6r5ez70px1yec3isZhx)
_Création d'un nouveau dépôt sur DAGsHub._

Lorsque vous créez un dépôt sur DAGsHub, vous obtenez deux remotes : Git et DVC.

![Image](https://lh4.googleusercontent.com/HzmNRfDG774q_7TeuwytoXTk2qmbEwxlrzofsYBu0rosNI_oHfp8nZK0O_hc0w7v2vxrTTONyHrJmusQe2BXMkljb699aN2dYolx_Xgf9gbLcepxChanbTn4bghIKH6jiivdnDFu)

Pour commencer à utiliser DAGsHub storage, copiez le lien DVC (que vous pouvez trouver sur la page d'accueil de votre dépôt) et ajoutez-le comme remote pour votre projet local.

Ouvrez votre projet dans un terminal et ajoutez le remote DVC :

```
dvc remote add <--dvc remote link-->

```

La prochaine étape consiste à configurer les identifiants DAGsHub pour votre machine locale, de la même manière que vous le feriez pour GitHub :

```
dvc remote modify origin --local auth basic
dvc remote modify origin --local user Linda-Ikechukwu
dvc remote modify origin --local ask_password true
```

Et voilà ! Vous pouvez maintenant pousser ou tirer des ensembles de données et des modèles de manière transparente avec `dvc push -r origin` ou `dvc pull -r origin`.

Si vous souhaitez basculer vers différentes versions de vos données, tout comme vous le faites avec git checkout, tout ce que vous avez à faire est d'exécuter :

```
git checkout <..branch or commit..>
dvc checkout

```

Qu'y a-t-il de plus ? Vous pouvez également recevoir et fusionner des pull requests pour votre projet avec [DAGsHub pull requests](https://dagshub.com/docs/collaborating_on_dagshub/data_science_pull_requests/).

## Conclusion

Avec DAGsHub Storage, le partage de données et de modèles devient aussi simple que le partage d'un lien, offrant aux collaborateurs un aperçu facile des données du projet, des modèles, du code, des expériences et des pipelines.

Tout cela offre une meilleure expérience collaborative pour les équipes de data science et aidera, espérons-le, au développement massif et à l'acceptation des projets Open Source Data Science (OSDS).

Vous cherchez plus d'articles comme celui-ci ?

Je m'appelle Linda et je suis une développeuse Frontend. Je tiens un blog : [codewithlinda](https://www.codewithlinda.com/blog/), destiné aux développeurs frontend en croissance où j'écris sur la façon d'obtenir et de survivre à votre premier emploi dans la tech, ainsi que des conseils techniques pour vous aider à monter en niveau. Vous pouvez également me trouver sur Twitter à @[_MsLinda](https://twitter.com/_MsLinda).