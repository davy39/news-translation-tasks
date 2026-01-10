---
title: 'Désorienté par une boucle : comprendre les boucles for et les timeouts en
  JavaScript'
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2018-04-02T11:28:02.000Z'
originalURL: https://freecodecamp.org/news/thrown-for-a-loop-understanding-for-loops-and-timeouts-in-javascript-558d8255d8a4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4x8Zuht2TaQ87ZhwYcLUqQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Désorienté par une boucle : comprendre les boucles for et les timeouts
  en JavaScript'
seo_desc: Often, JavaScript just works. And because it is written in human-readable
  syntax, certain things seem intuitive. But it’s easy to ignore what’s happening
  on a deeper level. Eventually, though, this lack of understanding results in an
  inability to sol...
---

Souvent, JavaScript fonctionne simplement. Et parce qu'il est écrit avec une syntaxe lisible par les humains, certaines choses *semblent* intuitives. Mais il est facile d'ignorer ce qui se passe à un niveau plus profond. Finalement, cependant, ce manque de compréhension entraîne une incapacité à résoudre un problème.

> L'intuition est la capacité à comprendre quelque chose immédiatement, sans avoir besoin de raisonnement conscient. — Google

Je passe une bonne partie de mon temps à essayer de résoudre des problèmes bidimensionnels, et une partie légèrement plus grande à essayer de résoudre des problèmes tridimensionnels.

Bien que j'aime pratiquer la programmation pendant mon temps libre, je suis contrôleur aérien pendant la journée. Les problèmes auxquels nous sommes confrontés en tant que contrôleurs aériens ne sont pas différents de ceux de tout autre travail. Il y a des problèmes routiniers avec des solutions routinières et des problèmes uniques avec des solutions uniques. C'est grâce à une compréhension plus profonde que nous pouvons résoudre les problèmes uniques.

De l'extérieur, en regardant le contrôle aérien, il peut sembler que tout est un problème unique – qu'il y a une compétence requise inhérente pour faire le travail. Cependant, bien que certaines aptitudes peuvent faciliter l'apprentissage de toute compétence, c'est finalement l'expérience qui conduit la résolution de problèmes à un niveau subconscient. Le résultat est l'intuition.

L'intuition suit l'observation. Observez un problème unique suffisamment de fois, et il et sa solution deviennent routiniers. C'est en remarquant les consistances à travers chaque situation que nous commençons à développer un sens de ce qui *devrait* se passer ensuite.

L'intuition ne *nécessite* pas, cependant, une compréhension profonde. Nous pouvons souvent pointer vers la solution correcte, sans être capables d'articuler comment ou pourquoi elle fonctionne. Parfois, cependant, nous choisissons des solutions qui *semblent* intuitives mais sont en fait gouvernées par un ensemble de règles peu familier.

### **Que produit ce code ?**

```js
for(var i = 1; i < 6; i++) {
  setTimeout(function() {
     console.log(i);
  },1000);
}
console.log('La boucle est terminée !');
```

Prenez un peu de temps pour réfléchir à ce que ce code va produire. Nous allons commencer à construire les bases pour répondre à cela, et nous y reviendrons plus tard.

#### JavaScript est un dialecte de langage.

J'ai grandi dans le nord-est des États-Unis. Bien que je parle anglais, ma parole contient indéniablement une variété régionale. Cette variété est appelée *dialecte*. Mon dialecte particulier est une *implémentation* (ou version) de la norme de la langue anglaise.

Il peut sembler que les normes donnent naissance aux dialectes, mais c'est le dialecte qui initialement pousse le besoin de normes. JavaScript est similaire. JavaScript est le dialecte, pas la norme. La norme est *ECMAScript*, créée par ECMA – l'Association européenne des fabricants d'ordinateurs. ECMAScript est une tentative de standardiser JavaScript.

Il existe plus d'une implémentation de ECMAScript, mais JavaScript se trouve être la plus populaire, et donc, les noms JavaScript et ECMAScript sont souvent utilisés de manière interchangeable.

