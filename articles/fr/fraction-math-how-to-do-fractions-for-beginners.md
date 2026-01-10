---
title: 'Mathématiques des fractions : Comment faire des fractions pour débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-11T18:57:45.000Z'
originalURL: https://freecodecamp.org/news/fraction-math-how-to-do-fractions-for-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c2f740569d1a4ca3077.jpg
tags:
- name: fractions
  slug: fractions
- name: Math
  slug: math
seo_title: 'Mathématiques des fractions : Comment faire des fractions pour débutants'
seo_desc: 'By Alexander Arobelidze

  We deal with fractions every day. But what exactly is a fraction? How do we get
  to know them better? In this tutorial we will explore the basics and practice together,
  so fractions can become valuable helpers in everyday life ...'
---

Par Alexander Arobelidze

Nous traitons des fractions tous les jours. Mais qu'est-ce qu'une fraction exactement ? Comment pouvons-nous mieux les comprendre ? Dans ce tutoriel, nous explorerons les bases et pratiquerons ensemble, afin que les fractions puissent devenir des aides précieuses dans la vie quotidienne et au-delà. 

## Partie 1. Fraction comme une part

Imaginons une tarte entière divisée en 4 parts égales. Une part est colorée en rouge.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction1.png)
_image d'un cercle avec un quart coloré en rouge_

**Une** part rouge sur **quatre** parts égales signifie que **1/4** de l'ensemble est coloré. Si nous pensons aux parts égales d'un ensemble comme des parts, une part de la tarte ici est colorée en rouge. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction2.png)
_dessin d'une fraction 1/4. 1 est le Numérateur, 4 est le Dénominateur_

Le nombre 1 **au-dessus** de la ligne est appelé **Numérateur**. Il montre combien de parts sont colorées. Le nombre 4 **en dessous** de la ligne est appelé **Dénominateur**. Il montre en combien de parts **égales** l'ensemble est divisé. Regardons un autre exemple.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fractions3.png)
_image d'un cercle avec trois sixièmes colorés en rouge_

La nouvelle tarte ci-dessus est divisée en **6** parts égales. Par conséquent, le dénominateur sera égal à 6. Parmi ces 6 parts égales, **3** sont colorées en rouge. Par conséquent, le numérateur sera égal à 3. En d'autres termes, **3/6** de la tarte est coloré. 

Maintenant, testons ce que nous avons appris jusqu'à présent. Comme vous le savez, il y a 24 heures dans une journée entière. Si vous avez passé 6 heures à étudier, quelle fraction de la journée avez-vous passée à étudier ? 

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs des éléments et les noms des fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Quelle fraction d'une journée représente 6 heures ?</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-11' style='padding: 10px;'>
   <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        6/24</label>
        <span id='result-11'></span>
    </div>
    <hr/>
    
    <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        6</label>
        <span id='result-12'></span>
    </div>	
    <hr/>
     
    <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/3' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        1/3</label>
        <span id='result-13'></span>
    </div>
    <hr/>
     
    <div id='block-14' style='padding: 10px;'>
        <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='1/6' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         1/6</label>
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
    // la fonction affiche le lien vers la réponse correcte
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

Une journée est divisée en **24** parts égales appelées heures. Donc le dénominateur sera 24. Pensez aux 6 heures passées à étudier comme à **6** parts colorées de la tarte. Cela rendra le numérateur égal à 6. La fraction que nous cherchons est **6/24**.

## Partie 2. Simplification des fractions

Vous souvenez-vous de la tarte de l'exemple précédent ? Elle avait 3/6 de sa surface colorée en rouge. Ajoutons deux nouvelles tartes et regardons-les ensemble.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fractions4.png)
_image de 3 cercles avec la moitié de chacun peinte en rouge_

La première tarte est divisée en 4 parts et deux sont colorées en rouge. Mais comme nous pouvons le voir, c'est la moitié de la tarte. La deuxième tarte est divisée en 6 parts et trois sont colorées en rouge. Encore la moitié de la tarte. Enfin, la troisième tarte est divisée en deux moitiés et une moitié est colorée en rouge. 

Puisque c'est **la moitié** d'une tarte qui est colorée dans chaque cas, nous pouvons conclure que les fractions sont égales : **2/4 = 3/6 = 1/2**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction5.png)
_image de 3 cercles avec la moitié de chacun peinte en rouge. 2/4 = 3/6 = 1/2_

