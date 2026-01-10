---
title: Comment gérer les dépendances de code en utilisant des shims pour vos abstractions
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-04-19T23:19:44.000Z'
originalURL: https://freecodecamp.org/news/manage-code-dependencies-by-shimming-your-abstractions
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/Always-Shim-your-Abstractions.png
tags:
- name: clean code
  slug: clean-code
- name: dependency management
  slug: dependency-management
seo_title: Comment gérer les dépendances de code en utilisant des shims pour vos abstractions
seo_desc: 'Dependencies are a very common part of any sufficiently mature codebase.
  And it''s important to cleanly handle any third party code that your program relies
  on to function.

  There are multiple ways to get third party code included and updated. And I re...'
---

Les dépendances sont une partie très courante de toute base de code suffisamment mature. Et il est important de gérer proprement tout code tiers dont votre programme dépend pour fonctionner.

Il existe plusieurs façons d'inclure et de mettre à jour du code tiers. Et j'ai lu quelque chose récemment qui est facilement devenu ma manière préférée de faire cela, alors je devais le partager.

Cette méthode consiste à **toujours utiliser des shims pour vos abstractions**.

Pour bien comprendre ce que cela signifie, définissons chaque mot avant de parler de l'idée plus large qu'il englobe.

## Abstractions

Les développeurs utilisent souvent des **abstractions** dans le code pour simplifier un système.

Les **abstractions** sont un moyen de cacher du code compliqué à l'intérieur de quelque chose, et elles fournissent généralement une interface facile à utiliser.

Par exemple, supposons que nous avons un code complexe qui effectue beaucoup de calculs mathématiques très spécifiques. Nous pouvons envelopper toute cette logique dans une fonction et fournir une interface très simple où vous passez simplement votre nombre et la fonction fera le travail.

Nous n'obligeons essentiellement pas la personne qui utilise notre code à se soucier des détails d'implémentation. Elle peut simplement appeler la fonction et obtenir sa réponse en retour – elle n'a pas à se soucier de ce que la fonction fait "sous le capot".

_C'est_ la force de l'abstraction des détails dans votre code.

Vous pouvez abstraire les choses dans une multitude de structures de données ou d'architectures de code. Et vous pouvez abstraire les détails d'implémentation à l'intérieur d'un prototype, d'une classe, d'une fonction ou plus.

Si vous deviez comprendre chaque ligne de code dans une grande base de code (disons une base de code de 2 millions de lignes), vous ne pourriez jamais commencer à coder.

Vous pouvez créer une base de code réutilisable, simple à comprendre et facilement modifiable en **abstrayant** certains détails dans les modules corrects/en séparant votre code.

### Comment fonctionne l'abstraction de code

Un exemple d'abstraction de la logique serait : imaginez que vous créez une machine pour faire du café pour vos utilisateurs. Il pourrait y avoir deux approches :

#### Comment la créer avec abstraction

* Avoir un bouton avec le titre "Faire du café"

#### Comment la créer sans abstraction

* Avoir un bouton avec le titre "Faire bouillir l'eau"
* Avoir un bouton avec le titre "Ajouter l'eau froide à la bouilloire"
* Avoir un bouton avec le titre "Ajouter 1 cuillère de café moulu dans une tasse propre"
* Avoir un bouton avec le titre "Nettoyer les tasses sales"
* Et tous les autres boutons

Voyez-vous comment, lorsque nous utilisons l'abstraction, nous n'attendons pas de l'utilisateur qu'il sache comment la machine fait le café ? Mais dans la machine sans **abstraction**, l'utilisateur doit savoir dans quel ordre appuyer sur chaque bouton, ce qui l'oblige à comprendre comment le café est fait.

Il y a une définition que nous devons couvrir avant de pouvoir continuer et comprendre le concept que j'ai introduit au début (toujours utiliser des shims pour vos abstractions), et c'est le shimming.

## Shimming

Le **shimming** est l'acte de placer quelque chose devant autre chose pour intercepter les données qui sont passées.

Regardons un exemple de son fonctionnement.

