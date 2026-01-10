---
title: Que signifie le S dans les expressions régulières ? Espace et métacaractères
  d'espace négatif
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-07T14:09:22.000Z'
originalURL: https://freecodecamp.org/news/what-does-s-in-regex-mean-space-and-negated-space-metacharacters
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--3-.png
tags:
- name: Regex
  slug: regex
seo_title: Que signifie le S dans les expressions régulières ? Espace et métacaractères
  d'espace négatif
seo_desc: "In regular expressions, “S” is a metacharacter that represents space. \n\
  The small letter “s” metacharacter stands for space, and the capital letter “S”\
  \ stands for non-space. That's how the pattern for most metacharacters works. \n\
  For instance, the smal..."
---

Dans les expressions régulières, « S » est un métacaractère qui représente l'espace. 

Le métacaractère de la lettre minuscule « s » représente l'espace, et la lettre majuscule « S » représente le non-espace. C'est ainsi que fonctionne le modèle pour la plupart des métacaractères. 

Par exemple, la lettre minuscule « d » est le métacaractère pour un chiffre, et la lettre majuscule « D » est le non-chiffre.

Dans cet article, nous examinerons ces deux variations du caractère « S » dans RegEx, ce qu'ils font, et leur utilisation dans les moteurs RegEx et la programmation.


## Ce que nous allons couvrir
- [Comment faire fonctionner les métacaractères ?](#heading-comment-faire-fonctionner-les-metacaractères)
- [Que fait le métacaractère « S » ?](#heading-que-fait-le-metacaractère-s)
- [Exemples d'utilisation du métacaractère « S »](#heading-exemples-dutilisation-du-metacaractère-s)
- [Conclusion](#heading-conclusion)


## Comment faire fonctionner les métacaractères ? 
Pour faire fonctionner les métacaractères, vous devez les échapper. 

La raison est que si vous tapez simplement le métacaractère « S », « s », ou « D » dans un moteur RegEx ou en écrivant RegEx dans un langage de programmation, il est interprété comme cette lettre. 

Ainsi, pour faire fonctionner les métacaractères dans RegEx, vous devez les échapper avec un antislash (`\`).

Dans l'exemple ci-dessous, j'ai pu faire correspondre les caractères d'espace parce que j'ai échappé le `s` :
![Screenshot-2023-03-07-at-10.18.37](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-07-at-10.18.37.png)

Pour l'exemple ci-dessous, j'ai pu faire correspondre les chiffres parce que j'ai échappé le `d` :
![Screenshot-2023-03-07-at-10.20.50](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-07-at-10.20.50.png)

## Que fait le métacaractère « S » ?
Comme je l'ai mentionné précédemment, le métacaractère « S » a deux formes – la lettre minuscule « s » et la lettre majuscule « S ». 

Quand il est en minuscule, il correspond à tous les caractères d'espace, tels que la barre d'espace, la tabulation et le retour chariot.

Et quand il est en majuscule, il correspond à tous les caractères non-espace tels que les chiffres, les symboles et les lettres. 

Chacun des caractères d'espace a également ses métacaractères respectifs :

* `\t` pour la tabulation
* `\r` pour le retour chariot
* `\n` pour une nouvelle ligne


## Exemples d'utilisation du métacaractère « S »
Vous pouvez faire correspondre tous les caractères non-espace avec une lettre majuscule échappée « S » :
![Screenshot-2023-03-07-at-10.36.55](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-07-at-10.36.55.png)

Vous pouvez faire correspondre tous les caractères d'espace avec une lettre minuscule échappée « s » :
![Screenshot-2023-03-07-at-10.18.37-1](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-07-at-10.18.37-1.png)

Les métacaractères `\s` et `\S` fonctionnent bien dans n'importe quel langage qui supporte RegEx. 

Voici un exemple en JavaScript :
```js
let regex1 = /\S/g;
let regex2 = /\s/g;

let str1 = 'Allofthesearenonsspacecharacters';
let str2 = `spacebar \ntab \nnewLine\n\n`;

console.log(regex1.test(str1)); //true
console.log(regex2.test(str2)); // true
```


## Conclusion
Cet article vous a montré ce que signifie le caractère « S » et ce qu'il fait dans RegEx. 

Nous avons examiné comment il fonctionne (il doit être échappé pour fonctionner), ses deux formes, et comment il fonctionne dans les moteurs RegEx et JavaScript.

Merci d'avoir lu. Bon codage !