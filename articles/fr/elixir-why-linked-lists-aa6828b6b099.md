---
title: Pourquoi Elixir utilise des listes chaînées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T03:12:13.000Z'
originalURL: https://freecodecamp.org/news/elixir-why-linked-lists-aa6828b6b099
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L8v2RUaCgJ2O1YiWqQTGwQ.png
tags:
- name: Computer Science
  slug: computer-science
- name: Elixir
  slug: elixir
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Pourquoi Elixir utilise des listes chaînées
seo_desc: 'By Edison Yap

  I’ve always thought data structures are cool, but you know what’s cooler? Seeing
  them in the wild!

  While going through Elixir’s docs, I saw that Elixir uses linked lists under the
  hood for their linear data structures. I thought this wa...'
---

Par Edison Yap

J'ai toujours pensé que les structures de données étaient cool, mais vous savez ce qui est encore plus cool ? Les voir en action !

En parcourant la documentation d'Elixir, j'ai vu qu'Elixir utilise des listes chaînées sous le capot pour leurs structures de données linéaires. J'ai trouvé cela cool, mais quelque chose m'a frappé ; je comprenais les tableaux et les listes chaînées, mais je n'avais aucune idée de leur relation avec les langages de programmation. Cela m'a tracassé depuis, et j'avais besoin de trouver pourquoi les listes chaînées étaient utilisées... d'où cet article !

