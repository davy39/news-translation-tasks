---
title: Comment se débloquer lorsque vous êtes confronté à un mur en programmation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-14T15:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-unstuck
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/get_unstuck-1.jpg
tags:
- name: Problem Solving
  slug: problem-solving
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
seo_title: Comment se débloquer lorsque vous êtes confronté à un mur en programmation
seo_desc: 'By Amy Haddad

  Getting stuck is part of being a programmer, no matter the level. The so-called
  “easy” problem is actually pretty hard. You’re not exactly sure how to move forward.
  What you thought would work doesn’t.

  The other part of being a programm...'
---

Par Amy Haddad

Être bloqué fait partie intégrante de la vie d'un programmeur, quel que soit son niveau. Le prétendu problème "facile" est en réalité assez difficile. Vous n'êtes pas tout à fait sûr de la manière de progresser. Ce que vous pensiez fonctionner ne fonctionne pas.

L'autre partie de la vie d'un programmeur consiste à se débloquer soi-même.

Je me suis retrouvé bloqué plusieurs fois récemment, donc trouver des moyens de me *débloquer* a été omniprésent dans mon esprit. Voici quelques tactiques que j'ai utilisées. Peut-être pourront-elles vous aider aussi.

## Rendre le problème concret

Créez un diagramme, faites un croquis rapide ou utilisez des objets réels pour vous donner une représentation visuelle. Cela rendra le problème beaucoup plus facile à réfléchir.

Un problème auquel j'ai été confronté me demandait de trouver la différence absolue entre les sommes des diagonales d'une matrice carrée. C'est un peu compliqué et difficile à garder en tête. J'ai donc dessiné : j'ai créé une matrice carrée de nombres et j'ai encerclé les diagonales.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/2020-01-15-12.58.06.jpeg)

Un simple croquis a littéralement fait apparaître les étapes devant moi : faire la somme d'une diagonale (qui est 15), puis de l'autre (qui est 17), et enfin trouver la différence absolue entre elles (qui est 2).

Cette approche s'applique à d'autres problèmes aussi. Lorsque j'apprenais les boucles for, j'ai itéré à travers une pile d'amandes. Lorsque je travaille sur un problème récursif, je fais un diagramme pour voir ce qui se passe sur la pile d'appels jusqu'à atteindre mon cas de base.

Le point commun est le suivant : rendre l'abstrait concret.

## Écrire exactement ce que vous essayez de faire

Écrivez l'étape spécifique sur laquelle vous travaillez lorsque vous sentez le cycle trop familier de "tourner en rond" vous envahir.

Les cinq ou dix secondes qu'il faut pour noter quelques mots sur un morceau de papier vous aideront à solidifier votre processus de réflexion et à rediriger votre attention.

Voici quelques exemples :

* Stocker les noms de cours comme clés dans l'objet
* Passer l'argument à la fonction de rappel
* Réinitialiser la variable "maxValue" à 0

Réinitialiser la variable "maxValue", par exemple, n'a pas résolu le problème. Mais c'était une étape importante dans le processus. Écrire cette courte phrase m'a remis sur la bonne voie : c'était un rappel de ce que j'avais entrepris de faire. Cela m'a également assuré de me concentrer sur une seule chose, et non sur plusieurs.

Donc, la prochaine fois que vous vous surprenez à essayer la même approche encore et encore et à obtenir le même résultat, arrêtez-vous et demandez-vous : "Qu'est-ce que j'essaie exactement de faire ici ?"

Ensuite, écrivez—oui, écrivez—votre réponse sur un morceau de papier.

Ce n'est pas suffisant de simplement penser à votre réponse. Si je "pense" simplement à moi-même, je vais précipiter le processus et ne pas gagner grand-chose (si quelque chose). Je dois l'écrire.

## Simplifier votre entrée donnée

Il est beaucoup moins intimidant de travailler avec quelques éléments plutôt qu'avec beaucoup. C'est pourquoi il est utile de simplifier votre entrée donnée.

Un problème m'a donné une liste de trois dictionnaires. Il n'y avait *que* trois dictionnaires, mais c'était encore deux de trop.

```
noms = [
    {'prénom':'John', 'nom':'Smith', 'email':'johns@example.com'},
    {'prénom':'Mary', 'nom':'McDonald', 'email':'marym@example.com'},
    {'prénom':'Sam', 'nom':'Davey', 'email':'samd@example.com'}
]
```

