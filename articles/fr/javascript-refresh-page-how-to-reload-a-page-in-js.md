---
title: JavaScript Actualiser la Page – Comment Recharger une Page en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-04-14T15:01:42.000Z'
originalURL: https://freecodecamp.org/news/javascript-refresh-page-how-to-reload-a-page-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-template--8-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Actualiser la Page – Comment Recharger une Page en JS
seo_desc: JavaScript is a versatile programming language that allows developers to
  create dynamic and interactive web applications. One common task in web development
  is to refresh or reload a web page, either to update its content or to trigger certain
  action...
---

JavaScript est un langage de programmation polyvalent qui permet aux développeurs de créer des applications web dynamiques et interactives. Une tâche courante dans le développement web consiste à actualiser ou recharger une page web, soit pour mettre à jour son contenu, soit pour déclencher certaines actions.

Dans cet article, nous allons explorer différentes façons d'actualiser une page en JavaScript et comprendre les avantages et les inconvénients de chaque approche.

## Pourquoi Actualiser une Page en JavaScript ?

Actualiser une page web peut être utile dans divers scénarios. Par exemple :

1. **Mise à Jour du Contenu :** Si le contenu d'une page web est dynamique et change fréquemment, vous devrez peut-être actualiser la page pour afficher les dernières données ou informations. Cela est couramment observé sur les sites d'actualités, les suiveurs de marché boursier, les applications météo, etc.
    
2. **Soumission de Formulaire :** Après avoir soumis un formulaire sur une page web, vous pourriez vouloir actualiser la page pour afficher un message de succès ou réinitialiser le formulaire pour une nouvelle soumission.
    
3. **Réinitialisation de l'État :** Dans certains cas, vous pourriez vouloir réinitialiser l'état d'une page web ou effacer certaines données pour repartir de zéro. Actualiser la page peut aider à atteindre cet objectif.
    

Maintenant, explorons différentes façons d'actualiser une page en JavaScript.

## Méthode 1 : Comment Actualiser la Page en Utilisant `location.reload()`

La manière la plus simple d'actualiser une page en JavaScript est d'utiliser la méthode `location.reload()`. Cette méthode recharge la page web actuelle depuis le serveur, en abandonnant le contenu actuel et en chargeant le contenu le plus récent.

```js
// Actualiser la page
location.reload();
```

### Avantages de l'Utilisation de location.reload()

* C'est simple et facile à utiliser.
    
* Elle recharge toute la page depuis le serveur, garantissant que vous obtenez le contenu le plus récent.
    

### Inconvénients de l'Utilisation de location.reload()

* Elle abandonne le contenu actuel de la page, ce qui peut entraîner une perte de saisie ou de données de l'utilisateur.
    
* Elle peut provoquer un effet de scintillement lors du rechargement de la page, ce qui peut affecter l'expérience utilisateur.
    

## Méthode 2 : Comment Actualiser la Page en Utilisant `location.replace()`

Une autre façon d'actualiser une page en JavaScript est d'utiliser la méthode `location.replace()`. Cette méthode remplace l'URL actuelle de la page web par une nouvelle URL, rechargeant effectivement la page avec le nouveau contenu.

Lorsque vous essayez cela dans votre console, vous remarquerez qu'elle affiche votre URL actuelle :

```js
console.log(location.href)
```

Cela signifie que lorsque vous utilisez la méthode `location.replace()` pour remplacer l'URL actuelle de la page web par une nouvelle URL (la même URL), votre page sera actualisée.

```js
// Actualiser la page en remplaçant l'URL par elle-même
location.replace(location.href);
```

### Avantages de l'Utilisation de location.replace()

* C'est un moyen rapide de recharger la page avec un nouveau contenu.
    
* Elle préserve le contenu actuel de la page et ne remplace que l'URL, évitant ainsi la perte de saisie ou de données de l'utilisateur.
    

### Inconvénients de l'Utilisation de location.replace()

* Elle remplace l'URL entière de la page, ce qui peut entraîner la perte de l'historique de navigation actuel.
    
