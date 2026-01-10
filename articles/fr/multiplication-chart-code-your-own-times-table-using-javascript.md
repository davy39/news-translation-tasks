---
title: Table de multiplication - Créez votre propre table de multiplication en utilisant
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-04T22:41:59.000Z'
originalURL: https://freecodecamp.org/news/multiplication-chart-code-your-own-times-table-using-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9966740569d1a4ca1f7a.jpg
tags:
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: Table de multiplication - Créez votre propre table de multiplication en
  utilisant JavaScript
seo_desc: "By Alexander Arobelidze\nLearning your times tables is an essential skill\
  \ and it's a basic part of any math education. A multiplication chart is a handy\
  \ tool that turns tedious memorization into a fun, logical exercise. \nThe chart\
  \ shows the products o..."
---

Par Alexander Arobelidze

Apprendre ses tables de multiplication est une compétence essentielle et c'est une partie fondamentale de toute éducation mathématique. Une **table de multiplication** est un outil pratique qui transforme la mémorisation fastidieuse en un exercice logique et amusant. 

La table montre les produits de deux nombres. Habituellement, un ensemble de nombres (1-9) est écrit dans la colonne de gauche, et l'autre ensemble sur la ligne du haut. Cela forme deux côtés d'un carré visuel. Leurs produits remplissent le reste de ce carré. Ressemblant à ceci :

<div class='flex-tableDemo'>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'></div>
      <div class='itemDemo headerDemo'>1</div>
      <div class='itemDemo headerDemo'>2</div>
      <div class='itemDemo headerDemo'>3</div>
      <div class='itemDemo headerDemo'>4</div>
      <div class='itemDemo headerDemo'>5</div>
      <div class='itemDemo headerDemo'>6</div>
      <div class='itemDemo headerDemo'>7</div>
      <div class='itemDemo headerDemo'>8</div>
      <div class='itemDemo headerDemo'>9</div>
   </div>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'>1</div>
      <div class='itemDemo'>1</div>
      <div class='itemDemo'>2</div>
      <div class='itemDemo'>3</div>
      <div class='itemDemo'>4</div>
      <div class='itemDemo'>5</div>
      <div class='itemDemo'>6</div>
      <div class='itemDemo'>7</div>
      <div class='itemDemo'>8</div>
      <div class='itemDemo'>9</div>
   </div>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'>2</div>
      <div class='itemDemo'>2</div>
      <div class='itemDemo'>4</div>
      <div class='itemDemo'>6</div>
      <div class='itemDemo'>8</div>
      <div class='itemDemo'>10</div>
      <div class='itemDemo'>12</div>
      <div class='itemDemo'>14</div>
      <div class='itemDemo'>16</div>
      <div class='itemDemo'>18</div>
   </div>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'>3</div>
      <div class='itemDemo'>3</div>
      <div class='itemDemo'>6</div>
      <div class='itemDemo'>9</div>
      <div class='itemDemo'>12</div>
      <div class='itemDemo'>15</div>
      <div class='itemDemo'>18</div>
      <div class='itemDemo'>21</div>
      <div class='itemDemo'>24</div>
      <div class='itemDemo'>27</div>
   </div>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'>4</div>
      <div class='itemDemo'>4</div>
      <div class='itemDemo'>8</div>
      <div class='itemDemo'>12</div>
      <div class='itemDemo'>16</div>
      <div class='itemDemo'>20</div>
      <div class='itemDemo'>24</div>
      <div class='itemDemo'>28</div>
      <div class='itemDemo'>32</div>
      <div class='itemDemo'>36</div>
   </div>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'>5</div>
      <div class='itemDemo'>5</div>
      <div class='itemDemo'>10</div>
      <div class='itemDemo'>15</div>
      <div class='itemDemo'>20</div>
      <div class='itemDemo'>25</div>
      <div class='itemDemo'>30</div>
      <div class='itemDemo'>35</div>
      <div class='itemDemo'>40</div>
      <div class='itemDemo'>45</div>
   </div>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'>6</div>
      <div class='itemDemo'>6</div>
      <div class='itemDemo'>12</div>
      <div class='itemDemo'>18</div>
      <div class='itemDemo'>24</div>
      <div class='itemDemo'>30</div>
      <div class='itemDemo'>36</div>
      <div class='itemDemo'>42</div>
      <div class='itemDemo'>48</div>
      <div class='itemDemo'>54</div>
   </div>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'>7</div>
      <div class='itemDemo'>7</div>
      <div class='itemDemo'>14</div>
      <div class='itemDemo'>21</div>
      <div class='itemDemo'>28</div>
      <div class='itemDemo'>35</div>
      <div class='itemDemo'>42</div>
      <div class='itemDemo'>49</div>
      <div class='itemDemo'>56</div>
      <div class='itemDemo'>63</div>
   </div>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'>8</div>
      <div class='itemDemo'>8</div>
      <div class='itemDemo'>16</div>
      <div class='itemDemo'>24</div>
      <div class='itemDemo'>32</div>
      <div class='itemDemo'>40</div>
      <div class='itemDemo'>48</div>
      <div class='itemDemo'>56</div>
      <div class='itemDemo'>64</div>
      <div class='itemDemo'>72</div>
   </div>
   <div class='table-rowDemo'>
      <div class='itemDemo headerDemo'>9</div>
      <div class='itemDemo'>9</div>
      <div class='itemDemo'>18</div>
      <div class='itemDemo'>27</div>
      <div class='itemDemo'>36</div>
      <div class='itemDemo'>45</div>
      <div class='itemDemo'>54</div>
      <div class='itemDemo'>63</div>
      <div class='itemDemo'>72</div>
      <div class='itemDemo'>81</div>
   </div>
