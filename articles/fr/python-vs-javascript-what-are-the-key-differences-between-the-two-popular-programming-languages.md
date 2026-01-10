---
title: Python VS JavaScript – Quelles sont les différences clés entre ces deux langages
  de programmation populaires ?
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2021-01-28T16:04:43.000Z'
originalURL: https://freecodecamp.org/news/python-vs-javascript-what-are-the-key-differences-between-the-two-popular-programming-languages
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Python-vs.-JavaScript-1.png
tags:
- name: 'Back end development '
  slug: back-end-development
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: programming languages
  slug: programming-languages
- name: Python
  slug: python
- name: Web Development
  slug: web-development
seo_title: Python VS JavaScript – Quelles sont les différences clés entre ces deux
  langages de programmation populaires ?
seo_desc: "Welcome! If you want to learn the differences between Python and JavaScript,\
  \ then this article is for you. \nThese two languages are very popular and powerful,\
  \ but they do have key differences. We will cover them in detail here.\nIn this\
  \ article, you w..."
---

**Bienvenue !** Si vous souhaitez apprendre les différences entre Python et JavaScript, alors cet article est fait pour vous. 

Ces deux langages sont très populaires et puissants, mais ils présentent des différences clés. Nous allons les couvrir en détail ici.

**Dans cet article, vous apprendrez :**

* Les différentes applications réelles de Python et JavaScript.
* Les différences syntaxiques et fonctionnelles clés entre Python et JavaScript.

**Commençons !** ✨

## 🔹 Python VS JavaScript : Applications réelles 

Nous allons commencer par un rapide tour d'horizon de leurs applications réelles.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-187.png)

### Python

Python est devenu un outil essentiel dans pratiquement toutes les applications scientifiques à travers le monde grâce à sa puissance et sa polyvalence. C'est un langage de programmation polyvalent qui supporte différents paradigmes de programmation.

Il est largement utilisé dans des applications scientifiques et spécialisées, y compris la science des données, l'intelligence artificielle, l'apprentissage automatique, l'éducation en informatique, la vision par ordinateur et le traitement d'images, la médecine, la biologie, et même l'astronomie. 

Il est également utilisé pour le développement web. C'est là que nous pouvons commencer à comparer ses applications à celles de JavaScript. Python est utilisé pour le développement back-end, qui est la partie du développement web responsable de la création des éléments que les utilisateurs ne voient pas, comme le côté serveur d'une application. 

### JavaScript

Alors que Python peut être utilisé pour développer la partie back-end d'une application web, JavaScript peut être utilisé pour développer à la fois le back-end et le front-end de l'application. 

Le front-end est la partie de l'application que l'utilisateur voit et avec laquelle il interagit. Chaque fois que vous voyez ou interagissez avec un site web ou une application web, vous utilisez JavaScript "en coulisses". 

De même, lorsque vous interagissez avec une application mobile, vous pourriez utiliser JavaScript car des frameworks comme [React Native](https://reactnative.dev/) nous permettent d'écrire des applications qui s'adaptent à différentes plateformes.

JavaScript est si largement utilisé dans le développement web car c'est un langage polyvalent qui nous donne les outils nécessaires pour développer les composants d'une application web. 

### Différences entre les applications de Python et JavaScript

En résumé, les développeurs utilisent Python pour une gamme d'applications scientifiques. Ils utilisent JavaScript pour le développement web, les fonctionnalités orientées utilisateur et les serveurs.

## 🔸 Python VS JavaScript : Syntaxe

Maintenant que vous savez à quoi ils servent, voyons comment ils sont écrits et les différences dans leur syntaxe.

Nous allons couvrir les différences dans leurs éléments principaux :

* Blocs de code
* Définitions de variables
* Conventions de nommage des variables
* Constantes
* Types de données et valeurs
* Commentaires
* Structures de données intégrées
* Opérateurs
* Entrée/Sortie
* Instructions conditionnelles
* Boucles For et While
* Fonctions
* Programmation orientée objet

## Blocs de code en Python et JavaScript

Chaque langage de programmation a son propre style pour définir les blocs de code. Voyons leurs différences en Python et JavaScript :

### Comment Python définit les blocs de code

Python repose sur l'indentation pour définir les blocs de code. Lorsqu'une série de lignes de code continues sont indentées au même niveau, elles sont considérées comme faisant partie du même bloc de code. 

Nous utilisons cela pour définir des conditionnelles, des fonctions, des boucles, et pratiquement toutes les instructions composées en Python. 

Voici quelques exemples :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-127.png)
_Utilisation de l'indentation pour définir des blocs de code en Python_

