---
title: 5 Astuces Terminal Géniales pour Vous Aider à Progresser en tant que Développeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-21T03:04:36.000Z'
originalURL: https://freecodecamp.org/news/terminal-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/termtrick.png
tags:
- name: command line
  slug: command-line
- name: terminal
  slug: terminal
- name: tips
  slug: tips
seo_title: 5 Astuces Terminal Géniales pour Vous Aider à Progresser en tant que Développeur
seo_desc: 'By Jackson Bates

  There are plenty of beginner tutorials around that help you learn command line basics,
  such as cd, ls, pwd and so on...but what about that fancy magic you''ve seen more
  experienced developers use?

  Here are my five favourite terminal c...'
---

Par Jackson Bates

Il existe de nombreux tutoriels pour débutants qui vous aident à apprendre les bases de la ligne de commande, comme `cd`, `ls`, `pwd`, etc... mais qu'en est-il de cette magie sophistiquée que vous avez vue utilisée par des développeurs plus expérimentés ?

Voici mes cinq commandes et utilitaires de terminal préférés (dans un ordre quelconque), pour vous aider à vous sentir comme le magicien que vous aspirez à être ! Cela est basé sur Ubuntu, mais devrait être similaire sur d'autres plateformes (avec peut-être un peu de recherche Google).

Si vous souhaitez mentionner comment obtenir des résultats similaires sur MacOS ou Windows, ou si vous avez d'autres astuces de terminal que vous aimeriez partager, faites-le moi savoir dans les commentaires ci-dessous.

_Ceci est adapté de ma récente [vidéo YouTube](https://www.youtube.com/watch?v=CmNTuq7M71U), que vous pouvez regarder pour voir ces astuces en action !_

## sudo !!

`sudo !!` (ou comme j'aime à crier SUDO BANG BANG) répétera la dernière commande que vous avez tapée, mais avec `sudo` devant.

Si vous avez déjà oublié d'utiliser votre privilège `sudo` lorsque vous faites quelque chose qui nécessite vos identifiants d'administrateur (comme `apt update` par exemple), alors `sudo !!` est un moyen pratique de le corriger sans avoir à retaper toute la commande.

## tig

`tig` et `tig status` sont probablement les outils que j'utilise le plus souvent dans mon travail quotidien.

Les plus observateurs parmi vous auront peut-être remarqué que c'est `git` épelé à l'envers, et en effet `tig` est un excellent utilitaire git.

L'un des points faibles de git pour moi est le manque d'interactivité disponible dans certaines des actions de base. Par exemple, bien que `git log` et `git status` me donnent des informations utiles, cela nécessite plus de commandes git manuelles pour faire quelque chose d'utile avec ces informations.

`tig` agit comme `git log`, mais vous permet de naviguer vers le haut et vers le bas dans le journal, et d'examiner le contenu de chaque commit depuis la ligne de commande.

`tig status` agit comme `git status` sauf qu'il permet également la même navigation que `tig`, et il vous permet également d'ajouter des fichiers à la zone de staging facilement depuis la ligne de commande.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/tig.png)

Les deux commandes peuvent être navigées en utilisant les touches `j` et `k` pour monter et descendre, et en appuyant sur `enter`, vous ouvrirez les informations sur le fichier (comme la différence de commit). `q` permet également de quitter chaque commande.

Pour ajouter ou supprimer des fichiers spécifiques de votre zone de staging dans git, il suffit de presser `u`.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/tigstatus.png)

Maintenant, lorsque vous allez faire `git commit...` comme d'habitude, vos fichiers ont déjà été ajoutés, donc pas besoin d'utiliser la commande `git add`.

## grep

C'est une astuce très connue mais elle est incroyablement utile tout de même.

`grep` vous permet de retourner les lignes pertinentes d'une sortie de texte qui correspondent à un motif particulier que vous lui passez.

Par exemple, si vous cherchez dans un long fichier `.log` une erreur, il peut être difficile de la voir parmi toutes les sorties non pertinentes. Grep peut réduire votre recherche aux seules lignes pertinentes.

Exemple : `grep error system.log`

Avec d'autres commandes qui produisent beaucoup de sortie de terminal, vous pouvez les rediriger vers `grep error` pour faire de même. Par exemple, si vous vouliez regarder vos routes Rails, mais que vous ne vous intéressiez qu'à celles liées à l'admin, vous pourriez faire ceci :

`rake routes | grep admin`

## history

`history` retourne simplement toutes les commandes que vous avez jamais tapées dans votre terminal. Pourquoi est-ce utile ? Eh bien, si, comme moi, vous êtes très oublieux, la commande `history` peut vous montrer ce que vous avez fait auparavant pour rafraîchir votre mémoire.

Par exemple, chaque fois que je dois restaurer une sauvegarde de base de données, je ne peux jamais me souvenir de la syntaxe. `history | grep pg_restore` me montrera chaque fois que j'ai utilisé la commande `pg_restore`, avec les flags et arguments exacts que j'ai dû utiliser.

Remarquez l'utilisation de `grep` pour affiner la recherche ? Travaillez intelligemment, pas dur !

## spd-say

Cela peut être réalisé de plusieurs manières, et avec divers outils sur chaque plateforme. `spd-say` est l'utilitaire de synthèse vocale par défaut d'Ubuntu.

En utilisant la capacité de votre terminal à enchaîner des commandes, vous pouvez utiliser l'outil de synthèse vocale de votre choix pour vous dire quand un processus long est terminé.

Exemple : `sudo apt update; spd-say done`

Remarquez le `;` entre les commandes ? Cela exécutera essentiellement `apt update` jusqu'à la fin, puis invoquera la commande suivante. Dans ce cas, il dira utilement 'done' quand ce sera terminé.

N'hésitez pas à le faire dire 'booyah!' si vous avez l'impression que votre journée a besoin de plus de célébrations de petites victoires.

---

## Partagez les vôtres avec moi !

Les développeurs adorent deux choses : les autocollants pour ordinateur portable et les commandes de terminal élégantes. J'ai plus de place pour les autocollants, mais j'adorerais entendre vos commandes de terminal préférées dans les commentaires ci-dessous !

Vous pouvez également me contacter sur Twitter [@JacksonBates](https://twitter.com/jacksonbates)