Donc, revenons à l'article : d'après ce que j'ai trouvé jusqu'à présent, il y a trois raisons pour lesquelles Elixir fait cela (et je pourrais avoir totalement tort, n'hésitez pas à me corriger !). Passons-les en revue une par une :

### Données Immuables

Dans Elixir (et en fait dans la plupart des langages fonctionnels), les données sont immuables. C'est une première étape importante pour comprendre pourquoi les listes chaînées sont utilisées, alors explorons cela.

> _Immuable signifie que, une fois les données déclarées, elles ne peuvent plus être mutées/modifiées._

En supposant que vous savez comment les tableaux fonctionnent sous le capot (consultez [mon autre article](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg) si vous voulez une piqûre de rappel), regardons ce qui se passe si nous essayons d'implémenter l'immuabilité avec un tableau !

Un tableau est défini comme un bloc continu de mémoire. Le problème avec cela est qu'un tableau de 5 éléments est toujours juste UN tableau, et lorsque nous ajoutons/suprimons un élément, nous le MUTONS. Comment pouvons-nous utiliser l'immuabilité avec les tableaux alors ? Ce n'est pas impossible, mais regardons pourquoi ce n'est pas pratique.

Si nous voulons imposer une véritable immuabilité dans les tableaux, cela signifie que nous devons faire une copie complète de l'ancien tableau chaque fois que nous voulons ajouter/supprimer dans le tableau.

Ce qui signifie que si vous avez un tableau de taille 5, si vous voulez ajouter un nouvel élément au tableau, votre utilisation de mémoire est instantanément doublée (parce que vous devez garder l'ancien tableau tel quel, et vous devez également créer un nouveau tableau des mêmes éléments). Et ce n'est que la complexité spatiale — il y a aussi la complexité temporelle à laquelle nous devons penser !

Une liste chaînée n'a pas les mêmes contraintes, car les nœuds sont tous stockés séparément en mémoire, ce qui signifie que nous n'avons pas vraiment à nous soucier de la complexité spatiale/temporelle lors de l'ajout/suppression de nœuds dans la liste.

Cela nous donne notre première raison pour laquelle elle utilise une liste, cependant ce n'est pas toute l'histoire. C'est là que le partage structurel/récursif de queue intervient et que tout commence à avoir du sens.

### Structure Récursive

Avez-vous remarqué que les listes chaînées sont récursives par définition ?

Par exemple, `A -> B -> C -> D` est une liste chaînée, mais `B -> C -> D`, `C -> D` et ainsi de suite le sont aussi, et chaque liste chaînée n'est qu'une sous-structure d'une autre liste chaînée !

Ce n'était pas très excitant en soi, mais c'est vital pour la prochaine pièce du puzzle !

> Fait Amusant : La nature récursive couplée au fait que les données doivent être immuables (donc vous ne pouvez pas avoir de compteur de boucle) est pourquoi les langages fonctionnels sont généralement associés à la récursion — ils doivent kinda !

### Partage Structurel/Queue

Donc, nous savons que les listes chaînées sont récursives par nature. Combiné avec la nature immuable du langage, nous savons que les données ne peuvent jamais changer.

C'est intéressant, car maintenant nous pouvons dire en toute confiance que `A -> B -> C -> D` est une liste différente de `B -> C -> D` (même si l'une contient récursivement l'autre). Parce que nous avons cette garantie (avec le fait qu'une liste NE PEUT PAS changer), nous n'avons pas à définir les mêmes données deux fois, et nous pouvons réutiliser les listes chaînées existantes ! Cela s'appelle le partage structurel.

Génial, n'est-ce pas ? Regardons un exemple.

e.g :

Maintenant nous avons TROIS listes différentes ! `list`, `list_one` et `list_two`, mais elles partagent toutes la même référence (la queue) et la seule différence entre elles est le pointeur de tête.

Cela signifie qu'il y aura un total de 6 éléments en mémoire. Ajouter à la liste a un faible coût en mémoire, tout en conservant l'immuabilité que nous désirons.

Réutilisable, baby !

![Image](https://cdn-media-1.freecodecamp.org/images/1*b31hiO4ynbDLRrXWEFF4aQ.png)

Si vous voulez lire un peu plus, vous pouvez consulter [les arbres Trie](https://en.wikipedia.org/wiki/Trie) qui ont les mêmes concepts de partage de données/préfixes !

### Collecte des Déchets & Mise en Cache ?

Ces deux points ne sont pas tout à fait clairs pour moi, mais j'ai entendu dire que les listes chaînées sont bonnes pour les GC et que le partage de queue fait un bon candidat pour la localité de référence/la mise en cache (je ne comprends pas comment, car elles ne sont pas stockées au même endroit). J'apprécierais que quelqu'un veuille donner son avis !

### Note de Clôture

Note de côté : en réalité, ce n'est pas tant une question d'Elixir puisqu'il compile en Erlang. Mais ce n'est pas non plus une question d'Erlang, car tous les langages de programmation fonctionnels font à peu près la même chose... mais c'est ce qui a suscité ma curiosité, d'où les liens avec Elixir.

En écrivant cet article, j'ai trouvé que je devais écrire en profondeur sur le fonctionnement des tableaux avant de pouvoir plonger dans la partie Elixir, alors je l'ai publié comme [un autre article ici](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg) à la place. Lisez-le pour mieux comprendre le compromis !

[**Comment les tableaux fonctionnent de la manière dont les tableaux fonctionnent**](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg)  
[_En informatique, il y a le concept de structure de données linéaire, ce qui signifie que les données sont structurées dans un..._dev.to](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg)

Je n'ai pas non plus vraiment parlé de la notation Big O, car j'ai pensé que cela pourrait ajouter un temps de lecture et une complexité inutiles à l'article, mais c'est assez vital et fondamental en informatique, alors je vous suggère de vous rafraîchir un peu la mémoire.

Si vous êtes du genre podcast, il y a [BaseCS](https://www.codenewbie.org/basecs) par CodeNewbie, co-animé par Vaidehi Joshi et Saron.

Si vous voulez lire, la version blog de Vaidehi Joshi (qui est ce qui a inspiré le podcast, je crois) est également excellente sur [BaseCS Medium](https://medium.com/basecs).

Pour les vidéos, [MyCodeSchool](https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P) est incroyable et c'est pratiquement là que j'ai appris tout ce que je sais maintenant, fortement recommandé !

Autrement, j'espère que vous avez tous apprécié l'article autant que j'ai apprécié l'écrire !

### Sources

[https://elixir-lang.org/getting-started/basic-types.html#linked-lists](https://elixir-lang.org/getting-started/basic-types.html#linked-lists) — La pièce qui a suscité cet article

_Originalement publié sur [dev.to](https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d)_