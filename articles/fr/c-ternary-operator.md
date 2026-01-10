---
title: Opérateur ternaire en C expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-20T17:00:00.000Z'
originalURL: https://freecodecamp.org/news/c-ternary-operator
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9db2740569d1a4ca3922.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: Opérateur ternaire en C expliqué
seo_desc: 'Programmers use the ternary operator for decision making in place of longer
  if and else conditional statements.

  The ternary operator take three arguments:


  The first is a comparison argument

  The second is the result upon a true comparison

  The third i...'
---

Les programmeurs utilisent l'**opérateur ternaire** pour la prise de décision à la place des instructions conditionnelles **if** et **else** plus longues.

L'opérateur ternaire prend trois arguments :

1. Le premier est un argument de comparaison
2. Le second est le résultat en cas de comparaison vraie
3. Le troisième est le résultat en cas de comparaison fausse

Il est utile de considérer l'opérateur ternaire comme une manière abrégée d'écrire une instruction if-else. Voici un exemple simple de prise de décision utilisant **if** et **else** :

```c
int a = 10, b = 20, c;

if (a < b) {
    c = a;
}
else {
    c = b;
}

printf("%d", c);
```

Cet exemple prend plus de 10 lignes, mais ce n'est pas nécessaire. Vous pouvez écrire le programme ci-dessus en seulement 3 lignes de code en utilisant un opérateur ternaire.

### **Syntaxe**

`condition ? valeur_si_vrai : valeur_si_faux`

L'instruction évalue `valeur_si_vrai` si `condition` est remplie, et `valeur_si_faux` sinon.

Voici l'exemple ci-dessus réécrit pour utiliser l'opérateur ternaire :

```c
int a = 10, b = 20, c;

c = (a < b) ? a : b;

printf("%d", c);
```

La sortie de l'exemple ci-dessus devrait être :

```c
10
```

`c` est défini égal à `a`, car la condition `a < b` était vraie.

Rappelez-vous que les arguments `valeur_si_vrai` et `valeur_si_faux` doivent être du même type, et ils doivent être des expressions simples plutôt que des instructions complètes.

Les opérateurs ternaires peuvent être imbriqués tout comme les instructions if-else. Considérez le code suivant :

```c
int a = 1, b = 2, ans;
if (a == 1) {
    if (b == 2) {
        ans = 3;
    } else {
        ans = 5;
    }
} else {
    ans = 0;
}
printf ("%d\n", ans);
```

Voici le code ci-dessus réécrit en utilisant un opérateur ternaire imbriqué :

```c
int a = 1, b = 2, ans;
ans = (a == 1 ? (b == 2 ? 3 : 5) : 0);
printf ("%d\n", ans);
```

La sortie des deux ensembles de code ci-dessus devrait être :

```c
3
```