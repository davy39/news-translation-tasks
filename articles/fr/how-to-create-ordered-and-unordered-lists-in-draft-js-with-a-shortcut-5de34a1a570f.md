---
title: Comment créer des listes ordonnées et non ordonnées dans Draft.js avec un raccourci
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-14T17:40:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-ordered-and-unordered-lists-in-draft-js-with-a-shortcut-5de34a1a570f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*CrE6mvHFmfzE8Nzz
tags:
- name: DraftJS
  slug: draftjs
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment créer des listes ordonnées et non ordonnées dans Draft.js avec
  un raccourci
seo_desc: 'By Andrey Semin

  We at Propeller have encountered many differences between Draft.js and popular text
  editors. We also found some issues like controlling list depth and multiline items
  in lists. The biggest difference is the inability to use shortcuts ...'
---

Par Andrey Semin

Nous chez [Propeller](https://www.propellercrm.com/) avons rencontré de nombreuses différences entre Draft.js et les éditeurs de texte populaires. Nous avons également trouvé certains problèmes comme le contrôle de la profondeur des listes et des éléments multilingues dans les listes. La plus grande différence est l'impossibilité d'utiliser des raccourcis pour démarrer une liste par défaut. Étonnamment, vous devez implémenter cette logique vous-même.

Comme toujours, il existe un [plugin](https://www.npmjs.com/package/draft-js-list-shortcut-plugin) disponible pour ajouter la prise en charge des raccourcis que vous utilisez. Je souhaite également faire référence à [draft-js-autolist-plugin](https://github.com/icelab/draft-js-autolist-plugin) comme source d'inspiration. Pour une raison quelconque, ce plugin n'a pas fonctionné lorsque nous l'avons essayé. Nous avons donc trouvé notre propre solution, qui est maintenant présentée dans cet article.

### Le problème

Ouvrez Google Docs, Word365 ou tout autre éditeur que vous utilisez. Essayez de taper `*` puis tapez `espace`. Boom ! Vous avez commencé une liste non ordonnée. Belle fonctionnalité à avoir, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*2mOm_bMFavV3jy2g3a-wvA.gif)

Si nous essayons le même truc avec la configuration par défaut de Draft.js, nous n'obtiendrons rien d'autre que du texte brut.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ExCt2l6cP0BUhRjq036IKg.gif)

Changeons cela !

### Solution

Pour implémenter cette fonctionnalité, nous devons suivre les trois dernières touches pressées. Pourquoi trois ? Eh bien, c'est parce que la combinaison de caractères la plus longue que nous devons prendre en charge est `1. + espace`, ce qui fait exactement trois pressions.

Pour commencer, implémentons la logique pour stocker ces pressions. Ici, nous utiliserions un simple tableau nommé `history`. Ce tableau stockera la valeur de la touche qui a été pressée. Nous ne voulons définitivement pas traiter les pressions de touches avec des modificateurs comme `shift`, `alt`, etc. Nous pouvons utiliser la fonction intégrée `KeyBindingUtil.hasCommandModifier` de Draft.js pour effectuer la vérification de tout modificateur.

Draft.js expose un événement `keyDown` pour nous dans la fonction `keyBindingFn`. Nous allons vérifier si nous devons démarrer une liste ici. Si c'est le cas, nous devons retourner une commande appelée `DraftEditorCommand`, qui est une chaîne de caractères. De plus, pour bénéficier des commandes au niveau du système d'exploitation, nous devons ajouter un appel à la fonction `getDefaultKeyBinding` comme cas de repli.

Nous devons vérifier si la touche actuellement pressée est un `espace`. Si c'est le cas, nous exécuterons nos vérifications contre le tableau `history`. Nous vérifions si nous avons un ensemble approprié de touches précédemment pressées — `*` pour une liste non ordonnée et `1.` pour une liste ordonnée. Si nous trouvons une correspondance, nous retournons une commande (chaîne de caractères) à traiter plus tard.

Maintenant, nous devons implémenter la fonction `handleKeyCommand` et la passer à l'éditeur. La logique est assez simple. Si nous obtenons une de nos commandes personnalisées, nous vérifions si nous devons démarrer une liste sur le bloc actuel. Voici donc un squelette de la fonction `handleKeyCommand`.

Pour vérifier si nous pouvons démarrer une liste, nous vérifions si le bloc actuellement sélectionné satisfait les trois règles suivantes :

* Le type de bloc est `unstyled`
* Le bloc a une `depth` de 0
* le bloc a `*` ou `1.` comme texte

Enveloppons le tout avec le code :

Maintenant, nous sommes en mesure de capturer le cas exact où Draft.js doit démarrer une liste ! Maintenant, il est temps d'implémenter la fonction `startList`.

Tout d'abord, nous devons mapper nos commandes personnalisées à un style de liste particulier. Cela signifie que nous devons démarrer une liste non ordonnée pour la commande `start-unoredered-list`.

Nous démarrons une liste ordonnée pour la commande `start-ordered-list`. Ensuite, nous devons mettre à jour le style du bloc vers le type sélectionné. Pour ce faire, nous utiliserions la fonction `toggleBlockType` du module `RichUtils`, qui fait partie de Draft.js.

Ensuite, nous devons remplacer le texte de raccourci que nous avons entré par une chaîne vide. Pour ce faire, nous devons appeler la méthode `replaceText` du module `Modifier`. Cette méthode nécessite une plage de sélection pour déterminer ce qui doit être remplacé. Nous devons obtenir la sélection du bloc et la mettre à jour pour que la valeur `focusOffset` soit égale à la longueur du bloc. Cette combinaison signifie que nous voulons remplacer tout le texte que nous avons entré.

Super ! Maintenant, nous devons mettre à jour notre état local de l'éditeur avec le nouvel état que nous obtenons de la fonction `startList`. Alors, rassemblons le tout !

OK ! Nous avons presque terminé ! Mais il y a un autre moment que nous devons gérer. Dans certains cas, lorsque l'une de nos commandes personnalisées se déclenche, nous ne devons pas démarrer une liste en fonction de la sortie de la fonction `shouldStartList`. Nous devons traiter l'insertion de l'espace manuellement.

Pour les détails d'implémentation de la méthode `getSelectedBlock`, consultez [mon précédent article](https://medium.com/p/800fb3a6714c) sur ce sujet Draft.js !

Pour ce faire, nous pouvons utiliser une méthode appelée `insertText` du module `Modifier`. Comme son nom l'indique, elle est utilisée pour construire un nouvel état de contenu avec le texte fourni inséré dedans. Comme toujours, nous devons fournir l'état actuel du contenu, l'état actuel de la sélection et le texte que nous voulons insérer (un seul espace dans notre cas).

Nous devons ajouter un appel à cette fonction à notre fonction `handleKeyCommand`. Voici donc la version finale :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KB28XT74Srehykb3VRSOyw.gif)
_Nous avons ajouté la prise en charge des raccourcis de listes. Bon travail !_

Si vous avez lu cet article jusqu'au bout, vous pouvez également consulter [mon précédent article](https://medium.com/p/800fb3a6714c) sur l'enchantement de Draft.js. Vous pouvez également l'appliquer à votre projet.