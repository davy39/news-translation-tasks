---
title: Un guide pour débutants sur Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T16:35:18.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-redux-9f652cbdc519
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BpaqVMW2RjQAg9cFHcX1pw.png
tags:
- name: beginner
  slug: beginner
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Un guide pour débutants sur Redux
seo_desc: 'By Safeer Hayat

  Understanding Redux as a beginner can be quite confusing. Redux has an abundance
  of new terms and concepts which are often pretty unintuitive. This guide presents
  a very simplified example of a Redux implementation. I will define each...'
---

Par Safeer Hayat

Comprendre Redux en tant que débutant peut être assez déroutant. Redux possède une abondance de nouveaux termes et concepts qui sont souvent assez peu intuitifs. Ce guide présente un exemple très simplifié d'une implémentation Redux. Je vais définir chacune des étapes et des termes de manière à ce que cela ait du sens pour un débutant complet.

Ce guide est destiné à démystifier les éléments de Redux. Il ne contient pas les définitions les plus techniquement précises. Il ne contient pas les meilleures pratiques. Il contient des définitions qui aideront à développer une compréhension pour quelqu'un sans connaissance préalable de ces concepts. Il y a une implémentation simple afin de ne pas confondre avec des détails inutiles.

L'exemple que nous allons parcourir dans ce guide sera une simple application de liste de tâches. L'application permet à un utilisateur d'ajouter ou de supprimer des éléments de la liste de tâches et de les voir affichés sur la page.

Je vais passer en revue étape par étape chaque élément de Redux, en expliquant ce que cet élément est et comment l'implémenter avec des exemples de code. Faites défiler jusqu'en bas pour voir l'exemple de code complet qui montrera comment tout cela s'assemble en une application React complète.

### Résumé des étapes

1. Écrire la fonction de réduction
2. Instancier le store dans le composant racine
3. Envelopper les composants avec le composant <Provider>, en passant le store comme une prop
4. Écrire le composant
5. Définir les actions
6. Définir le dispatch, attacher ceux-ci à l'endroit où les dispatches seront déclenchés (c'est-à-dire les écouteurs d'événements, etc.)
7. Définir la fonction mapStateToProps
8. Exporter la fonction connect, en passant mapStateToProps et null comme les 2 arguments et en passant le nom du composant dans la deuxième paire de crochets

### Étapes

#### 1. Écrire la fonction de réduction

La fonction de réduction est une fonction qui indique au store comment répondre aux actions. La fonction retourne le nouvel état mis à jour chaque fois qu'une action est dispatchée. L'état est immutable (ne peut pas être changé) donc le reducer retourne toujours un nouvel état. Le reducer utilise généralement l'opérateur de décomposition pour insérer l'état actuel dans un nouvel objet/tableau et y ajouter des éléments. La pratique courante est d'utiliser une instruction switch/case et de vérifier la propriété type de l'action passée. Ensuite, écrire le code qui met à jour l'état pour chaque cas.

Nous écrivons notre fonction de réduction en premier car nous devrons la passer lorsque nous instancierons notre store. Pour comprendre ce qui se passe, cependant, cela nécessite quelques connaissances sur les actions et le dispatch. Nous aborderons cela plus loin dans ce guide.

Pour l'instant, sachez que notre application de liste de tâches devra interagir avec le store de 2 manières : pour ajouter un nouvel élément de liste de tâches à l'état et pour supprimer un élément de la liste de tâches de l'état. Par conséquent, nous écrivons notre fonction de manière à ce qu'elle réponde à 2 cas de type d'action. Elle utilise la valeur de l'action pour ajouter ou supprimer un élément de la liste de tâches de l'état.

Le reducer reçoit 2 paramètres : state (c'est l'état entier actuellement dans le store, et nous lui donnons une valeur par défaut si l'état n'existe pas encore) et l'action. Nous retournons l'état dans le cas par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_HcMGsHCcl89CIbW5vBvxw.png)
_Fonction de réduction avec 2 cas_

#### 2. Instancier le store dans le composant racine

Le store est la chose qui contient réellement l'état. C'est un peu magique et vous n'avez pas vraiment besoin de connaître les tenants et les aboutissants. Tout ce que vous devez savoir, c'est que vous n'y accédez pas directement comme vous le feriez avec un état React normal. Vous y accédez et y apportez des modifications en utilisant des reducers, des actions et des dispatch.

