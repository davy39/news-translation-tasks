---
title: 5 utilitaires Linux pour améliorer votre flux de travail de programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-24T11:55:00.000Z'
originalURL: https://freecodecamp.org/news/5-linux-utilities-for-better-programming-workflow
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/linux-shell-utilities-cover.jpeg
tags:
- name: Linux
  slug: linux
- name: Productivity
  slug: productivity
- name: workflow
  slug: workflow
seo_title: 5 utilitaires Linux pour améliorer votre flux de travail de programmation
seo_desc: 'By Rishabh Rawat

  Working as a Software Developer, there are always new tools and frameworks coming
  out that can completely change your workflows – for the better (or worse?).

  Either way, there is always the possibility to optimize how you do things d...'
---

Par Rishabh Rawat

En tant que développeur logiciel, il y a toujours de nouveaux outils et frameworks qui sortent et qui peuvent complètement changer vos flux de travail – pour le mieux (ou le pire ?).

Dans tous les cas, il y a toujours la possibilité d'optimiser la façon dont vous faites les choses au quotidien.

Cet article contient quelques utilitaires Linux qui ont récemment remplacé mon flux de travail de programmation quotidien surutilisé et peu productif.

Vous apprendrez à connaître ces utilitaires et comment ils constituent une meilleure alternative à leurs homologues.

Commençons.

## Comment utiliser Mcfly

Est-ce que vous appuyez sans relâche sur la touche `flèche vers le haut` du terminal jusqu'à obtenir la commande que vous avez exécutée précédemment ? J'ai été là. Je ne savais pas que je pouvais optimiser cela, alors je l'utilisais religieusement pendant assez longtemps.

Ensuite, j'ai découvert `ctrl + r`. Il vous permet de rechercher dans votre historique de commandes et dispose d'une recherche avec caractères génériques. Wow.

Résultats ? Mon exercice de tapotement de doigts était terminé dès le premier jour. Encore une fois, je pensais que cela devait être le sommet de l'expérience développeur pour un si petit utilitaire. Je me trompais tellement.

Alors quoi ? Eh bien, il y a un meilleur `ctrl-r` pour vous. Je vous présente Mcfly 🦋.

En plus de la fonctionnalité régulière `ctrl+r`, il a quelques extras sympas :

1. Les suggestions sont personnalisées à l'aide d'un réseau neuronal qui prend en compte votre répertoire de travail actuel et les commandes récemment exécutées.

2. Il suit le statut de sortie des commandes (vous ne voulez probablement pas exécuter à nouveau une commande qui a échoué), l'horodatage et d'autres informations utiles.

3. Vous pouvez utiliser `%` comme caractère générique pour faire correspondre plusieurs caractères.

Voici les suggestions que j'ai obtenues sur deux dépôts différents, basées sur mon historique de shell :