**💡 Conseil :** Nous verrons les différences spécifiques entre ces éléments en Python et JavaScript dans un instant. Pour l'instant, concentrez-vous sur l'indentation.

### Comment JavaScript définit les blocs de code

En revanche, en JavaScript, nous utilisons des accolades (`**{}**`) pour regrouper les instructions qui appartiennent au même bloc de code. 

Voici quelques exemples :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-128.png)
_Utilisation des accolades pour définir des blocs de code en JavaScript_

## Définitions de variables en Python et JavaScript

L'instruction d'affectation est l'une des instructions les plus fondamentales dans tout langage de programmation. Voyons comment nous pouvons définir une variable en Python et JavaScript.

### Comment définir une variable en Python

Pour définir une variable en Python, nous écrivons le nom de la variable suivi d'un signe égal (`**=**`) et de la valeur qui sera assignée à la variable. 

Comme ceci :

```python
<nom_variable> = <valeur>
```

Par exemple :

```python
x = 5
```

### Comment définir une variable en JavaScript

La syntaxe est très similaire en JavaScript, mais nous devons simplement ajouter le mot-clé `**var**` ou `**let**` avant le nom de la variable et terminer la ligne par un point-virgule (`**;**`). 

Comme ceci :

```
var <nom_variable> = <valeur>;
```

**💡 Conseil :** Lorsque vous définissez une variable en utilisant `**var**`, la variable a une portée de fonction. 

Par exemple :

```
var x = 5;
```

Nous pouvons également utiliser le mot-clé `**let**` :

```
let <nom_variable> = <valeur>;
```

Par exemple :

```
let x = 5;
```

**💡 Conseil :** Dans ce cas, lorsque nous utilisons `**let**`, la variable aura une portée de bloc. Elle ne sera reconnue que dans le bloc de code où elle a été définie. 

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-125.png)
_Définitions de variables en Python et JavaScript_

💡 **Conseil :** En JavaScript, la fin d'une instruction est marquée par un point-virgule (`;`) mais en Python, nous commençons simplement une nouvelle ligne pour marquer la fin d'une instruction. 

## Conventions de nommage des variables en Python et JavaScript

Python et JavaScript suivent deux conventions de nommage de variables différentes.

### Comment nommer les variables en Python

En Python, nous devons utiliser le style de nommage `**snake_case**`.

Selon le [Guide de style Python](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names) :

> Les noms de variables suivent la même convention que les noms de fonctions.  
>   
> Les noms de fonctions doivent être **en minuscules, avec des mots séparés par des underscores** si nécessaire pour améliorer la lisibilité.

Par conséquent, un nom de variable typique en Python ressemblerait à ceci :

```python
prenom
```

💡 **Conseil :** Le guide de style mentionne également que "`**mixedCase**` est autorisé uniquement dans les contextes où c'est déjà le style dominant, pour conserver la compatibilité ascendante."

### Comment nommer les variables en JavaScript

En revanche, nous devons utiliser le style de nommage `**lowerCamelCase**` en JavaScript. Le nom commence par une lettre minuscule et ensuite chaque nouveau mot commence par une lettre majuscule. 

Selon l'article [JavaScript guidelines](https://developer.mozilla.org/en-US/docs/MDN/Guidelines/Code_guidelines/JavaScript#Variable_naming) des MDN Web Docs :

> Pour les noms de variables, utilisez lowerCamelCasing, et utilisez des noms concis, lisibles par l'homme, sémantiques lorsque c'est approprié.

