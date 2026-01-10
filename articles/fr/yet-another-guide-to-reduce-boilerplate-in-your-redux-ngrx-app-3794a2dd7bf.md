---
title: Un autre guide pour réduire le code répétitif dans votre application Redux
  (NGRX)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-05T23:47:09.000Z'
originalURL: https://freecodecamp.org/news/yet-another-guide-to-reduce-boilerplate-in-your-redux-ngrx-app-3794a2dd7bf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jtOmHUt-CfaFwspj81N6kA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Un autre guide pour réduire le code répétitif dans votre application Redux
  (NGRX)
seo_desc: 'By Andrey Goncharov

  What are we gonna cover here?

  In this article, we’re gonna discuss several ways/tips/tricks/ancient black magic
  rituals to reduce boilerplate in our overwhelmed-with-boilerplate Redux (and NGRX!)
  apps. I’ve come up with these over...'
---

Par Andrey Goncharov

### **Qu'allons-nous couvrir ici ?**

Dans cet article, nous allons discuter de plusieurs façons/conseils/astuces/rituels de magie noire ancestrale pour réduire le code répétitif dans nos applications Redux (et NGRX !) submergées de code répétitif. J'ai élaboré ces méthodes au fil des années grâce à mon expérience de production.

Soyons honnêtes. Au début, je voulais simplement parler de ma nouvelle micro-bibliothèque [flux-action-class](https://github.com/keenondrums/flux-action-class). Mais il semble que les blogs techniques ressemblent de plus en plus à Twitter ces derniers temps... et peut-être que vous voulez une lecture plus longue et plus significative. Alors je me suis dit : « Pourquoi pas ? J'ai quelques expériences et meilleures pratiques sur lesquelles j'ai transpiré et saigné. Peut-être que cela pourrait aider certaines personnes. Peut-être que les gens pourraient m'aider à améliorer certaines de ces pratiques. »

### Identifier le code répétitif

Examinons un exemple typique de la façon de faire des requêtes AJAX dans Redux. Dans ce cas particulier, imaginons que nous voulons obtenir une liste de chats depuis le serveur.

*Si vous vous demandez pourquoi j'ai des factories de sélecteurs (makeSelector...) regardez [ici](https://redux.js.org/recipes/computing-derived-data#computing-derived-data)*

Je laisse volontairement de côté la gestion des effets secondaires. C'est un sujet pour un article différent, rempli de colère et de critiques d'adolescent pour l'écosystème existant :D

Ce code présente plusieurs points faibles :

* Les créateurs d'actions sont des objets uniques en eux-mêmes, mais nous avons toujours besoin de types d'actions pour la sérialisation. Pourrions-nous faire mieux ?
* Lorsque nous ajoutons des entités, nous continuons à dupliquer la même logique pour basculer le flag `loading`. Les données réelles du serveur et la manière dont nous voulons les traiter peuvent changer, mais la logique pour `loading` est toujours la même. Pourrions-nous nous en débarrasser ?
* L'instruction switch est O(n) (ce qui n'est pas un argument solide en soi car Redux n'est pas très performant de toute façon). Redux nécessite quelques lignes de code supplémentaires pour chaque cas et les switches ne peuvent pas être facilement combinés. Pourrions-nous trouver quelque chose de plus performant et lisible ?
* Avons-nous vraiment besoin de conserver une erreur pour chaque entité séparément ?
* Utiliser des sélecteurs est une bonne idée. De cette façon, nous avons une abstraction sur notre store et pouvons changer sa forme sans casser toute l'application en ajustant simplement nos sélecteurs. Pourtant, nous devons créer une factory pour chaque sélecteur en raison du fonctionnement de la mémoïsation. Y a-t-il une autre façon ?

### Astuce 1 : Se débarrasser des types d'actions

Eh bien, pas vraiment. Mais nous pouvons faire en sorte que JS les génère pour nous !

Prenons une minute pour réfléchir à pourquoi nous avons besoin de types d'actions. Bien sûr, pour aider le reducer à différencier les actions entrantes et à changer notre état en conséquence. Mais doit-ce vraiment être une chaîne de caractères ? Si seulement nous avions un moyen de créer des objets (actions) de certains types... Les classes à la rescousse ! Nous pourrions définitivement utiliser des classes comme créateurs d'actions et faire un `switch` par type. Comme ceci :

Tout est bien, mais voici un problème... Nous ne pouvons plus sérialiser et désérialiser nos actions. Elles ne sont plus de simples objets avec un prototype de Object. Toutes ont des prototypes uniques qui font que le switch sur `action.constructor` fonctionne. Zut, j'aimais l'idée de sérialiser mes actions en une chaîne de caractères et de l'attacher aux rapports de bugs. Alors pourrions-nous faire encore mieux ?

En fait, oui ! Heureusement, chaque classe a un nom, qui est une chaîne de caractères, et nous pourrions les utiliser. Ainsi, pour les besoins de la sérialisation, chaque action doit être un simple objet avec un champ `type` (veuillez consulter [ici](https://github.com/redux-utilities/flux-standard-action) pour savoir ce que toute action qui se respecte devrait avoir d'autre). Nous pourrions ajouter un getter `type` à chacune de nos classes qui utiliserait le nom de la classe.

Cela fonctionnerait, mais de cette façon, nous ne pouvons pas préfixer nos types d'actions comme le suggère [cette](https://github.com/erikras/ducks-modular-redux) excellente proposition (en fait, j'aime encore plus son [successeur](https://github.com/alexnm/re-ducks)). Pour contourner le préfixage, nous devrions cesser d'utiliser directement le nom de la classe et créer un autre getter pour celui-ci. Cette fois, un getter statique.

Polissons cela un peu pour éviter la duplication de code et ajoutons une autre hypothèse pour réduire encore plus le code répétitif. Si l'action est une action d'erreur, `payload` doit être une instance de `Error`.

À ce stade, cela fonctionne parfaitement avec NGRX. Redux se plaint de la distribution d'objets non simples (il valide la chaîne de prototypes). Heureusement, JS nous permet de retourner une valeur arbitraire depuis le constructeur et nous n'avons pas vraiment besoin que nos actions aient un prototype.

Pour éviter que vous ne copiez-colliez la classe `ActionStandard` et que vous ne vous inquiétiez de sa fiabilité, j'ai créé une [petite bibliothèque appelée flux-action-class](https://github.com/keenondrums/flux-action-class), qui contient déjà tout ce code couvert par des tests avec une couverture de code de 100 %, écrite en TypeScript pour les projets TypeScript et JavaScript.

### Astuce 2 : Combiner vos reducers

L'idée est simple : utilisez [combineReducers](https://redux.js.org/api/combinereducers) non seulement pour les reducers de niveau supérieur, mais aussi pour combiner les reducers pour `loading` et autres. Laissez le code parler de lui-même :

### Astuce 3 : Passer du switch à autre chose

Utilisez des objets et choisissez parmi eux par clé ! Choisir une propriété d'un objet par clé est O(1) et cela semble beaucoup plus propre si vous me demandez. Comme ceci :

Je suggère de refactoriser un peu `reducerLoading`. Avec l'introduction des maps de reducers, il est logique de retourner une map de reducers depuis `reducerLoading`. Nous pourrions l'étendre si nécessaire (contrairement aux switches).

[La documentation officielle de Redux mentionne cela](https://redux.js.org/recipes/reducing-boilerplate#generating-reducers), mais pour une raison quelconque, j'ai vu beaucoup de gens utiliser encore des switch-cases. Il existe déjà une [bibliothèque](https://github.com/kolodny/redux-create-reducer) pour `createReducer`. N'hésitez pas à l'utiliser.

### Astuce 4 : Avoir un gestionnaire d'erreurs global

Il n'est pas nécessaire de conserver une erreur pour chaque entité. Dans la plupart des cas, nous devons afficher une boîte de dialogue d'erreur ou quelque chose. La même boîte de dialogue d'erreur pour toutes !

Créez un gestionnaire d'erreurs global. Dans le cas le plus simple, cela pourrait ressembler à ceci :

Ensuite, dans le bloc `catch` de votre effet secondaire, dispatch `ErrorInit`. Cela pourrait ressembler à ceci avec [redux-thunk](https://github.com/reduxjs/redux-thunk) :

Ensuite, vous pourriez arrêter de fournir un reducer pour la partie `error` de l'état des chats et `CatsGetError` juste pour basculer le flag `loading`.

### Astuce 5 : Arrêter de mémoïser tout

Examinons une fois de plus le désordre que nous avons avec les sélecteurs. 
*J'ai omis `makeSelectorCatsError` en raison de ce que nous avons découvert dans la section précédente.*

Pourquoi créer des sélecteurs mémoïsés pour tout ? Qu'y a-t-il à mémoïser ? Choisir un champ d'objet par clé (ce qui se passe exactement ici) est O(1). Écrivez simplement une fonction régulière non mémoïsée. Utilisez la mémoïsation uniquement lorsque vous souhaitez changer la forme des données dans votre store de manière à nécessiter un temps non constant avant de les retourner à votre composant.

La mémoïsation pourrait avoir du sens uniquement si des données dérivées sont calculées. Pour cet exemple, imaginons que chaque chat est un objet avec un champ `name` et que nous avons besoin d'une chaîne contenant les noms de tous les chats.

### Conclusion

Examinons ce avec quoi nous avons commencé :

Et voici le résultat :

Espérons que vous avez trouvé quelque chose d'utile pour votre projet. N'hésitez pas à me communiquer vos commentaires ! J'apprécie certainement toute critique et toute question.