### JavaScript s'exécute dans un moteur.

JavaScript n'est qu'un fichier texte. Comme un conducteur sans voiture, il ne peut pas aller très loin. Quelque chose doit exécuter ou interpréter votre fichier. Cela est fait par un moteur JavaScript.

Quelques exemples de moteurs JavaScript incluent V8, le moteur utilisé par Google Chrome ; SpiderMonkey, le moteur utilisé par Mozilla Firefox ; et JavaScriptCore, le moteur utilisé par Apple Safari. ECMAScript, la norme de langage, assure la cohérence entre les différents moteurs JavaScript.

### Les moteurs JavaScript s'exécutent dans un environnement.

Bien que JavaScript puisse s'exécuter dans différents *endroits* (par exemple, Node.js, une technologie côté serveur populaire, exécute JavaScript et utilise le même moteur V8 que Google Chrome), l'endroit le plus courant pour trouver un moteur JavaScript est un navigateur web.

Dans le navigateur, le moteur JavaScript n'est qu'une partie d'un environnement plus large qui aide à donner vie à notre code. Il y a trois parties principales à cet environnement, et ensemble elles constituent ce que l'on appelle l'*environnement d'exécution*.

#### La pile d'appels

La première partie est l'emplacement du code actuellement en cours d'exécution. Cela s'appelle la *pile d'appels*. Il n'y a qu'une seule pile d'appels en JavaScript, et cela deviendra important alors que nous continuons à construire notre fondation.

Voici un exemple simplifié de la pile d'appels :

```js
function doSomething() {
   //some other code
   doSomethingElse();
   //some other code
}

function doSomethingElse() {
 //some other code
}

doSomething();
```

La pile d'appels initiale est vide, car il n'y a pas de code en cours d'exécution. Lorsque notre moteur JavaScript atteint enfin la première invocation de fonction, `doSomething()`, elle est ajoutée à la pile :

```python
--Pile d'appels--

doSomething;
```

À l'intérieur de `doSomething()` nous exécutons un autre code puis atteignons `doSomethingElse()` :

```python
--Pile d'appels--

doSomething
doSomethingElse
```

Lorsque `doSomethingElse()` a fini de s'exécuter, elle est retirée de la pile d'appels :

```python
--Pile d'appels--

doSomething
```

Enfin, `doSomething()` termine le code restant, et est également retirée de la pile d'appels :

```python
--Pile d'appels--

Vide
```

#### Les API Web

La deuxième partie de notre environnement de navigateur comble quelque peu un vide. Étonnamment, des choses telles que l'interaction avec le DOM, la réalisation de requêtes serveur, et la plupart des tâches basées sur le navigateur ne font *pas* partie de la norme du langage ECMAScript.

Heureusement, les navigateurs nous offrent des fonctionnalités supplémentaires que notre moteur JavaScript peut utiliser. Ces fonctionnalités étendent la fonctionnalité de JavaScript dans le navigateur. Elles nous permettent de faire des choses comme écouter des événements ou faire des requêtes serveur — des choses que JavaScript ne peut pas faire par lui-même. Et elles sont appelées des *API Web*.

De nombreuses API Web nous permettent d'écouter ou d'attendre qu'un événement se produise. Lorsque cet événement se produit, nous exécutons ensuite un autre code.

Voici notre exemple de pile d'appels étendu pour inclure une (fausse) API Web.

```js
function doSomething() {
   //some other code
   listenForClick();
   doSomethingElse();
   //some other code
}

function doSomethingElse() {
 //some other code
}

listenForClick() {
   console.log('le bouton a été cliqué !')
}

doSomething();
```

Lorsque le navigateur rencontre `doSomething()` il est placé dans la pile d'appels :

```python
--Pile d'appels--

doSomething
```

Ensuite, il exécute un autre code et rencontre `listenForClick(...)` :

```python
--Pile d'appels--

doSomething
listenForClick
```

`listenForClick()` est branché à une API Web, et dans ce cas, il est retiré de notre pile d'appels.

