---
title: Comment construire un convertisseur de chiffres romains et un tableau interactif
  des chiffres romains
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-04T07:16:00.000Z'
originalURL: https://freecodecamp.org/news/roman-numeral-converter-interactive-roman-numerals-chart
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99dd740569d1a4ca2223.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
seo_title: Comment construire un convertisseur de chiffres romains et un tableau interactif
  des chiffres romains
seo_desc: 'By Alexander Arobelidze

  The Roman numerals are no longer an essential part of our daily lives. But we do
  use them when designing monuments, clocks, and even for sporting events.

  What are the Roman Numerals?

  Roman numerals originated in ancient Rome a...'
---

Par Alexander Arobelidze

Les chiffres romains ne font plus partie intégrante de notre vie quotidienne. Mais nous les utilisons encore pour concevoir des monuments, des horloges, et même pour des événements sportifs.

## Qu'est-ce que les chiffres romains ?

Les chiffres romains ont été créés dans la Rome antique et sont restés la manière courante d'écrire les nombres à travers l'Europe pendant de nombreux siècles. Leur utilisation a survécu longtemps à l'Empire romain lui-même. Ils ont été progressivement remplacés par le système de numération indo-arabe que nous utilisons aujourd'hui – les chiffres de zéro à neuf.

Les chiffres romains sont représentés par des combinaisons de lettres de l'alphabet latin, qui servent de chiffres dans ce système. Mais contrairement à la base décimale, avec les symboles **0 à 9**, le système romain utilise sept lettres latines majuscules **I, V, X, L, C, D, M**.

À l'origine, il n'y avait pas de désignation par une seule lettre pour le zéro. Au lieu de cela, ils utilisaient le mot latin **Nulla**, qui signifie « aucun ». 

## Comment fonctionnent les chiffres romains ?

La représentation indo-arabe de ces lettres est la suivante : **I = 1, V = 5, X = 10, L = 50, C = 100, D = 500 et M = 1000**.

D'autres nombres sont formés en combinant ces lettres selon certaines règles : Un symbole placé **après** un autre de valeur égale ou supérieure, ajoute sa valeur. 

Par exemple, **VI = V + I = 5 + 1 = 6** ou **LX = L + X = 50 + 10 = 60**. Les notations VI et LX se lisent comme « un de plus que cinq » et « dix de plus que cinquante ». 

Un symbole placé **avant** un autre de valeur supérieure soustrait sa valeur. Par exemple, **IX = X - I = 10 - 1 = 9**, et **XC = C - X = 100 - 10 = 90**. 

Les notations IX et XC se lisent comme « un de moins que dix » et « dix de moins que cent ». 

Les nombres supérieurs à 1 000 sont formés en plaçant un trait au-dessus du symbole. Ainsi **V̅ = 5 000**, **X̅ = 10 000**, **L̅ = 50 000**, **C̅ = 100 000**, **D̅ = 500 000** et **M̅ = 1 000 000**. 

La forme dite « standard » interdit l'utilisation du même symbole plus de trois fois de suite. Mais parfois, des exceptions peuvent être vues. Par exemple, IIII pour le nombre 4, VIIII pour le nombre 9, et LXXXX pour 90.

## Un tableau interactif des chiffres romains et de leurs combinaisons

Passez la souris sur chaque symbole pour révéler son équivalent indo-arabe :

