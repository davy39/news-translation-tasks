---
title: Graphique du cercle unité et calculatrice trigonométrique – Cos 0, Sin 0, Tan
  0, Radians et plus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T16:06:31.000Z'
originalURL: https://freecodecamp.org/news/unit-circle-chart-and-trig-calculator
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98d8740569d1a4ca1c60.jpg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: calculus
  slug: calculus
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
seo_title: Graphique du cercle unité et calculatrice trigonométrique – Cos 0, Sin
  0, Tan 0, Radians et plus
seo_desc: "By Alexander Arobelidze\nThe unit circle is a useful visualization tool\
  \ for learning about trigonometric functions. \nThe key to its usefulness is its\
  \ simplicity. It removes the need for memorizing different values and allows the\
  \ user to simply derive ..."
---

Par Alexander Arobelidze

Le **cercle unité** est un outil de visualisation utile pour apprendre les fonctions trigonométriques. 

La clé de son utilité réside dans sa simplicité. Il élimine le besoin de mémoriser différentes valeurs et permet à l'utilisateur de simplement dériver différents résultats pour différents cas. 

Apprenons-en plus à ce sujet et testons notre compréhension avec une calculatrice trigonométrique pratique que j'ai créée à la fin de l'article.

## Partie 1. Qu'est-ce que le cercle unité et comment est-il utilisé ?

Le cercle unité est un cercle avec un rayon d'**une** unité dont le centre est placé à l'origine. En d'autres termes, le centre est placé sur un graphique où les axes **X** et **Y** se croisent. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle1-1.png)
_**Fig 1**. Le graphique du cercle unité avec un rayon = 1 et les points d'intersection avec les axes X et Y_

Avoir un rayon égal à 1 unité nous permettra de créer des **triangles de référence** avec une hypotenuse égale à 1 unité. 

Comme nous le verrons bientôt, cela nous permet de mesurer directement le **sinus**, le **cosinus** et la **tangente**. Le triangle ci-dessous nous rappelle comment nous définissons le sinus et le cosinus pour un angle **alpha**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle2.png)
_**Fig 2**. Définition géométrique du sinus et du cosinus pour un angle avec une hypotenuse égale à 1_

Puisque l'hypotenuse est égale à 1 et que tout ce qui est divisé par 1 est égal à lui-même, le sinus de alpha est égal à la longueur de BC. Ou **sin(α) = BC/1 = BC**. 

De même, le cosinus sera égal à la longueur de AC. Ou **cos(α) = AC/1 = AC**. 

Ensuite, déplaçons ce triangle dans notre cercle unité, afin que le rayon du cercle puisse servir d'hypotenuse.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle3.png)
_**Fig 3**. Triangle de référence à l'intérieur du cercle unité. La coordonnée x = cos(α) et la coordonnée y = sin(α)_

Par conséquent, la coordonnée **y** du point où le triangle touche le cercle est égale à sin(α), ou **y = sin(α)**. De même, la coordonnée **x** sera égale à cos(α), ou **x = cos(α)**. 

Ainsi, en se déplaçant autour du cercle et en changeant l'angle, nous pouvons mesurer le sinus et le cosinus de cet angle en mesurant les coordonnées y et x respectivement. 

Les angles peuvent être mesurés en **degrés** et/ou en **radians**. Le point avec les coordonnées (1, 0) correspond à **0** degrés (voir Fig 1). La mesure augmente dans le sens inverse des aiguilles d'une montre, donc le point avec les coordonnées (0, 1) correspondra à **90** degrés. Un cercle complet – **360** degrés. 

## Partie 2. Angles importants et leurs valeurs correspondantes de sinus, cosinus et tangente

Puisqu'il est logique de commencer à 0 degré, notre cercle ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle4.png)
_**Fig 4**. Cercle unité montrant cos(0) = 1 et sin(0) = 0_

Parce que la **tangente** est égale au sinus divisé par le cosinus, **tan(0) = sin(0) / cos(0) = 0 / 1 = 0**. 

Ensuite, voyons ce qui se passe à 90 degrés. Les coordonnées du point correspondant sont (0, 1). Ainsi, sin(90) = y = 1 et cos(90) = x = 0. Le cercle ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle5.png)
_**Fig 5**. Cercle unité montrant cos(90) = 0 et sin(90) = 1_

Qu'en est-il de la tangente(90) ? Lorsque la mesure du cosinus approche 0, et qu'il s'avère être un dénominateur dans une fraction, la valeur de cette fraction augmente jusqu'à l'infini. Par conséquent, **tan(90) est dit indéfini**. 

