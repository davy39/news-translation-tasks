---
title: 'Comment fonctionnent les closures en JavaScript : Un guide pour les développeurs'
subtitle: ''
author: Sumit Saha
co_authors: []
series: null
date: '2025-11-25T15:07:41.623Z'
originalURL: https://freecodecamp.org/news/how-closures-work-in-javascript-a-handbook-for-developers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764083198713/3afde98a-fecd-4669-a2ad-3d78c28d3d5a.png
tags:
- name: JavaScript
  slug: javascript
- name: closure
  slug: closure
- name: closures in javascript
  slug: closures-in-javascript
- name: handbook
  slug: handbook
seo_title: 'Comment fonctionnent les closures en JavaScript : Un guide pour les développeurs'
seo_desc: If you're learning JavaScript, you've probably heard the term "closure"
  at some point. In many developers' experience, just hearing this word can trigger
  anxiety. In nearly 17 years of programming experience, I've noticed that closures
  are one of the...
---


Si vous apprenez le JavaScript, vous avez probablement entendu le terme "closure" à un moment donné. Dans l'expérience de nombreux développeurs, le simple fait d'entendre ce mot peut provoquer de l'anxiété. En près de 17 ans d'expérience en programmation, j'ai remarqué que les closures sont l'un des sujets les plus intimidants pour les développeurs JavaScript, même si elles ne devraient pas l'être.

L'objectif principal de ce guide est de supprimer cette peur. À la fin de ce guide, vous devriez être capable de dire avec confiance : « Je n'ai plus peur des closures ! »

Les closures ne sont pas si compliquées que cela quand on les décompose. Elles peuvent sembler difficiles à saisir tant que vous ne les comprenez pas clairement. De nombreux articles ou tutoriels n'expliquent pas le sujet en profondeur, ce qui vous laisse confus, vous posant des questions comme : « Qu'est-ce qu'une closure exactement ? » ou « Qu'est-ce que cela signifie réellement ? »

Tout au long de ce guide, je vous accompagnerai à travers plusieurs exemples étape par étape. Si vous suivez ce guide jusqu'au bout, je vous le promets : toute votre confusion sur les closures devrait disparaître.

## Voici ce que nous allons aborder

