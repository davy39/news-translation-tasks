---
title: Maîtrisez l'art de la boucle en JavaScript avec ces incroyables astuces
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T21:58:40.000Z'
originalURL: https://freecodecamp.org/news/master-the-art-of-looping-in-javascript-with-these-incredible-tricks-a5da1aa1d6c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oyfRe4XwyuFfhK41WJVMdw.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Maîtrisez l'art de la boucle en JavaScript avec ces incroyables astuces
seo_desc: 'By Yogi

  Many times in your code you require to loop through an array of numbers, strings
  or object. There are just so many ways to do it, and this tutorial aims to teach
  you all of them so that you become a Master of ‘Looping in JavaScript’.

  See this...'
---

Par Yogi

De nombreuses fois dans votre code, vous devez parcourir un **tableau de nombres, de chaînes ou d'objets**. Il existe tant de façons de le faire, et ce tutoriel vise à vous enseigner toutes ces méthodes afin que vous deveniez un Maître de la "Boucle en JavaScript".

Regardez ce chat ninja qui est le maître du saut.

<iframe src="https://giphy.com/embed/vhp0BocGjkVjO" width="480" height="373" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cat-ninja-parkour-vhp0BocGjkVjO">via GIPHY</a></p>

Comme le chat, vous deviendrez également un Maître de la Boucle en JavaScript, après avoir appris toutes les astuces de boucle.

### **1. La boucle "For"**

La **boucle For** est la manière la plus basique de boucler dans votre code JavaScript. Elle est très pratique pour exécuter un bloc de code un certain nombre de fois. Elle utilise un **compteur**, dont la valeur est d'abord initialisée, puis sa valeur finale est spécifiée.

Le **compteur est augmenté d'une valeur spécifique** chaque fois que la boucle s'exécute. La boucle For vérifie si le compteur est dans les limites (valeur initiale à valeur finale), et la boucle se termine lorsque la valeur du compteur dépasse la valeur finale.

Permettez-moi de vous montrer quelques exemples.

#### a. Parcourir un tableau

Dans le code ci-dessous, je parcours tous les **nombres d'un tableau** et j'affiche chacun d'eux dans la fenêtre de la console.

```js
var numbers = [10, 20, 30, 40, 50];
for (var i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
```

De la même manière, vous pouvez parcourir des tableaux de chaînes également.

#### b. Parcourir les éléments DOM

Supposons que vous souhaitez **trouver et colorer toutes les ancres** de la page en rouge. Alors ici aussi, vous pouvez utiliser la **boucle For** comme ceci :

```js
var elements = document.querySelectorAll("a");
for (var i= 0; i < elements.length; i++) {
    elements[i].style.color = "red";
}
```

_Explication_ : J'ai d'abord obtenu toutes les ancres dans un tableau en utilisant `**document.querySelectorAll("a")**`. Ensuite, j'ai simplement parcouru chacune d'elles et changé leur couleur en rouge.

Je suis allé sur le site W3Schools et j'ai exécuté le code ci-dessus sur la console du navigateur, et voyez ce qu'il a fait :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QNXWEhb8zst1xFsYJAD2pg.png)
_**Changement de la couleur de toutes les ancres en rouge**_

> Note : **jQuery** dispose également d'une méthode de boucle très pratique appelée [**méthode jQuery Each**](http://www.yogihosting.com/jquery-each/) qui vous aide à parcourir les tableaux, les objets, les éléments DOM, JSON et XML assez facilement. Si vous utilisez jQuery dans votre site web, envisagez de l'utiliser lors de vos boucles.

### **2. La boucle "For In"**

La boucle **For In** est utilisée pour parcourir les **propriétés d'un objet/tableau** sans utiliser de "compteur". C'est donc une version simplifiée de la **boucle For**.

Le bloc de code à l'intérieur de la boucle sera exécuté une fois pour chaque propriété.

#### a. Parcourir les propriétés d'un objet

J'ai un objet qui contient certaines propriétés. Je vais utiliser la **boucle For In** pour rechercher chaque propriété et sa valeur.

Le code ci-dessous **affiche toutes les propriétés et leurs valeurs** dans la fenêtre de la console.