Enfin, en multipliant ou en divisant à la fois le numérateur et le dénominateur par le **même** nombre, la fraction restera la même (sauf dans le cas où la division est par zéro, ce qui est hors du cadre de cet article et ne sera pas considéré ici). 

Cette règle aide à simplifier les fractions et facilite leur utilisation. Par exemple, considérons 4/12. En divisant le numérateur et le dénominateur par 4, nous obtenons (4 : **4**) / (12 : **4**) = 1 / 3. Il est temps de tester vos connaissances.

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs des éléments et les noms des fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Quelle fraction est la même que 2/5 ?</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-21' style='padding: 10px;'>
   <label for='option-21' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/24' id='option-21' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        4/25</label>
        <span id='result-21'></span>
    </div>
    <hr/>
    
    <div id='block-22' style='padding: 10px;'>
    <label for='option-22' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6' id='option-22' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        5/2</label>
        <span id='result-22'></span>
    </div>	
    <hr/>
     
    <div id='block-23' style='padding: 10px;'>
    <label for='option-23' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/3' id='option-23' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        8/20</label>
        <span id='result-23'></span>
    </div>
    <hr/>
     
    <div id='block-24' style='padding: 10px;'>
        <label for='option-24' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='1/6' id='option-24' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         6/10</label>
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
    // la fonction affiche le lien vers la réponse correcte
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

## Partie 3. Comparaison des fractions

Lorsque nous voyons deux parts d'une tarte, nous pouvons généralement dire laquelle est la plus grande. De même avec les fractions, il existe une méthode simple pour les comparer entre elles. 

Supposons que nous devons comparer 1/3 et 2/7. Comme ils ont des dénominateurs différents, ils ont un nombre de parts différent. Donc la **première étape** doit être de trouver un **terrain commun**. Nous le faisons en trouvant un **dénominateur commun**. 

L'une des méthodes pour trouver un dénominateur commun de deux ou plusieurs fractions est de multiplier les dénominateurs entre eux. **3** fois **7** = **21**. 

Maintenant que nous avons trouvé le dénominateur commun, nous devons remplacer le dénominateur de chaque fraction par le dénominateur commun. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction6.png)
_ramener 1/3 et 2/7 au dénominateur commun_

La première fraction est 1/3, donc nous divisons 21 par 3 et le résultat **7** est multiplié par le numérateur de cette fraction. Comme le numérateur est égal à 1, nous obtenons **7 fois 1 = 7**. 

La deuxième fraction est 2/7, donc 21 divisé par 7 donne 3. En multipliant 3 par le numérateur de cette fraction, nous obtenons **3 fois 2 = 6**.  

Maintenant que les fractions ont le même dénominateur, nous pouvons enfin les comparer. 7 parts est plus que 6 parts, donc 7/21 est plus grand que 6/21. 

