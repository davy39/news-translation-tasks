---
title: L'héritage prototypal de JavaScript expliqué à l'aide de CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-22T17:54:01.000Z'
originalURL: https://freecodecamp.org/news/understanding-prototypal-inheritance-in-javascript-with-css-93b2fcda75e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cR8HEE-toHzj9rXVXbJ_ng.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: L'héritage prototypal de JavaScript expliqué à l'aide de CSS
seo_desc: 'By Nash Vail

  Prototypal inheritance is arguably the least understood aspect of JavaScript. Well
  the good news is that if you understand how CSS works, you can also understand how
  JavaScript prototypes work.

  It’s beautiful when something simple is abl...'
---

Par Nash Vail

L'héritage prototypal est probablement l'aspect le moins compris de JavaScript. La bonne nouvelle, c'est que si vous comprenez comment fonctionne CSS, vous pouvez aussi comprendre comment fonctionnent les prototypes JavaScript.

C'est magnifique quand quelque chose de simple peut expliquer quelque chose de apparemment complexe, une analogie — comme un pilon enfonce un poteau profondément dans le sol, une analogie fait passer le message.

Je suis un amateur d'analogies, un analogophile.

C'est parti.

### Prototypes dans les boutons CSS

![Image](https://cdn-media-1.freecodecamp.org/images/ut3NNLvJqxWAYWUXXGc-KDX7gbjPaHMWIuer)

Vous voyez les deux boutons ci-dessus ? Nous allons les concevoir en CSS.

Commençons par écrire rapidement les styles pour ces deux boutons, en commençant par `.btn`

```
.btn { min-width: 135px; min-height: 45px; font-family: 'Avenir Next', sans-serif; font-size: 18px; font-weight: bold; letter-spacing: 1.3px; color: #4D815B; background-color: #FFF; border: 2px solid #4D815B; border-radius: 4px;  padding: 5px 20px; cursor: pointer;}
```

C'est un bloc de code CSS raisonnablement simple.

Passons maintenant aux styles pour `.btn-solid`

```
.btn-solid { min-width: 135px; min-height: 45px; font-family: 'Avenir Next', sans-serif; font-size: 18px; font-weight: bold; letter-spacing: 1.3px; color: #FFF; background-color: #4D815B; border: 2px solid #4D815B; border-radius: 4px;  padding: 5px 20px; cursor: pointer;}
```

Comme vous l'avez peut-être déjà remarqué, à part les éléments en gras, tous les autres styles dans `.btn-solid` sont identiques à ceux de `.btn`. Et si vous êtes familier avec [Sass](http://www.sass-lang.com/documentation/file.SASS_REFERENCE.html#extend), vous savez peut-être que les styles `.btn-solid` peuvent être réécrits en SASS comme suit :

```
.btn-solid { @extend .btn; color: #FFF; background-color: #4D815B;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/9GUw4npoqLuoLkW-aVY48eGsTpymMl6QjViz)
_.btn-solid est une version spécialisée de .btn_

Comme vous pouvez le voir, `.btn-solid` hérite des styles de `.btn`, puis en remplace certains (couleur de police et couleur de fond) pour se créer. Ce qui nous amène à la conclusion que `.btn-solid` est une version spécialisée de `.btn`. Ou, en d'autres termes, `.btn-solid` est `.btn` mais avec des couleurs de police et de fond différentes. Cela a du sens, n'est-ce pas ? Mais attendez, il y a plus.

Disons que nous voulons créer un bouton plus grand, `.btn-lg`. Nous utiliserons `.btn` comme **prototype** pour fournir les styles de base. Ensuite, de manière similaire à la façon dont nous avons modifié les couleurs de fond et de police pour créer `.btn-solid`, nous modifierons la propriété font-size à une valeur plus grande pour créer un bouton plus grand.

![Image](https://cdn-media-1.freecodecamp.org/images/LN7q4YbKvJBpPhDDsHHPWd7w9g-inio4nO3g)

`.btn-lg` et `.btn-solid` sont tous deux des versions spécialisées de `.btn`. `.btn` fournit des styles de base à `.btn-lg` et `.btn-solid` qui remplacent ensuite certains des styles de base pour se créer. Cela nous indique qu'un seul bouton que nous décidons — `.btn` dans notre cas — peut être utilisé comme fournisseur de styles de base pour plusieurs éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/zcuH3R125TKlm52wePiTLt7Wnzi8b4HHRxlX)

Dans cette section, nous avons essayé de définir le concept de **prototypes** pour les boutons CSS. Un prototype est une entité qui fournit des styles de base, qui peuvent être étendus pour créer différentes instances de boutons. Cette définition d'un prototype est très proche de ce que les prototypes signifient réellement en termes de programmation.

En termes de programmation, un prototype est un objet qui fournit un comportement de base à un second objet. Le second objet étend ensuite ce comportement de base pour former sa propre spécialisation. Voyons dans la section suivante comment notre connaissance des prototypes dans les boutons CSS se mappe à JavaScript.

### Prototypes en JavaScript

Considérons l'objet JavaScript suivant :

```
let obj = { a: 1};
```

Nous savons que la valeur de `a` peut être accédée par `obj.a`, étant donné que `a` est clairement une propriété de `obj`. Mais il y a plus, vous pouvez aussi appeler `obj.hasOwnProperty('a')` pour vérifier si `obj` a réellement une propriété nommée `a`.

Maintenant, attendez une seconde — d'après ce que nous pouvons voir, `obj` n'a pas de propriété appelée `hasOwnProperty` définie sur lui. D'où vient `hasOwnProperty` ? Pour répondre à cette question, nous devrons revenir aux boutons que nous venons de finir de créer.

`.btn-solid` n'a que les couleurs de fond et de police définies sur lui. D'où vient, par exemple, `border-radius` ? Nous savons que `.btn-solid` est une spécialisation de `.btn`, donc nous pouvons voir que `.btn-solid` obtient des styles comme `border-radius`, `width`, `height`, et `padding` de `.btn`. Pourrait-il en être de même avec `obj` ?

Tout comme `.btn-solid` et `.btn-lg` obtiennent leurs styles de base de `.btn`, `obj` ou tout autre objet JavaScript, d'ailleurs, reçoivent leur comportement de base d'**un autre objet** — `Object.prototype`. Et ce `Object.prototype` a `hasOwnProperty` défini sur lui. Et par conséquent, cela donne à `obj` l'accès à la méthode `hasOwnProperty` — tout comme `.btn-solid` avait accès à la propriété `border-radius` de `.btn`.

![Image](https://cdn-media-1.freecodecamp.org/images/P3Ie8UsHNht4QjK97BNe4jqZx2FYKeE7NTFe)
_obj est une spécialisation de Object.Prototype_

Ceci — **un objet** (obj) **héritant de ses propriétés et de son comportement de base d'un autre objet** (Object.prototype) — est ce que nous appelons l'héritage prototypal. Remarquez qu'il n'y a pas de `class` impliquée dans l'interaction.

Les mécanismes internes réels des prototypes JavaScript et de nos "prototypes" CSS sont très différents. Mais pour les besoins de notre analogie, nous pouvons ignorer comment ils fonctionnent en coulisses.

`Object.prototype` n'est pas le seul prototype disponible en JavaScript. Il y a `Array.prototype`, `Function.prototype`, `Number.prototype` et plusieurs autres. Le travail de tous ces prototypes est de fournir un comportement de base ou des méthodes utilitaires à leurs instances.

Par exemple, chaque tableau déclaré en JavaScript a accès à `.push`, `.sort`, `.forEach`, et `.map` uniquement grâce au lien prototypal. Et pour la même raison, chaque fonction a accès à `.call`, `.apply`, `.bind`.

Les prototypes et l'héritage prototypal ne sont pas spécifiques à JavaScript. Ce sont des constructions que JavaScript utilise en interne et qui nous permettent de les utiliser dans nos propres programmes. Avant de voir comment nous pouvons exactement faire cela, nous devons comprendre ce qu'est le chaînage prototypal.

### Chaînage prototypal

Nous devons revenir à l'analogie des boutons une fois de plus. Disons que je veux créer un grand bouton solide, `.btn-solid-lg` :

![Image](https://cdn-media-1.freecodecamp.org/images/IM65byinDcFRJk-K8r-zaHO9VbpVOjxZprXl)

Les styles de base pour `.btn-solid-lg` sont fournis par `.btn-solid`, et `.btn-solid-lg` remplace la propriété font-size pour se créer.

Regardez de plus près cependant. `.btn-solid` n'a que deux styles définis sur lui : background-color et color (police). Cela signifie que `.btn-solid-lg` n'a que 3 styles pour lui-même : background-color, color, et font-size. D'où viennent `width`, `height`, `border-radius` ?

Ok, voici un indice :

![Image](https://cdn-media-1.freecodecamp.org/images/J4aUh9PEkAdZkUabjB93c5Y0eaLbMcwTLzy3)
_Un indice indéchiffrable._

Si vous vouliez créer un bouton extra large `.btn-solid-xlg`, vous pourriez le faire avec `.btn-solid-lg` comme prototype. Mais comment tout cela se mappe-t-il à JavaScript ?

En JavaScript, vous êtes autorisé à créer des chaînes de prototypes aussi. Une fois que vous comprenez cela, vous débloquez tout un ensemble d'outils pour écrire du code incroyablement puissant. Oui, _incroyablement puissant_.

Voyons comment les chaînes de prototypes fonctionnent en JavaScript.

Vous vous souvenez de l'objet que nous avons créé dans la section précédente ? Celui que nous avons soigneusement nommé `obj` ? Saviez-vous que vous pouvez créer autant d'objets que vous voulez avec `obj` comme prototype ?

`[Object.create](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Object/create)` vous permet de créer un nouvel objet à partir d'un objet prototype spécifié. Cela signifie que vous pouvez créer un autre objet, `obj2`, qui a `obj` comme premier prototype :

```
let obj2 = Object.create(obj);
```

```
// Ajouter une propriété 'b' à obj2
obj2.b = 2;
```

Si vous avez suivi jusqu'à présent, vous devriez réaliser que même si `obj2` n'a pas de propriété `a` définie sur lui, faire `console.log(obj2.a)` ne résultera pas en une erreur, mais plutôt `1` sera enregistré dans la console. Un peu comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/DxNlRL9qpdY-hNZXK9PUlRgwfxe0G8fdeYpw)

Lorsque `obj2` cherche `a`, il recherche d'abord dans ses propres propriétés. S'il ne peut pas trouver la propriété correspondante, il demande à son prototype (obj), où il trouve finalement `a`. Si tel était le cas qu'il ne pouvait toujours pas trouver `a`, la recherche se poursuivrait le long de la chaîne de prototypes jusqu'à ce qu'elle atteigne le dernier maillon, `Object.prototype`.

D'un autre côté, si `a` était défini sur `obj2`, il remplacerait tous les autres `a` s'ils étaient définis sur l'un de ses prototypes. Similaire à la façon dont `.btn-solid` a remplacé les propriétés `color` et `background-color` de `.btn`. Cela s'appelle **l'ombrage de propriété**.

Mais qu'en est-il de la longueur de la chaîne de prototypes ? Y a-t-il une limite ?

Il n'y a pas de limite à la longueur de la chaîne de prototypes. Il n'y a pas non plus de limites sur le branchement. Cela signifie que vous pouvez créer plusieurs instances avec `Object.prototype`, `obj`, ou `obj2` comme prototype.

![Image](https://cdn-media-1.freecodecamp.org/images/m2PjrvRpNTiz8WFb9LxjwWTeHw9SvgOKBSGS)
_Vous pouvez vous brancher à chaque objet autant de fois que vous en avez besoin._

Alors, comment cette nouvelle connaissance des prototypes et du chaînage prototypal va-t-elle vous aider à écrire un meilleur code ?

### Écrire un meilleur code avec les prototypes

Le but de cet article était de vous expliquer ce que sont les prototypes et comment fonctionne l'héritage prototypal. J'espère avoir réussi.

Pour cette dernière section, je vais me permettre de faire un petit discours. J'espère que vous ne m'en tiendrez pas rigueur.

Si vous regardez le code JavaScript disponible en ligne — que ce soit dans des projets open source sur Github ou dans des pens sur Codepen — vous constaterez qu'une majorité d'entre eux utilisent le modèle de constructeur pour créer des objets.

```
function Circle(radius) {  this.radius = radius;}
```

```
Circle.prototype.area = function() {  return Math.PI * this.radius * this.radius;}
```

```
// Modèle de constructeur pour créer de nouveaux objets
let circ = new Circle(5);
```

Le modèle de constructeur ressemble à des classes. Dans les premiers jours, lorsque JavaScript était beaucoup moins populaire qu'aujourd'hui, le mot-clé `new` a été ajouté comme stratégie marketing.

Cette indirection était destinée à faire paraître JavaScript plus familier aux programmeurs formés de manière classique. Bien qu'il soit discutable de savoir dans quelle mesure cela a réussi, cela a également obscurci involontairement la véritable nature prototypale du langage.

La réalité est que bien que les constructeurs ressemblent à des classes, ils ne se comportent pas du tout comme des classes. En JavaScript, il y a des objets, et des objets qui étendent d'autres objets. Les constructeurs et les classes n'entrent jamais en jeu. Le modèle de constructeur complique inutilement les choses, il se passe beaucoup de choses [en coulisses](https://medium.com/@nashvail/lets-settle-this-part-two-2d68e6cb7dba#.ba3x9f34o).

Je vous implore — maintenant que vous avez une solide compréhension des prototypes — d'arrêter d'utiliser le modèle de constructeur.

Pourquoi ne pas faire ceci à la place ?

```
let Circle = {  create(radius) {    // Création de lien prototypal en utilisant Object.create    let obj = Object.create(this);    obj.radius = radius;    return obj;  },  area() {    return Math.PI * this.radius * this.radius;  }};
```

```
let circ = Circle.create(5);
```

J'espère que cette analogie vous a aidé à mieux comprendre les prototypes, le chaînage prototypal et l'héritage prototypal avec `Object.create`. Maintenant, vous pouvez écrire un meilleur code et arrêter d'utiliser des classes prétentieuses.

Merci d'avoir lu ! Si mon article vous a été utile, cliquez sur le petit cœur vert ci-dessous pour le recommander, et partagez-le avec vos collègues développeurs.

Et pour aller plus loin, consultez l'article de Aadit Shah [Why Prototypal Inheritance Matters](http://aaditmshah.github.io/why-prototypal-inheritance-matters/).

#### Vous en voulez plus ? Je publie régulièrement sur mon [blog à l'adresse nashvail.me](https://nashvail.me). À bientôt, et bonne journée !

![Image](https://cdn-media-1.freecodecamp.org/images/Thg5-ro0URqXRYm8OPjFqMTaCB7sPqfSr4RO)