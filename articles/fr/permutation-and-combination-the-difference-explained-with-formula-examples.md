---
title: 'Permutation et Combinaison : La Différence Expliquée avec des Exemples de
  Formules'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-23T17:34:42.000Z'
originalURL: https://freecodecamp.org/news/permutation-and-combination-the-difference-explained-with-formula-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b7e740569d1a4ca2c26.jpg
tags:
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
seo_title: 'Permutation et Combinaison : La Différence Expliquée avec des Exemples
  de Formules'
seo_desc: 'By Alexander Arobelidze

  Permutations and Combinations are super useful in so many applications – from Computer
  Programming to Probability Theory to Genetics.

  I''m going to introduce you to these two concepts side-by-side, so you can see how
  useful the...'
---

Par Alexander Arobelidze

Les permutations et les combinaisons sont super utiles dans de nombreuses applications – de la programmation informatique à la théorie des probabilités en passant par la génétique.

Je vais vous présenter ces deux concepts côte à côte, afin que vous puissiez voir à quel point ils sont utiles.

La différence clé entre ces deux concepts est l'ordre. Avec les **Permutations**, vous vous concentrez sur des **listes** d'éléments où leur ordre compte.

Par exemple, je suis né en **1977**. C'est le chiffre **1** suivi du chiffre **9**, suivi du chiffre **7**, suivi du chiffre **7**. Dans cet ordre particulier.

Si je change l'ordre en **7917** à la place, ce serait une année complètement différente. Ainsi, l'ordre **compte**.

Avec les **Combinations**, en revanche, l'accent est mis sur des **groupes** d'éléments où l'ordre n'a **pas** d'importance.

Comme ma tasse de café est une combinaison de **café**, **sucre** et **eau**. Peu importe l'ordre dans lequel j'ajoute ces ingrédients. Il pourrait tout aussi bien y avoir de l'**eau**, du **sucre** et du **café**, c'est toujours la même tasse de café. Ainsi, l'ordre n'a **pas** d'importance.

Maintenant, examinons de plus près ces concepts.

## Partie 1 : Permutations

### Permutations où la répétition est autorisée

Imaginez que vous avez un nouveau téléphone. En commençant à utiliser ce nouveau téléphone, à un moment donné, on vous demandera de configurer un mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-173.png)
_Image d'un écran de smartphone_

Le mot de passe doit être composé de **4** chiffres. N'importe quels 4 chiffres. Et ils peuvent être répétés.

Il y a **10** chiffres au total pour commencer. Ce sont : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Donc pour le premier chiffre de votre mot de passe, vous avez **10** choix.

Puisque vous pouvez utiliser le même chiffre à nouveau, le nombre de choix pour le deuxième chiffre de notre mot de passe sera **10** à nouveau ! Ainsi, en choisissant deux des chiffres du mot de passe jusqu'à présent, les permutations sont **10 fois 10**, ou **10 x 10 = 100** ou **10<sup>2</sup>**.

La même logique s'applique pour le troisième chiffre de votre mot de passe. Vous avez le choix parmi les mêmes 10 options. Cette fois, vous aurez **10 fois 10 fois 10**, ou **10 x 10 x 10 = 1,000** ou **10<sup>3</sup>** permutations.

Enfin, pour le quatrième chiffre du mot de passe et les mêmes 10 chiffres à choisir, nous obtenons **10 fois 10 fois 10 fois 10**, ou **10 x 10 x 10 x 10 = 10,000** ou **10<sup>4</sup>** permutations.

Comme vous l'avez probablement remarqué, vous aviez 4 choix à faire et vous avez multiplié 10 **quatre** fois (10 x 10 x 10 x 10) pour arriver à un nombre total de permutations (10,000). Si vous deviez choisir **3** chiffres pour votre mot de passe, vous multiplieriez 10 **trois** fois. Si **7**, vous le feriez **sept** fois, et ainsi de suite.

Mais la vie ne tourne pas autour des mots de passe avec des chiffres à choisir. Et si vous avez une fête d'anniversaire et que vous devez choisir **5** ballons de couleur parmi **20** couleurs différentes disponibles ?

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-175.png)
_image de ballons colorés_