Le symbole mathématique désignant notre résultat est le signe **>**. **7/21 > 6/21**. Il se lit comme "**plus grand que**". Le symbole désignant **plus petit que** ressemble à ceci : **<**. Nous pouvons réécrire notre résultat comme ceci : **6/21 < 7/21**. 

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs des éléments et les noms des fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Comparer 3/4 et 5/7</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-31' style='padding: 10px;'>
   <label for='option-31' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='5/7' id='option-31' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        3/4 est inférieur à 5/7</label>
        <span id='result-31'></span>
    </div>
    <hr/>
    
    <div id='block-32' style='padding: 10px;'>
    <label for='option-32' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='3/4' id='option-32' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        3/4 est supérieur à 5/7</label>
        <span id='result-32'></span>
    </div>	
    <hr/>
     
    <div id='block-33' style='padding: 10px;'>
    <label for='option-33' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1' id='option-33' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        3/4 est égal à 5/7</label>
        <span id='result-33'></span>
    </div>
    <hr/>
     
    <div id='block-34' style='padding: 10px;'>
        <label for='option-34' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='0' id='option-34' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         Ils ne peuvent pas être comparés</label>
        <span id='result-34'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer3()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer3'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer3() {
    	if (document.getElementById('option-32').checked) {
      
        document.getElementById('block-32').style.border = '3px solid limegreen'
        document.getElementById('result-32').style.color = 'limegreen'
		document.getElementById('result-32').innerHTML = 'Correct !'
        
        } 
        if (document.getElementById('option-31').checked) {
        document.getElementById('block-31').style.border = '3px solid red'
        document.getElementById('result-31').style.color = 'red'
		document.getElementById('result-31').innerHTML = 'Incorrect !'
        showCorrectAnswer3()
 		}
        if (document.getElementById('option-33').checked) {
        document.getElementById('block-33').style.border = '3px solid red'
        document.getElementById('result-33').style.color = 'red'
		document.getElementById('result-33').innerHTML = 'Incorrect !'
        showCorrectAnswer3()	
        }
        if (document.getElementById('option-34').checked) {
        document.getElementById('block-34').style.border = '3px solid red'
        document.getElementById('result-34').style.color = 'red'
		document.getElementById('result-34').innerHTML = 'Incorrect !'
        showCorrectAnswer3() 	
        }
     }
    // la fonction affiche le lien vers la réponse correcte
    function showCorrectAnswer3() {
        	 let showAnswer3 = document.createElement('p')
             showAnswer3.innerHTML = 'Afficher la bonne réponse'
        showAnswer3.style.position = 'relative'
        showAnswer3.style.top = '-180px'
        showAnswer3.style.fontSize = '1.75rem'
             document.getElementById('showanswer3').appendChild(showAnswer3)
             showAnswer3.addEventListener('click', () => {
        	 document.getElementById('block-32').style.border = '3px solid limegreen'
        document.getElementById('result-32').style.color = 'limegreen'
		document.getElementById('result-32').innerHTML = 'Correct !'
        document.getElementById('showanswer3').removeChild(showAnswer3)    
         
        })
        }
</script>

## Partie 4. Addition des fractions

Pour additionner des fractions, nous devons à nouveau trouver un dénominateur commun. Regardons l'exemple suivant. 

Nous devons additionner **2/7** et **3/9**. Le dénominateur commun est **7 fois 9 = 63**. L'étape suivante serait de remplacer le dénominateur de chaque fraction par le dénominateur commun. 

Pour la première fraction, **63 divisé par 7 = 9** et **9 fois 2 = 18**. Le résultat est **18/63**. Pour la deuxième, **63 divisé par 9 = 7** et **7 fois 3 = 21**. Le résultat est **21/63**. 

Ensuite, nous additionnons les numérateurs. **18 plus 21 = 39**, ce qui nous laisse avec la somme de **39/63**. 

Comme une habitude utile, vérifiez toujours si la fraction résultante peut être simplifiée davantage. 

Nous savons que 39 est divisible par 3. 63 est également divisible par 3. Puisque le numérateur et le dénominateur sont divisés par le même nombre, la fraction restera la même. **39 divisé par 3 = 13** et **63 divisé par 3 = 21**. Notre résultat final est **13/21**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction7.png)
_Calcul de l'addition de fractions 2/7 + 3/9 = 39/63 = 13/21_

Que faire si nous devons additionner des nombres mixtes ? Pour additionner des nombres mixtes, nous additionnons d'abord les nombres entiers ensemble, puis les fractions. 

Par exemple, pour additionner **1 et demi** à **2 et demi**, additionnez **1 et 2 = 3**, puis additionnez **1/2 et 1/2 = 1**. Enfin, **additionnez 3 et 1 = 4**. Faisons un peu de pratique et rappelons-nous comment simplifier les résultats. 

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs des éléments et les noms des fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Quel est le résultat de 4/6 + 2/9 ?</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-41' style='padding: 10px;'>
   <label for='option-41' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='8/9' id='option-41' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        8/9</label>
        <span id='result-41'></span>
    </div>
    <hr/>
    
    <div id='block-42' style='padding: 10px;'>
    <label for='option-42' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='9/8' id='option-42' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        9/8</label>
        <span id='result-42'></span>
    </div>	
    <hr/>
     
    <div id='block-43' style='padding: 10px;'>
    <label for='option-43' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/2' id='option-43' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        1/2</label>
        <span id='result-43'></span>
    </div>
    <hr/>
     
    <div id='block-44' style='padding: 10px;'>
        <label for='option-44' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='7/18' id='option-44' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         7/18</label>
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
    // la fonction affiche le lien vers la réponse correcte
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

