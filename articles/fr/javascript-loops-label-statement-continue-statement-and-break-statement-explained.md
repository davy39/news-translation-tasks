---
title: 'Boucles JavaScript : Déclaration Label, Déclaration Continue et Déclaration
  Break Expliquées'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-04T22:27:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-loops-label-statement-continue-statement-and-break-statement-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cca740569d1a4ca3436.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
- name: toothbrush
  slug: toothbrush
seo_title: 'Boucles JavaScript : Déclaration Label, Déclaration Continue et Déclaration
  Break Expliquées'
seo_desc: "Label Statement\nThe Label Statement is used with the break and continue\
  \ statements and serves to identify the statement to which the break and continue\
  \ statements apply. \nWe'll talk more about the break and continue statements below.\n\
  Syntax\nlabelname..."
---

## **Déclaration Label**

La **déclaration Label** est utilisée avec les instructions `break` et `continue` et sert à identifier l'instruction à laquelle les instructions `break` et `continue` s'appliquent.

Nous parlerons plus en détail des instructions `break` et `continue` ci-dessous.

### **Syntaxe**

```javascript
nomEtiquette:
  instructions
```

### **Utilisation**

Sans l'utilisation d'une instruction `labeled`, l'instruction `break` ne peut sortir que d'une boucle ou d'une instruction `switch`. L'utilisation d'une instruction `labeled` permet à `break` de sortir de n'importe quel bloc de code.

#### **Exemple**

```javascript
foo: {
  console.log("Ceci s'affiche :");
  break foo;
  console.log("Ceci ne s'affichera jamais.");
}
console.log("Car l'exécution saute ici !")
/* sortie
Ceci s'affiche :
Car l'exécution saute ici ! */
```

Lorsque vous utilisez une instruction `continue`, l'instruction `labeled` vous permet de sauter une itération de boucle. L'avantage est de pouvoir sortir d'une boucle interne vers une boucle externe lorsque vous avez des instructions de boucle imbriquées. Sans l'utilisation d'une instruction `labeled`, vous ne pourriez sortir que de l'itération de boucle actuelle vers `l'itération suivante de la même boucle`.

#### **Exemple**

```javascript
// sans instruction labeled, lorsque j==i, la boucle interne saute à l'itération suivante
function test() {
  for (var i = 0; i < 3; i++) {
    console.log("i=" + i);
    for (var j = 0; j < 3; j++) {
      if (j === i) {
        continue;
      }
      console.log("j=" + j);
    }
  }
}

/* sortie
i=0 (notez que j=0 est manquant)
j=1
j=2
i=1
j=0 (notez que j=1 est manquant)
j=2
i=2
j=0
j=1 (notez que j=2 est manquant)
*/

// en utilisant une instruction labeled, nous pouvons sauter vers la boucle externe (i) à la place
function test() {
  outer: for (var i = 0; i < 3; i++) {
    console.log("i=" + i);
    for (var j = 0; j < 3; j++) {
      if (j === i) {
        continue outer;
      }
      console.log("j=" + j);
    }
  }
}

/*
i=0 (j est enregistré uniquement lorsqu'il est inférieur à i)
i=1
j=0
i=2
j=0
j=1
*/
```

## **Instruction Break**

L'instruction **break** termine la boucle, l'instruction `switch` ou l'instruction `label` actuelle et transfère le contrôle du programme à l'instruction suivant l'instruction terminée.

```text
break;
```

Si l'instruction **break** est utilisée dans une instruction labeled, la syntaxe est la suivante :

```text
break nomEtiquette;
```

### Exemples

La fonction suivante contient une instruction **break** qui termine la boucle `while` lorsque **i** est égal à 3, puis retourne la valeur **3 * x**.

```text
function testBreak(x) {
  var i = 0;

  while (i < 6) {
    if (i == 3) {
      break;
    }
    i += 1;
  }

  return i * x;
}
```

🚀

[Exécuter le Code](https://repl.it/C7VM/0)

Dans l'exemple suivant, le compteur est configuré pour compter de 1 à 99 ; cependant, l'instruction **break** termine la boucle après 14 comptages.

```text
for (var i = 1; i < 100; i++) {
  if (i == 15) {
    break;
  }
}
```

🚀

[Exécuter le Code](https://repl.it/C7VO/0)

## **Instruction Continue**

L'instruction **continue** termine l'exécution des instructions dans l'itération actuelle de la boucle actuelle ou labeled, et continue l'exécution de la boucle avec l'itération suivante.

```text
continue;
```

Si l'instruction **continue** est utilisée dans une instruction labeled, la syntaxe est la suivante :

```text
continue nomEtiquette;
```

Contrairement à l'instruction **break**, **continue** ne termine pas entièrement l'exécution de la boucle ; au lieu de cela :

* Dans une boucle `while`, elle revient à la condition.
* Dans une boucle `for`, elle saute à l'expression de mise à jour.

### Exemples

L'exemple suivant montre une boucle `while` qui contient une instruction **continue** qui s'exécute lorsque la valeur de **i** est 3. Ainsi, **n** prend les valeurs 1, 3, 7 et 12.

```text
var i = 0;
var n = 0;

while (i < 5) {
  i++;

  if (i === 3) {
    continue;
  }

  n += i;
  console.log (n);
}
```

🚀

[Exécuter le Code](https://repl.it/C7hx/0)

Dans l'exemple suivant, une boucle itère de 1 à 9. Les instructions entre **continue** et la fin du corps du `for` sont ignorées en raison de l'utilisation de l'instruction **continue** avec l'expression `(i < 5)`.

```text
for (var i = 1; i < 10; i++) {
    if (i < 5) {
        continue;
    }
    console.log (i);
}
```

🚀

[Exécuter le Code](https://repl.it/C7hs/0)