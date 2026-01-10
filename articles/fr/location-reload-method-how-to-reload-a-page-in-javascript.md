---
title: 'Méthode Location Reload : Comment recharger une page en JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-09T21:43:00.000Z'
originalURL: https://freecodecamp.org/news/location-reload-method-how-to-reload-a-page-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ecf740569d1a4ca3f4d.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: 'Méthode Location Reload : Comment recharger une page en JavaScript'
seo_desc: 'JavaScript Location.reload() method provides means to reload the page at
  current URL.

  The syntax is the following:

  object.reload(forcedReload);, where forceReload is an optional parameter.

  To simply reload the page, you can input window.location as o...'
---

La méthode JavaScript `Location.reload()` permet de recharger la page à l'URL actuelle.

La syntaxe est la suivante :

`object.reload(forcedReload);` où `forceReload` est un paramètre optionnel.

Pour recharger simplement la page, vous pouvez utiliser `window.location` comme objet.

Le paramètre optionnel `forceReload` est une valeur booléenne qui, si définie à :

`True`, recharge la page depuis le serveur (par exemple, ne stocke pas les données mises en cache par le navigateur) :

```text
window.location.reload(true);
```

`False`, recharge la page en utilisant la version de la page mise en cache par le navigateur.

```text
window.location.reload(false);
```

`False` est le paramètre par défaut, donc si laissé vide, `object.reload()` recharge la page en utilisant les données mises en cache par le navigateur, c'est-à-dire qu'il est identique à l'utilisation de la méthode `object.reload(false)`.

Pour créer l'effet de l'option "Actualiser" fournie par le navigateur, vous pouvez créer un bouton HTML et faire l'une des actions suivantes :

* attacher `Location.reload()` au balisage du bouton HTML, comme ceci :

```text
<input type="button" value="Bouton Actualiser" onClick="window.location.reload()"> 
```

* assigner un événement on-click au bouton avec la fonction qui utilise la méthode, où le bouton ressemble à ceci :

```text
<button type="button" onClick="reloadThePage()">Actualiser !</button>
```

```text
<script>
function reloadThePage(){
    window.location.reload();
} 
</script>
```

### **Exemple :**

```javascript
// Recharger les ressources actuelles depuis le serveur
window.location.reload(true);

// Recharger les ressources actuelles depuis le cache du navigateur
window.location.reload();
```

Cela rechargera la page à l'URL actuelle depuis le serveur.

#### **Plus d'informations :**

* [MDN](https://developer.mozilla.org/docs/Web/API/Location/reload)