---
title: Try/Catch en JavaScript – Comment gérer les erreurs en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-30T16:59:00.000Z'
originalURL: https://freecodecamp.org/news/try-catch-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/neo-urban-1734495_1920-1.jpg
tags:
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
seo_title: Try/Catch en JavaScript – Comment gérer les erreurs en JS
seo_desc: "By Fakorede Damilola\nBugs and errors are inevitable in programming. A\
  \ friend of mine calls them unknown features :). \nCall them whatever you want,\
  \ but I honestly believe that bugs are one of the things that make our work as programmers\
  \ interesting. \n..."
---

Par Fakorede Damilola

Les bugs et les erreurs sont inévitables en programmation. Un ami à moi les appelle des **fonctionnalités inconnues** :).

Appelez-les comme vous voulez, mais je crois honnêtement que les bugs sont l'une des choses qui rendent notre travail en tant que programmeurs intéressant.

Je veux dire, peu importe à quel point vous pourriez être frustré en essayant de déboguer du code toute la nuit, je suis assez sûr que vous aurez un bon fou rire lorsque vous découvrirez que le problème était une simple virgule que vous avez négligée, ou quelque chose comme ça. Bien que, une erreur signalée par un client provoquera plus une grimace qu'un sourire.

Cela dit, les erreurs peuvent être ennuyeuses et un vrai casse-tête. C'est pourquoi dans cet article, je veux expliquer quelque chose appelé **try / catch** en JavaScript.

## Qu'est-ce qu'un bloc try/catch en JavaScript ?

Un bloc **try / catch** est essentiellement utilisé pour gérer les erreurs en JavaScript. Vous l'utilisez lorsque vous ne voulez pas qu'une erreur dans votre script interrompe votre code.

Bien que cela puisse ressembler à quelque chose que vous pouvez facilement faire avec une **instruction if**, try/catch vous offre de nombreux avantages au-delà de ce qu'une instruction if/else peut faire, dont certains que vous verrez ci-dessous.

```
try{
//...
}catch(e){
//...
}
```

Une instruction try vous permet de tester un bloc de code pour les erreurs.

Une instruction catch vous permet de gérer cette erreur. Par exemple :

```
try{ 
getData() // getData n'est pas défini 
}catch(e){
alert(e)
}
```

C'est essentiellement comment un try/catch est construit. Vous placez votre code dans le **bloc try**, et immédiatement s'il y a une erreur, JavaScript donne à l'instruction **catch** le contrôle et elle fait simplement ce que vous dites. Dans ce cas, elle vous alerte de l'erreur.

Toutes les erreurs JavaScript sont en fait des objets qui contiennent deux propriétés : le nom (par exemple, Error, syntaxError, etc.) et le message d'erreur réel. C'est pourquoi lorsque nous alertons **e**, nous obtenons quelque chose comme **ReferenceError: getData n'est pas défini**.

Comme tout autre objet en JavaScript, vous pouvez décider d'accéder aux valeurs différemment, par exemple **e.name**(ReferenceError) et **e.message**(getData n'est pas défini).

Mais honnêtement, cela n'est pas vraiment différent de ce que JavaScript fera. Bien que JavaScript vous respectera assez pour logger l'erreur dans la console et ne pas montrer l'alerte au monde entier :).

Quel est donc l'avantage des instructions try/catch ?

## Comment utiliser les instructions try/catch

### L'instruction `throw`

L'un des avantages de try/catch est sa capacité à afficher votre propre erreur personnalisée. Cela s'appelle **`(throw error)`**.

Dans des situations où vous ne voulez pas de cette chose laide que JavaScript affiche, vous pouvez lancer votre erreur (une exception) avec l'utilisation de l'**instruction throw**. Cette erreur peut être une chaîne, un booléen ou un objet. Et s'il y a une erreur, l'instruction catch affichera l'erreur que vous lancez.

```
let num =prompt("insérer un nombre supérieur à 30 mais inférieur à 40")
try { 
if(isNaN(num)) throw "Ce n'est pas un nombre (☉﹃☉)!" 
else if (num>40) throw "Avez-vous même lu les instructions (ಠﭛಠ), inférieur à 40"
else if (num <= 30) throw "Supérieur à 30 (ب_ب)" 
}catch(e){
alert(e) 
}
```

