---
title: Comment utiliser les outils de développement pour déboguer JavaScript dans
  le navigateur
date: '2024-10-30T15:00:55.881Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/how-to-use-developer-tools-to-debug-javascript-in-the-browser
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/gTs2w7bu3Qo/upload/f2ead89e25e967947691c8e4a1f8f862.jpeg
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
seo_desc: 'The console object is the number one go-to for developers when working
  with buggy JavaScript code.

  But if you still rely heavily on the console object alone to debug your JavaScript,
  then you''re missing out on some amazing browser developer tools fea...'
---


L'objet `console` est la ressource numéro un des développeurs lorsqu'ils travaillent sur du code JavaScript bogué.

<!-- more -->

Mais si vous vous appuyez encore exclusivement sur l'objet `console` pour déboguer votre JavaScript, vous passez à côté de fonctionnalités incroyables des outils de développement du navigateur.

Jetons un coup d'œil à la manière dont vous pouvez déboguer JavaScript avec les outils de développement de Chrome (DevTools).

## Le code bogué avec lequel nous travaillons

Pour commencer, j'ai préparé un code bogué qui est censé additionner quatre nombres et calculer leur moyenne.

Voici le HTML du code :

```
<label for="num1">Number 1:</label>
<input type="text" id="num1" placeholder="Enter a number" />

<label for="num2">Number 2:</label>
<input type="text" id="num2" placeholder="Enter a number" />

<label for="num3">Number 3:</label>
<input type="text" id="num3" placeholder="Enter a number" />

<label for="num4">Number 4:</label>
<input type="text" id="num4" placeholder="Enter a number" />

<button id="calculateBtn">Calculate Sum and Average</button>

<p id="addition-result"></p>
<p id="average-result"></p>

<script src="script.js"></script>
```

Voici le CSS minimal pour aligner les libellés sur leurs lignes respectives et agrandir un peu les éléments d'entrée et le bouton :

```
body {
  background: #d2d2d2;
}

label {
  display: block;
  margin-top: 0.5rem;
}

button {
  display: block;
  margin-top: 1rem;
}

input,
button {
  padding: 0.2rem;
}
```

Voici ce que le HTML et le CSS affichent dans le navigateur :

