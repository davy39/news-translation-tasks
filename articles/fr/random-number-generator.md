---
title: 'Générateur de nombres aléatoires : Comment les ordinateurs génèrent-ils des
  nombres aléatoires ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-26T21:51:45.000Z'
originalURL: https://freecodecamp.org/news/random-number-generator
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9819740569d1a4ca1826.jpg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Computer Science
  slug: computer-science
- name: Math
  slug: math
seo_title: 'Générateur de nombres aléatoires : Comment les ordinateurs génèrent-ils
  des nombres aléatoires ?'
seo_desc: 'By Alexander Arobelidze

  People have been using random numbers for millennia, so the concept isn''t new.
  From the lottery in ancient Babylon, to roulette tables in Monte Carlo, to dice
  games in Vegas, the goal is to leave the end result up to random ch...'
---

Par Alexander Arobelidze

Les gens utilisent des **nombres** **aléatoires** depuis des millénaires, donc le concept n'est pas nouveau. Des loteries dans l'ancienne Babylone, aux tables de roulette à Monte Carlo, aux jeux de dés à Vegas, le but est de laisser le résultat final au hasard. 

Mais en dehors des jeux de hasard, l'**aléatoire** a de nombreuses utilisations en science, en statistique, en cryptographie et plus encore. Pourtant, l'utilisation de dés, de pièces de monnaie ou de médias similaires comme dispositif aléatoire a ses limites. 

En raison de la nature mécanique de ces techniques, la génération de grandes quantités de nombres aléatoires nécessite beaucoup de temps et de travail. Grâce à l'ingéniosité humaine, nous disposons d'outils et de méthodes plus puissants.

## Méthodes pour générer des nombres aléatoires

### Nombres vraiment aléatoires

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-145-opt.png)
_Image d'un dispositif de traitement analogique-entrée numérique-sortie. Photo par [Harrison Broadbent](https://unsplash.com/@harrisonbroadbent?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Considérons deux méthodes principales utilisées pour générer des nombres aléatoires. La **première méthode** est basée sur un processus physique et tire sa source d'aléatoire d'un phénomène physique qui est **supposé** **être aléatoire**. 

Un tel phénomène se produit en dehors de l'ordinateur. Il est mesuré et ajusté pour d'éventuels biais dus au processus de mesure. Les exemples incluent la désintégration radioactive, l'effet photoélectrique, le rayonnement de fond cosmique, le bruit atmosphérique (que nous utiliserons dans cet article), et plus encore. 

Ainsi, les nombres aléatoires générés sur la base de cette aléatoire sont dits être des nombres "**vraiment**" aléatoires. 

Techniquement, la partie matérielle se compose d'un dispositif qui convertit l'énergie d'une forme à une autre (par exemple, le rayonnement en un signal électrique), d'un amplificateur et d'un convertisseur analogique-numérique pour transformer la sortie en un nombre numérique.