L'autre chose importante à savoir sur le store est qu'il contient certaines méthodes utiles et importantes. La méthode principale est la fonction dispatch. Il contient également une méthode getState (pour visualiser l'état) et une méthode subscribe (exécute un callback chaque fois qu'une action est dispatchée).

Le store est généralement instancié à la racine de votre application (par exemple, App.js). Il est stocké sous forme de variable et le reducer est passé en tant que paramètre. Le store est ensuite passé en tant que prop au composant Provider.

Nous instancions notre objet store en passant le reducer que nous venons de créer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*z9nl7lgc1dTcLozE6HGjFA.png)
_Store instancié avec le reducer que nous avons créé dans l'étape précédente_

#### 3. Envelopper les composants avec le composant <Provider>, en passant le store comme une prop

Le Provider est un composant créé pour faciliter le passage du store à tous vos composants. Le composant Provider enveloppe tous vos composants (par exemple, rendre vos composants comme enfants de Provider). Vous passez le store en tant que prop uniquement au Provider. Cela signifie que vous n'avez pas besoin de passer le store en tant que prop à chaque composant, car chaque composant le reçoit du Provider. Cependant, cela ne signifie pas que les composants ont accès à l'état pour l'instant. Vous devez toujours utiliser mapStateToProps (nous aborderons cela plus tard) pour avoir l'état accessible dans votre composant.

Nous enveloppons le composant Todo que nous allons créer avec notre composant Provider. Nous passons le store que nous avons créé dans l'étape précédente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oc_ahULWaWmVo5l0SdmlAg.png)
_Les composants sont enveloppés avec le composant Provider avec le store passé en tant que prop_

#### 4. Écrire le composant

Ensuite, nous commençons à écrire le composant Todo qui affichera les éléments de la liste de tâches et interagira avec le store Redux.

Le composant est un composant d'état contenant un élément d'état pour suivre ce que l'utilisateur a tapé dans l'entrée. Nous avons une fonction appelée handleChange. Cette fonction met à jour l'état chaque fois que l'utilisateur tape quelque chose dans l'entrée. Pour l'instant, c'est tout ce que nous allons écrire. Nous devons comprendre davantage sur Redux avant de pouvoir écrire la logique. La logique ajoutera de nouvelles tâches à l'état et récupérera les tâches actuelles de l'état pour les afficher sur la page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QQYkjyrBinJy7Jiq4WjwLg.png)
_Le début du composant Todo qui permet à un utilisateur de saisir de nouveaux éléments de liste de tâches_

#### 5. Définir les actions

Une action est un objet simple contenant une propriété appelée 'type'. Cet objet est passé dans la fonction dispatch. Il est utilisé pour indiquer au store quel événement vient de se produire (en lisant la propriété type de l'action). Il indique également quelle mise à jour il doit apporter à l'état en réponse (via la fonction de réduction). L'action peut également contenir d'autres propriétés pour toute autre donnée que vous souhaitez passer dans le reducer. Les données ne peuvent être passées que par ici, donc toute donnée nécessaire devra être passée ici.

Nous utiliserons des créateurs d'actions pour définir nos actions. Les créateurs d'actions sont une fonction qui retourne l'objet d'action. Son but est de rendre l'action plus portable et testable. Cela ne change pas le comportement de la façon dont les choses fonctionnent. C'est une autre méthode d'écriture et de passage de l'action. Cela vous permet également de passer des paramètres si vous souhaitez envoyer des données avec l'action, ce que nous allons faire. Nous devons donc utiliser des créateurs d'actions ici.

Si vous vous souvenez, notre reducer a répondu à 2 types d'actions — "ADD_TODO" et "REMOVE_TODO". Nous allons définir ces actions avec nos créateurs d'actions. Dans notre action add_todo, nous retournerons "ADD_TODO" comme type et l'élément todo que nous voulons ajouter au store comme valeur (nous avons besoin que le store ajoute cet élément todo à l'état pour qu'il soit passé ici). Dans remove_todo, nous retournons "REMOVE_TODO" comme type et l'index de l'élément todo dans le store comme valeur. Nous en aurons besoin pour le supprimer de la liste des todos.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nTgkcNwagEXQUytjG6-Bdg.png)
_Nous définissons ici nos 2 actions dans les créateurs d'actions. Ce sont celles que notre reducer lit lorsqu'il est déclenché pour mettre à jour l'état._

Si vous revenez à notre définition de la fonction reducer, cela devrait maintenant avoir plus de sens. En lisant le action.type, le reducer sait s'il doit ajouter un todo à l'état ou en supprimer un. Il a l'élément todo passé dans add_todo. Il l'ajoute à l'état actuel en utilisant l'opérateur de décomposition. Dans remove_todo, il utilise l'opérateur de décomposition pour créer un nouveau tableau en ajoutant l'état actuel découpé deux fois, une fois avec tous les éléments avant celui à supprimer et une seconde avec tous les éléments après celui à supprimer, créant ainsi notre nouvel objet d'état avec l'élément todo supprimé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_HcMGsHCcl89CIbW5vBvxw.png)
_La fonction de réduction que nous avons définie précédemment_

