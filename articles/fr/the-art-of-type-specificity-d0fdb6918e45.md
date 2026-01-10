---
title: Comment maîtriser l'art de la spécificité des types
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-16T03:13:56.000Z'
originalURL: https://freecodecamp.org/news/the-art-of-type-specificity-d0fdb6918e45
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KpUxhS8eOuejt0oaNggepQ.jpeg
tags:
- name: best practices
  slug: best-practices
- name: database
  slug: database
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment maîtriser l'art de la spécificité des types
seo_desc: 'By Jeff M Lowery

  Do more specific definitions result in less flexibility?

  In this post I will try to avoid the debate about strong/static vs. weak/dynamic
  types (what more could possibly be said?), or even schema vs. schema less data structures.
  Inst...'
---

Par Jeff M Lowery

_Les définitions plus spécifiques entraînent-elles moins de flexibilité ?_

Dans cet article, je vais essayer d'éviter le débat sur les types **forts/statiques** vs. **faibles/dynamiques** (que pourrait-on dire de plus ?), ou même sur les structures de données **avec schéma** vs. **sans schéma**. Au lieu de cela, je veux me concentrer sur le degré de granularité des définitions de types : quels sont les effets et les compromis ?

À une extrémité du spectre, des définitions très génériques englobent les propriétés **potentielles** et le comportement des objets. À l'autre extrémité, vous avez une riche hiérarchie de types, dont certains ne diffèrent que subtilement les uns des autres.

Je vais aborder le typage canard, les concepts de table-par-type (TPT) et de table-par-hiérarchie-de-types (TPH) en SQL, ainsi que les API paramétrées.

Lorsque vous pensez aux types génériques, vous pensez peut-être au Document Object Model (DOM), au XML ou YAML sans schéma, aux objets littéraux en JavaScript, ou aux documents de base de données NoSQL. Ceux-ci sont largement génériques, en ce sens qu'il y a des contraintes minimales sur la structure, les relations et le contenu.

Au lieu de cela, discutons des types définis par l'utilisateur. Ils peuvent être ou non appliqués par le langage de programmation ou un schéma, mais il y aura des contraintes, supposées ou non, dans le code qui les traite. Utilisons **Véhicule** comme analogie.

### Véhicule

Un véhicule est un concept large. Même si nous limitons la discussion aux véhicules à roues, cela couvre tout, des tricycles aux semi-remorques. Pourriez-vous englober le spectre des propriétés et des comportements de ces tricycles, voitures et semi-remorques en un seul type ? Oui, vous **pourriez**. Clairement, cela va poser quelques problèmes lors de la manipulation des instances de Véhicule dans le code du programme.

#### Le type Véhicule

Propriétés et méthodes possibles d'un Véhicule :

* pneus
  * nombre
  * type [pneumatique, autre]
* sièges
  * nombre
  * rembourrés [booléen]
* direction [volant, guidon]
* moteur
  * type [aucun, essence, diesel]
  * nombre de cylindres [uniquement si le type est essence ou diesel]
* conduire()
* carburant()
* lumières[allumées|pleins phares|éteintes]

Avec même cet ensemble minimal de propriétés, le type Véhicule couvre un domaine énorme et présente certains défis, l'intégrité des données en étant un. Si mon Véhicule est un tricycle, je n'ai pas de moteur. Si je n'ai pas de moteur, la propriété `nombre de cylindres` est sans signification. Si j'ai un tricycle sans moteur, mais que `nombre de cylindres > 0`, est-ce une erreur ?

Je peux faire le plein d'une voiture ou d'un camion, mais pas d'un tricycle. Que se passe-t-il si `carburant()` est appelé sur une instance de tricycle ? Lancer une Erreur ? Il est possible que certaines logiques d'application soient confuses, mais la demande peut-elle être traitée élégamment comme un no-op ?

Le seul avantage perçu de Véhicule est qu'il est flexible. Si nous divisons plutôt Véhicule en sous-classes **VéhiculeAMoteur** et **VéhiculeAPédales**, nous pourrions mettre ce qui suit dans VéhiculeAMoteur mais pas dans VéhiculeAPédales :