Par conséquent, un nom de variable typique en JavaScript devrait ressembler à ceci :

```javascript
prenom
```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-178.png)

## Constantes en Python et JavaScript

Bien. Maintenant que vous en savez plus sur les variables, parlons un peu des constantes. Les constantes sont des valeurs qui ne peuvent pas être modifiées pendant l'exécution du programme. 

### Comment définir des constantes en Python

En Python, nous nous appuyons sur des conventions de nommage pour définir des constantes car il n'y a pas de règles strictes dans le langage pour empêcher les modifications de leurs valeurs.

Selon le [Guide de style Python](https://www.python.org/dev/peps/pep-0008/#constants) :

> Les constantes sont généralement définies au niveau du module et **écrites en lettres majuscules avec des underscores séparant les mots**. 

C'est le style de nommage que nous devons utiliser pour définir une constante en Python :

```
NOM_CONSTANTE
```

Par exemple :

```javascript
TAUX_IMPOT_POURCENTAGE = 32
```

💡 **Conseil :** Cela sert d'avertissement rouge pour nous-mêmes et pour les autres développeurs indiquant que cette valeur ne doit pas être modifiée dans le programme. Mais techniquement, la valeur peut encore être modifiée. 

### Comment définir des constantes en JavaScript

En revanche, en JavaScript, nous pouvons définir des constantes qui ne peuvent pas être modifiées dans le programme, et l'identifiant de la variable ne peut pas être réassigné. 

Mais cela ne signifie pas que la valeur elle-même ne peut pas être modifiée. 

Selon l'article `**const**` dans [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) :

> La déclaration `const` crée une référence en lecture seule à une valeur. Cela ne signifie **pas** que la valeur qu'elle contient est immuable—seulement que l'identifiant de la variable ne peut pas être réassigné. Par exemple, dans le cas où le contenu est un objet, cela signifie que le contenu de l'objet (par exemple, ses propriétés) peut être modifié.

Pour définir une constante en JavaScript, nous ajoutons le mot-clé `**const**` avant le nom de la variable :

```
const TAUX_IMPOT_POURCENTAGE = 32;
```

Si nous essayons de changer la valeur de la constante, nous verrons cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-180.png)

Par conséquent, la valeur ne peut pas être modifiée. 

**💡 Conseil :** Pour exécuter et tester de petits extraits de code JavaScript, vous pouvez utiliser la [console dans Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools/console). 

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-181.png)

## Types de données et valeurs en Python et JavaScript

Voyons les principales différences entre les types de données Python et JavaScript. 

### Types de données numériques

**Python** a trois types numériques pour nous aider à effectuer des calculs précis à des fins scientifiques. Ces types numériques incluent : `int` (entiers),  `float` (nombres à virgule flottante), et `complex`. Chacun d'eux a ses propres propriétés, caractéristiques et applications. 

En revanche, **JavaScript** n'a que deux types numériques : `**Number**` et `**BigInt**`. Les entiers et les nombres à virgule flottante sont tous deux considérés comme étant de type `**Number**`. 

Selon l'article [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) dans MDN Web Docs :

