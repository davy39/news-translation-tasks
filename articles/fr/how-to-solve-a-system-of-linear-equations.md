---
title: Comment résoudre un système d'équations linéaires
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-10T12:48:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-a-system-of-linear-equations
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9baf740569d1a4ca2d4b.jpg
tags:
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: Comment résoudre un système d'équations linéaires
seo_desc: "By Alexander Arobelidze\nA linear equation is an equation that graphs a\
  \ line. A system of linear equations is when there are two or more linear equations\
  \ grouped together. \nTo simplify the illustration, we will consider systems of\
  \ two equations. As th..."
---

Par Alexander Arobelidze

Une équation linéaire est une équation qui représente une ligne. Un système d'équations linéaires est un ensemble de deux ou plusieurs équations linéaires regroupées.

Pour simplifier l'illustration, nous considérerons des systèmes de deux équations. Comme le suggère le nom, il y a deux variables inconnues. Souvent, elles sont désignées par les lettres **x** et **y**. Si les équations décrivent un certain processus, les lettres peuvent être choisies en fonction de leur rôle. Par exemple, **d** peut représenter la distance, et **t** le temps.

Dans cet article, nous apprendrons à résoudre des systèmes d'équations linéaires en utilisant deux méthodes amusantes. Mais avant de commencer, voyons comment nous obtenons un système particulier en examinant un exemple concret.

## Déduire un système

Un garçon monte sur son vélo et commence à rouler vers l'école. Il parcourt **200** yards chaque minute.

**6** minutes plus tard, sa mère réalise que son fils a oublié son déjeuner. Elle monte sur son propre vélo et commence à suivre le garçon. Elle parcourt **500** yards chaque minute (elle est une olympienne et médaillée d'or).

Nous voulons savoir combien de temps il faut à la mère pour rattraper le garçon, et quelle distance elle doit parcourir pour cela.

Puisque le garçon parcourt 200 yards chaque minute, en **t** minutes il parcourra **200** fois **t** yards, ou **200t** yards.

Sa mère commence à faire du vélo **6** minutes plus tard, donc elle roule pendant **(t - 6)** minutes. Puisqu'elle parcourt 500 yards chaque minute, en (t - 6) minutes elle parcourt **500** fois **(t - 6)** yards, ou **500(t - 6)** yards.

Au moment où elle le rattrape, ils ont tous les deux parcouru la même distance. Disons pour l'instant que cette distance est **d**.

Pour le garçon, nous avons **d = 200t** et pour sa mère, nous avons **d = 500(t - 6)**. Nous avons maintenant notre système de deux équations.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/system1.png)
_Un système de deux équations d=200t et d=500(t - 6)_

Une accolade est souvent ajoutée pour indiquer que les équations forment un système.

Maintenant, voyons comment nous pouvons résoudre ce système.

## Résolution par substitution

La première méthode que nous considérerons utilise la **substitution**.

Nous avons deux inconnues ici, **d** et **t**. L'idée est de se débarrasser d'une variable en l'exprimant à l'aide de l'autre variable.

L'équation du haut nous dit que **d = 200t**, alors remplaçons **200t** par **d** dans l'équation du bas. En résultat, nous avons une équation avec seulement la variable **t**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/system2.png)
_Une équation avec une seule variable 200t = 500(t - 6)_

D'abord, nous développons le côté droit : 500(t -6) = 500t - 500*6 = **500t - 3000**.

Ensuite, nous simplifions en déplaçant les membres inconnus d'un côté et les membres connus de l'autre. Le résultat est : **500t - 200t = 3000**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/system3.png)
_La résolution de l'équation 300t = 3000 donne t = 10_

Résoudre pour **t** nous donne **t = 10**, ou puisque nous mesurons le temps en minutes, **t = 10 minutes**. En d'autres termes, la mère rattrapera son fils en 10 minutes.

La deuxième partie de notre problème est de trouver combien de distance elle a dû parcourir pour le rattraper.

Pour répondre à cette question, nous devons trouver **d**. Substituer t = 10 dans l'une ou l'autre équation nous donnera cette réponse.

Pour simplifier, utilisons l'équation du haut, **d = 200t = 200 * 10 = 2000**. Puisque nous mesurons la distance en yards, **d = 2000 yards**.

