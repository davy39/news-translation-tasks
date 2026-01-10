---
title: Comment travailler avec les branches dans Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-09T21:42:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-branches-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/git-thumbnail.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment travailler avec les branches dans Git
seo_desc: 'By Deborah Kurata

  One of the things we fell in love with when we saw our future backyard was the tree.
  The valley oak is the largest North American oak. It can grow to be 600 years old
  and 100 feet tall. It''s known for its irregular, spreading branch...'
---

Par Deborah Kurata

L'une des choses dont nous sommes tombés amoureux lorsque nous avons vu notre future cour arrière était l'arbre. Le chêne de vallée est le plus grand chêne d'Amérique du Nord. Il peut vivre jusqu'à 600 ans et mesurer 100 pieds de haut. Il est connu pour ses branches étalées et irrégulières.

En parlant de branches... une fonctionnalité clé de Git est le branchement. Imaginez le tronc d'un arbre comme votre projet principal. Nous créons des branches pour séparer notre travail pour chaque tâche. Cela nous aide à isoler et à travailler sur une partie du projet sans impacter directement le projet principal jusqu'à ce que nous soyons prêts à fusionner nos modifications.

Explorons les concepts et apprenons à travailler avec les branches dans Git. Vous pouvez appliquer ces connaissances que vous utilisiez la ligne de commande ou un outil tel que GitHub Desktop ou l'intégration Git de VS Code.

Un tutoriel séparé explique les commandes pour travailler avec les branches. Vous pouvez également regarder la vidéo associée ici qui inclut des démonstrations utilisant VS Code.

