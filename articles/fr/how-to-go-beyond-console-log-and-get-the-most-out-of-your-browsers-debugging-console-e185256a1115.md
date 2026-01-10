---
title: Comment aller au-delà de console.log et tirer le meilleur parti de la console
  de débogage de votre navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-17T14:42:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-go-beyond-console-log-and-get-the-most-out-of-your-browsers-debugging-console-e185256a1115
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Lvtq6fDOejQmexdK5t2Npw.png
tags:
- name: console
  slug: console
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment aller au-delà de console.log et tirer le meilleur parti de la console
  de débogage de votre navigateur
seo_desc: 'By Gilad Dayagi

  The console object is a very useful feature of browsers that has been around for
  many years. It provides access to the browser’s debugging console.Most web developers
  know how to print messages to the console using console.log. But I’...'
---

Par Gilad Dayagi

L'objet `console` est une fonctionnalité très utile des navigateurs qui existe depuis de nombreuses années. Il permet d'accéder à la console de débogage du navigateur. 
La plupart des développeurs web savent comment afficher des messages dans la console en utilisant `console.log`. Mais j'ai remarqué que beaucoup ne connaissent pas les autres fonctionnalités de la `console`, alors qu'elles peuvent être très utiles pour chaque développeur web.

Dans cet article, je vais passer en revue certaines de ces fonctionnalités et capacités moins connues. J'espère que vous les trouverez utiles et intéressantes, et que vous les intégrerez dans votre flux de travail et votre code au quotidien.

J'ai ajouté une capture d'écran du résultat de chaque exemple. Si vous souhaitez essayer les choses par vous-même, ouvrez simplement les DevTools et copiez-collez les exemples.

### Utilisation de plusieurs arguments

Il est assez courant de journaliser plusieurs valeurs ensemble. Il peut s'agir d'un message accompagné d'une valeur associée ou du contenu de plusieurs variables associées.

Voici deux méthodes que j'ai vues les développeurs utiliser pour y parvenir :

#### 1. Concatenation de chaînes

```
const a = 123;const b = 'abc';const c = {aa: 234, bb: 345};console.log('Foo bar ' + a + ' ' + b + ' ' + c);
```