Maintenant, la question que vous pourriez poser : lorsque le sinus passe de 0 à 1 tandis que le cosinus passe de 1 à 0, s'égalisent-ils jamais ? La réponse est oui, et cela se produit exactement à mi-chemin à 45 degrés ! Le cercle ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle6.png)
_**Fig 6**. Cercle unité montrant sin(45) = cos(45) = 1 / √2_

En raison du fait que le numérateur est le même que le dénominateur, **tan(45) = 1**. 

Enfin, le cercle unité de référence général. Il reflète à la fois les valeurs positives et négatives pour les axes X et Y et montre les valeurs importantes que vous devriez retenir.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/unitCircle7.png)
_**Fig 7**. Cercle unité montrant les valeurs importantes de sinus et de cosinus à retenir_

En guise de note finale pour cette section, il est toujours utile de se souvenir de l'identité trigonométrique suivante basée sur le [théorème de Pythagore](https://en.wikipedia.org/wiki/Pythagorean_theorem) : sin²(α) + cos²(α) = 1. 

## Partie 3. Calculatrice trigonométrique

En tant qu'outil de pratique utile, j'ai ajouté une calculatrice trigonométrique simple. Elle prend des entrées pour les mesures d'angles et fournit les valeurs correspondantes pour les fonctions **sinus**, **cosinus** et **tangente**. 

Vous pouvez choisir les **degrés** ou les **radians** comme mesure d'angle. Chacun a ses avantages et ses inconvénients. Pour les relations quantitatives, puisque **π** radians **=** 180°, **1 radian** serait 180°/**π** ou environ **57°**. Il peut être calculé avec la précision souhaitée.   

Le code de la calculatrice contient une interactivité de base et une gestion des erreurs dans les limites de l'éditeur. Ses blocs de construction sont marqués et commentés afin que toute personne souhaitant le modifier puisse le faire facilement. 

