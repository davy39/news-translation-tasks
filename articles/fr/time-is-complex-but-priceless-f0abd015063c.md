---
title: 'Les algorithmes en anglais simple : complexité temporelle et notation Big-O'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-18T18:43:30.000Z'
originalURL: https://freecodecamp.org/news/time-is-complex-but-priceless-f0abd015063c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1-5hf_o6j3szhVe33L104A.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Les algorithmes en anglais simple : complexité temporelle et notation
  Big-O'
seo_desc: 'By Michael Olorunnisola

  Every good developer has time on their mind. They want to give their users more
  of it, so they can do all those things they enjoy. They do this by minimizing time
  complexity.

  Before you can understand time complexity in progra...'
---

Par Michael Olorunnisola

Tout bon développeur a le temps en tête. Ils veulent offrir plus de temps à leurs utilisateurs, afin qu'ils puissent faire toutes ces choses qu'ils aiment. Ils y parviennent en minimisant la **complexité temporelle**.

Avant de pouvoir comprendre la complexité temporelle en programmation, vous devez comprendre où elle est le plus couramment appliquée : dans la conception des **algorithmes**.

### Alors, qu'est-ce qu'un algorithme, au fait ?

Simplement, un algorithme est une série d'étapes contenues, que vous suivez dans un certain ordre pour atteindre un objectif ou produire une sortie. Prenons par exemple la recette de votre grand-mère pour cuire un gâteau. Attendez, cela compte-t-il comme un algorithme ? Bien sûr que oui !

```js
function BakeCake(flavor, icing){
"
 1. Préchauffer le four à 350 F
 2. Mélanger la farine, la poudre à lever, le sel
 3. Battre le beurre et le sucre jusqu'à ce que le mélange soit léger
 4. Ajouter les œufs.
 5. Incorporer la farine, la poudre à lever, le sel
 6. Ajouter le lait et " + flavor + "
 7. Mélanger davantage
 8. Mettre dans le moule
 9. Cuire pendant 30 minutes
10." + if(icing === true) return 'ajouter le glaçage' + "
10. Se régaler
"
}

BakeCake('vanilla', true) => délicieux
```

Les algorithmes sont utiles dans notre examen de la complexité temporelle car ils se présentent sous toutes les formes et toutes les tailles.

De la même manière que vous pouvez couper une tarte de 100 façons différentes, vous pouvez résoudre un seul problème avec de nombreux algorithmes différents. Certaines solutions sont simplement plus efficaces, prenant moins de temps et nécessitant moins d'espace que d'autres.

La question principale est donc : comment analyser quelles solutions sont les plus efficaces ?

Les mathématiques à la rescousse ! L'analyse de la complexité temporelle en programmation est simplement une méthode mathématique extrêmement simplifiée pour analyser combien de temps un algorithme avec un nombre donné d'entrées (n) prendra pour accomplir sa tâche. Elle est généralement définie en utilisant la **notation Big-O**.

### Qu'est-ce que la notation Big O, demandez-vous ?

Si vous promettez de ne pas abandonner et de continuer à lire, je vous le dirai.

La notation Big-O est une manière de convertir les étapes globales d'un algorithme en termes algébriques, puis d'exclure les constantes et coefficients d'ordre inférieur qui n'ont pas un impact si important sur la complexité globale du problème.

Les mathématiciens grimaceront probablement un peu face à mon hypothèse d'impact global, mais pour que les développeurs gagnent du temps, il est plus facile de simplifier les choses ainsi :

```
Régulier       Big-O

2             O(1)   --> Ce n'est qu'un nombre constant

2n + 10       O(n)   --> n a l'effet le plus grand

5n^2          O(n^2) --> n^2 a l'effet le plus grand
```

En bref, tout ce que cet exemple dit est : nous ne regardons que le facteur dans notre expression qui a le potentiel d'avoir le plus grand impact sur la valeur que notre expression retournera. (Cela change lorsque la constante devient extrêmement grande et que n devient petit, mais ne nous inquiétons pas de cela pour l'instant).

Voici quelques complexités temporelles courantes avec des définitions simples. N'hésitez pas à consulter [Wikipedia](https://en.wikipedia.org/wiki/Time_complexity), cependant, pour des définitions plus approfondies.

