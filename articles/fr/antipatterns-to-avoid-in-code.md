---
title: Anti-patterns à éviter dans votre code
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2020-11-23T21:23:30.000Z'
originalURL: https://freecodecamp.org/news/antipatterns-to-avoid-in-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/6-anti-patterns--2-.png
tags:
- name: spaghetti code
  slug: spaghetti-code
- name: anti pattern
  slug: anti-pattern
- name: clean code
  slug: clean-code
seo_title: Anti-patterns à éviter dans votre code
seo_desc: 'Every developer wants to write structured, simply planned, and nicely commented
  code. There are even a myriad of design patterns that give us clear rules to follow,
  and a framework to keep in mind.

  But we can still find anti-patterns in software that...'
---

Chaque développeur souhaite écrire un code structuré, simplement planifié et bien commenté. Il existe même une myriade de design patterns qui nous donnent des règles claires à suivre et un cadre à garder à l'esprit.

Mais nous pouvons encore trouver des anti-patterns dans des logiciels écrits il y a quelque temps ou écrits trop rapidement.

Un simple hack pour résoudre un problème rapidement peut créer un précédent dans votre base de code. Il peut être copié à plusieurs endroits et se transformer en un anti-pattern que vous devez résoudre.

## Qu'est-ce qu'un Anti-pattern ?

Dans le domaine du logiciel, un anti-pattern est un terme qui décrit comment NE PAS résoudre des problèmes récurrents dans votre code. Les anti-patterns sont considérés comme de mauvaises conceptions logicielles et sont généralement des correctifs inefficaces ou obscurs.

Ils ajoutent généralement aussi de la "dette technique" - c'est-à-dire du code que vous devez revenir corriger *proprement* plus tard.

Les six anti-patterns que je vais aborder dans cet article sont le **Code Spaghetti**, le **Marteau d'Or**, l'**Ancre de Bateau**, le **Code Mort**, la **Prolifération de Code** et l'**Objet Dieu**.

## Code Spaghetti

Le **Code Spaghetti** est l'anti-pattern le plus connu. C'est un code avec peu ou pas de structure.

Rien n'est modulaire. Il y a des fichiers aléatoires éparpillés dans des répertoires aléatoires. Le flux entier est difficile à suivre et est complètement emmêlé (comme des spaghettis).

Normalement, cela se produit lorsque quelqu'un n'a pas soigneusement réfléchi au flux de son programme au préalable et a simplement commencé à coder.

### Que fait-il ?! Je ne peux pas suivre ça

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1601054755926/AQtiQmp0X.png align="left")

Ce n'est pas seulement un cauchemar de maintenance, mais cela rend presque impossible l'ajout de nouvelles fonctionnalités.

Vous allez constamment casser des choses, ne pas comprendre la portée de vos changements, ou donner des estimations précises pour votre travail, car il est impossible de prévoir les innombrables problèmes qui surgissent lorsque vous faites de l'archéologie/devinettes.

