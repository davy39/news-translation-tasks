---
title: Apprenez les expressions régulières avec ce cours gratuit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-21T16:46:07.000Z'
originalURL: https://freecodecamp.org/news/learn-regular-expressions-with-this-free-course-37511963d278
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Sg2Vdih6v1wDWRPtgnX0DA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: software
  slug: software
- name: software development
  slug: software-development
seo_title: Apprenez les expressions régulières avec ce cours gratuit
seo_desc: 'By Beau Carnes


  “Some people, when confronted with a problem, think ‘I know, I’ll use regular expressions.’
  Now they have two problems.” -Jamie Zawinski


  For some people, using regular expressions can be a problem. But it doesn’t have
  to be a problem...'
---

Par Beau Carnes

> « Certaines personnes, lorsqu'elles sont confrontées à un problème, pensent : 'Je sais, je vais utiliser des expressions régulières.' Maintenant, elles ont deux problèmes. » _- Jamie Zawinski_

Pour certaines personnes, l'utilisation des expressions régulières peut être un problème. Mais cela ne doit pas être un problème pour vous. Cet article est un cours complet sur les expressions régulières.

### 1. Introduction

Les expressions régulières, ou simplement RegEx, sont utilisées dans presque tous les langages de programmation pour définir un motif de recherche qui peut être utilisé pour rechercher des choses dans une chaîne de caractères.

J'ai développé un [cours vidéo complet et gratuit](https://scrimba.com/g/gregularexpressions) sur Scrimba.com pour enseigner les bases des expressions régulières.