Cependant, ce n'est toujours pas une image complète. Nous n'avons pas encore couvert comment le reducer est appelé et reçoit l'action appropriée. Pour cela, nous devons passer à la définition de notre fonction dispatch.

#### 6. Définir le dispatch, attacher ceux-ci à l'endroit où les dispatches seront déclenchés (c'est-à-dire les écouteurs d'événements, etc.)

La fonction dispatch est une méthode du store qui est utilisée pour déclencher un changement dans l'état. Tout événement ou toute chose qui doit mettre à jour l'état doit appeler la méthode dispatch pour le faire. C'est le seul moyen de déclencher un changement/mise à jour de l'état. Dispatch est appelé et l'objet d'action est passé (ou le créateur d'action si celui-ci a été utilisé). Une fois qu'un dispatch est déclenché, le store appelle ensuite la fonction de réduction et passe l'action que le dispatch a fournie, ce qui met à jour l'état, comme nous l'avons vu précédemment.

Ci-dessous, nous définissons la moitié inférieure de notre méthode de rendu des composants. Nous créons nos boutons qui contiendront nos gestionnaires d'événements. À l'intérieur de ceux-ci, nous définirons nos fonctions dispatch.

Le premier bouton est un simple bouton d'ajout. Ce bouton dispatchera l'action add_todo au store. Il passera l'entrée utilisateur actuelle comme valeur (c'est l'élément todo que le reducer ajoute au nouvel état). Notez que nous appelons dispatch en tant que `this.props.dispatch`. C'est un peu hors du cadre de ce guide de comprendre comment et pourquoi cela est passé en tant que prop au composant. Donc, sachez simplement que c'est le cas et que nous pouvons l'appeler comme cela.

Le deuxième gestionnaire d'événements est écrit comme un onClick sur notre élément todo rendu. En cliquant sur n'importe quel élément todo sur la page, il déclenche un gestionnaire d'événements. Le gestionnaire d'événements recherche la liste des todos et trouve l'index de ce todo dans la liste. Il dispatch ensuite l'action remove_todo et passe l'index.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5kkjqmwSjk5tbTs3mWKz0Q.png)
_La moitié inférieure de notre définition de composant incluant nos gestionnaires d'événements qui appellent la fonction dispatch_

Le cycle pour mettre à jour l'état dans le store Redux est maintenant entièrement défini. Nous savons que chaque fois que nous voulons changer l'état, nous devons appeler la méthode dispatch, passer l'action appropriée et nous assurer que notre reducer gère ces actions et retourne le nouvel état en utilisant les valeurs que nous avons passées via l'action.

La seule pièce manquante maintenant est comment obtenir l'état du store Redux. Vous avez probablement remarqué que j'ai mappé une liste appelée `this.props.todos` dans l'exemple précédent. Vous vous demandez peut-être d'où cela vient. Vous vous souvenez peut-être également qu'au début de ce guide, j'ai mentionné que le passage du store au composant Provider n'est pas suffisant pour accéder à l'état dans le store. Tout cela est abordé dans les 2 prochaines étapes alors que nous définissons notre fonction mapStateToProps et passons cela dans la fonction connect.

#### 7. Définir la fonction mapStateToProps

Lorsque vous voulez que votre composant ait accès à l'état, vous devez spécifier explicitement ce dans l'état à quoi le composant aura accès. Votre composant n'aura pas accès à l'état sans cela.

mapStateToProps est une fonction qui retourne simplement un objet qui définit quel état doit être passé dans le composant en attribuant des valeurs dans l'état aux propriétés que vous définissez dans cet objet. Essentiellement, l'objet que vous retournez dans mapStateToProps est ce que vos props seront dans votre composant. La fonction mapStateToProps est passée dans la méthode connect en tant que premier argument.

mapStateToProps prend l'état entier comme paramètre et vous prenez seulement ce dont vous avez besoin. Ici, cependant, comme notre état ne contient que la liste des todos. Nous avons besoin de cette liste dans notre composant ToDo, nous retournerons l'état entier comme une propriété appelée todos.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EI0ei8et6carOyDGwKzMew.png)
_Notre définition mapStateToProps qui attribue simplement l'état entier à une prop appelée todos_