```js
var person = { fname: "Nick", lname: "Jonas", age: 26 };
for (var x in person) {
    console.log(x + ": " + person[x])
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*hcxLefNPQ0RsJn0GBskJEw.png)
_**Parcourir les propriétés d'un objet avec la boucle "For In" en JavaScript**_

#### b. Parcourir JSON

**JSON** est un format très populaire pour transmettre des objets de données constitués de paires **attribut-valeur** et de types de données de tableau. Les sites web utilisent JSON pour partager leurs informations avec des sites externes. Maintenant, je vais vous expliquer comment extraire des données d'un JSON.

Supposons que j'ai un JSON contenant certaines informations, comme montré ci-dessous :

```js
jsonData: {
one: [11, 12, 13, 14, 15],
two: [21, 22, 23],
three: [31, 32]
}
```

Le JSON a un nœud racine appelé "jsonData", et celui-ci contient 3 nœuds — "one", "two", "three". Les nœuds sont également appelés clés.

Le code ci-dessous montre comment extraire des informations d'un JSON en utilisant la boucle _For In_ :

```js
var json = {
jsonData: {
one: [11, 12, 13, 14, 15],
two: [21, 22, 23],
three: [31, 32]
}
};

for (var key in json.jsonData) {
    for (var key1 in json.jsonData[key]) {
        console.log(json.jsonData[key][key1])
    }
}
```

_Explication_ : Il y a **2 boucles For In** dans le code ci-dessus — boucle externe et boucle interne.

La **boucle externe** s'exécute 3 fois et couvre les nœuds "one", "two" et "three".

La **boucle interne** couvre toutes les valeurs à l'intérieur du nœud sélectionné, c'est-à-dire les nœuds "one", "two" et "three".

Exécutez le code dans votre page web ou dans la fenêtre de la console de votre navigateur, et vous verrez toutes les valeurs des nœuds imprimées, comme dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*7SRGhCXNeuVVdwa_cOaLAw.png)
_**Boucle "For In" dans JSON**_

#### **Aller un peu plus loin dans le JSON**

Le même JSON peut être exprimé en mettant **[]** pour contenir les 3 nœuds "one", "two", "three" :

```js
jsonData: [{
one: [11, 12, 13, 14, 15]
}, {
two: [21, 22, 23]
}, {
three: [31, 32]
}]
```

Maintenant, je vais utiliser une combinaison de boucles **For & For In** pour extraire toutes les informations de ce JSON. Le code ci-dessous fait ce travail pour moi :

```js
var json = {
jsonData: [{
one: [11, 12, 13, 14, 15]
}, {
two: [21, 22, 23]
}, {
three: [31, 32]
}]
};

for (var i = 0; i < json.jsonData.length; i++) {
    for (var key in json.jsonData[i]) {
        for (var j = 0; j < json.jsonData[i][key].length; j++) {
            console.log(json.jsonData[i][key][j])
        }
    }
}
```

### **3. La boucle "While"**

La **boucle While** a une condition spécifiée. Elle vérifie la condition et exécute le bloc de code tant que la **condition est vraie**. Notez que la boucle while **n'a pas de compteur** comme la boucle for.

#### a. Parcourir un élément de tableau HTML

Supposons que j'ai un **tableau HTML** qui montre les prix de différents produits. Ce tableau HTML ressemble à l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DKlO7m_UNsS57xCPwALDkQ.png)
_**Tableau des prix sans total des produits**_

Vous pouvez voir que ce tableau ne montre pas le **prix total** de tous les produits. Donc, si vous avez besoin d'afficher le prix total, vous pouvez **parcourir tous les prix** et afficher le total dans le pied de tableau. Voici comment procéder.

Ajoutez le code HTML du tableau à votre page web :

```js
<table id="priceTable">
    <tr>
        <th>Id</th>
        <th>Nom du produit</th>
        <th>Prix du produit</th>
    </tr>
    <tr> 
        <td>1</td>
        <td>Chemises</td>
        <td>49.99</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Pantalons</td>
        <td>55.50</td>
    </tr>
    <tr> 
        <td>3</td>
        <td>Chaussettes</td>
        <td>20</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Chaussures</td>
        <td>99</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Vestes</td>
        <td>88.90</td>
    </tr>
</table>
```

Ensuite, ajoutez le CSS pour donner un design approprié à ce tableau HTML :

```css
<style>
    #priceTable {
       font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
       border-collapse: collapse;
       width: 100%;
    }

        #priceTable td, #priceTable th {
            border: 1px solid #ddd;
            padding: 8px;
        }

        #priceTable tr {
            background-color: #f2f2f2;
        }

        #priceTable th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #4CAF50;
            color: white;
        }
</style>
```

Maintenant, parcourez le tableau avec la **boucle While** et calculez la somme de tous les produits. Ajoutez donc le code JavaScript suivant à votre page web qui fait ce travail :

```js
var table = document.getElementById("priceTable");