C'est bien, non ? Mais nous pouvons aller plus loin en lançant une erreur avec les erreurs du constructeur JavaScript.

En gros, JavaScript catégorise les erreurs en six groupes :

* **EvalError** - Une erreur s'est produite dans la fonction eval.
* **RangeError** - Un nombre hors de portée s'est produit, par exemple `1.toPrecision(500)`. `toPrecision` donne essentiellement aux nombres une valeur décimale, par exemple 1.000, et un nombre ne peut pas en avoir 500.
* **ReferenceError** - Utilisation d'une variable qui n'a pas été déclarée
* **syntaxError** - Lors de l'évaluation d'un code avec une erreur de syntaxe
* **TypeError** - Si vous utilisez une valeur qui est en dehors de la plage des types attendus : par exemple `1.toUpperCase()`
* **URI (Uniform Resource Identifier) Error** - Une URIError est lancée si vous utilisez des caractères illégaux dans une fonction URI.

Ainsi, avec tout cela, nous pourrions facilement lancer une erreur comme `throw new Error("Salut")`. Dans ce cas, le nom de l'erreur sera **Error** et le message **Salut**. Vous pourriez même créer votre propre constructeur d'erreur personnalisé, par exemple :

```
function CustomError(message){ 
this.value ="customError";
this.message=message;
}
```

Et vous pouvez facilement utiliser cela n'importe où avec `throw new CustomError("data n'est pas défini")`.

Jusqu'à présent, nous avons appris à connaître try/catch et comment il empêche notre script de mourir, mais cela dépend en réalité. Considérons cet exemple :

```
try{ 
console.log({{}}) 
}catch(e){ 
alert(e.message) 
} 
console.log("Cela devrait s'exécuter après les détails loggés")
```

Mais lorsque vous l'essayez, même avec l'instruction try, cela ne fonctionne toujours pas. Cela est dû au fait qu'il existe deux principaux types d'erreurs en JavaScript (ce que j'ai décrit ci-dessus - syntaxError et ainsi de suite - ne sont pas vraiment des types d'erreurs. Vous pouvez les appeler des exemples d'erreurs) : **les erreurs de parse-time** et **les erreurs d'exécution ou exceptions**. 

Les **erreurs de parse-time** sont des erreurs qui se produisent à l'intérieur du code, essentiellement parce que le moteur ne comprend pas le code.

Par exemple, ci-dessus, JavaScript ne comprend pas ce que vous voulez dire par **{{}}**, et à cause de cela, votre try / catch n'a aucune utilité ici (il ne fonctionnera pas).

D'autre part, les **erreurs d'exécution** sont des erreurs qui se produisent dans un code valide, et ce sont les erreurs que try/catch trouvera sûrement.

```
try{ 
y=x+7 
} catch(e){ 
alert("x n'est pas défini")
} 
alert("Pas besoin de s'inquiéter, try catch gérera cela pour empêcher votre code de se casser")
```

Croyez-le ou non, ce qui précède est un code valide et le try /catch gérera l'erreur de manière appropriée.

### L'instruction `Finally`

L'instruction **finally** agit comme un terrain neutre, le point de base ou le terrain final pour votre bloc try/ catch. Avec finally, vous dites essentiellement **peu importe ce qui se passe dans le try/catch (erreur ou pas d'erreur), ce code dans l'instruction finally devrait s'exécuter**. Par exemple :