* direction [volant]
* moteur
  * type [essence, diesel]
  * nombre de cylindres
* carburant()
* lumières[allumées|pleins phares|éteintes]

Cela semble avoir du sens. Il est concevable, cependant, qu'un tricycle ait des lumières. Il peut ne pas avoir de moteur à essence ou diesel (enfin, pas un tricycle d'enfant), mais il _pourrait_ avoir un moteur électrique. Si ces cas se présentent, alors il y a du refactoring à faire.

Dans certains langages ou systèmes de gestion de données, vous pouvez définir des interfaces, et composer des types concrets qui remplissent ces interfaces. Ainsi, vous pourriez avoir IVéhiculeAMoteur, qui pourrait avoir des interfaces connexes IVéhiculeÉlectrique et IVéhiculeÀCombustionInterne (qui à leur tour pourraient être divisés en IVéhiculeÀEssence et IVéhiculeDiesel).

Les interfaces sont peu coûteuses à définir et bonnes pour annoter des concepts, mais elles ne sont pas une solution complète. Certaines interfaces peuvent être incompatibles avec d'autres : un camion peut-il être à la fois un camion à glace et un camion de livraison de pizza ? Je suppose, si vous voulez de la pizza froide ou de la glace tiède.

Mis à part cela, plus de spécificité vous enferme et vous oblige à avoir une certaine connaissance préalable de tous les types de véhicules que vous rencontrerez.

Ce sont les **exceptions** qui vont vous causer des problèmes à mesure que le temps avance.

Pour cette raison, surtout lorsque le domaine est large et en évolution, il peut être tentant de définir les entités de véhicule de manière moins spécifique, initialement. Vous voulez être ouvert à tout ce qui peut arriver (jeu de mots intentionnel).

#### Coder contre des types génériques

Du côté du codage, il ne peut y avoir aucune hypothèse sur ce qu'est un Véhicule. Vous devez vérifier l'existence de chaque propriété. Les méthodes qui existent peuvent être sans signification pour l'entité spécifique représentée par Véhicule. Votre meilleur pari est que votre code ne suppose rien. Cela rend les tests difficiles, cependant. Comment pouvez-vous englober toutes les configurations raisonnables de Véhicule dans vos tests ?

D'un autre côté, vous avez un système assez flexible ; c'est-à-dire, si aucune hypothèse ne s'immisce dans votre code (plus à ce sujet dans « **Pourquoi un canard ?** »).