Testons votre compréhension jusqu'à présent – essayez de résoudre le système suivant par vous-même :

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs d'éléments et les noms de fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <div style='display: flex;'>
    <div style='transform: scale(4.3); margin-top: 52px;'>&#123;</div>
    <div style='margin-left: 20px;'>
      <h3>y = 2x</h3>
      <h3>y = 3(x - 1)</h3>
    </div>  
  </div>  
    
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-11' style='padding: 10px;'>
   <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        x = 3 et y = 6</label>
        <span id='result-11'></span>
    </div>
    <hr/>
    
    <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1 et y = 2</label>
        <span id='result-12'></span>
    </div>	
    <hr/>
     
    <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 6 et y = 3</label>
        <span id='result-13'></span>
    </div>
    <hr/>
     
    <div id='block-14' style='padding: 10px;'>
        <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         x = 1/2 et y = 2/3</label>
        <span id='result-14'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer1()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer1'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer1() {
    	if (document.getElementById('option-11').checked) {
      
        document.getElementById('block-11').style.border = '3px solid limegreen'
        document.getElementById('result-11').style.color = 'limegreen'
		document.getElementById('result-11').innerHTML = 'Correct !'
        
        } 
        if (document.getElementById('option-12').checked) {
        document.getElementById('block-12').style.border = '3px solid red'
        document.getElementById('result-12').style.color = 'red'
		document.getElementById('result-12').innerHTML = 'Incorrect !'
        showCorrectAnswer1()
 		}
        if (document.getElementById('option-13').checked) {
        document.getElementById('block-13').style.border = '3px solid red'
        document.getElementById('result-13').style.color = 'red'
		document.getElementById('result-13').innerHTML = 'Incorrect !'
        showCorrectAnswer1()	
        }
        if (document.getElementById('option-14').checked) {
        document.getElementById('block-14').style.border = '3px solid red'
        document.getElementById('result-14').style.color = 'red'
		document.getElementById('result-14').innerHTML = 'Incorrect !'
        showCorrectAnswer1() 	
        }
     }
    // la fonction affiche le lien vers la bonne réponse
    function showCorrectAnswer1() {
        	 let showAnswer1 = document.createElement('p')
             showAnswer1.innerHTML = 'Afficher la bonne réponse'
        showAnswer1.style.position = 'relative'
        showAnswer1.style.top = '-180px'
        showAnswer1.style.fontSize = '1.75rem'
             document.getElementById('showanswer1').appendChild(showAnswer1)
             showAnswer1.addEventListener('click', () => {
        	 document.getElementById('block-11').style.border = '3px solid limegreen'
        document.getElementById('result-11').style.color = 'limegreen'
		document.getElementById('result-11').innerHTML = 'Correct !'
        document.getElementById('showanswer1').removeChild(showAnswer1)    
         
        })
        }
</script>

Dans le système ci-dessus, les variables inconnues sont **x** et **y**.

De l'équation du haut, nous savons que **y = 2x**. En substituant cela dans l'équation du bas, nous obtenons **2(2x) = 3(x + 1)**.

Une fois que nous avons développé et simplifié, nous obtenons **4x = 3x + 3**. Ou **x = 3**. Par conséquent, **y = 2 * 3 = 6**.

## Résolution par graphique

La deuxième méthode que nous considérerons utilise le **graphique**, où nous trouvons la solution à un système d'équations en les traçant.

Par exemple, prenons ce système : **y = 2x + 3** et **y = 9 - x**.

Un graphique de chaque équation sera une ligne. Le premier pour **y = 2x + 3** ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph1-1.png)
_Un graphique de y = 2x + 3_

Ensuite, nous pouvons tracer une ligne pour **y = 9 - x** :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph2.png)
_Graphiques de y = 2x + 3 et y = 9 - x_

Ces deux lignes **se croisent** en exactement un point. Ce point est la seule solution aux deux équations :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph3-1.png)
_Graphiques de y = 2x + 3 et y = 9 - x se croisent au point (2, 7)_

La paire ordonnée **(2, 7)** nous donne les coordonnées de notre point d'intersection. Cette paire est la solution du système. Substituer **x = 2** et **y = 7** nous permettra de vérifier cela.

Et si les graphiques sont parallèles et ne se croisent pas du tout ? Par exemple :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph4.png)
_Graphiques de y = x - 1 et y = x - 3_

Lorsque les graphiques des équations ne se croisent pas, cela signifie que notre système n'a pas de solution. Essayer de résoudre par substitution le prouvera.

Le résultat de **x - 1** **= x - 3** sera **0 = -2**, ce qui est **toujours** **faux**.

Mais que se passe-t-il si deux graphiques sont les mêmes et sont directement l'un sur l'autre ?

