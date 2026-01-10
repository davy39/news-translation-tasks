---
title: Comment analyser les S-expressions en JavaScript
subtitle: ''
author: Jakub T. Jankiewicz
co_authors: []
series: null
date: '2024-04-04T22:22:06.000Z'
originalURL: https://freecodecamp.org/news/s-expressions-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/lisp-parser_2.png
tags:
- name: JavaScript
  slug: javascript
- name: Regular Expressions
  slug: regular-expressions
seo_title: Comment analyser les S-expressions en JavaScript
seo_desc: "S-expressions are the base of the Lisp family of programming languages.\
  \ In this article, I will show you how to create a simple S-expression parser step\
  \ by step. This can be a base for the Lisp parser. \nLisp is the easiest language\
  \ for implementation..."
---

Les S-expressions sont la base de la famille de langages de programmation Lisp. Dans cet article, je vais vous montrer comment créer un analyseur de S-expressions simple étape par étape. Cela peut servir de base pour l'analyseur Lisp. 

Lisp est le langage le plus facile à implémenter, et la création d'un analyseur est la première étape. Nous pouvons utiliser un générateur d'analyseur pour cela, mais il est plus facile d'écrire l'analyseur vous-même. Nous utiliserons JavaScript.

## Qu'est-ce que les S-expressions ?

Si vous n'êtes pas familier avec le langage Lisp, les S-expressions ressemblent à ceci :

```scheme
(+ (second (list "xxx" 10)) 20)

```

C'est un format de données, où tout est créé à partir d'atomes ou de listes entourées de parenthèses (où les atomes ou autres listes sont séparés par des espaces).

Les S-expressions peuvent avoir différents types de données, tout comme JSON :

* nombres
* chaînes de caractères
* symboles – qui sont comme des chaînes de caractères mais sans guillemets – peuvent être interprétés comme des noms de variables dans différents langages.

De plus, vous pouvez utiliser un opérateur spécial de point qui crée une paire.

```scheme
(1 . b)

```