<!-- HTML utilise Flexbox. Le conteneur est composé de boutons comme éléments de base. Les boutons sont connectés à des fonctions qui se déclenchent lors des événements mouseover et mouseout. Les identifiants des boutons actuels, les nombres arabes et romains servent d'arguments pour les fonctions d'écouteurs d'événements. -->
<div class='flex-container'>
    
	<div class='row1'>
    	<button class='item' id='1' onmouseover='handleMouseOver("1")' onmouseout='handleMouseOut("1", "I")'>I</button>
        <button class='item' id='2' onmouseover='handleMouseOver("2")' onmouseout='handleMouseOut("2", "II")'>II</button>
        <button class='item' id='3' onmouseover='handleMouseOver("3")' onmouseout='handleMouseOut("3", "III")'>III</button>
        <button class='item' id='4' onmouseover='handleMouseOver("4")' onmouseout='handleMouseOut("4", "IV")'>IV</button>
        <button class='item' id='5' onmouseover='handleMouseOver("5")' onmouseout='handleMouseOut("5", "V")'>V</button>
        <button class='item' id='6' onmouseover='handleMouseOver("6")' onmouseout='handleMouseOut("6", "VI")'>VI</button>
        <button class='item' id='7' onmouseover='handleMouseOver("7")' onmouseout='handleMouseOut("7", "VII")'>VII</button>
        <button class='item' id='8' onmouseover='handleMouseOver("8")' onmouseout='handleMouseOut("8", "VIII")'>VIII</button>
        <button class='item' id='9' onmouseover='handleMouseOver("9")' onmouseout='handleMouseOut("9", "IX")'>IX</button>
    </div>
    <div class='row2'>
    	<button class='item' id='10' onmouseover='handleMouseOver("10")' onmouseout='handleMouseOut("10", "X")'>X</button>
        <button class='item' id='20' onmouseover='handleMouseOver("20")' onmouseout='handleMouseOut("20", "XX")'>XX</button>
        <button class='item' id='30' onmouseover='handleMouseOver("30")' onmouseout='handleMouseOut("30", "XXX")'>XXX</button>
        <button class='item' id='40' onmouseover='handleMouseOver("40")' onmouseout='handleMouseOut("40", "XL")'>XL</button>
        <button class='item' id='50' onmouseover='handleMouseOver("50")' onmouseout='handleMouseOut("50", "L")'>L</button>
        <button class='item' id='60' onmouseover='handleMouseOver("60")' onmouseout='handleMouseOut("60", "LX")'>LX</button>
        <button class='item' id='70' onmouseover='handleMouseOver("70")' onmouseout='handleMouseOut("70", "LXX")'>LXX</button>
        <button class='item' id='80' onmouseover='handleMouseOver("80")' onmouseout='handleMouseOut("80", "LXXX")'>LXXX</button>
        <button class='item' id='90' onmouseover='handleMouseOver("90")' onmouseout='handleMouseOut("90", "XC")'>XC</button>
    </div>
    <div class='row3'>
    	<button class='item' id='100' onmouseover='handleMouseOver("100")' onmouseout='handleMouseOut("100", "C")'>C</button>
        <button class='item' id='200' onmouseover='handleMouseOver("200")' onmouseout='handleMouseOut("200", "CC")'>CC</button>
        <button class='item' id='300' onmouseover='handleMouseOver("300")' onmouseout='handleMouseOut("300", "CCC")'>CCC</button>
        <button class='item' id='400' onmouseover='handleMouseOver("400")' onmouseout='handleMouseOut("400", "CD")'>CD</button>
        <button class='item' id='500' onmouseover='handleMouseOver("500")' onmouseout='handleMouseOut("500", "D")'>D</button>
        <button class='item' id='600' onmouseover='handleMouseOver("600")' onmouseout='handleMouseOut("600", "DC")'>DC</button>
        <button class='item' id='700' onmouseover='handleMouseOver("700")' onmouseout='handleMouseOut("700", "DCC")'>DCC</button>
        <button class='item' id='800' onmouseover='handleMouseOver("800")' onmouseout='handleMouseOut("800", "DCCC")'>DCCC</button>
        <button class='item' id='900' onmouseover='handleMouseOver("900")' onmouseout='handleMouseOut("900", "CM")'>CM</button>
    </div>
    <div class='row4'>
    	<button class='item special' id='1000' onmouseover='handleMouseOver("1000")' onmouseout='handleMouseOut("1000", "M")'>M</button>
        <button class='item special' id='5000' onmouseover='handleMouseOver("5000")' onmouseout='handleMouseOut("5000", "V&#773;")'>V&#773;</button>
        <button class='item special' id='10000' onmouseover='handleMouseOver("10000")' onmouseout='handleMouseOut("10000", "X&#773;")'>X&#773;</button>
        <button class='item special' id='50000' onmouseover='handleMouseOver("50000")' onmouseout='handleMouseOut("50000", "L&#773;")'>L&#773;</button>
        <button class='item special' id='100000' onmouseover='handleMouseOver("100000")' onmouseout='handleMouseOut("100000", "C&#773;")'>C&#773;</button>
        <button class='item special' id='500000' onmouseover='handleMouseOver("500000")' onmouseout='handleMouseOut("500000", "D&#773;")'>D&#773;</button>
        <button class='item special' id='1000000' onmouseover='handleMouseOver("1000000")' onmouseout='handleMouseOut("1000000", "M&#773;")'>M&#773;</button>
    </div>
</div>


<!-- CSS  -->

<style>
    .flex-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;    
    margin: 0 auto; 
    align-items: center;
    justify-content: center;   
   }
    /* Mobile phones */