## Qu'est-ce que les nombres pseudo-aléatoires ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-146-opt.png)
_Image de code informatique s'écoulant à travers un écran d'ordinateur. Photo par [Markus Spiske](https://unsplash.com/@markusspiske?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)._

En alternative aux nombres "vraiment" aléatoires, la **deuxième méthode** de génération de nombres aléatoires implique des algorithmes computationnels qui peuvent produire des résultats apparemment aléatoires.

Pourquoi apparemment aléatoires ? Parce que les résultats finaux obtenus sont en fait complètement déterminés par une valeur initiale également connue sous le nom de valeur **seed** ou **clé**. Par conséquent, si vous connaissiez la valeur de la clé et le fonctionnement de l'algorithme, vous pourriez reproduire ces résultats apparemment aléatoires.

Les générateurs de nombres aléatoires de ce type sont fréquemment appelés générateurs de **nombres pseudo-aléatoires** et, par conséquent, produisent des nombres pseudo-aléatoires. 

Même si ce type de générateur ne collecte généralement aucune donnée à partir de sources de randomisation naturellement présentes, une telle collecte de clés peut être rendue possible lorsque cela est nécessaire. 

Comparons quelques aspects des générateurs de nombres vraiment aléatoires ou **TRNG** et des générateurs de nombres pseudo-aléatoires ou **PRNG**. 

Les PRNG sont plus rapides que les TRNG. En raison de leur nature déterministe, ils sont utiles lorsque vous devez rejouer une séquence d'événements aléatoires. Cela aide beaucoup dans les tests de code, par exemple. 

D'autre part, les TRNG ne sont pas périodiques et fonctionnent mieux dans les rôles sensibles à la sécurité tels que le chiffrement. 

Une **période** est le nombre d'itérations qu'un PRNG effectue avant de commencer à se répéter. Ainsi, toutes choses étant égales par ailleurs, un PRNG avec une période plus longue nécessiterait plus de ressources informatiques pour être prédit et craqué.

## Exemple d'algorithme pour générateur de nombres pseudo-aléatoires

Un ordinateur exécute du code basé sur un ensemble de règles à suivre. Pour les PRNG en général, ces règles tournent autour des points suivants : 

1. **Accepter** un nombre initial, c'est-à-dire une seed ou une clé. 
2. **Appliquer** cette seed dans une séquence d'opérations mathématiques pour générer le résultat. Ce résultat est le nombre aléatoire.
3. **Utiliser** ce nombre aléatoire résultant comme seed pour l'itération suivante. 
4. **Répéter** le processus pour émuler l'aléatoire. 

Maintenant, regardons un exemple.

### Le générateur congruentiel linéaire

Ce générateur produit une série de nombres pseudo-aléatoires. Étant donné une seed initiale **X<sub>0</sub>** et des paramètres entiers **a** comme multiplicateur, **b** comme incrément, et **m** comme module, le générateur est défini par la relation linéaire : **X<sub>n</sub> ≡ (aX<sub>n-1</sub> + b)mod m**. Ou en utilisant une syntaxe plus adaptée à la programmation : **X<sub>n</sub> = (a * X<sub>n-1</sub> + b) % m**. 

Chacun de ces membres doit satisfaire les conditions suivantes : 

* **m > 0** (le module est positif), 
* **0 < a < m** (le multiplicateur est positif mais inférieur au module), 
* **0** ≤ **b < m** (l'incrément est non négatif mais inférieur au module), et 
* **0** ≤ **X<sub>0</sub> < m** (la seed est non négative mais inférieure au module). 

Créons une fonction JavaScript qui prend les valeurs initiales comme arguments et retourne un tableau de nombres aléatoires d'une longueur donnée : 

<pre>
	<code>
    // x0=seed; a=multiplicateur; b=incrément; m=module; n=longueur de tableau souhaitée; 
	const linearRandomGenerator = (x0, a, b, m, n) => {
        const results = []
        for (let i = 0; i < n; i++) {
        	x0 = (a * x0 + b) % m
            results.push(x0)
        }
        return results
    }
	</code>
</pre>

Le générateur congruentiel linéaire est l'un des plus anciens et des plus connus des algorithmes PRNG.

En ce qui concerne les algorithmes de génération de nombres aléatoires exécutables par des ordinateurs, ils remontent aux années 1940 et 1950 (la [méthode du carré médian](https://en.wikipedia.org/wiki/Middle-square_method) et le [générateur de Lehmer](https://en.wikipedia.org/wiki/Lehmer_random_number_generator), par exemple) et continuent d'être écrits aujourd'hui ([Xoroshiro128+](https://en.wikipedia.org/wiki/Xoroshiro128%2B), [Squares RNG](https://en.wikipedia.org/wiki/Counter-based_random_number_generator_(CBRNG)#Squares_RNG), et plus).

## Un exemple de générateur de nombres aléatoires

Lorsque j'ai décidé d'écrire cet article sur l'intégration d'un générateur de nombres aléatoires dans une page web, j'avais un choix à faire.

J'aurais pu utiliser la fonction **`Math.random()`** de JavaScript comme base et générer une sortie en nombres pseudo-aléatoires comme je l'ai fait dans des articles précédents (voir [Table de multiplication - Codez votre propre table de multiplication](https://www.freecodecamp.org/news/multiplication-chart-code-your-own-times-table-using-javascript/)).

Mais cet article lui-même traite de la génération de nombres aléatoires. J'ai donc décidé d'apprendre à collecter des données basées sur une "vraie" aléatoire et de partager ma découverte avec vous. 

Voici donc le générateur de nombres "vraiment" aléatoires. Définissez les paramètres et cliquez sur Générer.

<!-- Éléments HTML -->
<div 
     class='flex-container' 
     style='margin: 0; 
            width: 50%;
            display: flex;
            flex-direction: column;
            justify-content: space-around; 
            align-items: center;
            border-radius:3px;
            border: 1px solid rgba(0,0,0,0.06);
            box-shadow:10px 5px 15px 4px rgba(0,0,0,0.06);
            '
     >
     <div 
         class='row' 
         style='margin: 0 auto;
                background: #1c96b5;
                color: white;
                font-size: 2.5rem;
                font-weight: 600;
                width: 100%;
                height: 60px;
                display: flex; 
                justify-content: space-around;
                align-items: center;'
         >
    	
            Générateur de nombres vraiment aléatoires
     </div>
     <div 
         class='row' 
         style='margin: 0 auto;
                background: white;
                width: 100%;
                height: 60px;
                display: flex; 
                justify-content: space-around;
                align-items: center;'
         >
    	 <input style='margin: 0 auto;
                       border: 2px solid #eee;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);
                       border-radius:5px;
                       font-size: 2.5rem;
                       background: #fff;
                       width: inherit;
                       height: inherit;
                       margin: 0 auto;
                       color: #1c96b5;'
               	   type='number' 
               	   name='' 
                   id='minimum' 
                   required
                   placeholder='Valeur entière limite inférieure' 
         />
       
     </div>
      <div 
         class='row' 
         style='margin: 0 auto;
                background: white;
                width: 100%;
                height: 60px;
                display: flex; 
                justify-content: space-around;
                align-items: center;'
         >
    	 <input style='margin: 0 auto;
                       border: 2px solid #eee;
                       box-shadow:0 0 15px 4px rgba(0,0,0,0.06);
                       border-radius:5px;
                       font-size: 2.5rem;
                       background: #fff;
                       width: inherit;
                       height: inherit;
                       margin: 0 auto;
                       color: #1c96b5;'
               	   type='number' 
               	   name='' 
                   id='maximum' 
                   required
                   placeholder='Valeur entière limite supérieure' 
         />
       
     </div>
     <div 
         class='row' 
         style='margin: 0 auto;
                background: white;
                color: #1c96b5;
                font-size: 2.5rem;
                font-weight: 600;
                width: 100%;
                height: 60px;
                display: flex; 
                justify-content: space-evenly;
                align-items: center;'
      >
       <div>
             
                            <label for="binary">Binaire<label>
             
  					  <input 
                              type="radio" 
                              id="binary" 
                              name="base" 	                             						          value="binary" 
                              style='transform: scale(1.3);
                                     margin: 0 3px 0 3px;
                                     vertical-align: middle;'
                         />
                                <label for="decimal">Décimal</label>
             
  					  <input 
                              type="radio" 
                              id="decimal" 
                              name="base" 	                             						          value="decimal" 
                              checked='checked'
                              style='transform: scale(1.3);
                                     margin: 0 3px 0 3px; 
                                     vertical-align: middle;'
                         />
                                <label for="hexadecimal">Hexadécimal</label>
             
  					  <input 
                              type="radio" 
                              id="hexadecimal" 
                              name="base" 	                             						          value="hexadecimal" 
                              style='transform: scale(1.3);
                                     margin: 0 3px 0 3px; 
                                     vertical-align: middle;'
                         />
  						
					</div>
     </div>   
     <div 
         class='row' 
         style='margin: 0 auto;
                background: white;
                width: 100%;
                height: 60px;
                display: flex; 
                justify-content: space-around;
                align-items: center;'
      >
        <button 
               style='background: #1c96b5; 
                      font-size: 3rem;
                      width: inherit;
                      height: inherit;
                      margin: 0 auto;
                      font-weight: 600;
                      border-radius:5px;
                      color:#fff;'
                type='button'
                id='generate'
                onclick='handleGenerate()'
        >
             Générer
           <audio 
                  id='generateSound' 			                                               src='https://www.fesliyanstudios.com/play-mp3/6683'
           />
        </button>
    </div>  
    <div 
         class='row' 
         style='margin: 0 auto;
                background: white;
                color: #1c96b5;
                font-size: 3rem;
                font-weight: 600;
                width: 100%;
                height: 60px;
                display: flex; 
                justify-content: space-between;
                align-items: center;'
      >
       Résultat : 
            <span 
                  style='padding-right: 10px;
                         font-size: 3.2rem;
                         '
                  id='result'
            ></span>
     </div>   
     <div 
          class='row' 
          style='margin: 0 auto; 
                 width: 100%; 
                 height: 60px; 
                 font-size: 3rem;
                 display: flex; 
                 justify-content: space-around;
                 align-items: center;'
         id='prompter'
    >
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
    const generateButton = document.getElementById('generate');
    const generateSound = document.getElementById('generateSound');
    const minimum = document.getElementById('minimum');
    const maxumum = document.getElementById('maximum');
    const prompter = document.getElementById('prompter');
    const resultValue = document.getElementById('result')
    const binary = document.getElementById('binary')
    const decimal = document.getElementById('decimal')
    const hexadecimal = document.getElementById('hexadecimal')
	
	
   // Animation handling
    const handleActive = (button) => {
        generateSound.currentTime = 0
        generateSound.play()
    	button.style.backgroundColor = '#18809a'
        button.style.transform = 'scale(0.95)'
        setTimeout(() => {
			button.style.backgroundColor = '#1c96b5'
        	button.style.transform = 'scale(1.0)'
        	}, 100)
    }
    
  // Reset handling
   	const handleRestart = () => {
         minimum.value = "";
         maximum.value = ""
   };
  
  
  // Generates a random number within user indicated interval
   const getRandom = async (min, max, base) => {
   	  const response = await fetch("https://www.random.org/integers/?num=1&min=" + min + "&max=" + max + "&col=1&base=" + base + "&format=plain&rnd=new")
      return response.text()
   } 
   
  
  // Output handling
    const handleGenerate = () => {
    	handleActive(generateButton)
        const base = binary.checked ? 2 : decimal.checked ? 10 : 16
        if (!minimum.value || !maximum.value) {
            prompter.style.color = 'red' 
        	prompter.textContent = "Entrez les valeurs Min & Max"
        } else {
        	getRandom(minimum.value, maximum.value, base).then((data) => {
        		resultValue.textContent = data
        		prompter.textContent = ""    
        	}).catch((error) => {
        		resultValue.textContent = 'ERREUR'
        		prompter.textContent = 'Erreur de connexion. Impossible de générer';    
        	})
       		 handleRestart()
        }
        
   }
    
</script>

Le code récupère les données de l'une des API, grâce à [**Random.org**](https://www.random.org/). Cette ressource en ligne dispose d'une pléthore d'outils utiles et personnalisables et est accompagnée d'une excellente documentation. 

L'aléatoire provient du bruit atmosphérique. J'ai pu utiliser des fonctions asynchrones. C'est un énorme avantage pour l'avenir. La fonction principale ressemble à ceci :


	<pre>
    // Génère un nombre aléatoire dans l'intervalle indiqué par l'utilisateur
   	<code>const getRandom = async (min, max, base) => {</code>
   	<code>	const response = await </code><code>	fetch("https://www.random.org/integers/?num=1&min="+min+"</code>
   <code> &max="+max+"&col=1&base="+base+"&format=plain&rnd=new")</code>
        <code>  	return response.text() </code>
   	<code>}</code> 
    </pre>


Les paramètres qu'elle prend permettent à un utilisateur de personnaliser la sortie des nombres aléatoires. Par exemple, **min** et **max** vous permettent de définir des limites inférieure et supérieure sur la sortie générée. Et **base** détermine si la sortie est imprimée en binaire, décimal ou hexadécimal. 

Encore une fois, j'ai choisi cette configuration, mais il y en a beaucoup d'autres disponibles à la [source](https://www.random.org/). 

Lorsque vous cliquez sur le bouton Générer, la fonction `handleGenerate()` est appelée. Elle invoque à son tour la fonction asynchrone `getRandom()`, gère les erreurs et produit les résultats :

<pre>
	<code>
    // Gestion de la sortie
    const handleGenerate = () => {
    	handleActive(generateButton)
        const base = binary.checked ? 2 : decimal.checked ? 10 : 16
        if (!minimum.value || !maximum.value) {
            prompter.style.color = 'red' 
        	prompter.textContent = "Entrez les valeurs Min & Max"
        } else {
        	getRandom(minimum.value, maximum.value, base).then((data) => {
        		resultValue.textContent = data
        		prompter.textContent = ""    
        	}).catch((error) => {
        		resultValue.textContent = 'ERREUR'
        		prompter.textContent = 'Erreur de connexion. Impossible de générer';    
        	})
       		 handleRestart()
        }
        
   }
    </code>
</pre>

Le reste du code traite de la structure HTML, de l'apparence et du style. 

Le code est prêt à être intégré et utilisé dans cette page web. Je l'ai séparé en parties composantes et l'ai fourni avec des commentaires détaillés. Il peut être facilement modifié. Vous pouvez également modifier la fonctionnalité et les styles selon vos besoins.

Voici le lien vers le dépôt GitHub du code complet : [https://github.com/sandroarobeli/random-generator](https://github.com/sandroarobeli/random-generator)