## Partie 5. Soustraction des fractions

Nous commencerons par deux fractions simples. Soustrayons 1/3 de 3/5. Comme dans le cas de l'addition, nous devons trouver un dénominateur commun. Donc si nous multiplions nos dénominateurs, cela **égale 3 fois 5 = 15**. 

Ensuite, nous remplaçons les anciens dénominateurs par le dénominateur commun.  

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction8.png)
_image de 3/5 - 1/3 = 4/15_

Ensuite, nous devons trouver nos numérateurs. Pour la première fraction, **15 divisé par 5 = 3** et **3 fois 3 = 9**. Le résultat est **9/15**. Pour la deuxième, **15 divisé par 3 = 5** et **5 fois 1 = 5**. Le résultat est **5/15**. 

La dernière étape consiste à soustraire les numérateurs ajustés : **9 moins 5 = 4.** La fraction résultante est égale à **4/15**.  

Regardons maintenant le cas où nous devons soustraire une fraction d'un **nombre entier**. Commençons par **1 - 2/7**. 

Vous vous souvenez des sections précédentes qu'un nombre entier est comme une tarte qui est complètement colorée. Ainsi, si une tarte est divisée en **3** parts, **toutes les 3** parts sont colorées. Si elle est divisée en **7** parts, alors **7** parts seront colorées. Donc, **1 = 3/3 = 7/7** etc. 

Puisque nous devons soustraire **2/7**, nous allons transformer **1 entier** en **7/7** pour faciliter notre tâche. **7/7 moins 2/7 = 5/7**. Si le nombre entier est autre que **1**, nous l'écrivons comme un nombre mixte et suivons les étapes de l'exemple précédent. 

Donc, soustrayons **2/7 de 3**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction9.png)
_image de 3 - 2/7 = 19/7_

Souvent, à la suite de calculs, nous pouvons obtenir une fraction où le numérateur est supérieur ou égal au dénominateur. De telles fractions sont appelées fractions impropres. Par exemple **5/3** (cinq tiers), **7/2** (sept moitiés) et ainsi de suite. Elles peuvent être converties en nombres mixtes et vice versa. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction10.png)
_Conversion de fractions impropres en nombres mixtes et vice versa_

Toutes les règles couvertes jusqu'à présent s'appliquent également aux fractions impropres. 

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs des éléments et les noms des fonctions ont dû être indexés.
 Affiche une question avec quatre réponses cliquables possibles --> 

<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Quel est le résultat de 9/11 - 3/4 ?</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-51' style='padding: 10px;'>
   <label for='option-51' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/7' id='option-51' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        6/7</label>
        <span id='result-51'></span>
    </div>
    <hr/>
    
    <div id='block-52' style='padding: 10px;'>
    <label for='option-52' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/44' id='option-52' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        6/44</label>
        <span id='result-52'></span>
    </div>	
    <hr/>
     
    <div id='block-53' style='padding: 10px;'>
    <label for='option-53' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='3/44' id='option-53' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        3/44</label>
        <span id='result-53'></span>
    </div>
    <hr/>
     
    <div id='block-54' style='padding: 10px;'>
        <label for='option-54' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='6/11' id='option-54' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         6/11</label>
        <span id='result-54'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer5()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer5'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer5() {
    	if (document.getElementById('option-53').checked) {
      
        document.getElementById('block-53').style.border = '3px solid limegreen'
        document.getElementById('result-53').style.color = 'limegreen'
		document.getElementById('result-53').innerHTML = 'Correct !'
        
        } 
        if (document.getElementById('option-51').checked) {
        document.getElementById('block-51').style.border = '3px solid red'
        document.getElementById('result-51').style.color = 'red'
		document.getElementById('result-51').innerHTML = 'Incorrect !'
        showCorrectAnswer5()
 		}
        if (document.getElementById('option-52').checked) {
        document.getElementById('block-52').style.border = '3px solid red'
        document.getElementById('result-52').style.color = 'red'
		document.getElementById('result-52').innerHTML = 'Incorrect !'
        showCorrectAnswer5()	
        }
        if (document.getElementById('option-54').checked) {
        document.getElementById('block-54').style.border = '3px solid red'
        document.getElementById('result-54').style.color = 'red'
		document.getElementById('result-54').innerHTML = 'Incorrect !'
        showCorrectAnswer5() 	
        }
     }
    // la fonction affiche le lien vers la réponse correcte
    function showCorrectAnswer5() {
        	 let showAnswer5 = document.createElement('p')
             showAnswer5.innerHTML = 'Afficher la bonne réponse'
        showAnswer5.style.position = 'relative'
        showAnswer5.style.top = '-180px'
        showAnswer5.style.fontSize = '1.75rem'
             document.getElementById('showanswer5').appendChild(showAnswer5)
             showAnswer5.addEventListener('click', () => {
        	 document.getElementById('block-53').style.border = '3px solid limegreen'
        document.getElementById('result-53').style.color = 'limegreen'
		document.getElementById('result-53').innerHTML = 'Correct !'
        document.getElementById('showanswer5').removeChild(showAnswer5)    
         
        })
        }