@media screen and (max-width: 767px){
    .flex-container {
       transform: scale(0.6);
    }
}
/* Tablets and iPads */
@media screen and (min-width: 768px) and (max-width: 1023px){
    .flex-container {
        transform: scale(0.8);
    }
}
    .row1, .row2, .row3 {
    display: flex;
    flex-direction: row;    
    align-items: center;
    justify-content: space-between;    
    }
    .row4 {
    display: flex;
    flex-direction: row nowrap;  
    align-items: center;
    justify-content: space-evenly;     
    }
    .item {
    margin: 0.2rem 0.2rem;
    width: 9rem;
    height: 9rem;  
    background-color: #3F51B5; 
    color: white;
    font-weight: 600;  
    border-radius: 0.2rem;
    box-shadow: 0 0 1rem 0.25rem; 
    transition-duration: 0.2s;
   }
    .special {
    margin: 0.2rem 0.3rem;    
    width: 11.5rem;
    height: 9rem;    
    }

</style>

<!-- JavaScript se compose de deux fonctions. L'une est appelée lors de l'événement mouseover, l'autre lors de l'événement mouseout. Les arguments qu'elles prennent déterminent quel nœud est actuellement actif et changent son apparence/contenu en conséquence. -->
<script>
 
function handleMouseOver(arabic) {
    let currentButton = document.getElementById(arabic)
 	currentButton.style.transform = 'scale(1.3)'
    currentButton.style.zIndex = '9'
    currentButton.textContent = arabic 
} 
 
function handleMouseOut(id, roman) {
    let currentButton = document.getElementById(id) 
    currentButton.style.transform = 'scale(1)'
    currentButton.style.zIndex = '0'
    currentButton.textContent = roman 
 }   
</script>

J'ai écrit le code pour ce tableau interactif de chiffres romains pour l'intégrer ici sur freeCodeCamp News.

Étant donné que la fonction d'intégration HTML n'est pas un éditeur de code à part entière, le code donné n'est pas structuré et présenté sous forme de fichiers HTML, CSS et JavaScript séparés. Il est plutôt écrit sous forme de fichier HTML unique avec des éléments `<style>` et `<script>` ajoutés pour le style et la fonctionnalité.