Par exemple, de nouvelles fonctions telles que **ctg**, **sec** et ainsi de suite peuvent être ajoutées ainsi que différents schémas de couleurs et bien plus encore. Le code source complet peut être consulté en [cliquant ici](https://github.com/sandroarobeli/TrigCalculator/blob/master/TrigCalculator.txt).

<!-- Éléments HTML -->
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
    	<h3 
            style='color: #1c96b5;
                   text-align: center;'
         >
            Entrez la mesure en degrés ou en radians et cliquez sur Soumettre
        </h3>
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
            <input style='margin: 0 auto;
                      	  border: 2px solid #eee;
                          box-shadow:0 0 15px 4px rgba(0,0,0,0.06);
                          border-radius:5px;
                          font-size: 2.3rem;
                          background: #fff;
                          width: 250px;
                          height: 60px;
                          margin: 0 auto;
                          color: #1c96b5;'
               	   type='number' 
               	   name='' 
                   id='currentMeasure' 
                   placeholder='Entrez la mesure ici' 
         	/>
        </div>
    	<div 
             style='width: 250px; 
                    height: 60px;'
         >
             <div
                  style='display: flex;
                		 justify-content: space-around; 
                		 align-items: center;
                         background:#fff; 
                   	     font-size: 2.3rem;
                         height: 60px;
                         line-height: 60px;
                         margin: 0 auto;
                         color: #1c96b5;
                         border-radius:5px;
                         border: 2px solid #eee;
                         box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
                  >
             		<div>
  						<input 
                               type="radio" 
                               id="degree" 
                               name="measure" 	                             								value="degree" 
                               checked='checked'
                               style='transform: scale(1.5); 
                                      margin-right: 3px; 
                                      vertical-align: middle;'
                         />
  						<label for="degree">
                            Degré
                        </label>
					</div>
					<div>
  						<input 
                               type="radio" 
                               id="radian" 
                               name="measure" 															   value="radian" 
                               style='transform: scale(1.5); 
                                      margin-right: 3px; 
                                      vertical-align: middle;'
                         />
  						 <label for="radian">
                             Radian
                         </label>
					</div>
             </div>
         </div>
         <div 
              style='width: 250px; 
                     height: 60px;'
              >
         	<button 
                    style='background: #1c96b5; 
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
        	>
                Soumettre
                	<audio 
                      id='submitSound' 			                                                   src='https://www.fesliyanstudios.com/play-mp3/6683'
                    />
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
        	<h3 
                style='background:#fff; 
                       font-size: 3rem;
                       height: 60px;
                       line-height: 60px;
                       margin: 0;
                       text-align: start;
                       padding-left: 30px;
                       color: #1c96b5;
                       border-radius:5px;
                       border: 2px solid #1c96b5;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
            	id=''
           >
                SIN: 
                	<span 
                          id='sin'
                    ></span>
            </h3>
        </div>
        <div 
             style='width: 250px; 
                    height: 60px;'
        >
        	<h3 
                style='background:#fff; 
                       font-size: 3rem;
                       height: 60px;
                       line-height: 60px;
                       margin: 0;
                       text-align: start;
                       padding-left: 30px;
                       color: #1c96b5;
                       border-radius:5px;
                       border: 2px solid #1c96b5;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
                id=''
         >
                COS: 
                	<span 
                          id='cos'
                    ></span>
            </h3>
        </div>
        <div 
             style='width: 250px;
                    height: 60px;'
         >
        	<h3 
                style='background:#fff; 
                       font-size: 3rem;
                       height: 60px;
                       line-height: 60px;
                       margin: 0;
                       text-align: start;
                       padding-left: 30px;
                       color: #1c96b5;
                       border-radius:5px;
                       border: 2px solid #1c96b5;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);'
                       id=''
         	>
                TAN: 
                	<span 
                          id='tan'
                    ></span>
            </h3>
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
    	<h3 
            style='background:#fff; 
                   font-size: 3rem;
                   height: 60px;
                   line-height: 60px;
                   margin: 0;
                   text-align: center;
                   color: #1c96b5;
                   border-radius:5px;
                   border: 2px solid #eee;
                   box-shadow:0 0 15px 4px rgba(0,0,0,0.06)'
        	id='prompter'
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
    // Déclaration des éléments
    const submitButton = document.getElementById('submit');
    const submitSound = document.getElementById('submitSound');
    const currentMeasure = document.getElementById('currentMeasure');
    const prompter = document.getElementById('prompter');
    const degreeInput = document.getElementById('degree')
    const radianInput = document.getElementById('radian')
    const sinValue = document.getElementById('sin')
    const cosValue = document.getElementById('cos')
    const tanValue = document.getElementById('tan')
	
	
   // Gestion de l'animation
    const handleActive = (button) => {
        submitSound.currentTime = 0
        submitSound.play()
    	button.style.backgroundColor = '#18809a'
        button.style.transform = 'scale(0.95)'
        setTimeout(() => {
			button.style.backgroundColor = '#1c96b5'
        	button.style.transform = 'scale(1.0)'
        	}, 100)
    }
    
  // Gestion de la réinitialisation
   	const handleRestart = () => {
         if (currentMeasure.value === '' || !/^(\d*\.)?\d+$/.test(currentMeasure.value.toString())) {
         	currentMeasure.style.background = '#f99996'
            prompter.style.color = 'red' 
         } else {
         	currentMeasure.value = ''  
            currentMeasure.style.background = 'white'
          	prompter.textContent = ''  
         }
   };
  
  
  // Calculatrices pour sin, cosinus et tan
   const calculateSin = (degree, measure) => {
  	 if (degree) {
        return measure % 180 === 0 ? '0.000' : Math.sin(measure * (Math.PI / 180)).toPrecision(4)
        } else {
    	return Math.sin(measure).toPrecision(4)
    }
  }
  
  const calculateCos = (degree, measure) => {
  	if (degree) {
       return measure % 180 !== 0 && measure % 90 === 0 ? '0.000' : Math.cos(measure * (Math.PI / 180)).toPrecision(4)
     } else {
    	return Math.cos(measure).toPrecision(4)
     }
  }
  
  const calculateTan = (degree, measure) => {
	if (degree) {
    	if (measure % 180 !== 0 && measure % 90 === 0) {
        	return 'Infinity'
        } else {
        	return (calculateSin(true, measure) / calculateCos(true, measure)).toPrecision(4)
        }
    } else {
       if (measure % Math.PI !== 0 && measure % (Math.PI / 2) === 0) {
       		return 'Infinity'
       } else {
       		return (calculateSin(false, measure) / calculateCos(false, measure)).toPrecision(4)
       }
    }
}
  
  
  // Gestion de la sortie
    const handleSubmit = () => {
    	handleActive(submitButton)
        if (currentMeasure.value === '' || !/^(\d*\.)?\d+$/.test(currentMeasure.value.toString())) {
            sinValue.innerText = ''
            cosValue.innerText = ''
            tanValue.innerText = ''
			prompter.textContent = 'Veuillez entrer la mesure de l\'angle et appuyer sur Soumettre';
        } else {
     		if (degreeInput.checked) {
            	sinValue.innerText = calculateSin(true, currentMeasure.value)
                cosValue.innerText = calculateCos(true, currentMeasure.value) 
                tanValue.innerText = calculateTan(true, currentMeasure.value)
            	} else {
            		sinValue.innerText = calculateSin(false, currentMeasure.value)
                	cosValue.innerText = calculateCos(false, currentMeasure.value)
                	tanValue.innerText = calculateTan(false, currentMeasure.value)
               }
   		}
        handleRestart()
   }
</script>

J'espère que l'article, ainsi que le code source de la calculatrice, vous seront bénéfiques. J'ai hâte de voir ses modifications bientôt.