1. [Prérequis](#heading-prerequis)
    
2. [Configuration du projet avant d'apprendre les closures](#heading-configuration-du-projet-avant-dapprendre-les-closures)
    
    * [Créer un nouveau dossier de projet](#heading-creer-un-nouveau-dossier-de-projet)
        
    * [Créer le fichier index.html](#heading-creer-le-fichier-indexhtml)
        
    * [Créer le dossier script + sept fichiers d'exemple](#heading-creer-le-dossier-script-sept-fichiers-dexemple)
        
    * [Note très importante](#heading-note-tres-importante)
        
    * [Lancer le projet](#heading-lancer-le-projet)
        
3. [Fonctions et paramètres - Les bases](#heading-fonctions-et-parametres-les-bases)
    
4. [Accéder aux variables sans paramètres](#heading-acceder-aux-variables-sans-parametres)
    
5. [Comprendre le Scope et le Lexical Scoping](#heading-comprendre-le-scope-et-le-lexical-scoping)
    
6. [Qu'est-ce qu'une Closure ?](#heading-quest-ce-quune-closure)
    
7. [Les fonctions en tant qu'objets](#heading-les-fonctions-en-tant-quobjets)
    
8. [La relation Fonction-Parent](#heading-la-relation-fonction-parent)
    
9. [Fonctions imbriquées et Closures](#heading-fonctions-imbriquees-et-closures)
    
10. [Affiner l'exemple](#heading-affiner-lexemple)
    
11. [Créer des propriétés privées avec les Closures](#heading-creer-des-proprietes-privees-avec-les-closures)
    
12. [Le rôle des Closures dans la confidentialité](#heading-le-role-des-closures-dans-la-confidentialite)
    
13. [Comprendre la mécanique des Closures](#heading-comprendre-la-mecanique-des-closures)
    
    * [Comment les Closures prennent des décisions](#heading-comment-les-closures-prennent-des-decisions)
        
14. [Closures et Enclosing Scopes](#heading-closures-et-enclosing-scopes)
    
    * [La définition de la documentation](#heading-la-definition-de-la-documentation)
        
    * [Le concept d'Enclosing Scope](#heading-le-concept-denclosing-scope)
        
    * [Interpréter la définition de la Closure](#heading-interpreter-la-definition-de-la-closure)
        
15. [Exemple pratique - Closures autonomes](#heading-exemple-pratique-closures-autonomes)
    
    * [Comprendre les références](#heading-comprendre-les-references)
        
16. [La différence entre var et let](#heading-la-difference-entre-var-et-let)
    
    * [Comprendre le Scoping de var et let](#heading-comprendre-le-scoping-de-var-et-let)
        
    * [Observer la différence](#heading-observer-la-difference)
        
    * [Utiliser IIFE avec let](#heading-utiliser-iife-avec-let)
        
17. [Comprendre les Closures à travers l'exemple pratique d'un chronomètre](#heading-comprendre-les-closures-a-travers-lexemple-pratique-dun-chronometre)
    
    * [Définir la fonction Stopwatch](#heading-definir-la-fonction-stopwatch)
        
    * [Utiliser le chronomètre](#heading-utiliser-le-chronometre)
        
    * [Appeler la fonction Timer](#heading-appeler-la-fonction-timer)
        
    * [Inspecter la fonction Timer](#heading-inspecter-la-fonction-timer)
        
    * [Closures et Garbage Collection](#heading-closures-et-garbage-collection)
        
18. [Les Closures dans le code asynchrone](#heading-les-closures-dans-le-code-asynchrone)
    
    * [Exemple asynchrone de base avec setTimeout](#heading-exemple-asynchrone-de-base-avec-settimeout)
        
    * [Exemple de référence de fonction externe](#heading-exemple-de-reference-de-fonction-externe)
        
19. [Exemple pratique : requêtes API avec les Closures](#heading-exemple-pratique-requetes-api-avec-les-closures)
    
    * [Refactorisation avec une fonction externe](#heading-refactorisation-avec-une-fonction-externe)
        
20. [Exemple avancé - Les Closures dans les boucles](#heading-exemple-avance-les-closures-dans-les-boucles)
    
    * [Exemple de boucle synchrone](#heading-exemple-de-boucle-synchrone)
        
    * [Exemple de boucle asynchrone](#heading-exemple-de-boucle-asynchrone)
        
    * [Le problème var vs let](#heading-le-probleme-var-vs-let)
        
    * [Utiliser console.dir avec les Closures de boucle](#heading-utiliser-consoledir-avec-les-closures-de-boucle)
        
    * [Le problème de la boucle var](#heading-le-probleme-de-la-boucle-var)
        
    * [Corriger le problème de la boucle var avec IIFE](#heading-corriger-le-probleme-de-la-boucle-var-avec-iife)
        
21. [Résumé et points clés](#heading-resume-et-points-cles)
    
    * [Qu'est-ce qu'une Closure ?](#heading-quest-ce-quune-closure-1)
        
    * [Les idées principales de ce guide](#heading-les-idees-principales-de-ce-guide)
        
    * [L'importance des Closures](#heading-limportance-des-closures)
        
22. [Mots de la fin](#heading-mots-de-la-fin)
    

## Prérequis

Pour suivre et tirer le meilleur parti de ce guide, vous devriez avoir :

1. Des connaissances de base en JavaScript (style ES6)
    
2. Une familiarité avec les outils de développement du navigateur
    
3. Une aisance avec le code asynchrone (promises)
    
4. Une capacité de base à utiliser le terminal / la ligne de commande
    
5. Une familiarité avec un éditeur de code comme VS Code – extension Live Server (pour exécuter des fichiers HTML localement)
    

J'ai également créé une vidéo pour accompagner cet article. Si vous êtes du genre à aimer apprendre par la vidéo autant que par le texte, vous pouvez la consulter ci-dessous.

%[https://www.youtube.com/watch?v=JVT_d9Qx_ro] 

## Configuration du projet avant d'apprendre les closures

Les closures sont un concept incroyable en JavaScript. Mais si vous vous lancez dans le code sans préparation, elles peuvent sembler un peu intimidantes.

Alors avant de commencer à explorer les closures, configurons un projet simple et propre où vous pourrez tester chaque exemple confortablement. Une fois cette configuration terminée, vous n'aurez plus besoin de la répéter tout au long de l'article. Suivez donc attentivement et vous préparerez tout d'un coup.

### Créer un nouveau dossier de projet

Ouvrez votre terminal et exécutez :

```bash
mkdir closure
cd closure
```

Ce dossier contiendra votre fichier HTML principal et tous les exemples JavaScript.

### Créer le fichier index.html

Maintenant, créez le fichier HTML :

```bash
touch index.html
```

Ouvrez `index.html` et ajoutez le code suivant :

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Closure Tutorial | LogicBase Labs</title>
    </head>
    <body>
        <script src="./script/example-1.js"></script>
        <script src="./script/example-2.js"></script>
        <script src="./script/example-3.js"></script>
        <script src="./script/example-4.js"></script>
        <script src="./script/example-5.js"></script>
        <script src="./script/example-6.js"></script>
        <script src="./script/example-7.js"></script>
    </body>
</html>
```

#### Pourquoi autant de balises `<script>` ?

Bonne question ! Dans ce tutoriel, vous explorerez les closures de **7 manières différentes**. Chaque exemple vivra dans son propre fichier JavaScript, afin que les choses restent propres et accessibles aux débutants. Si vous essayiez de tout mettre dans un seul fichier, les sorties se mélangeraient et deviendraient confuses. C'est pourquoi vous chargez chaque exemple séparément.

### Créer le dossier `script` + sept fichiers d'exemple

Créons un dossier nommé **script** :

```bash
mkdir script
cd script
```

Maintenant, créez les sept fichiers d'exemple :

```bash
touch example-1.js
touch example-2.js
touch example-3.js
touch example-4.js
touch example-5.js
touch example-6.js
touch example-7.js
```

Vous écrirez et testerez chaque exemple de closure à l'intérieur de ces fichiers.

### Note très importante :

Si les 7 fichiers s'exécutent en même temps, la sortie de votre console sera mélangée. Vous ne comprendrez pas quel message provient de quel exemple.

Voici donc la règle :

* Lorsque vous travaillez sur `example-1.js`, commentez le reste.
    
* Lorsque vous travaillez sur `example-3.js`, décommentez celui-là uniquement, et commentez les autres.
    

**Exemple :**

```html
<!-- <script src="./script/example-1.js"></script> -->
<!-- <script src="./script/example-2.js"></script> -->
<script src="./script/example-3.js"></script>
<!-- <script src="./script/example-4.js"></script> -->
<!-- <script src="./script/example-5.js"></script> -->
<!-- <script src="./script/example-6.js"></script> -->
<!-- <script src="./script/example-7.js"></script> -->
```

Cela permet de garder votre sortie propre, claire et sans conflit.

### Lancer le projet

Ouvrez **Live Server** depuis VS Code et vous verrez : [http://127.0.0.1:5500/closure/index.html](http://127.0.0.1:5500/closure/index.html)

C'est votre route de travail. À l'intérieur de ce projet, vous explorerez le monde complet des closures étape par étape. Vous êtes maintenant prêt à plonger dans les closures et à apprendre ce qu'elles sont, comment elles fonctionnent et pourquoi elles sont l'un des concepts les plus puissants de JavaScript.

## Fonctions et paramètres – Les bases

Vous allez maintenant travailler principalement sur le fichier `example-1.js`. Écoutez, tout au long de ce guide, vous écrirez d'abord le code complet, puis nous irons ligne par ligne pour comprendre le détail. Il n'y a pas de quoi s'inquiéter : nous allons tout découvrir en profondeur.

**Code complet :** `example-1.js`

```js
// example-1.js
function sum(num1, num2) {
    return num1 + num2;
}
console.log(sum(2, 3));
```

Habituellement, lorsque vous souhaitez utiliser une variable externe à l'intérieur d'une fonction, vous la passez en paramètre. Par exemple, considérons une fonction appelée `sum` :

```javascript
function sum(num1, num2)
```

Ici, deux nombres sont pris comme paramètres. Pour additionner ces nombres et retourner le résultat :

```javascript
return num1 + num2;
```

Pour voir le résultat :

```javascript
console.log(sum(2, 3));
```

Le résultat sera `5`. Simple, n'est-ce pas ?

## Accéder aux variables sans paramètres

**Code complet :** `example-1.js`

```js
var num1 = 2;
var num2 = 3;

function sum() {
    return num1 + num2;
}

console.log(sum());
```

Mais en JavaScript, il existe un moyen de faire la même chose sans passer de paramètres. Supprimons les paramètres de la fonction `sum`. À la place, vous définirez deux variables dans le scope global :

```javascript
var num1 = 2;
var num2 = 3;
```

Maintenant, lorsque vous appelez `sum()`, le résultat sera toujours `5`.

La question est : *« comment JavaScript fait-il cela ? »* Cela semble étrange, non ? À l'intérieur d'une fonction, vous utilisez des variables qui n'appartiennent pas réellement à cette fonction – elles existent à l'extérieur, dans l'environnement plus large où la fonction a été créée. En termes simples, la fonction utilise des variables de son scope parent.

## Comprendre le Scope et le Lexical Scoping

Ce concept se rapporte à l'un des principes les plus fondamentaux de JavaScript : tout ce qui provient d'un parent est accessible à l'enfant. S'il y avait des fonctions imbriquées à l'intérieur de cette fonction, même l'enfant le plus profond pourrait accéder à des variables comme `num1` et `num2` du parent. Les variables du parent sont entièrement accessibles à l'enfant, mais rien de l'enfant ne peut être accédé par le parent.

J'ai déjà couvert ce sujet dans une vidéo détaillée sur le **JavaScript Scope** sur la chaîne YouTube LogicBase Labs. Si vous souhaitez revoir le concept ou obtenir un rappel rapide, vous pouvez regarder la vidéo ci-dessous.

%[https://www.youtube.com/watch?v=NtHgwL3uubk] 

Par exemple, si vous définissez une nouvelle variable à l'intérieur de la fonction `sum`, elle ne peut pas être accédée depuis l'extérieur de la fonction. C'est l'idée centrale du scope. Ce système de scope est théoriquement appelé **Lexical Scoping**. Puisque le sujet d'aujourd'hui est les Closures, comprendre le scope est essentiel, car les closures et le scope sont profondément connectés.

Selon le lexical scoping, une fonction enfant peut accéder aux variables de son parent, mais un parent ne peut pas accéder à celles de l'enfant. Ce n'est pas aléatoire – c'est une convention ou une directive spécifique en JavaScript.

## Qu'est-ce qu'une Closure ?

Le mot "closure" signifie littéralement un "lien" ou une "enceinte". Pensez-y comme au fait de garder une variable enfermée en toute sécurité, tout comme on stocke quelque chose dans une boîte.

Même si la boîte est fermée, vous pouvez toujours utiliser son contenu en cas de besoin. C'est pourquoi on l'appelle une closure : parce que vous gardez les variables d'une fonction enfermées de telle sorte que, même si le monde extérieur ne peut pas y accéder directement, la fonction elle-même peut toujours les utiliser chaque fois que nécessaire.

## Les fonctions en tant qu'objets

En JavaScript, chaque fois que vous écrivez une fonction, la fonction est en réalité traitée comme un objet. Chaque fonction en JavaScript fonctionne comme un objet. Tout comme vous pouvez faire un `console.log` d'un objet pour le voir, vous pouvez également inspecter une fonction.

Imprimons notre fonction `sum` :

```javascript
console.dir(sum);
```

Remarquez que vous n'appelez pas la fonction. Vous imprimez plutôt son corps. Vous utilisez `dir` au lieu de `log` car `console.log` ne montre que le corps de la fonction, tandis que `console.dir` affiche la fonction comme un objet, vous permettant de voir chacune de ses propriétés une par une. Vous pouvez le voir comme une version améliorée de `console.log`.

En regardant la sortie, vous verrez un objet. En le développant, vous découvrirez de nombreuses propriétés, comme `name`, `length`, `prototype`, et plus encore. Tout en bas, il y a une propriété appelée `Scopes`. À l'intérieur de `Scopes`, il y a une section nommée `Global` contenant d'autres détails. La propriété `Scopes` est ce sur quoi nous allons principalement nous concentrer ici.

![Nested Function and Closure](https://cdn.hashnode.com/res/hashnode/image/upload/v1763460615059/210b2880-7cb7-4161-ac75-c67d196341ed.png align="left")

## La relation Fonction-Parent

Remarquez quelque chose ici : la fonction `sum` a son propre monde, n'est-ce pas ? Alors pourquoi référence-t-elle toujours le scope global ?

Chaque fonction maintient en fait une connexion avec son environnement parent. Elle ne vit pas seulement dans son propre monde – elle garde un lien vers l'environnement où elle a été créée. En termes simples, elle détient toujours une référence à son parent.

Pourquoi fait-elle cela ? Parce que si quelque chose change dans l'environnement parent (comme la valeur d'une variable ou le besoin de l'utiliser à l'intérieur de la fonction), la fonction peut toujours y accéder.

Tout ce processus est le concept central d'une closure. Une fonction garde la trace des variables qu'elle utilise en dehors de son propre scope en se refermant sur son parent, et le parent de son parent – essentiellement toute la chaîne de scopes au-dessus d'elle – les détient comme références.

C'est pourquoi cet exemple est en fait la forme la plus simple d'une closure. La fonction `sum` elle-même est une closure car elle a capturé certaines variables de son environnement extérieur et peut les utiliser chaque fois que nécessaire.

Même si vous voyez souvent les closures expliquées avec des exemples où « une fonction est à l'intérieur d'une autre fonction », l'idée fondamentale commence ici : *« toute fonction qui conserve l'accès aux variables de son scope extérieur est, par essence, une closure. »*

## Fonctions imbriquées et Closures

**Code complet :** `example-1.js`

```js
// example-1.js
var num1 = 2;
var num2 = 3;

function sum() {
    return function () {
        return num1 + num2;
    };
}

var myFunc = sum();

console.dir(myFunc);
```

Vous pouvez comprendre cela encore plus clairement en modifiant la fonction `sum` précédente. Au lieu de retourner directement une valeur, vous ferez en sorte que la fonction `sum` retourne une autre fonction :

```javascript
return function () {};
```

Et à l'intérieur de cette fonction interne, vous écrivez :

```javascript
return num1 + num2;
```

Alors, qu'est-ce que cela signifie ? La fonction `sum` ne retourne plus directement une valeur. À la place, elle retourne une fonction.

Maintenant, créez une autre variable appelée `myFunc` :

```javascript
var myFunc = sum();
```

Vous avez appelé la fonction `sum`, et tout ce qu'elle a retourné (la fonction interne) est maintenant stocké dans `myFunc`. En d'autres termes, `myFunc` est essentiellement la fonction interne retournée par `sum`.

Si vous imprimez `myFunc` dans la console :

```javascript
console.dir(myFunc);
```

Vous verrez `num1` et `num2` listés comme variables dans la sortie. Cette fonction tient toujours à son environnement global. Même s'il s'agit d'une fonction interne, elle est toujours connectée au scope global et maintient les mêmes références globales qu'auparavant.

![Nested Function and Closure](https://cdn.hashnode.com/res/hashnode/image/upload/v1763460615059/210b2880-7cb7-4161-ac75-c67d196341ed.png align="left")

## Affiner l'exemple

**Code complet :** `example-1.js`

```js
// example-1.js
var num1 = 2;

function sum() {
    var num2 = 3;
    return function () {
        return num1 + num2;
    };
}

var myFunc = sum();

console.dir(myFunc);
```

Maintenant, supprimez la variable `num2` du scope global et définissez-la à l'intérieur de la fonction `sum` à la place.

![Refine the closure](https://cdn.hashnode.com/res/hashnode/image/upload/v1763463873933/84153aca-ee54-476d-99be-4b638926c0f4.gif align="left")

Cette fois, dans le navigateur, vous pouvez clairement voir quelque chose étiqueté "Closure". En d'autres termes, le navigateur montre directement qu'une closure a été créée à l'intérieur de cette fonction.

Dans les anciennes versions de Chrome, vous auriez également vu "Closure" dans l'exemple précédent. Mais dans les versions plus récentes, il s'affiche comme "Global" jusqu'à ce qu'une fonction se referme réellement sur une autre fonction. Lorsqu'une fonction est retournée depuis une autre fonction, c'est là que le navigateur affiche "Closure". Mais gardez à l'esprit que théoriquement, l'exemple précédent était également une sorte de closure. La différence réside simplement dans la manière dont le navigateur le présente.

Lorsque vous avez fait `console.dir(myFunc)`, vous avez vu que cette fonction interne utilise à la fois `num1` et `num2` :

* `num1` est dans le scope global
    
* `num2` est à l'intérieur du scope de la fonction `sum`
    

Alors, que fait cette fonction interne ? Elle prend une référence à `num1` depuis le scope global et, en même temps, prend une référence à `num2` depuis sa fonction parente, `sum`. En d'autres termes, cette fonction interne porte désormais deux mondes en elle : l'un est le scope global, et l'autre est son scope parent. C'est exactement ce que fait une closure : elle garde tous les scopes extérieurs dont elle a besoin « enfermés » afin de pouvoir utiliser leurs variables chaque fois que nécessaire.

Dans le navigateur, vous pouvez voir qu'à l'intérieur de cette closure, `num2` existe, tandis que `num1` reste dans le scope global. Donc `num1` ne fait plus partie de la closure. Qu'est-ce que cela signifie ? La fonction ne transporte que les parties de l'environnement dont elle a réellement besoin pour son exécution. En termes simples, elle prend toutes les variables dont elle a besoin, ainsi que leurs références, sous la forme d'un paquet compact.

Pensez-y comme si la fonction détenait des références : chaque fois que l'une de ces variables est mise à jour, la fonction peut voir ces changements car elle est toujours connectée aux mêmes références.

Si vous avez appelé `myFunc = sum()` une fois et que vous continuez à appeler `sum()` à plusieurs reprises, il n'y a pas de problème. À chaque fois, une nouvelle fonction créera son propre scope séparé et gardera une référence à ce scope. Vous avez défini une fonction puis l'avez appelée ailleurs. Chaque fois que vous appelez cette fonction, elle peut toujours accéder aux données de son scope précédent. C'est parce que chaque fonction préserve toutes les informations de son scope parent sous forme de références. C'est exactement ainsi qu'une fonction se souvient de ses variables extérieures – et c'est ce qu'est une closure.

## Créer des propriétés privées avec les Closures

Jusqu'à présent, tous les exemples que vous avez vus étaient très simples. Voyons maintenant un exemple pratique qui vous aidera à mieux comprendre les closures et à dissiper toute confusion.

Pensez un instant aux autres langages de programmation : lorsque vous voulez créer une propriété privée, que faites-vous habituellement ? Vous définissez une propriété à l'intérieur d'une classe et la marquez comme "privée" afin que personne ne puisse y accéder directement depuis l'extérieur de la classe. Ensuite, à l'intérieur de la classe, vous créez une ou plusieurs fonctions publiques (comme des getters ou des setters) qui permettent un accès contrôlé ou une modification de cette propriété. En d'autres termes, vous ne pouvez pas toucher à la propriété directement depuis l'extérieur – vous ne pouvez interagir avec elle que par le biais de fonctions spécifiques définies à l'intérieur de la classe.

En JavaScript, vous pouvez réaliser la même idée beaucoup plus simplement en utilisant les closures, entièrement dans un style fonctionnel.

![Creating private property](https://cdn.hashnode.com/res/hashnode/image/upload/v1763463928785/5e2d10bf-0e21-420d-8c27-576ab7172896.gif align="left")

Comment ? Voyons un exemple. Supposons que vous ayez une fonction simple :

**Code complet :** `example-2.js`

```js
// example-2.js
function bankAccount(initialBalance) {
    var balance = initialBalance;

    return function () {
        return balance;
    };
}
var account = bankAccount(100000);

console.log(account());
console.dir(account);
```

```javascript
function bankAccount(initialBalance) {}
```

Vous l'avez nommée `bankAccount`, et elle prend le solde initial de l'utilisateur comme paramètre.

À l'intérieur, définissez une variable :

```javascript
var balance = initialBalance;
```

Ainsi, le solde initial de l'utilisateur est stocké en interne dans une variable appelée `balance`. Ensuite, retournez une fonction qui retourne cette variable `balance`. En d'autres termes, le solde ne peut être accédé que par cette fonction retournée.

À l'extérieur, dans le scope global, créez une variable :

```javascript
var account = bankAccount(100000);
```

Ici, vous avez appelé la fonction `bankAccount` et passé 100000 comme solde initial. Que fait réellement cette fonction ? Elle retourne une autre fonction. Donc maintenant, la variable `account` détient cette fonction retournée.

Si vous écrivez dans la console :

```javascript
console.log(account());
```

Le résultat sera 100000.

![Private Property Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763463963441/8104145d-b908-4131-8a6b-3c4c3ad88434.png align="left")

Mais si vous essayez ceci :

```javascript
console.log(balance);
```

cela ne fonctionnera pas, car la variable `balance` ne peut pas être accédée depuis l'extérieur.

![Error Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763463984564/6c70013b-6566-4bf2-a517-bea3672022e1.png align="left")

Qu'est-ce que cela signifie ? La propriété `balance` est protégée ou privée. Personne de l'extérieur ne peut la toucher directement. Pour voir le solde, vous ne pouvez qu'appeler la fonction retournée à l'intérieur de la fonction d'origine. C'est ainsi que vous gardez `balance` comme une variable privée et contrôlez l'accès à celle-ci.

## Le rôle des Closures dans la confidentialité

Alors, quel est le rôle de la closure ici ? C'est exactement ce qui rend cela possible. La fonction interne est la closure. Si vous écrivez :

```javascript
console.dir(account);
```

Vous verrez qu'à l'intérieur de la fonction `account` se trouve la fonction retournée.

En prenant la sortie et en la développant, vous verrez que la variable `balance` existe à l'intérieur de la closure. Exactement, n'est-ce pas ? Cela signifie que `balance` n'a pas été créée à l'intérieur de la fonction `account` elle-même – elle a été créée un niveau de scope au-dessus. Pourtant, vous pouvez toujours accéder à `balance` depuis la fonction retournée.

C'est similaire à l'exemple précédent, mais ce cas d'utilisation est légèrement différent. Ici, vous montrez comment une propriété privée peut être sécurisée. Même si vous avez appelé la fonction interne depuis l'extérieur, elle avait toujours accès à `balance` dans son scope. Ainsi, le scope extérieur ne peut pas accéder directement à `balance`, mais grâce à la closure, vous pouvez maintenir une référence vers celle-ci. Même si la fonction est appelée de l'extérieur, la closure vous permet d'accéder à la propriété privée de manière protégée.

Pourquoi protégée ? Parce que vous n'y accédez pas directement – vous ne pouvez voir `balance` qu'à travers l'appel de la fonction.

💡C'est un autre cas d'utilisation puissant des closures : sécuriser les propriétés privées afin qu'elles ne puissent pas être directement accédées de l'extérieur, mais seulement via des fonctions spécifiques.

## Comprendre la mécanique des Closures

### Comment les Closures prennent des décisions

Maintenant, examinons un autre aspect des closures. Revenons à notre premier exemple.

**Code précédent :** `example-1.js`

```js
// example-1.js
var num1 = 2;

function sum() {
    var num2 = 3;
    return function () {
        return num1 + num2;
    };
}

var myFunc = sum();

console.dir(myFunc);
```

Dans cet exemple, vous avez utilisé une variable appelée `num2` à l'intérieur de la fonction interne. C'est pourquoi la fonction a agi comme une closure, n'est-ce pas ?

**Code complet :** `example-3.js`

```js
// example-3.js
var num1 = 2;
function sum() {
    var num2 = 3;
    return function () {
        return num1;
    };
}
var myFunc = sum();
console.dir(myFunc);
```

Maintenant, gardez la variable mais arrêtez d'utiliser `num2` à l'intérieur de la fonction interne. Si vous vérifiez la sortie, vous verrez que la closure a disparu. Pourquoi ?

![Closure Gone Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464099671/a34e465a-ed85-4631-8a0d-07e681cecc52.png align="left")

C'est parce que `num2` n'est pas utilisé à l'intérieur de la fonction interne. JavaScript reconnaît intelligemment que cette variable n'est pas nécessaire, elle n'est donc pas incluse dans la closure. En d'autres termes, JavaScript décide de lui-même : les variables qui ne seront pas utilisées à l'intérieur de la fonction, même si elles existent dans le scope extérieur, ne sont pas incluses dans la closure. Seules les variables dont la fonction a réellement besoin font partie de la closure.

**Code complet :** `example-3.js`

```js
// example-3.js
var num1 = 2;
function sum() {
    var num2 = 3;
    var num = 6;
    return function () {
        return num;
    };
}
var myFunc = sum();
console.dir(myFunc);
```

Par exemple, si vous définissez une autre variable à l'intérieur de la fonction `sum` :

```javascript
var num = 6;
```

et que vous ne faites rien d'autre, il n'y a toujours pas besoin de closure. Mais si vous modifiez la fonction interne pour retourner `num` au lieu de `num1`, la closure réapparaît. Cette fois, la closure ne contient que `num`. `num2` ne sera pas là, mais `num1` reste car il existe dans le scope global. JavaScript préserve ce scope pour maintenir le lexical scoping.

![Closure with num Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464124937/3a155661-838d-4070-a8ab-e6c283a0838f.png align="left")

Si vous regardez le scope global, vous pouvez toujours voir `num1`. C'est parce que vous avez utilisé le mot-clé `var`. Si vous aviez utilisé `let`, il ne serait pas visible. La différence clé que vous remarquez est : `num1` existe dans le scope global, il reste donc dans l'« environnement » de la closure, mais si une variable à l'intérieur de la fonction interne n'est pas utilisée, elle n'est pas incluse dans la closure.

Par exemple, si vous utilisez `num1`, vous accédez à la variable globale. Alors que se passe-t-il maintenant ? Y aura-t-il une closure ? Regardez, il n'y en a pas. Puisque `num1` existe dans le scope global, il n'y a pas de besoin supplémentaire. Le scope global est suffisant, et aucune closure séparée n'est requise. Cela montre comment les closures fonctionnent réellement.

![No Closure with Global Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464145498/68d704f4-f614-49e9-929f-735880ef374a.png align="left")

Une closure décide quelles variables doivent être conservées à l'intérieur de la fonction et lesquelles ne le doivent pas. JavaScript prend cette décision automatiquement. Vous avez juste besoin de vous souvenir du lexical scoping pour que les variables du scope extérieur puissent être accédées.

En termes simples, les closures prennent des décisions intelligentes. Les variables utilisées à l'intérieur de la fonction sont gardées « à l'intérieur », les variables des scopes extérieurs qui ne sont pas utilisées ne sont pas incluses, et les variables globales sont accessibles directement, il n'est donc pas nécessaire de les inclure dans la closure.

Ici, vous avez gardé `num1`, et il existe dans le scope global. La fonction peut y accéder directement à partir de là. Mais si la fonction interne n'utilisait que `num` – qui n'existe pas dans son propre scope ou globalement – alors une closure devrait être créée pour transporter cette variable.

En résumé, une closure n'enveloppe pas tout. Elle n'inclut pas les variables qui sont déjà à l'extérieur. C'est un point important. Un autre point important est que les variables du scope global ne sont jamais incluses dans les closures.

## Closures et Enclosing Scopes

### La définition de la documentation

Souvent, il y a une certaine confusion quant au moment où une closure apparaît et au moment où elle affiche simplement global. Même les recruteurs seniors hésitent parfois à appeler le scope global une closure au premier coup d'œil.

Si vous regardez la documentation JavaScript maintenue par Mozilla, les documents de 2016 soulignaient quelque chose d'important.

Dans la définition, il était indiqué :

> "variables that are used locally, but defined in an enclosing scope" ([Référence](https://web.archive.org/web/20160722004334/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures))

Cela fait référence aux variables qui sont utilisées localement à l'intérieur d'une fonction mais qui sont en réalité définies dans un scope extérieur. C'est la clé. Seules les variables qui sont réellement utilisées à l'intérieur d'une fonction sont incluses dans la closure. Les variables qui existent dans un scope extérieur mais ne sont pas utilisées à l'intérieur de la fonction ne font pas partie de la closure.

En termes simples, une closure est une fonction qui se souvient de son scope local ainsi que des variables nécessaires d'un scope extérieur, de sorte que même si la fonction est appelée de l'extérieur, elle peut toujours accéder à ces variables.

### Le concept d'Enclosing Scope

Supposons que vous ayez une variable `num` définie à l'extérieur, mais que vous l'utilisiez localement à l'intérieur de la fonction. C'est pourquoi le navigateur l'affiche comme une closure, tout comme le dit la documentation.

**Code complet :** `example-3.js`

```js
// example-3.js
var num1 = 2;
function sum() {
    var num2 = 3;
    return num1 + num2;
}
console.dir(sum);
```

Mais si vous n'utilisez pas la variable extérieure à l'intérieur de la fonction retournée, que se passe-t-il ? Si vous supprimiez tout le reste et retourniez simplement `num1 + num2`, la fonction `sum` fonctionnerait très bien. Mais si vous faites `console.dir(sum)`, le mot "closure" n'apparaît pas.

Pourquoi ? Parce que `num2` est local à l'intérieur de la fonction, et il n'est pas nécessaire de l'inclure dans une closure. Une closure n'est nécessaire que pour utiliser des variables d'un scope extérieur. Puisqu'il s'agit du tout premier niveau de scope extérieur (c'est-à-dire le scope global) et qu'il n'est à l'intérieur d'aucune fonction, la fonction `sum` le capture déjà dans son propre scope. Aucune closure supplémentaire n'est donc créée.

La question critique est : *« quand le navigateur affiche-t-il une closure, et quand ne l'affiche-t-il pas ? »* L'explication vient de la documentation : "variables that are used locally, but defined in an enclosing scope." Votre variable `num1` est définie à l'extérieur mais utilisée localement à l'intérieur. Mais `num1` n'a pas d'enclosing scope. Ici, un enclosing scope signifie un scope qui en enveloppe un autre – à l'intérieur d'un ensemble d'accolades. Mais `num1` est directement dans le scope global, pas à l'intérieur d'un enclosing scope.

**Code complet :** `example-3.js`

```js
// example-3.js
(function () {
    var num1 = 2;
    function sum() {
        var num2 = 3;
        return num1 + num2;
    }

    console.dir(sum);
})();
```

Si vous voulez amener cela dans un enclosing scope, vous devez envelopper le tout dans une fonction. Vous pouvez écrire une fonction anonyme comme ceci :

```javascript
function(){}
```

Ensuite, vous mettez tout à l'intérieur de cette fonction et l'appelez immédiatement. C'est ce qu'on appelle une **Immediately Invoked Function Expression** (IIFE en abrégé). C'est essentiellement une fonction qui est définie et exécutée en même temps.

Lorsque vous utilisez une IIFE, tout est déplacé dans un enclosing scope. Le `num1` qui était auparavant ouvert dans le scope global est maintenant à l'intérieur de cette fonction. Il fait donc désormais partie d'un enclosing scope. Si vous vérifiez dans le navigateur et que vous le développez, vous voyez le mot "closure".

![Closure with Enclosing Scope Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464214402/43092c54-012f-42be-a7ea-d25c4d15eb90.png align="left")

C'est parce que vous avez amené les variables dans un enclosing scope. Le navigateur l'affiche maintenant comme une closure.

### Interpréter la définition de la Closure

Si quelqu'un est confus ou n'est pas d'accord, il pourrait dire : « L'extérieur n'est pas une closure, c'est juste le scope global. » Mais théoriquement, vous pouvez toujours le considérer comme une closure. Certains pourraient insister sur le fait que « c'est une closure », tandis que d'autres pourraient ne pas être d'accord.

Le fait est que JavaScript garde toujours le scope global intact pour maintenir le lexical scoping. Les personnes qui ne sont pas d'accord pourraient dire : « Le scope global est simplement préservé, ce n'est pas une closure. » Et c'est juste. Mais le concept est vraiment le même. Si une variable d'un scope extérieur est utilisée ou référencée à l'intérieur d'une fonction, elle se comporte exactement comme une closure. L'idée est cohérente.

Il y a cependant une petite différence : le scope global conserve toutes les variables qui existent en dehors de toute fonction. C'est pourquoi certains pourraient soutenir que ce n'est pas techniquement une closure. Mais d'un point de vue théorique, il se comporte comme tel, avec seulement des différences mineures pour les variables globales.

**Code complet :** `example-3.js`

```js
// example-3.js
var num1 = 2;
function sum() {
    var num2 = 3;
    return num1 + num2;
}

console.dir(sum);
```

Si vous n'utilisiez pas d'IIFE et reveniez à la configuration précédente, le navigateur ne l'afficherait plus comme une closure. Et le `var num1` est dans le scope global.

![No Closure with Global Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464280818/d25cc856-0178-4d94-9f56-654f4c62637d.png align="left")

Si vous ajoutez une autre variable :

```javascript
var num3 = 5;
```

Ce `num3` n'est pas utilisé par la fonction `sum`, mais si vous regardez dans le scope global, vous pouvez toujours le voir. Le navigateur affiche également `num3`.

![Global Scope with num3 Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464328789/6bcffff2-3e8c-4cc7-8da6-9f03910aee92.png align="left")

Mais une closure ne garde que ce qui est nécessaire. Ici, `num3` existe parce qu'il fait partie du scope global. L'objet global détient toujours des références à ses propres variables, c'est pourquoi `num3` est visible. Cela cause souvent de la confusion : faut-il l'appeler une closure ou non ?

Le fait est que dans la documentation de 2016, le terme "enclosing scope" était clairement mentionné. Dans la documentation actuelle, cette expression est absente. Cela signifie qu'ils ont intentionnellement évité cette confusion.

La définition moderne dit maintenant : "closure is the combination of a function bundled together with references to its surrounding state", ce qui est écrit de manière plus concise qu'auparavant. ([Référence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures))

Ici, "state" fait référence à l'environnement lexical – cela pourrait être l'environnement de l'enfant, l'environnement du parent ou le scope entier. Selon cette définition, une fonction se garde elle-même avec toutes les variables dont elle a besoin pour se souvenir, le tout regroupé. Expliquer cela clairement avec des mots peut être délicat. Mais vous verrez d'autres exemples plus loin, qui rendront chaque cas d'utilisation clair.

## Exemple pratique : Closures autonomes

**Code complet :** `example-3.js`

```js
// example-3.js
(function () {
    var num1 = 2;
    var num2 = 3;

    function sum() {
        return num1 + num2;
    }

    console.log(sum());
    console.dir(sum);
})();
```

Examinons un autre aspect. Vous revenez à la fonction IIFE. Ici, vous avez une fonction appelée `sum` qui additionne `num1` et `num2` et retourne le résultat. `num1` et `num2` existent tous deux à l'intérieur de la fonction IIFE. Cela signifie que vous avez gardé toute la configuration autonome à l'intérieur d'une fonction closure.

Lorsque vous appelez la fonction `sum` :

```javascript
console.log(sum());
```

et à la ligne suivante, écrivez :

```javascript
console.dir(sum);
```

Vérifiez le résultat. Initialement, `2 + 3` donne `5`, ce qui est exactement ce que vous voyez. Puisque `num1` et `num2` existent maintenant à l'intérieur du scope global de l'IIFE.

![IIFE Closure Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464361079/cdcff658-023c-4a25-8749-eb618b3cfcc3.png align="left")

**Code complet :** `example-3.js`

```js
// example-3.js
(function () {
    var num1 = 2;
    var num2 = 3;
    function sum() {
        return num1 + num2;
    }
    console.log(sum());
    console.dir(sum);

    num1 = 6;
    num2 = 7;

    console.log(sum());
    console.dir(sum);
})();
```

Vous pouvez modifier ces variables si vous le souhaitez :

```javascript
num1 = 6;
num2 = 7;
```

Ensuite, si vous appelez à nouveau :

```javascript
console.log(sum());
console.dir(sum);
```

Vous verrez deux résultats différents. Le premier appel retourne `5` car initialement `2 + 3` a été calculé. Après avoir changé `num1` et `num2`, l'appel suivant retourne `13`. Ainsi, vous pouvez voir qu'une closure garde les variables extérieures et les rend accessibles à l'intérieur de la fonction, n'est-ce pas ?

![IIFE Closure with Updated Values Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464386404/cd2447c8-447e-4fff-b72d-f6ec2d2c8122.png align="left")

À ce moment-là, vous avez vérifié la fonction en utilisant `console.dir`. Tout d'abord, développez le `dir` en bas. Ici, vous voyez une entrée étiquetée "closure", et à l'intérieur, vous remarquez `num1 = 6` et `num2 = 7`. C'est parfait, car avant d'écrire `dir`, vous aviez changé les valeurs de `num1` et `num2`, donc il affiche les dernières valeurs. Mais si vous revenez à l'état précédent et développez le premier `console.dir`, étonnamment, il affiche toujours `num1 = 6` et `num2 = 7`. Les deux sont identiques – assez bizarre, n'est-ce pas ?

C'est parce que lorsque vous avez fait `console.log`, le résultat affichait `2 + 3`. Mais à la ligne suivante, les valeurs n'avaient pas encore réellement changé. Dans `console.dir`, vous voyez qu'à l'intérieur de la closure, les valeurs restent 6 et 7.

![Closure with Updated Values Dir Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464426043/f7f87ffb-8bf5-4fbb-ac1c-091bee65570c.gif align="left")

C'est exactement ce sur quoi j'ai insisté : **une closure ne détient pas réellement les valeurs elles-mêmes. Elle détient une référence aux variables.**

### Comprendre les références

Alors, qu'est-ce que cela signifie ? Cela signifie qu'un pointeur est stocké vers l'emplacement mémoire de votre variable. Une fois qu'une référence est stockée, le pointeur lui-même reste le même, mais la valeur peut changer à tout moment.

Lorsque vous utilisez `console.dir`, le navigateur affiche cette référence, c'est pourquoi il affiche toujours la dernière valeur. Le navigateur travaille très vite, et la référence a déjà été mise à jour. Lorsque vous avez défini `num1` et `num2` à 6 et 7 à l'intérieur de la closure, la référence est mise à jour. Vous voyez exactement la même variable, mais vous ne voyez pas les valeurs intermédiaires. Mais quand vous faites `console.log`, la fonction utilise correctement sa valeur correspondante. C'est pourquoi chaque changement dans le scope intermédiaire n'est pas clairement visible. En raison des mises à jour de référence, vous voyez toujours la dernière valeur, pas l'état intermédiaire direct.

![Closure Reference Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464448552/b61bc77c-2563-4fb0-9630-d36a4f304439.png align="left")

Donc, pour réitérer : une closure ne stocke pas les valeurs réelles à l'intérieur. Elle stocke des références à ces valeurs.

Garder ce concept à l'esprit est vraiment crucial.

## La différence entre `var` et `let`

**Code complet :** `example-3.js`

```js
// example-3.js
var num1 = 2;
var num2 = 3;
function sum() {
    return num1 + num2;
}

console.dir(sum);
```

Examinons maintenant un autre aspect des closures. Plus tôt, vous avez déclaré deux variables dans le scope global : `num1` et `num2`. Jusqu'à présent, vous avez utilisé le mot-clé `var`. Si vous ne mettez rien à l'intérieur d'une IIFE et que vous restez simplement dans le scope global, vous ne verrez aucune closure dans le navigateur.

![No Closure In Global Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464484448/99a70a30-f07f-469d-a592-59f3ed5f193c.png align="left")

Mais où vivent `num1` et `num2` ? Eh bien, dans le scope global. C'est pourquoi vous écrivez `console.dir(sum)`. Dans le navigateur, vous pouvez voir `num1` et `num2` à l'intérieur de l'objet global.

Voici la partie intéressante : que se passe-t-il si vous remplacez ces mots-clés `var` par `let` ?

### Comprendre le Scoping de `var` et `let`

**Code complet :** `example-3.js`

```js
// example-3.js
let num1 = 2;
let num2 = 3;

function sum() {
    return num1 + num2;
}

console.log(sum());

console.dir(sum);
```

C'est là que la différence entre `var` et `let` entre en jeu. Beaucoup de gens pensent qu'ils sont identiques, mais en JavaScript, `var` et `let` ne sont pas égaux.

En termes simples :

* `var` est l'ancienne déclaration JavaScript, et elle est function-scoped. Une variable déclarée avec `var` ne vit qu'à l'intérieur de la fonction dans laquelle elle est définie. Si elle est définie en dehors de toute fonction, elle va dans le scope global.
    
* `let` est la nouvelle déclaration ES6, et elle est block-scoped. Une variable déclarée avec `let` n'existe qu'à l'intérieur du bloc ou du scope où elle a été définie et ne peut pas être accédée de l'extérieur.
    

Une différence importante est le hoisting. Les variables déclarées avec `var` sont hoistées, ce qui signifie que JavaScript déplace la déclaration vers le haut, mais l'initialisation n'a pas lieu. Donc, si vous utilisez un `var` avant qu'il ne soit déclaré, vous obtiendrez `undefined`. Avec `let`, même s'il est hoisté, la [temporal dead zone](https://www.freecodecamp.org/news/javascript-temporal-dead-zone-and-hoisting-explained/) garantit que son utilisation avant la déclaration lève une erreur.

### Observer la différence

Voyons ce qui se passe si vous déclarez la variable avec `let`. La dernière fois, quand elle était juste dans le scope global, vous pouviez voir les variables quand vous faisiez `console.dir`. Maintenant, cependant, vous voyez qu'un nouvel objet nommé `script` est apparu, et `num1` et `num2` ne sont plus dans le scope global.

![Let Scope Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464511845/d627b15b-8d03-48e2-ae11-3e3516cc760e.png align="left")

Pourquoi cela ? C'est à cause de la différence entre `let` et `var` dont vous avez parlé plus tôt. `let` est block-scoped, tandis que `var` est function-scoped. Si vous traitez le contexte extérieur comme une fonction principale, une variable déclarée avec `var` devient partie intégrante du scope global. Mais avec `let`, elle reste dans son block scope et ne devient pas directement partie de l'objet global. Ainsi, `let` vit en réalité à l'intérieur d'un objet séparé appelé `script` et non dans le scope global.

Comprendre cela est vraiment important, car si vous suivez ce guide et que vous essayez d'imprimer des variables tout en utilisant `let` par habitude, le résultat ne sera pas le même qu'avec `var`. Cela peut certainement être déroutant. En termes simples, `let` ne va pas dans l'objet global. Il existe à l'intérieur d'un objet `script` séparé.

### Utiliser IIFE avec `let`

**Code complet :** `example-3.js`

```js
// example-3.js
(function () {
    let num1 = 2;
    let num2 = 3;

    function sum() {
        return num1 + num2;
    }

    console.dir(sum);
})();
```

Mais que se passe-t-il si vous enveloppez à nouveau le tout dans une fonction englobante, comme auparavant avec une IIFE ? Lorsque vous vérifiez la sortie maintenant, tout retourne à l'intérieur de sa closure.

![Closure with Let in IIFE Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464534468/13f0579b-0476-47b4-a4b3-2d894b0e1570.png align="left")

En fin de compte, le concept de closures reste le même : ce qui change, c'est si la variable va dans le scope `var` ou `let`.

Maintenant, la situation devient un peu plus simple. Vous avez une fonction, et elle est dans son état de fermeture finale. Selon la définition d'une closure, la fonction interne de cette fonction utilise la variable extérieure `num1`. Donc, cette fonction interne a définitivement besoin d'une closure. Cette closure provient précisément de cette fonction.

JavaScript crée la closure et emballe `num1` à l'intérieur. Le monde global extérieur existe toujours séparément, bien sûr. Rappelez-vous également que lors de l'utilisation de `console.dir` dans le navigateur, la sortie aura un aspect différent selon que vous avez affaire à `let` ou `var`.

## Comprendre les Closures à travers l'exemple pratique d'un chronomètre

Jusqu'à présent, tous les exemples que vous avez vus étaient très simples. Voyons maintenant un exemple pratique qui vous aidera à mieux comprendre les closures et à dissiper toute confusion.

**Code complet :** `example-4.js`

```js
// example-4.js
function stopWatch() {
    var startTime = Date.now();

    var getDelay = function () {
        console.log(Date.now() - startTime);
    };
    return getDelay;
}

var timer = stopWatch();

for (let i = 0; i < 100000000; i++) {
    var a = Math.random() * 1000000;
}

timer();
```

### Définir la fonction Stopwatch

Définissons une fonction :

```javascript
function stopWatch() {}
```

Vous l'avez nommée `stopWatch`, et elle fonctionne exactement comme un vrai chronomètre. Tout comme lorsque vous lancez un chronomètre, attendez un moment, puis l'arrêtez pour obtenir le temps écoulé, cette fonction fera la même chose.

Tout d'abord, écrivez :

```javascript
var startTime = Date.now();
```

Cela stocke l'heure actuelle dans `startTime`. Ensuite, à l'intérieur de la fonction, définissez :

```javascript
var getDelay = function () {};
```

Créez une fonction `getDelay`, qui affichera le temps écoulé dans la console. Pour cela, écrivez :

```javascript
console.log(Date.now() - startTime);
```

Ici, le temps écoulé est calculé en soustrayant `startTime` de l'heure actuelle. Enfin, retournez simplement cette fonction `getDelay`. La fonction `stopWatch` ne fait qu'une chose : lorsque vous appelez `stopWatch`, elle démarre un chronomètre en utilisant `Date.now()` et retourne une fonction `getDelay`. Lorsque vous appelez cette fonction `getDelay`, elle affiche le temps écoulé entre l'heure de début et le moment actuel.

### Utiliser le chronomètre

Maintenant, appelez-la. Écrivez :

```javascript
var timer = stopWatch();
```

Ici, vous avez démarré le `stopWatch`. Cette fonction s'exécute, ce qui signifie que `startTime` est défini et que la fonction `getDelay` est définie. Ensuite, `stopWatch` retourne cette fonction `getDelay`. La fonction `stopWatch` elle-même n'est pas appelée directement par la suite – vous l'avez simplement appelée une fois, et la fonction extérieure retourne la fonction `getDelay`. Stockez cette fonction retournée dans `timer`.

À ce stade, le `stopWatch` est déjà en cours d'exécution car vous l'avez appelé, mais vous n'avez encore rien imprimé depuis `getDelay`. Avant d'appeler `getDelay`, créez un faux délai comme ceci :

```javascript
for (let i = 0; i < 100000000; i++) {}
```

Utilisez une grande boucle for pour perdre un peu de temps. Vous avez choisi un grand nombre intentionnellement pour qu'il y ait un délai notable. Si vous le souhaitez, vous pouvez également effectuer des opérations coûteuses dans la boucle, comme le calcul d'un nombre aléatoire :

```javascript
var a = Math.random() * 1000000;
```

Ainsi, vous créez un délai artificiel.

### Appeler la fonction Timer

Nous en venons maintenant à `timer`. `Timer` est en réalité une fonction car elle a été retournée par l'appel de `stopWatch`. Cette fonction `getDelay` retournée agit comme votre chronomètre réel. Appelons `timer()` et voyons ce qui se passe. Le résultat n'apparaît pas instantanément – cela prend un moment, puis il s'affiche. Vous obtenez donc un délai.

![Stopwatch Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464566077/f4a450a5-796b-4999-97cb-1e697afbbcfa.gif align="left")

La question est : comment cela fonctionne-t-il encore ? La fonction `stopWatch`, là où vous l'avez initialement appelée, a déjà fini de s'exécuter. Cela signifie que tout ce qui se trouve à l'intérieur de cette fonction devrait avoir disparu.

Alors, comment `timer()` connaît-il encore la valeur de `startTime` ? Surtout après avoir ajouté un délai aussi long avant de l'appeler ? Cela signifie que la fonction `timer` se souvient toujours de sa fonction parente – spécifiquement, de la variable `startTime` à l'intérieur de `stopWatch`. Elle conserve cette référence.

Comment ? Grâce à une closure. Lorsque `getDelay` a été créée, une closure a également été créée à l'intérieur d'elle, gardant la trace de la variable `startTime`. Ainsi, même après le délai, et même après un long moment, elle peut toujours utiliser cette ancienne valeur. Cela montre que JavaScript est vraiment intelligent. Il suit toutes les variables, références et closures, et quand c'est nécessaire, il peut les réutiliser. C'est pourquoi ce comportement est possible : grâce aux closures.

### Inspecter la fonction Timer

**Code complet :** `example-4.js`

```js
// example-4.js
function stopWatch() {
    var startTime = Date.now();
    var getDelay = function () {
        console.log(Date.now() - startTime);
    };
    return getDelay;
}

var timer = stopWatch();

for (let i = 0; i < 100000000; i++) {
    var a = Math.random() * 1000000;
}

timer();

console.dir(timer);
```

Si vous faites :

```javascript
console.dir(timer);
```

comme auparavant et que vous vérifiez la sortie dans le navigateur, vous remarquerez que cela prend un certain temps à apparaître à cause du délai. Mais même après le délai, elle conserve toujours `startTime` à l'intérieur de la closure.

![Timer Closure Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464588970/1dcb2502-4989-447f-9c4c-09056c948243.png align="left")

Si vous essayez :

```javascript
console.log(startTime);
```

vous ne pourrez pas accéder directement à `startTime`. Mais puisque `timer` est une fonction membre, elle peut utiliser ce `startTime` que vous avez initialisé il y a longtemps, avant la boucle for. Elle se souvient toujours de `startTime`. Peu importe la durée du délai, elle peut en garder la trace. Même s'il y avait plus de lignes de code ou des opérations plus coûteuses pendant le délai, au bout du compte, lorsque vous appelez le timer, la closure garantit que `startTime` est correctement préservé.

C'est l'un des aspects les plus fascinants de JavaScript : il peut réellement se souvenir de telles informations, et c'est l'un des plus grands cas d'utilisation des closures.

### Closures et Garbage Collection

C'est l'une des fonctionnalités les plus puissantes des closures. Grâce aux closures, peu importe le nombre de fois que vous appelez la fonction `timer()`, chaque appel fonctionne indépendamment et conserve sa propre référence. À chaque fois, une nouvelle référence est créée et conservée aussi longtemps qu'elle est nécessaire.

Considérons un petit exemple – mais imaginez que dans une grande application, il pourrait y avoir d'innombrables closures détenant des références à de nombreuses variables. Naturellement, la question se pose : si tant de choses sont mémorisées, les performances en souffriront-elles ?

C'est là qu'intervient l'optimisation des performances de JavaScript. **JavaScript est un langage intelligent avec Garbage Collection.** Cela signifie que lorsque JavaScript réalise qu'une référence ou une variable n'est plus nécessaire, il la supprime automatiquement de la mémoire.

Dans certaines situations, les programmeurs peuvent optimiser manuellement. Par exemple, si vous avez créé un timer détenant une référence à une fonction `getDelay()`, mais que vous n'avez pas encore appelé `getDelay()`, JavaScript ne sait pas si elle sera utilisée à l'avenir, il garde donc la référence.

**Code complet :** `example-4.js`

```js
// example-4.js
function stopWatch() {
    var startTime = Date.now();

    var getDelay = function () {
        console.log(Date.now() - startTime);
    };
    return getDelay;
}

var timer = stopWatch();

for (let i = 0; i < 100000000; i++) {
    var a = Math.random() * 1000000;
}

timer();

console.dir(timer);
timer = null;

timer();
```

Si vous êtes certain qu'elle ne sera plus utilisée, vous pouvez effacer manuellement la référence en écrivant :

```javascript
timer = null;
```

Maintenant, `timer()` ne fonctionnera plus car vous l'avez défini sur null. JavaScript comprend qu'il n'est plus nécessaire et effectue une Garbage Collection de la référence en mémoire. Si vous essayez cela dans le navigateur, vous verrez une erreur : "TypeError: timer is not a function" – parce que `timer` est maintenant null.

![Timer Null Error Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464662207/267dbda0-31c0-47b3-9df8-a6b18c04b317.png align="left")

En termes simples, définir `timer = null` dit à JavaScript : « Cette variable ne sera plus utilisée, oublie-la. » Le Garbage Collector reconnaît alors qu'il n'y a plus de références et la supprime discrètement de la mémoire, évitant ainsi le gaspillage de mémoire.

La partie intéressante est que JavaScript ne se contente pas d'exécuter le code – il prédit beaucoup de choses avant même la compilation. Lorsqu'il voit `timer = null`, il sait déjà : « D'accord, le programmeur n'a utilisé ce timer que jusque-là, et il ne sera plus nécessaire. » Ainsi, dès que le code a fini de s'exécuter, il nettoie intelligemment la mémoire.

Cela rend votre programme automatiquement optimisé. Il n'y a pas de fuites de mémoire, la charge du navigateur diminue et JavaScript s'exécute plus rapidement. C'est un tout petit exemple, mais il montre déjà avec quelle élégance vous pouvez gérer les performances en JavaScript.

## Les Closures dans le code asynchrone

Jusqu'à présent, tous les exemples que vous avez vus utilisaient les closures de manière synchrone. Maintenant, beaucoup de gens pourraient se demander : « D'accord, mais comment les closures fonctionnent-elles dans des situations asynchrones ? »

C'est une très bonne question. Dans le codage réel, la plupart des tâches s'exécutent de manière asynchrone – comme avec `setTimeout`, `fetch` ou des fonctions d'écoute d'événements. Le point clé est que le code synchrone s'exécute ligne par ligne, mais le code asynchrone prend un certain temps pour se terminer. Cela signifie que vous appelez une fonction, mais son résultat arrive un peu plus tard.

La question est donc : si le scope extérieur est déjà terminé d'ici là, comment la fonction interne se souvient-elle encore des valeurs des variables extérieures ?

**C'est exactement là que réside le véritable pouvoir des closures.** Une closure conserve la référence au scope extérieur tant que la fonction interne n'a pas encore été exécutée. Cela signifie que, que le code soit synchrone ou asynchrone, les closures fonctionnent de la même manière.

![Asynchronous Closures](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464732632/3d49dab4-4b0e-4f58-9923-fe5dae876915.gif align="left")

### Exemple asynchrone de base avec `setTimeout`

**Code complet :** `example-5.js`

```js
// example-5.js
function asyncExample() {
    var a = 20;

    setTimeout(function () {
        console.log(a);
    }, 3000);
}

asyncExample();
```

Voyons maintenant un petit exemple asynchrone pour comprendre comment fonctionnent les closures et pourquoi elles sont tout aussi fiables dans des scénarios asynchrones.

Définissez une fonction :

```javascript
function asyncExample() {}
```

À l'intérieur de cette fonction, écrivez :

```javascript
var a = 20;
```

Vous avez défini une variable. Ensuite, utilisez la fonction intégrée `setTimeout` de JavaScript :

```javascript
setTimeout(function () {});
```

`setTimeout` prend deux paramètres : l'un est la fonction à exécuter, et l'autre est le temps en millisecondes, ce qui signifie qu'il appellera cette fonction après le délai spécifié.

Maintenant, supposons que vous mettiez `console.log(a)` à l'intérieur de cette fonction. Étonnamment, même si `a` n'est pas défini à l'intérieur de la fonction timeout, elle peut toujours accéder au `a` du scope extérieur de `asyncExample`. C'est possible grâce aux closures. Après 3 secondes, il apparaît, et vous voyez `20`. C'est également possible grâce aux closures. La fonction à l'intérieur de `setTimeout` n'a pas de `a` défini en elle-même, pourtant elle peut accéder à `a` depuis le scope de `asyncExample`.

![Asynchronous Closure Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464763043/0d51130c-3299-49c1-bab9-6cac74b215ab.png align="left")

### Exemple de référence de fonction externe

**Code complet :** `example-5.js`

```js
// example-5.js
function asyncExample() {
    var a = 20;

    function myFunc() {
        console.log(a);
    }

    setTimeout(myFunc, 3000);
    console.dir(myFunc);
}

asyncExample();
```

Maintenant, que se passe-t-il si vous définissez la fonction `setTimeout` à l'extérieur de `asyncExample`, juste pour la démonstration – comme ceci :

```javascript
function myFunc() {}
```

À l'intérieur de `myFunc`, écrivez :

```javascript
console.log(a);
```

Ensuite, passez `myFunc` dans `setTimeout` et écrivez également :

```javascript
console.dir(myFunc);
```

Si vous vérifiez la sortie de `console.dir`, vous verrez qu'à l'intérieur de `myFunc`, la closure contient la variable `a=20`. C'est parce que `a` faisait partie du scope de `asyncExample`, donc `myFunc` peut toujours y accéder.

![Asynchronous Closure with External Function Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464809847/359fc698-cc18-4e41-beb7-e3b7148accc1.png align="left")

Tout comme auparavant, cela est possible grâce aux closures. Mais ici, il y a une subtile différence. Plus tôt, vous avez parlé d'un exemple de référence, mais cette référence fonctionne un peu différemment.

**Code complet :** `example-5.js`

```js
// example-5.js

var a = 20;

function asyncExample() {
    function myFunc() {
        console.log(a);
    }

    setTimeout(myFunc, 3000);
    console.dir(myFunc);
}

asyncExample();

a = 30;
```

Supposons que la variable `a=20` était à l'origine à l'intérieur de `asyncExample`. Maintenant, si vous déplacez `a` vers le scope global et écrivez :

```javascript
var a = 20;
```

En termes simples, vous l'avez définie à l'extérieur. Maintenant, la closure ne l'affichera pas, car elle fait partie du scope global. `a` existera simplement dans le scope global avec une valeur de `20`. Vous appelez la fonction `asyncExample`, qui démarre le timer `setTimeout`. Ensuite, à la ligne suivante après l'appel de `asyncExample`, vous changez la valeur de `a` :

```javascript
a = 30;
```

Maintenant, réfléchissez : si `myFunc` est appelée comme callback pour `setTimeout` et fait un `console.log(a)`, quelle valeur affichera-t-elle ? Si vous vérifiez la sortie, elle affichera `30`.

![Global Variable Asynchronous Closure Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464836227/3d4cc9aa-cd26-4026-bc14-2d0b980bc333.png align="left")

Qu'est-ce que cela signifie ?

Lorsque `asyncExample` est appelée, le `setTimeout` démarre et `myFunc` est prête en tant que callback. À l'intérieur de `myFunc`, vous avez `console.log(a)`. À ce moment-là, `a` était `20` dans son scope parent. Mais puisque `a` est maintenant global et que sa valeur a été modifiée de l'extérieur, lorsque le callback s'exécute, il affiche `30`.

Cela démontre que **les closures détiennent en réalité une référence à la variable.** Si la variable est globale, tout changement externe est également suivi. Ainsi, si vous développez le `a` global dans la console, vous verrez `a = 30`.

J'ai mentionné plus tôt que les closures gardent une référence à la valeur. Ainsi, lorsque `setTimeout` envoie le callback au main thread après 3 secondes, `myFunc` peut toujours accéder à cette référence. Rappelez-vous, `myFunc` revient via `setTimeout` d'un autre endroit – elle ne s'exécute pas directement sur le main thread. Cela fait partie du JavaScript asynchrone.

La fonction est appelée dans le main thread après être revenue de la Web API, mais elle conserve toujours la référence à `a`. Puisque `a` a été modifié globalement, lorsque `myFunc` l'imprime, elle affiche la nouvelle valeur `30`.

Ce point est très important. Pratiquer plusieurs exemples vous aidera à mieux comprendre comment les closures suivent les variables extérieures dans des situations asynchrones. C'est pourquoi vous devez être prudent lorsque vous utilisez des variables globales et `var`.

C'est aussi la raison pour laquelle `var` peut parfois causer des conflits, et pourquoi le mot-clé `let` a été introduit. Par exemple, si vous définissez `var a` globalement et que vous changez plus tard `a` quelque part dans le programme, toutes les fonctions asynchrones référençant `a` utiliseront la nouvelle valeur. C'est pourquoi l'utilisation de `var` avec `setTimeout` ou d'autres fonctions asynchrones peut entraîner de tels problèmes.

💡Un point important est qu'une closure ne garde pas la variable entière de son scope parent. Elle ne garde qu'une référence à cette variable.

## Exemple pratique : requêtes API avec les Closures

Voyons maintenant un autre exemple pratique de closures. Dans les applications JavaScript typiques, vous effectuez souvent des requêtes AJAX pour récupérer des données à partir d'une URL d'API. Nous allons voir comment les closures sont utilisées dans ce contexte. Pour des requêtes API comme celle-ci, la fonction intégrée `fetch` de JavaScript peut être utilisée, bien que des bibliothèques tierces comme `axios` ou `jQuery AJAX` puissent également accomplir la même tâche.

**Code complet :** `example-6.js`

```js
// example-6.js

function apiFunction(url) {
    fetch(url).then((res) => {
        console.log(res);
    });
}

apiFunction("https://jsonplaceholder.typicode.com/todos/1");
```

Ici, nous allons utiliser `fetch` pour un exemple pratique. Tout d'abord, écrivez une fonction :

```javascript
function apiFunction(url) {}
```

Vous l'avez nommée `apiFunction` et lui avez donné un paramètre appelé `url`. Cette fonction enverra une requête à cette URL. Ensuite, vous appelez la fonction intégrée `fetch` :

```javascript
fetch(url);
```

Alors, que fait `fetch` avec l'URL ? Fondamentalement, `fetch` retourne une promise. Vous savez que pour obtenir le résultat d'une promise, vous utilisez `then`. Vous écrivez donc :

```javascript
.then((res)=>{})
```

Une fois la réponse revenue, vous utilisez une fonction callback. Ici, vous affichez la réponse dans la console :

```javascript
console.log(res);
```

C'est ainsi que votre `apiFunction` est configurée.

Maintenant, appelez la fonction. Vous devez passer une URL pour l'appel API. Un choix populaire est [jsonplaceholder](https://jsonplaceholder.typicode.com/), utilisez donc son endpoint `/todos/1` :

```javascript
apiFunction("https://jsonplaceholder.typicode.com/todos/1");
```

Vérifiez le résultat. Remarquez qu'il apparaît après un court délai – c'est asynchrone.

![API Function Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464859727/39dd7757-f04e-49f2-ac8a-46f2472a429e.png align="left")

Pour rendre cela plus clair, écrivez une autre ligne en dessous :

```javascript
console.log("I am here");
```

Maintenant, la question est : laquelle s'imprime en premier ? Sans aucun doute, "I am here" s'imprime en premier, puis le résultat de `apiFunction` apparaît. Cela démontre clairement le flux des opérations asynchrones. Comme la réponse arrive rapidement, cela n'aurait peut-être pas été évident sans cette ligne supplémentaire.

![API Function with Log Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464881162/59208d49-83f9-48af-8ab4-c9d1c453356b.png align="left")

Qu'est-ce que cela signifie ? Le résultat arrive, n'est-ce pas ? Ici, le lien avec les closures est que vous avez passé le paramètre `url` de l'extérieur lors de l'appel de `apiFunction`. Cet `url` existe maintenant à l'intérieur du corps de `apiFunction`. `fetch` le prend comme paramètre, puis la fonction callback à l'intérieur de `then` s'exécute beaucoup plus tard.

À ce moment-là, l'appel à `apiFunction` est déjà terminé, mais le callback se souvient toujours des variables de son scope. C'est pourquoi même après l'arrivée du résultat, vous pouvez toujours accéder à `url`. Pour le voir, imprimez-le :

```javascript
console.log(url);
```

Remarquez que le résultat est correct. Cela signifie que s'il y avait plus de fonctions imbriquées à l'intérieur de `then`, comme un autre `then` à l'intérieur d'un `then`, tout au long de la chaîne, la fonction la plus interne pourrait toujours accéder à l'original `url`. Et cela n'est possible que grâce aux closures.

![API Function URL Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464901905/8980f4a3-3eb9-4af1-868f-d3ef6d907e9b.png align="left")

### Refactorisation avec une fonction externe

**Code complet :** `example-6.js`

```js
// example-6.js

function apiFunction(url) {
    handleResponse = function (res) {
        console.log(res);
        console.log(url);
    };

    fetch(url).then(handleResponse);
    console.dir(handleResponse);
}

apiFunction("https://jsonplaceholder.typicode.com/todos/1");
```

Pour faire une démonstration, réécrivons un peu différemment la fonction callback à l'intérieur de `apiFunction` :

```javascript
function handleResponse(res) {}
```

Cette fonction fait simplement `console.log(url)`. Maintenant, passez `handleResponse` dans le `then`. Ensuite, écrivez :

```javascript
console.dir(handleResponse);
```

Dans la sortie, vous verrez qu'à l'intérieur de `handleResponse`, la closure contient `url`. C'est parce qu'il faisait partie du scope de `apiFunction`, il peut donc y accéder.

![API Function with External Handler Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464922631/3a2edbeb-d3e9-470d-bea3-fdf46144165e.png align="left")

## Exemple avancé - Les Closures dans les boucles

Enfin, examinons un autre exemple qui revient souvent dans les entretiens d'embauche. Celui-ci est un peu plus complexe et délicat, et il montre comment l'utilisation de closures à l'intérieur de boucles peut créer des résultats imprévisibles.

### Exemple de boucle synchrone

**Code complet :** `example-7.js`

```js
// example-7.js

for (let i = 0; i < 3; i++) {
    function a() {
        console.log(i);
    }
    a();
}
```

Écrivons une boucle for simple :

```javascript
for (let i = 0; i < 3; i++) {}
```

Cette boucle s'exécutera trois fois, et à l'intérieur, nous définirons une autre fonction :

```javascript
function a() {}
```

À l'intérieur de cette fonction, vous faites simplement :

```javascript
console.log(i);
```

De là, vous voyez que la fonction `a` existe dans le scope de la `boucle for`, mais en réalité, elle est également accessible dans le scope global. Ensuite, vous appelez la fonction `a` :

```javascript
a();
```

Le résultat attendu serait 0, 1, 2. Tout d'abord, la valeur de `i` affiche 0, puis 1, puis 2 – l'un après l'autre. En regardant la sortie, vous voyez 0, 1, 2. C'est parce que vous avez défini `i` en utilisant `let`.

![Synchronous Loop Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763464949327/23ded10a-19c2-4aff-9d11-927e179c2c82.png align="left")

**Code complet :** `example-7.js`

```js
// example-7.js

for (var i = 0; i < 3; i++) {
    function a() {
        console.log(i);
    }
    a();
}
```

Si vous supprimez `let` et utilisez `var` à la place, que se passe-t-il ? Même avec `var`, le résultat sera le même dans ce cas simple car `var` fonctionne en dehors du block scope. Écrire `for (var i = 0)` ou déclarer `var i` séparément se comporte effectivement de la même manière.

```js
// example-7.js

var i;
for (i = 0; i < 3; i++) {
    function a() {
        console.log(i);
    }
    a();
}
```

Ainsi, dans ce cas, il n'y a pas de problème. Une closure n'est pas requise car vous exécutez la fonction dans le scope global. Votre `i` affiche 0, puis 1, puis 2, et tout fonctionne correctement.

### Exemple de boucle asynchrone

**Code complet :** `example-7.js`

```js
// example-7.js

for (let i = 0; i < 3; i++) {
    setTimeout(function () {
        console.log(i);
    }, 1000 * i);
}

console.log("After for loop");
```

Revenons maintenant en arrière et utilisons à nouveau `let` pour `i`. Supposons que vous vouliez appeler la fonction `a` depuis l'extérieur de la boucle. Imaginez que vous enveloppiez l'appel de la fonction dans un `setTimeout`, et que dans le premier paramètre vous passiez le corps de `a` comme callback, tandis que le second paramètre est `1000 * i` millisecondes.

En utilisant ce `1000 * i`, vous voulez que 0 s'affiche après 1 seconde, 1 après 2 secondes et 2 après 3 secondes. Lorsque vous exécutez cela, le résultat arrive exactement comme prévu : après 1 seconde, 0 s'affiche ; après 2 secondes, 1 s'affiche ; et après 3 secondes, 2 s'affiche.

Mais voici le point important : la boucle `for` elle-même est synchrone, tandis que les fonctions à l'intérieur de `setTimeout` sont asynchrones. Cela signifie que les fonctions à l'intérieur de `setTimeout` s'exécuteront une par une selon le timer, seulement après la fin de la boucle. D'abord après 1 seconde, puis après 2, puis après 3.

Vous pouvez vérifier ce comportement asynchrone. Supposons qu'à la fin de la boucle vous écriviez :

```javascript
console.log("After for loop");
```

Maintenant, si vous vérifiez la sortie, "After for loop" s'imprime en premier, puis après 1 seconde, 0 s'imprime, après 2 secondes, 1 s'imprime, et enfin 2 s'imprime. Cela montre clairement comment les fonctions asynchrones s'exécutent, n'est-ce pas ? Pas de confusion là-bas.

![Asynchronous Loop Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465056351/9ca676db-c54a-4dc2-9ac8-0bbf1cf08be4.gif align="left")

### Le problème `var` vs `let`

**Code complet :** `example-7.js`

```js
// example-7.js

for (var i = 0; i < 3; i++) {
    setTimeout(function () {
        console.log(i);
    }, 1000 * i);
}
console.log("After for loop");
```

Voyons maintenant ce qui se passe si vous remplacez `let i` par `var i`. La partie intéressante est que si vous utilisez "var i" au lieu de "let i", le comportement change. Les trois sorties finissent par être 3. Vous n'obtenez pas 0, 1, 2 comme auparavant. C'est exactement la partie délicate de cette question.

![Var Loop Problem Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465090022/87518cc5-4942-4c2e-a728-a11751d9a552.png align="left")

Cette question revient souvent dans les entretiens d'embauche car elle est un peu avancée, mais si vous comprenez les closures et la différence entre les scopes `let` et `var`, ce n'est pas compliqué du tout. Vous pouvez analyser cela en revenant à `let`. Supprimez `var` et écrivez :

```javascript
let i = 0;
```

Maintenant, le résultat attendu est 0, 1, 2. `let` est block-scoped, ce qui signifie que ce `i` n'existe qu'à l'intérieur de la boucle et n'a aucun effet à l'extérieur.

![Let Loop Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465164777/ba0b0084-95db-4de5-a1e6-67aaa8172c51.gif align="left")

Lors de la première itération, `i` est 0, et la fonction `setTimeout` est définie. Cette fonction sera appelée après la fin de la boucle, donc une closure est utilisée pour se souvenir de la valeur de i. Le callback a besoin d'une closure pour référencer i correctement. Puisque `let` ne fuit pas en dehors de la boucle, chaque itération crée un nouveau i. Par exemple, quand i devient 1, c'est un `i` complètement séparé de l'itération précédente.

**Code complet :** `example-7.js`

```js
// example-7.js

var i;

for (i = 0; i < 3; i++) {
    setTimeout(function () {
        console.log(i);
    }, 1000 * i);
}
console.log(i);
console.log("After for loop");
```

Ainsi, lorsque cette fonction s'exécute la deuxième fois, elle référence ce nouveau i. Mais avec `var`, la situation est différente. `var` est function-scoped, donc la même variable existe en dehors de la boucle. Si vous écrivez :

```javascript
var i;
```

et que vous utilisez ensuite la boucle :

```javascript
for (i = 0; i < 3; i++) {}
```

il n'y a qu'un seul i. Changer i à l'intérieur de la boucle modifie le même i – aucun nouveau i n'est créé. Ainsi, lorsque les callbacks setTimeout s'exécutent, ils référencent tous ce même i. D'après les exemples précédents, vous savez que les callbacks setTimeout s'exécutent après la fin de la boucle. Or, après la fin de la boucle, quelle est la valeur de i ? Puisque vous avez utilisé `var`, i est devenu 3.

Vérifiez-le avec :

```javascript
console.log(i);
```

Dans la console, vous verrez 3 s'imprimer en premier. Cela signifie que lorsque les callbacks s'exécutent, ils référencent tous le même i, qui est déjà 3.

![Var Loop Problem with Log Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465201159/7730557a-5255-4c32-8f46-ca01c11a6899.png align="left")

Ainsi, chaque console.log dans les callbacks affiche i = 3, ce qui explique parfaitement le résultat.

### Utiliser `console.dir` avec les Closures de boucle

**Code complet :** `example-7.js`

```js
// example-7.js

// var i;

for (let i = 0; i < 3; i++) {
    function myFunc() {
        console.log(i);
    }

    setTimeout(myFunc, 1000 * i);

    console.dir(myFunc);
}

console.log("After for loop");
```

Pour encore mieux comprendre cela, vous pouvez utiliser "console.dir" comme auparavant.

Voyons comment. Tout d'abord, vous resterez sur le cas `let`. Donc, dans la boucle for, vous écrivez :

```javascript
let i = 0;
```

Vous commentez le "var i;" global puisque `let` est block-scoped. Voyons maintenant comment fonctionne la closure. La closure est créée à l'intérieur de la fonction callback setTimeout, et vous voulez inspecter cette fonction callback.

Pour cela, vous définissez :

```javascript
function myFunc() {}
```

et passez ce myFunc à l'intérieur de setTimeout. Ensuite, pour l'inspecter, écrivez :

```javascript
console.dir(myFunc);
```

Si vous exécutez cela, le navigateur affiche le même résultat. Cela signifie que le dir de myFunc apparaît trois fois, mais dans la console de Chrome, il ne s'imprime qu'une seule fois. Chrome regroupe les objets similaires, donc même si les propriétés internes sont différentes, il ne les affiche pas séparément. Pour voir chaque propriété individuellement, passez à l'étape suivante.

![Let Loop with Dir Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465312812/f4ec260c-2b8f-474f-a1ad-59797eda63d4.gif align="left")

Sous le dir, écrivez :

```javascript
console.log("---");
```

Cela agit comme un séparateur. Maintenant, lorsque le navigateur imprime le dir de myFunc, il imprime également le séparateur, ce qui montre clairement que chaque instance est séparée.

En même temps, en dehors de la boucle for, ajoutez :

```javascript
console.log("After for loop");
```

Maintenant, si vous vérifiez la sortie, le navigateur affiche d'abord 'After for loop', puis 0, 1, 2. Lorsque vous l'avez défini, les logs de la console affichent myFunc et les tirets.

![Let Loop with Dir and Separator Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465334580/a92fd163-4095-4b6a-bdb5-f239350a7416.png align="left")

Remarquez que lorsque i est 0, la closure contient i = 0. Lorsque i = 1, la closure contient i = 1. Lorsque i = 2, la closure contient i = 2. Ainsi, les trois valeurs existent en tant que références jusqu'à la fin, c'est pourquoi vous obtenez trois sorties distinctes.

![Let Loop Closure Values Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465373352/5e8903fa-76c4-4031-9a09-d45e9cd29e5f.gif align="left")

### Le problème de la boucle `var`

**Code complet :** `example-7.js`

```js
// example-7.js

for (var i = 0; i < 3; i++) {
    function myFunc() {
        console.log(i);
    }

    setTimeout(myFunc, 1000 * i);

    console.dir(myFunc);

    console.log("---");
}

console.log("After for loop");

console.log(i);
```

Mais que se passe-t-il si vous remplacez `"let i"` par `"var i"` ? Après avoir imprimé `'After for loop'`, les trois sorties affichent 3. Comment ? Lorsque i est 0, il n'y a pas de closure car var déplace cette variable vers le scope global. Contrairement à l'exemple précédent, aucune closure n'est nécessaire ici. Var existe dans le scope global, et i change au sein de cette même variable globale.

![Var Loop with Dir Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465417027/24635534-867e-4b9d-a4cf-637abbd4610c.png align="left")

Ainsi, si vous développez le premier myFunc dans la console et cherchez i dans le scope global, vous verrez i = 3. Pourquoi ? Parce que la boucle for se termine en premier, et à la fin, i devient 3. Au moment de `'After for loop'`, i est 3. Si vous faites "console.log(i)" à cet endroit, le navigateur affiche 3. Cela signifie que lorsque les valeurs de référence sont appelées, elles utilisent toujours la référence à ce i. Même si i change plus tard dans le programme, puisque les appels ont lieu après, les valeurs de référence obtiennent le i mis à jour.

C'est pourquoi le premier appel affiche 3, le deuxième appel affiche 3 et le troisième appel affiche également 3. Si vous les développez tous, vous verrez i = 3 partout. Cela se produit car aucune closure n'est utilisée ici ; il référence le i d'origine dans le scope global, qui continue de se mettre à jour.

![Var Loop Closure Values Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465457673/56530a97-5bd4-4f67-9311-77655b9638cb.gif align="left")

La différence de scope entre let et var est la raison pour laquelle le résultat change complètement.

### Corriger le problème de la boucle `var` avec IIFE

Pour corriger ce problème de var, vous pouvez créer une IIFE à l'intérieur de la boucle for. Cette IIFE prendra un paramètre : dans ce cas, la valeur de votre variable de boucle "i".

**Code complet :** `example-7.js`

```js
// example-7.js

for (var i = 0; i < 3; i++) {
    (function (i) {
        function myFunc() {
            console.log(i);
        }

        setTimeout(myFunc, 1000 * i);

        console.dir(myFunc);

        console.log("---");
    })(i);
}

console.log("After for loop");
```

Vous écrivez le code. À l'intérieur de l'IIFE, vous passez un paramètre nommé "i". Bien sûr, vous pouvez le nommer comme vous le souhaitez – vous le savez déjà. Mais pour l'instant, gardez-le comme "i". Ensuite, lorsque vous appelez l'IIFE, passez la valeur "i" de la boucle à l'intérieur. Sympa, non ?

Voyons à quoi ressemble la sortie. Cette fois, vous obtenez 0, 1 et 2 correctement. Alors, pourquoi est-ce corrigé maintenant ? Parce que "i" est maintenant à l'intérieur de son propre scope au sein de l'IIFE. Chaque fois que vous passez "i" à myFunc, une copie séparée de ce "i" est créée en tant que paramètre à l'intérieur de myFunc, et c'est cette copie qui est utilisée à l'intérieur de la fonction.

![IIFE Loop with Dir Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465482476/0939504b-40c4-4b9c-b698-a55f266f24c4.gif align="left")

Tout est clair maintenant, n'est-ce pas ? Si vous développez les dirs à la fin, vous verrez : le dernier a "i = 2" dans sa closure, le deuxième a "i = 1" et le premier a "i = 0". Parfaitement clair, n'est-ce pas ?

![IIFE Loop Closure Values Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1763465516842/0c708a0d-f0c6-44de-828e-61827375ecc1.gif align="left")

## Résumé et points clés

Si vous avez une solide compréhension des concepts globaux abordés ici, et si vous pratiquez tous ces exemples à plusieurs reprises, votre compréhension des closures deviendra beaucoup plus forte.

Bien sûr, il existe des exemples plus complexes de closures, mais les bases que nous avons couvertes aujourd'hui sont les plus importantes. Une fois que vous les aurez comprises étape par étape, vous pourrez créer vous-même de nombreux cas d'utilisation et le débogage ne sera plus difficile. Car maintenant, d'un simple coup d'œil à `console.dir()` ou en jouant un peu avec le code, vous pouvez voir comment les closures fonctionnent réellement.

Ne pas avoir une bonne compréhension des closures peut vous bloquer dans de nombreuses parties de JavaScript, en particulier lorsque vous travaillez avec du code asynchrone.

### Pour résumer :

Si l'on vous demande lors d'un entretien d'embauche : « Qu'est-ce qu'une Closure ? », vous pouvez répondre simplement :

> Une closure est un mécanisme par lequel une fonction se souvient des variables situées en dehors de son propre scope et peut y accéder chaque fois que nécessaire.

En d'autres termes, des valeurs qui ne sont pas à l'intérieur de la fonction elle-même, mais la fonction en prend une référence depuis son scope parent ou extérieur. C'est ce que nous appelons une Closure.

**Closure = Fonction + Valeurs mémorisées**

C'est pourquoi les closures sont si importantes dans les entretiens d'embauche. Elles montrent à quel point un programmeur comprend JavaScript en profondeur. Un programmeur qui comprend les closures peut clairement saisir le comportement interne de JavaScript, la gestion de la mémoire et le flux asynchrone.

### L'importance des Closures

JavaScript a été créé à l'origine pour de petites tâches interactives dans le navigateur, mais vous pouvez désormais créer des applications à grande échelle, même des systèmes backend, avec lui. La raison en est les concepts puissants de JavaScript tels que les Closures, les Prototypes, et plus encore.

Beaucoup de gens disent : « Je connais var, let, const, alors parlez-moi des closures. » Mais comme vous l'avez vu, var, let et const ne sont pas si simples non plus. C'est là que commence la compréhension des closures.

## Mots de la fin

Nous avons couvert beaucoup de choses dans ce guide ! Si la lecture de tout cela en une seule fois vous semble écrasante, vous pouvez le diviser en parties et le lire étape par étape. J'ai essayé d'expliquer tout le sujet très simplement, pièce par pièce. S'il y a des domaines qui pourraient être plus clairs, j'apprécie vos commentaires. Mais une fois que vous aurez vraiment compris et digéré ces informations, vous ne devriez plus jamais être intimidé par le mot "Closure".

Vous pouvez trouver tout le code source de ce tutoriel dans ce [dépôt GitHub](https://github.com/logicbaselabs/understanding-closure/). S'il vous a aidé d'une manière ou d'une autre, envisagez de lui donner une étoile pour montrer votre soutien !

Si vous avez trouvé les informations ici précieuses, n'hésitez pas à les partager avec d'autres personnes qui pourraient en bénéficier. J'apprécierais vraiment vos réflexions – mentionnez-moi sur X [@sumit\_analyzen](https://x.com/sumit_analyzen) ou sur Facebook [@sumit.analyzen](https://www.facebook.com/sumit.analyzen), [regardez](https://www.youtube.com/@logicBaseLabs) mes tutoriels de codage, ou [connectez-vous simplement avec moi](https://www.linkedin.com/in/sumitanalyzen/) sur LinkedIn. Vous pouvez également consulter mon site officiel [sumitsaha.me](https://www.sumitsaha.me) pour plus de détails sur moi.