![Image](https://www.freecodecamp.org/news/content/images/2020/04/graph5.png)
_Graphiques de y = x - 2 et y = x - 2_

Dans de tels cas, il y a un nombre infini de points d'intersection. Cela signifie que notre système a un nombre infini de solutions. L'utilisation de la méthode de substitution le prouvera.

Le résultat de **x - 2 = x - 2** est **0 = 0**, ce qui est **toujours vrai**.

## Plus de pratique

Essayez d'utiliser à la fois les méthodes de substitution et de graphique pour résoudre les systèmes suivants. Ces méthodes se complètent et vous aideront à solidifier vos connaissances.

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs d'éléments et les noms de fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <div style='display: flex;'>
    <div style='transform: scale(4.3); margin-top: 52px;'>&#123;</div>
    <div style='margin-left: 20px;'>
      <h3>y = 2</h3>
      <h3>3y - 2x = 4</h3>
    </div>  
  </div>  
    
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-21' style='padding: 10px;'>
   <label for='option-21' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-21' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        Le système n'a pas de solution</label>
        <span id='result-21'></span>
    </div>
    <hr/>
    
    <div id='block-22' style='padding: 10px;'>
    <label for='option-22' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-22' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1/2 et y = 1</label>
        <span id='result-22'></span>
    </div>	
    <hr/>
     
    <div id='block-23' style='padding: 10px;'>
    <label for='option-23' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-23' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1 et y = 2</label>
        <span id='result-23'></span>
    </div>
    <hr/>
     
    <div id='block-24' style='padding: 10px;'>
        <label for='option-24' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-24' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         x = 0 et y = 2</label>
        <span id='result-24'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer2()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer2'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer2() {
    	if (document.getElementById('option-23').checked) {
      
        document.getElementById('block-23').style.border = '3px solid limegreen'
        document.getElementById('result-23').style.color = 'limegreen'
		document.getElementById('result-23').innerHTML = 'Correct !'
        
        } 
        if (document.getElementById('option-21').checked) {
        document.getElementById('block-21').style.border = '3px solid red'
        document.getElementById('result-21').style.color = 'red'
		document.getElementById('result-21').innerHTML = 'Incorrect !'
        showCorrectAnswer2()
 		}
        if (document.getElementById('option-22').checked) {
        document.getElementById('block-22').style.border = '3px solid red'
        document.getElementById('result-22').style.color = 'red'
		document.getElementById('result-22').innerHTML = 'Incorrect !'
        showCorrectAnswer2()	
        }
        if (document.getElementById('option-24').checked) {
        document.getElementById('block-24').style.border = '3px solid red'
        document.getElementById('result-24').style.color = 'red'
		document.getElementById('result-24').innerHTML = 'Incorrect !'
        showCorrectAnswer2() 	
        }
     }
    // la fonction affiche le lien vers la bonne réponse
    function showCorrectAnswer2() {
        	 let showAnswer2 = document.createElement('p')
             showAnswer2.innerHTML = 'Afficher la bonne réponse'
        showAnswer2.style.position = 'relative'
        showAnswer2.style.top = '-180px'
        showAnswer2.style.fontSize = '1.75rem'
             document.getElementById('showanswer2').appendChild(showAnswer2)
             showAnswer2.addEventListener('click', () => {
        	 document.getElementById('block-23').style.border = '3px solid limegreen'
        document.getElementById('result-23').style.color = 'limegreen'
		document.getElementById('result-23').innerHTML = 'Correct !'
        document.getElementById('showanswer2').removeChild(showAnswer2)    
         
        })
        }
</script>

Choisir une variable particulière à utiliser dans la substitution devrait faciliter la recherche d'une solution.

