---
title: JavaScript Asynchrone – Callbacks, Promises et Async/Await Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-20T20:10:50.000Z'
originalURL: https://freecodecamp.org/news/asynchronous-javascript-explained
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727436410214/26117e35-6f63-4788-9b97-3aa225527213.png
tags:
- name: async/await
  slug: asyncawait
- name: asynchronous
  slug: asynchronous
- name: JavaScript
  slug: javascript
seo_title: JavaScript Asynchrone – Callbacks, Promises et Async/Await Expliqués
seo_desc: 'By Njong Emy

  If you''ve been learning JavaScript for a while now, then you''ve probably heard
  the term "asynchronous" before.

  This is because JavaScript is an asynchronous language...but what does that really
  mean? In this article, I hope to show you t...'
---

Par Njong Emy

Si vous apprenez JavaScript depuis un certain temps, vous avez probablement déjà entendu le terme "asynchrone".

C'est parce que JavaScript est un langage asynchrone... mais qu'est-ce que cela signifie vraiment ? Dans cet article, j'espère vous montrer que le concept n'est pas aussi difficile qu'il n'y paraît.

# Synchrone vs Asynchrone

Avant de plonger dans le vif du sujet, examinons ces deux mots – synchrone et asynchrone.

Par défaut, JavaScript est un langage de programmation synchrone et monothread. Cela signifie que les instructions ne peuvent s'exécuter que les unes après les autres, et non en parallèle. Considérez le petit extrait de code ci-dessous :

```javascript
let a = 1;
let b = 2;
let sum = a + b;
console.log(sum);
```

Le code ci-dessus est assez simple – il additionne deux nombres puis enregistre la somme dans la console du navigateur. L'interpréteur exécute ces instructions les unes après les autres dans cet ordre jusqu'à ce qu'il ait terminé.

Mais cette méthode présente des inconvénients. Supposons que nous voulions récupérer une grande quantité de données depuis une base de données et les afficher ensuite sur notre interface. Lorsque l'interpréteur atteint l'instruction qui récupère ces données, le reste du code est bloqué jusqu'à ce que les données aient été récupérées et retournées.

Vous pourriez dire que les données à récupérer ne sont pas si volumineuses et que cela ne prendra pas de temps notable. Imaginez que vous devez récupérer des données à plusieurs endroits différents. Ce délai cumulé ne semble pas être quelque chose que les utilisateurs voudraient rencontrer.

Heureusement pour nous, les problèmes du JavaScript synchrone ont été résolus par l'introduction du JavaScript asynchrone.

Considérez le code asynchrone comme un code qui peut commencer maintenant et terminer son exécution plus tard. Lorsque JavaScript s'exécute de manière asynchrone, les instructions ne sont pas nécessairement exécutées les unes après les autres comme nous l'avons vu précédemment.

Afin de mettre en œuvre correctement ce comportement asynchrone, plusieurs solutions différentes ont été utilisées par les développeurs au fil des ans. Chaque solution améliore la précédente, ce qui rend le code plus optimisé et plus facile à comprendre en cas de complexité.

Pour mieux comprendre la nature asynchrone de JavaScript, nous allons passer en revue les fonctions de rappel, les promesses, et async et await.

# Que sont les Callbacks en JavaScript ?

Un callback est une fonction qui est passée à l'intérieur d'une autre fonction, puis appelée dans cette fonction pour effectuer une tâche.

Confus ? Décomposons cela en l'implémentant pratiquement.

```javascript
console.log('fired first');
console.log('fired second');

setTimeout(()=>{
    console.log('fired third');
},2000);

console.log('fired last');
```

L'extrait ci-dessus est un petit programme qui enregistre des éléments dans la console. Mais il y a quelque chose de nouveau ici. L'interpréteur exécutera la première instruction, puis la deuxième, mais il sautera la troisième et exécutera la dernière.

La fonction `setTimeout` est une fonction JavaScript qui prend deux paramètres. Le premier paramètre est une autre fonction, et le second est le temps après lequel cette fonction doit être exécutée en millisecondes. Vous voyez maintenant la définition des callbacks entrer en jeu.

La fonction à l'intérieur de `setTimeout` dans ce cas est requise pour s'exécuter après deux secondes (2000 millisecondes). Imaginez qu'elle soit emportée pour être exécutée dans une partie séparée du navigateur, tandis que les autres instructions continuent de s'exécuter. Après deux secondes, les résultats de la fonction sont ensuite retournés.

C'est pourquoi si nous exécutons l'extrait ci-dessus dans notre programme, nous obtiendrons ceci :

```javascript
fired first
fired second
fired last
fired third
```

Vous voyez que la dernière instruction est enregistrée avant que la fonction dans `setTimeout` ne retourne son résultat. Supposons que nous utilisions cette méthode pour récupérer des données depuis une base de données. Pendant que l'utilisateur attend que l'appel à la base de données retourne des résultats, le flux d'exécution ne sera pas interrompu.

