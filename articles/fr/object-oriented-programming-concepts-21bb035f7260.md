---
title: Comment expliquer les concepts de la programmation orientée objet à un enfant
  de 6 ans
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T22:16:19.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EirXoYV7GgRi4frvcW-b0A.jpeg
tags:
- name: interview
  slug: interview
- name: jobs
  slug: jobs
- name: object oriented
  slug: object-oriented
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment expliquer les concepts de la programmation orientée objet à un
  enfant de 6 ans
seo_desc: 'By Alexander Petkov

  Have you noticed how the same cliche questions always get asked at job interviews
  — over and over again?

  I’m sure you know what I mean.

  For example:


  Where do you see yourself in five years?


  or, even worse:


  What do you consider ...'
---

Par Alexander Petkov

Avez-vous remarqué comment les mêmes questions clichées sont toujours posées lors des entretiens d'embauche — encore et encore ?

Je suis sûr que vous voyez ce que je veux dire.

Par exemple :

> Où vous voyez-vous dans cinq ans ?

ou, encore pire :

> Quelle est, selon vous, votre plus grande faiblesse ?

Beurk… donnez-moi une pause. Je considère répondre à cette question comme une grande faiblesse ! Bref, ce n'est pas mon propos.

Aussi triviales que puissent être des questions comme celles-ci, elles sont importantes car elles donnent des indices sur vous. Votre état d'esprit actuel, votre attitude, votre perspective.

En répondant, vous devez être prudent, car vous pourriez révéler quelque chose que vous regretterez plus tard.

Aujourd'hui, je veux parler d'un type de question similaire dans le monde de la programmation :

> Quels sont les principes principaux de la programmation orientée objet ?

J'ai été des deux côtés de cette question. C'est l'un de ces sujets qui est posé si souvent que vous ne pouvez pas vous permettre de ne pas le connaître.

Les développeurs juniors et débutants doivent généralement y répondre. Parce que c'est un moyen facile pour l'intervieweur de déterminer trois choses :

1. **Le candidat s'est-il préparé pour cet entretien ?**   
Des points bonus si vous entendez une réponse immédiatement — cela montre une approche sérieuse.
2. **Le candidat est-il passé de la phase des tutoriels ?**   
Comprendre les principes de la programmation orientée objet (POO) montre que vous êtes allé au-delà du copier-coller des tutoriels — vous voyez déjà les choses d'une perspective plus élevée.
3. **La compréhension du candidat est-elle profonde ou superficielle ?**   
Le niveau de compétence sur cette question est souvent égal au niveau de compétence sur **la plupart des autres sujets**. Faites-moi confiance.