Supposons qu'une banque dispose d'une API très ancienne qui n'accepte pas le JSON en raison d'un défaut technique hérité. Au lieu de cela, elle ne peut accepter que le XML. Nous appellerons cela **LegacyAPI**.

Mais un grand pourcentage de développeurs qui souhaitent utiliser cette API bancaire veulent envoyer du JSON. La banque refuse de changer LegacyAPI car c'est trop risqué et pourrait casser l'API. Une grande partie de leur système en dépend, et ils ne peuvent pas se permettre de faire beaucoup de nouveau développement et de mettre hors service d'énormes parties de leur système s'ils font une erreur.

Ils pourraient toujours **shim** LegacyAPI s'ils ne veulent pas faire de nouveau développement dessus.

Ils pourraient le faire en créant une API qui se situe "devant" LegacyAPI. Nous l'appellerons **NewAPI**.

Le terme "devant" signifie simplement l'ordre de qui traite en premier la requête réseau. Par "devant", nous entendons simplement que NewAPI sera la première à recevoir les requêtes réseau.

Vous diriez aux développeurs qu'ils peuvent maintenant utiliser NewAPI avec JSON comme ils le souhaitaient, et NewAPI convertira le JSON en XML pour LegacyAPI et les deux parties pourront être satisfaites.

La banque peut maintenant étendre ses services (elle peut accepter JSON, par exemple) via NewAPI sans changer son ancienne API héritée dont elle se méfiait de changer.

Ce n'est qu'un exemple de **shimming**. Et pour résumer, il s'agit essentiellement d'ajouter quelque chose devant autre chose pour agir comme un homme au milieu afin de passer des données à autre chose.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-50.png)
_Un diagramme de la façon dont **NewAPI** intercepte les requêtes réseau de **LegacyAPI**._

Espérons que vous avez une bonne compréhension de ce qu'est le shimming et de ce que sont les abstractions. Rassemblons les deux définitions pour définir ce que nous entendons par **toujours utiliser des shims pour vos abstractions**.

## Pourquoi vous devriez toujours utiliser des shims pour vos abstractions

### Le problème

Chaque fois que nous devons gérer nos dépendances, nous voulons nous assurer que nous empêchons le code tiers de "fuiter" dans tout notre code principal.

Par "fuiter", je veux dire que le code de dépendance est importé plusieurs fois à différents endroits qui en ont besoin dans votre code.

Si vous laissez une dépendance "envahir" votre code source, vous devenez de plus en plus étroitement couplé à celle-ci chaque fois que vous l'importez.

Cela peut (parfois !) signifier que vous serez forcé de coder dans la direction que la bibliothèque choisit, car vous êtes étroitement couplé à celle-ci. Cela peut entraîner une surcharge cognitive significative, car vous essayez de plus en plus de faire fonctionner cette bibliothèque dans votre code, mais elle n'est pas en accord avec le reste de vos décisions architecturales.

Cela peut rendre tout refactoring que vous devez faire beaucoup plus long que si vous l'aviez isolé. Par exemple, si la dépendance change, quels arguments devrait-elle accepter pour créer un objet dans la dépendance ?

En plus de la difficulté à maintenir votre build fonctionnant bien avec la dépendance, si elle ne convient plus à vos besoins ou si vous trouvez une meilleure bibliothèque pour la remplacer, votre refactoring devient beaucoup plus difficile à réaliser pour vous en débarrasser.

### La solution

Pour essayer d'empêcher tout ce qui précède de se produire, mettons d'abord toutes les dépendances dont nous avons besoin dans leurs propres modules où elles ne sont référencées qu'une seule fois dans votre base de code.

C'est en essence notre **shim**.

Chaque fois que vous avez besoin de la dépendance tierce, vous n'avez qu'à importer le module wrapper que nous avons placé autour, pour agir comme un "homme au milieu", pour fournir un niveau avant que nous appelions notre dépendance tierce.

Ce module **shim** nous permet également de rendre nos dépendances **abstraites**. Les développeurs qui ont besoin d'utiliser nos dépendances tierces peuvent simplement utiliser une abstraction à la place (vous finirez probablement par l'envelopper dans une fonction ou une classe simple). Vous définirez les arguments par défaut à des valeurs par défaut sensées et essayerez de supprimer autant de détails d'implémentation fastidieux que possible.