</script>

## Partie 6. Multiplication des fractions

Supposons que nous devons multiplier deux fractions, **2/5 fois 3/7**. Le **numérateur** du produit sera le **produit des numérateurs** de ces fractions : **2 fois 3 = 6.** Le **dénominateur** du produit sera le **produit des dénominateurs** de ces fractions : **5 fois 7 = 35**. Ainsi, **2/5 fois 3/7 = 6/35**. 

Si nous devons multiplier une **fraction** par un **nombre entier**, le **numérateur** du produit sera le **produit du numérateur de la fraction et de ce nombre entier**. Le **dénominateur** du produit restera le même que le **dénominateur de la fraction**. 

Par exemple, **3/10 fois 5 = 15/10**. Pour simplifier, nous divisons le numérateur et le dénominateur par **5** et obtenons **3/2.** 

Enfin, si nous devons multiplier des nombres mixtes, nous les convertissons d'abord en fractions impropres, puis nous les multiplions comme nous l'avons fait ci-dessus. L'exemple ci-dessous montre les étapes. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction11.png)
_image de 3/2 fois 11/5 égale 33/10_

## Partie 7. Division des fractions

Pour diviser des fractions, inversez le diviseur de sorte que son numérateur devienne le **nouveau dénominateur** et le dénominateur devienne le **nouveau numérateur**. Ensuite, multipliez simplement les fractions comme nous l'avons fait précédemment. 

Par exemple, divisez 3/7 par 2/5. Après avoir inversé, **2/5** devient **5/2** et nous finissons par multiplier **3/7 fois 5/2 = 15/14**. 

Pour diviser une fraction par un **nombre entier**, nous inversons ce nombre et il devient **1 divisé par ce nombre**. 

Par exemple, **2 devient 1/2**, **9 devient 1/9** etc. Ensuite, nous multiplions comme ci-dessus. Comme vous l'avez probablement deviné, la division des nombres mixtes fonctionne de la même manière. Regardons l'exemple ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/fraction12.png)
_diviser 11/6 par 17/8 = 44/51_

Testons vos connaissances.

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs des éléments et les noms des fonctions ont dû être indexés.
 Affiche une question avec quatre réponses cliquables possibles --> 