var i = 1;
var sum = 0;
while (i < table.rows.length) {
    sum += parseFloat(table.rows[i].cells[2].innerHTML)
    i++;
}

var row = table.insertRow(i);
var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);
var cell3 = row.insertCell(2);

cell2.innerHTML = "Prix total";
cell3.innerHTML = sum;
```

_Explication_ : D'abord, j'obtiens la référence du tableau en utilisant `**var table = document.getElementById("priceTable")**`. Ensuite, j'ai ajouté 2 variables appelées "i" et "sum". La variable "i" est la variable conditionnelle de la boucle while, tandis que "sum" continuera à ajouter le prix de chaque produit.

J'ai donc exécuté la **boucle while** pour la valeur de la variable "i" de 1 à (total des lignes -1). J'ai obtenu le nombre total de lignes dans le tableau par **table.rows.length** et je l'ai ajouté à la condition de la boucle while :

```js
while (i < table.rows.length) {
  //...
}
```

_Note_ : Le tableau a 6 lignes de l'index 0 à 5, et chaque ligne a 3 colonnes de l'index 0 à 2. J'ai spécifiquement exécuté la boucle à partir de la valeur de la variable "i" de 1 et non de 0. Cela est dû au fait qu'à l'index 0 de la ligne du tableau se trouve le nom de la colonne (que je n'ai pas besoin).

À l'intérieur de la boucle while, j'ai continué à ajouter les valeurs de chaque prix de produit à la variable sum comme ceci : `**sum += parseFloat(table.rows[i].cells[2].innerHTML)**` et à la fin j'ai augmenté la valeur de "i" de 1.

Par exemple, lorsque la valeur de "i" est 1, alors `**table.rows[1]**` me donne la première ligne (premier élément "tr"). De même, `**table.rows[1].cells[2]**` donnera la valeur de la colonne de prix (élément "td" de prix) de la première ligne.

Après que la boucle soit terminée, j'ajoute une **nouvelle ligne au tableau** à la toute fin. À l'intérieur de cette ligne, j'ajoute les 3 colonnes — index 0, index 1 et index 2. Enfin, j'affiche la chaîne "total" dans la 1ère colonne et le prix total contenu dans la variable "sum" dans la **2ème colonne**.

Le code qui effectue l'ajout de cette nouvelle ligne est :

```js
var row = table.insertRow(i);
var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);
var cell3 = row.insertCell(2);

cell2.innerHTML = "Prix total";
cell3.innerHTML = sum;
```

Le `**table.insertRow(i)**` ajoutera une 6ème ligne car la valeur de la variable "i" est 6 au moment où la **boucle While** se termine.

Les colonnes (élément "td") sont ajoutées à cette nouvelle ligne par `**row.insertCell(0), row.insertCell(1), row.insertCell(2)**`.

J'affiche une valeur à l'intérieur de la colonne par :

```js
cell2.innerHTML = "Prix total";
cell3.innerHTML = sum;
```

Le code JavaScript ci-dessus créera une nouvelle ligne contenant le prix total du produit. Maintenant, le tableau ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JJruezS2_0bal7nO9xFFSw.png)
_**Tableau des prix avec le total des produits**_

#### b. Une boucle infinie

Voici la boucle infinie dans l'instruction While :

```js
var infiVal = true;

while (infiVal) {
  // votre code
}
```

Note : Les boucles infinies peuvent bloquer le navigateur, il est donc nécessaire d'exécuter la boucle à intervalles de quelques millisecondes. Vous pouvez utiliser la **méthode setInterval de JavaScript** pour exécuter une fonction donnée toutes les 1000 millisecondes. Voir le code ci-dessous :

```js
var myVar = setInterval(myTimer, 1000);

function myTimer() {
  // votre code
}
```

> Tutoriel de référence — [**Comprendre les méthodes de temporisation "setTimeout()" et "setInterval()" dans jQuery/JavaScript**](http://www.yogihosting.com/settimeout-setinterval-functions/)

### **4. La boucle "Do While"**

Dans la **boucle Do While**, la condition à vérifier est donnée à la fin, et donc la boucle s'exécute au moins une fois même si la condition n'est pas vraie. Vérifiez le code ci-dessous qui donnera un message "Hello" dans la boîte d'alerte, même si la condition est fausse dès le début (car la valeur de la variable "i" est toujours supérieure à 1).

```js
var i = 2;