Le moteur JavaScript passe maintenant à `doSomethingElse()` :

```python
--Pile d'appels--

doSomething
doSomethingElse
```

`doSomethingElse()` et `doSomething()` se terminent, et la pile d'appels est vide. Mais qu'est-il arrivé à `listenForClick()` ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*kVWy6v8bht__LNFEsgn3oA.png align="left")

#### File d'événements

C'est ici que nous introduisons la dernière partie de notre environnement de navigateur. Souvent, notre code d'API Web est une fonction qui prend un rappel. Un rappel est simplement un code que nous voulons exécuter après qu'une autre fonction s'est exécutée. Par exemple, écouter un événement de clic puis `console.log` quelque chose. Afin de s'assurer que notre `console.log` n'interfère pas avec un code actuellement en cours d'exécution, il passe d'abord par quelque chose appelé une *file d'événements*.

La file d'événements agit comme une zone d'attente jusqu'à ce que notre pile d'appels soit vide. Une fois la pile d'appels vide, la file d'événements peut passer notre code dans la pile d'appels pour qu'il soit exécuté. Continuons à construire sur notre exemple précédent :

```js
function doSomething() {
   //some other code
   listenForClick();
   doSomethingElse();
   //some other code
}

function doSomethingElse() {
 //some other code
}

listenForClick() {
   console.log('the button was clicked!')
}

doSomething();
```

Donc maintenant, notre code s'exécute comme ceci :

Notre moteur rencontre `doSomething()` :

```python
--Pile d'appels--

doSomething
```

`doSomething()` exécute un code puis rencontre `listenForClick(...)`. Dans notre exemple, cela prend un rappel, qui est le code que nous voulons exécuter après que l'utilisateur a cliqué sur un bouton. Le moteur passe `listenForClick(...)` hors de la pile d'appels et continue jusqu'à ce qu'il rencontre `doSomethingElse()` :

```python
--Pile d'appels--

doSomething
doSomethingElse
```

`doSomethingElse()` exécute un code, et se termine. À ce moment-là, notre utilisateur clique sur le bouton. L'API Web *entend* le clic et envoie l'instruction `console.log()` à la file d'événements. Nous allons prétendre que `doSomething()` n'est pas terminé ; par conséquent, la pile d'appels n'est pas vide, et l'instruction `console.log()` doit attendre dans la file d'événements.

```python
--Pile d'appels--

doSomething
```

Après quelques secondes, `doSomething()` se termine et est retiré de la pile d'appels :

```python
--Pile d'appels--

VIDE
```

Enfin, l'instruction `console.log()` peut être passée dans la pile d'appels pour être exécutée :

```python
--Pile d'appels--

console.log('The user clicked the button!')
```

*Gardez à l'esprit, notre code s'exécute incroyablement vite — prenant des millisecondes à un chiffre pour finir. Il n'est pas réaliste que nous puissions démarrer notre code, et que notre utilisateur puisse cliquer sur un bouton avant que le code ait fini de s'exécuter. Mais dans notre exemple simplifié, nous prétons que c'est vrai, pour mettre en évidence certains concepts.*

Ensemble, les trois parties (la pile d'appels, les API Web, et la file d'événements) forment ce que l'on appelle le modèle de concurrency, avec la *boucle d'événements* gérant le code qui passe de la file d'événements à la pile d'appels.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OxIQrHT8KLT_Yn3yPL6r_A.png align="left")

### Points à retenir des exemples ci-dessus :

#### JavaScript ne peut faire qu'une chose à la fois.

Il y a une idée fausse selon laquelle les gens peuvent faire plusieurs tâches à la fois. Ce n'est pas vrai. Les gens peuvent, cependant, passer d'une tâche à l'autre, un processus appelé *changement de tâche*.

JavaScript est similaire en ce sens qu'il ne peut pas faire plusieurs tâches à la fois. Parce que JavaScript n'a qu'une seule pile d'appels, le moteur JavaScript ne peut faire qu'une tâche à la fois. Nous disons que cela rend JavaScript *monothread*. Contrairement aux gens, cependant, JavaScript ne peut pas changer de tâche sans l'aide de nos API Web.