</div>
<style>
    .flex-tableDemo {
      
       display: flex;
       flex-direction: column;
       width: 60%;
       height: 60%;    
       margin: auto; 
       align-items: center;
       justify-content: center;   
    }
	/* Mobile phones */
    @media screen and (max-width: 767px){
       .flex-tableDemo {
          transform: scale(0.6);
       }
    }
    /* Tablets and iPads */
    @media screen and (min-width: 768px) and (max-width: 1023px){
       .flex-tableDemo {
          transform: scale(0.8);
       }
    }
    .table-rowDemo {
       display: flex;
       flex-direction: row;    
       align-items: center;
       justify-content: space-between;    
    }
    .itemDemo {
       margin: 0.06rem 0.06rem;
       width: 4rem;
       height: 4rem;  
       background-color: #3F51B5; 
       color: white;
       font-weight: 500;  
       border-radius: 0.12rem;
       box-shadow: 0 0 0.6rem 0.15rem; 
       text-align: center; 
       line-height: 3.6rem; 
   }
    .headerDemo {
    	background-color: #5698a9;
   }
</style>


La nature visuelle d'un tel outil améliore l'apprentissage en utilisant le concept des aires. **2 x 3** est égal au nombre **6** ainsi qu'à l'aire d'un rectangle avec un côté de **2** et un autre de **3**. 

Il existe d'innombrables façons de présenter le style et la fonctionnalité des tables de multiplication. Chaque auteur ajoutera sa touche spéciale. Dans cet article, je vais partager une façon de concevoir et d'écrire une telle table.        

Il y a un détail important que je dois mentionner avant de passer à la description de la table. Les blocs de code intégrés dans cet article peuvent ne pas être liés les uns aux autres de quelque manière que ce soit. 

Cependant, en coulisses, ils sont placés à l'intérieur d'un seul élément `<body>` par article. Par conséquent, assurez-vous d'utiliser des attributs **id** et **class** qui sont **uniques** pour chaque bloc. Sinon, une classe ou un id avec le même nom dans deux blocs ou plus peut interférer et affecter négativement le style et la fonctionnalité. 

## Comment construire une table de multiplication

La partie HTML est une version modifiée d'un [Tableau des chiffres romains](https://www.freecodecamp.org/news/roman-numeral-converter-interactive-roman-numerals-chart/). Le bloc de construction de base est un bouton. Vous pouvez également utiliser un **div** général, mais j'ai trouvé que le bouton était plus réactif. 

Les boutons sont d'abord placés dans des lignes, qui à leur tour sont placées dans le conteneur flex.

<pre>
	<code>
&lt;div class='flex-table'&gt; 
	&lt;h2 class='table-title'&gt;Table de multiplication&lt;/h2&gt; 
    	&lt;div class='table-row'&gt; 
    		&lt;button class='item header'&gt;1&lt;/button&gt; 
		&lt;button class='item core' onmouseover='onePlay()'&gt;1&lt;/button&gt; 
        	&lt;button class='item core' onmouseover='twoPlay()'&gt;2&lt;/button&gt; 
        	&lt;button class='item core' onmouseover='threePlay()'&gt;3&lt;/button&gt; 
		.......................................................... 
              	..........................................................
    	&lt;/div&gt;
    	 &lt;div class='table-row'&gt; 				       
                ..........................................................
                ..........................................................
        &lt;/div&gt;
                ............................................................. 
     &lt;div&gt;
	</code>
