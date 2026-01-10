---
title: Plongée approfondie dans les chaînes de portée et les fermetures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:18:03.000Z'
originalURL: https://freecodecamp.org/news/deep-dive-into-scope-chains-and-closures-21ee18b71dd9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tFNnwdoFlSJ7QmF_
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Plongée approfondie dans les chaînes de portée et les fermetures
seo_desc: 'By Kevin Turney

  How Scope chain and closures work under the hood with examples.


  _Photo by [Unsplash](https://unsplash.com/@anuragvh?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Anurag Harishchandrakar on <a href="ht...'
---

Par Kevin Turney

#### Comment les chaînes de portée et les fermetures fonctionnent sous le capot avec des exemples.

![Image](https://cdn-media-1.freecodecamp.org/images/JC6Wko1HdOI-OS-znRe4GntOJVoHvbHE-8zc)
_Photo par [Unsplash](https://unsplash.com/@anuragvh?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Anurag Harishchandrakar</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Comprendre la portée et les fermetures en JavaScript

Pour creuser profondément et obtenir les informations dont vous avez besoin, pensez comme un journaliste. Posez les six questions principales : qui, quoi, pourquoi, où, quand et comment. Si vous pouvez répondre à toutes ces questions sur un sujet particulier, alors vous avez saisi l'essence de ce que vous devez savoir.

Avant d'aborder les fermetures, nous devons comprendre la portée.

Tout d'abord, si vous savez ce que [[scope]] (double crochet scope) est, alors cet article n'est pas pour vous. Vous avez des connaissances plus avancées et pouvez passer à autre chose.

### Le quoi...

Qu'est-ce que la **portée** et pourquoi est-ce important ?

> **_La portée est l'environnement contextuel (également connu sous le nom d'environnement lexical) créé lors de l'écriture d'une fonction. Ce contexte définit à quelles autres données elle a accès._**

En d'autres termes, la portée concerne l'accès. La fonction a-t-elle la capacité de rechercher une variable pour l'exécution ou la manipulation, quelles variables sont visibles ?

Il existe deux types de portée : locale et globale. La résolution de portée, ou la recherche des variables appartenant à un endroit, commence au contexte le plus interne et procède vers l'extérieur jusqu'à ce que l'identifiant soit trouvé. Commençons petit...

```
var firstNum = 1;
```

```
function number() {  var secondNum = 2;  return firstNum + secondNum;}
```

```
number();
```

### Le quand, pourquoi et comment... contexte d'exécution

![Image](https://cdn-media-1.freecodecamp.org/images/UxvNw5GMNCWBibNq99xSI1iWoGnY-39EZipV)

Lorsqu'une fonction est invoquée, elle forme un nouveau contexte d'exécution. Qu'est-ce qu'un contexte d'exécution ? Eh bien, tout comme nous avons deux types de portée, nous avons deux types de contexte d'exécution. Il s'agit d'un contexte d'exécution global et d'un contexte d'exécution de fonction.

Le contexte global est toujours en cours d'exécution. Dans le cas d'un environnement de navigateur, il ne s'arrête que lorsque le navigateur est fermé. Lorsque nous appelons une fonction, nous plaçons le contexte d'exécution de cette fonction au-dessus du contexte d'exécution global. D'où la terminologie selon laquelle nous les **empilons**.

JavaScript est un langage à thread unique, ce qui signifie qu'il ne peut faire qu'une seule chose à la fois. Lorsque nous appelons une fonction, le contexte d'exécution précédent est mis en pause. La fonction appelée est au sommet et elle est alors exécutée. Lorsque cela se termine, elle est retirée de la pile et le contexte d'exécution plus ancien est repris. Cette « pile » d'exécution est ce qui suit la position de l'exécution dans notre application. Elle est également importante pour la recherche d'identifiants.

Maintenant que nous avons un contexte d'exécution formé, que se passe-t-il ensuite ?

#### **Chaque contexte d'exécution a un objet variable associé**

![Image](https://cdn-media-1.freecodecamp.org/images/fUmuSkkuMeZsJVFFqOMP6ViyoAyZxzcPhIbl)

Tout d'abord, un **objet d'activation** (non accessible par le code, mais opérant en arrière-plan) est formé. Il est associé à ce contexte d'exécution. Cet objet contient toutes les **variables déclarées**, **fonctions** et **paramètres** passés dans ce contexte (sa portée ou sa plage d'accessibilité).

Les paramètres d'une fonction sont implicitement définis. Ils sont « locaux » à la portée de cette fonction. Ces variables déclarées sont « hissées », prises au sommet de la portée à laquelle elles appartiennent.

Avant d'aller plus loin, pour éviter toute confusion — dans le contexte d'exécution global, un **objet variable** est créé, et s'il s'agit d'une fonction, il s'agit d'un **objet d'activation**. Ils sont pratiquement identiques.

![Image](https://cdn-media-1.freecodecamp.org/images/lPIm2hQe6Qz9ZTByQxWx9S8-qj93KbtRQ66G)

Maintenant, lorsque cette fonction est invoquée, une « chaîne de portée » de ces objets est créée. Pourquoi ? La chaîne de portée est un moyen de lier ou de fournir un accès systématique à toutes les variables et autres fonctions auxquelles le contexte d'exécution actuel (la fonction dans ce cas) a accès. [[Scope]] est le mécanisme caché qui lie ces objets variables pour la recherche d'identifiants. Ce [[Scope]] caché est une propriété de la fonction, créée à la déclaration, et non à l'invocation.

À la tête de la chaîne de portée, s'il s'agit d'une fonction, se trouve l'**objet d'activation**. Cet objet d'activation a ses propres variables déclarées, arguments et ceci.

Ensuite, dans la chaîne de portée, se trouve le prochain objet du contexte contenant. S'il s'agit d'une variable globale, il s'agit d'un **objet variable**. S'il s'agit d'une fonction, il s'agit d'un **objet d'activation**. Cela se produit jusqu'à ce que nous atteignions le contexte global. C'est pourquoi vous pouvez voir que nous commençons par le contexte le plus interne jusqu'au plus externe, pensez aux poupées russes.

Quelle est la différence entre une variable qui est déclarée et une qui ne l'est pas ? Si l'identifiant est précédé d'un var, let ou const, il est déclaré explicitement et un espace mémoire est alloué pour l'utilisation de cette variable. Si l'identifiant n'est pas déclaré explicitement, alors il est implicitement déclaré dans la portée globale, ce que nous explorerons bientôt. Aux fins de cet article, je m'en tiens à var, sans raison particulière.

Je sais, ce qui précède était un peu technique, et pour être honnête, en écrivant cela, j'ai moi-même appris l'existence des objets Variable et Activation. Maintenant que vous avez eu l'explication approfondie, voici une description à haut niveau...

La chaîne de portée est similaire à la chaîne de prototypes. Si une variable ou une propriété n'est pas trouvée, elle continue à remonter la chaîne jusqu'à ce qu'elle soit trouvée ou qu'une erreur soit levée. La fonction crée une propriété cachée [[scope]]. Cette propriété lie les portées les plus internes aux portées les plus externes. Dans ce cas, la chaîne de portée de number est liée à l'objet global window (le contexte contenant qui détient la fonction number). C'est ce qui permet au moteur de recherche de regarder à l'extérieur de la fonction number pour trouver firstNum et secondNum.

Par exemple, prenons la même fonction number et changeons une chose :

```
// portée globale - inclut firstNum, secondNum et la // fonction number
```

```
var firstNum = 1;
```

```
function number() {    // portée locale pour number - seulement thirdNum est local à number()    // car il a été explicitement déclaré. secondNum est implicitement déclaré dans    // la portée globale.
```

```
secondNum = 2;    var thirdNum = 3;    return firstNum + secondNum;  }
// À quoi avons-nous accès dans la portée globale ?
number(); // 3
firstNum; // 1
secondNum; // 2
thirdNum; // Reference Error: thirdNum n'est pas défini
```

![Image](https://cdn-media-1.freecodecamp.org/images/mZ88I9Xu0AfpjMKHwLSdNTEOUMdwg6DYfFgy)

En parlant de portée globale, les déclarations de variables, les déclarations de fonctions non imbriquées et les expressions de fonctions (toujours considérées comme une définition de variable) sont considérées dans la portée de l'objet global window dans le navigateur. Comme nous le voyons ci-dessus, l'objet window a des propriétés firstNum, secondNum et number ajoutées. Si nous procédons le long de la chaîne de portée à la recherche de celle-ci, nous continuons à chercher jusqu'à ce que nous atteignions l'objet variable du contexte global. Si elle n'y est pas, alors nous obtenons l'erreur de référence.

```
Dans un nouvel onglet, tapez "about:blank" dans la barre de recherche. Une page blanche s'ouvrira et appuyez sur cmd-option-i pour ouvrir les outils de développement.
```

```
Tapez le code ci-dessus et n'oubliez pas, shift-enter pour une nouvelle ligne !
```

```
Maintenant, tapez "window" et explorez toutes les propriétés de l'objet window.
```

```
Regardez attentivement et vous verrez que les propriétés firstNum, secondNum et number sont toutes disponibles sur l'objet window.
```

Lorsque nous essayons d'accéder à thirdNum en dehors de l'endroit où il a été déclaré, nous obtenons une erreur de référence. Le moteur qui compile le code n'a pas réussi à trouver un identifiant dans l'objet global window.

ThirdNum n'est disponible qu'à l'intérieur de la fonction où il a été déclaré. Il est encapsulé ou privé pour la fonction number.

La question que vous pourriez avoir est « La portée globale a-t-elle accès à tout ce qui est à l'intérieur de number ? » Encore une fois, la portée ne fonctionne que de l'intérieur vers l'extérieur, le contexte le plus interne, local, vers le contexte le plus externe, global.

En commençant par la portée locale, nous pouvons dire que les données et les variables qui sont enveloppées dans une fonction ne sont accessibles qu'aux membres de cette fonction. La chaîne de portée est ce qui lie firstNum à number().

Lorsque number() est invoqué, la conversation non technique se déroule comme suit...

> **_Moteur :_** _« Number, je te donne un nouveau contexte d'exécution. Laisse-moi trouver ce dont tu as besoin pour fonctionner »_

> **_Moteur_**_: « Ok, je vois que thirdNum est explicitement déclaré. Je réserve un espace pour toi, va en haut du bloc de fonction de number et attends que je t'appelle... »_

> **_Moteur_**_: « Number, je vois secondNum, est-ce qu'il t'appartient ? »_

> **_Number_**_: « Non. »_

> **_Moteur_**_: « Ok, je vois que tu es lié à l'objet global window, laisse-moi regarder à l'extérieur de toi. »_

> **_Moteur_**_: « Window, j'ai un identifiant nommé secondNum, est-ce qu'il t'appartient ? »_

> **_Window_**_: « Il ne s'est pas déclaré explicitement dans Number avec un var, let ou const, alors je vais le prendre et réserver un espace. »_

> **_Moteur_**_: « Cool. Number, je vois firstNum dans ton bloc de fonction, est-ce qu'il t'appartient ? »_

> **_Number_**_: « Non. »_

> **_Moteur_**_: « Window, je vois firstNum utilisé à l'intérieur de Number, il en a besoin, est-ce qu'il t'appartient ? »_

> **_Window_**_: « Oui, il a été déclaré. »_

> **_Moteur_**_: « Tout le monde est comptabilisé, maintenant j'assigne des valeurs aux variables. »_

> **_Moteur_**_: Number, je t'exécute, prêt, c'est parti ! »_

C'est à peu près tout pour comprendre la portée. Les points clés à retenir sont :

1. La recherche d'identifiants fonctionne de l'intérieur vers l'extérieur et s'arrête au premier match.
2. Il existe deux types de portée, globale et locale.
3. La chaîne de portée est créée à l'invocation de la fonction et est basée sur l'endroit où les variables et/ou les blocs de code sont écrits (environnement lexical). Les variables ou fonctions sont-elles imbriquées ?
4. En JavaScript, si un identifiant n'est pas précédé d'un var, let ou const, il est implicitement déclaré dans la portée globale.
5. La portée ne va pas de 1 pour 1 avec une fonction, elle va de 1 à 1 avec l'invocation de la fonction. Exécutez une fonction 3 fois, obtenez 3 portées différentes. Pourquoi ? Parce que si l'exécution d'une fonction est terminée, elle est retirée de la pile d'exécution et avec elle, son accès à d'autres variables via sa chaîne de portée. Ainsi, une nouvelle portée est créée chaque fois qu'une fonction est exécutée. Les fermetures fonctionnent un peu différemment !

Terminons avec un exemple plus complexe avant de passer aux fermetures.

```
a = 1;
var b = 2;
```

```
function outer(z) {  b = 3;  c = 4;  var d = 5;  e = 6;
```

```
function inner() {    var e = 0;    d = 2 * d;    return d;  }  return inner();  var e;}
outer(1);
```

1. Avant d'exécuter quoi que ce soit, le hissage est démarré au niveau global. Par conséquent, nous commençons avec une déclaration pour une **variable** **b**, et une déclaration de fonction pour **l'objet fonction outer**. À ce stade, rien n'est assigné, nous avons seulement ces deux clés configurées dans l'objet variable de portée globale.
2. Ensuite, nous commençons par **a = 1.** Il s'agit d'une assignation, ou d'une instruction « écrire vers », mais il n'y a pas de déclaration formelle pour celle-ci. Donc, ce qui se passe dans la portée globale, et si ce n'est pas en mode « strict », c'est que **a** sera implicitement déclaré comme appartenant à l'objet variable de portée globale.
3. Nous passons à la ligne suivante et recherchons l'identifiant **b**, grâce au hissage, il a été pris en compte et nous pouvons maintenant lui assigner une valeur, 2.

Jusqu'à présent, nous avons...

#### Portée globale

![Image](https://cdn-media-1.freecodecamp.org/images/WS9msWmNLLYx50YR5DCjUfXfKMs-GIrr424a)

4. Puisque nous avons construit l'**objet fonction outer**, au moment du hissage, nous passons ensuite à l'exécution, outer(1);

5. Rappelez-vous qu'à l'invocation de la fonction, un contexte d'exécution est d'abord créé. Avec cela, nous créons un objet d'activation. Il contient les données et les variables locales à ce contexte. Nous formons également la chaîne de portée.

6. Le paramètre **z** est implicitement déclaré pour cette fonction et se voit assigner 1.

Une note rapide : à ce moment-là, le contexte d'exécution de la fonction crée sa liaison « **this** ». Il crée également un **tableau d'arguments**, qui est un tableau de paramètres passés, dans ce cas, z. **Cela** dépasse le cadre de cet article, alors permettez-moi de le survoller.

7. Maintenant, nous recherchons les déclarations de variables explicites dans **la fonction outer**. Nous avons **d**, et **var e** est déclaré après **la fonction inner**.

8. Voici un peu de magie cachée, **à ce moment-là, une propriété cachée [[scope]] pour la fonction outer lie sa chaîne de portée d'objets variables. Dans ce cas, cela fonctionne comme une liste liée avec une propriété de type parent reliant l'objet d'activation de la fonction outer à l'objet variable du contexte d'exécution global.** Vous pouvez voir ici que la portée s'étend de l'intérieur vers l'extérieur pour former cette « liaison ». C'est la référence qui nous permet de remonter la chaîne de portée pour les recherches.

#### Portée pour la fonction outer

![Image](https://cdn-media-1.freecodecamp.org/images/cv8nLf3vH0T-8NFBDzxDArKSAL7n5gnLIn7w)

9. Nous entrons dans **outer** et commençons par **b** = 3. Est-ce que **b** est déclaré ? Non. Donc JavaScript utilise la propriété cachée **[[scope]]** attachée à la fonction **outer** pour remonter la chaîne de portée afin de trouver un « **b** ». Il le trouve dans l'objet de portée globale et, puisque nous sommes dans le corps de la fonction **outer**, nous assignons à **b** la valeur 3.

#### Portée globale à nouveau

![Image](https://cdn-media-1.freecodecamp.org/images/qpQb0nuu7Y1WbN3MJwp9ermPDVShi8R9u9Sj)

10. Ligne suivante, **c** = 4. Puisque cela est une écriture vers l'identifiant **c**, **c** a-t-il été explicitement déclaré dans la fonction **outer** ? Non, et donc il n'est pas trouvé par la recherche dans l'objet d'activation de outer. Il remonte donc la chaîne de portée et cherche dans l'objet variable de portée globale. Il n'y est pas. Parce que cela est une opération d'écriture/d'assignation, la portée globale va la gérer et la placer sur son objet variable.

#### Objet variable de portée globale

![Image](https://cdn-media-1.freecodecamp.org/images/kLw4Ge1eryBuP1xrBetBMr8EX9KtPsCmmjBk)

11. **d** = 5. Oui, il est ici donc nous lui assignons 5.

#### Portée pour la fonction outer

![Image](https://cdn-media-1.freecodecamp.org/images/rCC-QbTSWgdHODOvdaCuvVt39-kqwO2qCnpF)

12. **e** = 6. Vous vous souvenez de ce traînard, var **e** ? Il a été déclaré dans le corps de **outer** et donc nous avions déjà une place pour lui — donc nous lui assignons 6. S'il n'avait pas été déclaré comme **c**, nous serions remontés dans la chaîne de portée pour une recherche. Puisque c'est une écriture et non une opération de lecture et que ce n'est pas en mode « strict », il aurait été placé dans la portée globale.

13. Nous arrivons à l'invocation de la fonction **inner**. Nous recommenceons comme nous l'avons fait avec la fonction **outer** : hissage, configuration d'un objet d'activation et création d'une propriété cachée **[[scope]]**. Dans ce cas, le contexte contenant est la fonction **outer**, et **outer** « pointe » vers la portée globale.

#### Portée pour la fonction inner

![Image](https://cdn-media-1.freecodecamp.org/images/uM9gVd9l86C9w6eMypi55J1Xxi0f0CaThFSv)

14. Maintenant avec **e** et en général, les variables qui ont le même nom fonctionnent comme ceci. Puisque la recherche d'identifiants commence de la portée la plus interne à la portée la plus externe, la recherche s'arrête à la première trouvaille de cet identifiant. Dans le corps de **inner**, nous voyons var **e**= 0, terminé, stop, n'allez pas plus loin. Le **e** dans le corps de la fonction **outer** est « inaccessible ». Le terme couramment utilisé est « shadowing » **e** dans la fonction **inner** « shadow » ou obscurcit le **e** dans la fonction **outer**.

15. La ligne suivante est **d** = 2 * **d**. Avant d'assigner une valeur à **d** à gauche, nous devons évaluer l'expression à droite, 2 * **d**. Puisque **d** n'est pas local dans la portée de **inner**, nous remontons la chaîne de portée pour trouver une variable pour **d** et si elle a une valeur associée. Nous la trouvons dans la portée **outer** dans la fonction **outer** et c'est là que la valeur est changée.

#### Portée pour la fonction outer

![Image](https://cdn-media-1.freecodecamp.org/images/UfIUjuTpQ3t3JGOHDPpY0rxS6ZvpCHz0Eleo)

L'important ici est que **inner manipule les données dans sa portée externe !**

16. La fonction **inner** retourne une valeur **d**, 10.

17. La fonction **outer** retourne la valeur de la fonction **inner**.

18. Le résultat est 10.

19. Une fois que la fonction **outer** a complètement terminé son exécution, le **ramasse-miettes** a lieu. Le ramasse-miettes est la libération des ressources qui ne sont plus nécessaires. Il commence à la portée globale et travaille aussi loin qu'il a une « accessibilité ».

La portée globale dans cet exemple n'a pas de poignée sur la fonction **outer** ou la fonction **inner**, donc whoosh, disparues. Cela est important lorsque nous arrivons aux fermetures, car là, nous avons besoin que des données et certaines variables restent même après qu'une fonction a fini de s'exécuter.

### Enfin, obtenons une fermeture !

#### Comment définir une fermeture ?

Commençons par quelques définitions, toutes correctes, certaines plus approfondies, mais qui arrivent au même point.

```
1. Les fermetures sont des fonctions qui ont accès à des variables d'une autre portée de fonction. Cela est accompli en créant une fonction à l'intérieur d'une autre fonction.
```

```
2. Une fermeture est une fonction qui retourne une autre fonction.
```

```
3. Une fermeture est un lien implicite et permanent entre une fonction et sa chaîne de portée.
```

#### Pourquoi les fermetures ?

Sans pouvoir exploiter les règles de la chaîne de portée, les opérations asynchrones seraient impossibles. Parce qu'il n'y a aucune garantie que les données seront toujours disponibles pour une utilisation ultérieure. JavaScript n'a que la portée de fonction comme mécanisme d'encapsulation.

Les fermetures sont la meilleure forme de confidentialité pour les fonctions et les variables. Cela est évident dans l'utilisation de nombreux motifs de modules. Un motif de module retourne un objet pour exposer une API publique. Il garde également d'autres méthodes et variables privées. Les fermetures sont utilisées dans la gestion des événements et les rappels.

Un exemple de module...

```
var Toaster = (function(){    var setting = 0;    var temperature;    var low = 100;    var med = 200;    var high = 300;    // public    var turnOn = function(){        return heatSetting();    };    var adjustSetting = function(setting){        if(setting <= 3){            temperature = low;        }if (setting >3  && setting <= 6){            temperature = med;        }if (setting > 6 && setting <= 10){            temperature = high;
```

```
}return temperature;    };    // private    var heatSetting = function(adjustSetting){        var thermostat = adjustSetting;        return thermostat;        };    return{            turnOn:turnOn,            adjustSetting:adjustSetting        };})();
```

```
Toaster.adjustSetting(5);Toaster.adjustSetting(8);
```

Le module Toaster a des locaux privés et une interface publique et est écrit comme une Expression de Fonction Immédiatement Invoquée (IIFE). Nous créons une fonction, l'invoquons immédiatement et récupérons la valeur de retour.

Un autre petit exemple :

```
function firstName(first){    function fullName(last){        console.log(first + " " + last);    }    return fullName;}
var name = firstName("Mister");
name("Smith") // Mister Smith
name("Jones"); //Mister Jones
```

La fonction interne fullName() accède à la variable, first, dans sa portée externe, firstName(). **Même après que la fonction interne, fullName, a retourné, elle a toujours accès à cette variable**. Comment est-ce possible ? La chaîne de portée de la fonction interne inclut la portée de sa portée externe.

Lorsque une fonction est appelée, un contexte d'exécution et une chaîne de portée sont créés. De plus, la fonction obtient une propriété cachée [[Scope]]. L'objet d'activation pour la fonction est initialisé et placé dans la chaîne. Ensuite, l'objet d'activation de la fonction externe est placé dans la chaîne. Dans ce cas, enfin l'objet **Variable Object** global.

Dans cet exemple, fullName est défini. Une propriété [[Scope]] est créée. L'objet d'activation de la fonction contenant est ajouté à la chaîne de portée de fullName. Il est également ajouté à l'objet variable global. Cette référence à l'objet d'activation d'une fonction externe permet l'accès à toutes les variables des portées contenant. Il n'est pas collecté par le ramasse-miettes.

**C'est le plus important. L'objet d'activation de la fonction externe, firstName(), ne peut pas être détruit une fois qu'il a terminé son exécution, car la référence existe toujours dans la chaîne de portée de fullName. Après l'exécution de firstName()**
**est terminée, sa chaîne de portée pour ce contexte d'exécution est détruite. Mais l'objet d'activation restera en mémoire jusqu'à ce que fullName() soit détruit.** Nous pouvons faire cela en définissant sa référence à null.

L'observateur avisé notera que nous retournons une référence à fullName, pas la valeur de retour de fullName() !

C'est ce que nous entendons par un lien implicite et permanent entre une fonction et sa chaîne de portée.

Une fermeture obtient toujours la dernière valeur de la fonction contenant car la référence à l'objet variable est stockée.

Par exemple...

```
var myFunctions= [];
function createMyFunction(i) {    return function() {           console.log("My value: " + i);            };        }
for (var i = 0; i < 10; i++) {
myFunctions[i] = createMyFunction(i);
myFunctions[i]();}
```

```
My value: 0 My value: 1 My value: 2 My value: 3 My value: 4 My value: 5 My value: 6 My value: 7 My value: 8 My value: 9
```

Si nous revenons à notre exemple de portée original et changeons une chose :

```
a = 1;
var b = 2;
```

```
function outer(z) {  b = 3;  c = 4;  var d = 5;  e = 6;
```

```
function inner() {    var e = 0;    d = 2 * d;    return d;  }  return inner; // nous supprimons l'opérateur d'appel, maintenant nous retournons une référence à la fonction inner.  var e;}
myG = outer(1); // stocke une référence à la fonction inner dans la portée globale (la valeur de retour de outer)
myG(); // lorsque nous exécutons myG, la propriété [[Scope]] de inner est copiée pour recréer la chaîne de portée,    //  et cela lui donne accès aux portées qui contiennent la fonction inner, outter puis globale. Nous avons inner et inner a outter.
```

Voici quelques exemples supplémentaires :

```
function make_calculator() {    var n = 0;  // cette calculatrice stocke un seul nombre n    return {      add: function(a) { n += a; return n; },      multiply: function(a) { n *= a; return n; }    };}
```

```
first_calculator = make_calculator();
second_calculator = make_calculator();
```

```
first_calculator.add(3);                   // retourne 3
second_calculator.add(400);                // retourne 400
```

```
first_calculator.multiply(11);             // retourne 33
second_calculator.multiply(10);            // retourne 4000
```

Supposons que nous voulions exécuter un tableau de fonctions :

```
function buildList(list) {    var result = [];    for (var i = 0; i < list.length; i++) {        result.push(function number(i) {          var item = 'item' + list[i];          console.log(item + ' ' + list[i])} );    }    return result;}
buildList([1,2,3,4,5]);
```

```
function testList() {     var fnlist = buildList([1,2,3,4,5]);     for (var i = 0; i < fnlist.length; i++) {       fnlist[i](i); // une autre IIFE avec i passé comme paramètre !!     } }
 testList();
```

J'espère que cette explication de la portée et des fermetures aide. Jouez avec les motifs que vous voyez ici, expérimentez. En fait, écrire cet article était difficile — j'ai acquis une compréhension bien plus profonde que celle que j'avais lorsque j'ai commencé.

### Ressources

[YDKJS](https://github.com/getify/You-Dont-Know-JS/tree/master/scope%20%26%20closures)

[Dmitry Soshnikov, Javascript:Core](http://dmitrysoshnikov.com/ecmascript/javascript-the-core/#variable-object)

[ECMA 262.3](http://dmitrysoshnikov.com/ecmascript/chapter-2-variable-object/)

[StackOverflow](https://stackoverflow.com/questions/111102/how-do-javascript-closures-work)

[Nick Zakas](https://www.amazon.com/Professional-JavaScript-Developers-Nicholas-Zakas/dp/1118026691)