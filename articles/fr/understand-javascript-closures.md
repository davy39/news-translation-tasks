---
title: Comment fonctionnent les fermetures en JavaScript ? Expliqué avec des exemples
  de code
subtitle: ''
author: Austin Asoluka
co_authors: []
series: null
date: '2024-05-07T07:13:36.000Z'
originalURL: https://freecodecamp.org/news/understand-javascript-closures
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/hand-1222229_1280-2.jpg
tags:
- name: closure
  slug: closure
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionnent les fermetures en JavaScript ? Expliqué avec des exemples
  de code
seo_desc: "Sally and Joe are two love birds. They shared everything with each other\
  \ and soon enough it was almost impossible to think that anything could come between\
  \ them. One day, they had a quarrel which built up to a break up.   \nIt was hard\
  \ for Joe and he ..."
---

Sally et Joe sont deux tourtereaux. Ils partageaient tout l'un avec l'autre et bientôt il était presque impossible de penser que quoi que ce soit pourrait s'interposer entre eux. Un jour, ils ont eu une querelle qui a conduit à une rupture.   
   
C'était difficile pour Joe et il voulait une "fermeture". Bien que Sally ait déjà tourné la page, Joe a trouvé la fermeture en prenant le temps de réfléchir à toute l'expérience, en se remémorant les "souvenirs partagés" et en introspectant correctement. Même si la relation avait pris fin, Joe avait encore quelque chose qui lui rappelait Sally et il était à l'aise avec cela.

L'histoire se termine.

Si c'est la première fois que vous entendez le terme "fermeture", je vous ferai l'honneur de vous dire ce que cela signifie.  
  
La fermeture est simplement l'acte de mettre fin à quelque chose. La fermeture dans une relation fait référence au sentiment de paix et de compréhension que vous obtenez après la fin de la relation. C'est ce sentiment de "lâcher prise" et de pouvoir passer à autre chose.  
  
Pour certaines personnes, obtenir une fermeture implique de s'accrocher à un "souvenir partagé" avec l'autre partie, ou à quelque chose (peut-être un objet) qui leur rappelle l'autre.

Maintenant que vous êtes familiarisé avec le terme fermeture tel qu'il se rapporte aux humains, essayons de le comprendre en termes de relation entre les fonctions en JavaScript.

En JavaScript, on dit qu'une fermeture est créée lorsqu'une fonction conserve l'accès aux ressources déclarées dans sa portée parente même après que la fonction parente a été supprimée de la pile d'appels.

**Note** : En JavaScript, lorsqu'une fonction est dite avoir été retirée/supprimée de la pile, cela signifie que la fonction a terminé sa durée de vie (a terminé son exécution), et toutes ses ressources ont été supprimées de la mémoire et ne sont plus accessibles.

Pensez à la pile d'appels comme au monde, tandis que parent et enfant sont deux entités dans le monde.

Dans ce cas, `parent` est la fonction qui a terminé son exécution et logiquement, tout ce qui la concerne devrait être hors de portée. Mais grâce au concept de fermeture, même lorsque la relation entre les fonctions `parent` et `child` a pris fin – c'est-à-dire, lorsque le parent est retiré de la pile (supprimé du monde) – la fonction enfant se souvient encore de tout ce qu'ils ont partagé ensemble.

**Note** : Tout ce qu'ils ont partagé ensemble, comme utilisé ci-dessus, signifie simplement les variables déclarées dans la fonction `parent` qui sont utilisées par la fonction `child`.

```js
function parent () {
	let a = "Az";
    
    return function child () {
        console.log(a);
    }
}
```

Dans l'extrait de code ci-dessus, la variable `a` est ce que les fonctions `parent` et `child` partagent ensemble.  
  
Ainsi, même lorsque `parent` est retiré de la pile d'appels, `child` se souvient encore de la valeur de `a` tant qu'il existe.

Si vous arrêtez de lire à ce stade, vous savez déjà ce qu'est conceptuellement une fermeture. Mais si vous voulez la comprendre pleinement et ne jamais l'oublier, nous devons plonger profondément dans le fonctionnement de JavaScript.

## Plongée profonde dans le concept de fermeture.

Pour vraiment comprendre les fermetures en JavaScript, vous devez être familiarisé avec les concepts suivants :

1. Le concept des fonctions étant des citoyens de première classe en JavaScript. Cela signifie que :

* Les fonctions peuvent être assignées à des variables en tant que valeurs

```js
const getName = function () {
	return 'Allice'   
};
```

Maintenant, vous pouvez simplement appeler la fonction `getName` comme vous appelleriez toute autre fonction en utilisant les parenthèses comme ceci `getName()`  
  
Pensez aux fonctions comme des objets appelables. Cela signifie, tout comme nous pouvons assigner des objets à des variables et les passer, vous pouvez faire de même avec les fonctions. La différence entre eux est que vous pouvez appeler une fonction lorsque vous avez besoin que le code qu'elle contient s'exécute.

* Les fonctions peuvent être passées à d'autres fonctions en tant qu'arguments

```js
setTimeout(getName, 5000)
```

Comme vous pouvez le voir dans l'extrait de code ci-dessus, lors de l'invocation de la fonction `setTimeout`, nous avons passé la fonction `getName` en tant qu'argument. Encore une fois, cela est dû au fait que les fonctions sont simplement des objets qui sont appelables.   
  