<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Quel est le résultat de 11/3 divisé par 11/7 ?</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-71' style='padding: 10px;'>
   <label for='option-71' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='3/7' id='option-71' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        3/7</label>
        <span id='result-71'></span>
    </div>
    <hr/>
    
    <div id='block-72' style='padding: 10px;'>
    <label for='option-72' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='3' id='option-72' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        3</label>
        <span id='result-72'></span>
    </div>	
    <hr/>
     
    <div id='block-73' style='padding: 10px;'>
    <label for='option-73' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='7' id='option-73' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        7</label>
        <span id='result-73'></span>
    </div>
    <hr/>
     
    <div id='block-74' style='padding: 10px;'>
        <label for='option-74' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='7/3' id='option-74' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         7/3</label>
        <span id='result-74'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer7()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer7'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer7() {
    	if (document.getElementById('option-74').checked) {
      
        document.getElementById('block-74').style.border = '3px solid limegreen'
        document.getElementById('result-74').style.color = 'limegreen'
		document.getElementById('result-74').innerHTML = 'Correct !'
        
        } 
        if (document.getElementById('option-71').checked) {
        document.getElementById('block-71').style.border = '3px solid red'
        document.getElementById('result-71').style.color = 'red'
		document.getElementById('result-71').innerHTML = 'Incorrect !'
        showCorrectAnswer7()
 		}
        if (document.getElementById('option-72').checked) {
        document.getElementById('block-72').style.border = '3px solid red'
        document.getElementById('result-72').style.color = 'red'
		document.getElementById('result-72').innerHTML = 'Incorrect !'
        showCorrectAnswer7()	
        }
        if (document.getElementById('option-73').checked) {
        document.getElementById('block-73').style.border = '3px solid red'
        document.getElementById('result-73').style.color = 'red'
		document.getElementById('result-73').innerHTML = 'Incorrect !'
        showCorrectAnswer7() 	
        }
     }
    // la fonction affiche le lien vers la réponse correcte
    function showCorrectAnswer7() {
        	 let showAnswer7 = document.createElement('p')
             showAnswer7.innerHTML = 'Afficher la bonne réponse'
        showAnswer7.style.position = 'relative'
        showAnswer7.style.top = '-180px'
        showAnswer7.style.fontSize = '1.75rem'
             document.getElementById('showanswer7').appendChild(showAnswer7)
             showAnswer7.addEventListener('click', () => {
        	 document.getElementById('block-74').style.border = '3px solid limegreen'
        document.getElementById('result-74').style.color = 'limegreen'
		document.getElementById('result-74').innerHTML = 'Correct !'
        document.getElementById('showanswer7').removeChild(showAnswer7)    
         
        })
        }
</script>

## Partie 8. Quelques exemples pratiques

Pour trouver une fraction d'un nombre, nous devons **multiplier** le **nombre** donné par cette **fraction**. 

Imaginez que votre manuel scolaire compte 200 pages. Si vous lisez 3/5 du manuel, combien de pages avez-vous lues ? Nous avons le nombre qui est égal à 200. Pour trouver 3/5 de 200, nous multiplions **200 fois 3/5** et obtenons **120** pages. 

Résolvez la question suivante par vous-même. Mon gâteau d'anniversaire avait 12 parts. Quelques amis sont passés et ont apprécié 2/3 du gâteau. Combien de parts mes amis ont-ils eues ?

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs des éléments et les noms des fonctions ont dû être indexés.
 Affiche une question avec quatre réponses cliquables possibles --> 

<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Combien de parts mes amis ont-ils eues ?</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-81' style='padding: 10px;'>
   <label for='option-81' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='2/3' id='option-81' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        2/3</label>
        <span id='result-81'></span>
    </div>
    <hr/>
    
    <div id='block-82' style='padding: 10px;'>
    <label for='option-82' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='4' id='option-82' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        4</label>
        <span id='result-82'></span>
    </div>	
    <hr/>
     
    <div id='block-83' style='padding: 10px;'>
    <label for='option-83' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='9' id='option-83' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        9</label>
        <span id='result-83'></span>
    </div>
    <hr/>
     
    <div id='block-84' style='padding: 10px;'>
        <label for='option-84' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='8' id='option-84' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         8</label>
        <span id='result-84'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer8()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer8'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer8() {
    	if (document.getElementById('option-84').checked) {
      
        document.getElementById('block-84').style.border = '3px solid limegreen'
        document.getElementById('result-84').style.color = 'limegreen'
		document.getElementById('result-84').innerHTML = 'Correct !'
        
        } 
        if (document.getElementById('option-81').checked) {
        document.getElementById('block-81').style.border = '3px solid red'
        document.getElementById('result-81').style.color = 'red'
		document.getElementById('result-81').innerHTML = 'Incorrect !'
        showCorrectAnswer8()
 		}
        if (document.getElementById('option-82').checked) {
        document.getElementById('block-82').style.border = '3px solid red'
        document.getElementById('result-82').style.color = 'red'
		document.getElementById('result-82').innerHTML = 'Incorrect !'
        showCorrectAnswer8()	
        }
        if (document.getElementById('option-83').checked) {
        document.getElementById('block-83').style.border = '3px solid red'
        document.getElementById('result-83').style.color = 'red'
		document.getElementById('result-83').innerHTML = 'Incorrect !'
        showCorrectAnswer8() 	
        }
     }
    // la fonction affiche le lien vers la réponse correcte
    function showCorrectAnswer8() {
        	 let showAnswer8 = document.createElement('p')
             showAnswer8.innerHTML = 'Afficher la bonne réponse'
        showAnswer8.style.position = 'relative'
        showAnswer8.style.top = '-180px'
        showAnswer8.style.fontSize = '1.75rem'
             document.getElementById('showanswer8').appendChild(showAnswer8)
             showAnswer8.addEventListener('click', () => {
        	 document.getElementById('block-84').style.border = '3px solid limegreen'
        document.getElementById('result-84').style.color = 'limegreen'
		document.getElementById('result-84').innerHTML = 'Correct !'
        document.getElementById('showanswer8').removeChild(showAnswer8)    
         
        })
        }