Cet article contient le cours sous forme écrite. Mais si vous préférez regarder la version vidéo avec des leçons interactives, vous pouvez la consulter sur [Scrimba](https://scrimba.com/g/gregularexpressions). Les sections de cet article correspondent aux sections du cours Scimba.

Ce cours suit le programme [RegEx](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/regular-expressions) de freeCodeCamp.org. Vous pouvez le consulter pour des défis de codage et pour obtenir un certificat.

Ces leçons se concentrent sur l'utilisation de RegEx en JavaScript, mais les principes s'appliquent à de nombreux autres langages de programmation que vous pourriez choisir d'utiliser. Si vous ne connaissez pas déjà le JavaScript de base, il pourrait être utile de le couvrir un peu d'abord. J'ai également un cours de base sur JavaScript que vous pouvez consulter sur [Scrimba](https://scrimba.com/p/pPgdYTV/cEv4Lh6) et sur la [chaîne YouTube de freeCodeCamp.org](https://www.youtube.com/watch?v=PkZNo7MFNFg).

Alors, commençons ! Vous serez prêt à sauver la journée en un rien de temps. ?

![Image](https://cdn-media-1.freecodecamp.org/images/mR0hvYGgyvAY9jIH9iiSUNj1gz-dI39-34RS)
_De [https://xkcd.com/208/](https://xkcd.com/208/" rel="noopener" target="_blank" title=")_

### 2. Utilisation de la méthode Test

Pour faire correspondre des parties de chaînes de caractères en utilisant RegEx, nous devons créer des motifs qui aident à faire cette correspondance. Nous pouvons indiquer que quelque chose est un motif RegEx en plaçant le motif entre des barres obliques `/`, comme ceci `/motif-que-nous-voulons-faire-correspondre/`.

Regardons un exemple :

```
// Nous voulons vérifier la phrase suivante
let sentence = "The dog chased the cat."
```

```
// et voici le motif que nous voulons faire correspondre.
let regex = /the/
```

Remarquez comment nous utilisons `/the/` pour indiquer que nous cherchons « the » dans notre `sentence`.

Nous pouvons utiliser la méthode RegEx `test()` pour savoir si un motif est présent dans une chaîne de caractères ou non.

```
// Chaîne de caractères que nous voulons tester
let myString = "Hello, World!";
```

```
// Motif que nous voulons trouver
let myRegex = /Hello/;
```

```
// le résultat est maintenant vrai
let result = myRegex.test(myString);
```

### 3. Correspondance de chaînes littérales

Trouvons maintenant Waldo.

```
let waldoIsHiding = "Somewhere Waldo is hiding in this text.";
let waldoRegex = /Waldo/;
```

```
// test() retourne vrai, donc le résultat est maintenant aussi vrai
let result = waldoRegex.test(waldoIsHiding);
```

Notez que dans cet exemple, `waldoRegex` est sensible à la casse, donc si nous écrivions `/waldo/` avec un 'w' minuscule, alors notre `result` serait faux.

### 4. Correspondance d'une chaîne littérale avec différentes possibilités

RegEx a également un opérateur `OR` qui est le caractère `|`.

```
let petString = "James has a pet cat.";
```

```
// Nous pouvons maintenant essayer de trouver si l'un des mots est dans la phrase
let petRegex = /dog|cat|bird|fish/;
```

```
let result = petRegex.test(petString);
```

### 5. Ignorer la casse lors de la correspondance

Jusqu'à présent, nous avons examiné des motifs où la casse des lettres comptait. Comment pouvons-nous rendre nos motifs RegEx insensibles à la casse ?

Pour ignorer la casse, nous pouvons le faire en ajoutant le drapeau `i` à la fin d'un motif, comme ceci `/some-pattern/i`.

```
let myString = "freeCodeCamp";
```

```
// Nous ignorons la casse en utilisant le drapeau 'i'
let fccRegex = /freecodecamp/i;
```

```
// le résultat est vrai
let result = fccRegex.test(myString);
```

### 6. Extraire les correspondances

Lorsque nous voulons extraire la valeur correspondante, nous pouvons utiliser la méthode `match()`.

```
let extractStr = "Extract the word 'coding' from this string.";
```

```
let codingRegex = /coding/;
```

```
let result = extractStr.match(codingRegex);
```

```
console.log(result);
```

```
// Le terminal affichera : // > ["coding"]
```

### 7. Trouver plus que la première correspondance

Maintenant que nous savons comment extraire une valeur, il est également possible d'extraire plusieurs valeurs en utilisant le drapeau `g`.

```
let testStr = "Repeat, Repeat, Repeat";
```

```
let ourRegex = /Repeat/g;
```

```
testStr.match(ourRegex); // retourne ["Repeat", "Repeat", "Repeat"]
```

Nous pouvons également combiner le drapeau `g` avec le drapeau `i`, pour extraire plusieurs correspondances et ignorer la casse.

```
let twinkleStar = "Twinkle, twinkle, little star";
```

```
let starRegex = /twinkle/ig;// écrire /twinkle/gi aurait le même résultat.
```

```
let result = twinkleStar.match(starRegex);
```

```
console.log(result);
```

```
// Le terminal affichera : // > ["Twinkle", "twinkle"]
```

### 8. Correspondance avec n'importe quel caractère avec le point wildcard

Dans RegEx, `.` est un caractère wildcard qui correspond à n'importe quoi.

```
let humStr = "I'll hum a song";
```

```
let hugStr = "Bear hug";
```

```
// Recherche n'importe quoi avec 3 caractères commençant par 'hu'
let huRegex = /hu./;
```

```
humStr.match(huRegex); // Retourne ["hum"]
```

```
hugStr.match(huRegex); // Retourne ["hug"]
```

### 9. Correspondance d'un seul caractère avec plusieurs possibilités

Correspondre à n'importe quel caractère est bien, mais que faire si nous voulons restreindre la correspondance à un ensemble prédéfini de caractères ? Nous pouvons le faire en utilisant `[]` dans notre RegEx.

Si nous avons `/b[aiu]g/`, cela signifie que nous pouvons correspondre à 'bag', 'big' et 'bug'.

Si nous voulons extraire toutes les voyelles d'une phrase, voici comment nous pouvons le faire en utilisant RegEx.

```
let quoteSample = "Beware of bugs in the above code; I have only proved it correct, not tried it.";
```

```
let vowelRegex = /[aeiou]/ig;
```

```
let result = quoteSample.match(vowelRegex);
```

### 10. Correspondance des lettres de l'alphabet

Mais que faire si nous voulons correspondre à une plage de lettres ? Bien sûr, faisons cela.

```
let quoteSample = "The quick brown fox jumps over the lazy dog.";
```

```
// Nous pouvons correspondre à toutes les lettres de 'a' à 'z', en ignorant la casse.
let alphabetRegex = /[a-z]/ig;
```

```
let result = quoteSample.match(alphabetRegex);
```

### 11. Correspondance des chiffres et des lettres de l'alphabet

Les lettres sont bien, mais que faire si nous voulons aussi des chiffres ?

```
let quoteSample = "Blueberry 3.141592653s are delicious.";
```

```
// correspondre aux chiffres entre 2 et 6 (inclus), // et aux lettres entre 'h' et 's'.
let myRegex = /[2-6h-s]/ig;
```

```
let result = quoteSample.match(myRegex);
```

### 12. Correspondance des caractères uniques non spécifiés

Parfois, il est plus facile de spécifier les caractères que vous ne voulez pas voir. Ceux-ci sont appelés 'Caractères Négatifs' et dans RegEx, vous pouvez le faire en utilisant `^`.

```
let quoteSample = "3 blind mice.";
```

```
// Correspondre à tout ce qui n'est pas un chiffre ou une voyelle.
let myRegex = /[^0-9aeiou]/ig;
```

```
let result = quoteSample.match(myRegex);// Retourne [" ", "b", "l", "n", "d", " ", "m", "c", "."]
```

### 13. Correspondance des caractères qui apparaissent une ou plusieurs fois

Si vous voulez correspondre à des caractères qui apparaissent une ou plusieurs fois, vous pouvez utiliser `+`.

```
let difficultSpelling = "Mississippi";
```

```
let myRegex = /s+/g;
```

```
let result = difficultSpelling.match(myRegex);// Retourne ["ss", "ss"]
```

### 14. Correspondance des caractères qui apparaissent zéro ou plusieurs fois

Il existe également un quantificateur RegEx `*`. Celui-ci correspond même à 0 occurrences d'un caractère. Pourquoi cela pourrait-il être utile ? La plupart du temps, c'est généralement en combinaison avec d'autres caractères. Regardons un exemple.

```
let soccerWord = "gooooooooal!";
```

```
let gPhrase = "gut feeling";
```

```
let oPhrase = "over the moon";
```

```
// Nous essayons de correspondre à 'g', 'go', 'goo', 'gooo' et ainsi de suite.
let goRegex = /go*/;
```

```
soccerWord.match(goRegex); // Retourne ["goooooooo"]
```

```
gPhrase.match(goRegex); // Retourne ["g"]
```

```
oPhrase.match(goRegex); // Retourne null
```

### 15. Trouver des caractères avec une correspondance paresseuse

Parfois, vos correspondances de motifs peuvent avoir plus d'un résultat. Par exemple, disons que je cherche un motif dans un mot `titanic` et que mes valeurs correspondantes doivent commencer par un 't' et se terminer par un 'i'. Mes résultats possibles sont 'titani' et 'ti'.

C'est pourquoi RegEx a un concept de 'Correspondance Gloutonne' et 'Correspondance Paresseuse'.

La correspondance gloutonne trouve _la_ _plus longue correspondance possible_ de la chaîne qui correspond au motif RegEx, c'est une correspondance RegEx par défaut :

```
let string = "titanic";
```

```
let regex = /t[a-z]*i/;
```

```
string.match(regex);// Retourne ["titani"]
```

La correspondance paresseuse trouve _la_ _plus courte correspondance possible_ de la chaîne qui correspond au motif RegEx et pour l'utiliser, nous devons utiliser `?` :

```
let string = "titanic";
```

```
let regex = /t[a-z]*?i/;
```

```
string.match(regex);// Retourne ["ti"]
```

### 16. Trouver un ou plusieurs criminels dans une chasse

Maintenant, examinons un défi RegEx. Nous devons trouver tous les criminels ('C') dans une foule. Nous savons qu'ils restent toujours ensemble et vous devez écrire un RegEx qui les trouverait.

```
let crowd = 'P1P2P3P4P5P6CCCP7P8P9';
```

```
let reCriminals = /./; // Changez cette ligne
```

```
let matchedCriminals = crowd.match(reCriminals);
```

Vous pouvez me trouver en train de parcourir [la solution dans ce Scrimba cast](https://scrimba.com/p/peyvVAN/c3nEpta).

### 17. Correspondance des motifs de début de chaîne

RegEx permet également de correspondre à des motifs qui ne sont qu'au début d'une chaîne. Nous avons déjà parlé de `^` créant un ensemble négatif. Nous pouvons utiliser le même symbole pour trouver une correspondance _uniquement_ au début d'une chaîne.

```
let calAndRicky = "Cal and Ricky both like racing.";
```

```
// Correspondre à 'Cal' uniquement s'il est au début d'une chaîne.
let calRegex = /^Cal/;
```

```
let result = calRegex.test(calAndRicky); // Retourne vrai
```

```
let rickyAndCal = "Ricky and Cal both like racing.";
```

```
let result = calRegex.test(rickyAndCal); // Retourne faux
```

### 18. Correspondance des motifs de fin de chaîne

Et pour correspondre à un motif à la fin d'une chaîne ? Nous pouvons utiliser `$` pour cela.

```
let caboose = "The last car on a train is the caboose";
```

```
// Correspondre à 'caboose' s'il est à la fin d'une chaîne.
let lastRegex = /caboose$/;
```

```
let result = lastRegex.test(caboose); // Retourne vrai
```

### 19. Correspondance de toutes les lettres et chiffres

Plus tôt, dans les parties 10 et 11, je vous ai montré comment nous pouvons correspondre à des plages de lettres et de chiffres. Si je vous demandais d'écrire un RegEx qui correspond à toutes les lettres et chiffres et ignore leur casse, vous auriez probablement écrit quelque chose comme `/[a-z0-9]/gi` et c'est exactement cela. Mais c'est un peu trop long.

RegEx a quelque chose appelé '_Classes de caractères raccourcies_', qui est essentiellement un raccourci pour les expressions RegEx courantes. Pour correspondre à toutes les lettres et chiffres, nous pouvons utiliser `\w` et nous obtenons également le soulignement `_` correspondant en bonus.

```
let quoteSample = "The five boxing wizards jump quickly.";
```

```
// Identique à /[a-z0-9_]/gi pour correspondre à a-z (ignorer la casse), 0-9 et _
let alphabetRegexV2 = /\w/g;
```

```
// La longueur de tous les caractères dans une chaîne // à l'exclusion des espaces et du point.
let result = quoteSample.match(alphabetRegexV2).length;
```

```
// Retourne 31
```

### 20. Correspondance de tout sauf les lettres et chiffres

Si nous voulons faire l'inverse et correspondre à tout ce qui n'est pas une lettre ou un chiffre (exclure également le soulignement `_`), nous pouvons utiliser `\W`.

```
let quoteSample = "The five boxing wizards jump quickly.";
```

```
// Correspondre aux espaces et au point
let nonAlphabetRegex = /\W/g;
```

```
let result = quoteSample.match(nonAlphabetRegex).length;
```

```
// Retourne 6
```

### 21. Correspondance de tous les chiffres

D'accord, que faire si vous voulez seulement des chiffres ? Y a-t-il une classe de caractères raccourcie pour cela ? Bien sûr, c'est `\d`.

```
let numString = "Your sandwich will be $5.00";
```

```
// Correspondre à tous les chiffres
let numRegex = /\d/g;
```

```
let result = numString.match(numRegex).length; // Retourne 3
```

### 22. Correspondance de tous les non-chiffres

Voudriez-vous l'inverse et correspondre à tous les non-chiffres ? Utilisez `\D`.

```
let numString = "Your sandwich will be $5.00";
```

```
// Correspondre à tout ce qui n'est pas un chiffre
let noNumRegex = /\D/g;
```

```
let result = numString.match(noNumRegex).length; // Retourne 24
```

### 23. Restreindre les noms d'utilisateur possibles

Jusqu'à présent, tout va bien ! Bien joué pour être arrivé jusqu'ici. RegEx peut être délicat car ce n'est pas la manière la plus facile à lire pour coder. Regardons maintenant un exemple très concret et créons un validateur de nom d'utilisateur. Dans ce cas, vous avez 3 exigences :

* Si des chiffres sont présents, ils doivent être à la fin.
* Les lettres peuvent être en minuscules et en majuscules.
* Au moins deux caractères de long. Les noms à deux lettres ne peuvent pas avoir de chiffres.

Essayez de résoudre cela par vous-même et si vous trouvez cela difficile ou si vous voulez simplement vérifier la réponse, [consultez ma solution](https://scrimba.com/p/peyvVAN/cmb6nf9).

### 24. Correspondance des espaces blancs

Pouvons-nous correspondre à tous les espaces blancs ? Bien sûr, nous pouvons utiliser un raccourci pour cela aussi et c'est `\s`.

```
let sample = "Whitespace is important in separating words";
```

```
// Correspondre à tous les espaces blancs
let countWhiteSpace = /\s/g;
```

```
let result = sample.match(countWhiteSpace);
```

```
// Retourne [" ", " ", " ", " ", " "]
```

### 25. Correspondance des caractères non blancs

Pouvez-vous deviner comment correspondre à tous les caractères non blancs ? Bien joué, c'est `\S` !

```
let sample = "Whitespace is important in separating words";
```

```
// Correspondre à tous les caractères non blancs
let countWhiteSpace = /\S/g;
```

```
let result = sample.match(countWhiteSpace);
```

### 26. Spécifier le nombre supérieur et inférieur de correspondances

Vous pouvez spécifier le nombre inférieur et supérieur de correspondances de motifs avec des '_Spécificateurs de Quantité_'. Ils peuvent être utilisés avec la syntaxe `{}`, par exemple `{3,6}`, où `3` est la borne inférieure et `6` est la borne supérieure à correspondre.

```
let ohStr = "Ohhh no";
```

```
// Nous voulons correspondre à 'Oh's qui ont 3-6 caractères 'h'.
let ohRegex = /Oh{3,6} no/;
```

```
let result = ohRegex.test(ohStr); // Retourne vrai
```

### 27. Spécifier uniquement le nombre inférieur de correspondances

Lorsque nous voulons spécifier uniquement la borne inférieure, nous pouvons le faire en omettant la borne supérieure, par exemple pour correspondre à au moins trois caractères, nous pouvons écrire `{3,}`. Remarquez que nous avons toujours besoin d'une virgule, même lorsque nous ne spécifions pas la limite supérieure.

```
let haStr = "Hazzzzah";
```

```
// Correspondre à un motif qui contient au moins quatre caractères 'z'
let haRegex = /z{4,}/;
```

```
let result = haRegex.test(haStr); // Retourne vrai
```

### 28. Spécifier le nombre exact de correspondances

Dans la section précédente, j'ai mentionné que nous avons besoin d'une virgule dans `{3,}` lorsque nous spécifions uniquement la borne inférieure. La raison est que lorsque vous écrivez `{3}` sans virgule, cela signifie que vous cherchez à correspondre exactement à 3 caractères.

```
let timStr = "Timmmmber";
```

```
// let timRegex = /Tim{4}ber/;
```

```
let result = timRegex.test(timStr); // Retourne vrai
```

### 29. Vérifier la présence de tous ou aucun

Il arrive que vous souhaitiez spécifier une existence possible d'un caractère dans votre motif. Lorsqu'une lettre ou un chiffre est facultatif, nous utilisons `?` pour cela.

```
// Nous voulons correspondre aux orthographes britanniques et américaines // du mot 'favourite'
```

```
let favWord_US = "favorite";
let favWord_GB = "favourite";
```

```
// Nous correspondons à la fois à 'favorite' et 'favourite' // en spécifiant que le caractère 'u' est facultatif
let favRegex = /favou?rite/; // Changez cette ligne
```

```
let result1 = favRegex.test(favWord_US); // Retourne vrai
let result2 = favRegex.test(favWord_GB); // Retourne vrai
```

### 30. Lookahead positif et négatif

Les '_Lookaheads_' sont des motifs qui indiquent à votre JS de regarder vers l'avant pour vérifier des motifs plus loin. Ils sont utiles lorsque vous essayez de rechercher plusieurs motifs dans les mêmes chaînes. Il existe 2 types de lookaheads : positif et négatif.

Le lookahead positif utilise la syntaxe `?=`

```
let quit = "qu";
```

```
// Nous correspondons à 'q' uniquement s'il est suivi de 'u'.
let quRegex= /q(?=u)/;
```

```
quit.match(quRegex); // Retourne ["q"]
```

Le lookahead négatif utilise la syntaxe `?!`

```
let noquit = "qt";
```

```
// Nous correspondons à 'q' uniquement s'il n'est pas suivi de 'u'.
let qRegex = /q(?!u)/;
```

```
noquit.match(qRegex); // Retourne ["q"]
```

### 31. Réutiliser les motifs en utilisant des groupes de capture

Imaginons que nous devons capturer un motif répétitif.

```
let repeatStr = "regex regex";
```

```
// Nous voulons correspondre à des lettres suivies d'un espace et ensuite des lettres
let repeatRegex = /(\w+)\s(\w+)/;
```

```
repeatRegex.test(repeatStr); // Retourne vrai
```

Au lieu de répéter `(\w+)` à la fin, nous pouvons dire à RegEx de répéter le motif, en utilisant `\1`. Donc, la même chose que ci-dessus peut être réécrite comme :

```
let repeatStr = "regex regex";
```

```
let repeatRegex = /(\w+)\s\1)/;
```

```
repeatRegex.test(repeatStr); // Retourne vrai
```

### 32. Utiliser des groupes de capture pour rechercher et remplacer

Lorsque nous trouvons une correspondance, il est parfois utile de la remplacer par autre chose. Nous pouvons utiliser la méthode `replace()` pour cela.

```
let wrongText = "The sky is silver.";
```

```
let silverRegex = /silver/;
```

```
wrongText.replace(silverRegex, "blue");
```

```
// Retourne "The sky is blue."
```

### 33. Supprimer les espaces blancs du début et de la fin

Voici un petit défi pour vous. Écrivez un RegEx qui supprimerait tout espace blanc autour de la chaîne.

```
let hello = "   Hello, World!  ";
```

```
let wsRegex = /change/; // Changez cette ligne
```

```
let result = hello; // Changez cette ligne
```

Si vous êtes bloqué ou si vous voulez simplement vérifier ma solution, n'hésitez pas à regarder [le Scrimba cast où je résous ce défi](https://scrimba.com/p/peyvVAN/cZVvkH7).

### 34. Conclusion

Félicitations ! Vous avez terminé ce cours ! Si vous souhaitez continuer à apprendre, n'hésitez pas à consulter [cette playlist YouTube](https://www.youtube.com/playlist?list=PLWKjhJtqVAbleDe3_ZA8h3AO2rXar-q2V), qui contient de nombreux projets JavaScript que vous pouvez créer.

Continuez à apprendre et merci d'avoir lu !

Vous êtes maintenant prêt à jouer au regex golf. ?

![Image](https://cdn-media-1.freecodecamp.org/images/sRhyrBTA9B-XwaBVwi00yiBYdaIX2rHopdBJ)
_De [https://xkcd.com/1313/](https://xkcd.com/1313/" rel="noopener" target="_blank" title=")_