![Image](https://cdn-media-1.freecodecamp.org/images/WFSwkoS7zJAs08juQqlWTIZ2O2I8NVELVZ1Y)
_Résultat de la concatenation de chaînes_

#### 2. Utilisation de plusieurs appels

```
const a = 123;const b = 'abc';const c = {aa: 234, bb: 345};console.log('Foo bar');console.log(a);console.log(b);console.log(c);
```

![Image](https://cdn-media-1.freecodecamp.org/images/d2KZzOM5YcPtJSnoSwxdg4rS9XrUEkAKs6lr)
_Résultat de plusieurs appels_

Ces méthodes peuvent fonctionner (en quelque sorte), mais :

* Elles ne sont pas flexibles
* Elles ne sont pas très lisibles
* Elles sont fastidieuses à écrire
* Elles nécessitent des moyens spéciaux pour fonctionner correctement avec les variables d'objet

Il existe plusieurs alternatives meilleures pour sortir plusieurs variables. La plus utile pour un vidage rapide de données est d'envoyer plusieurs arguments à `console.log`, comme ceci :

```
const a = 123;const b = 'abc';const c = {aa: 234, bb: 345};console.log('Foo bar', a, b, c);
```

![Image](https://cdn-media-1.freecodecamp.org/images/5oOGL4AISGJppBuuhXTHdQst6tNS6rK0a5oO)
_Résultat de plusieurs arguments_

Cela est très pratique pour le débogage, mais la sortie n'est pas très contrôlable. Pour une sortie destinée à être lue (comme pour une bibliothèque), j'utiliserais une méthode différente, que nous verrons plus tard.

### Utilisation de différents niveaux de journalisation

Outre le familier `console.log`, il existe d'autres méthodes de journalisation qui correspondent à différents niveaux de journalisation :

```
console.debug('Message de débogage');console.info('Message d'information');console.log('Bon vieux message de journalisation');console.warn('Un message d'avertissement');console.error('Ceci est une erreur');
```

![Image](https://cdn-media-1.freecodecamp.org/images/7LZRb5ZUSjcnw5ObZc96va9fzNjsJpudvrhS)
_Niveaux de journalisation tels que vus dans Google Chrome_

Chaque niveau de journalisation peut avoir un style par défaut différent, ce qui facilite l'identification des erreurs et des avertissements d'un coup d'œil.

Vous pouvez généralement également filtrer les niveaux de journalisation que vous souhaitez voir dans la console des DevTools. Cela peut aider à réduire l'encombrement.

![Image](https://cdn-media-1.freecodecamp.org/images/4FS42J3jrB8sTwERLqDj-KS-5-8bq8GkXw0T)
_Filtrer les niveaux de journalisation dans Google Chrome_

L'apparence des différents niveaux et la granularité du filtrage changent d'un navigateur à l'autre.

### Regroupement des lignes de la console

Parfois, il est utile de regrouper les messages de journalisation ensemble. Cela peut permettre une sortie plus organisée et plus lisible.

Cela est en fait très simple à réaliser :

```
console.group();console.log('Premier message');console.log('Deuxième message');console.groupEnd();
```

![Image](https://cdn-media-1.freecodecamp.org/images/GYLLEc1rejWitvOzcAAIUyrzWGxYkIe7C4OI)
_Messages de journalisation regroupés_

Notez que les groupes de journalisation peuvent également être imbriqués et étiquetés :

```
console.group('Groupe aaa');console.log('Premier message');console.group('Groupe bbb');console.log('message de niveau 2 a');console.log('Message de niveau 2 b');console.groupEnd();console.log('Deuxième message');console.groupEnd();
```

![Image](https://cdn-media-1.freecodecamp.org/images/ddmYWHrx7W0lAeHRE0mLPx7wKk-adr2lxT00)
_Groupes imbriqués et étiquetés_

Si vous souhaitez que le groupe apparaisse replié, utilisez `console.groupCollapsed()`

### Mesure des performances

Mesurer le temps entre des points dans le code peut servir de moyen rapide pour vérifier les performances de certaines opérations.

Voici une manière triviale de faire cela :

```
const start = Date.now();// faire quelques chosesconsole.log('A pris ' + (Date.now() - start) + ' millisecondes');
```

Cela fonctionne, mais il existe une manière plus élégante d'obtenir quelque chose de similaire :

```
console.time('Étiquette 1');// faire quelques chosesconsole.timeEnd('Étiquette 1');
```

![Image](https://cdn-media-1.freecodecamp.org/images/OBuRCdSdW7cLv9BSmKHsTGcpwizTlUehKbEj)
_Mesurer le temps avec la console_

Le code est plus court, la mesure est plus précise, et vous pouvez suivre jusqu'à 10 000 minutages différents en parallèle sur une page.

### Substitution de chaîne

Précédemment, nous avons appris que vous pouvez passer plusieurs arguments à `console.log` pour sortir plusieurs valeurs simultanément. Une autre façon d'obtenir quelque chose de similaire est d'utiliser la substitution de chaîne. Cette méthode nécessite de connaître les placeholders disponibles, mais offre un meilleur contrôle sur la sortie.

```
const a = 123;const b = 'abc';const c = {aa: 234, bb: 345};console.log('nombre %d chaîne %s objet %o', a, b, c);
```

![Image](https://cdn-media-1.freecodecamp.org/images/m5jIme1eJX9jT0wCHsBxA6mSUyG70r5Af4aQ)
_Journalisation avec substitution de chaîne_

Consultez la documentation (lien à la fin) pour une liste des placeholders disponibles.

### Stylisation

Il peut être agréable de styliser différemment les messages de journalisation pour augmenter la lisibilité.

Nous avons déjà mentionné que les navigateurs donnent différents styles par défaut à certains niveaux de journalisation, mais cela peut également être personnalisé selon vos besoins spécifiques. La stylisation est effectuée en utilisant un sous-ensemble de règles CSS, passé dans une chaîne en tant que deuxième paramètre, et appliqué en utilisant le marqueur `%c`.

Notez que vous pouvez avoir différents styles pour différentes parties du message de journalisation.

Par exemple :

```
console.log("Normal %cStylisé %clorem %cipsum", "color: blue; font-weight: bold", "color: red", "background-image: linear-gradient(red, blue); color: white; padding: 5px;");
```

![Image](https://cdn-media-1.freecodecamp.org/images/al9DXYCJEKx4DtYd1gHx4K8CjKrn0xRCEznU)
_Messages de journalisation stylisés_

### Résumé

Dans cet article, nous avons vu certaines des fonctionnalités de `console` que je pense être moins connues et plus utiles. Ce n'est en aucun cas une liste exhaustive de tout ce que la `console` peut faire, car elle a encore beaucoup d'autres astuces.

Si cela vous a intéressé et que vous souhaitez découvrir ce que vous pouvez faire d'autre avec la `console`, je vous recommande de lire la [documentation pertinente sur MDN](https://developer.mozilla.org/en-US/docs/Web/API/console) et d'essayer des choses dans les DevTools.

*Si vous avez trouvé cela utile, veuillez partager cet article sur les réseaux sociaux.*  
*Vous pouvez également me suivre sur Twitter (@giladaya). Merci pour la lecture !*