</pre>    

L'architecture ou l'élément utilisé n'a pas besoin d'être unique, et vous pouvez ajouter votre propre touche originale. J'ai appliqué un style et des requêtes média pour permettre une visualisation confortable sur divers appareils.

<pre>
	<code>
    	/* Mobile phones */
    @media screen and (max-width: 767px){
       .flex-table {
          transform: scale(0.60);
       }
    }
    /* Tablets and iPads */
    @media screen and (min-width: 768px) and (max-width: 1023px){
       .flex-table {
          transform: scale(0.8);
       }
    }
    </code>
</pre>

Les effets visuels sont obtenus grâce au CSS. J'ai décidé d'introduire des éléments audio en utilisant JavaScript. J'ai été ravi de découvrir que cet éditeur le supportait. 

Chaque bouton représentant un résultat de multiplication est connecté à une fonction. Une fonction retourne un élément audio qui joue un fichier sonore unique à cet élément. Un événement de clic sert de déclencheur, appelant cette fonction.

Les littéraux de gabarit ne sont pas supportés ici. Ainsi, chaque appel de fonction a dû être câblé en dur dans les éléments et défini individuellement.

<pre>
	<code>
   &lt;script&gt;
  
function onePlay() {
  const one = 
  new Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/1.wav')
  one.currentTime = 0
  one.play()
}
function twoPlay() {
  const two = 
  new Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/2.wav')
  two.currentTime = 0
  two.play()
}
   ...............................................................
   ................................................................
   
   &lt;/script&gt;
    </code>
</pre>