* Elle peut ne pas fonctionner dans certains scénarios, comme lorsque la page web a été ouverte dans une nouvelle fenêtre ou un nouvel onglet.
    

## Méthode 3 : Comment Actualiser la Page en Utilisant `location.reload(true)`

La méthode `location.reload()` accepte également un paramètre booléen `forceGet` qui, lorsqu'il est défini sur `true`, force la page web à se recharger depuis le serveur, en contournant le cache.

Cela peut être utile lorsque vous souhaitez vous assurer d'obtenir le contenu le plus récent du serveur, même si la page est mise en cache.

```js
// Actualiser la page et contourner le cache
location.reload(true);
```

### Avantages de l'Utilisation de location.reload(true)

* Elle garantit que vous obtenez le contenu le plus récent du serveur, même si la page est mise en cache.
    

### Inconvénients de l'Utilisation de location.reload(true)

* Elle abandonne le contenu actuel de la page, ce qui peut entraîner une perte de saisie ou de données de l'utilisateur.
    
* Elle peut provoquer un effet de scintillement lors du rechargement de la page, ce qui peut affecter l'expérience utilisateur.
    

## Méthode 4 : Comment Actualiser la Page en Utilisant `location.href`

Une autre façon d'actualiser une page en JavaScript est d'utiliser la propriété `location.href` pour définir l'URL de la page web sur elle-même. Cela recharge effectivement la page avec la nouvelle URL, déclenchant une actualisation de la page.

```js
// Actualiser la page en définissant l'URL sur elle-même
location.href = location.href;
```

### Avantages de l'Utilisation de location.href

* C'est une méthode simple et efficace pour actualiser la page.
    
* Elle préserve le contenu actuel de la page et ne met à jour que l'URL, évitant ainsi la perte de saisie ou de données de l'utilisateur.
    

### Inconvénients de l'Utilisation de location.href

* Elle remplace l'URL entière de la page, ce qui peut entraîner la perte de l'historique de navigation actuel.
    
* Elle peut ne pas fonctionner dans certains scénarios, comme lorsque la page web a été ouverte dans une nouvelle fenêtre ou un nouvel onglet.
    

## Méthode 5 : Comment Actualiser la Page en Utilisant `location.reload()` avec un Délai

Si vous souhaitez ajouter un délai avant d'actualiser la page, vous pouvez utiliser la fonction `setTimeout()` en combinaison avec la méthode `location.reload()`.

Cela vous permet de spécifier un intervalle de temps en millisecondes avant que la page ne soit rechargée, vous donnant ainsi le contrôle sur le timing de l'actualisation.

```js
// Actualiser la page après un délai de 3 secondes
setTimeout(function(){
    location.reload();
}, 3000); // 3000 millisecondes = 3 secondes
```

### Avantages de l'Utilisation de location.reload() avec un Délai

* Elle vous permet de contrôler le timing de l'actualisation de la page en ajoutant un délai.
    
* Elle offre de la flexibilité dans les scénarios où vous souhaitez actualiser la page après un certain événement ou action.
    

### Inconvénients de l'Utilisation de location.reload() avec un Délai

* Elle peut provoquer un délai dans l'actualisation de la page, ce qui peut affecter l'expérience utilisateur.
    
* Elle peut ne pas fonctionner comme prévu dans les scénarios avec des connexions réseau instables ou lentes.
    

## Conclusion

Dans cet article, vous avez appris les différentes façons d'actualiser une page en JavaScript. Chaque méthode a ses avantages et ses inconvénients, ce qui devrait vous aider à choisir la meilleure méthode pour votre projet de développement web.

Lorsque vous utilisez l'une de ces méthodes pour actualiser une page, il est important de considérer l'impact sur l'expérience utilisateur, la perte de données et l'historique de navigation.

J'espère que cet article vous aide à comprendre comment recharger une page web en JavaScript et à choisir la méthode appropriée pour votre cas d'utilisation spécifique.

Bon codage !

Embarquez pour un voyage d'apprentissage ! [Parcourez 200+ articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part !