Tout autre endroit qui a besoin de cette dépendance chargera simplement votre module, et ce module pourra être injecté où nécessaire.

**Pourquoi ?** Une grande raison que nous avons déjà discutée est que cela empêche vos dépendances et votre code d'être trop étroitement couplés.

Cela fonctionne lorsque vous ne l'avez que dans un seul module. Tant que tout le monde qui charge votre module respecte une interface/contrat de données pour ce module, tout le monde ailleurs "l'obtient gratuitement". Vous n'avez alors qu'à changer un module pour que de nombreux autres endroits aient accès à quelque chose.

Cela nous permet alors de faire des changements beaucoup plus facilement, et maintient une séparation claire des préoccupations dans le code.

Nous n'avons parlé ici que d'une seule dépendance – mais vous pouvez voir à quel point cela peut être pire si, par exemple, vous dépendez de 25 autres bibliothèques personnalisées et que vous devez comprendre comment elles fonctionnent. Cela serait généralement une base de code assez fragile, et serait une mauvaise pratique de code.

## Exemple de dépendance HTTP

Regardons un exemple de dépendance que vous pourriez utiliser pour créer un client HTTP simple.

C'est une dépendance de base qui vous permet de frapper des endpoints et de passer du JSON, etc., comme données.

Imaginons alors que nous utilisons actuellement **Fetch** dans Node et que nous voulons utiliser **Axios** (un autre client HTTP que nous voulons maintenant utiliser). Nous avons décidé d'abandonner Fetch et de passer à Axios parce que notre application grandit en complexité et nous avons trouvé qu'Axios correspond maintenant mieux à nos cas d'utilisation.

Si Fetch a fuit partout dans notre base de code, alors notre refactoring pour le supprimer sera beaucoup plus difficile que nécessaire.

Plutôt que d'aller simplement dans notre module où nous avons **shimé** l'appel de fonction, nous devons maintenant aller à chaque endroit où nous l'utilisons. Cela crée un effet domino dans le code source qui se produira inévitablement en changeant quelque chose à plusieurs endroits.

```javascript
// Vous allez maintenant devoir trouver tout endroit où vous avez importé fetch
// Tout endroit où vous l'avez aliasé
// Et traiter toute défaillance du code source entourant l'endroit où vous l'avez utilisé une fois qu'il est supprimé
// Ce qui pourrait être plus complexe que de simplement rechercher
const fetch = require('node-fetch');
```

Nous pouvons améliorer cela en enveloppant la dépendance dans une **abstraction shimée** appropriée et en isolant son utilisation à un seul endroit.

Vous obtenez également un avantage lors de l'intégration de nouvelles personnes. Elles pourront voir des abstractions appelées `API` ou `DataStore` qui deviennent des panneaux clairs indiquant ce que font vos classes (plutôt qu'une bibliothèque avec laquelle un développeur n'est peut-être pas familier).

```javascript
// Dans vos abstractions, vous avez le pouvoir de lui donner un nom descriptif
// si le nom actuel n'est pas clair dans votre code non plus, peut-être comme :

var Money = require('dinero')
```

Cela ne sera pas un problème pour les dépendances bien connues comme **Express** ou **Lodash** peut-être. Mais je n'ai pas une mémoire parfaite de chaque package NPM et de ce qu'ils font.

Lorsque vous l'avez correctement **shimé**, cela n'a même pas d'importance pour les développeurs utilisant votre shim si vous utilisez Fetch ou Axios "sous le capot". Ils ne verront jamais la différence si vous le changez, tant que vous êtes sensé avec le shim.

# Conclusion

J'espère que cela a donné un bon aperçu des avantages du **shimming**, et de la manière dont il vous aide à maintenir vos dépendances.

Cet article entier a été influencé par les écrits de Sarah Dayan, trouvés [ici](https://twitter.com/frontstuff_io/status/1264189583220244480), et partagés avec son consentement.

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et souhaitez en voir plus.