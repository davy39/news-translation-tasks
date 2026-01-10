---
title: Comment utiliser les fonctions anonymes pour un espace de noms privé dans vos
  applications JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-anonymous-functions-for-private-namespacing-in-your-javascript-apps
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d01740569d1a4ca355f.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: JavaScript
  slug: javascript
- name: privacy
  slug: privacy
- name: toothbrush
  slug: toothbrush
seo_title: Comment utiliser les fonctions anonymes pour un espace de noms privé dans
  vos applications JavaScript
seo_desc: 'Let’s take a look at what a namespace is when it comes to building JavaScript
  applications and some of the benefits from using a private namespace when building
  your apps.

  Please note that this article references anonymous self-executing functions. I...'
---

Examinons ce qu'est un espace de noms lorsqu'il s'agit de créer des applications JavaScript et certains des avantages de l'utilisation d'un espace de noms privé lors de la création de vos applications.

**Veuillez noter que cet article fait référence aux fonctions anonymes auto-exécutantes. Si vous ne savez pas ce que c'est, veuillez lire cet excellent article de Noah Stokes : [Self-Executing Anonymous Functions or How to Write Clean Javascript](http://esbueno.noahstokes.com/post/77292606977/self-executing-anonymous-functions-or-how-to-write). Cet article entrera dans les détails sur les fonctions anonymes auto-exécutantes.**

## **Qu'est-ce qu'un espace de noms ?**

Pour faire simple, un espace de noms est simplement une section de code qui a son propre espace. Lorsque vous commencez à écrire des applications JS, vous tapez généralement le code et l'exécutez. Cela place tout le code dans ce qu'on appelle l'**espace de noms global**, qui contient tout le code pour la fenêtre dans laquelle vous travaillez.

Si vous gardez tout votre code dans l'**espace de noms global**, cependant, vous pouvez rencontrer des problèmes de collisions, de conventions de nommage, etc., surtout dans les grandes applications/jeux JS.

Examinons un exemple de la façon dont l'utilisation uniquement de l'**espace de noms global** pour développer un jeu est une mauvaise idée.

Supposons donc que nous avons un jeu qui suit les points que le joueur a accumulés :

```text
var points = 0;
```

Beaucoup de jeux suivent les points pour ajouter un côté compétitif au jeu. En tapant simplement cette ligne dans un script, nous avons créé une variable nommée _points_ qui peut suivre les points gagnés par l'utilisateur.

Et c'est très bien, mais supposons que nous avons un utilisateur plus avancé qui joue au jeu. Cet utilisateur sait comment regarder le code source d'une page web, et donc cette personne jette un coup d'œil au code source derrière le jeu JS et réalise que la variable _points_ est simplement là dans l'**espace de noms global**. Un sourire malicieux descend sur leur visage alors qu'ils contemplent les points qu'ils peuvent atteindre ! Ils décident qu'ils ne veulent pas attendre pour battre des méchants, ou écraser des champignons, ou ce que vous voulez, pour accumuler un tas de points. Ils veulent leurs points maintenant ! Eh bien, comment _un quadrillion de milliards de millions_ de points sonne-t-il ?! Alors, ils chargent la console sur leur navigateur préféré, et tapent simplement dans la console :

```text
points = 34750925489459203859095480917458059034;
```

Une fois que l'utilisateur appuie sur Entrée, la variable _points_ est mise à jour dans le jeu. Maintenant, l'utilisateur a un nombre de points vraiment énorme, et probablement irréaliste, dans le jeu, et il peut se vanter auprès de ses amis que personne ne peut probablement battre son score impressionnant.

Alors, comment pouvons-nous empêcher cela de se produire ? C'est là que les **espaces de noms privés** entrent en jeu.

## **Espaces de noms privés**

Les **espaces de noms privés** permettent aux développeurs de mettre leur code dans des sections (ou **espaces de noms**). Ces sections fonctionnent indépendamment les unes des autres mais peuvent toujours lire et écrire depuis l'**espace de noms global**.

Pour simplifier cela avec un scénario de la vie réelle, disons que vous travaillez dans un immeuble de bureaux. Vous avez votre propre bureau, et vous voyez d'autres personnes avec leur propre bureau. Chaque bureau est verrouillé, et seule la personne qui possède le bureau a une clé pour ce bureau. Disons aussi que vous avez un type de nouveau super verrou qui rend votre bureau impénétrable par toute autre personne dans le bâtiment. Considérons l'immeuble de bureaux lui-même comme l'**espace de noms global** et chaque bureau comme un **espace de noms privé**. Vous n'avez pas accès au bureau de quelqu'un d'autre ni eux n'ont accès au vôtre. Mais, chacun de vous a accès au reste de l'immeuble de bureaux, que ce soit pour prendre un café, prendre une collation, etc. Chacun de vous peut prendre quelque chose depuis l'**espace de noms global** (ou créer/modifier quelque chose là-bas), mais vous ne pouvez pas créer/modifier/prendre quoi que ce soit depuis les bureaux des autres ; vous ne pouvez créer/modifier/prendre que depuis votre propre **espace de noms privé**/bureau.

## **Atteindre un espace de noms privé**

Alors, comment atteindre cet **espace de noms privé** en JavaScript ? Utilisez une fonction anonyme auto-exécutante ! Si vous n'avez pas lu l'article de Noah Stokes, [Self-Executing Anonymous Functions or How to Write Clean Javascript](http://esbueno.noahstokes.com/post/77292606977/self-executing-anonymous-functions-or-how-to-write), veuillez le faire maintenant. Cet article entrera dans les détails sur les fonctions anonymes auto-exécutantes.

Examinons l'utilisation de cette variable _points_ de tout à l'heure, mais séparons-la dans un **espace de noms privé** :

```text
//La manière la plus courante dont vous verrez une fonction anonyme auto-exécutante
(function () {
    var points = 0;
})();

//Ce n'est qu'une des nombreuses autres manières alternatives d'utiliser une fonction anonyme auto-exécutante
/*
!function () {
    var points = 0;
}();
*/
```

Maintenant, lorsque l'utilisateur arrive sur la page, il ne pourra pas ouvrir la console dans son navigateur et changer la valeur de la variable points comme il le souhaite ! Génial !

## **Interaction entre l'espace de noms et le document**

Le code ci-dessus n'était qu'une utilisation de l'utilisation d'une fonction anonyme auto-exécutante pour donner au code son propre **espace de noms privé**. Gardez à l'esprit que les espaces de noms n'affectent que le code JS (variables/tableaux/objets/etc.), et non le code qui concerne le document lui-même.

Tout code dans un espace de noms a toujours le même accès au document HTML, et au CSS, comme vous le feriez normalement dans l'**espace de noms global**. Jetez un coup d'œil aux deux prochains exemples de code. Ils effectuent tous deux la même fonctionnalité, et aucun n'est plus bénéfique, ou plus efficace, que l'autre.

```text
<script type="text/javascript">
    (function () {
        document.querySelector('body').style.background = 'blue';
    })();
</script>
```

est le même que :

```text
<script type="text/javascript">
    document.querySelector('body').style.background = 'blue';
</script>
```

Gardez à l'esprit que ce n'est qu'une manière d'utiliser les espaces de noms dans les applications JavaScript. Adaptez votre code à ce qui convient le mieux à la situation en cours.