Notez que lorsque nous passons la fonction `getName` à la fonction `setTimeout`, nous ne l'appelons pas. Nous passons simplement la fonction en tant que valeur.   
  
Si nous appelions la fonction, nous passerions sa valeur de retour à la place et c'est une différence significative.  
  
J'aimerais également attirer votre attention sur le fait que mentionner le nom d'une fonction revient simplement à référencer cette fonction. Derrière la scène, le nom de la fonction est remplacé par la fonction elle-même.  
  
C'est-à-dire, ce code `setTimeout(getName, 5000)` est équivalent au code ci-dessous ;

```js
setTimeout(function () {
	return 'Allice'   
}, 5000)
```

Le nom de la fonction est remplacé par la fonction elle-même lors de l'exécution, tout comme un nom de variable régulier est remplacé par sa valeur lors de l'exécution.

* Les fonctions peuvent être retournées par d'autres fonctions.

```js
function multiplyBy (numberToMultiplyBy) {
	return function (numberToMultiply) {
		return numberToMultiply * numberToMultiplyBy
    }
}
```

En examinant de près l'extrait de code ci-dessus, vous remarquerez que nous avons une fonction appelée `multiplyBy` qui attend un argument lors de l'invocation et retourne une nouvelle fonction.   
  
La chose intéressante à noter ici est que lorsque nous appelons la fonction retournée, elle attend également un argument, mais cette fois, elle se souvient de l'argument passé à la fonction `multiplyBy` d'origine ( `numberToMultiplyBy` ), puis multiplie la valeur passée à elle-même ( `numberToMultiply` ) avec la valeur passée à sa fonction parente, et retourne le résultat.  
  
Observez attentivement le code ci-dessous qui utilise la fonction d'ordre supérieur `multiplyBy` :

```js
const multiplyByTwo = multiplyBy(2)
const result = multiplyByTwo(8)

console.log(result) // 16
```

2.  Le concept des fonctions d'ordre supérieur : c'est le deuxième concept dont vous devez être conscient pour comprendre la fermeture.

Une fonction d'ordre supérieur est une fonction qui :

* Accepte une fonction en tant qu'argument. Par exemple : `setTimeout`, `Promise`, et ainsi de suite.
* Retourne une fonction. Par exemple : la fonction `multiplyBy` déclarée ci-dessus.
* Ou remplit les première et deuxième conditions ci-dessus.

Maintenant que vous comprenez que les fonctions sont des citoyens de première classe et que vous avez vu des implémentations d'une fonction d'ordre supérieur, nous pouvons procéder à parler des fermetures.

Rappelez-vous qu'une fermeture se produit lorsqu'une fonction enfant conserve une référence à/se souvient d'une valeur ou d'une ressource qui appartenait à sa fonction parente même après que la fonction parente a été retirée de la pile d'appels.

Considérez ce code :

```js
function sally () {
	let age = 64;
    
    return function joe () {
        const data = {
        	name: "Joe",
            parentName: "Sally",
            parentAge: age
        }
		return data
    }
}
```

Dans l'extrait de code ci-dessus, nous pouvons observer que :

* `sally` est la fonction parente et elle déclare une portée
* `age` est une variable déclarée dans la portée `sally`
* `joe` est une fonction qui vit dans la portée `sally` et est retournée par la fonction `sally`. Vous devriez également noter que :  
- `joe` définit sa propre portée qui est une portée enfant de la portée `sally`  
- dans la portée `joe`, nous faisons référence à la variable `age` qui appartient à la portée `sally` (c'est là que la fermeture se produit parce que `joe` fait référence ou conserve une ressource/variable qui appartient à `sally`).

Parce que `joe` conserve une référence à la variable `age` qui appartient à `sally`, même lorsque `sally` a été retirée de la pile d'appels et sa portée supprimée, `joe` conservera l'accès à la variable `age` en raison du concept de fermeture.

Ainsi, dans le code ci-dessous :

```js
const joe = sally() // sally est invoquée et retourne la fonction joe
const joeyData = joe() // la fonction joe est invoquée et retourne un objet

console.log(joeyData) // nous enregistrons l'objet retourné.
```

Vous pouvez observer que même si `sally` est appelée et retirée de la pile, lorsque vous invoquez `joe` et enregistrez la valeur de retour de `joe` dans la console, elle se souvient encore de l'`age` de sally pendant l'exécution (auquel nous pouvons accéder dans l'objet retourné comme ceci `joeyData.parentAge`).

## Résumé

Lorsque une fonction enfant fait référence à des variables utilisées dans sa portée parente, une fermeture se produit.  
La fermeture est comme une boîte de mémoire qui stocke tous les éléments de la portée parente qui sont référencés à partir de la portée enfant.

Un coup d'œil aux diapositives ci-dessous devrait cimenter les connaissances que vous avez acquises jusqu'à présent et, espérons-le, tout se mettra en place.

<iframe class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/361482321f264b4aa170e04776365956" title="JavaScript Closure" allowfullscreen="true" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 432;" data-ratio="1.2962962962962963"></iframe>

Les fermetures déverrouillées ? Améliorez vos compétences en JavaScript avec plus de tutoriels de développement full-stack sur ma chaîne [YouTube](https://www.youtube.com/@asoluka_tee). Abonnez-vous maintenant pour ma prochaine playlist sur les concepts fondamentaux de JavaScript !

Merci d'avoir lu ! Bon codage !