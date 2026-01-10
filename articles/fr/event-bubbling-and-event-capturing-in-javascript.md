---
title: La remontée d'événements et la capture d'événements en JavaScript – Expliqué
  avec des exemples
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2023-10-17T21:26:37.000Z'
originalURL: https://freecodecamp.org/news/event-bubbling-and-event-capturing-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Event-Bubbling-and-Event-Capturing-in-JavaScript-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: La remontée d'événements et la capture d'événements en JavaScript – Expliqué
  avec des exemples
seo_desc: "If you want to improve your JavaScript code, you should understand how\
  \ event bubbling and event capturing work. The ability to consistently run your\
  \ code when certain events happen is crucial. \nIn this tutorial, you’ll learn about\
  \ the following topic..."
---

Si vous souhaitez améliorer votre code JavaScript, vous devez comprendre comment fonctionnent la remontée d'événements et la capture d'événements. La capacité à exécuter votre code de manière cohérente lorsque certains événements se produisent est cruciale. 

Dans ce tutoriel, vous apprendrez les sujets suivants :

* [Qu'est-ce que les événements en JavaScript](#heading-quest-ce-que-les-evenements-en-javascript) ?
* [Qu'est-ce que les gestionnaires d'événements](#heading-quest-ce-que-les-gestionnaires-devements) ?
* [Flux d'événements dans le DOM](#heading-flux-devements-dans-le-dom)
* [Qu'est-ce que la remontée d'événements](#heading-quest-ce-que-la-remontee-devements) ?
* [Qu'est-ce que la capture d'événements](#heading-quest-ce-que-la-capture-devements) ?
* [Comment fonctionne event.stopPropagation](#how-does-event-stoppropagation-work) ?
* [Qu'est-ce que la délégation d'événements](#heading-quest-ce-que-la-delegation-devements) ?
* [Conclusion](#heading-conclusion)

## Qu'est-ce que les événements en JavaScript ?

Les événements n'existent pas seulement en JavaScript mais dans tous les langages de programmation. L'idée principale derrière les événements en JavaScript est la capacité à exécuter du code lorsqu'un certain événement se produit. Cela pourrait être un utilisateur cliquant sur un bouton ou tout autre événement auquel vous pourriez penser et qui pourrait déclencher l'exécution de code. 

Bien qu'il existe une différence distincte entre les événements côté navigateur et côté serveur en JavaScript, l'idée de base reste la même. 

Comme les événements transportent des données, un objet est créé et donné comme argument à la fonction que vous définissez comme gestionnaire d'événements. Lorsque des événements se produisent en JavaScript, un objet contenant des informations sur cet événement est créé. Cet objet est ensuite passé comme argument à la fonction de gestionnaire d'événements. Cela vous donne un accès facile aux données de l'événement et facilite également la réponse.  

Voici une explication plus détaillée :

* Un événement peut être appelé par différentes actions. Des exemples sont les clics, les mouvements de souris et les intervalles de temps.
* JavaScript crée un objet événement chaque fois qu'un événement se produit. Cet objet a des propriétés et des méthodes, et fournit des détails sur l'événement.
* Vous pouvez définir une fonction qui sera exécutée chaque fois que l'événement se produit avec des gestionnaires d'événements en JavaScript. 
* L'objet événement est automatiquement créé chaque fois que l'événement est déclenché. Cet objet est donc passé comme argument à la fonction de gestionnaire d'événements.


Voyons à quoi cela ressemble en code :

```javascript
const button = document.getElementById('check')


button.addEventListener('click', (e) => {
  console.log('Type d\'événement : ' + e.type);
  console.log('Élément cible : ' + e.target);
});


//  La réponse

// Type d\'événement : click
// Élément cible : [object HTMLButtonElement]
```

#### Explication du code :

Le code ci-dessus est un extrait de code JavaScript.

La fonction fournie comme gestionnaire d'événements est appelée chaque fois que l'événement de clic se produit sur l'élément bouton. Elle reçoit ensuite l'objet événement comme paramètre d'événement, ce qui permet un accès facile aux propriétés et aux données liées à l'événement de clic.

En obtenant l'accès à cet objet événement dans le gestionnaire d'événements, vous pouvez personnaliser votre réponse en fonction des données et des propriétés de l'événement.

Il existe des informations spécifiques disponibles dans l'objet événement en fonction du type d'événement qui s'est produit. Pour l'événement de clic dans notre exemple, les détails inclus sont `event.target` et `event.type`.

## Qu'est-ce que les gestionnaires d'événements ?

Les gestionnaires d'événements sont comme une télécommande polyvalente spéciale qui peut effectuer certaines actions comme changer les chaînes de votre télévision, augmenter la température de votre climatiseur et changer l'état de votre éclairage dans votre maison. Mais ils ont besoin d'un professionnel pour gérer un bouton spécial qui y est attaché. 

L'analogie ci-dessus explique les concepts de gestion des événements en JavaScript. La télécommande représente l'application que vous utilisez. Le bouton de type élément HTML sur l'application est le bouton spécial attaché à la télécommande. Et le professionnel qui gère le bouton spécial est JavaScript. 

La gestion des événements en JavaScript rend les applications et les pages web réactives et interactives. Ils le font en définissant et en gérant des événements et en effectuant des actions spécifiques chaque fois que ces événements se produisent. 

Un gestionnaire d'événements est toute fonction ou méthode spécifiquement définie pour répondre à un événement spécifique en JavaScript. Il est également responsable de l'exécution du code lorsqu'un événement particulier se produit. Voici un exemple :

```javascript
const button = document.getElementById('check')


button.addEventListener('click', (e) => {
  console.log('Événement', e.target)
  console.log('Clic sur le bouton')
});


//  La réponse

// Événement <button id="check">Vérifier la commande</button>
// Clic sur le bouton
```

##### Explication du code :

Le code ci-dessus est un extrait de code JavaScript.

Un gestionnaire d'événements de clic est attaché à l'élément bouton. Lorsque le bouton est cliqué, il enregistre quelque chose dans la console.

Lorsque un événement se produit, un objet événement est créé par le navigateur. Cet objet est ensuite passé comme argument à la fonction de gestionnaire d'événements. Avec cela, les données et propriétés de l'objet événement peuvent être accessibles.
 
Comme vous l'avez maintenant compris, les gestionnaires d'événements sont une partie clé de la création d'applications web dynamiques.

## Flux d'événements dans le DOM

Les événements sont généralement traités en trois phases dans le DOM. Il s'agit de la phase de capture, de la phase cible et de la phase de remontée. 

### La phase de capture

La première phase est la **phase de capture**, qui se produit lorsqu'un élément imbriqué dans divers éléments est cliqué. Juste avant que le clic n'atteigne sa destination finale, l'événement de clic de chacun de ses éléments parents doit être déclenché. Cette phase se propage du haut de l'arbre DOM vers l'élément cible.

### La phase cible

La **phase cible** est la deuxième phase qui commence immédiatement après la fin de la phase de capture. Cette phase est essentiellement la fin de la capture et le début de la phase de remontée. 

L'élément cible est l'élément où l'événement s'est initialement produit. Par exemple, si vous soumettez un formulaire sur une page web, l'élément formulaire est l'élément cible pour l'événement de soumission. Dans le cas où il y a un gestionnaire d'événements sur un bouton sur une page web, le bouton est l'élément cible pour le gestionnaire d'événements. 

Les gestionnaires d'événements enregistrés sur l'élément bouton sont considérés comme l'élément cible pendant cette phase.

### La phase de remontée

La **phase de remontée**, qui est la dernière phase, est l'inverse de la phase de capture. Dans cette phase, l'événement remonte de l'élément cible à travers son élément parent, l'ancêtre, jusqu'à l'objet window global. Par défaut, tous les événements que vous ajoutez avec `addEventListener` sont dans la phase de remontée.

![Flux d'événements en JavaScript](https://www.freecodecamp.org/news/content/images/2023/10/bubbling-and-capturing2.png)
_Processus de flux d'événements_

## Qu'est-ce que la remontée d'événements ?

La remontée d'événements, comme je l'ai mentionné ci-dessus, est la phase où l'événement remonte de l'élément cible jusqu'à l'objet window global. 

Lorsque un événement "remonte" dans le contexte du flux d'événements `DOM`, cela fait référence à une phase du flux d'événements où un événement qui se produit traditionnellement après la phase cible continue à se propager de l'élément cible à la racine du document à travers la hiérarchie `DOM`.

#### Comment fonctionne la remontée d'événements

L'événement commence à remonter à travers la hiérarchie `DOM` après avoir été traité au niveau de l'élément cible. L'événement voyage ensuite de l'élément cible à la racine du document. Il passe par tous les éléments ancêtres selon leur imbrication dans la phase de remontée.

Pendant la phase d'exécution d'un gestionnaire d'événements, tous les gestionnaires d'événements enregistrés sur les éléments ancêtres sont exécutés. Cela permet une capture facile des événements à divers stades de la hiérarchie `DOM`. 

Cette action peut être arrêtée en utilisant la méthode `stopPropagation()` sur l'objet événement. Elle est utile lorsque vous souhaitez empêcher les gestionnaires d'événements des éléments ancêtres de se déclencher.

Avec la remontée, les événements peuvent être gérés de manière hiérarchique. En définissant un gestionnaire d'événements sur l'élément parent ou le conteneur, vous pouvez gérer les événements de plusieurs éléments enfants.

La remontée d'événements permet une mise en œuvre plus facile de la délégation d'événements.


![Remontée d'événements](https://www.freecodecamp.org/news/content/images/2023/10/bubbling-and-capturing3.png)

Voici un exemple de son fonctionnement, que je vais expliquer ci-dessous :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Pratique</title>
  </head>
  <body>
    <h1>Phase de remontée et de capture</h1>

    <div>
      <button class="child">cliquez-moi</button>
    </div>

    <script>
      const parent = document.querySelector("div");
      const child = document.querySelector(".child");

      parent.addEventListener("click", function () {
        console.log("parent cliqué");
      });

      child.addEventListener("click", function () {
        console.log("enfant cliqué");
      });
    </script>
  </body>
</html>



<!-- 

         RÉSULTATS DU CODE CI-DESSUS

         index.html:25 enfant cliqué
         index.html:21 parent cliqué
      
 -->

```

#### Explication du code :

Le code ci-dessus est un extrait de code HTML et JavaScript.

À l'intérieur de l'élément body, nous avons les éléments `h1`, `div` et `button`. La div est l'élément parent de l'élément bouton. Nous avons donné un nom de classe "child" pour l'élément bouton.

Dans la section JavaScript, nous avons créé des variables pour les éléments parent et enfant. Ensuite, nous avons ajouté des écouteurs d'événements aux éléments parent et enfant.

Ainsi, lorsque le bouton est cliqué, "enfant cliqué" est d'abord invoqué. Cela signifie que la fonction à l'intérieur de l'élément parent s'exécute après la fonction à l'intérieur de l'élément enfant.

## Qu'est-ce que la capture d'événements ?

La capture d'événements se produit lorsqu'un élément imbriqué est cliqué. L'événement de clic de ses éléments parents doit être déclenché avant le clic de l'élément imbriqué. Cette phase se propage du haut de l'arbre `DOM` vers l'élément cible.  

La capture d'événements ne peut pas se produire tant que le troisième argument de `addEventListener` n'est pas défini sur la valeur `Boolean` true comme montré ci-dessous (la valeur par défaut est false).  

Chaque fois que le troisième argument de `addEventListener` est défini sur `true`, les gestionnaires d'événements sont automatiquement déclenchés dans la phase de capture. Avec cela, le gestionnaire d'événements attaché à un élément ancêtre sera exécuté en premier lorsqu'un événement se produit sur un élément imbriqué dans la hiérarchie `DOM`. Cela est différent du comportement par défaut, où les gestionnaires d'événements sont déclenchés pendant la phase de remontée.

![Capture d'événements](https://www.freecodecamp.org/news/content/images/2023/10/bubbling-and-capturing4.png)
_Capture d'événements_

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Pratique</title>
  </head>
  <body>
    <h1>Phase de remontée et de capture</h1>

    <div>
      <button class="child">cliquez-moi</button>
    </div>

    <script>
      const parent = document.querySelector("div");
      const child = document.querySelector(".child");

      parent.addEventListener(
        "click",
        function () {
          console.log("parent cliqué");
        },
        true
      );

      child.addEventListener("click", function () {
        console.log("enfant cliqué");
      });
    </script>
  </body>
</html>

<!-- 

       RÉSULTATS DU CODE CI-DESSUS

      index.html:25 parent cliqué
      index.html:21 enfant cliqué
      
 -->

```

#### Explication du code :

Le code ci-dessus est un extrait de code HTML et JavaScript. À l'intérieur de l'élément body, nous avons les éléments `h1`, `div` et `button`.

La div est l'élément parent de l'élément bouton. Nous avons donné un nom de classe "child" à l'élément bouton.

Dans la section JavaScript, nous avons créé des variables pour les éléments parent et enfant. Nous avons également ajouté des écouteurs d'événements aux éléments parent et enfant.

Dans l'élément parent, nous avons défini la valeur `Boolean` sur "true" pour le troisième argument. La valeur par défaut est false.

Ainsi, lorsque le bouton est cliqué, "parent cliqué" est d'abord invoqué. Cela signifie que la fonction à l'intérieur de l'élément parent s'exécute avant la fonction à l'intérieur de l'élément enfant.

## Comment fonctionne la méthode `event.stopPropagation` ?

Par défaut, tous les gestionnaires d'événements sont enregistrés dans la phase de remontée (de l'élément cible à tous ses éléments ancêtres). Cette configuration par défaut peut être modifiée en ajoutant la méthode `event.stopPropagation` à l'élément cible.

Comme son nom l'indique, la méthode `Event.stopPropagation` arrête la propagation. Tout autre écouteur pour le même type d'événement sur un élément ancêtre ne déclenchera pas leur écouteur d'événement pour l'événement.

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Pratique</title>
  </head>
  <body>
    <h1>Phase de remontée et de capture</h1>

    <ul>
      <li>Kamal</li>
      <li>Lawal</li>
      <li>Olaide</li>
      <li>Ayinde</li>
    </ul>

    <script>
      const parent = document.querySelector("ul");
      const li = document.querySelectorAll("li");

      parent.addEventListener("click", function () {
        console.log("parent cliqué");
      });

      li.forEach(function (list) {
        list.addEventListener("click", function () {
          event.stopPropagation();
          event.target.classList.toggle("highlight");
        });
      });
    </script>
  </body>
</html>

```

Contrairement au comportement par défaut, `event.stopPropagation` empêchera l'élément parent `ul` de s'afficher dans la console. Notez que la méthode `event.stopPropagation` peut également être utilisée dans la phase de capture.

## Qu'est-ce que la délégation d'événements ?

Imaginez votre bureau sans manager. Ce bureau sera probablement moins efficace que celui avec un manager. Les managers ne font pas ou ne supervisent pas chaque tâche individuellement – au lieu de cela, ils délèguent des responsabilités à leurs employés. Cette délégation permet au manager de gérer efficacement la charge de travail, puis d'intervenir si quelque chose ne va pas.

La délégation d'événements en JavaScript est similaire à l'exemple ci-dessus, car elle facilite la gestion et le traitement des événements sur plusieurs éléments enfants. Elle tire parti de l'événement de remontée du `DOM` (Document Object Model). Cela signifie que la définition d'écouteurs d'événements sur des éléments ancêtres vous permet de gérer les événements efficacement. Contrairement à la définition d'écouteurs d'événements sur des éléments individuels qui déclenchent les événements. Rappelez-vous que dans la phase de remontée, les événements sur l'élément enfant remontent à leur élément parent.

Vérifiez le code ci-dessous pour vous aider à comprendre comment cela fonctionne :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Pratique</title>
  </head>
  <body>
    <ul>
      <li>Orange</li>
      <li>Banane</li>
      <li>Pomme de terre</li>
      <li>Pomme</li>
    </ul>

    <script>
      const li = document.querySelectorAll("li");

      li.forEach(function (list) {
        list.addEventListener("click", function () {
          alert("Oui, je clique");
        });
      });
    </script>
  </body>
</html>
```

Dans le code ci-dessus, un écouteur d'événements a été ajouté à chacun des `listItems`. Ensuite, chaque fois qu'ils sont cliqués, une alerte apparaît. Traditionnellement, ce n'est pas un mauvais code, mais cela va à l'encontre du but de la délégation d'événements. Dans le code ci-dessous, vous verrez l'importance de la délégation d'événements.

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Pratique</title>
  </head>
  <body>
    <h1>Phase de remontée et de capture</h1>

    <ul>
      <li>Kamal</li>
      <li>Lawal</li>
      <li>Olaide</li>
      <li>Ayinde</li>
    </ul>

    <script>
      const ul = document.querySelector("ul");

      ul.addEventListener("click", function () {
        event.target.classList.toggle("highlight");
      });
    </script>
  </body>
</html>

```

Contrairement au code initial, le parent des listItems `ul` gérera l'événement ici. Ainsi, le parent déléguera la logique que nous voulons atteindre à l'enfant. Rappelez-vous que les `listItems` remontent dans l'arbre `DOM`.

Mais il existe certaines situations où il sera presque impossible de déléguer à un élément enfant. Par exemple, c'est impossible si l'enfant a lui-même un élément enfant imbriqué. Dans ce cas, il sera impossible de déléguer à un élément enfant.

Voici un exemple de code qui vous montre pourquoi il peut être impossible de déléguer à un élément enfant :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Pratique</title>
  </head>
  <body>
    <h1>Phase de remontée et de capture</h1>

    <ul>
      <li>
        <h2>Orange</h2>
        <p>Kamal</p>
      </li>
      <li>
        <h2>Pomme</h2>
        <p>Lawal</p>
      </li>
      <li>
        <h2>Banane</h2>
        <p>Olaide</p>
      </li>
    </ul>

    <script>
      const ul = document.querySelector("ul");

      ul.addEventListener("click", function () {
        event.target.classList.toggle("highlight");
      });
    </script>
  </body>
</html>
```

Le code ci-dessus ne produira pas le résultat attendu. Cela est dû au fait que dans notre code, nous utilisons `event.target`.

En JavaScript, `event.target` est l'élément `DOM` réel qui est cliqué. Dans ce cas, les trois résultats possibles sont `li`, `h2` et `p`. Le code ci-dessous montre la solution à ce problème :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Pratique</title>
  </head>
  <body>
    <h1>Phase de remontée et de capture</h1>

    <ul>
      <li>
        <h2>Orange</h2>
        <p>Kamal</p>
      </li>
      <li>
        <h2>Pomme</h2>
        <p>Lawal</p>
      </li>
      <li>
        <h2>Banane</h2>
        <p>Olaide</p>
      </li>
    </ul>

    <script>
      const ul = document.querySelector("ul");

      ul.addEventListener("click", function () {
        event.target.closest("li").classList.toggle("highlight");
      });
    </script>
  </body>
</html>
```

Pour obtenir le résultat attendu de la sélection du listItem, nous combinons la méthode de parcours `DOM` avec `event.target`.

La méthode `closest` est disponible sur les objets `DOM`. `closest` parcourt l'arbre des ancêtres. Vous pouvez sélectionner l'élément le plus proche avec n'importe quel sélecteur CSS par ID, balise ou nom de classe. Une chose intéressante est que `closest` inclut l'élément sur lequel vous l'appelez, dans ce cas le `li`.

## Conclusion

Espérons qu'après avoir lu ce guide, vous avez maintenant une compréhension plus claire des événements, des gestionnaires d'événements et du flux d'événements en JavaScript. 

Vous avez appris comment fonctionnent la capture et la remontée d'événements, et vous devriez maintenant comprendre les principaux concepts derrière la délégation d'événements, également.

Merci d'avoir lu !