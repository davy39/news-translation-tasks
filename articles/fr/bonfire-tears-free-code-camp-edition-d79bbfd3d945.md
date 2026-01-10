---
title: Larmes d'algorithme
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-26T07:06:21.000Z'
originalURL: https://freecodecamp.org/news/bonfire-tears-free-code-camp-edition-d79bbfd3d945
coverImage: https://cdn-media-1.freecodecamp.org/images/0*reQ5pMmpwq1G06h-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Women
  slug: women
- name: women in tech
  slug: women-in-tech
seo_title: Larmes d'algorithme
seo_desc: 'By Tiffany White


  “Laughter and tears are both responses to frustration and exhaustion. I myself prefer
  to laugh, since there is less cleaning to do afterward.” ― Kurt Vonnegut


  There comes a point in every new programmers life when they hit a barrie...'
---

Par Tiffany White

> « Le rire et les larmes sont tous deux des réponses à la frustration et à l'épuisement. Je préfère moi-même rire, car il y a moins de nettoyage à faire ensuite. » — Kurt Vonnegut

Il arrive un moment dans la vie de chaque nouveau programmeur où il rencontre une barrière, un mur, un seuil entre la compréhension et la non-compréhension du matériel à portée de main.

J'ai atteint ce seuil hier.

Et avant-hier.

En rétrospective, la solution était si simple. J'avais la bonne idée plusieurs fois. J'ai été encouragée, et expliquée, et guidée, mais c'était comme si leurs mots rebondissaient simplement sur mon crâne au lieu d'être absorbés par ma matière grise.

Le défi de l'algorithme était :

> Vérifiez si une chaîne (premier argument) se termine par la chaîne cible donnée (deuxième argument).

> N'oubliez pas d'utiliser Rechercher-Lire-Demander si vous êtes bloqué. Écrivez votre propre code.

> Voici quelques liens utiles :

> String.substr()

Le code avec lequel Free Code Camp m'a commencé :

```
function end(str, target) { 
```

```
// « Ne jamais abandonner et la chance vous sourira. » 
```

```
// — Falcor 
```

```
return str; 
```

```
}
```

```
end("Bastian", "n"); 
```

#### Qu'est-ce que c'est ? Sous-chaînes ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*k9MyKxq8P6tLWagt.gif)

> Vous l'avez déjà fait et vous pouvez le faire maintenant. Voyez les possibilités positives. Redirigez l'énergie substantielle de votre frustration et transformez-la en détermination positive, efficace et inarrêtable. — Ralph Marston

Je savais, en regardant les tests échoués, que mon algorithme devait gérer des chaînes de différentes longueurs. Mais je continuais à coder en dur pour une seule des chaînes de test.

Comment coder cette chose pour différentes longueurs de chaîne ? Comment obtenir la longueur d'une chaîne ? .length() non ? OUI. Mais _comment_. Où placer le .length() ?

J'avais ce code :

```
function end(str, target) { 
```

```
     // « Ne jamais abandonner et la chance vous sourira. » 
```

```
    // — Falcor
```

```
   // 'abcdefghijklmn'.substr(0, 3)
```

```
  // 'abc'
```

```
 // « prendre 3 caractères en commençant par le caractère à l'adresse numéro 0 »  
```

```
    var isEqual = str.substr(6, 1) === target.substr(0, 1); 
```

```
    return isEqual;
```

```
}  end("Bastian", "n");
```

J'ai découvert dans l'une des salles de discussion d'aide de Free Code Camp que vous pouvez atteindre la fin d'une chaîne en utilisant un nombre négatif. Pas besoin de continuer à enlever toutes ces lettres avant le "n" sur Bastian.

Mais j'ai continué à coder en dur pour "Bastian" et "n".

J'avais besoin d'une approche plus large.

J'ai essayé :

```
function end(str, target) {
```

```
   var isEqual = str.substr(-1) === target.substr(-1); return isEqual;
```

```
}  end("Bastian", "n");
```

Mais je ne faisais pas vraiment de progrès. Tous les tests sauf un étaient réussis, et je n'utilisais toujours pas vraiment .length() pour traiter la variance de la longueur de la chaîne.

Alors j'ai essayé ceci :

```
function end(str, target) {
```

```
    var n = target.length;     var z = str.length;     var isEqual = str.substr(-1) === target.substr(-1); return isEqual;
```

```
}  end("Bastian", "n");
```

Même résultat. Je savais que je devais avoir .length() là-haut. Mais où aller après cela ?

#### Aha !

![Image](https://cdn-media-1.freecodecamp.org/images/0*bGUwwQpIJYjPywvs.gif)

Enfin, j'ai dû être guidée vers la réponse. La femme était en Grande-Bretagne et je suis presque sûre que je la tenais éveillée. Mais ensemble, nous avons trouvé cette solution :

```
// Vous ne pensiez pas que je donnerais la réponse, n'est-ce pas ?
```

Et enfin, j'ai compris. Cela a pris un certain temps pour y arriver, mais lorsque nous avons atteint la solution, je me suis sentie comme une idiote complète. Comment ai-je pu ne pas comprendre cela plus tôt ?

J'ai pleuré. J'ai littéralement pleuré. Une partie de cela était simplement moi étant déjà émotionnelle.

L'autre partie était moi ne voulant pas mettre mon poing à travers l'écran de mon MacBook Pro.

Les chaînes sont des caractères. Pas des mots. Et j'étais totalement bloquée là-dessus.

Des larmes d'algorithme, en effet.

_Publié à l'origine sur [Code Newbie in Pittsburgh](http://helloburgh.me/2015/11/26/bonfire-tears-free-code-camp-edition/)._