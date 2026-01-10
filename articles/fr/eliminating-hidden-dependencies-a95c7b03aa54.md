---
title: Comment éliminer (ou gérer) les dépendances cachées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-05T08:44:39.000Z'
originalURL: https://freecodecamp.org/news/eliminating-hidden-dependencies-a95c7b03aa54
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9wHrewC1Dyf2Au_qEqwWcg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment éliminer (ou gérer) les dépendances cachées
seo_desc: 'By Shalvah

  In software, a dependency occurs when one module in an application, A, depends on
  another module or environment, B. A hidden dependency happens when A depends on
  B in a way that’s not obvious.

  To discover a hidden dependency, you usually h...'
---

Par Shalvah

En informatique, une dépendance se produit lorsqu'un module d'une application, _A_, dépend d'un autre module ou environnement, _B_. Une dépendance cachée se produit lorsque _A_ dépend de _B_ d'une manière qui n'est pas évidente.

Pour découvrir une dépendance cachée, vous devez généralement creuser dans le code source du module. Un module peut désigner n'importe quoi, d'un service entier à une classe ou une fonction, voire quelques lignes de code.

Voici un petit exemple de dépendance, comparant deux façons de l'exprimer :

```
let customer = Customer.find({id: 1});
```

```
// explicite — le client doit être passé au panier
function Cart(customer) { this.customer = customer;}
let cart = new Cart(customer);
```

```
// caché — le panier a toujours besoin d'un client,
// mais il ne le dit pas explicitement
function Cart() { this.customer = customer; // une variable globale `customer`}
let cart = new Cart();
```

Remarquez la différence subtile ? Les deux implémentations du constructeur Cart dépendent d'un objet customer. Mais la première exige que vous passiez cet objet, tandis que la seconde suppose qu'il existe déjà un objet customer disponible dans l'environnement.

Un développeur voyant `let cart = new Cart()` n'aurait aucun moyen de savoir que l'objet cart dépend d'une variable globale customer, sauf s'il regarde le constructeur Cart.

#### Dépendances cachées dans la nature

Je vais partager quelques exemples de dépendances cachées que j'ai rencontrées dans des bases de code réelles.

* **Fichiers `include` PHP**

Prenons une application backend PHP typique. Dans notre `index.php`, le point d'entrée de notre application, nous pourrions avoir quelque chose comme ceci :

```
include 'config.php';
include 'loader.php';
$app = new Application($config);
```

Le code semble suspect, n'est-ce pas ? D'où vient la variable `$config` ? Voyons voir.

La directive `include` est similaire aux balises HTML `<script>`. Elle indique à l'interpréteur de récupérer le contenu du fichier spécifié, de l'exécuter et, s'il a une instruction de retour, de passer la valeur de retour à l'appelant. C'est un moyen de diviser le code en plusieurs fichiers. Comme une balise `<script>`, include peut également placer des variables dans la portée globale.

Regardons les fichiers que nous incluons. Le fichier `config.php` contient les paramètres de configuration typiques pour une application backend :

```
$config = [
  'database' => [
    'host' => '127.0.0.1',
    'port' => '3306',
    'name' => 'home',
  ],
  'redis' => [
    'host' => '127.0.0.1',
  ]];
```

Le fichier `loader.php` est essentiellement un chargeur de classes fait maison. Voici une version simplifiée de son contenu :

```
$loader = new Loader(__DIR__);
$loader->configure($config);
```

Voyez-vous le problème ? Le code dans `loader.php` (et le reste du code dans `index.php`) dépend d'une variable nommée `$config`, mais il n'est pas évident où `$config` est définie jusqu'à ce que vous ouvriez `config.php`. Ce modèle de codage n'est en réalité pas rare.

* **Inclusion de fichiers JavaScript via des balises `<script>`**

Ceci est probablement un exemple plus courant. Comparez les deux extraits de code suivants (supposez que `cart-fx` et `cart-utils` sont des bibliothèques JS aléatoires) :

Exemple A :

```
<script src="//some-cdn/cart-fx.js"></script>
<script src="//some-cdn/cart-utils.js"></script>
```

```
/* beaucoup de code */
```

```
<script>var cart = new Cart(CartManager.default, new Customer());</script>
```

Exemple B :

```
import Cart from 'cart-fx';
import CartManager from 'cart-utils';
```

```
/* beaucoup de code */
```

```
const cart = new Cart(CartManager.default, new Customer());
```

Dans le second exemple, il est évident que les variables `Cart` et `CartManager` ont été importées des modules `cart-fx` et `cart-utils` respectivement. Dans le premier exemple, nous devons deviner quel module possède `Cart` et quel module possède `CartManager`. Et n'oubliez pas `Customer` non plus ! (N'oubliez pas que notre propre code est également un module.)

* **Lecture depuis l'environnement**

