---
title: Que signifie JavaScript:Void(0) ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T18:06:00.000Z'
originalURL: https://freecodecamp.org/news/what-does-javascript-void-operator-do
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/jeremy-thomas-rMmibFe4czY-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Que signifie JavaScript:Void(0) ?
seo_desc: 'JavaScript’s void operator evaluates an expression and returns undefined.

  You can use the console to verify the same:


  Note: void, irrespective of any value passed along, always returns undefined as
  shown above. But, void with the operand 0 is prefer...'
---

L'opérateur void de JavaScript évalue une expression et retourne undefined.

Vous pouvez utiliser la console pour vérifier cela :

![ConsoleOutput](https://github.com/srawat19/-Guide_Images/blob/master/VoidConsole.PNG?raw=true)

**Note** : **void**, quelle que soit la valeur passée, *retourne toujours **undefined** comme montré ci-dessus*. Mais **void avec** l'**opérande 0 est préféré**.

Il y a deux façons d'utiliser l'opérande 0 : void(0) ou void 0. L'une ou l'autre est correcte.

## Quand utiliser Javascript void(0)

Utilisez javascript:void(0) si, lorsqu'un lien est cliqué, vous ne voulez pas que le navigateur charge une nouvelle page ou rafraîchisse la même page (selon l'URL spécifiée).

Au lieu de cela, il exécutera simplement le JavaScript attaché à ce lien.

### Exemple 1 avec Javascript void(0) :

```html
<html>
<body>
<a href="javascript:void(0);alert('Bonjour ! Je suis ici')">Cliquez-moi</a>
</body>
</html>
```

#### **Sortie :**

Lorsque quelqu'un clique sur le lien Cliquez-moi, une alerte apparaît comme ci-dessous :

![Output1](https://github.com/srawat19/-Guide_Images/blob/master/voidOutput1.PNG?raw=true)

### Exemple 2 avec Javascript void(0) :

```html
<html>
<body>
<a href="javascript:void(0)" ondblclick="alert('Salut, je n'ai pas rafraîchi la page')">Cliquez-moi</a>
</body>
</html>
```

#### **Sortie :**

Lorsque vous double-cliquez sur le lien, une alerte apparaîtra sans rafraîchissement de la page.

### Exemple 3 avec Javascript void(0) :

```html
<html>
<body>
<a href="javascript:void(0);https://www.google.co.in/" 
ondblclick="alert('Bonjour !! Vous me verrez et ne serez pas redirigé vers google.com')">Cliquez-moi</a>
</body>
</html>
```

#### **Sortie :**

Lorsque vous double-cliquez sur le lien, une alerte apparaîtra. La fermer ne vous redirigera pas vers google.com.

### Exemple sans Javascript void(0) :

```html
<html>
<body>
<a href="https://www.google.co.in/" ondblclick="alert('Bonjour !! Vous me verrez et serez ensuite redirigé vers google.com même si ce n'est pas nécessaire')">Cliquez-moi</a>
</body>
</html>
```

#### **Sortie :**

Lorsque vous double-cliquez sur le lien, une alerte apparaîtra, mais la fermer vous redirigera vers google.com.

## Conclusion

L'opérateur **void** est utile lorsque vous devez empêcher tout rafraîchissement ou redirection de page non désiré. Il exécute plutôt une opération JavaScript.

#### **Plus d'informations :**

1. [Documentation Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/void)