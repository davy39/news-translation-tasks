---
title: La différence entre les méthodes call, apply et bind de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T01:31:44.000Z'
originalURL: https://freecodecamp.org/news/the-difference-between-javascripts-call-apply-and-bind-methods-4e69917f77bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2ZGrvPwHxZnbTzABICrEAg.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: La différence entre les méthodes call, apply et bind de JavaScript
seo_desc: 'By Rajat Saxena

  Let’s drill it into our minds and be done with it, once and for all.


  JavaScript’s call vs apply vs bind

  I’m writing this micro post because the aforementioned question has haunted me for
  a very long time, and I knew I wasn’t the only...'
---

Par Rajat Saxena

#### Gravons-le dans nos esprits une fois pour toutes.

![Image](https://cdn-media-1.freecodecamp.org/images/yOtmD6BiySaust-L9saV-u4p1HeRZUWr8sKx)
_call vs apply vs bind de JavaScript_

J'écris ce micro-article parce que la question mentionnée ci-dessus m'a hanté pendant très longtemps, et je savais que je n'étais pas le seul. Chaque fois que je voyais quelqu'un utiliser l'une de ces trois méthodes, je devais me précipiter sur [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/) pour comprendre ce qui se passait.

Assez, c'était assez. Je savais que je devais faire quelque chose et je l'ai fait. J'ai supposément créé une balle d'argent proverbial qui peut aider les nouveaux développeurs JavaScript.

> **Avertissement** : Ceci n'est pas une solution théorique, mais un moyen vraiment astucieux de se souvenir de la différence.

La principale cause de confusion entre les méthodes `call()` et `apply()` est la manière de passer les arguments supplémentaires en plus de `this`. Et pourquoi avons-nous `bind()` de toute façon ?

Alors apprenons à distinguer facilement les trois.

#### Apply()

`**apply(this [, [arg1, arg2,...]])**`**:** Appelle une fonction avec une valeur `this` fournie. Les arguments supplémentaires sont fournis sous forme de **tableau unique**.

**_Moyen de s'en souvenir_** : "Apply accepte les arguments sous forme de tableau" ou "AA".

#### Call()

`call**(this [, arg1, arg2...])**`**:** Appelle une fonction avec un `this` fourni. Les arguments supplémentaires sont fournis sous forme de **liste séparée par des virgules**.

**_Moyens de s'en souvenir_** : "Les arguments de Call sont séparés par des virgules" ou "CC".

#### Bind()

`**bind(this)**`**:** Retourne une nouvelle fonction dont la valeur `this` est liée à la valeur fournie.

**_Moyens de s'en souvenir_** : `bind()` est la **seule** méthode parmi les trois qui retourne une nouvelle fonction. Elle n'appelle pas la fonction.

#### Conclusion

J'espère que l'explication ci-dessus pourra aider certains d'entre vous. Cela m'aide certainement.

Avez-vous d'autres astuces de mémorisation liées à la programmation ? Partagez-les avec la communauté, cela aidera tout le monde. Surtout pendant ces entretiens.

Si vous avez des questions ou des doutes, contactez-moi sur Twitter [@rajat1saxena](https://twitter.com/rajat1saxena) ou écrivez-moi à [rajat@raynstudios.com](mailto:rajat@raynstudios.com). Veuillez recommander cet article si vous l'avez aimé et partagez-le avec votre réseau.