do {
    alert("Hello");
    i++;
}
while (i < 1);
```

#### a. Parcourir XML

Maintenant, je vais utiliser la **boucle Do While** pour montrer comment **parcourir XML** et extraire des données. J'ai un fichier XML appelé "XMLFile1.xml" dont le contenu est :

```xml
<?xml version="1.0" encoding="utf-8" ?>
<cities>
    <city>Washington DC</city>    
    <city>Islamabad</city>
    <city>Beijing</city>
    <city>Tokyo</city>
</cities>
```

Je vais utiliser **AJAX pour lire ce fichier XML**, puis le parcourir avec la boucle Do While. Le code ci-dessous imprime tous les noms des villes (donnés dans le fichier XML) dans la fenêtre de la console.

```js
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
        myFunction(this);
    }
};
xhttp.open("GET", "XMLFile1.xml", true);
xhttp.send();

function myFunction(xml) {
    var xmlDoc = xml.responseXML;
    var cityNames = Array.from(xmlDoc.getElementsByTagName("city"));
    var i = 0;  
    
    do {
        console.log(cityNames[i].innerHTML);
        i++;
    }
    while (i < cityNames.length);
}
```

_Explication_ : J'ai créé un objet **XMLHttpRequest** pour effectuer l'appel AJAX. Lorsque le fichier XML est lu, l'événement appelé **onreadystatechange** est déclenché, voir le code ci-dessous :

```js
xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
        myFunction(this);
    }
};
```

Dans cet événement, j'appelle ma fonction personnalisée appelée **myFunction()**. Ici, je stocke le contenu XML à l'intérieur d'une variable appelée **xmlDoc** :

`var xmlDoc = xml.responseXML;`

Ensuite, j'ai converti tous les noms de villes en un **tableau** :

`var cityNames = Array.from(xmlDoc.getElementsByTagName("city"));`

Enfin, je parcours ce tableau de villes en utilisant la **boucle Do While** et j'imprime chaque nom de ville dans la fenêtre de la console :

```js
var i = 0;
do {
    console.log(cityNames[i].innerHTML);
    i++;
}
while (i < cityNames.length);
```

L'image ci-dessous illustre la sortie imprimée sur la console :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tzh2L8Ywe2ELU9GtmFznEA.png)
_**Valeurs des villes depuis XML**_

### **5. La méthode ".forEach()"**

L'édition ES6 de JavaScript a introduit une nouvelle méthode appelée `.forEach()` pour parcourir les éléments d'un tableau. Vous la trouverez très pratique lorsque vous traiterez avec des tableaux.

#### a. Parcourir un tableau avec la méthode .forEach() :

Dans cette situation, je parcours un élément de tableau avec la méthode **.forEach()** et j'imprime l'**index** et la **valeur** de chaque **élément** dans la fenêtre de la console. Voir le code ci-dessous :

```js
var names = ["jerry", "tom", "pluto", "micky", "mini"];
names.forEach(Function1);

function Function1(currentValue, index) {
    console.log("Index actuel du tableau est : " + index + " :: Valeur est : " + currentValue);
}
```

**Function1** est le nom de la fonction qui est appelée pour chaque élément du tableau. Dans mon cas, elle sera appelée 5 fois. Elle accepte 2 paramètres — "index" et "valeur" de l'élément actuel.

**Notez** que vous pouvez convertir un objet en tableau en utilisant la méthode **Array.from()** :

```js
var linksArr = Array.from(links);
```

### **_Conclusion_**

Merci d'avoir pris le temps de lire ce tutoriel. J'espère qu'il vous a appris quelque chose de nouveau sur la gestion des boucles en JavaScript. Maintenant, vous pouvez appliquer l'une de vos tactiques de boucle préférées, décrites dans ce tutoriel, dans votre projet web.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7DkA8yFAIsGLkhjpWhD_NA.jpeg)

Je publie 2 articles sur le développement web par semaine. Envisagez de me suivre et recevez une notification chaque fois que je publie un nouveau tutoriel sur Medium. Si cet article vous a été utile, veuillez cliquer sur le bouton d'applaudissements plusieurs fois pour montrer votre soutien ! _Cela mettra un sourire sur mon visage et me motivera à écrire davantage pour les lecteurs comme vous._

> J'ai également publié un autre tutoriel sur freeCodeCamp, que vous aimeriez peut-être voir aussi — [Comment créer une fonction de connexion avec Bootstrap Modal et jQuery AJAX](https://medium.freecodecamp.org/how-to-create-a-login-feature-with-bootstrap-modal-and-jquery-ajax-53dc0d281609)

Merci et bon codage !