%[https://youtu.be/_-SjD_k7uIY]

## Pourquoi utiliser les branches ?

Par défaut, lorsque nous initialisons un dépôt Git, Git crée une branche souvent appelée "main", bien que vous puissiez la voir avec d'autres noms. Nous ferons référence à la branche principale sous le nom de "main" tout au long de cet article.

Nous créons une branche séparée pour chaque problème ou fonctionnalité sur laquelle nous travaillons. Ainsi, pendant qu'une fonctionnalité est en cours, nous validons notre code dans la branche dédiée à cette fonctionnalité.

Par exemple, supposons que nous prévoyons de passer une semaine à travailler sur une fonctionnalité "Ajouter des commentaires" qui permet aux utilisateurs de commenter une recette. Pendant que nous travaillons, nous validons nos modifications dans la branche "Ajouter des commentaires".

Une autre personne de l'équipe travaille sur la mise à jour de l'avis de droits d'auteur sur toutes les pages de notre site. Elle valide ses modifications dans la branche "Ajouter les droits d'auteur".

Soudain, nous recevons une notification de nos utilisateurs indiquant que la connexion ne fonctionne pas. Nous créons une nouvelle branche pour corriger ce problème sans impacter les travaux partiellement terminés.

Lorsque le code de la branche "problème de connexion" est terminé, nous fusionnons la branche dans la branche principale. Et optionnellement, nous pouvons supprimer la branche fusionnée.

![Grand chêne avec "main" sur le tronc et les tâches sur les branches.](https://www.freecodecamp.org/news/content/images/2023/01/tree-branches.png)
_Figure 1. Version fonctionnelle dans la branche principale, travaux en cours dans les branches de fonctionnalités ou de problèmes_

Nous utilisons les branches pour maintenir une version fonctionnelle de notre code dans la branche principale, et le code partiellement terminé dans les branches de fonctionnalités ou de problèmes. Ainsi, notre branche principale aura toujours une version fonctionnelle du code.

Mais Git n'impose pas cela - plutôt, c'est à vous et à votre équipe de définir si et comment vous utiliserez les branches.

## Comment créer et changer de branches dans Git

Notre équipe construit un site web pour collecter et gérer des recettes. Nous créons un dépôt pour le projet avec Git. Par défaut, il crée la branche principale du projet, souvent appelée "main".

![Dossier de travail à gauche. Dépôt Git avec la branche principale à droite.](https://www.freecodecamp.org/news/content/images/2023/01/figure-2.png)
_Figure 2. Branche principale avec un commit._

À gauche dans la Figure 2 se trouve notre dossier de travail avec notre dépôt Git représenté comme une boîte. Cette boîte est agrandie à droite pour que nous puissions voir à l'intérieur. Et là, nous avons notre branche principale avec un seul commit. Le code dans notre dossier de travail correspond actuellement aux fichiers de ce commit le plus récent.

Nous commençons un projet pour mettre à jour le style du site web. Nous voulons nous assurer que notre travail sur cette tâche est isolé de notre code existant, nous créons donc une branche à partir de la branche principale.

Avant de commencer à travailler sur la branche, nous basculons vers cette branche. Ensuite, nous apportons des modifications pour notre tâche. Nous modifions un fichier, puis nous l'indexons et le validons dans la branche. Le résultat est montré dans la Figure 3.

![Dossier de travail à gauche. Dépôt Git à droite montrant la branche "changement de style".](https://www.freecodecamp.org/news/content/images/2023/01/figure-3.png)
_Figure 3. Branche "Changement de style" avec son premier commit._

À tout moment, si vous souhaitez travailler sur une branche, basculez vers cette branche. Basculer vers une branche extrait cette branche. Et le code dans notre dossier de travail est automatiquement modifié pour correspondre au code du dernier commit de cette branche. Tous les commits se font ensuite sur cette branche extraite.

À ce stade, l'un de nos utilisateurs signale un problème de connexion. Nous avons notre changement de style partiellement terminé, nous ne voulons donc pas faire notre correction dans cette branche.

Nous créons plutôt une autre branche à partir de la branche principale. Puisque nous l'avons créée à partir de la branche principale, le code initial de cette nouvelle branche est une copie du code de la branche principale. Elle n'a aucune de nos modifications de style.

Lorsque nous basculons vers cette branche, notre dossier de travail reflète le code de cette branche. Nous avons essentiellement réinitialisé notre dossier de travail au code de la nouvelle branche.

![Dossier de travail à gauche. Dépôt Git à droite montrant la branche "problème de connexion".](https://www.freecodecamp.org/news/content/images/2023/01/figure-4.png)
_Figure 4. Basculer vers la branche "problème de connexion" réinitialise le dossier de travail_

Nous corrigeons ensuite le problème de connexion dans cette nouvelle branche, modifions un fichier et indexons et validons la modification comme montré dans la Figure 5.

![Dossier de travail à gauche. Dépôt Git à droite avec la branche "problème de connexion"](https://www.freecodecamp.org/news/content/images/2023/01/figure-5.png)
_Figure 5. Branche "Problème de connexion" avec son premier commit._

Ce processus est-il clair à ce stade ? Parce que nous avons utilisé des branches, nous pouvons travailler sur d'autres problèmes lorsqu'ils surviennent sans impacter les tâches en cours.

## Comment fusionner des branches dans Git

Lorsque notre correction de connexion est terminée, nous fusionnons la branche "problème de connexion" dans la branche principale. La correction devient alors partie intégrante de notre code principal comme montré dans la Figure 6. Une fois la branche fusionnée, nous pouvons la supprimer.

![Dossier de travail à gauche. Dépôt Git montrant la fusion de la branche "problème de connexion" dans main](https://www.freecodecamp.org/news/content/images/2023/01/figure-6.png)
_Figure 6. Fusion de la branche "problème de connexion" dans main_

Maintenant, nous revenons à la branche "changement de style" pour terminer nos modifications. Le code dans notre dossier de travail est automatiquement basculé vers le code du dernier commit de cette branche de changement de style.

Nous apportons d'autres modifications de style et indexons et validons ces modifications dans la branche "changement de style". Le résultat est la Figure 7.

![Dossier de travail à gauche. Dépôt Git montrant les commits de la branche "changement de style"](https://www.freecodecamp.org/news/content/images/2023/01/figure-7.png)
_Figure 7. Branche "Changement de style" avec plusieurs commits_

Mais attendez... notre branche de code principale a maintenant notre correction de connexion, mais notre branche "changement de style" ne l'a pas.

À un moment donné, avant que la branche "changement de style" ne soit fusionnée dans main, nous devons intégrer la modification de connexion depuis main.

Nous fusionnons les dernières modifications de notre branche principale dans la branche "changement de style", en résolvant les éventuels conflits de fusion. Cela crée un autre commit comme montré dans la Figure 8. Remarquez que notre dossier de travail reflète maintenant les deux ensembles de modifications.

![Dossier de travail à gauche. Dépôt Git montrant la fusion de main vers la branche "changement de style"](https://www.freecodecamp.org/news/content/images/2023/01/figure-8.png)
_Figure 8. Fusion des modifications de main vers la branche "changement de style"_

Lorsque le changement de style est terminé, nous fusionnons la branche "changement de style" dans la branche principale.

Maintenant, notre branche principale contient toutes nos modifications, comme illustré dans la Figure 9. Et nous pouvons supprimer notre branche "changement de style".

![Dossier de travail à gauche. Dépôt Git à droite montrant la fusion de la branche "changement de style" dans main](https://www.freecodecamp.org/news/content/images/2023/01/figure-9.png)
_Figure 9. Fusion de la branche "changement de style" dans main_

Notez que la plupart des projets ont leur propre processus spécifique, leurs exigences et leurs préférences pour l'utilisation des branches, la définition des commits et la fusion des modifications. Assurez-vous de consulter la documentation du projet ou vos collaborateurs avant de créer des branches.

## Conclusion

Nous utilisons une branche pour isoler le travail sur une tâche, telle qu'une fonctionnalité, une modification ou un problème. Cela permet de garder notre branche principale exempt de code partiellement terminé ou non testé.

Nous pouvons avoir un nombre quelconque de branches de fonctionnalités définies à tout moment. Assurez-vous de basculer vers la branche appropriée avant d'indexer et de valider. Et fusionnez les modifications de la branche principale si nécessaire.

Lorsque la tâche est terminée, fusionnez la branche pour cette tâche dans main. Les branches sont destinées à être de courte durée et sont souvent supprimées après la fusion.

Pour plus d'informations sur Git et GitHub, consultez mon cours : ["Introduction en douceur à GitHub pour les débutants"](https://www.youtube.com/playlist?list=PLErOmyzRKOCoLfGDg91NbuGlRahF5mElq). Et pour des informations sur le développement web, y compris Angular, abonnez-vous à [ma chaîne YouTube](https://www.youtube.com/@deborah_kurata).

Maintenant, que diriez-vous d'une bonne sieste sous ces branches étalées ?