Cette méthode était très efficace, mais seulement jusqu'à un certain point. Parfois, les développeurs doivent faire plusieurs appels à différentes sources dans leur code. Pour faire ces appels, les callbacks sont imbriqués jusqu'à ce qu'ils deviennent très difficiles à lire ou à maintenir. Cela est appelé **Callback Hell**.

Pour résoudre ce problème, les promesses ont été introduites.

# Que sont les Promesses en JavaScript ?

Nous entendons les gens faire des promesses tout le temps. Ce cousin qui vous a promis de vous envoyer de l'argent gratuitement, un enfant promettant de ne plus toucher au bocal à cookies sans permission... mais les promesses en JavaScript sont légèrement différentes.

Une promesse, dans notre contexte, est quelque chose qui prendra un certain temps à faire. Il y a deux résultats possibles pour une promesse :

* Soit nous exécutons et résolvons la promesse, soit
  
* Une erreur se produit et la promesse est rejetée
  

Les promesses sont venues pour résoudre les problèmes des fonctions de rappel. Une promesse prend deux fonctions comme paramètres. C'est-à-dire, `resolve` et `reject`. Rappelez-vous que resolve est un succès, et reject est pour quand une erreur se produit.

Regardons les promesses en action :

```javascript
const getData = (dataEndpoint) => {
   return new Promise ((resolve, reject) => {
     //une requête vers l'endpoint;
     
     if(request is successful){
       //faire quelque chose;
       resolve();
     }
     else if(there is an error){
       reject();
     }
   
   });
};
```

Le code ci-dessus est une promesse, encapsulée par une requête vers un endpoint. La promesse prend `resolve` et `reject` comme je l'ai mentionné précédemment.

Après avoir fait un appel à l'endpoint par exemple, si la requête est réussie, nous résolvons la promesse et continuons à faire ce que nous voulons avec la réponse. Mais s'il y a une erreur, la promesse sera rejetée.

Les promesses sont une manière élégante de résoudre les problèmes causés par l'enfer des callbacks, dans une méthode connue sous le nom de **chaînage de promesses**. Vous pouvez utiliser cette méthode pour obtenir séquentiellement des données depuis plusieurs endpoints, mais avec moins de code et des méthodes plus faciles.

Mais il y a une manière encore meilleure ! Vous êtes peut-être familier avec la méthode suivante, car c'est une manière préférée de gérer les données et les appels API en JavaScript.

# Qu'est-ce que Async et Await en JavaScript ?

Le problème, c'est que le chaînage des promesses ensemble, tout comme les callbacks, peut devenir assez encombrant et confus. C'est pourquoi Async et Await a été introduit.

Pour définir une fonction async, vous faites ceci :

```javascript
const asyncFunc = async() => {

}
```

Notez qu'appeler une fonction async retournera toujours une Promise. Regardez ceci :

```javascript
const test = asyncFunc();
console.log(test);
```

En exécutant ce qui précède dans la console du navigateur, nous voyons que `asyncFunc` retourne une promesse.

Décortiquons vraiment du code maintenant. Considérez le petit extrait ci-dessous :

```javascript
const asyncFunc = async () => {
	const response = await fetch(resource);
   	const data = await response.json();
}
```

Le mot-clé `async` est ce que nous utilisons pour définir les fonctions async comme je l'ai mentionné ci-dessus. Mais qu'en est-il de `await` ? Eh bien, il bloque JavaScript d'assigner `fetch` à la variable response jusqu'à ce que la promesse soit résolue. Une fois la promesse résolue, les résultats de la méthode fetch peuvent maintenant être assignés à la variable response.

La même chose se produit à la ligne 3. La méthode `.json` retourne une promesse, et nous pouvons encore utiliser `await` pour retarder l'assignation jusqu'à ce que la promesse soit résolue.

# Bloquer le Code ou Non

Lorsque je dis 'bloquer', vous devez penser que la mise en œuvre de Async et Await bloque somehow l'exécution du code. Parce que, que se passe-t-il si notre requête prend trop de temps, n'est-ce pas ?

En fait, ce n'est pas le cas. Le code qui est à l'intérieur de la fonction async est bloquant, mais cela n'affecte en rien l'exécution du programme. L'exécution de notre code est tout aussi asynchrone que jamais. Pour le montrer,

```markdown
const asyncFunc = async () => {
	const response = await fetch(resource);
   	const data = await response.json();
}

console.log(1);
cosole.log(2);

asyncFunc().then(data => console.log(data));

console.log(3);
console.log(4);
```

Dans notre console de navigateur, la sortie de ce qui précède ressemblerait à ceci :

```markdown
1
2
3
4
data returned by asyncFunc
```

Vous voyez que lorsque nous avons appelé `asyncFunc`, notre code a continué à s'exécuter jusqu'à ce qu'il soit temps pour la fonction de retourner les résultats.

# Conclusion

Cet article ne traite pas de ces concepts en profondeur, mais j'espère qu'il vous montre ce que le JavaScript asynchrone implique et quelques points à surveiller.

C'est une partie très essentielle de JavaScript, et cet article ne fait qu'effleurer la surface. Néanmoins, j'espère que cet article a aidé à décomposer ces concepts.