* O(1) — Temps constant : Étant donné une entrée de taille n, il ne faut qu'une seule étape pour que l'algorithme accomplisse la tâche.
* O(log n) — Temps logarithmique : étant donné une entrée de taille n, le nombre d'étapes nécessaires pour accomplir la tâche est diminué par un certain facteur à chaque étape.
* O(n) — Temps linéaire : Étant donné une entrée de taille n, le nombre d'étapes requises est directement lié (1 à 1)
* O(n²) — Temps quadratique : Étant donné une entrée de taille n, le nombre d'étapes nécessaires pour accomplir une tâche est le carré de n.
* O(C^n) — Temps exponentiel : Étant donné une entrée de taille n, le nombre d'étapes nécessaires pour accomplir une tâche est une constante à la puissance n (nombre assez grand).

Avec cette connaissance en main, voyons le nombre d'étapes que chacune de ces complexités temporelles implique :

```js
let n = 16;

O (1) = 1 étape "(génial !)"

O (log n) = 4 étapes "(génial !)" -- base 2 supposée

O (n) = 16 étapes "(pas mal !)"

O(n^2) = 256 étapes "(euh... on peut travailler avec ça ?)"

O(2^n) = 65,536 étapes "(...)"
```

Comme vous pouvez le voir, les choses peuvent facilement devenir des ordres de grandeur plus complexes en fonction de la complexité de votre algorithme. Heureusement, les ordinateurs sont suffisamment puissants pour encore gérer des complexités très grandes relativement rapidement.

Alors, comment analyser notre code avec la notation Big-O ?

Voici quelques exemples rapides et simples de la manière dont vous pouvez appliquer cette connaissance aux algorithmes que vous pourriez rencontrer dans la nature ou coder vous-même.

Nous utiliserons les structures de données suivantes pour nos exemples :

```js
var friends = {
 'Mark' : true,
 'Amy' : true,
 'Carl' : false,
 'Ray' :  true,
'Laura' : false,
}
var sortedAges = [22, 24, 27, 29, 31]
```

#### **O(1) — Temps constant**

Les recherches de valeurs lorsque vous connaissez la clé (objets) ou l'index (tableaux) prennent toujours une étape et sont donc en temps constant.

```js
//Si je connais le nom de la personne, je n'ai qu'à faire une étape pour vérifier :

function isFriend(name){ //similaire à connaître l'index dans un tableau 
  return friends[name]; 
};

isFriend('Mark') // retourne True et n'a pris qu'une seule étape

function add(num1,num2){ // J'ai deux nombres, il faut une étape pour retourner la valeur
 return num1 + num2
}
```

#### **O(log n) — Temps logarithmique**

Si vous savez de quel côté du tableau chercher un élément, vous gagnez du temps en éliminant l'autre moitié.

```js
//Vous diminuez la quantité de travail que vous avez à faire à chaque étape

function thisOld(num, array){
  var midPoint = Math.floor( array.length /2 );
  if( array[midPoint] === num) return true;
  if( array[midPoint] < num ) --> ne regarder que la deuxième moitié du tableau
  if( array[midpoint] > num ) --> ne regarder que la première moitié du tableau
  // répéter récursivement jusqu'à ce que vous arriviez à votre solution
  
}

thisOld(29, sortedAges) // retourne true 

//Notes
 //Il y a un tas d'autres vérifications qui devraient aller dans cet exemple pour qu'il soit vraiment fonctionnel, mais ce n'est pas nécessaire pour cette explication.
 //Cette solution fonctionne parce que notre tableau est trié
 //Les solutions récursives sont souvent logarithmiques
 //Nous aborderons la récursivité dans un autre article !
```

#### **O(n) — Temps linéaire**

Vous devez regarder chaque élément du tableau ou de la liste pour accomplir la tâche. Les boucles **for** simples sont presque toujours en temps linéaire. De plus, les méthodes de tableau comme **indexOf** sont également en temps linéaire. Vous êtes simplement abstrait du processus de boucle.

```js
//Le nombre d'étapes que vous faites est directement corrélé à la taille de votre entrée

function addAges(array){
  var sum = 0;
  for (let i=0 ; i < array.length; i++){  //doit passer par chaque valeur
    sum += array[i]
  }
 return sum;
}

addAges(sortedAges) //133
```

#### **O(n²) — Temps quadratique**

Les boucles **for** imbriquées sont en temps quadratique, car vous exécutez une opération linéaire dans une autre opération linéaire (ou n*n = n²).