Puisque vous avez 20 couleurs différentes à choisir et que vous pouvez choisir la même couleur à nouveau, pour chaque ballon vous avez **20** choix. Le premier ballon est **20**, le deuxième ballon est **20 fois 20**, ou **20 x 20 = 400** etc. Pour le cinquième ballon, vous obtenez **20 x 20 x 20 x 20 x 20 = 3,200,000** ou **20<sup>5</sup>** permutations.

Résumons avec la règle générale : lorsque l'ordre compte et que la répétition est autorisée, si **n** est le nombre de choses à choisir (ballons, chiffres, etc.), et que vous en choisissez **r** (5 ballons pour la fête, 4 chiffres pour le mot de passe, etc.), le nombre de permutations sera égal à **P = n<sup>r</sup>**.

### Permutations où la répétition n'est pas autorisée

Ensuite, considérons le cas où la **répétition n'est pas autorisée**. Comme exemple, nous allons examiner les planètes de notre système solaire.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-174.png)
_image des planètes du système solaire_

Combien de façons différentes pouvez-vous arranger ces **8** planètes ? Les planètes sont : **Mercure**, **Vénus**, **Terre**, **Mars**, **Jupiter**, **Saturne**, **Uranus** et **Neptune**. Après avoir choisi, disons, Mercure, vous ne pouvez plus la choisir à nouveau. Ainsi, vous devez réduire le nombre de choix disponibles chaque fois qu'une planète est choisie.

Le premier choix aura **8** possibilités. Le deuxième choix aura **8 moins 1 égale 7** possibilités, puis **6**, suivi de **5**, suivi de **4**, jusqu'à ce qu'il ne reste **1** planète dans la liste.

En suivant la logique du scénario précédent, le nombre total de permutations est : **P = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40,320**.

En d'autres termes, il s'agit d'un produit de l'entier 8 et de tous les entiers positifs en dessous. Ce produit est appelé **Factorielle** et est noté avec un point d'exclamation, comme ceci : **8!**

Le nombre de permutations est égal à **P = 8!** ou plus généralement **P = n!**

Et si vous ne devez arranger que, disons, **5** de ces **8** planètes au lieu de toutes ? Alors vous ne prenez que les **5 premières** étapes de notre méthode. À savoir, **P = 8 x 7 x 6 x 5 x 4 = 6,720** sera le nombre de façons dont vous pouvez arranger **5** planètes parmi **8**. 

Mais pourquoi s'arrêter ici ? Pourquoi ne pas appliquer notre logique pour aboutir à une formule plus générale ? Pour rendre la notation ci-dessus facile à retenir pour n'importe quels nombres d'objets, nous utiliserons un truc. Dans une fraction, multiplier à la fois le numérateur et le dénominateur par le même nombre (sauf zéro) n'affecte pas cette fraction. Ainsi :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Permutations1.png)
_P(n, r) = n! / (n - r)!_

Nombre de planètes à choisir **n = 8**, vous en choisissez **r = 5**. En substituant les nombres dans la formule ci-dessus, nous obtenons **P = 8! / (8 - 5)! = 8! / 3!**. Même chose que **8 x 7 x 6 x 5 x 4 = 6,720**. 

À partir de là, le résultat de l'exemple précédent peut être dérivé. Là, vous avez arrangé toutes les **8** des **8** planètes disponibles. En utilisant la nouvelle formule, **P = 8! / (8 - 8)! = 8! / 0!**. Puisque la factorielle de **zéro** est considérée comme **égale à 1**, **P = 8! / 1 = 8!.** Ou plus généralement :

**P = n! / (n - n)! = n! / 0! = n!**.  

Une notation courte et pratique souvent utilisée est : **P(n, r) = n! / (n - r)!** 

Se souvenir des formules est important. Mais ce qui est plus important pour résoudre les problèmes de la vie réelle est de savoir quelles formules utiliser dans chaque situation. La pratique aide.