> Une valeur numérique littérale comme `37` dans le code JavaScript est une valeur à virgule flottante, pas un entier. Il n'y a pas de type entier séparé dans l'usage courant quotidien. (JavaScript a maintenant un type [BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt), mais il n'a pas été conçu pour remplacer Number pour les usages quotidiens. `37` est toujours un Number, pas un BigInt.)

### None vs. null 

En **Python**, il y a une valeur spéciale appelée `**None**` que nous utilisons généralement pour indiquer qu'une variable n'a pas de valeur à un moment particulier du programme. 

La valeur équivalente en **JavaScript** est `**null**`, qui "représente l'absence intentionnelle de toute valeur d'objet" ([source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-144.png)

### La valeur `undefined` 

En **JavaScript**, nous avons une valeur spéciale qui est assignée automatiquement lorsque nous déclarons une variable sans assigner de valeur initiale.

Voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-142.png)

Comme vous pouvez le voir, la valeur de la variable `**x**` est `**undefined**`.

En **Python**, vous devez assigner une valeur initiale à la variable. Nous ne pouvons pas la déclarer sans valeur initiale.

**💡 Conseil :** Vous pouvez assigner `**None**` comme valeur initiale d'une variable en Python pour représenter l'absence de valeur.

### Types de données primitifs en Python et JavaScript

Les types de données primitifs représentent les valeurs les plus fondamentales avec lesquelles nous pouvons travailler dans un langage de programmation. Comparons les types de données primitifs de ces deux langages :

* **Python** a quatre types de données primitifs : Entiers (`int`), Flottants (`float`), Booléens (`bool`), et chaînes de caractères (`str`).
* **JavaScript** a sept types de données primitifs : `undefined`**,** Boolean, String, Number, `BigInt`, `Symbol`, et `null` ([source](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)).

## Comment écrire des commentaires en Python et JavaScript

Les commentaires sont très importants pour écrire un code propre et lisible. Voyons comment vous pouvez les utiliser en Python et JavaScript :

### Commentaires sur une seule ligne

* En **Python**, nous utilisons un hashtag (`**#**`) pour écrire un commentaire. Tous les caractères sur la même ligne après ce symbole sont considérés comme faisant partie du commentaire. 
* En **JavaScript**, nous écrivons deux barres obliques (`**//**`) pour commencer un commentaire sur une seule ligne. 

Voici un exemple graphique :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-145.png)

En Python :

```python
# Commentaire
```

En JavaScript :

```javascript
// Commentaire
```

### Commentaires sur plusieurs lignes

* En **Python**, pour écrire un commentaire sur plusieurs lignes, nous commençons chaque ligne par un hashtag.
* En **JavaScript**, les commentaires sur plusieurs lignes commencent par un `**/***` et se terminent par un `***/**`. Tous les caractères entre ces symboles sont considérés comme faisant partie du commentaire. 

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-146.png)

En Python :

```python
# Commentaire sur plusieurs lignes 
# en Python pour expliquer
# le code en détail.
```

En JavaScript :

```javascript
/* 
Commentaire sur plusieurs lignes 
en JavaScript pour expliquer 
le code en détail.
*/
```

## Structures de données intégrées en Python et JavaScript

Les structures de données intégrées en Python et JavaScript présentent également des différences clés. 

### Tuples

* En **Python**, nous avons une structure de données intégrée appelée **tuple** qui est très similaire à une liste mais immuable. Par conséquent, elle ne peut pas être modifiée pendant l'exécution du programme, donc elle est utilisée pour stocker des données qui ne doivent pas être modifiées.
* En **JavaScript**, il n'y a pas de structure de données intégrée avec ces caractéristiques. Bien que vous puissiez implémenter une structure de données similaire avec certaines fonctionnalités du langage.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-182.png)

### Listes vs. Tableaux

* En **Python,** **listes** sont utilisées pour stocker une séquence de valeurs dans la même structure de données. Elles peuvent être modifiées, indexées, découpées et utilisées dans le programme. 
* En **JavaScript**, une version équivalente de cette structure de données est appelée **tableau**.

Voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-147.png)

### Tables de hachage

* En **Python**, il y a une structure de données intégrée appelée **dictionnaire** qui nous aide à mapper certaines valeurs à d'autres valeurs et à créer des paires clé-valeur. Cela fonctionne comme une table de hachage. 
* **JavaScript** n'a pas ce type de structure de données intégrée, mais il existe certaines façons de reproduire sa fonctionnalité avec certains éléments du langage. 

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-183.png)

## Opérateurs en Python et JavaScript

Les opérateurs sont essentiels pour écrire des expressions dans tout langage de programmation. Voyons leurs différences clés en Python et JavaScript.

### Division entière

Alors que la plupart des opérateurs arithmétiques fonctionnent exactement de la même manière en Python et JavaScript, l'opérateur de division entière est un peu différent. 

