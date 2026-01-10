---
title: Comment j'ai découvert que C# SortedList utilise la recherche binaire, et pourquoi
  vous devriez vous en soucier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-27T07:12:53.000Z'
originalURL: https://freecodecamp.org/news/how-i-discovered-c-sortedlist-uses-binary-search-and-why-you-should-care-a88cce40f49b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wnTXS4cPw-Tw_oC79VweTQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment j'ai découvert que C# SortedList utilise la recherche binaire,
  et pourquoi vous devriez vous en soucier
seo_desc: 'By Rina Artstain

  There is an age old debate: can programmers make do with just knowing how to code?
  Or do they need to understand some of their framework internals, basic data structures,
  and search/sort algorithms?

  I have encountered many bugs creat...'
---

Par Rina Artstain

Il existe un débat ancien : les programmeurs peuvent-ils se contenter de savoir simplement coder ? Ou doivent-ils comprendre certains des mécanismes internes de leur framework, les structures de données de base et les algorithmes de recherche/tri ?

J'ai rencontré de nombreux bugs créés par une méconnaissance de la mise en œuvre des tables de hachage. Ou par une petite négligence qui aurait été un mystère complet pour quelqu'un qui ne savait même pas qu'une recherche binaire existait. Vous pouvez donc deviner que je suis de l'avis que vous devez avoir des connaissances de base en structures de données/algorithmes. J'espère qu'après avoir lu ceci, vous serez d'accord avec moi — mais si ce n'est pas le cas, vous pouvez laisser vos désaccords dans la section des commentaires ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wnTXS4cPw-Tw_oC79VweTQ.jpeg)

### Aperçu du système

Imaginez un système de représentants du service client, où chaque utilisateur écrit des notes pour suivre les actions et les conversations avec les clients. Si la note nécessite une action future, l'utilisateur peut ajouter une date d'échéance pour une date et une heure spécifiques, et elle devient une « tâche ». À tout moment, l'utilisateur peut marquer la tâche comme « terminée » et la tâche sera supprimée tout en restant dans la liste des notes.

Pour un accès facile, toutes les notes sont affichées dans un ordre décroissant par date d'insertion (la note la plus ancienne en premier). Les tâches sont affichées dans un ordre croissant par date d'échéance (les tâches à venir/en retard en premier).

Comme d'habitude, une partie de la complexité du système original est omise pour simplifier (persistance, multithreading, etc.). J'ai également inclus un lien vers GitHub avec une version fonctionnelle du code inclus dans cet article. Vous pouvez l'exécuter vous-même. (Il est en bas de l'article, donc même si vous ne le lisez pas, vous devrez faire défiler jusqu'en bas ha !).

### Mise en œuvre

Commençons par la définition de la classe Note :

C'est un simple objet de données.

Ensuite, nous allons créer une classe NotesManager qui contient toutes les notes/tâches et gère l'accès à celles-ci :

La classe NotesManager utilise une SortedList pour garder les Notes/Tâches dans le bon ordre déterminé par le type de la liste et la SortDirection donnée au NoteComparer. Les notes sont triées par InsertDate, ascendantes, et les tâches sont triées par DueDate, descendantes. La classe NotesManager s'occupe de créer le NoteIndex avec la bonne date. Elle insère la note dans la liste appropriée.

La dernière fonctionnalité dont nous avons besoin est de marquer une tâche comme « terminée », ce qui supprime ensuite la tâche de la liste des tâches.

À quoi pensais-je lorsque j'ai écrit ce code ? Je ne m'en souviens honnêtement pas. Probablement à pas grand-chose. C'est le problème sous-jacent de nombreuses erreurs.

Prenez une seconde avant de continuer à lire et essayez de comprendre où se trouve le problème.

### Que se passe-t-il ?

Imaginez ma surprise lorsque j'ai commencé à tester le NotesManager. J'ai découvert que lorsque je marquais certaines tâches comme « terminées », elles n'étaient pas supprimées de la liste des tâches. Cela semblait être totalement aléatoire, fonctionnant parfois et parfois non.

