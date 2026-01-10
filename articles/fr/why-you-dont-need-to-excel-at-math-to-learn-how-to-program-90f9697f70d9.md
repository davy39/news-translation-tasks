---
title: Pourquoi vous n'avez pas besoin d'exceller en maths pour apprendre à programmer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-10T17:50:11.000Z'
originalURL: https://freecodecamp.org/news/why-you-dont-need-to-excel-at-math-to-learn-how-to-program-90f9697f70d9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*a_YBHDaex8qNOUBV.
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Pourquoi vous n'avez pas besoin d'exceller en maths pour apprendre à programmer
seo_desc: 'By Pau Pavón

  This is probably one of the greatest misconceptions I’ve ever heard.

  If you want to program, you must be good at math. It’s totally fake. Let me explain.

  You don’t need to excel at math to learn to code

  I started coding when I was 12 yea...'
---

Par Pau Pavón

Ceci est probablement l'un des plus grands malentendus que j'aie jamais entendus.

Si vous voulez programmer, vous devez être bon en maths. C'est totalement faux. Laissez-moi expliquer.

### Vous n'avez pas besoin d'exceller en maths pour apprendre à coder

J'ai commencé à coder quand j'avais 12 ans. Les maths que je connaissais étaient l'addition, la soustraction, la multiplication et la division. Et c'était **plus que suffisant** pour entrer dans le monde de la programmation. Même aujourd'hui, je n'utilise rien de plus complexe que les puissances ou les racines carrées.

Si vous avez déjà programmé ne serait-ce qu'une ligne de code, vous avez probablement réalisé que cela n'a presque rien à voir avec les maths. Si vous savez compter, vous êtes déjà bien parti.

### L'origine du mythe

Je crois avoir compris d'où vient ce 'mythe'. Vous connaissez ces vieux films (ou pas si vieux) sur les hackers et les programmeurs. Ils montrent souvent des ordinateurs avec beaucoup de 0 et de 1 dans une police verdâtre, défilant verticalement à l'écran ? C'est du code binaire (et il ne bouge pas normalement à l'écran, c'est juste du texte statique).

Les ordinateurs comprennent le code binaire, mais ce n'est pas de cela que traitent les langages de programmation. Cela peut sembler assez évident, car si vous lisez ceci, vous avez probablement un certain lien avec ce monde. Mais vous seriez surpris de voir combien de personnes pensent que tout est question de binaire.

![Image](https://cdn-media-1.freecodecamp.org/images/zzjUB1ePlD2vT4wPb2rx2aO4YZGyrrLmYLCX)
_Quand je code, mon écran ne ressemble pas à ça. Peut-être que je fais quelque chose de mal. Photo par [Unsplash](https://unsplash.com/@markusspiske?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Markus Spiske</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Mais outre cette idée fausse, je pense que l'autre facteur est la relation établie entre les mots _maths_ et _logique_. La programmation nécessite une pensée logique, et les maths aussi. Mais le golf et le basket-ball nécessitent tous deux une balle pour être joués, et cela ne signifie pas que vous devez savoir jouer au basket-ball pour vous mettre au golf.

### Vous faire croire ce que je viens de dire

Prenons un exemple concret. Imaginez que vous voulez créer une fonction pour afficher la table de multiplication d'un nombre. Donc, pour l'entrée 2, notre fonction retournera :

> 2 x 0 = 0

> 2 x 1 = 2

> 2 x 2 = 4

> 2 x 3 = 6

> …

> Et jusqu'à 2 x 10 = 20

Vous verrez combien peu de maths sont nécessaires pour faire cela (même si nous calculons quelque chose de 'mathématique'). Pour les besoins de cet exemple, nous utiliserons JavaScript.

Tout d'abord, nous déclarons la **fonction**. Nous l'appellerons **_tableDe(n)_**, où _n_ est le nombre dont nous voulons afficher la table.

```
function tableDe(n) {
```

```
//reste du code
```

```
}
```

Assez facile pour le moment. Maintenant, nous allons implémenter quelque chose appelé une **boucle for**. Cela ressemble à une fonction sauf que, lorsqu'elle atteint la fin, elle revient au début jusqu'à ce qu'une certaine condition soit vraie.

Nous voulons afficher _n_ fois une autre valeur (appelons-la _i_) jusqu'à ce que cette valeur atteigne 10. Nous devons également prendre en compte que _i_ doit commencer à 0, car nous voulons que _n x 0 = 0_ soit la première ligne affichée. Le code pourrait être le suivant :

```
for(i = 0; i < 11; i++) {
```

```
console.log(n, 'x', i, '=', n*i);
```

```
}
```

Passons en revue ce que nous venons de faire. Nous avons commencé la boucle for avec _i = 0_, ce qui signifie que _i_ commence à 0 (comme nous le voulions). Ensuite, nous disons i < 11, ce qui signifie que nous ne voulons pas sortir de la boucle tant que i est égal à 11 ou, en d'autres termes, nous voulons que la boucle continue si i est inférieur à 11. Ensuite, nous faisons i++, ce qui signifie que nous augmentons la valeur de i de 1 à chaque fois que la boucle recommence (pour qu'elle atteigne finalement 11 et sorte de la boucle).

Ensuite, nous affichons simplement _n_ (le nombre que nous avons entré), 'x' (pour le symbole _fois_), _i_ (le nombre par lequel _n_ est multiplié), '=' (pour le symbole _égal_), et enfin _n*i_ (l'opération réelle, _n fois i_).

Le code précédent, combiné :

```
function tableDe(n) {
```

```
for(i = 0; i < 11; i++) {
```

```
console.log(n, 'x', i, '=', n*i);
```

```
}
```

```
}
```

```
tableDe(2);
```

Et cela fonctionne. Est-ce des maths difficiles ? Les seules maths que nous avons faites étaient d'augmenter _i_ de un (addition), et de vérifier si _i_ était inférieur à 11. Pour cet exemple concret, nous avons également multiplié _n_ par _i_. **Wow**.

### L'autre côté de la médaille

Apprendre à coder vous rendra meilleur en maths.

Comme je l'ai dit auparavant, la programmation nécessite une pensée logique tout comme les maths. En écrivant vos programmes, vous rencontrerez beaucoup de problèmes qui doivent être résolus. La plupart du temps avec de la logique (mais soyons honnêtes, parfois l'essai et l'erreur fonctionnent très bien).

Développer les compétences pour résoudre ces problèmes va définitivement vous aider avec les maths — non seulement avec les concepts, mais aussi avec la résolution de problèmes. Vous pouvez étendre cela à d'autres disciplines également, comme la physique.

J'espère que cet article servira à encourager les personnes qui veulent essayer de coder à le faire. Croyez-moi, je savais peu de choses sur les maths et encore moins sur l'anglais, et j'ai quand même pu apprendre beaucoup. La connaissance n'a pas de limites.