* En **Python**, l'opération de division entière (également appelée "division entière") est représentée par une double barre oblique (`**//**`).
* En **JavaScript**, nous n'avons pas d'opérateur de division entière particulier. Au lieu de cela, nous appelons la méthode `**Math.floor()**` pour arrondir le résultat à l'entier le plus proche.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-149.png)

### Comparaison de valeurs et de types

En **Python**, nous utilisons l'opérateur `**==**` pour comparer si deux valeurs et leurs types de données sont égaux. 

Par exemple :

```python
# Comparaison de deux entiers
>>> 0 == 0     
True
# Comparaison d'un entier à une chaîne
>>> 0 == "0"
False
```

En **JavaScript**, nous avons également cet opérateur mais il fonctionne un peu différemment car il convertit les deux objets au même type avant d'effectuer réellement la comparaison. 

Si nous vérifions le résultat de la comparaison "entier vs. chaîne" de l'exemple précédent en utilisant JavaScript (`0 == "0"`), le résultat est `**True**` au lieu de `**False**` car les valeurs sont converties au même type de données avant d'être comparées :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-150.png)

En JavaScript, pour vérifier si la valeur **et** le type de données sont tous deux égaux, nous devons utiliser cet opérateur `**===**` (un triple signe égal). 

Maintenant, nous obtenons le résultat que nous attendions :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-151.png)

Génial, n'est-ce pas ? 

**💡 Conseil :** L'opérateur `**==**` en Python fonctionne comme l'opérateur `**===**` en JavaScript. 

### Opérateurs logiques

* En **Python**, les trois opérateurs logiques sont : `**and**`, `**or**`, et `**not**`.
* En **JavaScript**, ces opérateurs sont : `**&&**`, `**||**`, et `**!**` (respectivement).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-152.png)

### Opérateurs de type

* En **Python**, pour vérifier le type d'un objet, nous utilisons la fonction `**type()**`.
* En **JavaScript**, nous utilisons l'opérateur `**typeof**`.

Voici une description graphique de leur syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-153.png)

## Entrée et sortie en Python et JavaScript

Demander une entrée utilisateur et afficher des valeurs à l'utilisateur sont des opérations très courantes. Voyons comment vous pouvez faire cela en Python et JavaScript :

### Entrée

* En **Python**, nous utilisons la fonction `**input()**` pour demander une entrée utilisateur. Nous écrivons le message entre parenthèses. 
* En **JavaScript**, une alternative (si vous exécutez le code dans un navigateur) est d'afficher une petite invite avec `**window.prompt(message)**` et d'assigner le résultat à une variable. 

La principale différence entre ces deux approches est qu'en Python, l'utilisateur sera invité à entrer une valeur dans la console tandis qu'en JavaScript, une petite invite sera affichée dans le navigateur et demandera à l'utilisateur d'entrer une valeur.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-161.png)

💡 **Conseil :** Vous verrez cela dans la console Python pour entrer une valeur :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-184.png)

En JavaScript, si vous ouvrez Chrome Developer tools et entrez cette ligne de code dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-163.png)

Cette invite sera affichée :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-162.png)
_Invite affichée lorsque window.prompt() est appelé_

### Sortie

* En **Python**, nous imprimons une valeur dans la console avec la fonction `**print()**`, en passant la valeur entre parenthèses. 
* En **JavaScript**, nous imprimons une valeur dans la console en utilisant `**console.log()**`, en passant également la valeur entre parenthèses.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-164.png)

💡 **Conseil :** Si vous travaillez sur un navigateur, vous pouvez également appeler `**alert()**` pour afficher une petite invite avec le message (ou la valeur) passé entre parenthèses. 

## Instructions conditionnelles en Python et JavaScript

Avec les conditionnelles, nous pouvons choisir ce qui se passe dans le programme en fonction de si une condition spécifique est `**True**` ou `**False**`. Voyons leurs différences en Python et JavaScript.

### Instruction `if`

* En **Python**, nous nous appuyons sur l'indentation pour indiquer quelles lignes de code appartiennent à la conditionnelle. 
* En **JavaScript**, nous devons entourer la condition de parenthèses et le code d'accolades. Le code doit également être indenté.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-154.png)
_Conditionnelle en Python (à gauche) et JavaScript (à droite)_