Je suis le coupable dans cet exemple. J'ai construit un package PHP il y a quelque temps pour interagir avec une API. Le package permettait de passer vos clés API au constructeur. Malheureusement, il permettait également de spécifier vos clés en tant que variables d'environnement, et le package les utilisait automatiquement. [Jetez un coup d'œil, et ne riez pas de moi](https://github.com/Hng-X/moneywave-php/blob/ef4d491c9a23f084d7a13e7279219213e8d4f87f/README.md#configuration).

Quand j'ai fait cela, je croyais que je facilitais la vie du développeur. En réalité, cependant, je faisais des suppositions sur l'environnement dans lequel le code était exécuté, et je liais la fonctionnalité du package à certaines conditions devant être remplies dans l'environnement.

#### Pourquoi les dépendances cachées sont-elles dangereuses ?

Je peux penser à deux raisons principales :

* **Il est facile de supprimer involontairement le module dépendant sans supprimer la dépendance**. Par exemple, prenez le cas de mon package ci-dessus. Imaginez un développeur configurant une application qui utilise le package dans un nouvel environnement. En décidant quelles variables d'environnement transférer de l'ancien environnement, le développeur pourrait négliger d'ajouter celles nécessaires au package, _parce qu'il ne peut pas les trouver utilisées quelque part dans la base de code_.
* **Un petit changement dans le code dépendant pourrait casser toute l'application, ou la rendre boguée**. Prenez le cas de notre fichier `index.php` ci-dessus — échanger les deux premières lignes pourrait sembler un changement inoffensif, mais cela casserait l'application, car la ligne 2 dépend d'une variable définie dans la ligne 1. Un cas encore plus sérieux serait quelque chose comme ceci :

```
$config = [];
include 'bootstrap.php';
$app = new Application($config);
```

Supposons que notre fichier `bootstrap.php` apporte des modifications importantes à `$config`. Si, pour une raison quelconque, la deuxième ligne est déplacée en bas, l'application s'exécuterait sans lancer d'erreurs, mais les modifications de configuration cruciales que `bootstrap.php` apporte seraient invisibles pour l'application.

#### Se débarrasser des dépendances cachées

Comme beaucoup de choses en ingénierie logicielle, il n'y a pas de règles strictes pour traiter les dépendances cachées, mais j'ai trouvé quelques principes de base qui fonctionnent pour moi :

1. _Écrivez du code qui est vraiment modulaire_, pas seulement divisé en plusieurs fichiers. Un module idéal vise à être autonome et à avoir une dépendance minimale à l'état global partagé. Un module doit également déclarer explicitement ses dépendances.
2. _Réduisez le nombre de suppositions qu'un module doit faire_ sur son environnement ou d'autres modules.
3. _Exposez une interface claire._ Idéalement, au-delà des signatures de fonctions/classes, un utilisateur de votre module ne devrait pas avoir à regarder le code source pour comprendre quelles sont les dépendances du module.
4. _Évitez d'encombrer l'environnement._ Résistez à la tentation d'ajouter des variables à la portée parente. Chaque fois que possible, préférez retourner ou exporter explicitement des variables à l'appelant.

Je vais démontrer comment nous pourrions refactoriser le premier exemple ci-dessus en utilisant ces principes. La première chose à faire est de faire en sorte que le fichier de configuration **retourne** le tableau de configuration, afin que l'appelant puisse explicitement le sauvegarder dans une variable :

```
// config.php
return [
  'database' => [
    'host' => '127.0.0.1',
    'port' => '3306',
    'name' => 'home',
  ],
  'redis' => [
    'host' => '127.0.0.1',
  ]];
```

La prochaine chose que nous pouvons faire est de changer le fichier de chargement pour qu'il retourne une fonction. Cette fonction prendra un paramètre de configuration. De cette manière, nous rendons clair que le processus de chargement des fichiers dépend d'une configuration prédéfinie.

```
// loader.php
```

```
return function (array $config){
  $loader = new Loader(__DIR__);
  $loader->configure($config);}
```

En mettant tout cela ensemble, notre fichier `index.php` ressemble à ceci :

```
$config = include 'config.php';
(include 'loader.php')($config);
```

```
$app = new Application($config);
```

Nous pouvons même aller un peu plus loin en sauvegardant la fonction retournée dans une variable avant de l'appeler :

```
$config = include 'config.php';
```

```
$loadClasses = include 'loader.php';
$loadClasses($config);
```

```
$app = new Application($config);
```

Maintenant, toute personne regardant `index.php` peut voir d'un coup d'œil que :

1. Le fichier `config.php` retourne **quelque chose** (nous pouvons deviner qu'il s'agit d'une sorte de configuration, mais ce n'est pas important maintenant).
2. Le fichier de chargement et l'`Application` dépendent de ce **quelque chose** pour faire leur travail.

Beaucoup mieux, n'est-ce pas ?

Attaquons-nous à notre deuxième exemple. Nous pourrions refactoriser cela de plusieurs manières : passer à `import`/`require` pour les navigateurs supportés, ou utiliser des outils de build qui fourniraient des polyfills pour cela. Mais il y a un petit changement que nous pourrions faire pour améliorer quelque peu les choses :

```
<script src="//some-cdn/cart-fx.js"></script>
<script src="//some-cdn/cart-utils.js"></script>
```

```
/* beaucoup de code */
```

```
<script>var cart = new CartFx.Cart(CartUtils.CartManager.default, new Customer());</script>
```

En attachant les objets `CartManager` et `Cart` aux objets globaux `CartFx` et `CartUtils`, nous les avons effectivement déplacés dans des espaces de noms. Nous ferions de même pour toute autre variable que ces bibliothèques souhaitent rendre disponible, réduisant le nombre de dépendances potentiellement cachées à une seule par module.

#### Parfois, vous ne pouvez tout simplement pas l'éviter

Il arrive que vous soyez limité par les outils disponibles, les ressources limitées, etc. Il est important, cependant, de garder à l'esprit que ce qui semble si évident pour vous, l'auteur du code, peut ne pas l'être pour un nouveau venu. Cherchez de petites optimisations que vous pouvez faire pour améliorer cela.

Avez-vous des expériences avec les dépendances cachées ou des techniques pour les gérer ? N'hésitez pas à les partager dans les commentaires.