Vous pouvez représenter une liste comme des paires pointées (ce qui indique qu'elles sont en fait une structure de données de liste chaînée). 

Cette liste :

```scheme
(1 2 3 4)

```

Peut être écrite comme :

```scheme
(1 . (2 . (3 . (4 . nil))))

```

`nil` est le symbole spécial qui indique la fin de la liste ou une liste vide. Avec ce format, vous pouvez créer n'importe quel arbre binaire. Mais nous n'utiliserons pas cette notation pointée dans notre analyseur pour ne pas compliquer les choses.

## À quoi servent les S-expressions ?

Le code Lisp est créé à partir de S-expressions, mais vous pouvez également les utiliser comme format d'échange de données.

Elles font également partie de la [représentation textuelle de WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly/Understanding_the_text_format). Probablement en raison de la simplicité de l'analyseur, et du fait que vous n'avez pas besoin de créer votre propre format. Vous pouvez les utiliser pour la communication entre le serveur et le navigateur, au lieu de JSON.

### Comment implémenter un analyseur de S-expressions en JavaScript

#### Tokenizer 

Le tokenizer est une partie de l'analyseur qui divise le texte en tokens qui peuvent ensuite être analysés.

Habituellement, un analyseur est accompagné d'un Lexer ou d'un tokenizer qui génère les tokens. 
C'est ainsi que fonctionnent certains générateurs d'analyseurs (comme lex et Yacc ou flex et bison. Le second est un logiciel libre et open source, faisant partie du projet GNU). 

La manière la plus simple de tokeniser est d'utiliser des expressions régulières. Si vous n'êtes pas familier avec les expressions régulières (ou Regex en abrégé), vous pouvez lire cet article : 
[Un guide pratique des expressions régulières – Apprendre Regex avec des exemples concrets](https://www.freecodecamp.org/news/practical-regex-guide-with-real-life-examples/).

Voici la manière la plus simple de tokenisation :

```javascript
'(foo bar (baz))'.split(/(\(|\)|\n|\s+|\S+)/);

```

C'est une union (avec un opérateur pipe) de différents cas que nous devons gérer. Les parenthèses sont des caractères spéciaux dans Regex, elles doivent donc être échappées par une barre oblique.

Cela fonctionne presque. Le premier problème est qu'il y a des chaînes vides entre les correspondances regex. Comme cette expression :

```javascript
'(('.split(/(\(|\)|\n|\s+|\S+)/);
// ==> [ '', '(', '', '(', '' ]

```

Nous avons 5 tokens au lieu de 2. Nous pouvons résoudre ce problème avec un [Array::filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter).

```javascript
'(('.split(/(\(|\)|\n|\s+|\S+)/).filter(token => token.length);
// ==> ["(", "("]

```

Si le token est vide, la longueur retournera `0` et sera convertie en `false`, ce qui signifie qu'il filtrera toutes les chaînes vides.

Nous n'aurons également pas besoin d'espaces, nous pouvons donc également les filtrer :

```javascript
'(   ('.split(/(\(|\)|\n|\s+|\S+)/).filter(token => token.trim().length);
// ==> ["(", "("]

```

Le deuxième problème plus important est avec `baz))` comme dernier token, voici un exemple :

```javascript
'(foo bar (baz))'.split(/(\(|\)|\n|\s+|\S+)/).filter(token => token.trim().length);
// ==> ["(", "foo", "bar", "(", "baz))"]

```

Le problème est l'expression `\S+`, qui est gourmande et correspond à tout ce qui n'est pas un espace. Pour résoudre le problème, nous pouvons utiliser cette expression : `[^\s()]+`.

Elle correspondra à tout ce qui n'est pas un espace et pas une parenthèse (même que `\S+` mais avec des parenthèses).

```javascript
(foo bar (baz))'.split(/(\(|\)|\n|\s+|[^\s()]+)/).filter(token => token.trim().length);
// ==> ["(", "foo", "bar", "(", "baz", ")", ")"]

```

Comme vous pouvez le voir, la sortie est correcte. Écrivons ce tokenizer sous forme de fonction :

```javascript
const tokens_re = /(\(|\)|\n|\s+|[^\s()]+)/;
function tokenize(string) {
    string = string.trim();
    if (!string.length) {
        return [];
    }
    return string.split(tokens_re).filter(token => token.trim());
}

```

Nous n'avons pas besoin d'utiliser `length` après `token.trim()` car une chaîne vide est également convertie en valeur `false` et le filtre supprimera ces valeurs.

Mais qu'en est-il des expressions de chaînes (celles entre guillemets) ? Voyons ce qui se passera :

```javascript
tokenize(`(define (square x)
            "Function calculate square of a number"
            (* x x))`);
// ==> ["(", "define", "(", "square", "x", ")", "\"Function", "calculate", "square",
// ==>  "of", "a", "number\"", "(", "*", "x", "x", ")", ")"]

```

**NOTE :** Ceci est une fonction dans le dialecte Scheme de Lisp. Nous avons utilisé des littéraux de gabarit pour pouvoir ajouter des caractères de nouvelle ligne à l'intérieur du code Lisp.

Comme vous pouvez le voir dans la sortie, les chaînes simples sont toutes divisées par des espaces. Corrigons cela :

##### Expressions régulières pour les chaînes

Nous devons ajouter les littéraux de chaîne comme une exception à notre tokenizer. Le mieux est le premier élément de l'union dans notre regex. 

L'expression qui gère les littéraux de chaîne ressemble à ceci :

```javascript
/"[^"\\]*(?:\\[\S\s][^"\\]*)*"/

```

Elle gère les guillemets échappés à l'intérieur d'une chaîne.

Voici à quoi devrait ressembler l'expression régulière complète :

```javascript
const tokens_re = /("[^"\\]*(?:\\[\S\s][^"\\]*)*"|\(|\)|\n|\s+|[^\s()]+)/;

```

**NOTE :** Nous pouvons également ajouter des commentaires Lisp, mais comme ceci n'est pas un analyseur Lisp mais S-expression, nous ne le ferons pas ici. JSON ne supporte pas non plus les commentaires. Si vous souhaitez créer un analyseur Lisp, vous pouvez les ajouter comme exercice.

Notre tokenizer fonctionne maintenant correctement :

```javascript
tokenize(`(define (square x)
            "Function calculate square of a number"
            (* x x))`);
// ==> ["(", "define", "(", "square", "x", ")",
// ==>  "\"Function calculate square of a number\"",
// ==>  "(", "*", "x", "x", ")", ")"]

```

#### Analyseur

Nous allons créer notre analyseur en utilisant une [structure de données de pile](https://www.freecodecamp.org/news/learn-data-structures-and-algorithms/) (LIFO - Last In First Out).

Pour comprendre pleinement comment fonctionne l'analyseur, il est bon de connaître les structures de données, comme les listes chaînées, les arbres binaires et les piles.

Voici la première version de notre analyseur :

```javascript
function parse(string) {
    const tokens = tokenize(string);
    const result = []; // en tant que tableau normal
    const stack = []; // en tant que pile
    tokens.forEach(token => {
        if (token == '(') {
            stack.push([]); // ajoute une nouvelle liste à la pile
        } else if (token == ')') {
            if (stack.length) {
                // le sommet de la pile est une liste déjà construite
                const top = stack.pop();
                if (stack.length) {
                    // ajoute la liste construite à la liste précédente
                    var last = stack[stack.length - 1];
                    last.push(top);
                } else {
                    result.push(top); // liste entièrement construite
                }
            } else {
                throw new Error('Erreur de syntaxe - parenthèse fermante non appariée');
            }
        } else {
            // atome trouvé, ajoute au sommet de la pile
            // le sommet est utilisé comme un tableau, nous ajoutons uniquement à la fin
            const top = stack[stack.length - 1];
            top.push(token);
        }
    });
    if (stack.length) {
        throw new Error('Erreur de syntaxe - parenthèse fermante attendue');
    }
    return result;
}

```

La fonction retourne un tableau de nos structures sous forme de tableaux. Si nous devons analyser plus d'une S-expression, nous aurons plus d'éléments dans un tableau :

```javascript
parse(`(1 2 3) (1 2 3)`)
// ==> [["1", "2", "3"], ["1", "2", "3"]]

```

Bien que nous n'ayons pas besoin de gérer les points, les S-expressions peuvent être sous cette forme :

```scheme
((foo . 10) (bar . 20))

```

Nous n'avons pas besoin de créer une structure spéciale pour nos listes pour avoir un analyseur fonctionnel. Mais c'est une bonne idée d'avoir cette structure dès le début (pour que vous puissiez l'utiliser comme base pour un interpréteur Lisp). Nous utiliserons une classe `Pair`, pour pouvoir créer n'importe quel arbre binaire.

```javascript
class Pair {
    constructor(head, tail) {
        this.head = head;
        this.tail = tail;
    }
}

```

Nous aurons également besoin de quelque chose qui représentera la fin de la liste (ou une liste vide). Dans le langage Lisp, c'est généralement `nil` :

```javascript
class Nil {}
const nil = new Nil();

```

Nous pouvons créer une méthode statique qui convertira un tableau en notre structure :

```javascript
class Pair {
    constructor(head, tail) {
        this.head = head;
        this.tail = tail;
    }
    static fromArray(array) {
        if (!array.length) {
            return nil;
        }
        let [head, ...rest] = array
        if (head instanceof Array) {
            head = Pair.fromArray(head);
        }
        return new Pair(head, Pair.fromArray(rest));
    }
}

```

Pour ajouter cela à notre analyseur, tout ce que nous avons à faire est de l'ajouter à la fin :

```javascript
result.map(Pair.fromArray);

```

**NOTE :** Si vous souhaitez ajouter un opérateur de point plus tard, vous devrez créer des paires manuellement, à l'intérieur de l'analyseur.

Nous n'avons pas converti le tableau entier car cela sera le conteneur pour nos S-expressions. Chaque élément d'un tableau doit être une liste, c'est pourquoi nous avons utilisé [Array::map](https://www.freecodecamp.org/news/javascript-map-reduce-and-filter-explained-with-examples/).

Voyons comment cela fonctionne :

```javascript
parse('(1 (1 2 3))')

```

La sortie sera une structure comme celle-ci (c'est la sortie de `JSON.stringify` avec la valeur insérée de `nil`).

```javascript
{
    "head": "1",
    "tail": {
        "head": {
            "head": "1",
            "tail": {
                "head": "2",
                "tail": {
                    "head": "3",
                    "tail": nil
                }
            }
        },
        "tail": nil
    }
}

```

La dernière chose que nous pouvons ajouter est de `stringify` la Liste, en ajoutant une méthode `toString` à notre classe `Pair` :

```javascript
class Pair {
    constructor(head, tail) {
        this.head = head;
        this.tail = tail;
    }
    toString() {
        const arr = ['('];
        if (this.head) {
            const value = this.head.toString();
            arr.push(value);
            if (this.tail instanceof Pair) {
                // remplacer le hack pour la liste imbriquée
                // car la structure est un arbre
                // et ici la queue est l'élément suivant
                const tail = this.tail.toString().replace(/^\(|\)$/g, '');
                arr.push(' ');
                arr.push(tail);
            }
        }
        arr.push(')');
        return arr.join('');
    }
    static fromArray(array) {
        // ... même chose qu'avant
    }
}

```

Voyons comment cela fonctionne :

```javascript
parse("(1 (1 2 (3)))")[0].toString()
// ==> "(1 (1 2 (3)))"

```

Le dernier problème est que la structure de sortie n'a pas de nombres. Tout est une chaîne.

#### Analyse des atomes

Nous utiliserons les expressions régulières suivantes :

```javascript
const int_re = /^[-+]?[0-9]+([eE][-+]?[0-9]+)?$/;
const float_re = /^([-+]?((\.[0-9]+|[0-9]+\.[0-9]+)([eE][-+]?[0-9]+)?)|[0-9]+\.)$/;
if (atom.match(int_re) || atom.match(float_re)) {
    // en javascript, chaque nombre est un float, mais si c'est lent, vous pouvez utiliser parseInt pour int_re
    return parseFloat(atom);
}

```

Ensuite, nous pouvons analyser les chaînes. Nos chaînes sont presque les mêmes que celles de JSON, la seule différence est qu'elles peuvent contenir des nouvelles lignes (c'est généralement ainsi que les chaînes sont gérées dans les dialectes Lisp). Nous pouvons donc utiliser `JSON.parse` et remplacer `\n` par `\\n` (échapper la nouvelle ligne).

```javascript
if (atom.match(/^".*"$/)) {
   return JSON.parse(atom.replace(/\n/g, '\\n'));
}

```

Ainsi, nous pouvons avoir tous les caractères d'échappement gratuitement (c'est-à-dire : `\t` ou les caractères Unicode `\u`).

L'élément suivant des S-expressions est les symboles. Ils sont toute séquence de caractères qui ne sont pas des nombres ou des chaînes. Nous pouvons créer une classe `LSymbol`, pour la distinguer de `Symbol` de JavaScript.

```javascript
class LSymbol {
    constructor(name) {
        this.name = name;
    }
    toString() {
        return this.name;
    }
}

```

La fonction pour analyser les atomes peut ressembler à ceci :

```javascript
function parseAtom(atom) {
    if (atom.match(int_re) || atom.match(float_re)) { // nombres
        return parseFloat(atom);
    } else if (atom.match(/^".*"$/)) {
       return JSON.parse(atom.replace(/\n/g, '\\n')); // chaînes
    } else {
       return new LSymbol(atom); // symboles
    }
}

```

Notre fonction d'analyseur avec l'ajout de `parseAtom` :

```javascript
function parse(string) {
    const tokens = tokenize(string);
    const result = [];
    const stack = [];
    tokens.forEach(token => {
        if (token == '(') {
           stack.push([]);
        } else if (token == ')') {
           if (stack.length) {
               const top = stack.pop();
               if (stack.length) {
                  const last = stack[stack.length - 1];
                  last.push(top);
               } else {
                  result.push(top);
               }
           } else {
               throw new Error('Erreur de syntaxe - parenthèse fermante non appariée');
           }
        } else {
           const top = stack[stack.length - 1];
           top.push(parseAtom(token)); // cette ligne a été ajoutée
        }
    });
    if (stack.length) {
        throw new Error('Erreur de syntaxe - parenthèse fermante attendue');
    }
    return result.map(Pair.fromArray);
}

```

Nous pouvons également améliorer la méthode `toString` sur `Pair` pour utiliser `JSON.stringify` pour les chaînes afin de les distinguer des symboles :

```javascript
class Pair {
    constructor(head, tail) {
        this.head = head;
        this.tail = tail;
    }
    toString() {
        const arr = ['('];
        if (this.head) {
            let value;
            if (typeof this.head === 'string') {
                value = JSON.stringify(this.head).replace(/\\n/g, '\n');
            } else {
                // tout objet incluant Pair et LSymbol
                value = this.head.toString(); 
            }
            arr.push(value);
            if (this.tail instanceof Pair) {
                // remplacer le hack pour la liste imbriquée car
                // la structure est un arbre et ici la queue
                // est l'élément suivant
                const tail = this.tail.toString().replace(/^\(|\)$/g, '');
                arr.push(' ');
                arr.push(tail);
            }
        }
        arr.push(')');
        return arr.join('');
    }
    static fromArray(array) {
        // ... même chose qu'avant
    }   
}

```

Et voici un analyseur complet. Il reste les valeurs `true` et `false` (et peut-être `null`), mais elles sont laissées comme exercice pour le lecteur. Le code complet peut être trouvé sur [GitHub](https://gist.github.com/jcubic/ca6548847137584138823f3ba90a002a).

## Différentes approches de l'analyseur Lisp en JavaScript

Le code ci-dessus est bon pour une implémentation simple de Lisp. J'ai utilisé un code similaire comme implémentation initiale de [LIPS Scheme](https://lips.js.org/), qui peut encore être trouvé sur [CodePen](https://codepen.io/jcubic/pen/gvvzdp).

Actuellement, LIPS utilise un Lexer plus avancé (utilisant une [machine à états](https://w.wiki/5v8)) au lieu d'un tokenizer. Le Lexer a été réécrit car l'approche avec la pile était trop difficile à modifier.

**NOTE :** Cet article est d'abord apparu sur le blog polonais [**Głównie JavaScript**](https://jcubic.pl/) (ang. Mostly JavaScript), l'article s'intitulait : [Parser S-Wyrażeń (języka LISP) w JavaScript](https://jcubic.pl/2019/06/parser-jezyka-lisp-javascript.html).