#### JavaScript doit terminer une tâche avant de passer à la suivante.

Parce que JavaScript ne peut pas passer d'une tâche à l'autre, si vous avez un code qui prend un certain temps à s'exécuter, il bloquera la ligne de code suivante. Cela s'appelle du *code bloquant*, et cela se produit parce que JavaScript est *synchrone*. Synchrone signifie simplement que JavaScript doit terminer une tâche avant de pouvoir en commencer une autre.

Un exemple de code bloquant pourrait être une requête serveur qui nous oblige à attendre que des données soient retournées. Heureusement, les API Web fournies par le navigateur nous donnent un moyen de contourner cela (avec l'utilisation de rappels).

En déplaçant le code bloquant de la pile d'appels vers la boucle d'événements, notre moteur peut passer à l'élément suivant dans la pile d'appels. Par conséquent, avec du code s'exécutant dans notre pile d'appels, et du code qui s'exécute simultanément dans une API Web, nous avons un comportement _asynchrone_.

Toutes les API Web, cependant, ne vont pas dans la boucle d'événements. Par exemple, `console.log` est une API Web, mais comme elle n'a pas de rappel et n'a pas besoin d'attendre quoi que ce soit, elle peut être exécutée immédiatement.

Gardez à l'esprit que monothread n'est pas la même chose que synchrone. Monothread signifie « une chose à la fois ». Synchrone signifie « finir avant de passer à la suivante ». Sans l'aide des API asynchrones, le cœur de JavaScript est à la fois monothread et synchrone.

### **Le scoop sur la portée**

Avant de revenir à notre question initiale, nous devons aborder la portée. La portée est le terme utilisé pour décrire quelles parties de notre code ont accès à quelles variables.

Intuitivement, il peut sembler qu'une variable déclarée et initialisée par une boucle `for` ne serait disponible qu'à l'intérieur de cette boucle `for`. En d'autres termes, si vous essayez d'y accéder en dehors de la boucle, vous obtiendrez une erreur.

Ce n'est pas le cas. Déclarer une variable avec le mot-clé `var` crée une variable qui est également disponible dans sa portée parente.

Cet exemple montre qu'une variable déclarée par `var` à l'intérieur d'une boucle `for` est également disponible dans la portée parente (dans ce cas, la portée globale).

```js
for(var a = 1; a < 10; a++) {} // déclaré "à l'intérieur" de la boucle
console.log(a); // affiche "10" et est appelé "en dehors de la boucle"
```

### **La réponse révélée**

À ce stade, nous avons discuté suffisamment pour construire notre réponse.

Voici notre exemple revisité :

```js
for(var i = 1; i < 6; i++) {
  setTimeout(function() {
     console.log(i);
  },1000);
}
console.log('La boucle est terminée !');
```

Intuitivement, vous pourriez croire que cela imprimera les nombres de un à cinq, avec une seconde entre chaque nombre imprimé :

```python
// une seconde entre chaque log

1
2
3
4
5
La boucle est terminée !
```

Cependant, ce que nous obtenons réellement est :

```python
La boucle est terminée !

// puis environ une seconde plus tard et tout à la fois

6
6
6
6
6
```

#### **Que se passe-t-il ?**

Rappelons notre discussion sur les API Web. Les API Web asynchrones, ou celles avec des rappels, passent par la boucle d'événements. `setTimeout()` se trouve être une API Web asynchrone.

Chaque fois que nous bouclons, `setTimeout()` est passé en dehors de la pile d'appels et entre dans la boucle d'événements. À cause de cela, le moteur est capable de passer à la partie suivante du code. La partie suivante du code se trouve être les itérations restantes de la boucle, suivies de `console.log('La boucle est terminée !')`.

Pour montrer que les instructions `setTimeout()` sont passées de la pile d'appels, et que la boucle est en cours d'exécution, nous pouvons placer une instruction `console.log()` en dehors de la fonction `setTimeout()` et imprimer les résultats. Nous pouvons également placer une méthode de minuterie intégrée pour montrer à quelle vitesse tout se passe. Nous utilisons `console.time()` et `console.timeEnd()` pour cela.

```js
console.time('myTimer');
for(var i = 1; i < 6; i++) {
   console.log('Loop Number' + i); // ajouté ceci
   setTimeout(()=>{
      console.log(i);
   },1000);
}
console.log('La boucle est terminée !');
console.timeEnd('myTimer');
```

Résultats :

```python
Loop Number 1
Loop Number 2
Loop Number 3
Loop Number 4
Loop Number 5
La boucle est terminée !

// puis, environ une seconde plus tard et tout à la fois :

6
6
6
6
6
myTimer: 1.91577ms   // Wow, c'est rapide !
```

Tout d'abord, nous pouvons voir que la boucle est en fait en cours d'exécution. De plus, le minuteur que nous avons ajouté nous dit que tout sauf nos fonctions `setTimeout()` a pris moins de deux millisecondes à s'exécuter ! Cela signifie que chaque fonction `setTimeout()` a environ 998 millisecondes restantes avant que le code qu'elle contient ne passe dans la file d'événements et enfin dans la pile d'appels. Souvenez-vous plus tôt quand j'ai dit qu'il serait difficile pour un utilisateur d'être plus rapide que notre code !

Si vous exécutez ce code plusieurs fois, vous remarquerez probablement que la sortie du minuteur changera légèrement. Cela est dû au fait que les ressources disponibles de votre ordinateur changent constamment et qu'il peut être légèrement plus rapide ou plus lent chaque fois.

Voici donc ce qui se passe :

1. Notre moteur rencontre notre boucle for. Nous déclarons et initialisons une variable globale nommée `i` égale à un.

2. Chaque itération de la boucle passe `setTimeout()` à une API Web et dans la boucle d'événements. Par conséquent, notre boucle `for` se termine très rapidement, puisque il n'y a pas d'autre code à l'intérieur à exécuter. En fait, la seule chose que fait notre boucle est de changer la valeur de `i` à six.

3. À ce stade, la boucle est terminée, nos fonctions `setTimeout()` comptent toujours, et il ne reste dans la pile d'appels que `console.log('La boucle est terminée !')`.

4. Avancez rapidement un peu, et les fonctions `setTimeout()` ont terminé, et les instructions `console.log(i)` passent dans la file d'événements. À ce moment-là, notre `console.log('La boucle est terminée !')` a été imprimé et la pile d'appels est vide.

5. Puisque la pile d'appels est vide, les cinq instructions `console.log(i)` sont passées de la file d'événements à la pile d'appels.

6. Souvenez-vous, `i` est maintenant égal à six, et c'est pourquoi nous voyons cinq six imprimés à l'écran.

### Créons la sortie que nous pensions obtenir

Jusqu'à présent, nous avons discuté de la sortie *réelle* de quelques lignes de code simples qui se sont avérées ne pas être si simples. Nous avons parlé de ce qui se passe à un niveau plus profond et de ce qu'est le résultat. Mais, que faire si nous voulons créer la sortie que nous *pensions* obtenir ? En d'autres termes, comment pouvons-nous inverser le résultat suivant :

```python
1 // après une seconde, puis
2 // une seconde plus tard (2 secondes au total)
3 // une seconde plus tard (3 secondes au total)
4 // une seconde plus tard (4 secondes au total)
5 // une seconde plus tard (5 secondes au total)
'La boucle est terminée !' // une seconde plus tard (6 secondes au total)
```

#### **La durée de notre timeout change-t-elle quelque chose ?**

Régler la durée du timeout à zéro semble être une solution possible. Essayons.

```js
for(var i = 1; i < 6; i++) {
   setTimeout(()=>{
      console.log(i);
   },0);
}
console.log('La boucle est terminée !');
```

Résultats :

```python
// Tout apparaît (essentiellement) en même temps

La boucle est terminée !
6
6
6
6
6
```

Cela n'a toujours pas fonctionné. Que s'est-il passé ?

Rappelez-vous, simplement parce que la durée de `setTimeout()` est zéro, il est toujours asynchrone et géré par une API Web. Peu importe la durée, il sera passé à la file d'événements puis à la pile d'appels. Donc même avec un timeout de zéro, le processus reste le même, et la sortie est *relativement* inchangée.

Remarquez que j'ai dit *relativement*. Une chose que vous avez peut-être remarquée et qui était différente, c'est que tout a été imprimé *presque* en même temps. Cela est dû au fait que la durée de `setTimeout()` expire instantanément, et son code passe de l'API Web, à la file d'événements, et enfin à la pile d'appels presque immédiatement. Dans notre exemple précédent, notre code devait attendre 1000 millisecondes avant de passer dans la file d'événements puis dans la pile d'appels.

Donc, si changer la durée à zéro n'a pas fonctionné, que faire maintenant ?

#### Revisiter la portée

Que produira ce code ?

```js

function myFunction1() {
   var a = 'Brandon';
   console.log(a);
}
function myFunction2() {
   var a = 'Matt';
   console.log(a);
}
function myFunction3() {
   var a = 'Bill';
   console.log(a);
}
myFunction1()
myFunction2()
myFunction3()
```

Remarquez comment chaque fonction utilise la même variable nommée `a`. Il pourrait sembler que chaque fonction pourrait lancer une erreur, ou éventuellement écraser la valeur de `a`.

Résultats :

```python
Brandon
Bill
Matt
```

Il n'y a pas d'erreur, et `a` est unique chaque fois.

Il semble que la variable `a` soit unique à chaque fonction. C'est très similaire à la façon dont une adresse fonctionne. Les noms et numéros de rues sont invariablement partagés à travers le monde. Il y a plus d'une seule adresse 123 Main St. C'est la ville et l'état qui fournissent la *portée* à laquelle l'adresse appartient.

Les fonctions fonctionnent de la même manière. Les fonctions agissent comme une bulle protectrice. Tout ce qui est à l'intérieur de cette bulle ne peut pas être accessible par quoi que ce soit à l'extérieur. C'est pourquoi la variable `a` n'est pas réellement la *même* variable. Ce sont trois *variables différentes* situées à trois endroits différents en mémoire. Elles se trouvent simplement toutes partager le même nom.

#### Appliquer les principes de portée à notre exemple :

Nous savons que nous avons accès à la valeur itérative de `i`, juste pas lorsque les instructions `setTimeout()` se terminent. Et si nous prenons la valeur de `i` et l'emballons avec l'instruction `setTimeout()` dans sa propre bulle (comme un moyen de préserver `i`) ?

```js
for(var i = 1; i < 6; i++) {
   function timer(){ // créer une fonction unique (portée) chaque fois
      var k = i; // sauvegarder i dans la variable k qui
      setTimeout(()=>{
         console.log(k);
      },1000);
   }
   timer();
}
```

Résultat :

```python
La boucle est terminée !
1
2
3
4
5
```

#### Cela *fonctionne presque*. Que avons-nous fait ?

Nous commençons à aborder le sujet des *fermetures*. Une discussion approfondie sur les fermetures dépasse le cadre de cet article. Cependant, une brève introduction aidera notre compréhension.

Rappelez-vous, chaque fonction crée une portée unique. Grâce à cela, des variables avec le même nom peuvent exister dans des fonctions séparées et ne pas interférer les unes avec les autres. Dans notre exemple le plus récent, chaque itération a créé une nouvelle portée unique (ainsi qu'une nouvelle variable unique `k`). Lorsque la boucle `for` est terminée, ces cinq valeurs uniques de `k` sont toujours en mémoire et sont accessibles de manière appropriée par nos instructions `console.log(k)`. C'est la fermeture en un mot.

Dans notre exemple original où nous déclarons `i` avec `var`, chaque itération a écrasé la valeur de `i` (qui dans notre cas était une variable globale).

### ES6 rend cela beaucoup plus propre.

En 2015, ECMAScript a publié une mise à jour majeure de ses normes. La mise à jour contenait de nombreuses nouvelles fonctionnalités. L'une de ces fonctionnalités était une nouvelle façon de déclarer des variables. Jusqu'à présent, nous avons utilisé le mot-clé `var` pour déclarer des variables. ES6 a introduit le mot-clé `let`.

```js
for(let i = 1; i < 6; i++) {
   setTimeout(()=>{
      console.log(i);
   },1000);
}
console.log('La boucle est terminée !');
```

Résultats :

```python
La boucle est terminée !
1
2
3
4
5
```

Simplement en changeant `var` en `let`, nous sommes beaucoup plus proches du résultat que nous voulons.

#### Une brève introduction à « let » vs « var »

Dans notre exemple, `let` fait deux choses :

Tout d'abord, il rend `i` disponible uniquement à l'intérieur de notre boucle for. Si nous essayons de logger `i` à l'extérieur de la boucle, nous obtenons une erreur. Cela est dû au fait que `let` est une variable de portée de bloc. Si elle est à l'intérieur d'un bloc de code (comme une boucle `for`), elle ne peut être accessible que là. `var` est de portée de fonction.

Un exemple pour montrer le comportement de `let` vs `var` :

```js
function variableDemo() {
   var i = 'Hello World!';
   for(let i = 1; i < 3; i++) {
      console.log(i); // 1, 2, 3
   }
   console.log(i); // "Hello World!" 
   // la valeur de i de la boucle for est cachée à l'extérieur de la boucle avec let
}

variableDemo();
console.log(i); //Erreur, ne peut pas accéder à aucune valeur de i
```

Remarquez comment nous n'avons pas accès à l'une ou l'autre des valeurs de `i` à l'extérieur de la fonction `variableDemo()`. Cela est dû au fait que 'Hello World' est de portée de fonction, et `i` est de portée de bloc.

La deuxième chose que `let` fait pour nous est de créer une valeur unique de `i` chaque fois que la boucle itère. Lorsque notre boucle est terminée, nous avons créé six valeurs séparées de `i` qui sont stockées en mémoire et que nos instructions `console.log(i)` peuvent accéder. Avec `var`, nous n'avions qu'une seule variable que nous continuions à écraser.

### La boucle n'est pas terminée.

Nous y sommes presque. Nous affichons toujours 'La boucle est terminée !' en premier, et nous n'affichons pas tout à une seconde d'intervalle. Tout d'abord, nous allons examiner deux façons de traiter la sortie 'La boucle est terminée !'.

#### Option 1 : Utiliser setTimeout() et le modèle de concurrency à notre avantage.

Cela est assez simple. Nous voulons que 'La boucle est terminée !' passe par le même processus que les instructions `console.log(i)`. Si nous enveloppons 'La boucle est terminée !' dans un `setTimeout()` dont la durée est supérieure ou égale aux timeouts de la boucle `for`, nous nous assurons que 'La boucle est terminée !' arrive après et expire après les derniers timeouts de la boucle `for`.

Nous allons diviser notre code un peu pour le rendre un peu plus clair :

```js
function loopDone() { // nous allons appeler cela ci-dessous
   console.log('La boucle est terminée !')
}
               
for(let i = 1; i < 6; i++) {
   setTimeout(()=>{
      console.log(i);
   },1000);
}
   
setTimeout(loopDone, 1001);
```

Résultats :

```python
1
2
3
4
5
La boucle est terminée !
```

#### Option 2 : Vérifier la fin de la dernière console.log(i)

Une autre option est de vérifier quand les instructions `console.log(i)` sont terminées.

```js
function loopDone() {
   console.log('La boucle est terminée !');
}
for(let i = 1; i < 6; i++) {
   setTimeout(()=>{
      console.log(i);
      if(i === 5){ // vérifier quand la dernière instruction a été loguée
         loopDone();
      }
   },1000);
}
```

Résultats :

```python
1
2
3
4
5
La boucle est terminée !
```

Remarquez que nous avons placé notre vérification de fin de boucle à l'intérieur de la fonction `setTimeout()`, *pas* dans le corps principal de la boucle for.

Vérifier quand la boucle est terminée ne nous aidera pas, puisque nous devons encore attendre que les timeouts se terminent. Ce que nous voulons faire, c'est vérifier quand les instructions `console.log(i)` sont terminées. Nous savons que ce sera *après* que la valeur de `i` soit 5 et *après* que nous l'ayons loguée. Si nous plaçons notre vérification de fin de boucle après l'instruction console.log(i), nous pouvons nous assurer que nous avons logué le `i` final *avant* d'exécuter `loopDone()`.

### Faire en sorte que tout se passe à une seconde d'intervalle.

Tout se passe essentiellement en même temps parce que la boucle est si rapide, et tous les timeouts arrivent à l'API Web en quelques millisecondes les uns des autres. Par conséquent, ils expirent à peu près au même moment et passent à la file d'événements et à la pile d'appels à peu près au même moment.

Nous ne pouvons pas facilement changer quand ils arrivent à l'API Web. Mais nous pouvons, avec la valeur unique de chaque `i`, retarder combien de temps ils y restent.

```js
function loopDone() {
   console.log('La boucle est terminée !');
}
for(let i = 1; i < 6; i++) {
   setTimeout(()=>{
      console.log(i);
      if(i === 5){ 
         loopDone();
      }
   },i * 1000); // multiplier i par 1000
}
```

Puisque `i` est maintenant unique (parce que nous utilisons `let`), si nous multiplions `i` par 1000, chaque timeout durera une seconde de plus que le timeout précédent. Le premier timeout arrivera avec une durée de 1000 millisecondes, le second avec 2000 et ainsi de suite.

Bien qu'ils arrivent au même moment, il faudra maintenant à chaque timeout une seconde de plus que le précédent pour passer à la file d'événements. Puisque notre pile d'appels est vide à ce moment-là, il passe de la file d'événements immédiatement dans la pile d'appels pour être exécuté. Avec chaque instruction `console.log(i)` arrivant à une seconde d'intervalle dans la file d'événements, nous aurons *presque* la sortie souhaitée.

```python
1 // après une seconde, puis
2 // une seconde plus tard (2 secondes au total)
3 // une seconde plus tard (3 secondes au total)
4 // une seconde plus tard (4 secondes au total)
5 // une seconde plus tard (5 secondes au total)
'La boucle est terminée !' // se produit toujours avec le dernier log
```

Remarquez que 'La boucle est terminée !' arrive toujours *avec* la dernière instruction `console.log(i)`, et non une seconde après. Cela est dû au fait que lorsque `i===5`, `loopDone()` est exécuté. Cela imprime à la fois `i` et les instructions 'La boucle est terminée !' à peu près au même moment.

Nous pouvons simplement envelopper `loopDone()` dans un `setTimeout()` pour résoudre cela.

```js
function loopDone() {
   console.log('La boucle est terminée !');
}
for(let i = 1; i < 6; i++) {
   setTimeout(()=>{
      console.log(i);
      if(i === 5){ 
         setTimeout(loopDone, 1000); // mettre à jour ceci
      }
   },i * 1000);
}
```

Résultats :

```python
1 // après une seconde, puis
2 // une seconde plus tard (2 secondes au total)
3 // une seconde plus tard (3 secondes au total)
4 // une seconde plus tard (4 secondes au total)
5 // une seconde plus tard (5 secondes au total)
'La boucle est terminée !' // une seconde plus tard (6 secondes au total)
```

Nous avons enfin les résultats que nous voulions !

La majeure partie de cet article est née de mes propres luttes et des moments de révélation qui ont suivi, dans une tentative de comprendre les fermetures et la boucle d'événements JavaScript. J'espère que cela peut donner un sens aux processus de base en jeu et servir de fondation pour des discussions plus avancées sur le sujet.

Merci !

woz