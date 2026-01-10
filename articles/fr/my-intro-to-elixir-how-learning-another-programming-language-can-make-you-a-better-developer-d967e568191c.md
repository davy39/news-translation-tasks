---
title: 'Mon introduction à Elixir : comment apprendre un autre langage de programmation
  peut vous rendre meilleur développeur'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T00:33:19.000Z'
originalURL: https://freecodecamp.org/news/my-intro-to-elixir-how-learning-another-programming-language-can-make-you-a-better-developer-d967e568191c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-roj-FWdYdOaPvpF9qo-hw.jpeg
tags:
- name: Elixir
  slug: elixir
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Mon introduction à Elixir : comment apprendre un autre langage de programmation
  peut vous rendre meilleur développeur'
seo_desc: 'By Nikolas O''Donnell

  I attended ElixirConf EU in Warsaw earlier this year. It was actually my first ever
  programming conference. My colleague was giving a talk about Elixir and Phoenix
  called ‘Phoenix and the World of Tomorrow’.

  Now, my background is...'
---

Par Nikolas O'Donnell

J'ai assisté à ElixirConf EU à Varsovie plus tôt cette année. C'était en fait ma toute première conférence de programmation. Mon collègue donnait une conférence sur Elixir et Phoenix intitulée « Phoenix et le monde de demain ».

Maintenant, mon expérience est en JavaScript, mais mon entreprise est obsédée par Elixir. Ayant goûté au kool-aid de l'entreprise et vu ce qu'il peut faire — je suis assez bien converti.

JavaScript sera toujours mon premier langage et occupe une place spéciale dans mon cœur. Je l'utilise toujours, je l'apprends et je fais très beaucoup partie de la communauté JavaScript et React vibrante et en croissance.

Bien que je me familiarise avec Elixir pour le travail, j'ai fini par voir une grande valeur à apprendre un autre langage de programmation.

C'est une expérience similaire à l'apprentissage d'une nouvelle langue parlée. Vous êtes poussé hors de votre zone de confort. Devoir comprendre et raisonner d'une autre manière, même d'une autre perspective.

De plus, vous devez souvent reconstruire à partir de premiers principes — ce qui peut à son tour avoir les avantages supplémentaires de briser les hypothèses et les limitations préconçues.

C'est une chose saine à faire et en fin de compte, nous devrions être agnostiques en matière de langage, de bibliothèque et de framework.

Notre travail n'est pas réellement d'écrire du code, et certainement pas d'écrire un code dans un langage spécifique.

Plutôt, il s'agit de résoudre des problèmes pour nos entreprises, nos clients et nos clients.

Avoir d'autres langages, frameworks et paradigmes de codage à votre disposition lors de la résolution d'un problème augmente vos chances de le résoudre de manière meilleure. De plus, cela fait de vous un programmeur plus complet et un membre d'équipe précieux.

#### Explorer Elixir plus en profondeur

Elixir est un langage de méta-programmation relativement nouveau créé par Jose Valim et lancé en 2012.

La partie « méta » n'est pas juste moi qui essaie d'être « branché », « à la mode » et « dans le coup avec les enfants cool ». Cela donne une information supplémentaire sur ce qu'est Elixir.

