---
title: Comment fonctionne le stockage Web – Local vs Session Storage expliqué
subtitle: ''
author: Tooba Jamal
co_authors: []
series: null
date: '2022-10-12T14:08:46.000Z'
originalURL: https://freecodecamp.org/news/how-web-storage-works
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/webstorage-1-1.png
tags:
- name: data
  slug: data
- name: localstorage
  slug: localstorage
- name: storage
  slug: storage
seo_title: Comment fonctionne le stockage Web – Local vs Session Storage expliqué
seo_desc: 'Anyone who works with the web needs to store data for a later use. Backend
  developers have some powerful databases in their toolkit. But if you are a frontend
  developer, you can still store and process data using web storage.

  In this article, you''ll ...'
---

Toute personne travaillant avec le web a besoin de stocker des données pour une utilisation ultérieure. Les développeurs backend disposent de bases de données puissantes dans leur boîte à outils. Mais si vous êtes un développeur frontend, vous pouvez toujours stocker et traiter des données en utilisant le stockage web.

Dans cet article, vous apprendrez ce qu'est le stockage web, les différents types de stockage web et quand utiliser chacun d'eux.

## Qu'est-ce que le stockage Web ?

Le stockage web est une fonctionnalité HTML5 qui vous permet de stocker des données sous forme de paires clé-valeur dans le navigateur. Cela permet aux applications de stocker des données côté client afin que vous puissiez y accéder ou les manipuler plus tard. Toutes les données stockées dans le stockage web restent dans le navigateur et ne sont transférées nulle part ailleurs.

## Types de stockage web

Les deux principaux types de stockage web sont le stockage local et le stockage de session. Chacun a ses propres caractéristiques uniques.

Mais ils ont une chose en commun : ils stockent les données dans le navigateur particulier que l'utilisateur utilise pour accéder à la page web. Vous ne pourrez pas accéder aux mêmes données via un autre navigateur.

Examinons maintenant chacun d'eux en détail.

### Stockage Local

Le stockage local peut stocker 5 Mo de données par application pour toute la durée de vie de l'application. La fermeture du navigateur n'affectera en aucune façon les données – elles restent là à moins que vous ne les supprimiez.

Vous ne pouvez accéder à l'objet de stockage local qu'à travers `localStorage`. Les méthodes que vous pouvez utiliser pour effectuer des opérations sur l'objet localStorage sont :

```javascript
localStorage // pour accéder à l'objet localStorage 
localStorage.setItem('name', 'John') // définit name égal à john localStorage.getItem('name') // "John" 
localStorage.removeItem('name') // supprime name du localStorage localStorage.clear() // efface le localStorage
```

`localStorage.setItem()` prend une clé et une valeur en tant que paramètres et définit un nouvel élément dans l'objet de stockage local égal à la paire clé-valeur donnée.

`localStorage.getItem()` prend une clé en tant que paramètre et retourne la valeur stockée pour cette clé dans le stockage.

`localStorage.clear()` efface tout l'objet localStorage.

`localStorage.removeItem()` prend une clé en tant que paramètre et supprime la paire clé-valeur correspondante.

Tout élément que vous stockez dans localStorage sera stocké sous forme de chaîne de caractères. Cela signifie que vous devez convertir d'autres types de données tels que les tableaux ou les objets en chaînes de caractères – sinon vous perdez leur structure.

Voir l'exemple ci-dessous :

```javascript
const scores = [10, 8, 6, 3, 9] 
const scoresJSON = JSON.stringify(scores) 
localStorage.setItem('scores', scoresJSON) 
localStorage // sortie >> {scores: '[10, 8, 6, 3, 9]', length: 1}
```

Dans l'exemple ci-dessus, nous avons d'abord créé un tableau de scores, puis nous l'avons converti en chaîne de caractères en utilisant JSON.stringify(), et enfin nous avons sauvegardé le tableau de scores converti en chaîne dans localStorage.

Prenez votre temps pour regarder la sortie que j'obtiens lorsque j'exécute le même extrait de code dans la console de mon navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/localstorage-3.png)
_Exemple de code dans la console du navigateur_

Notez que la clé scores a une valeur égale à notre tableau de scores converti en chaîne. Mais si nous ne convertissons pas le tableau de scores en chaîne, notre tableau perdra sa structure et les éléments seront sauvegardés sous forme de chaîne comme ci-dessous :

```javascript
const scores = [10, 8, 6, 3, 9] 
localStorage.setItem('scores', scores) 
localStorage // sortie >> {scores: '10, 8, 6, 3, 9', length: 1}

```

Exécutons également le code dans la console du navigateur pour voir ce qui est journalisé dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/localstorage-2.png)
_Sauvegarde d'un tableau sans le convertir en chaîne_

Voyez comment notre tableau de scores est converti en chaîne lorsque nous ne le convertissons pas en chaîne en utilisant JSON.stringify() ?

### Stockage de Session

Le stockage de session vous permet de stocker des données dans le navigateur en fonction de la mémoire système et des données stockées dans le navigateur jusqu'à ce que le navigateur soit fermé. En d'autres termes, la fermeture du navigateur effacera toutes les données stockées dans le stockage de session.

Comme localStorage, vous pouvez accéder au stockage de session en tapant sessionStorage dans la console du navigateur.

```javascript
sessionStorage // accéder au stockage de session 
sessionStorage.setItem('name', 'John') // ajouter name au stockage de session avec la valeur john 
sessionStorage.getItem('name') // obtenir l'élément name du stockage de session sessionStorage.removeItem('name') // supprimer l'élément name du stockage de session sessionStorage.clear() // effacer le stockage de session
```

`sessionStorage.setItem()` prend une clé et une valeur en tant que paramètres et définit un nouvel élément dans l'objet de stockage local égal à la paire clé-valeur donnée.

`sessionStorage.getItem()` prend une clé en tant que paramètre et retourne la valeur stockée pour cette clé dans le stockage.

`sessionStorage.removeItem()` prend une clé en tant que paramètre et supprime la paire clé-valeur correspondante.

`sessionStorage.clear()` efface tout l'objet localStorage.

Comme localStorage, tout élément stocké dans sessionStorage sera stocké sous forme de chaîne de caractères. Cela signifie que nous devons les convertir en chaînes de caractères avant de les stocker dans le sessionStorage.

## Cas d'utilisation du stockage Web

Vous pouvez utiliser le **stockage local** lorsque vous souhaitez que vos données soient disponibles lorsque l'utilisateur revisite la page web, comme pour un panier d'achat ou un score de jeu/quiz. Gardez simplement à l'esprit que les informations sauvegardées dans le stockage local ne doivent pas être sensibles.

Vous pouvez utiliser le **stockage de session** lorsque les données à sauvegarder sont sensibles. L'authentification de l'utilisateur est un exemple de données que vous souhaitez effacer dès que l'utilisateur ferme l'onglet.

## Conclusion

Dans cet article, vous avez appris les méthodes modernes de stockage de données temporaires dans le navigateur. J'espère que cela vous a aidé à comprendre comment et quand utiliser les deux types de stockage web dans vos projets.

Intéressé à se connecter sur LinkedIn ? Contactez-moi sur [Tooba Jamal](https://www.linkedin.com/in/tooba-jamal/).