Voici [le dépôt de code complet pour mon tableau interactif de chiffres romains](https://github.com/sandroarobeli/RomanNumeralChart.git). 

## Convertisseur de chiffres romains

Entrez un entier non négatif entre 0 et 5 000. Ensuite, cliquez sur Convertir pour révéler l'équivalent en chiffres romains. 

<!-- Éléments HTML 
L'interface utilisateur se compose d'un élément d'entrée de type 'number' qui garantit que seuls les caractères numériques et le point décimal peuvent être saisis. La gestion des points décimaux est 
gérée par la logique JavaScript ci-dessous. De plus, un élément de bouton 'convertir' sur lequel on clique déclenche la conversion des chiffres arabes en chiffres romains et un autre élément de bouton qui affiche le résultat de la conversion. Dans le cas où l'on se demande pourquoi un élément de bouton affiche le résultat, la réponse a à voir avec la gestion du style étant donné la fonctionnalité assez limitée de la plateforme.  
-->

<div  
    id='converter' 
    style='box-sizing: border-box; 
           width: 90%; 
           margin: 0 auto;'>
   <label 
         for='arabicNumeral' 
         style='display:block; 
                text-align: center; 
                font-weight: 600; 
                color: #3F51B5;'>Arabe vers Romain
      <input 
            type='number' 
            name='arabicNumeral'  
            id='arabicNumeral' 
            min='0' max='5000' step='1' 
            placeholder="Entrez un entier entre 0 et 5000" 
            style='padding: 10px; 
                   margin: 0 auto; 
                   border: 2px solid #eee; 
                   box-shadow:0 0 15px 4px rgba(0,0,0,0.06); 
                   border-radius:10px; 
                   width:100%; 
                   font-size: inherit;' /> 				
   </label> <hr/>
   <button 
          type='button' 
          id='convert'
          onclick='convertToRoman()'           
          style='padding:10px; 
                 border:none;
                 margin: 0 auto;                                                                background-color:#3F51B5;
                 color:#fff;
                 font-weight:600;
                 border-radius:5px;
                 width:100%;'>Convertir
   </button>
   <button 
          type='button' 
          id='display' 
          style='padding:10px;
                 border:none;
                 margin: 0 auto;                                                                background-color:#fff;
                 color:#3F51B5;
                 font-weight:600;
                 font-size: 3rem;       
                 border-radius:5px;
                 width:100%; '>
   </button>
 </div>   
 
<script>
 
  /* Le bloc suivant est structuré de cette manière principalement en raison des limitations de la plateforme. Le convertisseur couvre actuellement les nombres entre 0 et 5000, mais il peut être modifié pour couvrir les nombres négatifs ainsi que les nombres au-delà de 5000. La plage choisie couvre largement le but du convertisseur en tant qu'outil interactif dans l'article. 
  */   	
   
 
 const inputField = document.querySelector('input');
 const outputField = document.getElementById('display');
 const convertButton = document.getElementById('convert');
 

  
 
function convertToRoman() {
 
 let arabic = document.getElementById('arabicNumeral').value;
 let roman = '';
    
 const arabicArray = [5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
 const romanArray = ['V&#773;', 'MV&#773;','M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

  
if (/^(0|[1-9]\d*)$/.test(arabic)) {
  if (arabic == 0) {  
    outputField.innerHTML = 'Nulla'
  } else if (arabic != 0) {
   for (let i = 0; i < arabicArray.length; i++) {
    while (arabicArray[i] <= arabic) {
      roman += romanArray[i]
      arabic -= arabicArray[i]
    }
 }
   outputField.innerHTML = roman
  }
} else {
   outputField.innerHTML = "Veuillez entrer uniquement des entiers non négatifs. Pas de points décimaux."
}
 
 }     
 
</script>

Il n'y a pas de limitation programmatique au nombre 5 000 ou au-delà. L'algorithme qui régit la conversion fonctionnerait de la même manière. 

L'espace requis pour afficher les équivalents en chiffres romains des grands nombres devient de plus en plus grand sans grand bénéfice supplémentaire de révéler quelque chose de nouveau. 

Le code lui-même se compose d'une partie HTML décrivant le contenu avec des styles en ligne pour faciliter l'interaction et du JavaScript ajouté pour la fonctionnalité.

Il y a un élément d'entrée de type "number" pour limiter les données d'entrée aux valeurs numériques et deux boutons. Le bouton "Convertir" est connecté à la fonction qui effectue la conversion, et le bouton "Afficher" affiche l'équivalent en chiffres romains. 

Pourquoi afficher via un élément de bouton ? Le style fonctionnait bien lorsqu'il était appliqué aux deux boutons ensemble. Et compte tenu de la fonctionnalité limitée de l'intégration, cela semblait être un gain de temps. 

Pour plus de clarté, ces éléments sont assignés à des variables :

```js
const inputField = document.querySelector('input'); // élément d'entrée
const convertButton = document.getElementById('convert'); // bouton de conversion
const outputField = document.getElementById('display'); // élément de sortie
```

La fonction `convertToRoman()` contient la logique et rend le résultat :

```js
function convertToRoman() {
  let arabic = document.getElementById('arabicNumeral').value; // valeur d'entrée
  let roman = '';  // variable qui contiendra le résultat
}
```

La valeur numérique de l'élément d'entrée est enregistrée dans une variable appelée "**arabic**" pour un test ultérieur. La variable nommée "**roman**" contiendra la chaîne représentant l'équivalent romain de l'entrée arabe.

Ensuite, il y a deux tableaux de longueurs égales, l'un contenant les chiffres arabes et l'autre contenant leurs équivalents romains. Les deux sont en ordre décroissant pour simplifier la soustraction :

```js
// ordre décroissant simplifie la soustraction lors de la boucle
const arabicArray = [5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] 
const romanArray = ['V&#773;', 'MV&#773;','M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'] 
```

Les tables Unicode aident à former des symboles supérieurs à 1 000. 

Enfin, voici la logique qui teste le nombre saisi et le convertit.

```js
if (/^(0|[1-9]\d*)$/.test(arabic)) {
  // Expression régulière teste
  if (arabic == 0) {
    // pour les points décimaux et les négatifs
    outputField.innerHTML = "Nulla"; // signes
  } else if (arabic != 0) {
    for (let i = 0; i < arabicArray.length; i++) {
      while (arabicArray[i] <= arabic) {
        roman += romanArray[i];
        arabic -= arabicArray[i];
      }
    }
    outputField.innerHTML = roman;
  }
} else {
  outputField.innerHTML =
    "Veuillez entrer uniquement des entiers non négatifs. Pas de points décimaux.";
}
```

Le premier test vérifie la présence de points décimaux et de signes négatifs. Si trouvés, le message demande de "saisir uniquement des entiers non négatifs".

Le test suivant vérifie si le nombre saisi est égal à zéro. Dans ce cas, la chaîne "Nulla" est affichée. 

Sinon, les boucles continuent de concaténer les chaînes romaines tout en soustrayant les nombres arabes jusqu'à ce que ces derniers satisfassent la condition de la boucle while. Ensuite, il affiche l'équivalent romain de la saisie de l'utilisateur.

Tout comme pour le tableau interactif, le code pour le convertisseur de chiffres romains est prêt à être copié et intégré dans n'importe quel article. Voici [le dépôt de code complet](https://github.com/sandroarobeli/RomanNumeralConverter.git).