Mon travail était de trier chaque dictionnaire par nom de famille, puis par prénom (c'est-à-dire, Davey, Sam : samd@example.com). Cependant, le problème était plus facile à réfléchir lorsque j'ai réduit la liste de trois dictionnaires à une liste d'un seul.

```
nom = [
    {'prénom':'John', 'nom':'Smith', 'email':'johns@example.com'}
]
```

J'ai résolu le problème en utilisant un seul dictionnaire. Ensuite, j'ai appliqué la même logique au problème plus large en question.

Lorsque vous simplifiez votre entrée donnée, vous rendez le problème beaucoup plus gérable.

## Résoudre un problème plus petit

Repérer les motifs plus facilement et comprendre ce que l'on vous demande *réellement* de faire lorsque vous résolvez une version plus petite du problème.

Voici un exemple de problème du livre de Reuven Lerner, *Python Workout* :

"Utilisez une compréhension de liste pour inverser l'ordre des mots des lignes dans un fichier texte. C'est-à-dire, si la première ligne est abc def et la deuxième ligne est ghi jkl, alors vous devez retourner la liste ['def abc', 'jkl ghi']."

Lorsque je résous une version plus petite d'un problème, je trouve utile de supprimer les couches de complexité et d'utiliser ma structure de données idéale. Dans cet exemple, cela signifiait ignorer le fichier texte et la compréhension de liste (couches de complexité) et utiliser une liste (ma structure de données idéale).

Ensuite, j'ai résolu le problème. J'ai ouvert mon éditeur et tapé ma structure de données idéale.

```
lettres = ['abc def', 'ghi jkl']
```

J'ai inversé l'ordre et obtenu le résultat attendu en utilisant une boucle for.

```
lettres_inversees = []
for lettre in lettres:
   liste_lettres = lettre.split(" ")
   liste_lettres.reverse()
   lettres_inversees.append(" ".join(liste_lettres))
```

Une fois que cela a fonctionné, j'ai réajouté les couches de complexité une par une jusqu'à ce que je résolve le problème tel que demandé dans l'énoncé.

Résoudre une version plus petite du problème aide à atteindre le cœur de ce que vous devez faire. C'est aussi une autre façon de rendre le complexe simple.

## Faire une pause

Votre cerveau ne cesse pas de penser simplement parce que vos doigts arrêtent de taper.

Est-ce qu'une idée vous est déjà "venue" à l'esprit alors que vous faisiez autre chose que de la programmation ? Êtes-vous déjà revenu à un problème après une séance de sport et la solution vous a sauté aux yeux ? Cela m'est arrivé.

Ce n'est pas une coïncidence si vous avez eu votre idée ou solution lorsque vous faisiez autre chose—lorsque vous ne travailliez pas délibérément. "Les épiphanies peuvent sembler venir de nulle part," explique [Scientific American](https://www.scientificamerican.com/article/mental-downtime/), "mais elles sont souvent le produit d'une activité mentale inconsciente pendant les temps d'arrêt."

Si vous avez l'impression de vous heurter à un mur de briques, c'est peut-être bien le cas. Il est peut-être préférable de faire une pause. Donnez à votre esprit le temps de digérer ce sur quoi vous travaillez et revenez au problème avec un nouvel élan.

## Travailler en binôme avec un autre programmeur

Travailler avec quelqu'un d'autre peut être un excellent moyen de générer des idées et de voir un problème sous un autre angle. Mais je vous recommande vivement de tout faire pour vous débloquer vous-même en premier.

Il y aura toujours des obstacles. Apprendre à résoudre vos propres problèmes est une compétence cruciale à acquérir. Il est facile de dire "Je ne comprends pas. Laissez-moi demander à cet ingénieur senior." Ensuite, laissez l'ingénieur senior résoudre le problème pour vous. Il est plus difficile de le résoudre soi-même, mais vous devez au moins essayer.

Si vous avez sincèrement fait de votre mieux, alors contactez un programmeur avec une question spécifique. Cela montre du respect pour le temps de l'autre programmeur et cela rendra votre session de binôme plus efficace.

Ensuite, demandez un indice—ne laissez pas le programmeur résoudre le problème pour vous. Vous rencontrerez sans doute une situation similaire à l'avenir, alors utilisez la session de binôme comme une opportunité d'apprentissage. Cela vous aidera à long terme.

## Conclusion

Être bloqué est frustrant, c'est certain. Vous pouvez essayer une seule des tactiques ci-dessus et avoir un moment "eureka", ou vous pouvez avoir besoin d'essayer une combinaison et vous retrouver à avancer lentement pendant le processus.

Mais il y a deux choses que j'ai apprises en embrassant la lutte : j'apprends beaucoup et la percée arrive. Continuez ainsi.

*J'écris sur l'apprentissage de la programmation et les meilleures façons de s'y prendre* ([amymhaddad.com](https://amymhaddad.com/)).