```js
//Le nombre d'étapes que vous faites est le carré de la taille de votre entrée

function addedAges(array){
  var addedAge = [];
    for (let i=0 ; i < array.length; i++){ //doit passer par chaque valeur
      for(let j=i+1 ; j < array.length ; j++){ //et les parcourir à nouveau
        addedAge.push(array[i] + array[j]);
      }
    }
  return addedAge;
}

addedAges(sortedAges); //[ 46, 49, 51, 53, 51, 53, 55, 56, 58, 60 ]

//Notes
 //Boucles for imbriquées. Si une boucle for est en temps linéaire (n)
 //Alors deux boucles for imbriquées sont (n * n) ou (n^2) Quadratique !
```

#### **O(2^n) — Temps exponentiel**

Le temps exponentiel est généralement pour les situations où vous ne savez pas grand-chose, et vous devez essayer toutes les combinaisons ou permutations possibles.

```js
//Le nombre d'étapes nécessaires pour accomplir une tâche est une constante à la puissance n

//Exemple de réflexion
 //Essayer de trouver toutes les combinaisons de lettres pour un mot de passe de longueur n
```

Vous devriez analyser la complexité temporelle chaque fois que vous écrivez du code qui doit s'exécuter rapidement.

Lorsque vous avez diverses routes pour résoudre un problème, il est définitivement plus sage de créer une solution qui fonctionne d'abord. Mais à long terme, vous voudrez une solution qui s'exécute aussi rapidement et efficacement que possible.

Pour vous aider dans le processus de résolution de problèmes, voici quelques questions simples à poser :

> 1. Cela résout-il le problème ? **Oui** =>  
>   
> 2. Avez-vous le temps de travailler sur cela  
>   
> **Oui** => passez à l'étape 3  
>   
> **Non** => Revenez-y plus tard et passez à l'étape 6 pour l'instant.  
>   
> 3. Cela couvre-t-il tous les cas limites ? **Oui** =>  
>   
> 4. Mes complexités sont-elles aussi basses que possible ?  
>   
> **Non** => réécrire ou modifier en une nouvelle solution -> retour à l'étape 1  
>   
> **Oui** => passez à l'étape 5  
>   
> 5. Mon code est-il D.R.Y ? **Oui** =>  
>   
> 6. Réjouissez-vous !  
>   
> **Non** => Rendez-le D.R.Y, puis réjouissez-vous !

Analysez la complexité temporelle chaque fois que vous essayez de résoudre un problème. Cela fera de vous un meilleur développeur à long terme. Vos coéquipiers et utilisateurs vous en seront reconnaissants.

Encore une fois, la plupart des problèmes auxquels vous serez confronté en tant que programmeur — qu'ils soient algorithmiques ou programmatiques — auront des dizaines, sinon des centaines de façons de les résoudre. Ils peuvent varier dans la manière dont ils résolvent le problème, mais ils résolvent tous ce problème.

Vous pourriez prendre des décisions sur l'utilisation de sets ou de graphes pour stocker des données. Vous pourriez décider d'utiliser Angular, React ou Backbone pour un projet d'équipe. Toutes ces solutions résolvent le même problème de manière différente.

Étant donné cela, il est difficile de dire qu'il existe une seule réponse juste ou meilleure à ces problèmes. Mais il est possible de dire qu'il existe des réponses meilleures ou pires à un problème donné.

En utilisant l'un de nos exemples précédents, il pourrait être préférable d'utiliser React pour un projet d'équipe si la moitié de votre équipe a de l'expérience avec celui-ci, afin qu'il faille moins de temps pour se lancer.

La capacité à décrire une meilleure solution provient généralement d'une certaine forme d'analyse de la complexité temporelle.

En bref, si vous allez résoudre un problème, résolvez-le bien. Et utilisez un peu de Big-O pour vous aider à déterminer comment.

Voici un récapitulatif final :

* **O(1) —** Temps constant : il ne faut qu'une seule étape pour que l'algorithme accomplisse la tâche.
* **O(log n) —** Temps logarithmique : Le nombre d'étapes nécessaires pour accomplir une tâche est diminué par un certain facteur à chaque étape.
* **O(n) —** Temps linéaire : Le nombre d'étapes requises est directement lié (1 à 1).
* **O(n²) —** Temps quadratique : Le nombre d'étapes nécessaires pour accomplir une tâche est le carré de n.
* **O(C^n) —** Exponentiel : Le nombre d'étapes nécessaires pour accomplir une tâche est une constante à la puissance n (nombre assez grand).

Et voici quelques ressources utiles pour en apprendre davantage :

* [Wikipedia](https://en.wikipedia.org/wiki/Time_complexity)
* Le [Big O Cheat Sheet](http://bigocheatsheet.com/) est une excellente ressource avec des complexités temporelles algorithmiques courantes et une représentation graphique. Consultez-le !