![Calculateur de somme et de moyenne](https://cdn.hashnode.com/res/hashnode/image/upload/v1729767323533/db4b903d-8cfe-4d6b-85b2-2233a2a2bcd0.png)

Et voici le JavaScript dans lequel le bogue se produit :

```
const calculateBtn = document.getElementById('calculateBtn');
const sumText = document.getElementById('sum');
const avgText = document.getElementById('average');

function calculateTotal(a, b, c, d) {
 return a + b + c + d;
}

function calculateAverage(total, count) {
 return total / count;
}

function handleButtonClick() {
 let num1 = document.getElementById('num1').value;
 let num2 = document.getElementById('num2').value;
 let num3 = document.getElementById('num3').value;
 let num4 = document.getElementById('num4').value;

 let total = calculateTotal(num1, num2, num3, num4);
 let average = calculateAverage(total, 4);

 sumText.textContent = `The sum is ${total}`;
 avgText.textContent = `The average is: ${average}`;
}

calculateBtn.addEventListener('click', handleButtonClick);
```

Voici ce qui se passe si vous saisissez les 4 nombres, par exemple `3`, `4`, `2`, `1`, et que vous cliquez sur le bouton `Calculate Sum and Average` :

![Somme et moyenne incorrectes](https://cdn.hashnode.com/res/hashnode/image/upload/v1729767417791/6c5a49d1-dc6f-45db-9720-c3c6daedbeb3.png)

Malheureusement, les nombres ont simplement été fusionnés et la moyenne est calculée sur cette base, ce qui signifie qu'une concaténation a lieu au lieu d'une addition. L'addition boguée entraîne également un calcul de moyenne erroné.

Investiguons ce qui se passe avec les outils de développement du navigateur.

## Comment déboguer du code JavaScript à l'aide des outils de développement Chrome

Lorsqu'un tel bogue survient, vous pourriez être tenté d'ajouter une multitude de logs console.

Bien souvent, les logs console permettent de résoudre le problème, mais vous devez passer beaucoup de temps à analyser les choses.

Les outils de développement du navigateur vous offrent plus d'options, comme l'ajout de points d'arrêt (breakpoints), la surveillance d'expressions particulières et même l'exécution du code ligne par ligne pour voir où le bogue se produit.

### Comment ouvrir les outils de développement et l'onglet Sources

Pour commencer, faites un clic droit dans le navigateur et sélectionnez "Inspecter" pour ouvrir les DevTools de Chrome.

Une fois dans les DevTools, rendez-vous sur l'onglet "Sources" pour voir les fichiers du programme. Vous pouvez également appuyer sur `F12` sur votre clavier et sélectionner l'onglet Sources.

Voici une brève anatomie de l'onglet Sources des DevTools de Chrome :

![Anatomie de l'onglet Sources des outils de développement Chrome](https://cdn.hashnode.com/res/hashnode/image/upload/v1729767628385/30310aa1-ddb0-41d5-a3ce-9ecc84b034e3.png)

En haut de l'onglet du débogueur se trouvent des icônes grisées. Lorsqu'elles sont actives, elles vous permettent d'exécuter votre code pas à pas et d'ajouter ou de supprimer des points d'arrêt.

On trouve également dans l'onglet du débogueur :

-   Watch : où vous pouvez ajouter et voir les expressions surveillées.
    
-   Breakpoints : où vous pouvez voir le code de la ligne où vous avez ajouté un point d'arrêt.
    
-   Scope : contient les variables locales et globales.
    
-   Callstack : affiche les appels de fonctions qui mènent au point actuel de l'exécution du code.
    

Pour voir le contenu d'un fichier, il suffit de cliquer dessus. Après cela, certaines icônes de l'onglet du débogueur ne seront plus grisées.

![Icônes de l'onglet Sources des outils de développement Chrome](https://cdn.hashnode.com/res/hashnode/image/upload/v1729767971149/04f8e5c7-a08a-49b3-be7f-2854f820b94a.png)

### Comment déboguer le code en ajoutant des points d'arrêt

Pour commencer à déboguer le code, vous pouvez ajouter un point d'arrêt à une ligne en cliquant sur son numéro.

Un point d'arrêt est comme un marqueur de ligne que vous pouvez définir dans les outils de développement pour suspendre l'exécution de votre code avant que cette ligne ne s'exécute. Cela vous permet de vérifier les valeurs des variables, de voir si les fonctions sont appelées comme prévu ou d'observer le flux général du code.

Lorsque vous ajoutez un point d'arrêt et exécutez le code, une icône bleuâtre apparaît sur cette ligne, indiquant que l'exécution s'arrêtera avant cette ligne.

Alternativement, vous pouvez ajouter l'instruction `debugger` à la ligne où vous souhaitez que l'exécution soit suspendue. Mais restons-en à l'utilisation des points d'arrêt.

Par exemple, ajoutons un point d'arrêt à la ligne 14, puis saisissons les quatre nombres et cliquons sur le bouton `Calculate Sum and Average` pour que le code s'exécute :

![Point d'arrêt à la ligne 14](https://cdn.hashnode.com/res/hashnode/image/upload/v1729768234921/8c1f0d4e-5fb2-4461-8e62-574d95a51672.png)

À ce stade, vous pouvez voir que l'exécution ne s'est pas poursuivie – c'est pourquoi vous voyez "value unavailable" pour toutes les variables sous "Local".

À partir de là, vous pouvez commencer à parcourir le code ligne par ligne en appuyant sur l'icône de pas à pas (step) dans le coin supérieur droit :

![L'icône de pas à pas de l'onglet Sources des outils de développement Chrome](https://cdn.hashnode.com/res/hashnode/image/upload/v1729768323163/45fb5c6b-682d-4b90-8bec-d4ef8596c4b7.png)

Une fois que vous cliquez sur l'icône de pas à pas, la ligne que vous quittez s'exécute.

![Cliquer sur l'icône de pas à pas](https://cdn.hashnode.com/res/hashnode/image/upload/v1729768411765/f2670800-c8d8-490f-8dc9-1fdfa8c8da7b.png)

Vous pouvez voir que `"3"` est la valeur pour la ligne `14`. Cette valeur est entourée d'une paire de guillemets doubles. Cela signifie qu'il s'agit d'une chaîne de caractères (string). Vous devez cependant en être certain, et c'est ce que la fonctionnalité Watch vous permet de faire. Vous découvrirez cette fonctionnalité bientôt.

Si vous travaillez avec plusieurs lignes de code, parcourir le code ligne par ligne peut prendre du temps. Vous devrez donc peut-être ajouter un autre point d'arrêt.

Je vais maintenant définir un point d'arrêt à la ligne `23` et exécuter à nouveau le code :

![Point d'arrêt à la ligne 23](https://cdn.hashnode.com/res/hashnode/image/upload/v1729768528136/478fc837-0c16-4990-9b70-19ff1695331e.png)

Maintenant, vous pouvez voir que tous les résultats des variables, à l'exception de `average`, semblent être des chaînes de caractères. Cela nous amène à la fonctionnalité suivante du débogueur des outils de développement Chrome : le Watcher.

### Comment utiliser la fonctionnalité Watch des outils de développement

La fonctionnalité Watch des outils de développement vous permet de surveiller des variables ou des expressions spécifiques pendant l'exécution de votre code.

Pour confirmer le type de données des variables, vous pouvez ajouter une expression watch qui affiche leurs valeurs ou, plus précisément, leurs types.

Pour ajouter une expression watch, cliquez sur l'icône plus (+) juste à côté de "Watch" et appuyez sur `ENTER` sur votre clavier.

![Ajout d'une expression watch](https://cdn.hashnode.com/res/hashnode/image/upload/v1729768780977/ef22ae71-068c-41a2-9a2e-509c7c6a8afb.png)

Voici les expressions watch qui confirment que `num1` à `num4` ainsi que `total` sont des chaînes de caractères – alors qu'elles devraient être des entiers :

![Expressions watch](https://cdn.hashnode.com/res/hashnode/image/upload/v1729768808497/5d7352d6-37b3-490c-9ce2-f430c2d9a0e6.png)

Vous pouvez également vérifier cela dans l'onglet console en examinant les types des variables à cet endroit :

![Types de variables dans la console](https://cdn.hashnode.com/res/hashnode/image/upload/v1729768847227/3730a133-0a5b-4eb1-a5dd-257fa0ac2293.png)

Cela signifie que les nombres que vous saisissez sont interprétés comme des chaînes de caractères. C'est parce qu'en JavaScript, les valeurs provenant d'éléments HTML comme les champs de saisie (input) sont toujours récupérées sous forme de chaînes.

Cela se produit car la propriété `value` d'un élément input renvoie une chaîne, que vous saisissiez des chiffres ou non – et c'est ainsi que le bogue a été introduit.

Rappelez-vous que JavaScript ne fait que concaténer les chaînes, même s'il s'agit de nombres. Cela signifie que `"3"` est de type string et non de type integer.

Pour corriger le bogue, vous devez changer les types de `num1` à `num4` en entiers afin que JavaScript puisse additionner correctement leurs valeurs.

Vous pouvez ensuite corriger cela directement dans les DevTools et appuyer sur `CTRL + S` sous Windows ou `CMD + S` sur Mac pour enregistrer le code. Vous pouvez également le corriger dans votre éditeur de code en enveloppant les variables des nombres dans `parseInt()`.

Une fois cela fait et le code réexécuté, les types de données corrects devraient apparaître dans le watcher, et les valeurs de variables correctes devraient s'afficher sous Local :

![Types de variables corrects dans le watch](https://cdn.hashnode.com/res/hashnode/image/upload/v1729768941146/964cabbd-2298-4303-ac0d-2b54af070d66.png)

Vous pouvez également implémenter les modifications dans votre éditeur de code pour que tout fonctionne. Voici le code corrigé :

```
const calculateBtn = document.getElementById('calculateBtn');
const sumText = document.getElementById('sum');
const avgText = document.getElementById('average');

function calculateTotal(a, b, c, d) {
  return a + b + c + d;
}

function calculateAverage(total, count) {
  return total / count;
}

function handleButtonClick() {
  let num1 = parseInt(document.getElementById('num1').value);
  let num2 = parseInt(document.getElementById('num2').value);
  let num3 = parseInt(document.getElementById('num3').value);
  let num4 = parseInt(document.getElementById('num4').value);

  let total = calculateTotal(num1, num2, num3, num4);
  let average = calculateAverage(total, 4);

  sumText.textContent = `The sum is ${total}`;
  avgText.textContent = `The average is: ${average}`;
}

calculateBtn.addEventListener('click', handleButtonClick);
```

Et voici le résultat dans le navigateur :

![Calculateur de somme et de moyenne fonctionnant correctement](https://cdn.hashnode.com/res/hashnode/image/upload/v1729769063113/b7e39538-e9fe-4ce5-a4de-e98f43263235.png)

## Conclusion

C'est ainsi que vous pouvez déboguer JavaScript à l'aide des outils de développement de Chrome. Les fonctionnalités de point d'arrêt et de watcher, ainsi que les boutons d'exécution pas à pas, sont des améliorations majeures par rapport à un simple log console.

Notez que chaque navigateur moderne possède cet outil de débogage JavaScript intégré, vous pouvez donc utiliser la même approche pour déboguer JavaScript avec Firefox ou Edge.