Me voilà, fixant le débogueur avec incrédulité. La tâche est là, juste devant moi, dans la liste des tâches, mais « remove » ne la supprimait pas. Je n'avais aucune idée de ce qui se passait.

J'ai supposé qu'il y avait un problème avec la mise en œuvre du NoteComparer. J'ai ajouté un point d'arrêt dans la méthode Compare. Là, j'ai trouvé quelque chose d'étrange : les tâches n'étaient pas scannées séquentiellement. Le débogueur semblait accéder de manière aléatoire aux éléments de la liste des tâches.

Hmmmm. Bizarre. Pendant une seconde, j'ai pensé qu'il pourrait y avoir un problème de multithreading, mais c'était un environnement de développement local — il n'y avait personne d'autre qui pouvait accéder à mon serveur web (et si c'était le cas, quelle était la probabilité qu'ils testent le même utilisateur et les mêmes données que j'utilisais actuellement ?). Non, la réponse devait être ailleurs.

Après quelques tests supplémentaires, un schéma est apparu. Le premier accès à Compare était quelque part au milieu de la liste. Ensuite, il a sauté à un autre endroit. Ensuite, un autre saut et un autre, avant de finalement abandonner. Puis est venu le moment #facepalm, et j'ai réalisé que SortedList devait utiliser la recherche binaire pour trouver des éléments dans la liste ! Cela aurait dû être évident (tout autre chose aurait été stupide, vraiment).

J'ai essayé de vérifier mon idée en recherchant dans la [Documentation MSDN](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.sortedlist-2?view=netframework-4.7.2), et là, c'était — [Remove](https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.sortedlist-2.remove?view=netframework-4.7.2#System_Collections_Generic_SortedList_2_Remove__0_) utilise la recherche binaire. OK, donc mon hypothèse était correcte — mais pourquoi la recherche binaire ne fonctionnait-elle pas ?

Cette fois, j'ai déplacé le point d'arrêt un peu plus bas dans la mise en œuvre du Comparer. J'ai immédiatement vu où était le problème. Je passais le NoteIndex avec seulement l'Id, en supposant que cela serait suffisant pour l'égalité.

Si cela avait été une liste régulière, cela aurait fonctionné. Mais couper ce coin en combinaison avec la recherche binaire (au lieu d'un scan séquentiel que je supposais implicitement) a résulté en l'incapacité de la SortedList à trouver la Note qu'elle cherchait. J'ai donc changé la mise en œuvre de « MarkDone ».

Et cela a fonctionné !

(Il y a aussi un bug dans cette mise en œuvre, mais je voulais me concentrer sur le problème en question. Pouvez-vous trouver le problème ?)

Vous pouvez télécharger un exemple fonctionnel qui montre le bug et sa solution [ici](https://github.com/rinaarts/NoteSystem).

### Points clés à retenir

Voici les points clés à retenir de ce cas :

1. Si vous utilisez un nouveau service ou une nouvelle structure de données, prenez 5 minutes pour lire la documentation. Si je l'avais fait et réalisé que la clé sur la SortedList était utilisée pour l'unicité et non seulement pour le tri, je n'aurais probablement pas fait l'erreur que j'ai faite.
2. Avoir une bonne compréhension des structures de données de base et des algorithmes est essentiel pour le travail quotidien. Ce type de bug est extrêmement difficile à trouver et à résoudre. Il se produit de manière sporadique sans logique apparente. Il est préférable d'éviter ce type de bug, mais si vous ne pouvez pas l'éviter — au moins soyez capable de l'analyser après qu'il se soit produit.

### Question bonus

Pourquoi ai-je remplacé GetHashCode() sur la classe Note ? Pourquoi devriez-vous **toujours** remplacer GetHashCode() si vous avez remplacé Equals() ?

Indice : quelle structure de données utilise les codes de hachage ?

Vous avez aimé ce que vous avez lu ? Partagez l'amour en applaudissant. Vous avez une question ou un commentaire ? Faites-le moi savoir dans la section des commentaires.