### Instruction `if/else`

La clause else est très similaire dans les deux langages. La seule différence est que :

* En **Python**, nous écrivons un deux-points (`**:**`) après le mot-clé `**else**` 
* En **JavaScript**, nous entourons le code qui appartient à cette clause d'accolades (`**{}**`). 

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-155.png)

### Conditions multiples

Pour écrire plusieurs conditions :

* En **Python**, nous écrivons le mot-clé `**elif**` suivi de la condition. Après la condition, nous écrivons un deux-points (`:`) et le code indenté sur la ligne suivante.
* En **JavaScript**, nous écrivons les mots-clés `**else if**` suivis de la condition (entourée de parenthèses). Après la condition, nous écrivons des accolades et le code indenté à l'intérieur des accolades. 

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-156.png)
_Conditionnelle en Python (à gauche) et JavaScript (à droite)_

### Switch en JavaScript

* En **JavaScript**, nous avons une structure de contrôle supplémentaire que nous pouvons utiliser pour choisir ce qui se passe en fonction de la valeur d'une expression. Cette instruction est appelée `**switch**`.
* **Python** n'a pas ce type de structure de contrôle intégrée.

Voici la syntaxe générale de cette instruction :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-159.png)
_Instruction switch en JavaScript_

En JavaScript :

```javascript
switch (expression) {
    case valeur1:
        // Code
        break;
    case valeur2:
        // Code
        break;
    case valeur3:
        // Code
        break;
    default:
        // Code
}
```

**💡 Conseil :** Nous pouvons ajouter autant de cas que nous en avons besoin et l'expression peut être une variable.

## Boucles For et While en Python et JavaScript

Voyons maintenant comment nous pouvons définir différents types de boucles en Python et JavaScript et leurs principales différences. 

### Boucles For

La syntaxe pour définir une boucle for en Python est relativement plus simple que la syntaxe en JavaScript. 

* En **Python**, nous écrivons le mot-clé `for` suivi du nom de la variable de boucle, du mot-clé `in`, et d'un appel à la fonction `range()` en spécifiant le(s) paramètre(s) nécessaire(s). Ensuite, nous écrivons un deux-points (`:`) suivi du corps de la boucle indenté. 
* En **JavaScript**, nous devons spécifier plusieurs valeurs explicitement. Nous commençons par le mot-clé `for` suivi de parenthèses. À l'intérieur de ces parenthèses, nous définissons la variable de boucle avec sa valeur initiale, la condition qui doit être `False` pour arrêter la boucle, et comment la variable sera mise à jour à chaque itération. Ensuite, nous écrivons des accolades pour créer un bloc de code et à l'intérieur des accolades, nous écrivons le corps de la boucle indenté. 

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-165.png)
_Boucle For en Python (à gauche) et JavaScript (à droite)_

### Itération sur des itérables

Nous pouvons utiliser une boucle for en Python et JavaScript pour itérer sur les éléments d'un itérable.

* En **Python**, nous écrivons le mot-clé `for` suivi de la variable de boucle, du mot-clé `in`, et de l'itérable. Ensuite, nous écrivons un deux-points (`:`) et le corps de la boucle (indenté).
* En **JavaScript**, nous pouvons utiliser une boucle `**for .. of**`. Nous écrivons le mot-clé `for` suivi de parenthèses et à l'intérieur de ces parenthèses, nous écrivons le mot-clé `var` ou `let` suivi de la variable de boucle, du mot-clé `of`, et de l'itérable. Nous entourons le corps de la boucle d'accolades et ensuite nous l'indentons.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-167.png)
_Boucle For en Python (à gauche) et JavaScript (à droite)_

En **JavaScript**, nous avons également des boucles `**for .. in**` pour itérer sur les propriétés d'un objet.

Selon [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in) :

> L'instruction **`for...in`** itère sur toutes les propriétés énumérables d'un objet qui sont clés par des chaînes (en ignorant celles clés par des Symboles), y compris les propriétés énumérables héritées.