Essayez d'exprimer **x** avec deux autres membres dans l'équation du haut, puis substituez le résultat dans l'équation du bas. De cette façon, vous éviterez de traiter avec des fractions.

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs d'éléments et les noms de fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <div style='display: flex;'>
    <div style='transform: scale(4.3); margin-top: 52px;'>&#123;</div>
    <div style='margin-left: 20px;'>
      <h3>x + 5y = 7</h3>
      <h3>3x - 2y = 4</h3>
    </div>  
  </div>  
    
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-31' style='padding: 10px;'>
   <label for='option-31' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-31' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        x = 5 et y = 5/2</label>
        <span id='result-31'></span>
    </div>
    <hr/>
    
    <div id='block-32' style='padding: 10px;'>
    <label for='option-32' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-32' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1 et y = 2</label>
        <span id='result-32'></span>
    </div>	
    <hr/>
     
    <div id='block-33' style='padding: 10px;'>
    <label for='option-33' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-33' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 1 et y = 1</label>
        <span id='result-33'></span>
    </div>
    <hr/>
     
    <div id='block-34' style='padding: 10px;'>
        <label for='option-34' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-34' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         x = 2 et y = 1</label>
        <span id='result-34'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer3()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer3'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer3() {
    	if (document.getElementById('option-34').checked) {
      
        document.getElementById('block-34').style.border = '3px solid limegreen'
        document.getElementById('result-34').style.color = 'limegreen'
		document.getElementById('result-34').innerHTML = 'Correct !'
        
        } 
        if (document.getElementById('option-31').checked) {
        document.getElementById('block-31').style.border = '3px solid red'
        document.getElementById('result-31').style.color = 'red'
		document.getElementById('result-31').innerHTML = 'Incorrect !'
        showCorrectAnswer3()
 		}
        if (document.getElementById('option-32').checked) {
        document.getElementById('block-32').style.border = '3px solid red'
        document.getElementById('result-32').style.color = 'red'
		document.getElementById('result-32').innerHTML = 'Incorrect !'
        showCorrectAnswer3()	
        }
        if (document.getElementById('option-33').checked) {
        document.getElementById('block-33').style.border = '3px solid red'
        document.getElementById('result-33').style.color = 'red'
		document.getElementById('result-33').innerHTML = 'Incorrect !'
        showCorrectAnswer3() 	
        }
     }
    // la fonction affiche le lien vers la bonne réponse
    function showCorrectAnswer3() {
        	 let showAnswer3 = document.createElement('p')
             showAnswer3.innerHTML = 'Afficher la bonne réponse'
        showAnswer3.style.position = 'relative'
        showAnswer3.style.top = '-180px'
        showAnswer3.style.fontSize = '1.75rem'
             document.getElementById('showanswer3').appendChild(showAnswer3)
             showAnswer3.addEventListener('click', () => {
        	 document.getElementById('block-34').style.border = '3px solid limegreen'
        document.getElementById('result-34').style.color = 'limegreen'
		document.getElementById('result-34').innerHTML = 'Correct !'
        document.getElementById('showanswer3').removeChild(showAnswer3)    
         
        })
        }
</script>

Faisons un dernier défi :

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs d'éléments et les noms de fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
  <div style='display: flex;'>
    <div style='transform: scale(4.3); margin-top: 52px;'>&#123;</div>
    <div style='margin-left: 20px;'>
      <h3>-6x - 8y = 4</h3>
      <h3>y = -x - 1</h3>
    </div>  
  </div>  
    
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-41' style='padding: 10px;'>
   <label for='option-41' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-41' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        x = -2 et y = 1</label>
        <span id='result-41'></span>
    </div>
    <hr/>
    
    <div id='block-42' style='padding: 10px;'>
    <label for='option-42' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-42' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        Nombre infini de solutions</label>
        <span id='result-42'></span>
    </div>	
    <hr/>
     
    <div id='block-43' style='padding: 10px;'>
    <label for='option-43' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='0' id='option-43' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        x = 2 et y = -1</label>
        <span id='result-43'></span>
    </div>
    <hr/>
     
    <div id='block-44' style='padding: 10px;'>
        <label for='option-44' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-44' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         x = -1/6 et y = 6</label>
        <span id='result-44'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer4()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer4'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer4() {
    	if (document.getElementById('option-41').checked) {
      
        document.getElementById('block-41').style.border = '3px solid limegreen'
        document.getElementById('result-41').style.color = 'limegreen'
		document.getElementById('result-41').innerHTML = 'Correct !'
        
        } 
        if (document.getElementById('option-42').checked) {
        document.getElementById('block-42').style.border = '3px solid red'
        document.getElementById('result-42').style.color = 'red'
		document.getElementById('result-42').innerHTML = 'Incorrect !'
        showCorrectAnswer4()
 		}
        if (document.getElementById('option-43').checked) {
        document.getElementById('block-43').style.border = '3px solid red'
        document.getElementById('result-43').style.color = 'red'
		document.getElementById('result-43').innerHTML = 'Incorrect !'
        showCorrectAnswer4()	
        }
        if (document.getElementById('option-44').checked) {
        document.getElementById('block-44').style.border = '3px solid red'
        document.getElementById('result-44').style.color = 'red'
		document.getElementById('result-44').innerHTML = 'Incorrect !'
        showCorrectAnswer4() 	
        }
     }
    // la fonction affiche le lien vers la bonne réponse
    function showCorrectAnswer4() {
        	 let showAnswer4 = document.createElement('p')
             showAnswer4.innerHTML = 'Afficher la bonne réponse'
        showAnswer4.style.position = 'relative'
        showAnswer4.style.top = '-180px'
        showAnswer4.style.fontSize = '1.75rem'
             document.getElementById('showanswer4').appendChild(showAnswer4)
             showAnswer4.addEventListener('click', () => {
        	 document.getElementById('block-41').style.border = '3px solid limegreen'
        document.getElementById('result-41').style.color = 'limegreen'
		document.getElementById('result-41').innerHTML = 'Correct !'
        document.getElementById('showanswer4').removeChild(showAnswer4)    
         
        })
        }
</script>

Maintenant que vous en savez assez sur la substitution et le graphique, sortez et résolvez plus d'équations linéaires.