</script>

Enfin, il y a un autre cas que je souhaite explorer. Que faire si nous savons ce qu'une fraction donnée d'un nombre équivaut et que nous devons trouver ce nombre ? 

Par exemple, nous savons que mes amis ont eu **8** parts du gâteau d'anniversaire et que cela représentait **2/3** du **gâteau entier**. Combien de parts le gâteau avait-il au début ? Pour trouver ce **nombre entier**, nous devons **diviser 8 par 2/3**, ce qui donne **12**. 

Résolvez la question suivante par vous-même. Une voiture de course a parcouru 900 mètres sur une piste, ce qui représente 3/5 de la distance totale. Quelle est la longueur de la piste de course ?  

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèles, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les IDs des éléments et les noms des fonctions ont dû être indexés.
 Affiche une question avec quatre réponses cliquables possibles --> 

<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Quelle est la longueur de la piste de course ?</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-91' style='padding: 10px;'>
   <label for='option-91' style='padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1200' id='option-91' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        1200 mètres</label>
        <span id='result-91'></span>
    </div>
    <hr/>
    
    <div id='block-92' style='padding: 10px;'>
    <label for='option-92' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1500' id='option-92' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        1500 mètres</label>
        <span id='result-92'></span>
    </div>	
    <hr/>
     
    <div id='block-93' style='padding: 10px;'>
    <label for='option-93' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='2700' id='option-93' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        2700 mètres</label>
        <span id='result-93'></span>
    </div>
    <hr/>
     
    <div id='block-94' style='padding: 10px;'>
        <label for='option-94' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='540' id='option-94' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        540 mètres</label>
        <span id='result-94'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer9()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer9'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer9() {
    	if (document.getElementById('option-92').checked) {
      
        document.getElementById('block-92').style.border = '3px solid limegreen'
        document.getElementById('result-92').style.color = 'limegreen'
		document.getElementById('result-92').innerHTML = 'Correct !'
        
        } 
        if (document.getElementById('option-91').checked) {
        document.getElementById('block-91').style.border = '3px solid red'
        document.getElementById('result-91').style.color = 'red'
		document.getElementById('result-91').innerHTML = 'Incorrect !'
        showCorrectAnswer9()
 		}
        if (document.getElementById('option-93').checked) {
        document.getElementById('block-93').style.border = '3px solid red'
        document.getElementById('result-93').style.color = 'red'
		document.getElementById('result-93').innerHTML = 'Incorrect !'
        showCorrectAnswer9()	
        }
        if (document.getElementById('option-94').checked) {
        document.getElementById('block-94').style.border = '3px solid red'
        document.getElementById('result-94').style.color = 'red'
		document.getElementById('result-94').innerHTML = 'Incorrect !'
        showCorrectAnswer9() 	
        }
     }
    // la fonction affiche le lien vers la réponse correcte
    function showCorrectAnswer9() {
        	 let showAnswer9 = document.createElement('p')
             showAnswer9.innerHTML = 'Afficher la bonne réponse'
        showAnswer9.style.position = 'relative'
        showAnswer9.style.top = '-180px'
        showAnswer9.style.fontSize = '1.75rem'
             document.getElementById('showanswer9').appendChild(showAnswer9)
             showAnswer9.addEventListener('click', () => {
        	 document.getElementById('block-92').style.border = '3px solid limegreen'
        document.getElementById('result-92').style.color = 'limegreen'
		document.getElementById('result-92').innerHTML = 'Correct !'
        document.getElementById('showanswer9').removeChild(showAnswer9)    
         
        })
        }
</script>