Comme vous pouvez le voir maintenant, nous avons accès à notre liste complète de todos dans nos props en tant que `this.props.todos`. C'est ainsi que nous avons pu rendre tous nos todos dans l'exemple précédent en les mappant.

Enfin, nous devons passer cette fonction dans notre méthode connect pour tout connecter ensemble.

#### 8. Exporter la fonction connect, en passant mapStateToProps et null comme les 2 arguments et en passant le nom du composant dans la deuxième paire de crochets

Connect est une méthode qui relie les fonctions mapStateToProps et mapDispatchToProps (voir ci-dessous) à votre composant afin que le store puisse lire ces fonctions et s'assurer que ce que vous avez défini dedans soit passé dans le composant en tant que props. Cette méthode a une syntaxe spéciale qui ressemble à ceci :

`connect(mapStateToProps, MapDispatchToProps)(YourComponent)`

Vous passez les 2 fonctions `map...ToProps` à connect, puis le nom de votre composant à l'intérieur de la deuxième paire de crochets. Un modèle typique consiste à exporter la méthode connect au lieu de votre composant lorsque vous exportez votre composant à la fin de votre fichier. Par exemple :

`export default connect(mapStateToProps, MapDispatchToProps)(YourComponent)`

Cela agit ensuite de la même manière que l'exportation normale, sauf que l'état et les dispatches seront passés en tant que props. mapStateToProps et mapDispatchToProps sont en fait des paramètres optionnels pour connect. Si vous ne souhaitez pas en passer un ou les deux, mettez null à leur place.

Vous vous demandez peut-être d'où vient cette fonction mapDispatchToProps et pourquoi nous ne l'avons mentionnée nulle part avant ici. Eh bien, comme ce guide est l'exemple le plus simplifié d'un store Redux et que mapDispatchToProps n'est pas strictement obligatoire, je ne l'ai pas inclus dans notre exemple. Si vous ne passez pas mapDispatchToProps et passez null à la place, vous pouvez toujours accéder à la fonction dispatch dans votre composant comme nous l'avons fait précédemment en tant que `this.props.dispatch`.

Donc, pour terminer notre exemple d'application, tout ce que nous avons à faire est d'exporter notre composant en l'enveloppant avec la fonction connect et en passant mapStateToProps que nous venons de définir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gfbjcvHkDGt1J5jN2zV9eQ.png)
_Nous exportons notre composant en l'enveloppant avec la méthode connect et en passant notre fonction mapStateToProps_

Et c'est tout ! C'est une implémentation complète d'un store Redux. Voir ci-dessous pour l'exemple fonctionnel de ce que nous avons implémenté.

### Exemple de code complet annoté

> **App.js**

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Jn_9Tix-ErbBeCGaJSsGQ.png)
_Code complet pour le fichier App.js_

> **Todo.js**

![Image](https://cdn-media-1.freecodecamp.org/images/1*-cjCZtjQ4o_GYdd93fgxFw.png)
_Code complet pour le fichier Todo.js_

J'espère que ce guide peut simplifier certains des détails étranges et parfois déroutants de Redux. Ce n'est pas un guide complet de Redux, car il y a définitivement plus d'éléments et de modèles à comprendre. Mais si vous pouvez comprendre ce guide, alors vous êtes bien parti pour pouvoir travailler avec et installer Redux dans vos applications.