Question éclair :

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèle, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les ID d'éléments et les noms de fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Le tournoi est en cours et six équipes sont en compétition. La première place obtient une médaille d'or et la deuxième place une médaille d'argent. Combien de façons distinctes les médailles peuvent-elles être attribuées à ces équipes ?</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-11' style='padding: 10px;'>
   <label for='option-11' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/24' id='option-11' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        30</label>
        <span id='result-11'></span>
    </div>
    <hr/>
    
    <div id='block-12' style='padding: 10px;'>
    <label for='option-12' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6' id='option-12' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        360</label>
        <span id='result-12'></span>
    </div>	
    <hr/>
     
    <div id='block-13' style='padding: 10px;'>
    <label for='option-13' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/3' id='option-13' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        720</label>
        <span id='result-13'></span>
    </div>
    <hr/>
     
    <div id='block-14' style='padding: 10px;'>
        <label for='option-14' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='1/6' id='option-14' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         15</label>
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
		document.getElementById('result-11').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-12').checked) {
        document.getElementById('block-12').style.border = '3px solid red'
        document.getElementById('result-12').style.color = 'red'
		document.getElementById('result-12').innerHTML = 'Incorrect!'
        showCorrectAnswer1()
 		}
        if (document.getElementById('option-13').checked) {
        document.getElementById('block-13').style.border = '3px solid red'
        document.getElementById('result-13').style.color = 'red'
		document.getElementById('result-13').innerHTML = 'Incorrect!'
        showCorrectAnswer1()	
        }
        if (document.getElementById('option-14').checked) {
        document.getElementById('block-14').style.border = '3px solid red'
        document.getElementById('result-14').style.color = 'red'
		document.getElementById('result-14').innerHTML = 'Incorrect!'
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
		document.getElementById('result-11').innerHTML = 'Correct!'
        document.getElementById('showanswer1').removeChild(showAnswer1)    
         
        })
        }
</script>

Explication : vous avez **6** équipes à choisir. Ainsi **n = 6**. L'or et l'argent ensemble vous donnent **2** médailles à attribuer. Ainsi **r = 2**. En substituant ces nombres dans votre formule, nous obtenons **P(6, 2) = 6! / (6 - 2)! = 6! / 4! = 6 x 5 = 30**. 

## Partie 2 : Combinaisons

### Combinaisons sans répétition

Pour rendre la comparaison plus vivante, revisitons notre exemple de sélection de planètes. Et si vous voulez savoir quelles planètes sont choisies et **non** leur ordre d'apparition ?

Là, vous aviez 6 720 façons distinctes d'arranger 5 des 8 planètes. Mais puisque l'ordre d'apparition n'a **pas** d'importance maintenant, beaucoup de ces façons sont **redondantes**. Elles sont les mêmes pour nous.

Un **groupe** de Vénus, Terre, Mars, Jupiter, Saturne est le même **groupe** que Mars, Jupiter, Vénus, Terre, Saturne et le **groupe** que Saturne, Mars, Terre, Jupiter, Vénus. Ce sont simplement des séquences différentes des mêmes 5 planètes.

Combien de groupes avez-vous qui sont les mêmes ? Si vous choisissez **r** planètes par groupe, vous obtenez **r!** groupes. Pour **r = 5**, vous obtenez **r! = 5! = 120** groupes.

Ainsi, pour éliminer les groupes inutiles qui sont les mêmes, vous divisez le nombre original de **6 720** Permutations par **5!**. Le résultat est 6 720 / 120 = **56**. 

Pour généraliser, afin d'arriver au nombre de **Combinaisons**, vous devez déterminer toutes les **Permutations** et diviser par toutes les **Redondances**.

En utilisant une notation courte et pratique : **C(n, r) = P(n, r) / r! = n! / (r!(n - r)!)**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Permutations2.png)
_C(n, r) = n! / (r!(n - r)!)_

Et cela suppose que l'ordre n'a **pas** d'importance et qu'il n'y a **pas** de répétitions (c'est-à-dire qu'il n'y a qu'une seule Jupiter à choisir).

Revisitons l'exemple du tournoi :

<!-- Code pour les questions à choix multiples et l'évaluation des réponses
 L'éditeur ne supporte pas les chaînes de modèle, donc la fonctionnalité a dû être codée en dur. Puisque chaque bloc question-réponse fait toujours partie d'une seule instance de code HTML, les ID d'éléments et les noms de fonctions ont dû être indexés.