Un grand merci aux spécialistes qui ont créé cette bibliothèque sonore et la maintiennent. Le code complet peut être trouvé en tant que dépôt Github en [cliquant ici](https://github.com/sandroarobeli/MultiplicationChart/blob/master/MultiplicationChart.txt).

<!--   HTML utilise Flexbox. Le conteneur est composé de boutons en tant qu'éléments de base. Les boutons sont connectés à des fonctions qui se déclenchent avec des événements de clic.   -->


<div class='flex-table'>
   <h2 class='table-title'>Table de multiplication. Survolez et cliquez</h2>
   <div class='table-row'>
      <button class='item header'></button>
      <button class='item header'>1</button>
      <button class='item header'>2</button>
      <button class='item header'>3</button>
      <button class='item header'>4</button>
      <button class='item header'>5</button>
      <button class='item header'>6</button>
      <button class='item header'>7</button>
      <button class='item header'>8</button>
      <button class='item header'>9</button>
   </div>
   <div class='table-row'>
      <button class='item header'>1</button>
      <button class='item core' onclick='onePlay()'>1</button>
      <button class='item core' onclick='twoPlay()'>2</button>
      <button class='item core' onclick='threePlay()'>3</button>
      <button class='item core' onclick='fourPlay()'>4</button>
      <button class='item core' onclick='fivePlay()'>5</button>
      <button class='item core' onclick='sixPlay()'>6</button>
      <button class='item core' onclick='sevenPlay()'>7</button>
      <button class='item core' onclick='eightPlay()'>8</button>
      <button class='item core' onclick='ninePlay()'>9</button>
    </div>
   	<div class='table-row'>
      <button class='item header'>2</button>
      <button class='item core' onclick='twoPlay()'>2</button>
      <button class='item core' onclick='fourPlay()'>4</button>
      <button class='item core' onclick='sixPlay()'>6</button>
      <button class='item core' onclick='eightPlay()'>8</button>
      <button class='item core' onclick='tenPlay()'>10</button>
      <button class='item core' onclick='twelvePlay()'>12</button>
      <button class='item core' onclick='fourteenPlay()'>14</button>
      <button class='item core' onclick='sixteenPlay()'>16</button>
      <button class='item core' onclick='eighteenPlay()'>18</button>
    </div>
    <div class='table-row'>
      <button class='item header'>3</button>
      <button class='item core' onclick='threePlay()'>3</button>
      <button class='item core' onclick='sixPlay()'>6</button>
      <button class='item core' onclick='ninePlay()'>9</button>
      <button class='item core' onclick='twelvePlay()'>12</button>
      <button class='item core' onclick='fifteenPlay()'>15</button>
      <button class='item core' onclick='eighteenPlay()'>18</button>
      <button class='item core' onclick='twentyonePlay()'>21</button>
      <button class='item core' onclick='twentyfourPlay()'>24</button>
      <button class='item core' onclick='twentysevenPlay()'>27</button>
    </div>
    <div class='table-row'>
      <button class='item header'>4</button>
      <button class='item core' onclick='fourPlay()'>4</button>
      <button class='item core' onclick='eightPlay()'>8</button>
      <button class='item core' onclick='twelvePlay()'>12</button>
      <button class='item core' onclick='sixteenPlay()'>16</button>
      <button class='item core' onclick='twentyPlay()'>20</button>
      <button class='item core' onclick='twentyfourPlay()'>24</button>
      <button class='item core' onclick='twentyeightPlay()'>28</button>
      <button class='item core' onclick='thirtytwoPlay()'>32</button>
      <button class='item core' onclick='thirtysixPlay()'>36</button>
    </div>
    <div class='table-row'>
      <button class='item header'>5</button>
      <button class='item core' onclick='fivePlay()'>5</button>
      <button class='item core' onclick='tenPlay()'>10</button>
      <button class='item core' onclick='fifteenPlay()'>15</button>
      <button class='item core' onclick='twentyPlay()'>20</button>
      <button class='item core' onclick='twentyfivePlay()'>25</button>
      <button class='item core' onclick='thirtyPlay()'>30</button>
      <button class='item core' onclick='thirtyfivePlay()'>35</button>
      <button class='item core' onclick='fourtyPlay()'>40</button>
      <button class='item core' onclick='fourtyfivePlay()'>45</button>
    </div>
    <div class='table-row'>
      <button class='item header'>6</button>
      <button class='item core' onclick='sixPlay()'>6</button>
      <button class='item core' onclick='twelvePlay()'>12</button>
      <button class='item core' onclick='eighteenPlay()'>18</button>
      <button class='item core' onclick='twentyfourPlay()'>24</button>
      <button class='item core' onclick='thirtyPlay()'>30</button>
      <button class='item core' onclick='thirtysixPlay()'>36</button>
      <button class='item core' onclick='fourtytwoPlay()'>42</button>
      <button class='item core' onclick='fourtyeightPlay()'>48</button>
      <button class='item core' onclick='fiftyfourPlay()'>54</button>
    </div>
    <div class='table-row'>
      <button class='item header'>7</button>
      <button class='item core' onclick='sevenPlay()'>7</button>
      <button class='item core' onclick='fourteenPlay()'>14</button>
      <button class='item core' onclick='twentyonePlay()'>21</button>
      <button class='item core' onclick='twentyeightPlay()'>28</button>
      <button class='item core' onclick='thirtyfivePlay()'>35</button>
      <button class='item core' onclick='fourtytwoPlay()'>42</button>
      <button class='item core' onclick='fourtyninePlay()'>49</button>
      <button class='item core' onclick='fiftysixPlay()'>56</button>
      <button class='item core' onclick='sixtythreePlay()'>63</button>
    </div>
    <div class='table-row'>
      <button class='item header'>8</button>
      <button class='item core' onclick='eightPlay()'>8</button>
      <button class='item core' onclick='sixteenPlay()'>16</button>
      <button class='item core' onclick='twentyfourPlay()'>24</button>
      <button class='item core' onclick='thirtytwoPlay()'>32</button>
      <button class='item core' onclick='fourtyPlay()'>40</button>
      <button class='item core' onclick='fourtyeightPlay()'>48</button>
      <button class='item core' onclick='fiftysixPlay()'>56</button>
      <button class='item core' onclick='sixtyfourPlay()'>64</button>
      <button class='item core' onclick='seventytwoPlay()'>72</button>
    </div>
    <div class='table-row'>
      <button class='item header'>9</button>
      <button class='item core' onclick='ninePlay()'>9</button>
      <button class='item core' onclick='eighteenPlay()'>18</button>
      <button class='item core' onclick='twentysevenPlay()'>27</button>
      <button class='item core' onclick='thirtysixPlay()'>36</button>
      <button class='item core' onclick='fourtyfivePlay()'>45</button>
      <button class='item core' onclick='fiftyfourPlay()'>54</button>
      <button class='item core' onclick='sixtythreePlay()'>63</button>
      <button class='item core' onclick='seventytwoPlay()'>72</button>
      <button class='item core' onclick='eightyonePlay()'>81</button>
    </div>
</div>


<!-- CSS  -->
<!-- media accomodates two additional viewport sizes -->
<style>
    
    .flex-table {
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
       .flex-table {
          transform: scale(0.60);
       }
    }
    /* Tablets and iPads */
    @media screen and (min-width: 768px) and (max-width: 1023px){
       .flex-table {
          transform: scale(0.8);
       }
    }
    .table-title {
    	color: #3F51B5;
        font-style: italic;
        text-align: center;
    }
    
    .table-row {
       display: flex;
       flex-direction: row;    
       align-items: center;
       justify-content: space-between;    
    }
    
    .item {
       margin: 0.1rem 0.1rem;
       width: 6rem;
       height: 6rem;  
       background-color: #3F51B5; 
       color: white;
       font-weight: 600;  
       border-radius: 0.2rem;
       box-shadow: 0 0 1rem 0.25rem; 
       transition-duration: 0.2s;
   }
    .header {
    	background-color: #5698a9;
       
    }
    
    .core:hover { 
        transform: scale(1.3);
        z-index: 9;
    }

</style>

<!-- JavaScript consists of functions creating audio objects representing each number in the table. Clicking on a button triggers play method vocalizing its numeric value-->

<script>
    // 1 
  function onePlay() {
   	const one = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/1.wav')
    one.currentTime = 0
    one.play()
   }
  function twoPlay() {
   	const two = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/2.wav')
    two.currentTime = 0
    two.play()
   } 
  function threePlay() {
   	const three = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/3.wav')
    three.currentTime = 0
    three.play()
   }
  function fourPlay() {
   	const four = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/4.wav')
    four.currentTime = 0
    four.play()
   }  
  function fivePlay() {
   	const five = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/5.wav')
    five.currentTime = 0
    five.play()
   }  
    function sixPlay() {
   	const six = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/6.wav')
    six.currentTime = 0
    six.play()
   }  
    function sevenPlay() {
   	const seven = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/7.wav')
    seven.currentTime = 0
    seven.play()
   }  
    function eightPlay() {
   	const eight = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/8.wav')
    eight.currentTime = 0
    eight.play()
   }  
    function ninePlay() {
   	const nine = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/9.wav')
    nine.currentTime = 0
    nine.play()
   }  
  // 2 
 function tenPlay() {
   	const ten = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/10.wav')
    ten.currentTime = 0
    ten.play()
   }  
 function twelvePlay() {
   	const twelve = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/12.wav')
    twelve.currentTime = 0
    twelve.play()
   }  
 function fourteenPlay() {
   	const fourteen = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/14.wav')
    fourteen.currentTime = 0
    fourteen.play()
   }  
 function sixteenPlay() {
   	const sixteen = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/16.wav')
    sixteen.currentTime = 0
    sixteen.play()
   }  
  function eighteenPlay() {
   	const eighteen = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/18.wav')
    eighteen.currentTime = 0
    eighteen.play()
   }    
 // 3
function fifteenPlay() {
   	const fifteen = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/15.wav')
    fifteen.currentTime = 0
    fifteen.play()
   }  
function twentyonePlay() {
   	const twentyone = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/21.wav')
    twentyone.currentTime = 0
    twentyone.play()
   }  
 function twentyfourPlay() {
   	const twentyfour = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/24.wav')
    twentyfour.currentTime = 0
    twentyfour.play()
   }  
 function twentysevenPlay() {
   	const twentyseven = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/27.wav')
    twentyseven.currentTime = 0
    twentyseven.play()
   }  
 // 4
 function twentyPlay() {
   	const twenty = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/20.wav')
    twenty.currentTime = 0
    twenty.play()
   }  
 function twentyeightPlay() {
   	const twentyeight = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/28.wav')
    twentyeight.currentTime = 0
    twentyeight.play()
   }  
 function thirtytwoPlay() {
   	const thirtytwo = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/32.wav')
    thirtytwo.currentTime = 0
    thirtytwo.play()
   }  
  function thirtysixPlay() {
   	const thirtysix = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/36.wav')
    thirtysix.currentTime = 0
    thirtysix.play()
   }  
 // 5
 function twentyfivePlay() {
   	const twentyfive = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/25.wav')
    twentyfive.currentTime = 0
    twentyfive.play()
   }  
 function thirtyPlay() {
   	const thirty = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/30.wav')
    thirty.currentTime = 0
    thirty.play()
   }  
  function thirtyfivePlay() {
   	const thirtyfive = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/35.wav')
    thirtyfive.currentTime = 0
    thirtyfive.play()
   }  
  function fourtyPlay() {
   	const fourty = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/40.wav')
    fourty.currentTime = 0
    fourty.play()
   }  
  function fourtyfivePlay() {
   	const fourtyfive = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/45.wav')
    fourtyfive.currentTime = 0
    fourtyfive.play()
   }    
 // 6
 function fourtytwoPlay() {
   	const fourtytwo = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/42.wav')
    fourtytwo.currentTime = 0
    fourtytwo.play()
   }  
 function fourtyeightPlay() {
   	const fourtyeight = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/48.wav')
    fourtyeight.currentTime = 0
    fourtyeight.play()
   }  
  function fiftyfourPlay() {
   	const fiftyfour = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/54.wav')
    fiftyfour.currentTime = 0
    fiftyfour.play()
   }    
 // 7
 function fourtyninePlay() {
   	const fourtynine = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/49.wav')
    fourtynine.currentTime = 0
    fourtynine.play()
   }  
 function fiftysixPlay() {
   	const fiftysix = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/56.wav')
    fiftysix.currentTime = 0
    fiftysix.play()
   }  
  function sixtythreePlay() {
   	const sixtythree = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/63.wav')
    sixtythree.currentTime = 0
    sixtythree.play()
   }    
 // 8
 function sixtyfourPlay() {
   	const sixtyfour = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/64.wav')
    sixtyfour.currentTime = 0
    sixtyfour.play()
   }   
  function seventytwoPlay() {
   	const seventytwo = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/72.wav')
    seventytwo.currentTime = 0
    seventytwo.play()
   }   
 // 9
  function eightyonePlay() {
   	const eightyone = new 			Audio('https://evolution.voxeo.com/library/audio/prompts/numbers/81.wav')
    eightyone.currentTime = 0
    eightyone.play()
   }      
</script>

## Comment construire un jeu de multiplication

Puisque la pratique est la meilleure façon d'apprendre et que la multiplication ne fait pas exception, j'ai décidé d'écrire un petit jeu, que vous pouvez voir ci-dessous. 

<!-- HTML elements 
UI consists of an input element of type 'number' that ensures only numeric characters can be entered. Also, a 'Submit' button element clicking 
on which evaluates user's answers and credits Correct or Incorrect sets accordingly. Another button element 'Restart', resets answer count to zero and restarts the game. The buttons and headers are placed within standardized div elements to insure uniformly reliable user experience. 
-->
<div 
     class='flex-container' 
     style='margin: 0; 
            display: flex;
            flex-direction: column;
            justify-content: space-around; 
            align-items: center;'
     >
    <div 
         class='row' 
         style='margin: 0 auto;
                width: 100%;
                height: 60px;
                display: flex; 
                justify-content: space-around;
                align-items: center;'
         >
    	<h2 
            style='color: #3F51B5;
                   text-align: center;'
            >Entrez votre réponse et cliquez sur Soumettre
        </h2>
    </div>
    <div 
         class='row' 
         style='margin: 0 auto; 
                width: 100%; 
                height: 60px; 
                display: flex;
                justify-content: space-around; 
                align-items: center;'
         >
    	<div 
             style='width: 250px;
                    height: 60px;'
             >
         	<h3 
                style='background:#fff; 
                   	   font-size: 3rem;
                       height: 60px;
                       line-height: 60px;
                       margin: 0 -3px 0 0;
                       text-align: center;
                       color: #3F51B5;
                       border-radius:5px;
                       border: 2px solid #eee;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
                id='currentQuestion'
         	    >
            </h3>
         </div>
    	 <div 
              style='width: 250px; 
                     height: 60px;'
              >
        	<input style='margin: 0 auto;
                      	  border: 2px solid #eee;
                          box-shadow:0 0 15px 4px rgba(0,0,0,0.06);
                          border-radius:5px;
                          font-size: 3rem;
                          background: #fff;
                          width: 250px;
                          height: 60px;
                          margin: 0 auto;
                          color: #3F51B5;'
               	   type='number' 
               	   name='' 
                   id='currentAnswer' 
                   min='0' max='81' step='1' 
                   placeholder='Réponse ici' 
         	/>
         </div>
         <div 
              style='width: 250px; 
                     height: 60px;'
              >
         	<button style='background: #3F51B5; 
                           font-size: 3rem;
                           width: 250px;
                           height: 58px;
                           line-height: 56px;
                           margin: 0;
                           font-weight: 600;
                           border-radius:5px;
                           color:#fff;'
                	type='button'
                	id='submit'
                	onclick='handleSubmit()'
        	>Soumettre<audio id='submitSound' src='https://www.fesliyanstudios.com/play-mp3/6683'/>
            </button>
         </div>
    </div>
    <div 
         class='row' 
         style='margin: 0 auto; 
                width: 100%; 
                height: 60px; 
                display: flex; 
                justify-content: space-around; 
                align-items: center;'
         >
    	<div 
             style='width: 250px; 
                    height: 60px;'
             >
        	<h3 style='background:#fff; 
                       font-size: 3rem;
                       height: 60px;
                       line-height: 60px;
                       margin: 0 0 0 0;
                       text-align: center;
                       color: #3fef10;
                       border-radius:5px;
                       border: 2px solid #3fef10;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
            id='greenScore'
          >Correct : <span id='green'></span>
            </h3>
        </div>
        <div 
             style='width: 250px; 
                    height: 60px;'
             >
        	<h3 style='background:#fff; 
                       font-size: 3rem;	
                       height: 60px;
                       line-height: 60px;
                       margin: 0 0 0 0;
                       text-align: center;
                       color: #f60e09;
                       border-radius:5px;
                       border: 2px solid #f60e09;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
            id='redScore'
         >Incorrect : <span id='red'></span>
            </h3>
        </div>
        <div 
             style='width: 250px;
                    height: 60px;'
             >
        	<button style='background: #3F51B5; 
                           font-size: 3rem;
                           width: 250px;
                           height: 58px;
                           line-height: 56px;
                           margin: 0;
                           font-weight: 600;
                           border-radius:5px;
                           color:#fff;'
                type='button'
                id='restart'
                onclick='handleRestart()'
        >Redémarrer<audio id='restartSound' src='https://www.fesliyanstudios.com/play-mp3/6683'/>
            </button>
        </div>
    </div>
     <div 
          class='row' 
          style='margin: 0 auto; 
                 width: 100%; 
                 height: 60px; 
                 display: flex; 
                 justify-content: space-around;
                 align-items: center;'
          >
    	<h3 style='background:#fff; 
                   font-size: 3rem;
                   height: 60px;
                   line-height: 60px;
                   margin: 0;
                   text-align: center;
                   color: #3F51B5;
                   border-radius:5px;
                   border: 2px solid #eee;
                   box-shadow:0 0 15px 4px rgba(0,0,0,0.06)'
        id='gameResult'
         ></h3>
    </div>
 </div>

<!--   CSS   -->
<!-- media accomodates two additional viewport sizes -->
<style>
    
    /* Mobile phones */
    @media screen and (max-width: 767px){
       .flex-container {
          transform: scale(0.60);
         }
     }
    /* Tablets and iPads */
    @media screen and (min-width: 768px) and (max-width: 1023px){
       .flex-container {
          transform: scale(0.8);
       }
    }
</style>

<!--   JS   --->
<script>
    // Element declaration
    const submitButton = document.getElementById('submit');
    const restartButton = document.getElementById('restart');
    const submitSound = document.getElementById('submitSound');
    const restartSound = document.getElementById('restartSound');
    const currentQuestion = document.getElementById('currentQuestion');
	const currentAnswer = document.getElementById('currentAnswer');
	const gameResult = document.getElementById('gameResult');
	const greenScore = document.getElementById('green');
	const redScore = document.getElementById('red');
	let indexer; 
	let green; 
	let red; 
    
   // Standalone audio elements
    const successSound = new Audio('https://www.pacdv.com/sounds/applause-		sounds/app-29.wav')
	const failureSound = new Audio('https://www.pacdv.com/sounds/voices/no-		thats-not-gonna-do-it.wav')
    const noAnswerSound = new         Audio('https://www.pacdv.com/sounds/mechanical_sound_effects/glass_breaking_2.wav')			                                 
   
    // Question set
    const matrix = [
    '1 X 1','1 X 2', '1 X 3', '1 X 4', '1 X 5', '1 X 6', '1 X 7', '1 x 8', '1 X 9', '2 X 1', '2 X 2', '2 X 3', '2 X 4', '2 X 5', '2 X 6', '2 X 7', '2 X 8', '2 X 9', '3 X 1', '3 X 2', '3 X 3', '3 X 4', '3 X 5', '3 X 6', '3 X 7', '3 X 8', '3 X 9', '4 X 1', '4 X 2', '4 X 3', '4 X 4', '4 X 5', '4 X 6', '4 X 7', '4 X 8', '4 X 9', '5 X 1', '5 X 2', '5 X 3', '5 X 4', '5 X 5', '5 X 6', '5 X 7', '5 X 8', '5 X 9', '6 X 1', '6 X 2', '6 X 3', '6 X 4', '6 X 5', '6 X 6', '6 X 7', '6 X 8', '6 X 9', '7 X 1', '7 X 2', '7 X 3', '7 X 4', '7 X 5', '7 X 6', '7 X 7', '7 X 8', '7 X 9', '8 X 1', '8 X 2', '8 X 3', '8 X 4', '8 X 5', '8 X 6', '8 X 7', '8 X 8', '8 X 9', '9 X 1', '9 X 2', '9 X 3', '9 X 4', '9 X 5', '9 X 6', '9 X 7', '9 X 8', '9 X 9'
    ]
    
  // Random integer generator
   	const getRandomInt = max => Math.floor(Math.random() * Math.floor(max));
  
 
  // Animation handling
    const handleActive = (button) => {
        submitSound.currentTime = 0
        submitSound.play()
    	button.style.backgroundColor = '#5698a9'
        button.style.transform = 'scale(0.95)'
        setTimeout(() => {
			button.style.backgroundColor = '#3F51B5'
        	button.style.transform = 'scale(1.0)'
        	}, 100)
    }
    
  // Initial load and restart handling
   	const handleRestart = () => {
        handleActive(restartButton)
        submitButton.disabled = false;
   		indexer = getRandomInt(81);
   		green = 0;
   		red = 0;
   		currentQuestion.textContent = matrix[indexer];
   		greenScore.textContent = green;
   		redScore.textContent = red;
   		gameResult.textContent = '';
   		currentAnswer.value = '';
	};
  
  // Initializes somponents ad page loads  
    window.addEventListener('DOMContentLoaded', handleRestart());
  
  // Load next question
   	const getNext = () => {
  		currentAnswer.value = '';
  		indexer = getRandomInt(81);
  		currentQuestion.textContent = matrix[indexer]; 
	};
    
  // Summarize and display final result
   	const endGame = () => {
        green > red ? successSound.play() : failureSound.play()
    	gameResult.textContent = green > red ? 'Bon travail ! Jouez à nouveau pour 			renforcer vos connaissances' : 'Vous pouvez faire mieux, essayez à nouveau';  
        submitButton.disabled = true;
	};
    
  // Evaluation handling
    const handleSubmit = () => {
    	   handleActive(submitButton)
        if (currentAnswer.value === '') {
            noAnswerSound.play()
            gameResult.textContent = 'Veuillez entrer votre réponse et appuyer 				Sur Soumettre';
        } else {
            let trueOrFalse = eval(matrix[indexer].replace(' X ', '*')) 			 		== currentAnswer.value;
            if (trueOrFalse) {
     			green++;
    			greenScore.textContent = green;
   				gameResult.textContent = 'Correct';
    		} else {
    			red++;
    			redScore.textContent = red;
   				gameResult.textContent = 'Incorrect';
    		}
            green + red < 10 ? getNext() : endGame()
        }
    }
    
</script>

Dans la fenêtre en haut à gauche, il y a une question de défi. À côté se trouve un élément d'entrée qui prend une réponse. Cliquer sur le bouton Soumettre évalue cette réponse et affiche le message indiquant si elle est correcte. 

Les réponses correctes sont ajoutées au compteur vert "Réponses correctes", tandis que les réponses incorrectes sont ajoutées au compteur rouge à côté. 

Une fois la réponse évaluée, une nouvelle question de défi est générée à l'aide d'un générateur de nombres aléatoires et le cycle se répète. Après dix cycles de questions, le jeu s'arrête et le résultat final est affiché, accompagné de la lecture d'un fichier sonore. 

Appuyer sur le bouton Redémarrer commence un nouveau jeu de dix questions. Appuyer sur le bouton Soumettre sans entrer de réponse déclenche un message d'avertissement et un son. 

Vous pouvez facilement changer le design visuel et l'emplacement des éléments dans les limites de l'éditeur. De plus, la logique employée ici peut être appliquée dans la conception d'autres jeux. Par exemple, la multiplication peut être changée en Trivia de films et bien plus encore.

Le code complet avec des commentaires peut être consulté en tant que dépôt Github en [cliquant ici](https://github.com/sandroarobeli/MultiplicationGame/blob/master/MultiplicationGame.txt).