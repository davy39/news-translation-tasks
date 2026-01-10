---
title: Node.js module.exports vs. exports
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-07T14:15:39.000Z'
originalURL: https://freecodecamp.org/news/node-js-module-exports-vs-exports-ec7e254d63ac
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb7b4740569d1a4cae663.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Node.js module.exports vs. exports
seo_desc: 'By lazlojuly

  What are they, how to use them and how not to use them

  (Note that this article was written after the Node.js 6.1.0 release)

  TL;DR


  Think of module.exports as the variable that gets returned from require(). It is
  an empty object by defaul...'
---

Par lazlojuly

#### Qu'est-ce que c'est, comment les utiliser et comment ne pas les utiliser

(Notez que cet article a été écrit après la sortie de Node.js 6.1.0)

#### **TL;DR**

* Considérez module.exports comme la variable qui est retournée par require(). C'est un objet vide par défaut, et il est possible de le changer en n'importe quoi.
* Exports ? Eh bien, « exports » lui-même n'est jamais retourné ! Ce n'est qu'une référence à module.exports ; une variable de commodité pour aider les auteurs de modules à écrire moins de code. Travailler avec ses propriétés est sûr et recommandé.

```
exports.method = function() {
}
```

```
vs.
```

```
module.exports.method = function() {
}
```

### Un exemple simple de module

Tout d'abord, nous avons besoin d'un exemple de code. Commençons par une calculatrice simple :

Usage :

### L'enveloppe de module

Node.js **enveloppe internement** tous les modules require()-ed dans une fonction d'enveloppe :

### L'objet module

La variable « **module** » est un objet représentant le module actuel. Il **est** **local à chaque module** et il est également privé (accessible uniquement depuis le code du module) :

### Module.exports

* **C'est la référence d'objet qui est retournée par les appels require().**
* Il est automatiquement créé par Node.js.
* Ce n'est qu'une référence à un objet JavaScript simple.
* Il est également vide par défaut (notre code y attache une méthode « add() »)

Il y a deux façons dont nous pouvons utiliser module.exports :

1. **Attacher des méthodes publiques** à celui-ci (comme nous l'avons fait dans l'exemple de la calculatrice).
2. **Le remplacer** par notre objet ou fonction personnalisé.

Pourquoi le remplacer ? En le remplaçant, nous pouvons retourner n'importe quelle instance arbitraire d'une autre classe. Voici un exemple écrit en ES2015 :

Ci-dessus, « calculator-base » exporte une classe. 
Étendons la classe « Calculator » et exportons une instance cette fois :

Usage :

### Alias Exports

* **« exports » est juste une variable de commodité pour que les auteurs de modules puissent écrire moins de code**
* Travailler avec ses propriétés est sûr et recommandé.   
(par ex. : exports.add = function
)
* **Exports** n'est PAS retourné par require() (module.exports l'est !)

Voici quelques bons et mauvais exemples :

**Note :** Il est courant de remplacer module.exports par des fonctions ou objets personnalisés. Si nous faisons cela mais que nous souhaitons continuer à utiliser le raccourci « exports » ; alors « exports » doit être redirigé vers notre nouvel objet personnalisé (également fait dans le code ci-dessus à la ligne 12) :

```
exports = module.exports = {}
```

```
exports.method = function() {...}
```

### Conclusion

Une variable nommée **exports** qui n'est pas entièrement exportée est déroutante, surtout pour les nouveaux venus dans Node.js. Même la documentation officielle a une prise légèrement étrange à ce sujet :

> En tant que directive, si la relation entre exports et module.exports semble magique pour vous, ignorez exports et n'utilisez que module.exports.

Mon avis est que le code n'est pas magique. Les développeurs devraient toujours chercher une compréhension plus approfondie des plateformes et des langages qu'ils utilisent. En faisant cela ; les programmeurs gagnent une confiance et des connaissances précieuses qui, à leur tour, impactent positivement la qualité du code, l'architecture du système et la productivité.

Merci d'avoir lu mon article. Les commentaires et les réflexions sont toujours les bienvenus dans la section des commentaires.

[lazlojuly](https://twitter.com/lazlojuly)

#### Articles connexes :

* [Les modules Node.js sont-ils des singletons ?](https://medium.com/@lazlojuly/are-node-js-modules-singletons-764ae97519af)

#### Sources :

* [Documentation Node.js sur les Modules](https://nodejs.org/api/modules.html)

**Découvrez ma nouvelle série de blogs sur les tests unitaires :**

[**Comment commencer avec les tests unitaires ? Partie #1**](https://medium.com/@lazlojuly/how-to-get-started-with-unit-testing-part-1-7f490bbf560a)  
[_Je suppose que beaucoup d'entre nous peuvent se reconnaître dans une situation décrite ci-dessus._](https://medium.com/@lazlojuly/how-to-get-started-with-unit-testing-part-1-7f490bbf560a)  
[_Un endroit où les tests unitaires sont considérés comme une corvée._medium.com](https://medium.com/@lazlojuly/how-to-get-started-with-unit-testing-part-1-7f490bbf560a)