Voici un exemple :

```javascript
const objet = { a: 1, b: 2, c: 3 };

for (const propriete in objet) {
  console.log(propriete, objet[propriete]);
}
```

La sortie lorsque nous exécutons ce code dans la console de Chrome Developer Tools est :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-168.png)

### Boucles While

Les boucles While sont très similaires en Python et JavaScript. 

* En **Python**, nous écrivons le mot-clé `while` suivi de la condition, un deux-points (`:`), et sur une nouvelle ligne, le corps de la boucle (indenté).
* En **JavaScript**, la syntaxe est très similaire. Les différences sont que nous devons entourer la condition de parenthèses et le corps de la boucle d'accolades.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-169.png)
_Boucle While en Python (à gauche) et JavaScript (à droite)_

### Boucles `do..while` en JavaScript

En **JavaScript**, nous avons également un type de boucle qui n'existe pas en Python. 

Ce type de boucle est appelé une boucle `**do..while**` car elle fait quelque chose au moins une fois et continue de s'exécuter tant qu'une condition est `True`. 

Voici la syntaxe de base :

```javascript
do {
    // Code
} while (condition);
```

💡 **Conseil :** Ce type de boucle garantit que le code sera exécuté au moins une fois. 

Cela est particulièrement utile lorsque nous demandons une entrée utilisateur car l'utilisateur sera invité à entrer l'entrée. Si l'entrée est valide, nous pouvons continuer avec le programme. Mais si elle n'est pas valide, nous pouvons inviter l'utilisateur à entrer la valeur à nouveau jusqu'à ce qu'elle soit valide.

## Fonctions en Python et JavaScript

Les fonctions sont incroyablement importantes pour écrire des programmes concis, maintenables et lisibles. La syntaxe est très similaire en Python et JavaScript, mais analysons leurs différences clés :

* En **Python**, nous écrivons le mot-clé `**def**` suivi du nom de la fonction, et à l'intérieur des parenthèses la liste des paramètres. Après cette liste, nous écrivons un deux-points (`:`) et le corps de la fonction (indenté). 
* En **JavaScript**, les seules différences sont que nous définissons une fonction en utilisant le mot-clé `**function**` et entourons le corps de la fonction d'accolades. 

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-170.png)
_Fonction en Python (en haut) et JavaScript (en bas)_

De plus, il y a une différence très importante entre les fonctions Python et JavaScript :

### Nombre d'arguments de fonction

* En **Python**, le nombre d'arguments passés à l'appel de fonction doit correspondre au nombre de paramètres définis dans la définition de la fonction (sauf si des valeurs par défaut leur ont été assignées dans la définition de la fonction). Si ce n'est pas le cas, une exception se produira.

Voici un exemple :

```python
>>> def foo(x, y):
	print(x, y)

	
>>> foo(3, 4, 5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    foo(3, 4, 5)
TypeError: foo() takes 2 positional arguments but 3 were given
```

* En **JavaScript**, cela n'est pas nécessaire puisque les paramètres sont optionnels. Vous pouvez appeler une fonction avec moins ou plus d'arguments que les paramètres qui ont été définis dans la définition de la fonction. Les arguments manquants sont assignés la valeur `**undefined**` par défaut et les arguments supplémentaires peuvent être accessibles avec l'objet `**arguments**`.

Voici un exemple en JavaScript :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-171.png)

Remarquez comment la fonction a été appelée avec trois arguments mais seulement deux paramètres ont été inclus dans la liste des paramètres de la définition de la fonction.

💡 **Conseil :** Pour obtenir le nombre d'arguments passés à la fonction, vous pouvez utiliser **`arguments.length`** à l'intérieur de la fonction. 

## Programmation orientée objet en Python et JavaScript

Python et JavaScript supportent tous deux la programmation orientée objet, alors voyons comment vous pouvez créer et utiliser les principaux éléments de ce paradigme de programmation.

### Classes

La première ligne d'une définition de classe est très similaire en Python et JavaScript. Nous écrivons le mot-clé `**class**` suivi du nom de la classe. 