```
let data=prompt("nom")
try{ 
if(data==="") throw new Error("data est vide") 
else alert(`Salut ${data} comment allez-vous aujourd'hui`) 
} catch(e){ 
alert(e) 
} finally { 
alert("bienvenue dans l'article try catch")
}
```

### Imbrication des blocs try

Vous pouvez également imbriquer des blocs try, mais comme toute autre imbrication en JavaScript (par exemple if, for, etc.), cela tend à devenir maladroit et illisible, donc je déconseille. Mais c'est juste moi.

L'imbrication des blocs try vous donne l'avantage d'utiliser une seule instruction catch pour plusieurs instructions try. Bien que vous puissiez également décider d'écrire une instruction catch pour chaque bloc try, comme ceci :

```
try { 
try { 
throw new Error('oops');
} catch(e){
console.log(e) 
} finally { 
console.log('finally'); 
} 
} catch (ex) { 
console.log('outer '+ex); 
}
```

Dans ce cas, il n'y aura aucune erreur du bloc try externe car rien ne va avec lui. L'erreur provient du bloc try interne, et il s'en occupe déjà lui-même (il a sa propre instruction catch). Considérez ceci ci-dessous :

```
try { 
try { 
throw new Error('erreur de catch interne'); 
} finally {
console.log('finally'); 
} 
} catch (ex) { 
console.log(ex);
}
```

Ce code ci-dessus fonctionne un peu différemment : l'erreur se produit dans le bloc try interne sans instruction catch mais avec une instruction finally.

Notez que **try/catch** peut être écrit de trois manières différentes : `try...catch`, `try...finally`, `try...catch...finally`), mais l'erreur est lancée à partir de ce try interne.

L'instruction finally pour ce try interne fonctionnera définitivement, car comme nous l'avons dit plus tôt, elle fonctionne peu importe ce qui se passe dans try/catch. Mais même si le try externe n'a pas d'erreur, le contrôle est toujours donné à son catch pour logger une erreur. Et encore mieux, il utilise l'erreur que nous avons créée dans l'instruction try interne car l'erreur provient de là.

Si nous devions créer une erreur pour le try externe, il afficherait toujours l'erreur interne créée, sauf si l'interne attrape sa propre erreur.

Vous pouvez jouer avec le code ci-dessous en commentant le catch interne.

```
try { 
try { 
throw new Error('erreur de catch interne');
} catch(e){ //comment this catch out
console.log(e) 
} finally { 
console.log('finally'); 
} 
throw new Error("erreur de catch externe") 
} catch (ex) { 
console.log(ex);
}
```

### L'erreur de relancement

L'instruction catch attrape en fait toutes les erreurs qui viennent à elle, et parfois nous ne voulons pas cela. Par exemple,

```
"use strict" 
let x=parseInt(prompt("entrez un nombre inférieur à 5")) 
try{ 
y=x-10 
if(y>=5) throw new Error(" y n'est pas inférieur à 5") 
else alert(y) 
}catch(e){ 
alert(e) 
}
```

Supposons une seconde que le nombre saisi sera inférieur à 5 (le but de **"use strict"** est d'indiquer que le code doit être exécuté en "mode strict"). Avec le **mode strict**, vous ne pouvez pas, par exemple, utiliser des variables non déclarées ([source](https://www.w3schools.com/)).

Je veux que l'instruction try lance une erreur de **y n'est pas...** lorsque la valeur de y est supérieure à 5 ce qui est proche de l'impossible. L'erreur ci-dessus devrait être pour **y n'est pas inférieur...** et non **y est indéfini**.

Dans des situations comme celle-ci, vous pouvez vérifier le nom de l'erreur, et si ce n'est pas ce que vous voulez, **la relancer** :

```
"use strict" 
let x = parseInt(prompt("entrez un nombre inférieur à 5"))
try{
y=x-10 
if(y>=5) throw new Error(" y n'est pas inférieur à 5") 
else alert(y) 
}catch(e){ 
if(e instanceof ReferenceError){ 
throw e
}else alert(e) 
} 

```

Cela **relancera simplement l'erreur** pour qu'un autre try statement l'attrape ou interrompe le script ici. Cela est utile lorsque vous voulez surveiller uniquement un type particulier d'erreur et que d'autres erreurs qui pourraient survenir à cause de la négligence devraient interrompre le code.

## Conclusion

Dans cet article, j'ai essayé d'expliquer les concepts suivants liés à try/catch :

* Ce que sont les instructions try /catch et quand elles fonctionnent
* Comment lancer des erreurs personnalisées
* Ce qu'est l'instruction finally et comment elle fonctionne
* Comment fonctionnent les instructions try / catch imbriquées
* Comment relancer des erreurs

Merci d'avoir lu. Suivez-moi sur twitter [@fakoredeDami](https://twitter.com/fakoredeDami).