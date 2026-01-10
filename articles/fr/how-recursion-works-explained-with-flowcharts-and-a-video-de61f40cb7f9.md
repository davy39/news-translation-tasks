---
title: Comment fonctionne la récursivité — Expliqué avec des organigrammes et une
  vidéo
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2017-08-22T20:07:58.000Z'
originalURL: https://freecodecamp.org/news/how-recursion-works-explained-with-flowcharts-and-a-video-de61f40cb7f9
coverImage: null
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne la récursivité — Expliqué avec des organigrammes et
  une vidéo
seo_desc: 'Illustration (and all in this article) by Adit Bhargava


  “In order to understand recursion, one must first understand recursion.”


  Recursion can be tough to understand — especially for new programmers. In its simplest
  form, a recursive function is on...'
---

![Image](https://cdn-media-1.freecodecamp.org/images/1*FVSUmSQEEsagXaKa_ajtvA.png)
_Illustration (et toutes celles de cet article) par Adit Bhargava_

> « Pour comprendre la récursivité, il faut d'abord comprendre la récursivité. »

La récursivité peut être difficile à comprendre — surtout pour les nouveaux programmeurs. Dans sa forme la plus simple, une fonction récursive est une fonction qui s'appelle elle-même. Permettez-moi d'essayer d'expliquer avec un exemple.

Imaginez que vous allez ouvrir la porte de votre chambre et qu'elle est verrouillée. Votre fils de trois ans surgit de derrière le coin et vous fait savoir qu'il a caché la seule clé dans une boîte. (« Tout comme lui », pensez-vous.) Vous êtes en retard pour le travail et vous devez absolument entrer dans la pièce pour prendre votre chemise.

Vous ouvrez la boîte pour trouver... d'autres boîtes. Des boîtes à l'intérieur de boîtes. Et vous ne savez pas laquelle contient la clé ! Vous devez trouver cette chemise rapidement, alors vous devez penser à un bon algorithme pour trouver cette clé.

Il existe deux approches principales pour créer un algorithme pour ce problème : itérative et récursive. Voici les deux approches sous forme d'organigrammes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QrQ5uFKIhK3jQSFYeRBIRg.png)

Quelle approche vous semble la plus facile ?

La première approche utilise une boucle while. Tant que la pile n'est pas vide, prenez une boîte et cherchez dedans. Voici un pseudocode inspiré de JavaScript qui montre ce qui se passe. (Le pseudocode est écrit comme du code, mais est destiné à être plus proche du langage humain.)

```javascript
function look_for_key(main_box) {
    let pile = main_box.make_a_pile_to_look_through();
    while (pile is not empty) {
        box = pile.grab_a_box();
        for (item in box) {
            if (item.is_a_box()) {
                pile.append(item)
            } else if (item.is_a_key()) {
                console.log("found the key!")
            }
        }
    }}
```

La deuxième méthode utilise la récursivité. Rappelez-vous, la récursivité est lorsqu'une fonction s'appelle elle-même. Voici la deuxième méthode en pseudocode.

```javascript
function look_for_key(box) {
  for (item in box) {
    if (item.is_a_box()) {
      look_for_key(item);
    } else if (item.is_a_key()) {
      console.log("found the key!")
    } 
  }
}
```

Les deux approches accomplissent la même chose. Le principal avantage de l'approche récursive est que, une fois que vous la comprenez, elle peut être plus claire à lire. Il n'y a en réalité aucun avantage de performance à utiliser la récursivité. L'approche itérative avec des boucles peut parfois être plus rapide. Mais c'est surtout la simplicité de la récursivité qui est parfois préférée.

De plus, comme beaucoup d'algorithmes utilisent la récursivité, il est important de comprendre comment elle fonctionne. Si la récursivité ne vous semble toujours pas simple, ne vous inquiétez pas : je vais passer en revue quelques autres exemples.

### Cas de base et cas récursif

Une chose à laquelle vous devez faire attention lorsque vous écrivez une fonction récursive est la boucle infinie. C'est lorsque la fonction continue de s'appeler elle-même... et ne s'arrête jamais !

Par exemple, vous pourriez vouloir écrire une fonction de compte à rebours. Vous pourriez l'écrire de manière récursive en JavaScript comme ceci :

```javascript
// ATTENTION : Cette fonction contient une boucle infinie !
function countdown(i) {  console.log(i)  countdown(i - 1)}

countdown(5);    // C'est l'appel initial à la fonction.
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*LGjfggsIiQHbfJothG1hYw.png)

Cette fonction continuera à compter à rebours indéfiniment. Si vous exécutez accidentellement du code avec une boucle infinie, vous pouvez appuyer sur « Ctrl-C » pour arrêter votre script. (Ou, si vous utilisez parfois CodePen comme moi, vous devez ajouter « ?turn_off_js=true » à la fin de l'URL.)

Une fonction récursive doit toujours indiquer quand arrêter de se répéter. Il doit toujours y avoir deux parties dans une fonction récursive : le cas récursif et le cas de base. Le cas récursif est lorsque la fonction s'appelle elle-même. Le cas de base est lorsque la fonction arrête de s'appeler elle-même. Cela empêche les boucles infinies.

Voici à nouveau la fonction de compte à rebours, avec un cas de base :

```javascript
function countdown(i) {
    console.log(i)  if (i <= 1) {  // cas de base
        return;
    } else {     // cas récursif
        countdown(i - 1);
    }
}

countdown(5);    // C'est l'appel initial à la fonction.
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rQ9Z3DmtGk1Bb6_Mx5W6rQ.png)