La seule différence est que :

* En **Python**, après le nom de la classe, nous écrivons un deux-points (`**:**`) 
* En **JavaScript**, nous entourons le contenu de la classe d'accolades (`**{}**`)

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-172.png)
_Définition de classe en Python (à gauche) et JavaScript (à droite)_

**💡 Conseil :** En Python et JavaScript, les noms de classe doivent commencer par une lettre majuscule et chaque mot doit également commencer par une lettre majuscule.

### Constructeur et attributs

Le constructeur est une méthode spéciale qui est appelée lorsqu'une nouvelle instance de la classe (un nouvel objet) est créée. Son but principal est d'initialiser les attributs de l'instance.

* En **Python**, le constructeur qui initialise la nouvelle instance est appelé `**init**` (avec deux underscores de début et de fin). Cette méthode est appelée automatiquement lorsqu'une instance de la classe est créée pour initialiser ses attributs. Sa liste de paramètres définit les valeurs que nous devons passer pour créer l'instance. Cette liste commence par `**self**` comme premier paramètre.
* En **JavaScript**, la méthode constructeur est appelée `**constructor**` et elle a également une liste de paramètres. 

**💡 Conseil :** En Python, nous utilisons `**self**` pour faire référence à l'instance tandis qu'en JavaScript nous utilisons `**this**`.

Pour assigner des valeurs aux attributs en **Python**, nous utilisons cette syntaxe :

```
self.attribut = valeur
```

En revanche, nous utilisons cette syntaxe en **JavaScript** :

```
this.attribut = valeur;
```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-174.png)
_Exemple de classe en Python (à gauche) et JavaScript (à droite)_

## Méthodes en Python et JavaScript

* En **Python**, nous définissons des méthodes avec le mot-clé `**def**` suivi de leur nom et de la liste des paramètres à l'intérieur des parenthèses. Cette liste de paramètres commence par le paramètre `**self**` pour faire référence à l'instance qui appelle la méthode. Après cette liste, nous écrivons un deux-points (`**:**`) et le corps de la méthode indenté. 

Voici un exemple :

```python
class Cercle:

	def __init__(self, rayon, couleur):
		self.rayon = rayon
		self.couleur = couleur

	def calc_diametre(self):
		return self.rayon * 2
```

* En **JavaScript**, les méthodes sont définies en écrivant leur nom suivi de la liste des paramètres et des accolades. À l'intérieur des accolades, nous écrivons le corps de la méthode. 

```javascript
class Cercle {

    constructor(rayon, couleur) {
        this.rayon = rayon;
        this.couleur = couleur;
    }

    calcDiametre() {
        return this.rayon * 2;
    }
}
```

### Instances

Pour créer des instances d'une classe :

* En **Python**, nous écrivons le nom de la classe et passons les arguments à l'intérieur des parenthèses.

```python
mon_cercle = Cercle(5, "Rouge")
```

* En **JavaScript**, nous devons ajouter le mot-clé `**new**` avant le nom de la classe. 

```javascript
mon_cercle = new Cercle(5, "Rouge");
```

## 🔹 Pour résumer

Python et JavaScript sont des langages très puissants avec différentes applications réelles. 

Python peut être utilisé pour le développement web et pour une large gamme d'applications, y compris à des fins scientifiques. JavaScript est principalement utilisé pour le développement web (front-end et back-end) et pour le développement d'applications mobiles. 

Ils ont des différences importantes, mais ils ont tous deux les mêmes éléments de base dont nous avons besoin pour écrire des programmes puissants. 

**J'espère que vous avez aimé cet article et que vous l'avez trouvé utile.** Maintenant, vous connaissez les différences clés entre Python et JavaScript. 

⭐ [**Abonnez-vous à ma chaîne YouTube**](https://www.youtube.com/channel/UCng0h8WiHLmT57JJ8At4LfQ) et suivez-moi sur [**Twitter**](https://twitter.com/EstefaniaCassN) pour trouver plus de tutoriels et de conseils de codage.