Trop de spécificité nécessite des ajustements constants au modèle de type, y compris des décisions sur ce que la taxonomie de l'héritage est, quelle propriété va à quel niveau, et des difficultés potentielles dans les changements du modèle lorsqu'ils affectent non seulement le code au niveau des données, mais aussi le niveau de présentation. Si vous vous trompez complètement (en raison d'une analyse précipitée), vous avez beaucoup de retravail continu.

#### Types et leurs propriétés

Si vous achetez une [boîte de surprises](https://mcphee.com/products/super-awesome-surprise-box) dans une boutique de nouveautés en ligne, vous pouvez vous attendre à une boîte. Vous avez une vague idée de ce qu'elle contient, mais vous ne le saurez pas avant de l'ouvrir et de trier chaque article un par un. Le fardeau est sur vous, le client, et il y a des hypothèses limitées que vous pouvez faire (on pourrait espérer un poulet en caoutchouc, mais aucune garantie !).

Une trousse de premiers secours a une gamme plus étroite de possibilités quant à ce qu'elle contient. C'est un type d'objet plus spécifique, et vous pouvez faire des hypothèses quant à son contenu et procéder en conséquence. Elle va contenir de la gaze et des bandages. Elle aura un antiseptique, et probablement des analgésiques. Pour les choses qu'elle **pourrait** contenir, vous avez au moins une meilleure idée de ce qu'il faut chercher.

### Pourquoi un canard ?

Le typage canard fonctionne par incidence plutôt que par déclaration. La logique du programme tourne autour de l'interrogation d'un objet : « Au fait, avez-vous la propriété A ? Avez-vous la méthode B ?… ».

Les actions sont effectuées en fonction des réponses à l'interrogation. Si cela marche comme un canard, cancane comme un canard et a des plumes, alors c'est probablement un canard. La logique basée sur le typage canard ne se soucie pas vraiment, canard ou non, car elle ne suppose rien ; elle fonctionne sur ce qu'elle trouve.

Pourtant, des hypothèses s'immisceront dans toute logique logicielle qui pense obtenir ce qu'elle attend. Peut-être autant que 50 % de la maintenance logicielle implique la correction d'hypothèses incorrectes ou l'affinage de celles qui existent.

#### **Typage canard et le premier intervenant**

Supposons que j'ai un incendie dans ma cuisine et que j'appelle un numéro d'urgence. Le premier intervenant a un badge, un casque, et arrive dans un véhicule avec sirène et gyrophares. Youpi ! Le pompier ! Ma maison est sauvée. Je commande, en pointant vers la cuisine : « Éteignez cet incendie ! »

Le policier me regarde avec perplexité.

J'ai fait toute mon interrogation de typage canard, mais j'ai atteint la mauvaise conclusion. Peut-être que la ville a récemment décidé que les policiers devraient répondre aux alarmes incendie s'ils sont à proximité, pour aider les pompiers.

Je dois maintenant ajouter à ma liste de questions : « Éteignez-vous les incendies ? »

#### Des propriétés, des discriminateurs et des types nommés

Le typage canard est extrêmement flexible, mais votre code doit traiter chaque objet comme s'il pouvait être n'importe quoi. Au lieu d'interroger toutes les propriétés, vous pouvez ajouter une propriété **discriminateur** spéciale qui identifie le type d'objet que votre code reçoit. Une interrogation, et vous êtes parti. Bien sûr, l'objet doit avoir la valeur de discriminateur correcte.

Un type nommé est moins susceptible de vous causer des problèmes, car les types sont assignés à la création de l'objet. Dans un langage faiblement typé, comme JavaScript, les choses peuvent ne pas être ce qu'elles semblent, mais vous êtes quelque peu plus en sécurité en supposant.

Pourtant, les discriminateurs ou les types ne résolvent pas vraiment le problème de la spécificité. Le bon vieux type Object ne dit pas grand-chose sur ses instances. C'est un type, il fait quelques garanties, mais ne fait pas grand-chose par lui-même.

Vous pouvez passer un objet littéral à une méthode, mais la méthode doit soit 1) supposer ce qu'elle reçoit, soit 2) être prête à le découvrir.

Maintenir du code qui gère des types génériques peut être un exercice de frustration : bien que vous puissiez voir ce que le code client _pourrait_ faire, savoir ce qu'il _fera_ nécessite les spécificités des données qu'il traite.

Un débogueur aide, mais si votre point d'arrêt est enfoui profondément dans la pile d'appels, ou est en réponse à un rappel, bonne chance ! Vous pourriez avoir beaucoup de creusage à faire pour savoir comment vous êtes arrivé où vous êtes, logiquement parlant.

### Table-par-Type et Table-par-Hiérarchie-de-Types

Les bases de données relationnelles rencontrent également ce problème. Si une table représente un type de chose, [toutes les lignes de la table sont-elles homogènes en termes de type](http://blog.devart.com/table-per-type-vs-table-per-hierarchy-inheritance.html) ? Ou chaque ligne pourrait-elle refléter un type plus spécifique, et la table représente un supertype de ces choses ?

Dans le premier cas (table-par-type, ou TPT), chaque colonne de chaque ligne est garantie de contenir une valeur valide (NULL peut être valide). Votre code peut anticiper des résultats de requête qui sont cohérents dans leur uniformité.

Dans le second cas, certaines colonnes ou valeurs de colonnes peuvent être valides pour certains types (lignes) mais pas pour d'autres. C'est la table-par-hiérarchie-de-types, ou TPH.

Une table TPH est un type défini de manière lâche. L'intégrité des valeurs de colonnes dans chaque ligne dépend de la logique du programme. Si j'ai une table appelée Véhicule contenant des données pour tous les véhicules de mon domaine, alors la colonne « poids de la bobine » n'est pas applicable pour les lignes représentant des tricycles.

Le fardeau incombe maintenant au code client de comprendre les divers types possibles de véhicules dans la table Véhicule, et d'effectuer la logique en conséquence. Cela est très similaire au cas d'un objet à typage canard, où les propriétés peuvent ou non être applicables pour chaque instance du type générique.

### Un schéma, quelqu'un ?

Un schéma (ou un autre système de types) résout-il ce problème ? Eh bien, non. Comme vient d'être montré, un schéma TPH dans une base de données relationnelle peut représenter une entité super-type, mais les lignes peuvent chacune définir des entités plus spécifiques. Une valeur de colonne discriminateur peut aider à trier le sous-type de chaque ligne, mais elle doit être vérifiée dans la logique du programme.

Le principal avantage de l'utilisation de TPH est d'éviter un schéma énorme avec de nombreuses tables, et de réduire le nombre de jointures nécessaires pour rassembler les données pour une instance de type. Il y a toujours des compromis à toute approche.

### Listes de paramètres et options

Les paramètres de méthode sont un autre problème. Le cas le plus courant est celui où le type de paramètre est défini par l'ordre d'occurrence :

```js
function cercle(int x, int y, double rayon) {...}
```

ou

```js
function cercle(Position xy, double rayon) {...}
```

Les arguments définis de cette manière sont verrouillés : vous ne pouvez pas passer un booléen au rayon, par exemple. En JavaScript, il n'y a pas de paramètres typés, donc la plupart des fonctions supposent le type en fonction de l'ordre d'occurrence.

Non seulement le type de paramètre est connu (par déclaration) ou supposé (par convention), le nombre de paramètres dicte comment la méthode est appelée.

Je ressens toujours une légère irritation chaque fois que je veux afficher du JSON formaté dans la console, et que je dois taper `JSON.stringify(obj, **null**, 4)`. Ce deuxième argument, qui est rarement utilisé, est pour le paramètre [replacer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

#### **Options**

En JavaScript, vous pouvez passer un objet littéral comme argument, et cela est souvent utilisé comme une liste de paramètres nommés. Les paramètres nommés sont plus flexibles qu'une liste d'arguments, et pour des méthodes plus complexes, ils peuvent être très utiles.

```js
function cercle(options) {
    const {x, y, rayon, ...reste} = options;
    if (reste.largeurLigne) {...}
    if (reste.couleurRemplissage) {...}
    ...
}
```

Flexible, oui, mais beaucoup d'interrogation. De plus, les arguments `x, y` et `rayon` sont supposés être présents. La meilleure pratique semble être de mélanger la liste de paramètres spécifique au type avec l'objet littéral plus « générique » :

```js
function cercle(x, y, rayon, options) {...}
```

Où options est généralement compris comme faisant référence à un [objet dont les propriétés sont documentées](https://lodash.com/docs/4.17.4#debounce).

### Que faire ?

Peu de pratiques en logiciel sont entièrement bonnes ou mauvaises (GOTO étant l'exception[[?](http://echochamber.me/viewtopic.php?t=43199)]). Un système rigide et riche en types empêchera sans doute certaines erreurs de codage, même si ces types ne sont pas fortement appliqués par le langage ou la base de données. Le code qui utilise des types spécifiques est plus lisible.

D'un autre côté, une hiérarchie de types stricte représente des métadonnées qui doivent être maintenues, et souvent le client sait ce qu'il demande et sait ce qu'il recevra. Pointer chaque « i » et croiser chaque « t » juste pour le transfert de données entre deux méthodes internes semble parfois être un travail de comptabilité.

Il n'y a pas de bonne réponse, et la plupart des programmeurs utilisent des types de spécificité variable (ou aucune). Beaucoup dépend du domaine. Si vous écrivez du code pour un système financier, il semblerait que vous vouliez un ensemble riche et rigide de définitions de types ; cependant, je comprends que certains systèmes financiers sont [écrits en MUMPS](https://en.wikipedia.org/wiki/MUMPS#Current_users_of_MUMPS_applications), alors qu'est-ce que j'en sais ?