![mcfly donnant des suggestions contextuelles dans le shell](https://www.freecodecamp.org/news/content/images/2022/08/mcfly-in-git-project.png align="left")

*les suggestions incluent un script de build spécifique à ce projet*

![mcfly donnant des suggestions contextuelles dans le shell](https://www.freecodecamp.org/news/content/images/2022/08/mcfly-in-different-git-project.png align="left")

*le projet a un script de build différent*

Vous pouvez installer Mcfly depuis [ici](https://github.com/cantino/mcfly#installation).

## Comment utiliser Cheat.sh

Qui aime lire les pages de manuel ? Pas moi. Quand je lutte avec une commande, la dernière chose que je veux lire est une page de manuel. Non pas parce que ce n'est pas utile, mais parce que c'est accablant.

J'ai souvent juste besoin d'exemples rapides que je peux saisir à la volée et utiliser. Quand j'ai trouvé les [pages TLDR](https://tldr.sh/), j'étais la personne la plus heureuse. Maintenant, avec Cheat (sheets), je suis encore plus heureux.

Cheat vous donne accès aux [cheatsheets](https://github.com/cheat/cheatsheets/) pour potentiellement toutes les commandes dont vous aurez jamais besoin — seulement des exemples, sans l'encyclopédie.

Si vous ne voulez pas installer l'utilitaire, vous pouvez obtenir la cheatsheet en utilisant CURL comme ceci :

```bash
curl cheat.sh/uptime
```

Ainsi, au lieu d'installer les cheatsheets sur votre machine, vous récupérez les informations pour seulement la commande dont vous avez besoin. Vous pouvez visiter [cheat.sh](https://cheat.sh/) et l'utiliser sur votre navigateur également.

Voici à quoi ressemble la sortie de la commande ci-dessus :

![Sortie de la cheatsheet pour la commande uptime](https://www.freecodecamp.org/news/content/images/2022/08/Image-Pasted-at-2022-8-19-13-56.png align="left")

*Sortie de la cheatsheet pour la commande uptime*

Vous trouverez beaucoup d'exemples dans le [codebase](https://github.com/cheat/cheat).

## Comment utiliser Git Open

J'ai souvent besoin d'ouvrir le dépôt GitHub du projet sur lequel je travaille dans le navigateur. Cela peut être pour vérifier les mises à jour de commentaires sur la Pull Request que j'ai soumise, changer les paramètres du dépôt, ou tout ce qui nécessitera la page du dépôt GitHub.

Eh bien, nous avons même un utilitaire pour cela !

Exécuter `git open` ouvrira votre dépôt de travail actuel dans votre navigateur. Par défaut, il ouvre la page distante pour la branche sur laquelle vous vous trouvez. Vous pouvez même créer un alias pour les commandes afin d'éviter de tout taper.

Voici quelques idées d'alias pour vous :

```bash
alias go="git open"
alias blog="git open https://github.com/<username>/blog <branch>"
```

Consultez Git Open sur Github [ici](https://github.com/paulirish/git-open).

## Comment utiliser Bat

Nous avons tous utilisé `cat`, n'est-ce pas ? Bat est simplement cela mais avec une coloration syntaxique, de belles options de formatage et de style, et une prise en charge de git diff. Il est très polyvalent, s'intègre facilement avec d'autres outils et offre également des options de thématiques personnalisées.

Prenons un exemple. Voici notre fichier serveur express en utilisant `cat` :

![sortie de la commande cat](https://www.freecodecamp.org/news/content/images/2022/08/Image-Pasted-at-2022-8-19-16-26.png align="left")

*sortie de la commande cat*

La sortie ci-dessus n'a pas de coloration syntaxique, ce qui diminue la lisibilité du code. Faisons la même chose en utilisant `bat` :

![sortie de la commande bat](https://www.freecodecamp.org/news/content/images/2022/08/Image-Pasted-at-2022-8-19-16-27.png align="left")

*sortie de la commande bat*

Cela est clairement plus lisible. Il a la coloration syntaxique appropriée appliquée automatiquement (sans aucune configuration), fournit le nom du fichier et les numéros de ligne.

N'hésitez pas à commencer à l'utiliser [ici](https://github.com/sharkdp/bat).

## Comment utiliser Jq

Jq est un processeur de ligne de commande pour JSON. Vous pouvez découper votre JSON, effectuer une projection pour n'afficher que certains champs et extraire uniquement les informations requises d'un (énorme) JSON. Plus de débordement de la sortie du terminal.

```javascript
[
  {"value": 1, "rating": 2 },
  {"value": 2, "rating": 4 },
  {"value": 3, "rating": 5 }
]
```

L'accès à une clé depuis un tableau ressemble à ceci :

```javascript
jq '.[0] | { value }'
```

Nous demandons le premier élément du tableau et projetons uniquement le champ `value` :

```javascript
{
  "value": 1
}
```

Pour en savoir plus, rendez-vous sur leur [tutoriel officiel](https://stedolan.github.io/jq/tutorial/).

Ils ont également un terrain de jeu en ligne pratique. J'ai créé un extrait [ici](https://jqplay.org/s/E2-xscbiHba). N'hésitez pas à le modifier et à jouer avec.

Vous pouvez même aller plus loin avec [jid](https://github.com/simeji/jid). C'est un fouilleur JSON interactif qui utilise Jq. Il vous fournit des suggestions très pratiques et une fonctionnalité d'auto-complétion.

## Conclusion

Ce sont quelques-uns des utilitaires qui ont élargi l'horizon pour moi et m'ont fait réaliser qu'il y a toujours une meilleure façon de faire les choses. Vous devez simplement continuer à chercher sur Google. Commencez par "comment faire X" et "meilleures alternatives à X".

J'utilise ces utilitaires assez souvent dans mon flux de travail de programmation quotidien. J'espère qu'au moins l'un d'entre eux vous sera utile.

J'aimerais savoir quels utilitaires sont cruciaux pour votre flux de travail quotidien – utilisez-vous l'un de ceux mentionnés dans cet article ?

Aimez-vous l'article ? [Recevez des pilules d'amélioration bihebdomadaires sur le développement web backend](https://rrawat.com/newsletter) 💌.