Vous pouvez [en lire plus ici](https://en.wikipedia.org/wiki/Spaghetti_code) sur l'anti-pattern **Code Spaghetti**.

## Marteau d'Or

> "Je suppose qu'il est tentant, si le seul outil que vous avez est un marteau, de traiter tout comme si c'était un clou." Abraham Maslow

Imaginez un scénario avec moi : votre équipe de développement est très, très compétente dans la nouvelle architecture Marteau. Elle a parfaitement fonctionné pour tous vos problèmes passés. Vous êtes l'équipe leader mondiale de l'architecture Marteau.

Mais maintenant, d'une manière ou d'une autre, tout finit toujours par utiliser cette architecture. Une vis à tête plate ? Marteau. Une vis cruciforme ? Marteau. Vous avez besoin d'une clé Allen ? Non, vous n'en avez pas besoin, enfoncez-la avec un marteau.

Vous commencez à appliquer une approche architecturale qui ne correspond pas *tout à fait* à ce dont vous avez besoin, mais qui fait le travail. Vous êtes trop dépendant d'un seul pattern et devez apprendre à utiliser le meilleur outil pour le meilleur travail.

Votre programme entier pourrait subir une sérieuse baisse de performance parce que vous essayez d'enfoncer un carré dans un trou rond. Vous savez que cela prend deux fois plus de temps à coder et à exécuter un programme utilisant l'architecture marteau pour ce problème, mais c'est *plus facile* et c'est ce avec quoi vous êtes à l'aise.

Ce n'est pas non plus très prévisible. Différents langages ont des solutions courantes aux problèmes qu'ils rencontrent, et leurs propres standards. Vous ne pouvez pas appliquer chaque règle qui a bien fonctionné pour vous dans un langage à un autre, sans problèmes.

Ne négligez pas l'apprentissage continu dans votre carrière. Choisissez le bon langage pour votre problème. Réfléchissez à l'architecture et sortez de votre zone de confort. Recherchez et investigatez de nouveaux outils et de nouvelles façons d'aborder les problèmes que vous rencontrez.

Vous pouvez [en lire plus ici](https://sourcemaking.com/antipatterns/golden-hammer) sur l'anti-pattern **Marteau d'Or**.

## Ancre de Bateau

L'anti-pattern **Ancre de Bateau** est lorsque les programmeurs laissent du code dans la base de code parce qu'*ils pourraient en avoir besoin plus tard*.

Ils ont codé quelque chose légèrement hors spécification et ce n'est pas nécessaire pour l'instant, mais ils sont sûrs qu'ils en auront besoin le mois prochain. Donc ils ne veulent pas le supprimer. Envoyez-le en production et plus tard, lorsqu'ils en auront besoin, ils pourront le faire fonctionner rapidement.

Mais cela cause des cauchemars de maintenance dans la base de code qui contient tout ce code obsolète. Le gros problème est que leurs collègues auront du mal à déterminer quel code est obsolète et ne change pas le flux, versus le code qui le fait.

Imaginez que vous êtes sur une correction urgente et que vous essayez désespérément de comprendre ce qui est responsable de l'envoi des détails de carte des clients à l'API pour retirer des fonds de leur banque. Vous pourriez perdre du temps à lire et à déboguer du code obsolète, sans réaliser que vous n'êtes même pas au bon endroit dans la base de code.

Le problème final est que le code obsolète rend votre temps de construction plus long et vous pourriez mélanger du code fonctionnel et obsolète. Vous pourriez même commencer à l'"activer" involontairement en production.

Maintenant, vous pouvez probablement voir pourquoi cela s'appelle l'anti-pattern de l'ancre de bateau – c'est lourd à porter (ajoute de la dette technique) mais ne fait rien (littéralement, le code ne sert à rien, il ne fonctionne pas).

Vous pouvez [en lire plus ici](https://sourcemaking.com/antipatterns/boat-anchor) sur l'anti-pattern **Ancre de Bateau**.

## Code Mort

Avez-vous déjà dû regarder du code écrit par quelqu'un qui ne travaille plus dans votre entreprise ? Il y a une fonction qui ne semble rien faire. Mais elle est appelée de partout ! Vous demandez autour de vous et personne d'autre n'est tout à fait sûr de ce qu'elle fait, mais tout le monde a trop peur de la supprimer.

Parfois, vous pouvez voir ce qu'elle fait, mais le contexte manque. Vous êtes capable de lire et de comprendre le flux, mais *pourquoi* ? Il ne semble plus nécessaire d'atteindre ce point de terminaison. La réponse est toujours la même pour chaque utilisateur différent.

Cela est communément décrit comme l'anti-pattern **Code Mort**. Lorsque vous ne pouvez pas voir quel est le code "actuel" nécessaire au flux et à l'exécution réussie de votre programme, versus ce qui n'était nécessaire qu'il y a 3 ans, et non maintenant.

Cet anti-pattern particulier est plus courant dans le code de preuve de concept ou de recherche qui a fini en production.

Une fois, lors d'une rencontre technologique, j'ai rencontré un homme qui avait exactement ce problème. Il avait des tonnes de code mort, dont il savait qu'il était mort, et beaucoup d'autres dont il soupçonnait qu'ils étaient morts. Mais il ne pouvait pas obtenir la permission de la direction pour supprimer tout le code mort.

Il appelait son approche **Test de Singe**, où il a commencé à commenter et à désactiver des choses pour voir ce qui explosait en production. Peut-être un peu trop risqué !

Si vous n'avez pas envie de faire des **tests de singe** sur votre application en production, essayez de présenter la dette technique à la direction comme un ["risque technique"](https://killalldefects.com/2019/12/24/technical-debt-as-risks/) pour mieux expliquer pourquoi vous pensez qu'il est si important de nettoyer.

Ou même, écrivez tout ce que votre module/section particulier fait que vous voulez réécrire, et adoptez une approche itérative pour supprimer pièce par pièce le code mort. Vérifiez à chaque fois que vous n'avez rien cassé.

Vous n'avez pas à faire une réécriture massive avec des milliers de changements. Mais vous comprendrez soit pourquoi c'est si crucial et documenterez pourquoi c'est nécessaire, soit vous supprimerez le code mort comme vous le souhaitiez.

Vous pouvez [en lire plus ici](https://sourcemaking.com/antipatterns/lava-flow) sur l'anti-pattern **Code Mort**.

## Prolifération de Code

Les objets ou modules communiquent régulièrement avec d'autres. Si vous avez une base de code propre et modulaire, vous devrez souvent appeler d'autres modules séparés et appeler de nouvelles fonctions.

L'anti-pattern **Prolifération de Code** est lorsque vous avez des objets dans votre base de code qui n'existent que pour invoquer un autre objet plus important. Leur but est seulement d'être un intermédiaire.

Cela ajoute un niveau d'abstraction inutile (ajoute quelque chose que vous devez retenir) et ne sert à rien, sinon à confondre les personnes qui doivent comprendre le flux et l'exécution de votre base de code.

Une solution simple ici est de simplement le supprimer. Déplacez la responsabilité d'invoquer l'objet que vous voulez *vraiment* vers l'objet appelant.

Vous pouvez [en lire plus ici](https://flylib.com/books/en/4.425.1.31/1/) sur l'anti-pattern **Prolifération de Code**.

## Objet Dieu

Si partout dans votre base de code vous avez besoin d'accéder à un objet, il pourrait s'agir d'un objet Dieu.

Les objets Dieu font *trop*. Ils sont responsables de l'identifiant de l'utilisateur, de l'identifiant de la transaction, du prénom et du nom de famille du client, du montant total de la transaction, des articles que l'utilisateur achète... vous voyez le tableau.

On l'appelle parfois l'anti-pattern **Couteau Suisse** parce que vous n'en avez vraiment besoin que pour couper de la ficelle, mais il peut aussi être une lime à ongles, une scie, une paire de pinces, des ciseaux, un ouvre-bouteille et un tire-bouchon.

Dans ce cas, vous devez mieux séparer et modulariser votre code.

Les programmeurs comparent souvent ce problème à demander une banane, mais à recevoir un gorille tenant une banane. Vous obtenez ce que vous avez demandé, mais plus que ce dont vous avez besoin.

Les principes SOLID discutent explicitement de cela dans les langages orientés objet, pour nous aider à mieux modéliser notre logiciel ([si vous ne savez pas ce que sont les principes SOLID, vous pouvez lire cet article](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/)).

Le S de l'acronyme signifie Single Responsibility - chaque classe/module/fonction doit avoir la responsabilité d'une partie du système, et non de plusieurs.

Vous pouvez voir ce problème encore et encore, que dire de l'interface ci-dessous ?

```typescript
interface Animal {
        numOfLegs: string;
        weight: number;
        engine: string;
        model: string;
        sound: string;
        claws: boolean;
        wingspan: string;
        customerId: string;
}
```

Pouvez-vous voir, même en scannant brièvement cette interface, que la responsabilité de celle-ci est beaucoup trop large et nécessite un refactoring ? Tout ce qui implémente cela a le potentiel de devenir un objet Dieu.

Que pensez-vous de ceci ?

```typescript

interface Animal {
        numOfLegs: string;
        weight: number;
        sound: string;
        claws: boolean;
}

interface Car {
        engine: string;
        model: string;
}

interface Bird {
        wingspan: string;
}

interface Transaction {
        customerId: string;
}
```

La séparation des interfaces gardera votre code clair sur les responsabilités, et empêchera de forcer les classes qui n'ont besoin que de `wingspan` à implémenter également `engine`, `customerId` et `model`, etc.

Vous pouvez [en lire plus ici](https://en.wikipedia.org/wiki/God_object) sur l'anti-pattern **Objet Dieu**.

## Conclusion

Dans toute grande base de code, il y a un équilibre constant entre la gestion de la dette technique, le démarrage de nouveaux développements et la gestion d'une file d'attente de bugs pour votre produit.

J'espère que cet article vous a donné un œil pour repérer lorsque vous pourriez tomber dans le terrier de l'anti-pattern, et quelques outils pour le résoudre proprement.

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et souhaitez en voir plus.