Affiche une question avec quatre réponses cliquables possibles -->
<div style='transform: scale(0.65); position: relative; top: -100px;'>
<h3>Le tournoi est en cours et six équipes sont en compétition. La première place obtient une médaille d'or et la deuxième place une médaille d'argent. Combien de groupes de gagnants de médailles sont possibles ? L'ordre des équipes n'a pas d'importance</h3>	
    <p>Choisissez 1 réponse</p>
    <hr/>
   
    <div id='block-21' style='padding: 10px;'>
   <label for='option-21' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6/24' id='option-21' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 
        360</label>
        <span id='result-21'></span>
    </div>
    <hr/>
    
    <div id='block-22' style='padding: 10px;'>
    <label for='option-22' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='6' id='option-22' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        15</label>
        <span id='result-22'></span>
    </div>	
    <hr/>
     
    <div id='block-23' style='padding: 10px;'>
    <label for='option-23' style=' padding: 5px; font-size: 2.5rem;'>
        <input type='radio' name='option' value='1/3' id='option-23' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
        30</label>
        <span id='result-23'></span>
    </div>
    <hr/>
     
    <div id='block-24' style='padding: 10px;'>
        <label for='option-24' style=' padding: 5px; font-size: 2.5rem;'>
         <input type='radio' name='option' value='1/6' id='option-24' style='transform: scale(1.6); margin-right: 10px; vertical-align: middle; margin-top: -2px;' /> 				
         720</label>
        <span id='result-24'></span>
    </div>
    <hr/>
    <button type='button' onclick='displayAnswer2()' style='width: 100px; height: 40px; border-radius: 3px; background-color: lightblue; font-weight: 700;'>Soumettre</button>
</div>
<a id='showanswer2'></a>
<script>
    
 //    La fonction évalue la réponse et affiche le résultat
	function displayAnswer2() {
    	if (document.getElementById('option-22').checked) {
      
        document.getElementById('block-22').style.border = '3px solid limegreen'
        document.getElementById('result-22').style.color = 'limegreen'
		document.getElementById('result-22').innerHTML = 'Correct!'
        
        } 
        if (document.getElementById('option-21').checked) {
        document.getElementById('block-21').style.border = '3px solid red'
        document.getElementById('result-21').style.color = 'red'
		document.getElementById('result-21').innerHTML = 'Incorrect!'
        showCorrectAnswer2()
 		}
        if (document.getElementById('option-23').checked) {
        document.getElementById('block-23').style.border = '3px solid red'
        document.getElementById('result-23').style.color = 'red'
		document.getElementById('result-23').innerHTML = 'Incorrect!'
        showCorrectAnswer2()	
        }
        if (document.getElementById('option-24').checked) {
        document.getElementById('block-24').style.border = '3px solid red'
        document.getElementById('result-24').style.color = 'red'
		document.getElementById('result-24').innerHTML = 'Incorrect!'
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
        	 document.getElementById('block-22').style.border = '3px solid limegreen'
        document.getElementById('result-22').style.color = 'limegreen'
		document.getElementById('result-22').innerHTML = 'Correct!'
        document.getElementById('showanswer2').removeChild(showAnswer2)    
         
        })
        }
</script>

Comme avant, vous avez **6** équipes. Ainsi, **n = 6**. Il y a deux médailles attribuées, donc **r = 2**. Cependant, cette fois, cela n'a **pas** d'importance qui gagne l'or et qui gagne l'argent. L'équipe d'or et l'équipe d'argent est la même que l'équipe d'argent et l'équipe d'or. En substituant ces nombres dans votre formule, nous obtenons **C(6, 2) = 6! / (2!(6 - 2)!) = 6! / 2! 4! = 15**.

### Combinaisons avec répétition

Pour compléter cet article, il y a un cas qui nécessite une attention particulière. Jusqu'à présent, dans nos combinaisons, nous avons supposé qu'il n'y avait pas de répétition. Aucun des deux éléments n'était identique.

Et si nous **pouvons** avoir des répétitions ? Et si, comme dans notre exemple précédent, nous pouvons choisir plus d'un ballon de la même couleur ? Si le nombre de ballons à choisir est **n** et que nous en choisissons **r** tout en **autorisant** les mêmes couleurs et en **ignorant** l'ordre de disposition, nous aboutirons à **(n + r - 1)! / (r!(n - 1)!) Combinaisons**.

Ainsi, pour résumer, voici un tableau que vous pouvez utiliser pour référencer ces concepts et leurs formules.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Permutations3.png)
_Tableau des formules pour les Permutations et les Combinaisons_

J'espère que cet article vous a aidé à mieux comprendre ces deux concepts mathématiques importants. Merci d'avoir lu.