![Image](https://cdn-media-1.freecodecamp.org/images/9mzHbZ-kiW9wJnVKRlhZqPotx9diwe0omWXX)
_À quoi ressemble un développeur débutant après avoir réussi cette question !_

Les quatre principes de la programmation orientée objet sont **l'encapsulation**, **l'abstraction**, **l'héritage** et **le polymorphisme**.

Ces mots peuvent sembler effrayants pour un développeur junior. Et les explications complexes et excessivement longues de Wikipedia doublent parfois la confusion.

C'est pourquoi je veux donner une explication simple, courte et claire pour chacun de ces concepts. Cela peut sembler quelque chose que vous expliquez à un enfant, mais j'adorerais vraiment entendre ces réponses lorsque je mène un entretien.

### Encapsulation

Disons que nous avons un programme. Il a quelques objets logiquement différents qui communiquent entre eux — selon les règles définies dans le programme.

L'encapsulation est réalisée lorsque chaque objet garde son état **privé**, à l'intérieur d'une classe. Les autres objets n'ont pas d'accès direct à cet état. Au lieu de cela, ils ne peuvent appeler qu'une liste de fonctions publiques — appelées méthodes.

Ainsi, l'objet gère son propre état via des méthodes — et aucune autre classe ne peut le toucher sauf si cela est explicitement autorisé. Si vous voulez communiquer avec l'objet, vous devez utiliser les méthodes fournies. Mais (par défaut), vous ne pouvez pas changer l'état.

Disons que nous construisons un petit jeu Sims. Il y a des personnes et il y a un chat. Ils communiquent entre eux. Nous voulons appliquer l'encapsulation, donc nous encapsulons toute la logique « chat » dans une classe `Chat`. Cela peut ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/M4t8zW9U71xeKSlzT2o8WO47mdzrWkNa4rWv)
_Vous pouvez nourrir le chat. Mais vous ne pouvez pas changer directement à quel point le chat a faim._

Ici, l'« état » du chat est représenté par les **variables privées** `humeur`, `faim` et `énergie`. Il a également une méthode privée `miauler()`. Il peut l'appeler quand il veut, les autres classes ne peuvent pas dire au chat quand miauler.

Ce qu'ils peuvent faire est défini dans les **méthodes publiques** `dormir()`, `jouer()` et `nourrir()`. Chacune d'elles modifie l'état interne d'une certaine manière et peut invoquer `miauler()`. Ainsi, le lien entre l'état privé et les méthodes publiques est établi.

C'est l'encapsulation.

### Abstraction

L'abstraction peut être considérée comme une extension naturelle de l'encapsulation.

Dans la conception orientée objet, les programmes sont souvent extrêmement grands. Et les objets séparés communiquent beaucoup entre eux. Ainsi, maintenir une base de code aussi grande pendant des années — avec des changements en cours de route — est difficile.

L'abstraction est un concept visant à faciliter ce problème.

Appliquer l'abstraction signifie que chaque objet ne doit **exposer** qu'un mécanisme de haut niveau pour son utilisation.

Ce mécanisme doit masquer les détails internes de l'implémentation. Il ne doit révéler que les opérations pertinentes pour les autres objets.

Pensez à une machine à café. Elle fait beaucoup de choses et fait des bruits étranges sous le capot. Mais tout ce que vous avez à faire est de mettre du café et d'appuyer sur un bouton.

De préférence, ce mécanisme doit être facile à utiliser et ne doit que rarement changer avec le temps. Pensez-y comme à un petit ensemble de méthodes publiques que n'importe quelle autre classe peut appeler sans « savoir » comment elles fonctionnent.

Un autre exemple concret d'abstraction ?   
Pensez à la façon dont vous utilisez votre téléphone :

![Image](https://cdn-media-1.freecodecamp.org/images/hiX0NQOcZFShroq-a3FM5pFP2LV4UUI5mLle)
_Les téléphones portables sont complexes. Mais les utiliser est simple._

Vous interagissez avec votre téléphone en utilisant seulement quelques boutons. Que se passe-t-il sous le capot ? Vous n'avez pas besoin de le savoir — les détails de l'implémentation sont cachés. Vous n'avez besoin de connaître qu'un petit ensemble d'actions.

Les changements d'implémentation — par exemple, une mise à jour logicielle — affectent rarement l'abstraction que vous utilisez.

### Héritage

OK, nous avons vu comment l'encapsulation et l'abstraction peuvent nous aider à développer et à maintenir une grande base de code.

Mais savez-vous quel est un autre problème courant dans la conception OOP ?

Les objets sont souvent très similaires. Ils partagent une logique commune. Mais ils ne sont pas **entièrement** identiques. Beurk…

Alors, comment réutiliser la logique commune et extraire la logique unique dans une classe séparée ? Une façon d'y parvenir est l'héritage.

Cela signifie que vous créez une classe (enfant) en dérivant d'une autre classe (parent). De cette façon, nous formons une hiérarchie.

La classe enfant réutilise tous les champs et méthodes de la classe parent (partie commune) et peut implémenter les siens (partie unique).

Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/ZIm7lFjlrKeMWxcH8fqBapNkuSJIxW9-t9yf)
_Un professeur particulier est un type de professeur. Et tout professeur est un type de Personne._

Si notre programme doit gérer des professeurs publics et privés, mais aussi d'autres types de personnes comme des étudiants, nous pouvons implémenter cette hiérarchie de classes.

De cette façon, chaque classe ajoute seulement ce qui est nécessaire pour elle tout en réutilisant la logique commune avec les classes parentes.

### Polymorphisme

Nous en arrivons au mot le plus complexe ! Le polymorphisme signifie « plusieurs formes » en grec.

Nous connaissons déjà la puissance de l'héritage et l'utilisons avec plaisir. Mais voici un problème qui survient.

Disons que nous avons une classe parent et quelques classes enfants qui en héritent. Parfois, nous voulons utiliser une collection — par exemple une liste — qui contient un mélange de toutes ces classes. Ou nous avons une méthode implémentée pour la classe parent — mais nous aimerions l'utiliser pour les enfants aussi.

Cela peut être résolu en utilisant le polymorphisme.

Simplement dit, le polymorphisme donne un moyen d'utiliser une classe exactement comme son parent afin qu'il n'y ait pas de confusion avec le mélange de types. Mais chaque classe enfant conserve ses propres méthodes telles qu'elles sont.

Cela se produit généralement en définissant une interface (parent) à réutiliser. Elle décrit un ensemble de méthodes communes. Ensuite, chaque classe enfant implémente sa propre version de ces méthodes.

À chaque fois qu'une collection (comme une liste) ou une méthode attend une instance du parent (où les méthodes communes sont décrites), le langage se charge d'évaluer la bonne implémentation de la méthode commune — peu importe quel enfant est passé.

Jetez un coup d'œil à un croquis de l'implémentation des figures géométriques. Elles réutilisent une interface commune pour calculer la surface et le périmètre :

![Image](https://cdn-media-1.freecodecamp.org/images/8GySv1U8Kh9nVVyiTqv5cDuWZC7p0uARVeF0)
_Triangle, Cercle et Rectangle peuvent maintenant être utilisés dans la même collection_

Le fait que ces trois figures héritent de l'interface parent `Figure` vous permet de créer une liste de `triangles`, `cercles` et `rectangles` mélangés. Et de les traiter comme le même type d'objet.

Ensuite, si cette liste tente de calculer la surface pour un élément, la méthode correcte est trouvée et exécutée. Si l'élément est un triangle, la méthode `CalculerSurface()` du triangle est appelée. Si c'est un cercle — alors la méthode `CalculerSurface()` du cercle est appelée. Et ainsi de suite.

Si vous avez une fonction qui opère avec une figure en utilisant son paramètre, vous n'avez pas à la définir trois fois — une fois pour un triangle, un cercle et un rectangle.

Vous pouvez la définir une fois et accepter une `Figure` comme argument. Que vous passiez un triangle, un cercle ou un rectangle — tant qu'ils implémentent `CalculerParamètre()`, leur type n'a pas d'importance.

J'espère que cela vous a aidé. Vous pouvez directement utiliser ces mêmes explications lors des entretiens d'embauche.

Si vous trouvez quelque chose encore difficile à comprendre — n'hésitez pas à demander dans les commentaires ci-dessous.

### Qu'est-ce qui suit ?

Être préparé à répondre à l'une des questions classiques des entretiens de tous les temps est génial — mais parfois vous n'êtes jamais appelé pour un entretien.

Ensuite, je me concentrerai sur ce que les employeurs veulent voir chez un développeur junior et comment se démarquer de la foule lors de la recherche d'un emploi.

Restez à l'écoute.

![Image](https://cdn-media-1.freecodecamp.org/images/PWiBgy57Ye32At-VBM3qIcWdVJQ01Td-ILKl)
_Avez-vous aimé la lecture ? Si vous souhaitez me soutenir, vous pouvez m'offrir un café :)