Il n'est peut-être pas évident de comprendre exactement ce qui se passe dans cette fonction. Je vais vous expliquer ce qui se passe lorsque vous appelez la fonction countdown avec le paramètre « 5 ».

Nous commençons par afficher le nombre 5 en utilisant `console.log`. Comme cinq n'est _pas_ inférieur ou égal à zéro, nous passons à l'instruction else. Là, nous appelons à nouveau la fonction countdown avec le nombre quatre (5–1=4 ?).

Nous affichons le nombre 4. Encore une fois, `i` n'est _pas_ inférieur ou égal à zéro, donc nous passons à l'instruction else et appelons countdown avec 3. Cela continue jusqu'à ce que `i` soit égal à zéro. Lorsque cela se produit, nous affichons le nombre zéro et ensuite `i` _est_ inférieur ou égal à zéro. Nous atteignons enfin l'instruction return et sortons de la fonction.

### La pile d'appels

Les fonctions récursives utilisent quelque chose appelé « la pile d'appels ». Lorsqu'un programme appelle une fonction, cette fonction est placée au sommet de la pile d'appels. Cela ressemble à une pile de livres. Vous ajoutez des choses une à la fois. Ensuite, lorsque vous êtes prêt à retirer quelque chose, vous retirez toujours l'élément du dessus.

Je vais vous montrer la pile d'appels en action avec la fonction `factorial`. `factorial(5)` est écrit 5! et est défini comme suit : 5! = 5 * 4 * 3 * 2 * 1. Voici une fonction récursive pour calculer la factorielle d'un nombre :

```javascript
function fact(x) {
    if (x == 1) {
        return 1;
    } else {
        return x * fact(x-1);
    }
}
```

Maintenant, voyons ce qui se passe si vous appelez `fact(3)`. L'illustration ci-dessous montre comment la pile change, ligne par ligne. La boîte la plus haute de la pile vous indique quel appel à `fact` vous êtes en train d'exécuter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YRkMsMPRFAt8Y9BiC0QVDg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AWu17xnQ-lxVwpgVhEo_lA.png)
_Crédit image : Adit Bhargava_

Remarquez comment chaque appel à `fact` a sa propre copie de `x`. Cela est très important pour que la récursivité fonctionne. Vous ne pouvez pas accéder à la copie de `x` d'une autre fonction.

### _Avez-vous trouvé la clé ?_

Revenons brièvement à l'exemple initial sur la recherche d'une clé dans des boîtes imbriquées. Rappelez-vous, la première méthode était itérative utilisant des boucles. Avec cette méthode, vous faites une pile de boîtes à chercher, donc vous savez toujours quelles boîtes vous devez encore chercher.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qFezr1s9YpK6-GsMJqwhOA.png)

Mais il n'y a pas de pile dans l'approche récursive. Comment votre algorithme sait-il quelles boîtes vous devez encore chercher ? La « pile de boîtes » est sauvegardée sur la pile. Il s'agit d'une pile d'appels de fonctions à moitié terminés, chacun avec sa propre liste à moitié terminée de boîtes à chercher. La pile garde une trace de la pile de boîtes pour vous !

Et grâce à la récursivité, vous pouvez enfin trouver la clé et obtenir votre chemise !

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Y0_goJ5oKvt1tzSX4d8Tw.png)

Vous pouvez également regarder cette vidéo de 5 minutes que j'ai réalisée sur la récursivité. Elle devrait renforcer ces concepts de récursivité.

%[https://www.youtube.com/watch?v=vPEJSJMg4jY]

### **Conclusion**

J'espère que cet article vous a apporté plus de clarté sur la récursivité en programmation. Cet article est basé sur une leçon de mon nouveau cours vidéo de Manning Publications intitulé [Algorithms in Motion](https://www.manning.com/livevideo/algorithms-in-motion?a_aid=algmotion&a_bid=9022d293). Le cours (et aussi cet article) est basé sur le livre _amazing_ [Grokking Algorithms](https://www.amazon.com/gp/product/1617292230/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=bcar08-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1617292230&linkId=83471c93327ff24766dd812f9799f95a) d'Adit Bhargava. C'est lui qui a dessiné toutes les illustrations amusantes de cet article.

Si vous apprenez mieux avec des livres, [achetez le livre](https://www.amazon.com/gp/product/1617292230/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=bcar08-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1617292230&linkId=83471c93327ff24766dd812f9799f95a) ! Si vous apprenez mieux avec des vidéos, envisagez [d'acheter mon cours](https://www.manning.com/livevideo/algorithms-in-motion?a_aid=algmotion&a_bid=9022d293).

> Obtenez 39 % de réduction sur mon cours en utilisant le code '39carnes' !

![Image](https://cdn-media-1.freecodecamp.org/images/1*a5UFtQIHwXy7SCQpI9GdVQ.png)

Et enfin, pour vraiment comprendre la récursivité, vous devez relire cet article. ?