Pour expliquer davantage Elixir, je suppose que je dois d'abord parler un peu d'Erlang. C'est parce qu'Elixir est construit sur Erlang (d'où la partie « méta »). Il s'exécute sur la machine virtuelle Erlang, appelée BEAM en raison d'un acronyme que je devrais [DuckDuckGo](https://www.freecodecamp.org/news/my-intro-to-elixir-how-learning-another-programming-language-can-make-you-a-better-developer-d967e568191c/undefined) pour découvrir.

Erlang a été créé par Joe Armstrong, Robert Virding et Mike Williams, alors qu'ils travaillaient pour Ericsson dans les années 1980.

Ericsson travaille dans le domaine des télécommunications. Ils avaient le problème de créer un logiciel robuste, tolérant aux pannes et asynchrone — pour que les appels ne tombent pas !

Chargés de cette mission, ces ingénieurs ont créé Erlang. L'ingénieur danois [Agner Krarup Erlang](https://en.wikipedia.org/wiki/Agner_Krarup_Erlang) est souvent cité comme l'homonyme... bien que ce soit aussi un choix assez pratique pour un langage **Er**icsson (je vous ai à l'œil 😉).

Revenons à Elixir. En tant que langage fonctionnel, il est super agréable de garder les choses ordonnées, organisées et lisibles.

Cette fonction fait cette tâche spécifique. Ce module fait cet ensemble de fonctions. Aucun n'a vraiment besoin de savoir ce que l'autre fait. Ce modèle de conception modulaire facilite le maintien d'une base de code propre.

Il est en fait considéré comme un langage multi-paradigme car il est fonctionnel, concurrent, distribué et orienté processus. Belle histoire — mais que signifie tout cela ?

* La **programmation fonctionnelle** utilise des fonctions (idéalement des « fonctions pures » où les entrées et les sorties sont clairement déclarées) sans valeurs cachées entrant ou sortant pour construire le programme. Le but est de supprimer les effets secondaires ou les sorties non intentionnelles du code.
* La **concurence** permet à un programme d'exécuter plusieurs calculs en même temps. Il n'a pas besoin d'attendre qu'une chose se termine avant de commencer une autre. Cela est appelé « bloquant » car l'exécution de l'élément suivant est bloquée jusqu'à ce que l'élément précédent soit terminé.
* **Distribué** décrit comment les informations sont échangées. Dans les systèmes distribués, les problèmes sont décomposés en tâches plus petites. Celles-ci sont complétées par l'échange de messages. Comme ces messages peuvent communiquer entre eux à travers des machines/réseaux, il est distribué.
* **Orienté processus** reflète également comment les problèmes sont décomposés en tâches ou processus plus petits et vise à séparer les structures de données des processus qui interagissent avec elles. La raison de vouloir faire cela est qu'elle permet aux programmeurs d'être plus assurés d'obtenir le résultat qu'ils attendent.

Voici à quoi ressemble le code Elixir :

![Image](https://cdn-media-1.freecodecamp.org/images/1*I2Z7z9DnrvgDAf2gb1WY6w.gif)
_[https://marketplace.visualstudio.com/items?itemName=mjmcloug.vscode-elixir](https://marketplace.visualstudio.com/items?itemName=mjmcloug.vscode-elixir" rel="noopener" target="_blank" title=")_

Propre, n'est-ce pas, et assez lisible — notez le schéma suivant :

```elixir
defmodule <Module_name> do

 def <something> do
  
  <the things to do>
  |> {you can use the pipe operator (|>) to parse..}
  |> {the result from a function..}
  |> {as the fist argument to the next function..}
  |> {creating a 'pipeline' with a final output..} 
  |> {of the entire cross function calls!}
  
 end
 
end
```

#### Mais où est toute la syntaxe supplémentaire ?

Eh bien, étant un nouveau langage, il a la chance de bénéficier du recul. Le langage emprunte certains des meilleurs aspects d'autres langages. Comme mentionné, il est construit sur Erlang et est en fait compatible — ce qui signifie que vous pouvez utiliser la syntaxe Erlang dans le code Elixir.

Il tire également parti de la syntaxe propre et de la structure de code de Ruby — son créateur venant d'un arrière-plan Ruby.

#### Phoenix

Phoenix est un framework web construit pour Elixir par Chris McCord. Vous pouvez penser à cela comme un moyen de démarrer un projet. Il est modulaire (grâce à Elixir). Il est également super rapide (grâce à Erlang), et en fin de compte très puissant.

Vous pouvez l'utiliser comme couche API entre votre base de données et votre front-end. Vous pouvez également facilement utiliser les modèles HTML et CSS qui accompagnent Phoenix. Vous pouvez utiliser Brunch JS pour injecter ces parties dans votre site web/application.

Alternativement, vous pourriez également utiliser un framework front-end comme Ember ou React pour faire de même — en faisant une approche « le meilleur des deux mondes ».

Voici la conférence que mon collègue Ley a donnée à ElixirConf EU dont j'ai parlé plus tôt. Cela vaut bien la peine d'être regardé, car il examine le rôle que Phoenix peut jouer dans les prochains milliards d'utilisateurs accédant à Internet sur des appareils < 3G :

Alors, si vous êtes intrigué, pourquoi ne pas goûter à Elixir ? Je pense que vous pourriez bien être accro.

Bien que dans tous les cas, goûtez à quelque chose de nouveau. Sortez de votre zone de confort de programmation et défiez-vous d'explorer un autre langage, une autre perspective et une autre façon de penser. Quel est le pire qui puisse arriver... ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*x49mx2qULeZcmfooM7cCOA.gif)
_[https://gfycat.com/gifs/detail/fewalarmingcaiman](https://gfycat.com/gifs/detail/fewalarmingcaiman" rel="noopener" target="_blank" title=")_