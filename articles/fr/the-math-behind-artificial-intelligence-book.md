---
title: 'Les Mathématiques Derrière l''Intelligence Artificielle : Un Guide des Fondements
  de l''IA [Livre Complet]'
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2026-01-06T23:14:23.200Z'
originalURL: https://freecodecamp.org/news/the-math-behind-artificial-intelligence-book
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767723634484/4748bd8a-26a1-4d9c-89c3-1a6d07bde69e.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Mathematics
  slug: mathematics
- name: book
  slug: book
- name: MathJax
  slug: mathjax
seo_title: 'Les Mathématiques Derrière l''Intelligence Artificielle : Un Guide des
  Fondements de l''IA [Livre Complet]'
seo_desc: '"To understand is to perceive patterns." - Isaiah Berlin


  This is not a math book filled with complex formulas, theorems, and concepts that
  are hard to grasp.

  Instead, it’s a detailed guide where we’ll break complex ideas down into simpler
  terms.

  Eve...'
---

> "Comprendre, c'est percevoir des motifs." - Isaiah Berlin

Ce n'est **pas** un livre de mathématiques rempli de formules complexes, de théorèmes et de concepts difficiles à saisir.

Au lieu de cela, c'est un guide détaillé où nous décomposerons les idées complexes en termes plus simples.

Même si vous n'avez qu'une compréhension générale de l'algèbre, vous devriez pouvoir suivre facilement.

### Voici ce que nous allons couvrir :
* [Chapitre 1 : Contexte de ce livre](#heading-chapitre-1-contexte-de-ce-livre)
    
    * [L'objectif ici](#heading-lobjectif-ici)
        
    * [Pourquoi ce livre sur l'IA est-il différent ?](#heading-pourquoi-ce-livre-sur-lia-est-il-different)
        
    * [Permettez-moi de me présenter](#heading-permettez-moi-de-me-presenter)
        
    * [Prérequis](#heading-prerequis)
        
* [Chapitre 2 : L'architecture des mathématiques](#heading-chapitre-2-larchitecture-des-mathematiques)
    
    * [L'arbre des mathématiques : comment tout est connecté](#heading-larbre-des-mathematiques-comment-tout-est-connecte)
        
    * [Une brève histoire des mathématiques : du comptage à l'infini](#heading-une-breve-histoire-des-mathematiques-du-comptage-a-linfini)
        
    * [Les fondements de la relativité : comment Einstein a utilisé les mathématiques pour comprendre l'espace et le temps](#heading-les-fondements-de-la-relativite-comment-einstein-a-utilise-les-mathematiques-pour-comprendre-lespace-et-le-temps)
        
    * [Le plus grand paradoxe de Gödel : les mathématiques peuvent-elles s'expliquer elles-mêmes ?](#heading-le-plus-grand-paradoxe-de-godel-les-mathematiques-peuvent-elles-sexpliquer-elles-memes)
        
    * [Qu'en est-il des mathématiques appliquées et de l'ingénierie ?](#heading-quen-est-il-des-mathematiques-appliquees-et-de-lingenierie)
        
    * [Exemples de code : Approches analytiques et numériques](#heading-exemples-de-code-approches-analytiques-et-numeriques)
        
        * [Exemple 1 : Résoudre un problème de manière analytique](#heading-exemple-1-resoudre-un-probleme-de-maniere-analytique)
            
        * [Exemple 2 : Résoudre numériquement (Approximation)](#heading-exemple-2-resoudre-numeriquement-approximation)
            
        * [Pourquoi ces deux approches sont importantes](#heading-pourquoi-ces-deux-approches-sont-importantes)
            
    * [L'impact d'une théorie unifiée des mathématiques](#heading-limpact-dune-theorie-unifiee-des-mathematiques)
        
        * [Quelle est la valeur de cette grande unification pour la société ?](#heading-quelle-est-la-valeur-de-cette-grande-unification-pour-la-societe)
            
    * [Une leçon finale de l'histoire](#heading-une-lecon-finale-de-lhistoire)
        
* [Chapitre 3 : Le domaine de l'intelligence artificielle](#heading-chapitre-3-le-domaine-de-lintelligence-artificielle)
    
    * [Qu'est-ce que l'intelligence artificielle ?](#heading-quest-ce-que-lintelligence-artificielle)
        
        * [L'intelligence artificielle générale n'est pas encore là](#heading-lintelligence-artificielle-generale-nest-pas-encore-la)
            
    * [IA symbolique vs. IA non symbolique : Quelle est la différence ?](#heading-ia-symbolique-vs-ia-non-symbolique-quelle-est-la-difference)
        
        * [Qu'est-ce que l'IA symbolique ?](#heading-quest-ce-que-lia-symbolique)
            
        * [Qu'est-ce que l'IA non symbolique ?](#heading-quest-ce-que-lia-non-symbolique)
            
    * [Avant l'IA : La Théorie du Contrôle comme la "Première IA"](#heading-avant-lia-la-theorie-du-controle-comme-la-premiere-ia)
        
* [Chapitre 4 : Algèbre Linéaire - La Géométrie des Données](#heading-chapitre-4-algebre-lineaire-la-geometrie-des-donnees)
    
    * [Que sont les Matrices et Pourquoi Simplifient-elles les Équations ?](#heading-que-sont-les-matrices-et-pourquoi-simplifient-elles-les-equations)
        
    * [Vecteurs et Transformations : Se Déplacer dans Plusieurs Directions](#heading-vecteurs-et-transformations-se-deplacer-dans-plusieurs-directions)
        
    * [Indépendance Linéaire, Dépendance et Rang : Pourquoi C'est Important](#heading-independance-lineaire-dependance-et-rang-pourquoi-cest-important)
        
        * [Pourquoi ces concepts sont-ils importants ?](#heading-pourquoi-ces-concepts-sont-ils-importants)
            
    * [Déterminants : Mesurer l'Espace et la Mise à l'Échelle](#heading-determinants-mesurer-lespace-et-la-mise-a-lechelle)
        
        * [Le même calcul fonctionne pour d'autres matrices !](#heading-le-meme-calcul-fonctionne-pour-dautres-matrices)
            
    * [Que sont les espaces mathématiques et comment simplifient-ils les calculs ?](#heading-que-sont-les-espaces-mathematiques-et-comment-simplifient-ils-les-calculs)
        
    * [Valeurs propres et vecteurs propres : Déverrouiller des motifs cachés](#heading-valeurs-propres-et-vecteurs-propres-deverrouiller-des-motifs-caches)
        
    * [Applications de l'algèbre linéaire en IA et en théorie du contrôle](#heading-applications-de-lalgebre-lineaire-en-ia-et-en-theorie-du-controle)
        
* [Chapitre 5 : Calcul multivariable – Changement dans de nombreuses directions](#heading-chapitre-5-calcul-multivariable-changement-dans-de-nombreuses-directions)
    
    * [Limites et continuité : Comprendre le changement fluide](#heading-limites-et-continuite-comprendre-le-changement-fluide)
        
        * [Qu'est-ce que la continuité ?](#heading-quest-ce-que-la-continuite)
            
        * [Comment les limites garantissent-elles la continuité ?](#heading-comment-les-limites-garantissent-elles-la-continuite)
            
    * [Pourquoi les limites sont-elles importantes pour comprendre les dérivées et les intégrales ?](#heading-pourquoi-les-limites-sont-elles-importantes-pour-comprendre-les-derivees-et-les-integrales)
        
    * [Dérivées : Comment les choses changent et à quelle vitesse](#heading-derivees-comment-les-choses-changent-et-a-quelle-vitesse)
        
        * [Où et pourquoi les dérivées sont-elles si importantes ?](#heading-ou-et-pourquoi-les-derivees-sont-elles-si-importantes)
            
    * [Qu'en est-il du calcul intégral ?](#heading-quen-est-il-du-calcul-integral)
        
        * [Où et comment cela est-il appliqué ?](#heading-ou-et-comment-cela-est-il-applique)
            
    * [Applications en IA et théorie du contrôle : le calcul en action](#heading-applications-en-ia-et-theorie-du-controle-le-calcul-en-action)
        
* [Chapitre 6 : Probabilité & Statistiques - Apprendre de l'incertitude](#heading-chapitre-6-probabilite-amp-statistiques-apprendre-de-lincertitude)
    
    * [Moyenne, Médiane, Mode : Mesurer la tendance centrale](#heading-moyenne-mediane-mode-mesurer-la-tendance-centrale)
        
        * [1. Quelle est la moyenne du rendement pendant une année d'activité ?](#heading-1-quelle-est-la-moyenne-du-rendement-pendant-une-annee-dactivite)
            
        * [2. Quel est le mode de l'engrais utilisé ?](#heading-2-quel-est-le-mode-de-lengrais-utilise)
            
        * [3. Quelle est la médiane du rendement](#heading-3-quelle-est-la-mediane-du-rendement)
            
    * [Variance et écart-type : Mesurer la dispersion](#heading-variance-et-ecart-type-mesurer-la-dispersion)
        
    * [Qu'est-ce que la distribution normale ? La courbe en cloche de la vie](#heading-quest-ce-que-la-distribution-normale-la-courbe-en-cloche-de-la-vie)
        
    * [Comment le théorème central limite aide à approximer le monde](#heading-comment-le-theoreme-central-limite-aide-a-approximer-le-monde)
        
        * [Et pourquoi est-ce important ?](#heading-et-pourquoi-est-ce-important)
            
    * [Théorème de Bayes : Apprendre à partir des preuves](#heading-theoreme-de-bayes-apprendre-a-partir-des-preuves)
        
        * [Qu'est-ce que la probabilité conditionnelle ?](#heading-quest-ce-que-la-probabilite-conditionnelle)
            
        * [Théorème de Bayes](#heading-theoreme-de-bayes)
            
        * [Où cela est-il appliqué dans la vie réelle ?](#heading-ou-cela-est-il-applique-dans-la-vie-reelle)
            
    * [Que sont les modèles de Markov ? Prédire la prochaine étape, une étape à la fois](#heading-que-sont-les-modeles-de-markov-predire-la-prochaine-etape-une-etape-a-la-fois)
        
        * [Analogie de la chaîne de Markov](#heading-analogie-de-la-chaine-de-markov)
            
        * [Chaîne de Markov expliquée en anglais simple](#heading-chaine-de-markov-expliquee-en-anglais-simple)
            
        * [Applications des chaînes de Markov](#heading-applications-des-chaines-de-markov)
            
        * [Types de chaînes de Markov](#heading-types-de-chaines-de-markov)
            
        * [Exemple de code de chaînes de Markov cachées](#heading-exemple-de-code-de-chaines-de-markov-cachees)
            
        * [Exemple de code :](#heading-exemple-de-code)
            
    * [Applications en IA et théorie du contrôle : Prendre des décisions en cas d'incertitude](#heading-applications-en-ia-et-theorie-du-controle-prendre-des-decisions-en-cas-dincertitude)
        
* [Chapitre 7 : Théorie de l'optimisation - Enseigner aux machines à s'améliorer](#heading-chapitre-7-theorie-de-loptimisation-enseigner-aux-machines-a-sameliorer)
    
    * [Qu'est-ce que la théorie de l'optimisation ?](#heading-quest-ce-que-la-theorie-de-loptimisation)
        
    * [Pourquoi l'optimisation guide l'apprentissage en IA](#heading-pourquoi-loptimisation-guide-lapprentissage-en-ia)
        
        * [Types de méthodes de théorie de l'optimisation en ML et Deep Learning](#heading-types-de-methodes-de-theorie-de-loptimisation-en-ml-et-deep-learning)
            
        * [Comment la théorie de l'optimisation se connecte-t-elle à l'algèbre linéaire, au calcul et aux probabilités et statistiques ?](#heading-comment-la-theorie-de-loptimisation-se-connecte-t-elle-a-lalgebre-lineaire-au-calcul-et-aux-probabilites-et-statistiques)
            
    * [Techniques d'optimisation simples : Comment les machines apprennent étape par étape](#heading-techniques-doptimisation-simples-comment-les-machines-apprennent-etape-par-etape)
        
        * [Régression linéaire](#heading-regression-lineaire)
            
        * [Réseaux de neurones](#heading-reseaux-de-neurones)
            
    * [Qu'est-ce qu'Adam ? La méthode la plus populaire pour que les modèles d'IA trouvent le meilleur chemin d'apprentissage](#heading-quest-ce-quadam-la-methode-la-plus-populaire-pour-que-les-modeles-dia-trouvent-le-meilleur-chemin-dapprentissage)
        
        * [Exemple de code :](#heading-exemple-de-code-1)
            
    * [Applications en IA et en théorie du contrôle de la théorie de l'optimisation](#heading-applications-en-ia-et-en-theorie-du-controle-de-la-theorie-de-loptimisation)
        
* [Conclusion : Où les mathématiques et l'IA se rencontrent](#heading-conclusion-ou-les-mathematiques-et-lia-se-rencontrent)
    
    * [Les mathématiques sont le fondement de l'IA](#heading-les-mathematiques-sont-le-fondement-de-lia)
        
    * [L'avenir : L'IA sur appareil et la démocratisation de l'IA](#heading-lavenir-lia-sur-appareil-et-la-democratisation-de-lia)
        
    * [Réflexions finales](#heading-reflexions-finales)
        
    * [Remerciements](#heading-remerciements)
        
* [À propos de l'auteur](#heading-a-propos-de-lauteur)
    
    * [Pourquoi ai-je choisi le génie électrique et informatique ?](#heading-pourquoi-ai-je-choisi-le-genie-electrique-et-informatique)
        
    * [Qu'ai-je gagné exactement ?](#heading-quai-je-gagne-exactement)

## Chapitre 1 : Contexte de ce livre

### L'objectif ici

Mon objectif dans ce livre est simple : expliquer les idées mathématiques clés que vous devez comprendre afin de saisir profondément l'IA et d'entraîner des modèles d'apprentissage automatique.

Vous vous demandez peut-être : Pourquoi est-il important d'avoir de bonnes bases en mathématiques avant de créer ces modèles ?

Eh bien, il y a plusieurs raisons, mais en voici quelques-unes :

* Cela vous donne la capacité de comprendre de nouvelles recherches en IA par vous-même.
    
* Vous pouvez utiliser cette même base pour étudier d'autres concepts STEM comme la théorie du signal et les méthodes statistiques avancées.
    
* Cela vous aide à comprendre que les modèles d'IA sont simplement un mélange de différentes idées mathématiques travaillant ensemble et vous donne un aperçu de la manière dont les nouvelles innovations rendent les LLMs plus efficaces.
    
* Cela vous donne une base afin que vous sachiez comment calibrer les modèles d'IA et même créer des modèles dérivés.
    

Ces compétences sont également importantes pour les fondateurs de startups, en particulier dans la Silicon Valley. De nombreuses startups commencent avec des APIs ou des enveloppeurs d'API mais finissent par avoir besoin de leurs propres solutions d'IA.

Externaliser toute l'IA n'est pas idéal. Ce livre vous aidera à comprendre les fondements de l'IA afin que vous puissiez concevoir de meilleures stratégies de croissance et communiquer efficacement avec les investisseurs – en particulier ceux qui étaient des cofondateurs techniques à succès.

### Pourquoi ce livre sur l'IA est-il différent ?

Dans ce livre, nous examinerons l'IA d'un point de vue ingénierie. Cela diffère de l'approche typique de l'informatique de l'IA que la plupart des cours d'introduction adoptent.

En faisant cela, je ne passerai pas beaucoup de temps à expliquer les formules et les théorèmes. Au lieu de cela, j'expliquerai leur importance, comment et pourquoi ils sont appliqués de la manière dont ils le sont.

De cette manière, j'espère offrir un point de vue unique qui met l'accent sur les principes d'ingénierie et les bonnes pratiques qui sous-tendent toutes les technologies modernes d'IA.

Je vais également expliquer comment beaucoup de ces idées mathématiques étranges rendent possibles des industries de plusieurs milliards de dollars.

Nous commencerons par les fondamentaux : la structure des domaines des mathématiques et de l'IA. Après cela, nous examinerons les quatre sous-domaines des mathématiques qui rendent l'IA possible :

* Algèbre linéaire
    
* Calcul
    
* Théorie des probabilités et statistiques
    
* Théorie de l'optimisation
    

Après avoir parcouru toutes les mathématiques, nous les connecterons avec les fondements de ChatGPT et tous ces grands modèles de langage.

De cette façon, vous obtiendrez une base de base dans les concepts mathématiques clés qui, lorsqu'ils sont mélangés ensemble comme les ingrédients d'un gâteau, rendent tous les modèles d'IA possibles.

En sachant d'où viennent les idées, vous développerez une compréhension systémique de l'IA et une approche basée sur les premiers principes.

Gardez simplement à l'esprit que, même si des concepts comme le calcul intégral et les valeurs propres/vecteurs propres ne sont peut-être pas largement utilisés en IA, ils vous aideront à développer ces approches systémique et de premiers principes.

De plus, ce livre sera un travail en progrès. Après sa première publication, je chercherai des commentaires sur les choses que je dois perfectionner, les chapitres à ajouter, et ainsi de suite.

Voici mon email pour tout commentaire que vous pourriez avoir : monteiro.t@northeastern.edu

Et voici le dépôt GitHub du livre avec tout le code : [https://github.com/tiagomonteiro0715/The-Math-Behind-Artificial-Intelligence-A-Guide-to-AI-Foundations](https://github.com/tiagomonteiro0715/The-Math-Behind-Artificial-Intelligence-A-Guide-to-AI-Foundations)

### Permettez-moi de me présenter

Je m'appelle Tiago Monteiro, ingénieur en électricité et informatique et étudiant en maîtrise d'IA à l'université Northeastern, campus de la Silicon Valley. J'ai écrit 20+ articles avec 240K+ vues ici sur freeCodeCamp sur les mathématiques, l'IA et la technologie.

Si vous souhaitez en savoir plus sur mon parcours, je le partagerai à la fin du livre.

### Prérequis

En termes de exigences minimales, vous n'avez besoin de connaître que les bases des mathématiques et de la programmation :

* Algèbre de base et ce que sont les fonctions et le système de coordonnées.
    
* Vous devriez être capable de lire du code Python et de comprendre des choses comme les variables, les fonctions et les boucles.
    

## Chapitre 2 : L'architecture des mathématiques

![Couverture du chapitre sur l'architecture des mathématiques](https://cdn.hashnode.com/res/hashnode/image/upload/v1766099739986/049ff3c0-0150-495e-97e9-4f16f3861058.png align="center")

Les mathématiques sont plus que des nombres. C'est la science de la localisation des motifs complexes qui façonnent notre monde. Pour vraiment comprendre les mathématiques, nous devons regarder au-delà des nombres et des formules pour saisir ses structures.

Ce chapitre vise à montrer les mathématiques comme un arbre en croissance d'idées, un système vivant de logique, pas seulement des formules à mémoriser. Avec des analogies, de l'histoire et des exemples de code, je veux vous aider à comprendre profondément les mathématiques et comment les appliquer à la programmation.

J'ai inclus des exemples de code pour connecter la théorie et la pratique, montrant comment les idées mathématiques s'appliquent à des problèmes réels. Que vous soyez nouveau dans les mathématiques avancées ou plus expérimenté, ces exemples vous aideront à appliquer les mathématiques en programmation.

De cette façon, avant de commencer à passer en revue les différents piliers mathématiques qui soutiennent l'IA, vous comprendrez la structure du domaine.

### L'arbre des mathématiques : comment tout est connecté

![Voir un arbre de sa racine à un arbre](https://cdn.hashnode.com/res/hashnode/image/upload/v1765001557970/7ac6c8c8-d0fd-4a67-be6a-6d8b9a1a6615.jpeg align="center")

Photo par [Lerkrat Tangsri](https://www.pexels.com/photo/bottom-view-of-green-leaved-tree-during-daytime-91153/)

Imaginez les mathématiques comme un vaste arbre en constante croissance.

Les racines sont les fondements : la logique et la théorie des ensembles. De ces racines émergent les principaux domaines : l'arithmétique, l'algèbre, la géométrie et l'analyse.

À mesure que l'arbre se ramifie, de nouveaux sous-domaines comme la topologie et l'algèbre abstraite apparaissent. Parfois, les branches se connectent entre elles.

Cet arbre continue de croître dans de nombreuses directions. L'histoire montre que parfois il croît rapidement grâce à des découvertes scientifiques, tandis qu'à d'autres moments, la croissance est lente.

Et vous pourriez vous demander : Combien de nouvelles branches et de connexions entre elles continueront à apparaître ?

### Une brève histoire des mathématiques : du comptage à l'infini

Les premières idées mathématiques sont apparues indépendamment dans les anciennes civilisations, telles que :

* L'invention du zéro en Inde
    
* Les avancées algébriques islamiques
    
* La rigueur géométrique grecque
    

De grands mathématiciens ont développé et partagé ces idées à travers des écrits et des conférences. Au fil du temps, de nouvelles générations ont construit sur ces idées, créant de nouvelles branches des mathématiques. Cette croissance sans fin est la raison pour laquelle Isaac Newton a écrit à Robert Hooke en 1675 :

> "Si j'ai vu plus loin, c'est en montant sur les épaules de géants."

Il voulait dire qu'en travaillant à partir des connaissances précédentes, il avait pu créer et (re)découvrir de nouvelles idées.

Pourtant, le vrai pouvoir des mathématiques réside dans la pratique répétée et l'étude approfondie.

Comme l'a souligné l'un de mes professeurs :

> *"Plus important que de connaître les théorèmes est de connaître les idées derrière eux et l'histoire de leur création."*

Pour résoudre des problèmes, il est souvent nécessaire de penser à partir des premiers principes, et les mathématiques enseignent cela. Les mathématiques ne sont pas seulement un sujet académique. C'est un langage global pour les scientifiques et les ingénieurs.

En les préservant et en les partageant, de nouvelles mathématiques peuvent croître à partir d'anciennes idées, permettant à l'arbre de continuer à s'étendre.

### Les fondements de la relativité : comment Einstein a utilisé les mathématiques pour comprendre l'espace et le temps

![Un satellite dans l'espace](https://cdn.hashnode.com/res/hashnode/image/upload/v1766903578928/a4102586-cb63-4410-8793-72950145726d.jpeg align="center")

Photo par [Pixabay](https://www.pexels.com/photo/gray-and-white-satellite-41006/)

Albert Einstein a développé les théories de la relativité générale et spéciale, qui impactent :

* Le GPS et la communication globale
    
* Les télécommunications par satellite
    
* L'exploration spatiale et les lancements de satellites
    

Et plus encore.

Mais cela n'a été possible qu'en combinant la géométrie avec le calcul, connu sous le nom de **géométrie différentielle**. Ce domaine a évolué sur des siècles, grâce à de nombreux grands mathématiciens. En voici quelques-uns, bien que la liste ne soit pas exhaustive :

* **Euclide (vers 300 av. J.-C.) :** A contribué à la géométrie, posant les bases des systèmes mathématiques ultérieurs
    
* **Archimède (vers 287–212 av. J.-C.) :** A été un pionnier dans la compréhension du volume, de la surface et des principes de la mécanique
    
* **Renée Descartes (1596–1650) :** A développé les coordonnées cartésiennes et la géométrie analytique
    
* **Isaac Newton (1642–1727) & Gottfried Wilhelm Leibniz (1646–1716) :** Les lois du mouvement et de la gravitation de Newton, ainsi que le développement du calcul par Leibniz, ont formé la base de la mécanique classique qu'Einstein a cherché à étendre et à modifier dans sa théorie de la relativité.
    
* **Leonhard Euler (1707–1783) :** A contribué au développement des équations différentielles, essentielles dans les fondements mathématiques de la physique.
    
* **Gaspard Monge (1746–1818) :** Le père de la géométrie différentielle et pionnier en géométrie descriptive
    
* **Carl Friedrich Gauss (1777–1855) :** A réalisé des avancées révolutionnaires en géométrie, y compris le concept de surfaces courbes.
    
* **Bernhard Riemann (1826–1866) :** A introduit la géométrie riemannienne, une branche de la géométrie différentielle.
    

En revenant à Albert Einstein, il a vu ce que personne d'autre de son temps n'a vu, grâce à ces grands géants des mathématiques et à d'innombrables autres.

### Le plus grand paradoxe de Gödel : les mathématiques peuvent-elles s'expliquer elles-mêmes ?

Le plus grand paradoxe des mathématiques, découvert par Kurt Gödel, est ses théorèmes d'incomplétude. Ils montrent que dans tout système formel cohérent capable d'arithmétique simple, il existe des énoncés vrais qui ne peuvent être prouvés dans le système.

Cela signifie qu'il y a des limites à ce qui peut être prouvé comme vrai ou faux. Pour les mathématiciens, cela implique que certaines vérités sont au-delà des preuves formelles, pourtant nous supposons qu'elles sont vraies. Cela démontre que, peu importe les efforts ou l'IA utilisés, certaines choses restent non prouvables, connues seulement par des approximations et des méthodes non exactes.

### Qu'en est-il des mathématiques appliquées et de l'ingénierie ?

Les mathématiques appliquées et l'ingénierie impliquent l'adaptation des idées de mathématiques pures dans des scénarios du monde réel.

En fait, dans de nombreux cas, c'est la combinaison de nombreuses idées mathématiques.

Considérons quelques exemples :

* En **analyse harmonique**, les transformées de Laplace, de Fourier et Z sont un moyen de voir la même chose dans un nouveau domaine pour obtenir de nouvelles perspectives. Dans ce cas, les intégrales sont utilisées pour rendre ce mappage possible.
    
* **L'analyse en composantes principales (PCA)** est un outil largement utilisé en science des données. Pourtant, c'est un mélange d'algèbre linéaire (dans la PCA, les valeurs propres) avec l'optimisation (ordonner les valeurs propres qui représentent plus de données avec moins de données) afin de rendre les ensembles de données plus courts.
    
* En **apprentissage automatique**, la régression logistique est un mélange de calcul avec des statistiques et des probabilités.
    
* En **apprentissage profond**, les réseaux de neurones ne sont que de nombreuses matrices se multipliant et se mettant à jour qui s'adaptent pour modéliser un ensemble de données représentant un système. Cette optimisation des valeurs de matrice se fait avec des fonctions d'activation, une méthode d'optimisation basée sur la descente de gradient (indique de combien les valeurs doivent changer), et la rétropropagation (applique ces altérations à toutes les valeurs de matrice).
    

Mais le meilleur exemple de cette fusion des mathématiques en ingénierie est dans la [théorie du contrôle](https://www.freecodecamp.org/news/basic-control-theory-with-python/). La théorie du contrôle est l'étude de l'architecture des systèmes. Des trains aux voitures en passant par les avions, tout est basé sur la théorie du contrôle. Elle est partout, dans presque tous les appareils électroniques modernes. Dans les circuits électriques, la théorie du contrôle est également largement utilisée pour garantir la stabilité des circuits face aux perturbations électriques.

Ainsi, comme vous pouvez probablement commencer à le voir, beaucoup des outils que nous avons maintenant ne sont qu'un mélange de nombreuses idées de mathématiques pures – comme différentes recettes. En essence, les mathématiques appliquées sont l'application des mathématiques pures en tant qu'« ingrédients » dans des « recettes » pour résoudre des problèmes.
Ainsi, nous avons exploré la structure et l'évolution des mathématiques. Mais il est important de voir comment nous pouvons appliquer ces idées dans la vie réelle. Les mathématiques pures créent le cadre, et les mathématiques appliquées appliquent ce cadre pour résoudre des problèmes. Pour comprendre cela, nous examinerons deux exemples de code qui montrent comment vous pouvez utiliser des idées mathématiques comme outils de programmation.

### Exemples de code : Approches analytiques et numériques

Ces exemples de code démontrent quelques façons dont vous pouvez utiliser Python pour résoudre des équations mathématiques.

Dans le premier exemple de code, nous résoudreons le problème de la même manière que les enfants à l'école résolvent les exercices de maths : essentiellement, à la main avec un crayon. Dans le deuxième exemple, nous résoudreons le problème en utilisant l'analyse numérique.

#### Exemple 1 : Résoudre un problème de manière analytique

Dans ce problème, nous devons trouver les valeurs des variables x et y. Nous déplacerons donc les variables de gauche à droite pour trouver leurs valeurs.

Lorsque nous résolvons des problèmes de maths de manière analytique, comme nous le faisions à l'école, nous manipulons des symboles pour obtenir des valeurs exactes. Souvent, ces symboles sont x, y et z.

Le code ci-dessous résout un système de deux équations avec deux variables inconnues, x et y.

Nous utiliserons la bibliothèque Python [SymPy](https://www.sympy.org) pour cela. Elle est principalement utilisée pour les mathématiques symboliques.

```python
from sympy import symbols, Eq, solve

x, y = symbols('x y')
eq1 = Eq(2*x + 3*y, 6)
eq2 = Eq(-x + y, 1)

solution = solve((eq1, eq2), (x, y))
print(solution)
```

![Image des équations et de la méthode analytique en Python](https://cdn.hashnode.com/res/hashnode/image/upload/v1747160359386/7a21cddc-f4ba-4f9f-afa0-d1cc11fb27d6.png align="center")

Encore une fois, avec ce code, nous trouvons les valeurs des variables x et y.

Essentiellement, nous trouvons x et y basés sur cette équation :

$$\begin{align} 2x + 3y &= 6 \\ -x + y &= 1 \end{align}$$

Ce qui nous donne le résultat suivant :

```python
{x: 3/5, y: 8/5}
```

Ou :

* x = 0,6
    
* y = 1,6
    

Lorsque nous disons que nous résolvons cela de manière analytique, cela signifie que nous trouvons une solution mathématique exacte en utilisant des formules ou des équations.

Mais souvent, les problèmes sont plus difficiles et peuvent être résolus en ajoutant des symboles à droite ou à gauche de l'équation. Parfois, il peut y avoir tant de symboles et de versions transformées de ceux-ci, avec des choses comme des dérivées et des intégrales, que cela peut devenir très difficile à gérer et prendre beaucoup de temps.

Par exemple, regardons cette équation différentielle partielle :

$$\begin{cases} \frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}, & 0 < x < L, \, t > 0 \\ u(0,t) = 0, & t > 0 \\ u(L,t) = 0, & t > 0 \\ u(x,0) = f(x), & 0 < x < L \end{cases}$$

Elle peut être résolue avec une méthode analytique appelée séparation des variables.

Mais cela nécessite de nombreuses étapes, et il est facile de faire des erreurs. Même les ingénieurs qui ont appris cela ont souvent du mal à se souvenir du processus plus tard.

Lorsque j'ai rencontré ce type d'exercice de maths dans mon diplôme d'ingénierie électrique et informatique au Portugal, il m'a fallu 20 à 30 minutes pour le résoudre.

Pour cette raison, il existe une branche des mathématiques appelée analyse numérique qui se concentre sur la recherche d'approximations de formules existantes. Cela aide à résoudre les problèmes plus rapidement. C'est la méthode que nous explorerons ensuite.

#### Exemple 2 : Résoudre numériquement (Approximation)

Maintenant, résolvons un problème différent : nous allons trouver les valeurs de chacune des 5 variables :

$$\begin{bmatrix} 3 & 2 & -1 & 4 & 5 \\ 1 & 1 & 3 & 2 & -2 \\ 4 & -1 & 2 & 1 & 0 \\ 5 & 3 & -2 & 1 & 1 \\ 2 & -3 & 1 & 3 & 4 \end{bmatrix} \times \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix} = \begin{bmatrix} 12 \\ 5 \\ 7 \\ 9 \\ 10 \end{bmatrix}$$

Résoudre cela à la main prendra un certain temps... mais avec le code Python, c'est très rapide.

Nous utiliserons également la bibliothèque Python [SciPy](https://scipy.org) pour cet exemple.

Résolvons le système numériquement :

```python
import numpy as np
from scipy.linalg import solve

A = np.array([[3, 2, -1, 4, 5],
              [1, 1, 3, 2, -2],
              [4, -1, 2, 1, 0],
              [5, 3, -2, 1, 1],
              [2, -3, 1, 3, 4]])

b = np.array([12, 5, 7, 9, 10])

solution = solve(A, b)

print(solution)
```

![Image des équations et de la méthode numérique](https://cdn.hashnode.com/res/hashnode/image/upload/v1747160347486/d1f17aa6-b288-4e41-9be7-0810c45e778c.png align="center")

Ce qui correspond à cette opération :

$$\begin{bmatrix} 3 & 2 & -1 & 4 & 5 \\ 1 & 1 & 3 & 2 & -2 \\ 4 & -1 & 2 & 1 & 0 \\ 5 & 3 & -2 & 1 & 1 \\ 2 & -3 & 1 & 3 & 4 \end{bmatrix} \times \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix} = \begin{bmatrix} 12 \\ 5 \\ 7 \\ 9 \\ 10 \end{bmatrix}$$

Encore une fois, cela prend du temps à résoudre et il est très facile de faire une simple erreur.

Mais dans cet exemple de code, cette ligne de code :

```python
solution = solve(A, b)
```

Utilise la méthode `solve` de SciPy :

```python
from scipy.linalg import solve
```

C'est une méthode qui vous aide à trouver les valeurs de x dans une équation A·x=b, où A est une grille carrée de nombres et b est une liste de nombres. Cela nous donne ce qui suit :

```python
[ 1.35022026 -0.79955947 -1.17180617  3.14317181 -0.83920705]
```

Ce qui correspond à :

$$\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix} = \begin{bmatrix} 1.35022026 \\ -0.79955947 \\ -1.17180617 \\ 3.14317181 \\ -0.83920705 \end{bmatrix}$$

Et est la même chose que :

$$\begin{align} x_1 &= 1.35022026 \\ x_2 &= -0.79955947 \\ x_3 &= -1.17180617 \\ x_4 &= 3.14317181 \\ x_5 &= -0.83920705 \end{align}$$

#### Pourquoi ces deux approches sont importantes

Nous avons résolu deux problèmes mathématiques de deux manières différentes :

* Analytique : Solutions exactes par manipulation algébrique
    
* Numérique : Solutions approximatives utilisant des algorithmes
    

En ingénierie et en IA, nous choisissons constamment entre ces approches.

Lors de l'entraînement de modèles d'IA avec des millions de paramètres, les solutions analytiques sont impossibles. C'est pourquoi, dans ces cas, nous avons besoin d'approches numériques.

Lors de la création de théorèmes mathématiques, nous avons besoin de précision analytique pour nous assurer qu'il s'agit de la meilleure solution possible.

C'est l'une des nombreuses choses qu'un diplôme d'ingénierie vous enseigne : souvent, dans le monde réel, il est préférable d'écrire simplement du code pour résoudre un problème plutôt que de le résoudre réellement à la main avec des maths. D'autres fois, la meilleure solution est de simplement penser en premiers principes et de là créer de nouveaux théorèmes pour résoudre un problème.

Maintenant, sortons des exemples de code et voyons comment différentes branches des mathématiques se connectent.

### L'impact d'une théorie unifiée des mathématiques

Est-il possible d'unifier toutes les maths ?

En théorie, oui. C'est ce qu'on appelle la théorie unifiée des mathématiques. C'est l'idée que tous les différents domaines des maths peuvent être liés ensemble pour découvrir des motifs plus profonds en mathématiques.

Le [programme de Langlands](https://en.wikipedia.org/wiki/Langlands_program) tente de rendre cette unification possible. C'est une tentative d'interconnecter les plus grandes parties de l'arbre des maths pour découvrir de nouveaux motifs en maths.

Avec une théorie unifiée des mathématiques, nous pourrions comprendre comment chaque branche de l'arbre se connecte avec les autres et toutes les relations entre elles.

#### Quelle est la valeur de cette grande unification pour la société ?

En étudiant l'histoire, nous pouvons trouver des motifs. L'unification de divers domaines a créé de nombreux impacts massifs sur la société, tels que :

* Au 19ème siècle, James Clerk Maxwell a uni les domaines de l'électricité et du magnétisme avec ses célèbres équations de Maxwell. Cela a permis la création de radios et de réseaux électriques à travers le globe. À son tour, cela a servi de fondation à tous les progrès technologiques des 20ème et 21ème siècles.
    
* Au 20ème siècle, l'unification de l'algèbre avec la logique a conduit à l'essor des systèmes numériques. À leur tour, les systèmes numériques ont donné naissance aux processeurs et à l'évolution des ordinateurs et des ordinateurs portables modernes.
    
* Également au 20ème siècle, l'unification de la probabilité et de la communication a conduit à la théorie de l'information. Cela est devenu la fondation de l'internet. Cette unification a été réalisée par un grand mathématicien nommé Claude Shannon.
    

En fin de compte, une théorie unifiée des mathématiques pourrait être l'une des plus grandes réalisations de la société moderne.

En IA, cela pourrait aider à unifier tous les modèles d'apprentissage automatique dans une architecture commune. Cela aiderait à accélérer le développement de nouveaux modèles d'IA et pourrait également ouvrir la porte à de nouvelles avancées en science des matériaux.

Cela pourrait aider à révéler — avec les maths — les motifs profonds que nous n'avons pas encore trouvés dans ces domaines. Tout comme l'unification de l'électricité et du magnétisme a conduit à la technologie moderne, un cadre mathématique unifié conduirait à une vague d'innovation.

### Une leçon finale de l'histoire

De la géométrie grecque à l'IA, les maths ont grandi comme un arbre sur des siècles. En comprenant sa structure, il est possible de voir son rôle dans la recherche des motifs de notre univers.

J'espère avoir pu vous faire voir les maths de cette manière. J'espère que vous pouvez également voir que l'unification des domaines scientifiques aide à poser les fondations pour la création de nouvelles innovations pour aider la société à avancer.

De nombreuses transformations sociétales majeures n'ont vu le jour que grâce à des idées mathématiques abstraites. Lorsque celles-ci sont partagées et affinées, elles deviennent l'architecture cachée du progrès dans la société. L'innovation commence lorsque des idées déconnectées sont unies, bien liées et largement partagées.

## Chapitre 3 : Le domaine de l'intelligence artificielle

### Qu'est-ce que l'intelligence artificielle ?

![Un homme jouant aux échecs contre un robot](https://cdn.hashnode.com/res/hashnode/image/upload/v1765001693682/bbec3565-643f-421f-b32e-3de62285a2c0.jpeg align="center")

Photo par [Pavel Danilyuk](https://www.pexels.com/photo/elderly-man-thinking-while-looking-at-a-chessboard-8438918/)

Le terme Intelligence Artificielle est né du travail de John McCarthy, qui est souvent appelé le "père de l'IA".

Il l'a utilisé lorsqu'il a proposé, avec Marvin Minsky, Nathaniel Rochester et Claude Shannon, le célèbre Dartmouth Summer Research Project on Artificial Intelligence en 1956.

L'intelligence artificielle a été définie, lors de la conférence de Dartmouth, comme :

> *Chaque aspect de l'apprentissage ou toute autre caractéristique de l'intelligence peut en principe être décrit avec tant de précision qu'une machine peut être faite pour le simuler.*

Depuis lors, le domaine a évolué par vagues d'innovation, des premiers systèmes basés sur des règles aux réseaux de neurones modernes.

Mais au fil du temps, plutôt que de créer une [intelligence générale](https://en.wikipedia.org/wiki/Artificial_general_intelligence), la plupart des systèmes d'IA ont été conçus pour exceller dans des tâches spécifiques.

Par exemple :

* Des programmes de jeu d'échecs comme Deep Blue qui ont battu le champion du monde Garry Kasparov
    
* Des systèmes de reconnaissance d'images qui peuvent identifier des objets dans des photographies avec une précision impressionnante
    
* Des modèles de traitement du langage naturel qui peuvent traduire entre les langues
    
* Des IA de jeu comme AlphaGo qui ont maîtrisé l'ancien jeu de Go
    

#### L'intelligence artificielle générale n'est pas encore là

Seuls des modèles d'IA très spécifiques ont démontré des performances de niveau humain ou surhumain dans leurs domaines spécifiques.

À mon avis, et comme nous le verrons dans ce livre, l'AGI sera la combinaison et l'interaction de différents grands modèles de langage interagissant les uns avec les autres et avec les outils disponibles pour eux.

### IA symbolique vs. IA non symbolique : Quelle est la différence ?

![Image comparant l'intelligence artificielle générale avec l'IA spécifique, et à l'intérieur de l'IA spécifique, les cercles de l'IA non symbolique et de l'IA symbolique](https://cdn.hashnode.com/res/hashnode/image/upload/v1755906822438/f639efd3-3f8b-45a7-ad2d-d1795d772947.png align="center")

#### Qu'est-ce que l'IA symbolique ?

L'IA symbolique fait référence à la création d'un programme basé sur de nombreuses règles et symboles pour simuler la façon dont les humains pensent.

Elle utilise des symboles pour représenter des concepts (comme les fermes et les distributeurs) et des règles logiques pour raisonner à leur sujet.

Les données spécifiques sur votre domaine sont appelées faits. Les faits sont les morceaux d'information sur lesquels les règles opèrent. Par exemple, un fait pourrait être "green_acres a une utilisation élevée de l'eau et de bons niveaux de pH."

De plus, imaginez que quelqu'un veut optimiser la logistique de distribution des fermes. Les symboles représenteraient les fermes, les distributeurs et les méthodes de transport. Ensuite, les règles seraient :

* Si la ferme a une utilisation élevée de l'eau et de bons niveaux de pH, alors la classer comme producteur à haut rendement
    
* Si un producteur à haut rendement et un distributeur ont une faible demande, alors prioriser la connexion directe
    
* Si une connexion directe est nécessaire, alors sélectionner le transport avec le moindre impact environnemental
    

Les faits seraient les données réelles comme "la ferme X a une utilisation élevée de l'eau" ou "le distributeur Y a une faible demande."

De cette manière, le système combine ces règles et faits par raisonnement logique pour prendre des décisions. Un langage de programmation très populaire que nous utilisons dans ce domaine s'appelle Prolog, qui a été conçu pour créer des systèmes basés sur des règles.

**Programme d'IA symbolique : Gérer les réseaux agricoles avec un programme Prolog.**

Examinons un exemple de projet pour comprendre cela plus clairement. Le projet que nous examinerons s'appelle SymbolicAIHarvest. Il faisait partie d'un cours à l'Université NOVA pendant mes études de premier cycle en génie électrique et informatique. Le cours s'intitulait "Modélisation des données en ingénierie".

SymbolicAIHarvest est un système d'IA développé avec Prolog pour gérer les réseaux agricoles. [Voici le projet](https://github.com/tiagomonteiro0715/SymbolicAIHarvest) sur GitHub pour que vous puissiez le consulter.

Le projet optimise les opérations agricoles en utilisant un raisonnement basé sur des règles. Il surveille les capteurs pour des données en temps réel et améliore la planification des itinéraires pour les machines. Il coordonne également le mouvement des produits pour réduire les retards et les déchets, améliorant la productivité et la durabilité.

Comprendre le code ci-dessous n'est pas une priorité pour ce livre. Je veux simplement vous montrer un exemple de tous les faits du projet :

```plaintext
% FERMIERS(propriétaire)
farmer(ana).
farmer(asdrubal).
farmer(miguel).
farmer(joao).
farmer(teresinha).
farmer(victor).
farmer(carlos).
farmer(anabela).

% FERMES(nom, propriétaire, région, type)
farm(q1, ana, alentejo, vinha).
farm(q2, ana, alentejo, olival).
farm(q3, asdrubal, lisboa, cenoureira).
farm(q4, asdrubal, lisboa, milharal).
farm(q5, asdrubal, lisboa, vinha).
farm(q6, miguel, evora, trigal).
farm(q7, miguel, evora, cenoureia).
farm(q8, miguel, evora, vinha).
farm(q9, miguel, evora, morangueira).
farm(q10, joao, porto, vinha).
farm(q11, joao, porto, trigal).
farm(q12, joao, porto, cenoureira).
farm(q13, teresinha, algarve, olival).
farm(q14, teresinha, algarve, vinha).
farm(q15, victor, setubal, olival).
farm(q16, victor, setubal, vinha).
farm(q17, victor, setubal, trigal).
farm(q18, carlos, sintra, milharal).
farm(q19, carlos, sintra, vinha).
farm(q20, anabela, coina, milharal).
farm(q21, anabela, coina, olival).
farm(q22, anabela, coina, trigal).

% LECTURES DES CAPTEURS(nom, type, valeur)
sensor_reading(q1,humidity,28).
sensor_reading(q2,humidity,35).
sensor_reading(q3,humidity,42).
sensor_reading(q4,humidity,38).
sensor_reading(q5,humidity,33).
sensor_reading(q6,humidity,45).
sensor_reading(q7,humidity,30).
sensor_reading(q8,humidity,36).
sensor_reading(q9,humidity,50).
sensor_reading(q10,humidity,41).
sensor_reading(q11,humidity,40).
sensor_reading(q12,humidity,44).
sensor_reading(q13,humidity,32).
sensor_reading(q14,humidity,29).
sensor_reading(q15,humidity,47).
sensor_reading(q16,humidity,39).
sensor_reading(q17,humidity,53).
sensor_reading(q18,humidity,27).
sensor_reading(q19,humidity,24).
sensor_reading(q20,humidity,31).
sensor_reading(q21,humidity,37).
sensor_reading(q22,humidity,46).
sensor_reading(q1, temperature, 25).
sensor_reading(q2, temperature, 25).
sensor_reading(q3, temperature, 25).
sensor_reading(q4, temperature, 25).
sensor_reading(q5, temperature, 25).
sensor_reading(q6, temperature, 25).
sensor_reading(q7, temperature, 25).
sensor_reading(q8, temperature, 25).
sensor_reading(q9, temperature, 25).
sensor_reading(q10, temperature, 25).
sensor_reading(q11, temperature, 25).
sensor_reading(q12, temperature, 25).
sensor_reading(q13, temperature, 25).
sensor_reading(q14, temperature, 25).
sensor_reading(q15, temperature, 25).
sensor_reading(q16, temperature, 25).
sensor_reading(q17, temperature, 25).
sensor_reading(q18, temperature, 25).
sensor_reading(q19, temperature, 25).
sensor_reading(q20, temperature, 25).
sensor_reading(q21, temperature, 25).
sensor_reading(q22, temperature, 25).
sensor_reading(q1, water, 47000).
sensor_reading(q2, water, 52500).
sensor_reading(q3, water, 39000).
sensor_reading(q5, water, 61000).
sensor_reading(q8, water, 58000).
sensor_reading(q10, water, 43000).
sensor_reading(q13, water, 72000).
sensor_reading(q16, water, 49000).
sensor_reading(q18, water, 35000).
sensor_reading(q21, water, 66500).
sensor_reading(q1, ph, 6.5).
sensor_reading(q2, ph, 4.7).
sensor_reading(q3, ph, 8.2).
sensor_reading(q4, ph, 7.0).
sensor_reading(q5, ph, 5.1).
sensor_reading(q6, ph, 8.0).
sensor_reading(q7, ph, 4.5).

% DISTRIBUTEURS (nom, région, capacité, niveau de demande)
distributor(d1, alentejo, 1000, 2).
distributor(d2, lisboa, 800, 1).
distributor(d3, evora, 1200, 3).
distributor(d4, porto, 900, 2).
distributor(d5, algarve, 700, 2).
distributor(d6, setubal, 1100, 1).
distributor(d7, sintra, 950, 2).
distributor(d8, coina, 1000, 1).

% TRANSPORTS (nom, capacité, type, autonomie, région, impact)
transport(t1, 1000, fossil, 100, alentejo, 3).
transport(t2, 500, electric, 10, alentejo, 1).
transport(t3, 800, fossil, 400, algarve, 5).
transport(t4, 700, hybrid, 300, setubal, 2).
transport(t5, 150, electric, 340, coina, 1).
transport(t6, 700, fossil, 220, porto, 3).
transport(t7, 900, hybrid, 350, evora, 2).
transport(t8, 1000, electric, 170, sintra, 1).

% Connexions basées sur l'image du graphe

% Haut du réseau
link(q2, d1, 5).
link(q1, d1, 7).
link(q3, d1, 6).

% Centre du réseau
link(q3, q4, 8).
link(q4, d2, 6).
link(q4, d3, 7).
link(q4, q5, 5).
link(q4, d4, 6).

% Connexions supplémentaires
link(q2, d2, 8).
link(q3, d3, 7).
```

Ce code Prolog modélise un système de chaîne d'approvisionnement agricole qui comprend :

* Fermiers
    
* Fermes
    
* Lectures de capteurs
    
* Distributeurs
    
* Transports
    

De plus, dans cette partie du code sur les faits du système :

```plaintext
% Haut du réseau
link(q2, d1, 5).
link(q1, d1, 7).
link(q3, d1, 6).

% Centre du réseau
link(q3, q4, 8).
link(q4, d2, 6).
link(q4, d3, 7).
link(q4, q5, 5).
link(q4, d4, 6).

% Connexions supplémentaires
link(q2, d2, 8).
link(q3, d3, 7).
```
Nous connectons les fermes avec les distributeurs. Ainsi, nous pouvons voir qu'entre la ferme `q1` et le distributeur `d1`, il y a une distance de 7 km. Cela permet de trouver/créer des algorithmes pour trouver le chemin le plus court entre eux.

En fin de compte, l'IA symbolique crée simplement des programmes basés sur un contexte et des règles appliquées à ce contexte.

#### Qu'est-ce que l'IA non symbolique ?

![IA non symbolique avec un cercle intitulé apprentissage automatique à l'intérieur. À l'intérieur du cercle d'apprentissage automatique se trouve un autre cercle avec le texte apprentissage profond.](https://cdn.hashnode.com/res/hashnode/image/upload/v1755906892854/197f7bc3-8c05-46f2-aa2a-99dbaa733a9a.png align="center")

L'IA non symbolique n'utilise pas de symboles ou de règles pour penser. Au lieu de cela, elle est basée sur les données. En d'autres termes, elle apprend des motifs à partir de grands ensembles de données. C'est l'approche utilisée dans l'apprentissage automatique et l'apprentissage profond.

Lorsque nous créons un modèle d'IA, nous pouvons l'associer à une API (Interface de Programmation d'Applications) afin de pouvoir utiliser le modèle d'IA dans des sites web, des applications et d'autres systèmes. Basiquement, le modèle d'IA entraîné est configuré derrière un point de terminaison API. Un point de terminaison API est comme un service web qui permet à d'autres applications d'envoyer des requêtes au modèle et de recevoir des réponses.

Par exemple, lorsque vous utilisez ChatGPT dans un navigateur web, vos messages sont envoyés via l'API d'OpenAI à leur modèle de langage, qui traite votre entrée et renvoie une réponse.

Un agent IA est un programme logiciel qui peut effectuer des tâches de manière autonome en prenant des décisions et en agissant pour atteindre des objectifs spécifiques.

Contrairement aux chatbots basiques qui ne répondent qu'aux questions, les agents IA peuvent planifier des étapes, utiliser des outils et travailler à la réalisation d'objectifs complexes. Ils le font en combinant des modèles de langage avec des fonctionnalités supplémentaires comme l'accès à des données externes ou la collaboration avec d'autres agents IA.

[Voici un exemple](https://github.com/tiagomonteiro0715/ai-content-lab) d'un projet d'agent IA non symbolique sur lequel j'ai travaillé. Je l'ai développé en utilisant la bibliothèque Python [crewAI](https://www.crewai.com/) et l'API OpenAI, l'une des bibliothèques les plus populaires pour créer des agents IA.

Dans ce système, cinq agents IA collaborent pour créer du contenu optimisé :

* **Chercheur et Vérificateur de Faits** : Effectue des recherches pour trouver des tendances et des données.

* **Spécialiste de l'Audience** : Analyse les besoins de l'audience pour un meilleur engagement.

* **Rédacteur Principal de Contenu** : Rédige un contenu engageant basé sur les recherches.

* **Directeur Editorial Senior** : Garantit la qualité et la cohérence du contenu.

* **Spécialiste SEO** : Optimise le contenu pour les moteurs de recherche.

En utilisant l'API OpenAI, il emploie ChatGPT avec crewAI pour faire travailler ces agents pour moi.

### Avant l'IA : La Théorie du Contrôle comme la "Première IA"

Avant l'IA symbolique et non symbolique, le génie électrique avait des méthodes basées sur les données. Un domaine clé que j'ai déjà mentionné ci-dessus était la théorie du contrôle (qui étudie les systèmes de contrôle pour des machines comme les voitures et les fusées). Ce domaine nous permet de concevoir des systèmes qui assurent la stabilité malgré les perturbations et atteignent des objectifs au-delà des capacités humaines.

De nos jours, après avoir créé un algorithme de théorie du contrôle, nous vérifions si l'IA peut améliorer le système de contrôle. Selon mon expérience, seules certaines méthodes avancées d'apprentissage profond sont efficaces. La plupart des méthodes d'apprentissage automatique ne surpassent pas la théorie du contrôle en termes d'efficacité et de sécurité.

La théorie du contrôle offre également une meilleure interprétabilité, nous permettant de comprendre les décisions, contrairement à l'apprentissage automatique avancé et à l'apprentissage profond.

En raison de l'importance historique de la théorie du contrôle, je continuerai à mentionner son rôle et ses applications mathématiques. Cela vous aidera à apprendre les fondements mathématiques de l'IA et à comprendre son importance dans les systèmes électroniques et les applications de l'IA en ingénierie au-delà des prédictions de jeux de données.

## Chapitre 4 : Algèbre Linéaire - La Géométrie des Données

![Loupe pointant vers un livre](https://cdn.hashnode.com/res/hashnode/image/upload/v1765002362611/905a356e-7686-4212-94ac-2b4a5b359c8a.jpeg align="center")

Photo par [Nothing Ahead](https://www.pexels.com/photo/monochrome-photo-of-math-formulas-3729557/).

L'algèbre linéaire est comme avoir des conteneurs organisés pour les données.

Au lieu de jouer avec des nombres individuels, nous pouvons les emballer dans des boîtes structurées qui sont plus faciles à manipuler. Ces boîtes structurées sont appelées matrices.

Lorsque vous avez beaucoup de variables comme des données clients, des lectures de capteurs ou des images, ces boîtes structurées sont très utiles. De plus, ce que nous pouvons faire lorsque nous manipulons ces boîtes est très précieux.

En IA, l'algèbre linéaire est partout. Prenons les matrices, par exemple, un concept clé en algèbre linéaire. Les LLMs effectuent de nombreuses multiplications de matrices comme opération principale. Les données qu'ils prennent sont également organisées en matrices. En reconnaissance d'images, les matrices sont utilisées pour représenter les pixels des images.

Comme vous pouvez le voir, ce concept fondamental de l'algèbre linéaire est important à comprendre. Commençons !

### Que sont les Matrices et Pourquoi Simplifient-elles les Équations ?

Très souvent, les systèmes dans le monde réel peuvent être simplifiés et modélisés avec un système d'équations.

Ces équations sont souvent des équations différentielles de nombreux ordres. Mais pour simplifier, choisissons un système très simple comme celui ci-dessous :

$$\begin{align} 2x + 3y - z &= 7 \\ x - 2y + 4z &= -1 \\ 3x + y + 2z &= 10 \end{align}$$

Lorsque l'on traite de nombreuses variables et équations, écrire chaque équation séparément devient rapidement frustrant. Les matrices fournissent un moyen compact de représenter ces systèmes.

Par exemple, voici le système ci-dessus sous forme d'une seule équation matricielle :

$$\begin{bmatrix} 2 & 3 & -1 \\ 1 & -2 & 4 \\ 3 & 1 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 7 \\ -1 \\ 10 \end{bmatrix}$$

En voyant les systèmes d'équations comme des matrices, nous pouvons utiliser des techniques d'algèbre linéaire pour comprendre comment le système se comporte.

Certaines de ces techniques sont :

* Indépendance Linéaire, Dépendance et Rang

* Déterminants

* Valeurs Propres et Vecteurs Propres

Donc pour résumer :

1. Un système réel peut être représenté comme un système d'équations

2. Un système d'équations peut être compressé dans une forme structurée manipulable appelée matrice.

3. Avec les matrices et les techniques d'algèbre linéaire, nous pouvons comprendre comment le système fonctionne.

Ainsi, nous pouvons étudier le comportement de base d'un système avec l'algèbre linéaire.

Pour les systèmes complexes comme une fusée, l'algèbre linéaire reste la fondation. Des outils plus avancés de la théorie du contrôle sont utilisés, mais comprendre les systèmes plus simples est essentiel pour modéliser et créer des systèmes complexes.

### Vecteurs et Transformations : Se Déplacer dans Plusieurs Directions

Les vecteurs sont des matrices **avec une seule ligne ou une seule colonne.** Vous pouvez également les considérer comme les éléments de base de l'IA. Ils représentent des choses comme des points de données, des paramètres de modèle, et bien plus encore.

Par exemple, chaque entrée de données (comme une image ou une phrase) devient un vecteur que le modèle peut traiter.

Voici deux exemples de vecteurs :

$$\mathbf{A} = \begin{bmatrix} 4 & -2 & 7 & 1 & 5 \end{bmatrix}$$

Et :

$$\mathbf{B} = \begin{bmatrix} 3 \\ -1 \\ 8 \\ 0 \\ -4 \end{bmatrix}$$

Toutes les opérations que vous pouvez effectuer sur les matrices peuvent également être effectuées sur les vecteurs.

En Python, nous pouvons représenter cela par :

```plaintext
import numpy as np

# Définir les vecteurs A et B
A = np.array([4, -2, 7, 1, 5])
B = np.array([3, -1, 8, 0, -4])
```

![Image du code Python représentant le code ci-dessus. Définition de deux tableaux NumPy.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756171163870/4fa7dc5d-5b68-4baf-a211-3db0c3915781.png align="center")

Nous utilisons la bibliothèque [NumPy](https://numpy.org/) car elle facilite et accélère les calculs mathématiques avec des tableaux.

En tant que simplification d'un système d'équations, un vecteur avec une seule ligne représente :

$$\mathbf{A} = \begin{bmatrix} 4 & -2 & 7 & 1 & 5 \end{bmatrix}$$

Et cela représente ce système d'équations :

$$4x_1 - 2x_2 + 7x_3 + x_4 + 5x_5 = k$$

Un vecteur avec une seule colonne représente :

$$\mathbf{B} = \begin{bmatrix} 3 \\ -1 \\ 8 \\ 0 \\ -4 \end{bmatrix}$$

Ce qui représente ce système d'équations :

$$\begin{align} x_1 &= 3 \\ x_2 &= -1 \\ x_3 &= 8 \\ x_4 &= 0 \\ x_5 &= -4 \end{align}$$

Maintenant, voyons quelques opérations matricielles.

Par exemple :

$$\mathbf{A} + \mathbf{B}^T = \begin{bmatrix} 4 & -2 & 7 & 1 & 5 \end{bmatrix} + \begin{bmatrix} 3 & -1 & 8 & 0 & -4 \end{bmatrix} = \begin{bmatrix} 7 & -3 & 15 & 1 & 1 \end{bmatrix}$$

```plaintext
vector_addition = A + B
print("A + B =", vector_addition)
```

![Image du code Python représentant le code ci-dessus. Addition de deux tableaux NumPy.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756171174149/62309c55-a5c5-4f69-aef6-e8ab341b5926.png align="center")

Ce qui donne le résultat de l'équation ci-dessus.

Souvent, l'addition de vecteurs est utilisée pour combiner des caractéristiques. Par exemple, l'addition de nombreux vecteurs de préférences utilisateur crée un profil d'utilisateur.

Voici une **multiplication scalaire** :

$$3\mathbf{A} = 3\begin{bmatrix} 4 & -2 & 7 & 1 & 5 \end{bmatrix} = \begin{bmatrix} 12 & -6 & 21 & 3 & 15 \end{bmatrix}$$

```plaintext
scalar_mult = 3 * A
print("3 * A =", scalar_mult)
```

![Image du code Python représentant le code ci-dessus. Multiplication d'un tableau NumPy par un scalaire.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756171180976/17e260a4-baab-4866-ba30-fc12e090b87a.png align="center")

Ce qui donne le résultat de l'équation ci-dessus.

En IA, la mise à l'échelle des vecteurs est généralement effectuée pour ajuster la pertinence. Par exemple, si nous faisons une multiplication par produit scalaire d'un vecteur par 100, cela signifie que nous augmentons sa valeur. Si c'est par 0,3, cela signifie que nous réduisons son importance.

Voici une **multiplication par produit vectoriel** (également appelée **produit extérieur**) :

$$\mathbf{A} \times \mathbf{B} = \mathbf{A} = \begin{bmatrix} 4 & -2 & 7 & 1 & 5 \end{bmatrix} \times \begin{bmatrix} 3 \\ -1 \\ 8 \\ 0 \\ -4 \end{bmatrix} = 50$$

Habituellement, en ingénierie, une multiplication par produit vectoriel est utilisée en apprentissage automatique (construction/mise à jour de matrices de poids) et en infographie (transformations).

```plaintext
import numpy as np

outer_product = np.outer(A, B)
print("A  B =", outer_product)
```

![Image du code Python représentant le code ci-dessus. Multiplication d'un tableau NumPy via produit extérieur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756171191991/303e708a-2006-46e7-aa6d-1377ab1ba735.png align="center")

Ce qui donne le résultat de l'équation ci-dessus.

Voici une **multiplication par produit scalaire** (également appelée **produit scalaire**) :

$$\mathbf{A} \cdot \mathbf{B}^T = \begin{bmatrix} 4 & -2 & 7 & 1 & 5 \end{bmatrix} \cdot \begin{bmatrix} 3 & -1 & 8 & 0 & -4 \end{bmatrix}$$

$$= 4 \cdot 3 + (-2) \cdot (-1) + 7 \cdot 8 + 1 \cdot 0 + 5 \cdot (-4) = 50$$

Nous utilisons principalement les produits scalaires lorsque nous voulons mesurer la similarité ou l'alignement entre deux vecteurs.

En apprentissage automatique, en une phrase simple, cela nous donne une mesure de similarité.

```plaintext
import numpy as np

dot_product = np.dot(A, B)
print("A  B =", dot_product)
```

![Image du code Python représentant le code ci-dessus. Multiplication d'un tableau NumPy via produit scalaire.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756171200508/ee7b9e61-c1cb-497d-b038-b6a672c6d24b.png align="center")

Ce qui donne le résultat de l'équation ci-dessus.

### Indépendance Linéaire, Dépendance et Rang : Pourquoi C'est Important

Très souvent, les matrices peuvent être réduites et simplifiées. Il est donc bon de réduire une matrice à sa forme la plus simple avant de commencer à analyser ses propriétés.

Lorsque chaque ligne d'une matrice peut être créée avec d'autres lignes, alors cette matrice est linéairement dépendante. Cela signifie que la matrice peut être davantage modifiée.

Ainsi, une matrice a la propriété d'indépendance linéaire lorsque ses lignes ne peuvent pas être créées en les combinant.

Par exemple, lorsque nous avons une matrice complexe comme celle-ci :

$$C = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 2 & 4 & 6 & 8 \\ 1 & 3 & 5 & 7 \\ 0 & 1 & 2 & 3 \end{bmatrix}$$

Nous pouvons, avec des calculs, la convertir en ceci :

$$C_{\text{réduite}} = \begin{bmatrix} 1 & 0 & -1 & -2 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

Si vous n'êtes pas familier avec la réduction de lignes, je recommande [cette vidéo YouTube](https://www.youtube.com/watch?v=eDb6iugi6Uk).

La matrice simplifiée ci-dessus est la même chose que ceci :

$$C_{\text{réduite}} = \begin{bmatrix} 1 & 0 & -1 & -2 \\ 0 & 1 & 2 & 3 \end{bmatrix}$$

Ainsi, nous concluons que la matrice C a un **rang** de 2.

En d'autres termes, puisque la forme la plus simple de la matrice n'a que 2 lignes avec des nombres, elle a un rang de 2.

De cela, nous pouvons conclure que la version réduite de la matrice est **linéairement indépendante**. Cela est dû au fait qu'aucune ligne ou colonne ne peut être créée à partir des lignes ou colonnes existantes. C'est la matrice la plus simple possible.

La matrice originale C est linéairement dépendante car certaines lignes sont simplement des multiples ou des combinaisons d'autres lignes. Par exemple, la ligne 2 de la matrice originale C est exactement la ligne 1 multipliée par 2.

Une autre façon de voir cela est que nous avons 4 lignes dans la matrice originale et le rang de la matrice C est 2. Puisqu'ils ne sont pas égaux, C est linéairement dépendante.

#### Pourquoi ces concepts sont-ils importants ?

L'indépendance linéaire et le rang sont importants en ingénierie car ils montrent si les équations, représentées sous forme de matrices, donnent des informations uniques. Dans les circuits électriques et les systèmes de contrôle, savoir que les équations, représentées sous forme de matrices, sont indépendantes garantit que vous avez des solutions uniques et évite la confusion.

Le rang de la matrice montre le nombre maximum d'équations indépendantes qui peuvent exister. Cela aide les ingénieurs à modéliser la forme la plus simple possible des systèmes.

Dans les LLMs comme ChatGPT, Gemini, Grok et Claude, l'indépendance linéaire, la dépendance et le rang sont utilisés dans une technique très importante appelée LoRA (Low-Rank Adaptation).

LoRA (Low-Rank Adaptation) est largement utilisé pour calibrer ces modèles afin de s'assurer qu'ils s'adaptent efficacement à de nouvelles tâches ou domaines sans réentraîner le modèle complet. De plus, il existe des variantes de cette technique, comme Quantized LoRA. Ainsi, dans de nombreux centres de données, LoRA économise de l'énergie, de l'eau pour le refroidissement, et bien d'autres choses.

### Déterminants : Mesurer l'Espace et la Mise à l'Échelle

Pourquoi les déterminants sont-ils importants ?

Les déterminants nous indiquent si un système d'équations a des solutions infinies, aucune solution, ou s'il a une solution unique sans avoir à résoudre tout le système.

Ainsi, au lieu d'essayer immédiatement de résoudre un système complexe, nous pouvons d'abord utiliser le déterminant pour savoir s'il vaut même la peine de le résoudre.

De nombreux ingénieurs ne comprennent pas vraiment l'importance du déterminant. La seule chose qu'ils connaissent est la formule et comment l'appliquer.

Alors maintenant, apprenons, avec quelques exemples, ce qu'est exactement le déterminant et pourquoi il est important.

Un déterminant est juste un nombre. Il est toujours calculé à partir d'une matrice carrée. En calculant le déterminant, nous pouvons trouver certaines propriétés du système qu'il représente.

Le déterminant d'une matrice donnée A :

$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}.$$

peut être représenté par deux notations :

$$\det(A) = ad - bc$$

ou

$$|A| = ad - bc$$

Les deux sont la même chose.

Voyons comment calculer un déterminant :

$$|A| = \begin{vmatrix} 2 & 3 \\ 1 & 4 \end{vmatrix} = (2)(4) - (3)(1) = 8 - 3 = 5.$$

Voyons comment faire cela en Python :

```plaintext
import numpy as np

# Définir la matrice
A = np.array([
    [2, 3],
    [1, 4]
])

# Calculer le déterminant
det_A = np.linalg.det(A)

print("Déterminant de A :", det_A)
```

![Image du code Python représentant le code ci-dessus. Trouver le déterminant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756233259727/feea57a3-5a33-49b9-a74a-979eba5ec7fe.png align="center")

#### Le même calcul fonctionne pour d'autres matrices !

Voici la formule du déterminant pour une matrice 3x3 :

Pour une matrice 3 par 3 :

$$|B|= \begin{vmatrix} a & b & c \\ d & e & f \\ g & h & i \end{vmatrix} = aei + bfg + cdh - ceg - bdi - afh.$$

Maintenant, appliquons la formule à un exemple :

$$|B| = \begin{vmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 1 & 0 & 6 \end{vmatrix} = (1)(4)(6) + (2)(5)(1) + (3)(0)(0) - (3)(4)(1) - (2)(0)(6) - (1)(5)(0)$$

Évaluons chaque terme :

$$= (1)(4)(6) + (2)(5)(1) - (3)(4)(1) = 4 \cdot 6 + 2 \cdot 5 - ( 3 \cdot 4) = 24+10-12 = 22$$

En code Python :

```plaintext
import numpy as np

# Définir la matrice
B = np.array([
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
])

# Calculer le déterminant
det_B = np.linalg.det(B)

print("Déterminant de B :", det_B)
```

![Image du code Python représentant le code ci-dessus. Trouver un déterminant 3 par 3.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756233606615/4e333b35-4714-480a-8a3b-62db799614e1.png align="center")

Maintenant, visualisons la matrice A en traçant ses vecteurs colonnes. Chaque colonne deviendra un vecteur : (2,1) et (3,4). Cela nous montre géométriquement ce que la matrice fait réellement.

Dans un graphique geogebra, cela nous donne ceci :

![Représentation de 2 vecteurs dans un plan cartésien.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756235393476/6b5c38ea-7b27-4e3d-8ad4-346417d35e77.png align="center")

Comme nous pouvons le voir, les vecteurs définissent comment chaque variable influence le système. En visualisant ce que font les matrices, nous pouvons trouver des motifs qui sont plus difficiles à trouver simplement en regardant les formules.

**Que signifie cela visuellement ?**

Cela signifie que dans l'espace, voici à quoi ressemble notre matrice. C'est aussi comment notre système d'équations est représenté.

C1 représente la "force" ou l'impact que la variable x1 a. Et C2 fait de même pour la variable x2.

Maintenant, nous allons nous concentrer sur un exemple de matrice 3D. Cette matrice D représente un système de trois équations avec trois variables :

$$D = \begin{bmatrix} 2 & -1 & 3 \\ 4 & 0 & -2 \\ -1 & 5 & 1 \end{bmatrix}$$

$$\begin{align} 2x_1 - x_2 + 3x_3 &= p \\ 4x_1 + 0x_2 - 2x_3 &= q \\ -x_1 + 5x_2 + x_3 &= r \end{align}$$

Chaque colonne peut être décrite comme un vecteur séparé :

$$\begin{equation} D = \left[ D_1 \mid D_2 \mid D_3 \right] = \left[ \begin{bmatrix} 2 \\ 4 \\ -1 \end{bmatrix} \mid \begin{bmatrix} -1 \\ 0 \\ 5 \end{bmatrix} \mid \begin{bmatrix} 3 \\ -2 \\ 1 \end{bmatrix} \right] \end{equation}$$

Comme nous pouvons le voir, D a été décomposé en 3 nouveaux vecteurs colonnes :

$$\begin{equation} D_1 = \begin{bmatrix} 2 \\ 4 \\ -1 \end{bmatrix} \end{equation}$$

et :

$$\begin{equation} D_2 = \begin{bmatrix} -1 \\ 0 \\ 5 \end{bmatrix} \end{equation}$$

et :

$$\begin{equation} D_3 = \begin{bmatrix} 3 \\ -2 \\ 1 \end{bmatrix} \end{equation}$$

Dans un graphique geogebra, cela nous donne ceci :

![Représentation de 3 vecteurs dans un plan cartésien 3D.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756236913078/8d8a3d48-20a9-423b-bfb8-4368d92ec340.png align="center")

En 3D, chaque vecteur pointe dans sa propre direction. Ensemble, ils organisent trois plans. Là où les trois plans se touchent se trouve la solution du système.

Ceci est un avantage clé des matrices et de l'algèbre linéaire. Elles nous aident à visualiser à la fois des systèmes simples et complexes, améliorant la pensée systémique et la pensée par premiers principes.

Le déterminant est directement lié à ces visualisations. Par exemple, en 2D, il mesure la surface que les vecteurs couvrent. Maintenant, nous allons voir comment cela est possible.

Utilisons la matrice A et voyons à quoi ressemble son déterminant en termes géométriques :

$$A = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}$$

Qui peut être décomposée en 2 vecteurs `u` et `v` :

![Représentation de 2 vecteurs (matrice A) dans un plan cartésien.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756241016899/ded47498-b030-4fa1-a4fe-07153d138a7f.png align="center")

Cela nous donne ce déterminant :

$$|A| = \begin{vmatrix} 2 & 3 \\ 1 & 4 \end{vmatrix} = (2)(4) - (3)(1) = 8 - 3 = 5.$$

Maintenant, visualisons le déterminant.

À partir de (2,1) et (3,4), nous pouvons tracer des vecteurs parallèles à u et v. Ceux-ci sont appelés u' et v' et ont la même magnitude. Ils se rencontrent en (5,5), et nous avons un parallélogramme qui est complété avec ces points : (0,0),(2,1),(3,4),(5,5)

![Représentation des 4 vecteurs utilisés dans le déterminant](https://cdn.hashnode.com/res/hashnode/image/upload/v1756241586617/d825b8e2-d839-4b15-bdd0-d9b5efd80942.png align="center")

L'aire du parallélogramme est le déterminant :

![Illustration montrant que l'aire limitée par les 4 vecteurs est le déterminant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756241692073/deb2e0cd-32a3-4a1a-90e7-e556f5039169.png align="center")

Regardons un autre exemple.

Utilisons une matrice F et voyons ce qu'elle est vraiment :

$$F = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$$

Cela nous donne ce déterminant :

$$|F| = \begin{vmatrix} 1 & 2 \\ 2 & 4 \end{vmatrix} = (1)(4) - (2)(2) = 4 - 4 = 0$$

Dans GeoGebra, nous pouvons voir que :

![Représentation des 2 vecteurs utilisés dans le déterminant](https://cdn.hashnode.com/res/hashnode/image/upload/v1756242215981/d88f2e80-04ba-46b9-979d-d7684f161210.png align="center")

Maintenant, essayons de voir le déterminant visuellement :

![Illustration montrant que l'aire limitée par les 2 vecteurs est le déterminant et qu'elle n'existe pas. Donc le déterminant est zéro.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756242340382/46551578-69a5-4ef9-ab86-9149e7fb4aaa.png align="center")

Nous pouvons conclure que l'aire est 0.

Maintenant, utilisons une matrice G et voyons ce qu'elle est vraiment :

$$G = \begin{bmatrix} 1 & 5 \\ 2 & 3 \end{bmatrix}$$

Cela nous donne ce déterminant :

$$|G| = \begin{vmatrix} 1 & 5 \\ 2 & 3 \end{vmatrix} = (1)(3) - (5)(2) = 3 - 10 = -7$$

Dans GeoGebra, nous pouvons voir que :

![Représentation des 2 vecteurs utilisés pour trouver le déterminant](https://cdn.hashnode.com/res/hashnode/image/upload/v1756242987960/d182b725-81ba-4042-81e1-6b0232e09ffb.png align="center")

Maintenant, essayons de voir le déterminant visuellement.

À partir de (1,2) et (5,3), nous pouvons tracer des vecteurs parallèles à u et v. Ceux-ci sont appelés u' et v' et ont la même magnitude. Ils se rencontrent en (6,5). Un parallélogramme est complété avec ces points : (0,0),(1,2),(5,3),(6,5)

![Représentation de 4 vecteurs utilisés pour trouver le déterminant avant de montrer l'aire](https://cdn.hashnode.com/res/hashnode/image/upload/v1756243098714/881693d4-7a84-4b72-bb87-3fb48b25fe4b.png align="center")

Encore une fois, l'aire du parallélogramme est le déterminant :

![Illustration montrant que l'aire limitée par les 4 vecteurs est le déterminant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756243316071/ce8fa65b-6370-4ada-9fe6-cdf20ab4546d.png align="center")

Nous venons de voir que le déterminant est l'aire d'un parallélogramme formé par les vecteurs. Lorsque le déterminant est 0, il n'y a pas d'aire. Dans les autres cas, il y a une aire. Mais que signifie cela, et pourquoi nous soucions-nous de ces différentes valeurs ?

**Lorsque le det = 0 :**

* Les vecteurs sont linéairement dépendants (l'un peut être écrit comme une combinaison des autres)

* Ils se trouvent sur la même ligne ou l'un est une version mise à l'échelle de l'autre

* Le parallélogramme s'effondre en une ligne, d'où une aire nulle

* Cela nous indique que la matrice n'a pas d'inverse

* **Les systèmes d'équations n'ont soit aucune solution, soit une infinité de solutions**

**Lorsque le det ≠ 0 (det > 0 ou det < 0) :**

* Les vecteurs forment un parallélogramme propre avec une aire

* Si det > 0, l'aire est positive et la transformation préserve l'orientation

* Si det < 0, l'aire est négative et l'orientation est inversée

* Les vecteurs sont linéairement indépendants

* **Les systèmes d'équations ont exactement une solution**

En ingénierie électrique, les déterminants aident à vérifier si un système de contrôle est contrôlable et observable.

Les systèmes de contrôle utilisent beaucoup de matrices. Pour cette raison, vérifier si leurs déterminants sont nuls ou non nuls indique aux ingénieurs :

* S'il est contrôlable, cela signifie que le système est atteignable, ce qui aide à la stabilisation et à l'optimisation des performances.

* S'il est observable, cela signifie que le système est mesurable, ce qui aide à la détection de défauts et à la surveillance du système.

Dans l'analyse par éléments finis, un outil mathématique très populaire pour résoudre les équations différentielles partielles, les déterminants aident à déterminer rapidement si les calculs donneront des résultats fiables.

Ainsi, avec l'analyse par éléments finis, nous pouvons concevoir des bâtiments plus sûrs, optimiser les ailes d'avions et simuler des implants médicaux – tout cela ayant un grand impact sur la vie et la sécurité humaines.

En apprentissage automatique, les déterminants sont cruciaux pour comprendre les transformations de données. Dans ces méthodes, si un déterminant avec une valeur de zéro apparaît, cela signifie que vous perdez des informations et ne pouvez pas récupérer les données originales.

De plus, en apprentissage profond, il est utilisé pour décider des premiers paramètres des réseaux de neurones (initialisation des poids) afin de prévenir des problèmes comme les gradients qui disparaissent ou explosent.

Dans une matrice 3×3, le déterminant représente le volume d'un parallélépipède (une "boîte" 3D) formé par trois vecteurs dans l'espace 3D.

* Si det = 0 : Les trois vecteurs se trouvent dans le même plan, donc ils ne couvrent aucun volume 3D

* Si det ≠ 0 : Les vecteurs forment une forme 3D propre avec un volume réel

La valeur absolue |det| vous donne le volume exact de ce [parallélépipède](https://en.wikipedia.org/wiki/Parallelepiped).

Par exemple, si vous avez des vecteurs a, b et c, le déterminant vous indique combien d'espace 3D ils "remplissent" lorsque vous les utilisez comme les arêtes d'une boîte.

C'est là que cela devient fascinant :

* Matrice 4×4 : Le déterminant représente le "hypervolume" d'un parallélépipède 4D formé par quatre vecteurs dans l'espace à quatre dimensions.

* Matrice 1000×1000 : Le déterminant représente l'hypervolume dans l'espace à 1000 dimensions !

Ainsi, pour résumer, le déterminant nous indique facilement s'il n'y a pas de solutions, une infinité de solutions ou exactement une solution dans un système d'équations, représenté par une matrice compacte.

### Que sont les espaces mathématiques et comment simplifient-ils les calculs ?

Nous avons maintenant une excellente base pour comprendre le reste de ce chapitre sur l'algèbre linéaire.

Maintenant, nous allons voir comment une matrice linéairement indépendante crée quelque chose appelé une base. De plus, nous verrons qu'une base est simplement un ensemble de blocs de construction pour les espaces mathématiques !

Les vecteurs lignes d'une matrice linéairement indépendante forment une base.

Par exemple, dans la matrice A, qui est linéairement indépendante :

$$A = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$$

forme cet ensemble :

$$((1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1))$$

Dans ce cas, puisque la matrice A est linéairement indépendante, l'ensemble des lignes de la matrice est appelé une **base**. À partir de cette base, vous pouvez créer d'innombrables combinaisons linéaires de tout autre vecteur. La collection de toutes ces combinaisons possibles est appelée un **espace mathématique**.

Un espace mathématique est un ensemble infini où toutes les combinaisons linéaires d'une base existent. Il est appelé une base parce que ces vecteurs **forment la base** pour exprimer tout vecteur dans l'espace comme une combinaison linéaire.

Cette matrice B est linéairement indépendante :

$$B = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ \end{bmatrix}$$

Et forme cet ensemble :

$$((1, 0), (0, 1))$$

Et de cela viennent tous les points possibles dans ce système de coordonnées cartésien :

![Montrant dans le plan cartésien où se trouve le point (2, 3)](https://cdn.hashnode.com/res/hashnode/image/upload/v1756247201687/a847b8c0-5678-431c-b446-e1897afdffc6.png align="center")

Par exemple, mathématiquement, nous pouvons obtenir le point (2,3) par :

$$(x=2, y=3) = 2(1, 0) + 3(0, 1) = (2, 0) + (0, 3) = (2, 3)$$

Remarque : Il existe d'autres bases pour le plan de coordonnées cartésien. J'ai choisi celle-ci parce qu'elle est la plus facile à comprendre.

### Valeurs propres et vecteurs propres : Déverrouiller des motifs cachés

Les valeurs propres et les vecteurs propres, à mon avis, sont bien plus simples que ce que les professeurs de mathématiques en font à l'université :

* Les valeurs propres vous indiquent combien une matrice étire ou rétrécit les choses.

* Les vecteurs propres vous indiquent quelles directions restent inchangées lorsque la matrice les transforme.

Ainsi, une matrice peut avoir une ou plusieurs valeurs propres qui à leur tour résultent en plusieurs vecteurs propres.

Regardons un exemple :

Pour une matrice carrée A, une valeur propre λ, et un vecteur propre v :

$$Av=\lambda v$$

La manière la plus simple de trouver la valeur propre est de calculer ceci :

$$det(A−\lambda I)=0$$

ou :

$$|A−\lambda I|=0$$

Encore une fois, nous avons différentes notations pour le déterminant, mais elles représentent la même chose.

Quoi qu'il en soit, définissons une matrice A très simple :

$$A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$$

Maintenant, faisons quelques calculs.

Cette formule :

$$det(A−\lambda I)=0$$

Peut être décomposée en :

$$det(\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} - \lambda \times \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}) = 0$$

Ce qui est la même chose que :

$$det(\begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} - \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix}) = 0$$

Ce qui nous donne :

$$det(\begin{bmatrix} 2−\lambda & 0 \\ 0 & 3−\lambda \end{bmatrix}) = 0$$

D'après les calculs que nous avons faits ci-dessus sur le déterminant, nous pouvons conclure que :

$$(2−\lambda) \times (3−\lambda) = 0$$

Ce qui est la même chose que :

$$2−\lambda = 0 \text{ ou } 3−\lambda = 0$$

Ce qui nous donne ces valeurs propres :

$$\lambda_1 = 2, \quad \lambda_2 = 3$$

Et ces vecteurs propres :

$$\mathbf{v_1} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad \mathbf{v_2} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

Cela signifie que dans le système de coordonnées cartésien :

![Montrant comment les vecteurs propres sont liés aux vecteurs de la matrice A visuellement. Les deux ont les mêmes directions mais des valeurs scalaires différentes.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756321668969/949a5a4b-12ff-4490-bbff-1cc032bc5705.png align="center")

En appliquant les vecteurs propres, nous pouvons voir que :

* La valeur propre 2 est associée au vecteur propre v1 :

$$A\mathbf{v_1} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix} = 2\begin{bmatrix} 1 \\ 0 \end{bmatrix}$$

* La valeur propre 3 est associée au vecteur propre v2 :

$$A\mathbf{v_2} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}\begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 3 \end{bmatrix} = 3\begin{bmatrix} 0 \\ 1 \end{bmatrix}$$

Voici le code Python pour calculer cela :

```plaintext
import numpy as np

# Définir la matrice A
A = np.array([[2, 0],
              [0, 3]])

# Calculer les valeurs propres et les vecteurs propres
valeurs_propres, vecteurs_propres = np.linalg.eig(A)

print("Valeurs propres :")
print(valeurs_propres)

print("Vecteurs propres (colonnes) :")
print(vecteurs_propres)
```

![Code Python, avec un tableau NumPy, montrant comment trouver les valeurs propres](https://cdn.hashnode.com/res/hashnode/image/upload/v1756322044095/bc76f0ec-1d13-4845-b0f3-2847118860a3.png align="center")

Les valeurs propres et les vecteurs propres sont des outils clés en ingénierie et en apprentissage automatique car ils révèlent le comportement fondamental d'une matrice. Bien qu'une transformation matricielle puisse sembler complexe, en réalité :

* Les valeurs propres montrent combien d'étirement ou de compression se produisent.

* Les vecteurs propres identifient les directions spéciales où cet étirement se produit le plus naturellement.

En apprentissage automatique, nous pouvons utiliser l'analyse en composantes principales (PCA) pour réduire la taille des ensembles de données.

Ainsi, par exemple, disons que vous construisez une application d'apprentissage automatique pour prédire les maladies cardiaques. Vous avez 100 catégories de données et 1 variable cible indiquant si une personne en est atteinte ou non.

Avec la PCA, vous pouvez convertir les 100 catégories en, disons, 40 catégories. De cette façon, vous pouvez créer un modèle d'apprentissage automatique plus petit et économiser des ressources de calcul.

La PCA utilise les vecteurs propres des matrices de covariance pour trouver les directions importantes dans les données avec de nombreuses variables. Elle réduit la taille des données sans perdre beaucoup de détails, aidant les algorithmes d'apprentissage automatique à se concentrer sur les caractéristiques clés et à ignorer les informations inutiles.

### Applications de l'algèbre linéaire en IA et en théorie du contrôle

L'algèbre linéaire sert de fondement mathématique à tous les domaines de l'ingénierie.

De plus, les principes des matrices et des transformations linéaires fournissent la base computationnelle qui rend l'IA moderne possible tout en permettant le contrôle de systèmes complexes.

Tous les LLMs, de ChatGPT et Claude à Gemini et Grok, reposent sur des opérations linéaires.

Tous ces systèmes effectuent d'énormes multiplications de matrices pour traiter et créer du langage humain. Ainsi, lorsque vous tapez quelque chose dans ChatGPT, probablement des millions de multiplications de matrices se produisent pendant que vous attendez une réponse !

En théorie du contrôle, surtout dans un domaine appelé théorie du contrôle par espace d'état, les matrices rendent possible la création de contrôleurs complexes. L'algèbre linéaire aide les ingénieurs à concevoir des contrôleurs pour des choses comme les pilotes automatiques d'avions et les systèmes robotiques, parmi d'autres applications.

Par exemple, lorsqu'une fusée ajuste sa trajectoire ou qu'un drone maintient un vol stable, de nombreuses multiplications de matrices se produisent pour déterminer la meilleure façon de garantir la stabilité du système.

Grâce aux GPUs, les matrices d'algèbre linéaire sont très efficaces à calculer. De plus, tout nouvel algorithme de multiplication de matrices ou matériel spécial pour des opérations linéaires plus rapides peut grandement améliorer l'IA et les systèmes de contrôle.

En fin de compte, l'algèbre linéaire est le moteur mathématique caché alimentant la révolution actuelle de l'IA.

## Chapitre 5 : Calcul multivariable – Changement dans de nombreuses directions

![Photo d'une femme écrivant une équation de calcul sur un tableau](https://cdn.hashnode.com/res/hashnode/image/upload/v1765002238157/a377cdc6-7e85-491b-90b8-8b3243618288.jpeg align="center")

[Photo par ThisIsEngineering](https://www.pexels.com/photo/woman-writing-on-a-whiteboard-3862130/)

### Limites et continuité : Comprendre le changement fluide

Le calcul est l'un des domaines les plus précieux des mathématiques et il se concentre sur l'étude du changement continu.

Avant de commencer à apprendre un sujet qui fait abandonner de nombreuses personnes leurs études d'ingénierie, je veux une fois de plus vous assurer que ce chapitre est très facilement expliqué avec beaucoup d'images et d'exemples de code.

De plus, tout comme l'algèbre linéaire, de nombreux concepts en calcul sont des composants d'outils qui ont aidé à créer des industries de plusieurs milliards de dollars.

#### Qu'est-ce que la continuité ?

Avant d'aller expliquer des sujets comme les dérivées et les intégrales, nous devons comprendre la continuité.

En termes simples, la continuité signifie qu'une fonction n'a pas de cassures, de sauts ou de trous.

Essentiellement, vous pouvez la tracer sans lever le crayon du papier.

Par exemple, cette fonction est continue :

![Exemple d'une fonction qui est continue](https://cdn.hashnode.com/res/hashnode/image/upload/v1756402257225/f9cfc4f3-a6f1-4fb9-9ed1-f690c4ffffc4.png align="center")

Vous pouvez tracer ce graphique sans lever le crayon du papier.

Le graphique ci-dessus est représenté par cette fonction :

$$y = x^2 - 4x + 3$$

Mais la fonction ci-dessous **n'est pas** continue :

![Exemple d'une fonction qui n'est pas continue](https://cdn.hashnode.com/res/hashnode/image/upload/v1756402337970/b5a65748-572d-4342-9685-9472babde38a.png align="center")

Celle-ci, vous **ne pouvez pas** la tracer sans lever le crayon du papier.

Elle est représentée par cette fonction définie par morceaux :

$$y = \begin{cases} 1.5 + \frac{1}{x+1} & \text{si } -1 < x < 2 \\ 2 + \frac{2}{(x-1)^2} & \text{si } x > 2 \end{cases}$$

Cette fonction définie par morceaux est essentiellement deux fonctions individuelles pour deux intervalles de nombres différents. Puisque le calcul est l'étude du changement continu, nous ne pouvons réalistement l'utiliser que dans des fonctions continues.

#### Comment les limites garantissent-elles la continuité ?

Nous ne pouvons utiliser des outils comme les dérivées et les intégrales que si une fonction est continue.

Comment pouvons-nous décrire mathématiquement qu'une fonction est continue – comme la tracer sans lever notre crayon du papier ?

Les limites résolvent ce problème.

Lorsque nous prenons la limite d'une fonction en un point donné, nous demandons : quelle valeur une fonction approche-t-elle lorsque nous nous rapprochons de ce point ?

Regardons quelques exemples de cette fonction à ces points et comprenons également la notation utilisée dans les limites :

![Exemple d'une fonction qui est continue et ses divers points](https://cdn.hashnode.com/res/hashnode/image/upload/v1756403511442/de3450f2-dcf9-40e3-a04e-846334abeebd.png align="center")

1. **Quelle est la limite du point x=0 ?**

C'est 3. Elle traverse effectivement l'axe des y.

En notation mathématique,

$$\begin{align} \lim_{x \to 0} (x^2 - 4x + 3) &= (0)^2 - 4(0) + 3 \\ &= 0 - 0 + 3 \\ &= 3 \end{align}$$

Dans cette notation, nous demandons quelle est la valeur de la fonction y lorsque x se rapproche très près de 0. Imaginez x à 0.00000000000001 ou -0.00000000000001. Il se rapproche tellement que nous pouvons le considérer comme suffisamment proche.

2. **Quelle est la limite du point x=1 ?**

Voyons un autre exemple :

Dans ce cas, c'est 0.

$$\begin{align} \lim_{x \to 1} (x^2 - 4x + 3) &= (1)^2 - 4(1) + 3 \\ &= 1 - 4 + 3 \\ &= 0 \end{align}$$

Dans cette notation, nous demandons quelle est la valeur de la fonction y lorsque x se rapproche très près de 1. Imaginez x à 0.99999999999999 ou 1.00000000000001. Il se rapproche tellement que nous pouvons le considérer comme suffisamment proche.

3. **Quelle est la limite du point x=2 ?**

Voyons un autre exemple

Ici, c'est -1.

$$\begin{align} \lim_{x \to 2} (x^2 - 4x + 3) &= (2)^2 - 4(2) + 3 \\ &= 4 - 8 + 3 \\ &= -1 \end{align}$$

Quelques exemples rapides supplémentaires :

4. **Quelle est la limite du point x=3 ?**

Dans cette notation, nous demandons quelle est la valeur de la fonction y lorsque x se rapproche très près de 1. Imaginez x à 1.99999999999999 ou 2.00000000000001. Il se rapproche tellement que nous pouvons le considérer comme suffisamment proche.

5. **Quelle est la limite du point x=4 ?**

C'est 0.

6. **Quelle est la limite du point x=5 ?**

C'est 3.

Maintenant, regardons un autre exemple :

![Exemple d'une fonction qui n'est pas continue en un point x=2](https://cdn.hashnode.com/res/hashnode/image/upload/v1756403617161/b67b2977-8ae4-4c06-8156-d7c6a64ee2e1.png align="center")

Au point x=2, elle n'est pas bien définie

* Si nous traçons avec un crayon de la gauche à x=2, nous obtenons 1.83333

* Si nous traçons avec un crayon de la droite à x=2, nous obtenons 4

### Pourquoi les limites sont-elles importantes pour comprendre les dérivées et les intégrales ?

Comme nous l'avons vu, lorsque nous parlons de limites, nous parlons d'une valeur qui symbolise la valeur qu'une fonction approche lorsqu'elle se dirige vers un point particulier.

Il est crucial de noter que nous ne regardons pas la valeur de ce point lui-même. Nous regardons ce qui se passe lorsque nous nous en approchons si près que nous pouvons déterminer quelle valeur la fonction approche.

Je vais maintenant montrer un exemple très simple pour démontrer ce concept en utilisant la notation mathématique.

Je sais que les limites peuvent être un concept difficile à comprendre au premier abord. Mais si vous comprenez bien les limites, alors vous serez bien préparé pour comprendre les dérivées et les intégrales.

Et, comme vous le verrez, les dérivées sont responsables de l'IA moderne et les intégrales sont des parties importantes des outils largement utilisés dans des industries de plusieurs milliards de dollars.

Je veux que vous compreniez l'**intuition** derrière cela.

La fonction z(x) est continue :

$$z(x) = \frac{3x + 7}{x + 2}$$

**Vers quelle valeur cette expression converge-t-elle lorsque x approche l'infini ?**

Si vous avez des connaissances en mathématiques, vous pourriez voir pourquoi. Mais voici pour ceux qui ne sont pas sûrs :

* Elle converge vers 3.

Cette fois, la limite approchera l'infini au lieu d'une constante :

$$\begin{align} \lim_{x \to \infty} \frac{3x + 7}{x + 2} \end{align}$$

Résolvons cela de manière très simple :

* Pour x = 1 :

$$f(1) = \frac{3(1) + 7}{1 + 2} = \frac{10}{3} \approx 3.333...$$

* Pour x = 5 :

$$f(5) = \frac{3(5) + 7}{5 + 2} = \frac{22}{7} \approx 3.143...$$

* Pour x = 10 :

$$f(10) = \frac{3(10) + 7}{10 + 2} = \frac{37}{12} \approx 3.083...$$

* Pour x = 50 :

$$f(50) = \frac{3(50) + 7}{50 + 2} = \frac{157}{52} \approx 3.019...$$

* Pour x = 100 :

$$f(100) = \frac{3(100) + 7}{100 + 2} = \frac{307}{102} \approx 3.010...$$

* Pour x = 1000 :

$$f(1000) = \frac{3(1000) + 7}{1000 + 2} = \frac{3007}{1002} \approx 3.001...$$

* Pour x = 10000 :

$$f(10000) = \frac{3(10000) + 7}{10000 + 2} = \frac{30007}{10002} \approx 3.0001...$$

À mesure que x devient de plus en plus grand, nous nous rapprochons de plus en plus de 3.

C'est l'idée principale des limites : décrire la valeur qu'une fonction approche lorsque l'entrée approche un certain point.

Cette même idée s'applique aux dérivées : elles ne sont que des limites qui mesurent les taux de changement (pentes des lignes tangentes).

Et de même, les intégrales ne sont que des limites qui mesurent les quantités accumulées (aires sous les courbes).

Maintenant, voyons comment les dérivées fonctionnent en profondeur.

### Dérivées : Comment les choses changent et à quelle vitesse

Comme je l'ai dit auparavant, les dérivées ne sont que des limites qui mesurent les taux de changement (pentes des lignes tangentes).

Mais que signifie cela réellement ?

Regardons un exemple :

![Exemple d'une fonction](https://cdn.hashnode.com/res/hashnode/image/upload/v1756755419750/75b36254-0f4a-4395-8dd4-14ac16399ff3.png align="center")

**Quel est le taux de changement au point A ?**

Question difficile, n'est-ce pas ? Réfléchissons à comment y répondre avec les limites.

Nous pouvons trouver la limite du taux de changement au point A(0.72, 0.66), également appelée le taux de changement instantané.

Faisons cela :

![Exemple d'une fonction et choix de deux points (B et C) pour trouver le taux de changement au point A](https://cdn.hashnode.com/res/hashnode/image/upload/v1756755680672/40f94361-55c7-4a9e-bfaf-b2b855fa0712.png align="center")

Pour trouver la pente, nous prenons les coordonnées des points B(0.2, 0.2) et C(1.6, 1) :

$$\text{pente} = \frac{1 - 0.2}{1.6 - 0.2} = \frac{0.8}{1.4} = \frac{4}{7} \approx 0.571$$

Cela nous donne un taux de changement :

$$y=0.571x + 0.084$$

Approximons davantage :

![Exemple d'une fonction et choix de deux points (B et C) pour trouver le taux de changement au point A. Mais B et C sont plus proches de A.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756756069833/3a4a1991-4983-4751-a68e-68bd6780300d.png align="center")

Zoomons également :

![Exemple d'une fonction et choix de deux points (B et C) pour trouver le taux de changement au point A. Mais B et C sont plus proches de A, et nous devons zoomer.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756756131072/f96b7f82-a4ed-4720-8c87-fd2936bae9d9.png align="center")

Pour trouver la pente, nous utilisons les coordonnées des points B(0.58, 0.55) et C(0.85, 0.75) :

$$\text{pente} = \frac{0.85- 0.58}{0.75 - 0.55} = \frac{0.27}{0.2} = \frac{2.7}{2} \approx 1.35$$

Cela nous donne un taux de changement :

$$y=1.35x + 0.11$$

Maintenant, approximons beaucoup :

![Exemple d'une fonction et choix de deux points (B et C) pour trouver le taux de changement au point A. Mais B et C sont plus proches de A, et nous devons zoomer.](https://cdn.hashnode.com/res/hashnode/image/upload/v1756756879223/11d26af3-06ec-4419-b631-10308b4cadef.png align="center")

Pour trouver la pente, nous utilisons les coordonnées des points B(0.7242549, 0.6625776) et C(0.7242884, 0.66260026) :

$$\text{pente} = \frac{0.66260026- 0.6625776}{0.7242884- 0.7242549} = \frac{0.0000226}{0.0000335} = \frac{0.226}{0.335} \approx 0.674$$

Maintenant, zoomons en arrière :

![Taux de changement au point C](https://cdn.hashnode.com/res/hashnode/image/upload/v1756757322888/a6f58b41-d6ff-44fd-b18f-06fb1f8f0e06.png align="center")

Comme nous pouvons le voir, nous sommes si proches que nous pouvons considérer la limite du taux de changement comme étant 0.65.

Cela nous donne le taux de changement :

$$y=0.674x + 0.12$$

**De cette manière, la limite d'un taux de changement est appelée une dérivée.**

Pour résumer, voici une animation :

![GIF animation basé sur les images précédentes](https://cdn.hashnode.com/res/hashnode/image/upload/v1756766733257/a1754b47-7c57-4387-8b4c-886ed7b8f80a.gif align="center")

Voici un exemple de code Python qui vous permet de trouver la dérivée au point A :

```python
import sympy as sp

x = sp.symbols('x')
f = sp.sin(x)

# Dérivée de sin(x)
derivative_of_sin = sp.diff(f, x)

# Évaluer à x = 0.72 et x = 0.66
val = f_prime.subs(x, 0.72).evalf()

print("Dérivée de sin(x) à x=0.72:", val)
```

![Image de l'exemple de code pour trouver la dérivée de la fonction sin(x)](https://cdn.hashnode.com/res/hashnode/image/upload/v1756758436107/3bda58c5-96d6-4834-a2ec-ab8fedc4cb56.png align="center")

La fonction qui avait le point A est appelée une onde sinusoïdale.

Nous la convertissons en sa fonction dérivée. À partir de là, nous avons notre taux de changement au point 0.72.

Lorsque nous faisons des mathématiques à la main, **nous avons généralement de nombreuses règles pour convertir une fonction en sa dérivée, et à partir de celles-ci trouver le taux de changement pour un point donné.**

Avant de le voir, regardons un exemple très simple pour comprendre la définition d'une dérivée :

$$\frac{d}{dx}f(x) \approx \frac{f(\textcolor{green}{x + h}) - f(\textcolor{red}{x - h})}{\textcolor{green}{x + h} - \textcolor{red}{x - h}} = \frac{f({x + h}) - f({x - h})}{2h}$$

![Image montrant dans la définition de la dérivée comment chaque composant est lié visuellement à une ligne représentant le taux de changement](https://cdn.hashnode.com/res/hashnode/image/upload/v1756767749954/87486d8c-9437-460c-b556-e9333b1590c5.png align="center")

`h` représente une petite différence.

La dérivée est la pente du petit changement de la fonction près d'un point. En d'autres termes, c'est la limite du taux de changement d'un point donné.

Une simple transformation de dérivée pourrait ressembler à ceci :

$$\frac{d}{dx}x^n = nx^{n-1}$$

Deux exemples sont :

$$\frac{d}{dx}x^3 = 3x^2$$

Et :

$$\frac{d}{dx}x^5 = 5x^4$$

Il y en a beaucoup d'autres. Mais nous n'entrerons pas dans les détails profonds de ce sujet.

#### Où et pourquoi les dérivées sont-elles si importantes ?

Les dérivées sont l'un des outils mathématiques les plus importants qui existent. Elles servent de fondation pour comprendre le changement dans presque tous les domaines des STEM.

En physique (mécanique classique), les dérivées sont très importantes pour trouver de nouvelles informations qui s'appuient sur des informations déjà disponibles.

Par exemple, connaître comment la position d'un corps change au fil du temps nous permet d'utiliser les dérivées pour trouver sa vitesse et son accélération. Cela est crucial pour les voitures autonomes, les trains, les fusées, et plus encore.

De plus, les dérivées sont la fondation de la compréhension de la manière dont l'électricité fonctionne en profondeur. Sans les dérivées, il n'y aurait pas eu de théorie électromagnétique. Sans la théorie électromagnétique, la technologie moderne n'existerait pas.

En apprentissage automatique, les dérivées sont si importantes qu'elles ont servi à créer l'algorithme qui est l'un des composants les plus importants de ChatGPT et d'autres modèles d'IA. (rétropropagation).

La rétropropagation est en fait si importante que ses créateurs, John Hopfield et Geoffrey Hinton, ont remporté le prix Nobel de physique 2024 pour cela.

De plus, les véhicules autonomes comme Tesla et Waymo utilisent des modèles d'IA appelés réseaux de neurones qui dépendent de la rétropropagation pour fonctionner.

C'est incroyable qu'un concept mathématique créé au 17ème siècle soit maintenant l'une des fondations de la révolution actuelle de l'IA.

### Qu'en est-il du calcul intégral ?

Avant d'expliquer davantage les dérivées, je vais vous poser une question :

Comment pouvons-nous trouver l'aire de la forme ci-dessous ?

![Image d'une intégrale finie de la fonction sin(x)](https://cdn.hashnode.com/res/hashnode/image/upload/v1764401826343/2583b3b0-0bcd-4204-921e-300b27c9fc3d.png align="center")

En d'autres termes, comment pouvons-nous trouver l'intégrale de la fonction dans l'intervalle donné ?

Voyons comment le faire étape par étape.

Tout d'abord, nous allons essayer d'utiliser 2 rectangles pour approximer l'aire derrière la courbe :

![Utilisation de 2 rectangles pour essayer de trouver l'aire sous la courbe](https://cdn.hashnode.com/res/hashnode/image/upload/v1764402058848/5023772e-ed0d-4efc-a5cd-3e1a856f6d69.png align="center")

Maintenant, l'aire des rectangles est 6.282573.

Mais il y a encore beaucoup d'erreur...

Comme nous pouvons le voir, le rectangle de gauche ne couvre pas complètement la courbe et le rectangle de droite couvre trop.

Nous allons donc ajouter plus de petits rectangles afin de mieux approximer la courbe.

Maintenant, essayons d'utiliser 4 rectangles :

![Utilisation de 4 rectangles pour essayer de trouver l'aire sous la courbe](https://cdn.hashnode.com/res/hashnode/image/upload/v1764483444354/c06cd1c2-0f92-4728-898e-fbaf1534d57f.png align="center")

Maintenant, l'aire est 6.497481. Mais il y a encore une certaine erreur.

Comme nous pouvons le voir, l'erreur devient plus petite. En d'autres termes, les 4 rectangles couvrent l'aire de la courbe mieux que les 2 rectangles. Mais il y a encore beaucoup de place pour l'améliorer.

Essayons d'utiliser 8 rectangles :

![Utilisation de 8 rectangles pour essayer de trouver l'aire sous la courbe](https://cdn.hashnode.com/res/hashnode/image/upload/v1764402069389/e9ad0576-dd9d-4535-bf3a-4c4bcd77db98.png align="center")

Maintenant, l'aire est 6.604935.

Et si nous utilisons 16 rectangles ?

![Utilisation de 16 rectangles pour essayer de trouver l'aire sous la courbe](https://cdn.hashnode.com/res/hashnode/image/upload/v1764402075078/6ad6278f-4b71-411b-8552-2554152a04cb.png align="center")

Maintenant, l'aire est 6.658662.

Essayons d'utiliser 32 rectangles :

![Utilisation de 32 rectangles pour essayer de trouver l'aire sous la courbe](https://cdn.hashnode.com/res/hashnode/image/upload/v1764402079649/4e673391-7e7a-4ca3-b07a-22508c5b058e.png align="center")

Maintenant, l'aire est 6.685525.

Maintenant, essayons d'utiliser 64 rectangles :

![Utilisation de 64 rectangles pour essayer de trouver l'aire sous la courbe](https://cdn.hashnode.com/res/hashnode/image/upload/v1764402084920/4851d710-ff9d-4562-ba7d-9b759473f577.png align="center")

Maintenant, l'aire est 6.698957.

Et en utilisant 128 rectangles :

![Utilisation de 128 rectangles pour essayer de trouver l'aire sous la courbe](https://cdn.hashnode.com/res/hashnode/image/upload/v1764402090280/bd5b139c-58e1-4a7a-869d-5107b7eff345.png align="center")

Maintenant, l'aire est 6.705673.

Qu'en est-il d'utiliser 256 rectangles :

![Utilisation de 256 rectangles pour essayer de trouver l'aire sous la courbe](https://cdn.hashnode.com/res/hashnode/image/upload/v1764402098061/3ee50020-0143-42b1-aea7-8c762aa33e53.png align="center")

Maintenant, l'aire est 6.709031. Et l'erreur a atteint 0.0000 !

Maintenant, regardons une animation de cela :

![GIF animation des rectangles de 2 à 256 pour représenter l'intégrale finie](https://cdn.hashnode.com/res/hashnode/image/upload/v1764402052869/e9a54332-75b5-4e46-90cc-3bc09e636ad3.gif align="center")

Comme vous pouvez le voir, nous pouvons approximer l'aire en ayant une limite à l'infini du nombre de rectangles pour approximer l'aire.

De cette manière, nous pouvons conclure que :

$$F(x) = \int_0^{3.14} f(x) \, dx = \int_0^{3.14} (\sin(x) + 1.5) \, dx = 6.71$$

Cela signifie que l'aire entre 0 et 3.14, limitée par l'équation mathématique, est 6.71 !

Ou, mathématiquement, l'intégrale de f(x) dans l'intervalle 0 et 3.14 est 6.71.

#### Où et comment cela est-il appliqué ?

En génie électrique, les intégrales calculent l'utilisation totale d'énergie dans les circuits en intégrant la puissance sur le temps. Par exemple, lors de la conception d'une alimentation pour un appareil, les ingénieurs intègrent la puissance pour déterminer les coûts énergétiques totaux et les exigences d'absorption de chaleur.

En d'autres termes, ils voient l'aire sur le temps et combien de puissance est utilisée.

Regardons un exemple :

![Image d'intégrale](https://cdn.hashnode.com/res/hashnode/image/upload/v1764832775180/911672dd-05ff-47c7-ac5f-81f4933c96ff.png align="center")

Imaginez que dans l'image ci-dessus :

* L'axe X peut être le temps en mois.

* L'axe Y est la puissance utilisée en Watts (Joules par seconde).

Nous pouvons conclure qu'en 3.14 mois (3 mois et 4 jours), la quantité totale d'énergie est 6.71 watt-mois.

Voici le code pour le découvrir :

```plaintext
# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Create Function
x = np.linspace(0, 3.14, 100)
y = np.sin(x) + 1.5

# Find the area under the function
area = np.trapezoid(y, x)

# Show the final image
plt.fill_between(x, y)
plt.title(f'Area = {area:.2f}')
plt.show()
```

![Code pour trouver l'intégrale finie de la fonction sin entre deux points](https://cdn.hashnode.com/res/hashnode/image/upload/v1765435075995/defc251b-812c-44ae-8b67-9a323c0af040.png align="center")

Dans ce code, nous importons les bibliothèques, créons la fonction, et trouvons l'aire et la traçons.

Nous avons utilisé numpy.trapezoid pour trouver l'aire, car c'est une approximation numérique pour trouver rapidement l'intégrale d'une fonction entre deux valeurs x.

numpy.trapezoid utilise une méthode d'approximation numérique appelée la **règle trapézoïdale composite.**

L'idée de base de la règle trapézoïdale composite est de diviser l'aire sous la courbe en de nombreux trapèzes et de les sommer tous.

Si vous voulez en savoir plus sur cela, je recommande de lire la [documentation NumPy sur cette méthode](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html).

À partir de cette valeur, nous pouvons convertir vers d'autres unités :

* 52,400,000 joules

* 14.6 kWh

En convertissant vers d'autres unités, nous pouvons plus facilement comparer cet appareil avec d'autres appareils et voir s'il obéit à des normes et lois techniques.

**Ceci est une application réelle des intégrales en ingénierie.**

Dans mon diplôme, j'ai utilisé cela beaucoup dans des cours liés au génie électrique. En termes simples, le génie électrique est un sous-domaine du génie électrique axé sur le travail avec l'électricité avec des valeurs de tension très élevées et des moteurs électriques.

En compression audio, la transformée de Fourier (construite sur des intégrales) décompose les ondes sonores en composantes de fréquence. Les encodeurs MP3 utilisent cela pour identifier et supprimer les fréquences que les humains ne peuvent pas entendre. Cela réduit les tailles de fichiers tout en préservant la qualité.

L'imagerie médicale repose sur la transformée de Radon, qui utilise des intégrales pour reconstruire des images 3D à partir de projections de rayons X 2D. Lorsque vous passez un scanner CT, la machine prend des centaines de "tranches" de rayons X à différents angles. Pendant ce processus, les intégrales combinent les "tranches" en une image transversale détaillée de votre corps.

### Applications en IA et théorie du contrôle : le calcul en action

L'IA moderne dépend des dérivées qui utilisent l'algorithme de rétropropagation.

Lors de l'entraînement d'un réseau de neurones, le système calcule les dérivées partielles de l'erreur par rapport à des millions de paramètres. De cette manière, il découvre comment ajuster chaque poids pour améliorer les performances. Sans cela, les grands modèles de langage comme ChatGPT ne pourraient pas apprendre à partir des données.

Les contrôleurs PID, qui stabilisent la température dans votre four ou maintiennent l'altitude dans les systèmes de pilote automatique des aéronefs, combinent des idées de calcul :

* Le terme proportionnel répond à l'erreur actuelle.

* Le terme intégral accumule les erreurs passées pour éliminer la dérive en régime permanent.

* Le terme dérivé prédit les tendances futures pour éviter les dépassements.

Et ce ne sont là que quelques-unes des applications du calcul !

## Chapitre 6 : Probabilité & Statistiques - Apprendre de l'incertitude

![De nombreux dés violets ensemble](https://cdn.hashnode.com/res/hashnode/image/upload/v1765002445093/b606e188-969e-49d8-9be9-9c15330a2939.jpeg align="center")

[Photo par Armando Are](https://www.pexels.com/photo/purple-dices-with-different-geometrical-shape-on-a-white-surface-3649115/)

C'est grâce aux probabilités et aux statistiques que de nombreuses industries ont tant grandi. Avec les statistiques, nous pouvons prendre des décisions éclairées et optimiser de nombreux processus différents. Avec les probabilités, nous pouvons comprendre et modéliser l'incertitude dans les systèmes et, de cette manière, résoudre ou même éviter des problèmes.

Bien que vous soyez peut-être familier avec certains des concepts clés comme la médiane et la moyenne, nous commencerons par quelques bases pour construire votre intuition sur des sujets plus avancés comme le théorème central limite, le théorème de Bayes et les chaînes de Markov.

### Moyenne, Médiane, Mode : Mesurer la tendance centrale

Imaginons que vous êtes un scientifique des données travaillant dans la recherche. Vous allez travailler avec des données pour optimiser la production des fermes dans la Central Valley en Californie.

L'idée est de prendre un ensemble de données, et en l'étudiant, vous pouvez aider les agriculteurs à prendre de meilleures décisions.

Voici les données d'une année d'activité :

| Ferme | Rendement (tonnes/ha) | Engrais utilisé (kg/ha) | Précipitations (mm) |
| --- | --- | --- | --- |
| A | 4,2 | 150 | 280 |
| B | 5,8 | 220 | 420 |
| C | 3,9 | 120 | 230 |
| D | 6,1 | 250 | 480 |
| E | 4,7 | 200 | 340 |
| F | 5,3 | 200 | 390 |

Nous avons 6 fermes dans notre ensemble de données. Pour chaque ferme, nous savons :

* Combien de rendement a été obtenu en tonnes par hectare

* Combien d'engrais a été utilisé en kilogrammes par hectare

* Combien de précipitations il y a eu pendant une année d'activité

Maintenant, répondons à quelques questions que nous pourrions avoir sur les données pour comprendre la **moyenne**, le **mode** et la **médiane** :

#### 1. Quelle est la moyenne du rendement pendant une année d'activité ?

Pour trouver la moyenne, nous devons simplement additionner toutes les valeurs de rendement et diviser par le nombre de fermes. Comme ceci :

$$\text{Moyenne} = \frac{4,2 + 5,8 + 3,9 + 6,1 + 4,7 + 5,3}{6} = \frac{30}{6} = 5$$

C'est ce qu'on appelle la moyenne. La moyenne est simplement la somme de toutes les valeurs divisée par le nombre de valeurs.

En Python, nous pouvons faire ce qui suit pour calculer la moyenne :

```plaintext
def calculer_moyenne(valeurs):
    return sum(valeurs) / len(valeurs)

# Exemple d'utilisation
données = [4.2, 5.8, 3.9, 6.1, 4.7, 5.3]
résultat = calculer_moyenne(données)
print(f"Moyenne : {résultat}")
```

![Code Python dans une image montrant comment trouver la moyenne](https://cdn.hashnode.com/res/hashnode/image/upload/v1763102054838/b5619d92-95ca-4c50-bb32-39d6e8e7ba7b.png align="center")

#### 2. Quel est le mode de l'engrais utilisé ?

Le mode est simplement la valeur la plus fréquente dans un ensemble de données donné. Dans notre cas, c'est **200** puisque c'est la valeur la plus courante qui apparaît dans notre ensemble de données de fermes.

En Python, nous pouvons faire ceci pour calculer le mode :

```plaintext
import statistics

def calculer_mode(valeurs):
    return statistics.mode(valeurs)

# Exemple d'utilisation
données = [150, 220, 120, 250, 200, 200]
résultat = calculer_mode(données)
print(f"Mode : {résultat}")
```

![Code Python dans une image montrant comment trouver le mode](https://cdn.hashnode.com/res/hashnode/image/upload/v1763102576660/3ca71e03-f762-44ad-85c3-8ccb4cb1db54.png align="center")

#### 3. Quelle est la médiane du rendement ?

La médiane est simplement la valeur au milieu d'un ensemble de nombres. Si le nombre d'éléments dans la liste est pair, nous prenons la moyenne des deux nombres du milieu. Voici nos valeurs de rendement actuelles :

$$4,2, 5,8, 3,9, 6,1, 4,7, 5,3$$

Tout d'abord, nous trions les valeurs :

$$3,9, 4,2, 4,7, 5,3, 5,8, 6,1$$

Puisque nous avons 6 valeurs (nombre pair), la médiane est la moyenne des deux valeurs du milieu :

$$\text{Médiane} = \frac{4,7 + 5,3}{2} = \frac{10}{2} = 5$$

En Python, nous pouvons faire ceci pour calculer la médiane :

```plaintext
import statistics

def calculer_médiane(valeurs):
    return statistics.median(valeurs)

# Exemple d'utilisation
données = [4.2, 5.8, 3.9, 6.1, 4.7, 5.3]
résultat = calculer_médiane(données)
print(f"Médiane : {résultat}")
```

![Code Python dans une image montrant comment trouver la médiane](https://cdn.hashnode.com/res/hashnode/image/upload/v1763102389405/52e5009b-6bc8-42c5-b8da-efe8c372fe96.png align="center")

### Variance et écart-type : Mesurer la dispersion

Connaître la moyenne, le mode et la médiane des données est utile. Mais il est également important de savoir à quel point les points de données sont éloignés les uns des autres.

C'est là que les mesures de [dispersion](https://en.wikipedia.org/wiki/Statistical_dispersion) entrent en jeu. La variance nous indique, en moyenne, à quel point les nombres sont éloignés de la moyenne.

Regardons un exemple de la façon de calculer cela.

Étant donné les données de rendement du tableau :

$$4,2, 5,8, 3,9, 6,1, 4,7, 5,3$$

La première étape consiste à calculer la moyenne :

$$\bar{x} = \frac{4,2 + 5,8 + 3,9 + 6,1 + 4,7 + 5,3}{6} = \frac{30}{6} = 5$$

La deuxième étape consiste à calculer la variance avec la formule de la variance de l'échantillon :

$$s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}$$

Appliquons la formule peu à peu pour comprendre comment elle fonctionne.

Nous allons d'abord calculer la variance de chaque point de données de rendement :

$$\begin{align*} (4,2 - 5,0)^2 &= (-0,8)^2 = 0,64 \\ (5,8 - 5,0)^2 &= (0,8)^2 = 0,64 \\ (3,9 - 5,0)^2 &= (-1,1)^2 = 1,21 \\ (6,1 - 5,0)^2 &= (1,1)^2 = 1,21 \\ (4,7 - 5,0)^2 &= (-0,3)^2 = 0,09 \\ (5,3 - 5,0)^2 &= (0,3)^2 = 0,09 \end{align*}$$

Ensuite, nous additionnons toutes les différences au carré :

$$\sum(x_i - \bar{x})^2 = 0,64 + 0,64 + 1,21 + 1,21 + 0,09 + 0,09 = 3,88$$

Maintenant, nous trouvons enfin la variance :

$$s^2 = \frac{3,88}{6-1} = \frac{3,88}{5} = 0,776$$

L'écart-type est simplement la racine carrée de la variance.

$$s = \sqrt{s^2} = \sqrt{0,776} \approx 0,881 tonnes/ha$$

Pourquoi est-ce utile ?

Cela ramène la dispersion aux mêmes unités que les données, ce qui facilite l'interprétation.

Un petit écart-type signifie que les données se regroupent près de la moyenne, tandis qu'un grand écart-type signifie qu'elles sont largement dispersées.

Et voici un exemple de code de la façon de calculer les deux :

```plaintext
import statistics

def calculer_variance_et_écart_type(valeurs):
    variance = statistics.variance(valeurs)
    écart_type = statistics.stdev(valeurs)
    return variance, écart_type

# Exemple d'utilisation
données = [4.2, 5.8, 3.9, 6.1, 4.7, 5.3]
variance, écart_type = calculer_variance_et_écart_type(données)
print(f"Variance : {variance}")
print(f"Écart-type : {écart_type}")
```

![Code Python dans une image montrant comment trouver la variance et l'écart-type](https://cdn.hashnode.com/res/hashnode/image/upload/v1763102806607/a8236667-e4b0-48a5-9171-544c4b94096e.png align="center")

### Qu'est-ce que la distribution normale ? La courbe en cloche de la vie

La distribution normale nous indique comment les données convergent naturellement autour de la valeur moyenne. La plupart des valeurs sont concentrées au centre, et les valeurs extrêmes sont plus vers les bords. Cela crée une courbe en cloche.

En comprenant cette distribution, nous pouvons comprendre d'autres distributions et également le théorème central limite.

Pour comprendre ce qu'est la distribution normale, regardons-la :

![Image représentant la distribution normale](https://cdn.hashnode.com/res/hashnode/image/upload/v1763529094535/f90ffdb8-543e-4d1f-9627-335e8f356512.png align="center")

La distribution normale ressemble à une montagne.

Comme vous pouvez le voir, la plupart des valeurs sont autour de la moyenne. De plus, autour de la moyenne se trouve le pic. Vers les extrêmes, la courbe devient de plus en plus basse. Cela signifie que dans les extrêmes, il y a de moins en moins de valeurs.

La distribution normale a également une formule qui lui est associée :

$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right)$$

Je n'entrerai pas dans les détails de la façon dont la formule fonctionne ici. Je veux simplement que vous compreniez l'idée principale derrière le concept.

Il existe de nombreuses autres distributions en plus de la distribution normale. Certaines des plus courantes sont :

* Distribution du chi carré

* Distribution t de Student

* Distribution de Bernoulli

* Distribution binomiale

* Distribution de Poisson

Chaque distribution peut modéliser différents événements et phénomènes. Par exemple, la distribution du chi carré est largement utilisée pour trouver la corrélation entre deux phénomènes (comme les coups de soleil et le cancer de la peau, par exemple).

La distribution de Poisson est également utilisée pour modéliser les comptes d'événements, comme le nombre de clients qui entrent dans un magasin par heure ou le nombre de paquets de données qui sont transmis dans un câble Ethernet.

Mais il est également possible d'approximer de nombreuses distributions à la distribution normale en utilisant l'un des théorèmes les plus importants de toutes les mathématiques : le théorème central limite. C'est ce que nous allons explorer ensuite.

### Comment le théorème central limite aide à approximer le monde

![Personne tenant une petite version du monde dans sa main](https://cdn.hashnode.com/res/hashnode/image/upload/v1766902263857/9a03bb38-a7b9-4ef0-93f2-a7e0d80bd249.jpeg align="center")

Photo par [Porapak Apichodilok](https://www.pexels.com/photo/person-holding-world-globe-facing-mountain-346885/)

L'idée principale du théorème central limite est très simple :

* La plupart des distributions peuvent être approximées pour devenir la distribution normale.

C'est un peu comme verser du sable dans un entonnoir. Les grains peuvent tomber aléatoirement, mais avec le temps, le tas de sable commencera toujours à former la forme d'une montagne.

Ainsi, nous pouvons prendre de nombreux points de données et les moyenner. Avec le temps, cela convergera pour devenir une distribution normale.

En d'autres termes, lorsque des variables aléatoires indépendantes sont toutes additionnées, leur somme tend vers une distribution normale.

Voici la formule :

$$\bar{X} \approx N\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{ou de manière équivalente} \quad Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \approx N(0, 1)$$

Vous n'avez pas besoin de comprendre en profondeur ce que cela signifie. Comprenez simplement que c'est un théorème qui approxime d'autres distributions à la distribution normale.

#### Et pourquoi est-ce important ?

Parce que ce théorème rend possibles de nombreuses industries de plusieurs milliards de dollars.

Au lieu de tester chaque scénario possible, nous pouvons tester un plus petit nombre de scénarios et supposer que si cela fonctionne pour le plus petit, cela fonctionnera pour le plus grand.

Par exemple, dans les télécommunications, au lieu de tester chaque appel téléphonique ou transmission de données possible, nous pouvons simplement tester quelques connexions. Si cela fonctionne pour ces quelques connexions, nous pouvons supposer que cela fonctionnera pour des millions d'appels téléphoniques et de transmissions de données.

Pour les essais cliniques, au lieu de tester un médicament sur des millions de personnes, nous pouvons simplement tester un plus petit nombre de patients. Si cela fonctionne pour un (relativement) petit nombre de patients, nous pouvons supposer que cela fonctionnera pour la plupart des personnes atteintes de la même condition.

Sans cette idée, les essais cliniques ne seraient pas possibles. Il en va de même pour les télécommunications et tant d'autres domaines de l'ingénierie.

### Théorème de Bayes : Apprendre à partir des preuves

Maintenant, nous allons commencer à examiner la probabilité plus en profondeur en nous basant sur le tableau de données que nous avons utilisé.

Voici à nouveau le tableau pour que vous puissiez vous y référer plus facilement :

<table><tbody><tr><td colspan="1" rowspan="1"><p>Ferme</p></td><td colspan="1" rowspan="1"><p>Rendement (tonnes/ha)</p></td><td colspan="1" rowspan="1"><p>Engrais utilisé (Kg/ha)</p></td><td colspan="1" rowspan="1"><p>Précipitations (mm)</p></td></tr><tr><td colspan="1" rowspan="1"><p>A</p></td><td colspan="1" rowspan="1"><p>4,2</p></td><td colspan="1" rowspan="1"><p>150</p></td><td colspan="1" rowspan="1"><p>280</p></td></tr><tr><td colspan="1" rowspan="1"><p>B</p></td><td colspan="1" rowspan="1"><p>5,8</p></td><td colspan="1" rowspan="1"><p>220</p></td><td colspan="1" rowspan="1"><p>420</p></td></tr><tr><td colspan="1" rowspan="1"><p>C</p></td><td colspan="1" rowspan="1"><p>3,9</p></td><td colspan="1" rowspan="1"><p>120</p></td><td colspan="1" rowspan="1"><p>230</p></td></tr><tr><td colspan="1" rowspan="1"><p>D</p></td><td colspan="1" rowspan="1"><p>6,1</p></td><td colspan="1" rowspan="1"><p>250</p></td><td colspan="1" rowspan="1"><p>480</p></td></tr><tr><td colspan="1" rowspan="1"><p>E</p></td><td colspan="1" rowspan="1"><p>4,7</p></td><td colspan="1" rowspan="1"><p>200</p></td><td colspan="1" rowspan="1"><p>340</p></td></tr><tr><td colspan="1" rowspan="1"><p>F</p></td><td colspan="1" rowspan="1"><p>5,3</p></td><td colspan="1" rowspan="1"><p>200</p></td><td colspan="1" rowspan="1"><p>390</p></td></tr></tbody></table>

Il existe de nombreuses idées et formules liées aux probabilités. Mais ici, je veux vous expliquer les concepts clés qui sont appliqués en IA et vous donner une définition de haut niveau des choses.

Nous commencerons par la probabilité conditionnelle, qui est fondamentale pour comprendre le théorème de Bayes. Ensuite, nous aborderons la formule étendue du théorème de Bayes.

Alors, commençons !

#### Qu'est-ce que la probabilité conditionnelle ?

![Image d'une personne jouant aux échecs avec les pièces noires](https://cdn.hashnode.com/res/hashnode/image/upload/v1766903189931/420cc60a-71cd-4c37-ab0a-f8aebe825ca7.jpeg align="center")

Photo par [KOUSHIK BALA](https://www.pexels.com/photo/black-and-yellow-chess-pieces-3830671/)

La probabilité conditionnelle est la probabilité qu'un événement se produise étant donné qu'un autre événement s'est déjà produit.

Confus ? Ne vous inquiétez pas ! Regardons un exemple :

Supposons que :

* A = La ferme a des précipitations supérieures ou égales à 400 mm

* B = La ferme a un rendement supérieur ou égal à 5,0 tonnes/ha

Voici la formule pour la probabilité conditionnelle :

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

Maintenant, regardons cette formule plus en détail :

$$P(A)$$

Cela représente la probabilité qu'une ferme ait des précipitations supérieures ou égales à 400 mm.

Nous avons 6 fermes, et 2 d'entre elles (fermes B et D) ont des précipitations supérieures ou égales à 400 mm.

Ainsi, la probabilité qu'une ferme ait des précipitations supérieures ou égales à 400 mm est :

$$P(A) = \frac{2}{6} = \frac{1}{3} \u2248 0,33$$

Maintenant, regardons pour l'événement B :

$$P(B)$$

Cela représente la probabilité qu'une ferme ait un rendement supérieur ou égal à 5,0 tonnes/ha.

Nous avons 6 fermes et 3 d'entre elles (fermes B, D et F) ont un rendement supérieur ou égal à 5,0 tonnes/ha.

Ainsi, la probabilité qu'une ferme ait un rendement supérieur ou égal à 5,0 tonnes/ha est :

$$P(B) = \frac{3}{6} = \frac{1}{2} = 0,5$$

Et si nous voulons voir les probabilités des deux conditions en même temps ?

$$P(A \cap B)$$

Cela fait référence à la probabilité que A et B soient tous deux vrais.

Dans notre exemple, cela signifie la probabilité qu'une ferme ait à la fois des précipitations supérieures ou égales à 400 mm **et** un rendement supérieur ou égal à 5,0 tonnes/ha.

Nous avons :

* 6 fermes et 2 d'entre elles (fermes B et D) ont des précipitations supérieures ou égales à 400 mm

* 6 fermes et 3 d'entre elles (fermes B, D et F) ont un rendement supérieur ou égal à 5,0 tonnes/ha

Pour que A et B soient vrais, seules 2 fermes (fermes B et D) ont les deux conditions.

Ainsi :

$$P(A \cap B) = \frac{2}{6} = \frac{1}{3} \u2248 0,33$$

Maintenant, nous sommes prêts à trouver la probabilité conditionnelle :

$$P(A|B)$$

Cela signifie la probabilité de A, sachant que B est vrai.

Dans notre exemple, nous pouvons conclure que :

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{0,33}{0,5} = 0,66$$

Ainsi, la probabilité qu'une ferme ait des précipitations supérieures ou égales à 400 mm – sachant qu'elle a un rendement supérieur ou égal à 5,0 tonnes/ha – est de 0,66.

#### Théorème de Bayes

C'est l'un des théorèmes les plus importants en mathématiques.

Le théorème de Bayes est une formule qui nous indique comment changer la probabilité d'une prédiction lorsque de nouvelles données vérifiées deviennent disponibles.

En d'autres termes, c'est comme une règle qui nous indique comment mettre à jour nos croyances lorsque de nouvelles preuves apparaissent.

Maintenant, sur la base de ce que nous savons déjà, voyons comment fonctionne le théorème de Bayes.

Voici sa formule :

$$P(B|A) = \frac{P(A|B) \cdot P(A)}{P(B)}$$

Maintenant, sur la base des valeurs précédentes, nous pouvons très facilement trouver la probabilité de B, étant donné que A est vrai.

En d'autres termes, la probabilité qu'une ferme ait un rendement supérieur ou égal à 5,0 tonnes/ha, sachant qu'elle a des précipitations supérieures ou égales à 400 mm.

Trouvons la réponse :

$$P(B|A) = \frac{P(A|B) \cdot P(A)}{P(B)}= \frac{0,66 \cdot 0,33}{0,5}=0,44$$

Ainsi, la probabilité qu'une ferme ait un rendement supérieur ou égal à 5,0 tonnes/ha, sachant qu'il a plu égal ou plus de 400 mm, est de 44 %.

Maintenant que nous avons passé en revue cette formule étape par étape, espérons qu'elle ne semble plus aussi complexe.

#### Où cela est-il appliqué dans la vie réelle ?

Comme pour de nombreuses idées mathématiques dans ce livre, le théorème de Bayes a des applications dans de nombreux secteurs d'activité.

Par exemple, quelle est la meilleure façon de créer un système de contrôle pour une voiture autonome, un robot ou vraiment tout autre appareil ?

Une approche efficace consiste à utiliser un [filtre de Kalman](https://en.wikipedia.org/wiki/Kalman_filter). Les filtres de Kalman reposent fortement sur le théorème de Bayes pour gérer les systèmes de contrôle avec des données incomplètes.

Les filtres de Kalman ont de nombreuses applications en ingénierie. Par exemple, grâce aux filtres de Kalman, les avions commerciaux peuvent voler en toute sécurité en pilote automatique.

Ainsi, comme vous pouvez le voir, le théorème de Bayes est la base de nombreux systèmes de contrôle utilisés dans des industries à risque.

### Que sont les modèles de Markov ? Prédire la prochaine étape, une étape à la fois

![Image de la main d'une personne lançant des dés en l'air](https://cdn.hashnode.com/res/hashnode/image/upload/v1766902389612/c80d7118-f13d-4f9b-a149-861db3f2037d.jpeg align="center")

Photo par [lil artsy](https://www.pexels.com/photo/person-about-to-catch-four-dices-1111597/)

Comment prédire l'avenir avec les mathématiques ? Les chaînes de Markov vous permettent de le faire dans une certaine mesure.

Pour cette raison, les chaînes de Markov sont largement utilisées en science, en ingénierie, en économie et dans de nombreux autres domaines.

En plus de cela, les processus de décision de Markov sont une base très importante pour l'apprentissage par renforcement. L'apprentissage par renforcement est une branche de l'IA où les agents apprennent à prendre des décisions en interagissant avec un environnement pour maximiser les récompenses.

Dans cette section, je vais vous présenter les chaînes de Markov et les processus de décision avec une analogie, une explication en anglais simple et un exemple de code.

Si vous souhaitez approfondir le sujet, je vous recommande mon [article freeCodeCamp sur le sujet](https://www.freecodecamp.org/news/what-is-a-markov-chain/).

#### Analogie de la chaîne de Markov

Imaginez que vous voulez prédire la météo de demain, et qu'elle **ne dépend** que de la météo d'aujourd'hui. La météo peut être soit ensoleillée, soit pluvieuse.

Voici les probabilités :

* S'il fait ensoleillé aujourd'hui, il y a 80 % de chances qu'il fasse à nouveau ensoleillé demain, et 20 % de chances qu'il pleuve.

* S'il pleut aujourd'hui, il y a 50 % de chances qu'il fasse ensoleillé demain, et 50 % de chances qu'il pleuve.

Dans ce scénario, nous pouvons prédire les états futurs de la météo en fonction des états actuels en utilisant des probabilités.

Cette idée de prédire l'avenir uniquement sur la base des probabilités du présent est appelée une chaîne de Markov.

Ici, les états sont soit ensoleillés, soit pluvieux, et les probabilités décrivent les chances que la météo change en fonction de l'état actuel.

#### Chaîne de Markov expliquée en anglais simple

Une chaîne de Markov décrit des processus aléatoires où les systèmes passent d'un état à l'autre, et un nouvel état ne dépend que de l'état actuel, et non de la façon dont il y est parvenu.

Mathématiquement, les chaînes de Markov sont appelées modèles stochastiques car elles modélisent (simulent) des événements de la vie réelle qui sont aléatoires par nature (stochastiques).

Les chaînes de Markov sont populaires car elles sont faciles à mettre en œuvre et efficaces pour modéliser des systèmes complexes.

Un autre avantage clé est leur propriété "sans mémoire". Cela les rend plus rapides à exécuter sur les ordinateurs et puissantes pour étudier les processus aléatoires et faire des prédictions basées sur les conditions actuelles.

#### Applications des chaînes de Markov
![Image d'un carré blanc avec une étoile sombre à l'intérieur, entouré de nombreux autres carrés sombres](https://cdn.hashnode.com/res/hashnode/image/upload/v1766902558494/8129d378-5cd8-4fdc-be48-8ba0a34181b7.jpeg align="center")

Photo par [Google DeepMind](https://www.pexels.com/photo/shapes-on-a-dark-background-25630338/)

À un certain niveau, presque tous les événements de la vie réelle sont stochastiques. En d'autres termes, ils impliquent de l'aléatoire et de l'incertitude.

C'est exactement pourquoi ils sont si largement utilisés.

Ils peuvent prédire le comportement des systèmes en fonction des conditions actuelles :

* En finance, ils sont utilisés pour détecter les changements dans les notations de crédit pour prévoir les régimes de marché.

* En génétique, ils aident à comprendre comment les protéines changent au fil du temps (ce qui est important lors de l'étude des variations génétiques).

Ces exemples concrets montrent à quel point les chaînes de Markov peuvent être efficaces pour résoudre des problèmes réels dans différents domaines.

En IA, les chaînes de Markov sont utilisées pour modéliser un environnement comme une usine ou une maison. La modélisation d'un environnement avec des chaînes de Markov est appelée un processus de décision de Markov.

En utilisant un processus de décision de Markov, il est possible d'utiliser l'apprentissage par renforcement pour créer et optimiser des agents afin qu'ils agissent dans l'environnement.

Bien sûr, de nouvelles et meilleures variantes du processus de décision de Markov sont apparues au fil des ans. Mais l'idée clé ici est que c'est grâce aux processus de décision de Markov que la base de l'apprentissage par renforcement existe.

L'apprentissage par renforcement est largement utilisé dans les systèmes publicitaires, la logistique, la robotique, les jeux vidéo et bien d'autres applications.

#### Types de chaînes de Markov

Il existe de nombreux types de chaînes de Markov. Dans cette section, nous ne discuterons que des variantes les plus importantes.

1. Chaînes de Markov à temps discret (DTMCs)

Dans les DTMCs, le système change d'état à des étapes de temps spécifiques. Elles sont appelées discrètes car les transitions d'état se produisent à des intervalles de temps distincts et séparés.

Elles sont utilisées dans la théorie des files d'attente (étude du comportement des files d'attente), la génétique et l'économie car elles sont simples à analyser.

2. Chaînes de Markov à temps continu (CTMCs)

Les CTMCs diffèrent des DTMCs en ce sens que les transitions d'état peuvent se produire à n'importe quel point dans le temps continu, et non à des intervalles fixes.

Cela en fait des modèles stochastiques où les changements d'état se produisent en continu. Cela est important dans les réactions chimiques et l'ingénierie de la fiabilité.

3. Chaînes de Markov réversibles

Les chaînes de Markov réversibles sont spéciales. Le processus de changement d'état est le même que la direction soit vers l'avant ou vers l'arrière, comme rembobiner une vidéo et la rejouer.

Cette propriété facilite la connaissance de la stabilité d'un système et l'étude du comportement d'un système au fil du temps. Elles sont largement utilisées en physique statistique et en économie.

4. Chaînes de Markov doublement stochastiques

Les chaînes de Markov doublement stochastiques sont définies par une matrice de probabilités de transition. Dans la matrice, la somme des probabilités dans chaque ligne et chaque colonne est égale à 1.

Cela signifie que chaque ligne et chaque colonne représentent une distribution de probabilités valide. En d'autres termes, chaque ligne et colonne représentent une liste de chances pour différents résultats.

Cette propriété est cruciale en informatique quantique et en mécanique statistique.

Grâce aux chaînes de Markov doublement stochastiques, les systèmes changent de manière à préserver les probabilités et la symétrie, rendant la modélisation et l'analyse des systèmes d'informatique quantique bien plus précises.

#### Exemple de code de chaînes de Markov cachées

![Image de lunettes, un ordinateur MAC et du code flou à l'intérieur](https://cdn.hashnode.com/res/hashnode/image/upload/v1766903059652/ad8c6509-87ae-4978-8b64-24146161d1cb.jpeg align="center")

Photo par [Kevin Ku](https://www.pexels.com/photo/data-codes-through-eyeglasses-577585/)

Avant de nous lancer dans des exemples de code, comprenons d'abord ce que sont les chaînes de Markov cachées.

L'idée principale derrière les chaînes de Markov cachées est de modéliser des systèmes qui ont des états cachés (états dont nous ne connaissons pas les valeurs) qui ne peuvent être découverts que par des événements observables.

En d'autres termes, les chaînes de Markov cachées nous permettent de prédire le comportement d'un système en :

* Considérant la probabilité de passer d'un état à un autre.

* Connaissant la probabilité d'observer un certain événement à partir de chaque état.

Nous pouvons comprendre cela en observant comment les états changent d'un point de vue indirect.

Nous ne connaissons peut-être pas les valeurs originales des états. Mais en connaissant la manière dont ils changent, nous pouvons prédire quelles seront leurs valeurs dans le futur.

Ainsi, les chaînes de Markov cachées sont flexibles pour modéliser des séquences, capturant à la fois les transitions entre les états cachés et les résultats observables.

Grâce à cela, les modèles de Markov cachés sont utilisés dans des domaines tels que l'ingénierie, la modélisation financière, la reconnaissance vocale, la bioinformatique, et bien d'autres.

#### Exemple de code :

Dans cet exemple de code, nous verrons un exemple simple avec des données synthétiques.

Voici le code complet :

```python
import numpy as np
from hmmlearn import hmm

# Définir la graine aléatoire pour la reproductibilité
np.random.seed(42)

# Définir les paramètres du HMM
n_components = 2  # Nombre d'états
n_features = 1    # Nombre de caractéristiques d'observation

# Créer un HMM gaussien
model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag")

# Définir la matrice de transition (les lignes doivent faire 1)
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])

# Définir les moyennes et les covariances pour chaque état
model.means_ = np.array([[0.0], [3.0]])
model.covars_ = np.array([[0.5], [0.5]])

# Générer des données d'observation synthétiques
X, Z = model.sample(100)  # 100 échantillons

# Créer une nouvelle instance de HMM
new_model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag", n_iter=100)

# Ajuster le modèle aux données
new_model.fit(X)

# Imprimer les paramètres appris
print("Matrice de transition :")
print(new_model.transmat_)
print("Moyennes :")
print(new_model.means_)
print("Covariances :")
print(new_model.covars_)

# Prédire les états cachés pour les données observées
hidden_states = new_model.predict(X)

print("États cachés :")
print(hidden_states)
```

![Exemple de code complet de HMM (Hidden Markov Chain)](https://cdn-media-0.freecodecamp.org/2024/06/1.png align="center")

Maintenant, décomposons le code bloc par bloc :

**Importer les bibliothèques et définir la graine aléatoire :**

```python
import numpy as np
from hmmlearn import hmm

np.random.seed(42)
```

![Exemple de code de HMM (Hidden Markov Chain) - Importer les bibliothèques et définir la graine aléatoire](https://cdn.hashnode.com/res/hashnode/image/upload/v1763529887680/2440547e-ccf4-4067-83c2-20fafb16f045.png align="center")

Dans ce bloc de code, nous avons importé deux bibliothèques Python :

* [NumPy](https://numpy.org/) : Pour les opérations numériques.

* [hmmlearn](https://hmmlearn.readthedocs.io/en/latest/index.html) : Pour l'implémentation du modèle de Markov caché.

Ensuite, nous avons défini une graine aléatoire avec la bibliothèque NumPy. Une graine aléatoire est une valeur utilisée pour démarrer un générateur de nombres pseudo-aléatoires.

Avec une graine aléatoire fixe, nous pouvons nous assurer que la séquence de nombres pseudo-aléatoires générée est toujours la même. Cela nous permet de dupliquer des expériences et de vérifier les résultats.

La valeur spécifique de la graine n'a pas d'importance tant qu'elle reste cohérente.

**Définir les paramètres du HMM et créer un HMM gaussien :**

```python
n_components = 2  # Nombre d'états
n_features = 1    # Nombre de caractéristiques d'observation

model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag")
```

![Exemple de code de HMM (Hidden Markov Chain) - Définir les paramètres du HMM et créer un HMM gaussien](https://cdn.hashnode.com/res/hashnode/image/upload/v1763529894398/094ac272-2788-4856-a984-b1f687464e90.png align="center")

Dans ce bloc de code, nous avons créé un HMM avec deux états cachés et une seule variable observée.

`covariance_type "diag"` signifie que les matrices qui représentent la covariance (comment deux variables changent ensemble) sont diagonales. En d'autres termes, chaque ligne et colonne est supposée être indépendante des autres.

Cela implique que les distributions de probabilité de chaque ligne et colonne sont indépendantes les unes des autres.

Mais il y a encore quelque chose d'étrange lorsque nous avons défini la chaîne de Markov cachée :

**Que signifie "Gaussien" ?**

C'est un très grand sujet en statistiques, mais en quelques mots, les chaînes de Markov ne peuvent être créées que lorsque nous spécifions les probabilités de transition (chances de passer d'un état à un autre dans une chaîne de Markov) et une distribution de probabilité initiale.

Un HMM gaussien suppose que les événements sont initialement modélisés par une distribution gaussienne, également appelée distribution normale !

Et rappelez-vous, nous avons déjà vu ce qu'est une distribution normale.

La voici à nouveau :

![Exemple de code de HMM (Hidden Markov Chain) - Image de distribution normale](https://cdn.hashnode.com/res/hashnode/image/upload/v1763529107399/e51cb7a3-e751-45c7-8164-c07795ad32e1.png align="center")

À partir d'une distribution normale et d'autres composants, nous pouvons créer une chaîne de Markov cachée. Et les chaînes de Markov cachées servent de fondement à des systèmes qui affectent des millions de vies.

**Définir la matrice de transition, les moyennes et les covariances pour chaque état :**

```python
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])

model.means_ = np.array([[0.0], [3.0]])
model.covars_ = np.array([[0.5], [0.5]])
```

![Exemple de code de HMM (Hidden Markov Chain) - Définir la matrice de transition, les moyennes et les covariances pour chaque état](https://cdn.hashnode.com/res/hashnode/image/upload/v1763529901607/53442504-bcec-46d0-8114-fcd627947576.png align="center")

```python
model.startprob_ = np.array([0.6, 0.4])
```

Cette ligne définit les probabilités initiales des états pour un modèle de Markov caché (HMM). Elle indique qu'il y a 60 % de chances de commencer dans l'état 0 et 40 % de chances de commencer dans l'état 1.

```python
model.transmat_ = np.array([[0.7, 0.3], [0.4, 0.6]])
```

Cette ligne de code définit la matrice de probabilités de transition d'état pour le HMM.

La matrice spécifie les probabilités de passer d'un état à un autre :

* À partir de l'état 0, il y a 70 % de chances de rester dans l'état 0 et 30 % de chances de passer à l'état 1.

* À partir de l'état 1, il y a 40 % de chances de passer à l'état 0 et 60 % de chances de rester dans l'état 1.

```python
model.means_ = np.array([[0.0], [3.0]])
```

Cette ligne définit les valeurs moyennes pour les distributions d'observation dans chaque état.

Elle indique que les observations sont normalement distribuées avec une moyenne de 0,0 dans l'état 0 et une moyenne de 3,0 dans l'état 1.

```python
model.covars_ = np.array([[0.5], [0.5]])
```

Cette ligne définit les valeurs de covariance pour les distributions d'observation dans chaque état.

Elle spécifie que la variance (covariance dans ce cas unidimensionnel) des observations est de 0,5 pour l'état 0 et l'état 1.

**Créer des données, une nouvelle instance de HMM et ajuster le modèle avec les données :**

```python
X, Z = model.sample(100)  # 100 échantillons

new_model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag", n_iter=100)

new_model.fit(X)

print("Matrice de transition :")
print(new_model.transmat_)
print("Moyennes :")
print(new_model.means_)
print("Covariances :")
print(new_model.covars_)
```

![Exemple de code de HMM (Hidden Markov Chain) - Créer des données, une nouvelle instance de HMM et ajuster le modèle avec les données](https://cdn.hashnode.com/res/hashnode/image/upload/v1763529906427/009804bc-40db-4979-99dd-564935b175cc.png align="center")

Dans ce code, nous avons créé un modèle avec 100 échantillons, l'avons itéré 100 fois et avons imprimé la nouvelle matrice de transition d'état, les moyennes et les covariances.

En d'autres termes, nous avons :

1. Généré 100 échantillons à partir du modèle original

2. Ajusté un nouveau HMM à ces échantillons.

3. Imprimé les paramètres appris de ce nouveau modèle.

Que signifient X et Z ici ?

X signifie les échantillons de données observées générés par le modèle original, tandis que Z signifie les séquences d'états cachés correspondant aux échantillons de données observées générés par le modèle original.

La matrice de transition imprime :

```python
[[0.8100804  0.1899196 ]
 [0.49398918 0.50601082]]
```

Ce qui signifie que le modèle tend à rester dans l'état 0 et a presque les mêmes chances de changer ou de rester lorsqu'il est dans l'état 1.

Les moyennes impriment :

```python
[[0.01577373]
 [3.06245496]]
```

Ce qui signifie que la valeur observée moyenne est d'environ 0,016 dans l'état 0 et 3,062 dans l'état 1.

Les covariances impriment :

```python
[[[0.41987084]]
 [[0.53146802]]]
```

Ce qui signifie que les valeurs observées varient d'environ 0,420 dans l'état 0 et 0,531 dans l'état 1.

Ainsi, nous ne connaîtrons peut-être jamais les valeurs exactes des états, mais nous connaissons leur valeur observée moyenne et comment ils varient et tendent à changer les uns avec les autres.

**Prédire les états cachés pour les données observées :**

```python
hidden_states = new_model.predict(X)

print("États cachés :")
print(hidden_states)
```

![Exemple de code de HMM (Hidden Markov Chain) - Prédire les états cachés pour les données observées](https://cdn.hashnode.com/res/hashnode/image/upload/v1763529913530/f81b3dbf-f517-4857-ac92-4732a524a621.png align="center")

Dans ce code, en fonction des échantillons de données observées X, nous avons prédit les nouveaux états du modèle de Markov.

Les états cachés impriment :

```python
[0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 0 0 1 1 0 1 1 0 1 0 0 0 1
 1 1 1 1 0 0 0 1 1 0 0 1 1 1 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0
 0 0 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0]
```

Ce qui signifie que les états cachés passent de l'état 0 à l'état 1, montrant comment le système change d'états au fil du temps.

### **Applications en IA et théorie du contrôle : Prendre des décisions en cas d'incertitude**

![Image de nombreux instruments de vol dans un avion](https://cdn.hashnode.com/res/hashnode/image/upload/v1765002495967/325e5ee4-df14-4adc-a520-0764d89fe8c8.jpeg align="center")

[Photo par capt.sopon](https://www.pexels.com/photo/gray-airplane-control-panel-3402846/)

Je vous ai donné un aperçu de haut niveau du domaine des probabilités et des statistiques. Comme je l'ai expliqué auparavant, je voulais rendre les explications simples à comprendre.

En tant que titulaire d'une licence en ingénierie électrique et informatique, je peux vous assurer que, bien que ce chapitre semble simple, en probabilités et statistiques, les choses peuvent devenir très compliquées très rapidement.

Beaucoup d'autres concepts comme :

* les valeurs p

* les méthodes avancées de Monte Carlo

* les réseaux bayésiens

* les hypothèses statistiques

Ne sont pas aussi simples que les idées que je viens de vous expliquer.

Mais en l'état, les probabilités et les statistiques sont les points de départ pour prendre des décisions où l'incertitude existe en IA et en théorie du contrôle.

Par exemple, le théorème de Bayes, en plus d'être le fondement du filtre de Kalman, est également le fondement de nombreux modèles probabilistes dans le domaine de l'IA. Les modèles probabilistes sont généralement utilisés dans les sociétés quantitatives et les banques pour modéliser le risque.

En théorie du contrôle, les probabilités et les statistiques sont largement utilisées pour concevoir des systèmes de contrôle robustes (comme c'est le cas avec les filtres de Kalman).

Ainsi, comme vous pouvez le voir, l'application des probabilités et des statistiques, comme le calcul et l'algèbre linéaire, est le fondement de nombreux outils qui impactent des millions de vies et déplacent des milliards de dollars dans l'économie mondiale.

## Chapitre 7 : Théorie de l'optimisation - Enseigner aux machines à s'améliorer

![Image en noir et blanc de nombreuses voies ferrées provenant d'une seule](https://cdn.hashnode.com/res/hashnode/image/upload/v1765002637327/9dea740c-4582-42bf-95a6-1230b7e9092d.jpeg align="center")

[Photo par Pixabay](https://www.pexels.com/photo/railroad-tracks-in-city-258510/)

C'est le chapitre de mathématiques le plus avancé du livre. Pour vraiment le comprendre, il est très important que vous ayez d'abord lu les autres chapitres.

Nous allons examiner quelques méthodes d'apprentissage automatique, et je vous montrerai quelques recettes de la manière dont l'apprentissage automatique est simplement l'utilisation de l'algèbre linéaire, du calcul, des probabilités et des statistiques, et de la théorie de l'optimisation.

Tout comme faire un gâteau !

### Qu'est-ce que la théorie de l'optimisation ?

En IA, la théorie de l'optimisation est responsable des algorithmes qui optimisent les modèles d'IA basés sur les données.

Souvent, les grandes entreprises investissent des millions dans la recherche pour créer ou affiner des algorithmes qui rendent l'entraînement des modèles d'IA plus rapide.

Ainsi, les entreprises économisent bien plus d'argent que les coûts de recherche initiaux lorsqu'elles passent à l'échelle pour entraîner plusieurs grands modèles d'IA.

C'est grâce à la théorie de l'optimisation que le deep learning a pu s'adapter efficacement, conduisant finalement à la création de ChatGPT et de nombreux autres grands modèles de langage.

**Mais pourquoi cela ?**

Dans tous les modèles d'apprentissage automatique basés sur les données, il y a une phase d'apprentissage qui doit avoir lieu. C'est-à-dire qu'il y a une période où les algorithmes font des prédictions qui ne sont pas correctes et doivent ensuite changer certains paramètres pour s'assurer que les prochaines prédictions sont correctes — ou au moins plus proches de l'être.

Sans optimisation, les algorithmes d'apprentissage automatique ne progressent pas sur leur chemin d'apprentissage vers la bonne solution. Sans optimisation, ils passent trop de temps sur un chemin d'apprentissage qui n'augmentera pas leur capacité à prédire les choses de la bonne manière.

Alors, commençons à apprendre !

### Pourquoi l'optimisation guide l'apprentissage en IA

![Image d'un robot blanc très mignon](https://cdn.hashnode.com/res/hashnode/image/upload/v1766903297889/4075d065-9b55-42e2-a6f6-8aae02de940f.jpeg align="center")

[Photo par Alex Knight](https://www.pexels.com/photo/high-angle-photo-of-robot-2599244/)

La théorie de l'optimisation est le fondement mathématique qui permet aux algorithmes d'améliorer leurs performances sur de nombreuses itérations.

Lorsque nous combinons un algorithme avec un chemin pour changer ses paramètres afin de répondre à un certain objectif (réalisé avec une méthode d'optimisation), cela s'appelle un algorithme d'apprentissage automatique.

Ce processus d'apprentissage implique toujours de minimiser ou de maximiser un certain objectif. Par exemple, pour de nombreux algorithmes d'apprentissage automatique, l'objectif principal est de minimiser les erreurs. Pour ce faire, sur de nombreuses itérations, les méthodes d'optimisation "disent" aux composants internes d'un algorithme quoi changer après avoir reçu des commentaires sur la qualité de ses performances.

C'est comme quelqu'un qui apprend d'abord à conduire une voiture. Les premières fois, cela peut être compliqué. Mais après un certain temps et un peu de pratique, le conducteur apprend à conduire correctement et à ne plus faire les mêmes erreurs qu'il faisait autrefois dans le passé avec l'aide de l'instructeur.

La même chose s'applique aux méthodes d'optimisation lors de l'optimisation des algorithmes.

#### Types de méthodes de théorie de l'optimisation en ML et Deep Learning
Le domaine de la théorie de l'optimisation est immense ! Comme de nombreux domaines des mathématiques, il est en constante évolution chaque année.

Mais pour les besoins de ce livre, il existe trois catégories principales de méthodes d'optimisation :

1. **Méthodes de premier ordre**

Ce sont les plus utilisées en apprentissage profond et dans tous les modèles de LLM comme Gemini, Grok, et autres.

Elles sont appelées méthodes de premier ordre car elles utilisent toutes la première dérivée des fonctions. La première dérivée d'une fonction mesure combien la sortie d'une fonction change lorsque son entrée change très peu. Les plus largement utilisées en apprentissage profond sont des variantes avancées de la descente de gradient.

Bien qu'il existe de nombreuses variantes, voici quelques exemples populaires :

* Descente de gradient par lots standard

* Descente de gradient stochastique

* Descente de gradient par mini-lots

* RMSprop

* **Adam**

Dans ce chapitre, nous allons examiner en profondeur l'une de ces méthodes appelée **Adam** (ci-dessous).

2. **Méthodes de second ordre**

Elles sont appelées méthodes de second ordre car elles utilisent des informations des dérivées secondes pour de meilleures mises à jour. Il existe de nombreuses méthodes, comme :

* BFGS

* L-BFGS

* Méthode de Newton

Mais celles-ci ne sont pas souvent utilisées en apprentissage automatique et profond. Bien qu'elles optimisent avec moins d'itérations, pour le type de problèmes d'optimisation que les algorithmes en IA créent (problèmes de haute dimension), elles sont très coûteuses en calcul.

Ainsi, elles ne sont pas largement utilisées comme les méthodes d'optimisation de premier ordre.

3. **Méthodes d'ordre zéro et autres méthodes**

Ces méthodes ne nécessitent pas de dérivées pour optimiser les algorithmes. Voici quelques exemples d'algorithmes où les dérivées ne sont pas utilisées :

* Algorithmes génétiques

* Algorithmes de programmation dynamique

* Méthodes d'optimisation par essaim de particules

Le problème avec ces algorithmes est qu'ils sont souvent très lents pour de nombreuses variables.

Mais dans certains contextes d'IA, ils peuvent aider à optimiser l'architecture des modèles d'apprentissage profond pour améliorer les modèles d'IA d'un point de vue architectural (au lieu d'un point de vue paramétrique).

#### Comment la théorie de l'optimisation se connecte-t-elle à l'algèbre linéaire, au calcul et aux probabilités et statistiques ?

Essentiellement :

* Le calcul vous enseigne les dérivées, qui vous aident à comprendre la théorie de l'optimisation.

* L'algèbre linéaire vous enseigne les matrices, qui vous aident à comprendre comment différents états se relient et se transforment.

* Les probabilités et les statistiques vous enseignent des concepts comme la covariance et la corrélation, qui vous aident à comprendre comment les variables sont connectées entre elles.

Ainsi, avec l'algèbre linéaire et les probabilités et statistiques, vous acquérez les connaissances nécessaires pour comprendre les algorithmes. Avec le calcul, vous obtenez la base pour comprendre la théorie de l'optimisation et comment elle modifie certains paramètres des algorithmes fondamentaux pour minimiser/maximiser un certain objectif.

### Techniques d'optimisation simples : Comment les machines apprennent étape par étape

![Image d'un robot Star Wars bleu et blanc](https://cdn.hashnode.com/res/hashnode/image/upload/v1765002727335/a265939c-dea8-4763-8861-7c7a0dbe1081.jpeg align="center")

[Photo par LJ Checo](https://www.pexels.com/photo/star-wars-r2-d2-2085831/)

Maintenant, nous allons voir des exemples d'algorithmes d'apprentissage automatique utilisés pour l'optimisation et les déconstruire afin que vous puissiez comprendre comment ces domaines des mathématiques s'appliquent à eux.

Dans chaque exemple, j'expliquerai leur idée principale avec une analogie ainsi que la manière dont chaque domaine mathématique est utilisé dans chaque algorithme.

#### Régression linéaire

Imaginez que vous résolvez un puzzle. Pour compléter le puzzle, vous devez arranger les pièces dans le bon design/ordre.

La même idée s'applique à la régression linéaire.

Nous avons des matrices (algèbre linéaire) qui représentent les paramètres du modèle de régression linéaire et les données qui y circulent.

Et nous pouvons voir au fil du temps à quel point la ligne s'ajuste aux nombres, ainsi que son erreur (probabilités et statistiques).

Pour trouver la meilleure ligne pour la régression linéaire, nous devons savoir combien les paramètres du modèle doivent changer (calcul) et appliquer effectivement ce changement aux paramètres (théorie de l'optimisation).

Ainsi, le calcul nous indique dans quelle direction changer les paramètres, et la théorie de l'optimisation nous indique combien les changer effectivement.

![GIF animation de la régression linéaire fonctionnant sur de nombreuses itérations](https://cdn.hashnode.com/res/hashnode/image/upload/v1764295886800/0c5efd95-9368-4b68-b945-ff911632ca4c.gif align="center")

Voyons comment coder la régression linéaire ci-dessus :

```python
import numpy as np

np.random.seed(42)
X = np.linspace(0, 10, 50)
y_true = 3 * X + 2
noise = np.random.normal(0, 2, 50)
y = y_true + noise

w = 0.1 
b = 0.5
learning_rate = 0.01
iterations = [0, 1, 2, 3, 4, 5]
saved_states = []

for epoch in range(max(iterations) + 1):
    y_pred = w * X + b
    error = np.mean((y - y_pred) ** 2)
    
    if epoch in iterations:
        saved_states.append({
            'epoch': epoch,
            'w': w,
            'b': b,
            'y_pred': y_pred.copy(),
            'error': error
        })
    
    dw = -2 * np.mean(X * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    
    w = w - learning_rate * dw
    b = b - learning_rate * db
```

![Exemple de code de régression linéaire - exemple de code complet](https://cdn.hashnode.com/res/hashnode/image/upload/v1765335029715/f77be0d9-ea3d-48f1-8cb5-f4806d1295e6.png align="center")

Voyons le code bloc par bloc :

**Importer la bibliothèque :**

```plaintext
import numpy as np
```

![Exemple de code de régression linéaire - Importer la bibliothèque](https://cdn.hashnode.com/res/hashnode/image/upload/v1765335026504/94989760-bb16-4469-947e-eba7bd25b5be.png align="center")

Pour ce problème, nous allons importer l'une des bibliothèques Python les plus utilisées : NumPy (avec laquelle nous avons travaillé plus tôt dans le livre).

**Créer des points de données :**

```python
np.random.seed(42)
X = np.linspace(0, 10, 50)
y_true = 3 * X + 2
noise = np.random.normal(0, 2, 50)
y = y_true + noise
```

![Exemple de code de régression linéaire - Créer des points de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1765335038511/59e01c3d-27bf-4e6c-8500-9178f1ff569f.png align="center")

Dans ce code, nous définissons une ligne de base qui aidera à générer les points de données :

![Exemple de code de régression linéaire - image d'une ligne de base verte qui aidera à générer les points de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1765336338665/caa859d0-92cb-424e-8eb2-292093c24355.png align="center")

```python
X = np.linspace(0, 10, 50)
y_true = 3 * X + 2
```

Après avoir créé cette ligne verte, nous allons ajouter du bruit pour créer les points de données :

![Exemple de code de régression linéaire - image d'une ligne de base verte qui aidera à générer les points de données avec des points bleus ajoutés par le bruit introduit](https://cdn.hashnode.com/res/hashnode/image/upload/v1765336395290/80849617-9489-471d-88f6-fb2aaea5b385.png align="center")

```plaintext
noise = np.random.normal(0, 2, 50)
y = y_true + noise
```

C'est ainsi que nous avons défini les points de données pour le jeu de données de la ligne.

**Initialisation des paramètres de régression linéaire et autres :**

```python
w = 0.1 
b = 0.5
learning_rate = 0.01
iterations = [0, 1, 2, 3, 4, 5]
saved_states = []
```

![Exemple de code de régression linéaire - Initialisation des paramètres de régression linéaire et autres](https://cdn.hashnode.com/res/hashnode/image/upload/v1765335044810/72a775ee-9929-488d-b05e-ab5d32d6b031.png align="center")

Dans ce bloc de code, nous initialisons :

* Les paramètres de régression linéaire : Poids à 0,1 et biais à 0,5

* Un hyperparamètre : Taux d'apprentissage

* Le nombre d'itérations que nous allons utiliser pour améliorer la régression linéaire

* Un tableau appelé saved\_states pour stocker des valeurs afin de créer des graphiques plus tard

Ainsi, nous commençons avec cette ligne rouge :

![Exemple de code de régression linéaire - initialisation des paramètres de régression linéaire et ligne pour ajuster les points de données en commençant avec une pente proche de zéro](https://cdn.hashnode.com/res/hashnode/image/upload/v1765336283612/d7bb34b5-aefc-4565-bed2-d2819bc449df.png align="center")

**Faire apprendre la régression linéaire avec les données :**

```python
for epoch in range(max(iterations) + 1):
    y_pred = w * X + b
    error = np.mean((y - y_pred) ** 2)
    
    if epoch in iterations:
        saved_states.append({
            'epoch': epoch,
            'w': w,
            'b': b,
            'y_pred': y_pred.copy(),
            'error': error
        })
    
    dw = -2 * np.mean(X * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    
    w = w - learning_rate * dw
    b = b - learning_rate * db
```

![Exemple de code de régression linéaire - Faire apprendre la régression linéaire avec les données](https://cdn.hashnode.com/res/hashnode/image/upload/v1765335055978/2395671a-d873-4bd1-bfa0-349cc6c7be65.png align="center")

Cela peut sembler compliqué, mais voyons cela en plus petits blocs :

* Boucle for

```python
for epoch in range(max(iterations) + 1):
```

* Faire une prédiction et voir son erreur

```python
y_pred = w * X + b
error = np.mean((y - y_pred) ** 2)
```

Dans ce bloc de code, nous trouvons les valeurs prédites pour les paramètres actuels et voyons son erreur par rapport aux valeurs réelles.

* Sauvegarder les valeurs de l'itération actuelle pour les statistiques futures

```plaintext
if epoch in iterations:
     saved_states.append({
         'epoch': epoch,
         'w': w,
         'b': b,
         'y_pred': y_pred.copy(),
         'error': error
     })
```

Ici, nous stockons simplement dans le tableau saved\_states les valeurs de l'itération actuelle pour calculer des images plus tard.

* Trouver les gradients

```plaintext
dw = -2 * np.mean(X * (y - y_pred))
db = -2 * np.mean(y - y_pred)
```

Dans ce bloc de code, nous trouvons les valeurs des gradients pour la prédiction actuelle.

En d'autres termes, pour le poids et le biais, nous découvrons combien ils doivent changer afin de mieux approximer les valeurs des paramètres aux points de données.

* Mettre à jour les valeurs des paramètres

```plaintext
w = w - learning_rate * dw
b = b - learning_rate * db
```

Enfin, nous mettons à jour le poids et le biais avec les nouvelles valeurs afin que la ligne approximera mieux les points de données :

![GIF animation de la régression linéaire fonctionnant sur de nombreuses itérations](https://cdn.hashnode.com/res/hashnode/image/upload/v1765335279159/97e4914a-ed8a-4cf7-8155-e7cde0fa7edd.gif align="center")

#### Réseaux de neurones

La même idée de puzzle s'applique aux réseaux de neurones. Les réseaux de neurones sont des modèles algorithmiques inspirés du cerveau qui apprennent des motifs à partir de données. Ils font partie d'un domaine de l'apprentissage automatique appelé apprentissage profond, qui utilise des réseaux de neurones pour apprendre des motifs complexes.

Les réseaux de neurones sont importants car ils alimentent les applications modernes d'IA comme :

* La reconnaissance d'images

* La traduction linguistique

* Les chatbots

Par exemple, ChatGPT signifie Chat Generative Pre-trained Transformer. Un transformateur est une architecture de réseaux de neurones.

Si vous comprenez les réseaux de neurones, vous comprendrez les fondements qui font fonctionner ChatGPT.

* Nous avons des matrices (algèbre linéaire) qui représentent les paramètres du modèle de réseau de neurones et les données qui y circulent.

* Et nous pouvons savoir au fil du temps à quel point le modèle de réseau de neurones converge vers le jeu de données, s'ajuste aux nombres, et voir son erreur (probabilités et statistiques).

* Le calcul nous dira dans quelle direction les paramètres du réseau de neurones doivent changer.

* La théorie de l'optimisation nous dira combien ils doivent changer.

Par exemple, voici un réseau de neurones :

![Exemple d'image d'un réseau de neurones simple](https://cdn.hashnode.com/res/hashnode/image/upload/v1764296443948/e1f46e04-d508-407c-8da6-de8e267a2ba7.png align="center")

Ce modèle a au total 13 paramètres :

* Il a 10 lignes (connexions entre les cercles). Ce sont les poids.

* Il a 2 cercles dans la couche cachée et 1 dans la couche de sortie. Chaque cercle a un biais.

**Grande question :**

Imaginez que vous travaillez dans une banque. Vous êtes responsable de décider qui obtient des cartes de crédit ou non. Pour cela, vous créez le réseau de neurones ci-dessus qui prend 4 entrées :

* Revenu

* Score de crédit

* Ratio d'endettement

* Historique de faillite

Avec ce réseau de neurones bien optimisé, vous pouvez le découvrir !

Très simplement, sans entrer dans des détails comme les fonctions d'activation, le réseau traite les 4 entrées à travers ses poids et ses biais.

Chaque connexion multiplie l'entrée par son poids. Après cela, chaque nœud ajoute son biais.

La sortie finale est un nombre entre 0 et 1 :

* Les nombres proches de 0 signifient "Non approuvé"

* Les nombres proches de 1 signifient "Approuvé"

Par exemple, un revenu élevé, un bon score de crédit et aucun historique de faillite circulent à travers les réseaux de neurones et produisent 0,92. Cela signifie qu'il devrait être approuvé.

Mais un revenu faible avec un historique de faillite peut produire 0,15, ce qui entraîne un refus.

En réalité, les systèmes bancaires et autres ont des réseaux de neurones qui prennent beaucoup plus de paramètres bien choisis et décident cela automatiquement.

C'est précisément ainsi que l'IA peut être utilisée pour l'approbation de crédit.

Mais une question reste : Quelle est la meilleure façon de savoir combien les paramètres doivent changer ?

Dans la prochaine partie, nous allons voir l'algorithme le plus célèbre de la théorie de l'optimisation qui nous aidera à décider cela.

### Qu'est-ce qu'Adam ? La méthode la plus populaire pour que les modèles d'IA trouvent le meilleur chemin d'apprentissage

![Image d'une montagne](https://cdn.hashnode.com/res/hashnode/image/upload/v1766902926221/0b6fbbee-dfda-4a55-bd5d-21215ea33074.jpeg align="center")

[Photo par Lum3n](https://www.pexels.com/photo/green-leafed-trees-during-fog-time-167684/)

Pour optimiser les modèles d'IA basés sur des réseaux de neurones, l'une des méthodes les plus populaires s'appelle Adam, qui signifie Adaptive Moment Estimation.

L'article qui a introduit la méthode est l'un des plus influents du 21e siècle en apprentissage automatique, avec des milliers de citations. Comme toutes les idées en IA non symbolique, Adam est un mélange de différents concepts mathématiques.

Il est composé des idées de deux autres méthodes d'optimisation :

* Descente de gradient avec moment : Accumule la vitesse des gradients précédents pour se déplacer plus rapidement dans des directions cohérentes

* Propagation de la racine carrée moyenne (RMSProp) : Adapte les taux d'apprentissage en fonction des magnitudes récentes des gradients

**Comprenons-les avec une analogie.**

Imaginez que vous descendez une montagne à vélo petit à petit. Vous connaissez déjà la direction grâce au calcul.

Mais comment descendre en toute sécurité sans perdre le contrôle ou aller trop lentement ?

Tout d'abord, vous devez accumuler de la vitesse progressivement en utilisant le moment passé. C'est l'une des principales idées de la descente de gradient avec moment.

Il est également important que vous ajustiez votre vitesse en fonction de l'élévation du terrain. C'est l'idée principale de RMSProp.

Ainsi, vous pouvez accélérer et freiner de manière appropriée.

Lors de l'optimisation d'un modèle avec Adam, c'est le même concept. Avec Adam, nous voulons optimiser un modèle de manière rapide et stable.

La descente de gradient avec moment assure la partie rapide, et RMSProp assure la partie sécurisée.

De nos jours, pour les LLM, qui sont une fois de plus de très grands modèles de réseaux de neurones, une variante d'Adam appelée AdamW est plus souvent utilisée.

Maintenant, construisons un exemple de code utilisant Adam.

#### Exemple de code :

En utilisant Adam, nous allons optimiser ce réseau de neurones basé sur de fausses données.

![Image d'un réseau de neurones](https://cdn.hashnode.com/res/hashnode/image/upload/v1765148552889/28101efb-529f-4828-bb7e-adfbf5202d7f.png align="center")

Il prendra 4 caractéristiques :

* Revenu

* Score de crédit

* Ratio d'endettement

* Historique de faillite

Et il nous dira si nous devons ou non approuver le crédit pour une personne donnée.

De plus, puisque ce livre est une introduction aux mathématiques de l'IA, je ne discuterai pas, dans cet exemple de code, de l'optimisation des hyperparamètres, des techniques de régularisation et d'autres sujets plus avancés et bonnes pratiques.

Je veux montrer pourquoi ce réseau de neurones échoue avec ces données et expliquer l'importance d'utiliser de grandes données.

Voici le code complet (et nous verrons chaque partie plus en détail ci-dessous) :

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, random_split
import pytorch_lightning as pl
import matplotlib.pyplot as plt

torch.manual_seed(42)
x = torch.randn(10000, 4)
y = torch.randint(0, 2, (10000, 1)).float()
dataset = TensorDataset(x, y)

train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)

class CreditApprovalNet(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(4, 2)
        self.relu = nn.ReLU()
        self.output = nn.Linear(2, 1)
        self.sigmoid = nn.Sigmoid()
        self.loss_fn = nn.BCELoss()
        self.train_losses = []
    
    def forward(self, x):
        x = self.relu(self.hidden(x))
        return self.sigmoid(self.output(x))
    
    def training_step(self, batch, batch_idx):
        x, y = batch
        y_pred = self(x)
        loss = self.loss_fn(y_pred, y)
        self.log('train_loss', loss)
        self.train_losses.append(loss.item())
        return loss
    
    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=0.0001)

model = CreditApprovalNet()
trainer = pl.Trainer(max_epochs=100, logger=False, enable_checkpointing=False)
trainer.fit(model, train_loader, val_loader)

# 
plt.plot(model.train_losses)
plt.xlabel('Training Step')
plt.ylabel('Loss')
plt.title('Credit Approval Training')
plt.grid(True, alpha=0.3)
plt.show()
```

![Exemple de code d'entraînement d'un réseau de neurones - Code complet](https://cdn.hashnode.com/res/hashnode/image/upload/v1765150336432/8bb2eab8-60a1-4a01-babf-1b5b11d9187a.png align="center")

Maintenant, décomposons-le :

**Importation des bibliothèques :**

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader, random_split
import pytorch_lightning as pl
import matplotlib.pyplot as plt
```

![Exemple de code d'entraînement d'un réseau de neurones - Importation des bibliothèques](https://cdn.hashnode.com/res/hashnode/image/upload/v1765151014087/80097a4b-6bf2-4af0-94da-7f929cf35d2c.png align="center")

Dans ce bloc de code, nous importons du code de 3 bibliothèques Python :
* [PyTorch](https://pytorch.org/) : L'une des bibliothèques Python les plus populaires pour créer de nouveaux modèles d'IA dans la recherche en intelligence artificielle

* [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/) : Un wrapper PyTorch qui organise le code d'entraînement et gère automatiquement les tâches répétitives

* [Matplotlib](https://matplotlib.org/) : L'une des bibliothèques Python les plus populaires pour créer des graphiques à partir de données

**Création des données :**

```python
torch.manual_seed(42)
x = torch.randn(10000, 4)
y = torch.randint(0, 2, (10000, 1)).float()
dataset = TensorDataset(x, y)
```

![Exemple de code d'entraînement d'un réseau de neurones - création de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1765151040691/a2405e15-8ed0-4988-8b78-724f1bd60347.png align="center")

Dans cette partie, nous définissons une graine pour rendre les nombres aléatoires reproductibles. En d'autres termes, lorsque nous exécutons le code plusieurs fois, les mêmes nombres aléatoires seront générés.

Ensuite, nous allons créer 10 000 demandes de crédit avec 4 caractéristiques dans X et leurs décisions d'approbation dans y. Après cela, nous unifions tout dans la variable dataset.

Nous utiliserons TensorDataset car il nous permet d'avoir les 4 caractéristiques et la cible appariées ensemble. De cette façon, les données ne se mélangent pas pendant l'entraînement.

**Division des données :**

```python
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
```

![Exemple de code d'entraînement d'un réseau de neurones - Division des données](https://cdn.hashnode.com/res/hashnode/image/upload/v1765151063358/8325f2eb-3cf9-4900-909d-545637e20608.png align="center")

Dans ce bloc de code, nous divisons les données en un ensemble d'entraînement et un ensemble de validation.

De cette façon, nous avons un ensemble de données qui est utilisé pour l'entraînement et la recherche des paramètres tout en comparant les résultats avec l'ensemble de validation.

Comme nous pouvons le voir, 80 % des données seront des données d'entraînement, et 20 % des données seront des données de validation.

**Chargement des données :**

```python
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)
```

![Exemple de code d'entraînement d'un réseau de neurones - Chargement des données](https://cdn.hashnode.com/res/hashnode/image/upload/v1765151090966/a80b2483-0bc3-4693-9b58-36765e4b2da2.png align="center")

Ici, nous chargeons les données dans des chargeurs de données pour que le modèle d'IA les utilise.

De cette façon, nous avons les données automatiquement divisées en petits lots et mélangées. Ainsi, au lieu de traiter tous les 10 000 points de données, le modèle sera entraîné sur un lot, amélioré, puis un autre lot, puis amélioré à nouveau, et ainsi de suite. Cela rend l'entraînement plus rapide.

**Création du modèle d'IA et processus d'entraînement :**

```python
class CreditApprovalNet(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(4, 2)
        self.relu = nn.ReLU()
        self.output = nn.Linear(2, 1)
        self.sigmoid = nn.Sigmoid()
        self.loss_fn = nn.BCELoss()
        self.train_losses = []
    
    def forward(self, x):
        x = self.relu(self.hidden(x))
        return self.sigmoid(self.output(x))
    
    def training_step(self, batch, batch_idx):
        x, y = batch
        y_pred = self(x)
        loss = self.loss_fn(y_pred, y)
        self.log('train_loss', loss)
        self.train_losses.append(loss.item())
        return loss
    
    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=0.0001)
```

![Exemple de code d'entraînement d'un réseau de neurones - Création du modèle d'IA et processus d'entraînement](https://cdn.hashnode.com/res/hashnode/image/upload/v1765151116959/d75bd178-24bb-4e5d-b043-c504e280f500.png align="center")

Ce bloc de code semble compliqué, mais examinons chaque méthode bloc par bloc :

* **Création de la classe avec héritage :**

```python
class CreditApprovalNet(pl.LightningModule):
```

De cette façon, en une ligne, nous pouvons importer tout ce dont nous avons besoin pour définir à la fois le modèle et la manière dont il sera entraîné.

* **init : Construit les couches et les composants du modèle :**

```python
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(4, 2)
        self.relu = nn.ReLU()
        self.output = nn.Linear(2, 1)
        self.sigmoid = nn.Sigmoid()
        self.loss_fn = nn.BCELoss()
        self.train_losses = []
```

Dans cette section du code, nous définissons l'architecture du modèle d'IA.

* **forward : Traite les données d'entrée à travers le réseau pour faire des prédictions :**

```python
    def forward(self, x):
        x = self.relu(self.hidden(x))
        return self.sigmoid(self.output(x))
```

Dans cette partie du code, nous définissons comment les données circuleront dans le modèle d'IA en fonction de l'architecture définie.

* **training_step : Calcule la perte pour chaque lot pendant l'entraînement :**

```python
    def training_step(self, batch, batch_idx):
        x, y = batch
        y_pred = self(x)
        loss = self.loss_fn(y_pred, y)
        self.log('train_loss', loss)
        self.train_losses.append(loss.item())
        return loss
```

Ici, nous définissons comment le modèle sera entraîné. En d'autres termes, comment nous allons trouver les meilleurs paramètres pour que le modèle prédise bien.

* **configure_optimizers : Définit l'optimiseur Adam avec un taux d'apprentissage :**

```python
    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=0.0001)
```

Enfin, ici nous définissons quel optimiseur nous allons utiliser pour, étape par étape, améliorer les paramètres du modèle d'IA.

**Entraînement du modèle d'IA :**

```python
model = CreditApprovalNet()
trainer = pl.Trainer(max_epochs=100, logger=False, enable_checkpointing=False)
trainer.fit(model, train_loader, val_loader)
```

![Exemple de code d'entraînement d'un réseau de neurones - Entraînement du modèle d'IA](https://cdn.hashnode.com/res/hashnode/image/upload/v1765151149824/33cb6ad3-3a5d-4964-ab45-ccfd68cd0521.png align="center")

Dans ce bloc de code :

* Nous créons le modèle de réseau de neurones dans la première ligne

* Dans les 2ème et 3ème lignes, nous préparons les paramètres d'entraînement et entraînons le modèle pendant 100 époques

De cette façon, dans la ligne de commande, cela apparaît :

![Exemple de code d'entraînement d'un réseau de neurones - entraînement d'un modèle d'IA - ligne de commande montrant le nombre de couches et de paramètres](https://cdn.hashnode.com/res/hashnode/image/upload/v1765152230535/3a5a6a13-12b1-4f31-8bec-cfbc830510a6.png align="center")

Le code PyTorch nous indique essentiellement le nombre de paramètres dans le modèle d'IA !

**Visualisation des résultats et compréhension de leur médiocrité :**

```python
plt.plot(model.train_losses)
plt.xlabel('Étape d'entraînement')
plt.ylabel('Perte')
plt.title('Entraînement à l'approbation de crédit')
plt.grid(True, alpha=0.3)
plt.show()
```

![Exemple de code de visualisation des résultats et de compréhension de leur médiocrité :](https://cdn.hashnode.com/res/hashnode/image/upload/v1765151210074/3cbecda5-616e-4c3b-a942-2512f81697a1.png align="center")

En utilisant la bibliothèque Matplotlib, nous traçons les résultats :

![Exemple de code d'entraînement d'un réseau de neurones - Tracer l'entraînement effectué au fil du temps.](https://cdn.hashnode.com/res/hashnode/image/upload/v1765152336092/6cfce900-ffb6-449f-9d5d-827ff71735bb.png align="center")

**Le modèle d'IA ne converge pas.**

Nous pouvons le voir car la perte est proche de 0,7 (70 %) au fil du temps.

La principale raison pour laquelle le modèle ne converge pas bien est qu'il y a peu ou pas de relation entre les 4 caractéristiques et la variable cible.

En d'autres termes, nous n'avons pas de bonnes données.

Le code fonctionne parfaitement, mais cela montre la **règle la plus importante en apprentissage automatique** : lorsque nous créons un modèle d'IA, la chose LA PLUS IMPORTANTE est la donnée.

Peu importe si vous utilisez une régression linéaire simple ou un réseau de neurones basé sur des transformateurs ou autre chose. Si vous n'avez pas de données de haute qualité, le modèle ne fonctionnera pas bien.

Même si nous utilisons un bon optimiseur, comme Adam, cela ne résoudra pas le problème des données.

**Prochaines étapes : Erreurs courantes des débutants**

J'ai également écrit cet exemple de code exact pour vous montrer quelque chose de très important : les réseaux de neurones ne sont pas toujours les meilleurs modèles à utiliser.

C'est une erreur très courante chez les débutants. Vous pouvez commencer avec des réseaux de neurones pour tout, alors que souvent des méthodes d'apprentissage automatique avec peu de prétraitement des données font bien le travail.

Pour ce type de problème, la solution est d'essayer d'abord des méthodes d'apprentissage automatique au lieu de passer directement aux réseaux de neurones.

Il y a plusieurs raisons à cela, mais les principales sont :

* Les méthodes d'apprentissage automatique sont plus simples et souvent plus rapides à entraîner que les réseaux de neurones

* Les méthodes d'apprentissage automatique sont plus simples à comprendre pour savoir comment elles prennent des décisions. En d'autres termes, nous pouvons comprendre comment le modèle d'apprentissage automatique a pensé pour faire une prédiction.

* Avec l'apprentissage computationnel, nous pouvons deviner avec certains modèles d'apprentissage automatique à quel point ils prédiront bien à l'avenir et fournir des garanties théoriques sur leurs performances.

Une autre erreur courante est de ne pas diviser les données.

Pour simplifier, j'ai créé seulement une division des données en entraînement et validation

Dans un projet sérieux, vous devriez toujours les diviser en 3 parties : entraînement, validation et test.

Avec l'entraînement, vous créez le modèle. Avec la validation, vous testez le modèle en fonction des données sur lesquelles il a été entraîné. Avec la partie ensemble de test, vous comparez si la perte du modèle est similaire à celle de la validation ou différente. Si elles sont très différentes, cela signifie que le modèle d'IA a convergé vers l'ensemble de validation mais pas vers l'ensemble de test.

Je vous lance le défi de réfléchir davantage à la manière dont vous pourriez améliorer ce code et d'essayer de rendre les données synthétiques plus corrélées afin d'améliorer leur qualité.

### Applications en IA et en théorie du contrôle de la théorie de l'optimisation

![Image d'une main de robot touchant une toile](https://cdn.hashnode.com/res/hashnode/image/upload/v1765002780396/5aaf78bb-a06a-4d09-b681-a604a323d430.jpeg align="center")

[Photo de Tara Winstead](https://www.pexels.com/photo/robot-pointing-on-a-wall-8386440/)

La théorie de l'optimisation sert de moteur aux systèmes d'IA et de contrôle qui façonnent nos vies.

Du déverrouillage de votre téléphone avec la reconnaissance faciale aux systèmes de pilote automatique guidant les avions, les algorithmes d'optimisation sont constamment au travail.

Lorsque vous posez une question à ChatGPT, la théorie de l'optimisation détermine les valeurs de milliards de paramètres pendant l'entraînement.

Il en va de même pour tous les autres LLM comme Gemini, Claude, Grok, DeepSeek, et autres. Ils contiennent tous des millions et des millions de paramètres. La seule façon de trouver la meilleure combinaison de paramètres pour atteindre un certain objectif est avec la théorie de l'optimisation.

En théorie du contrôle, de nombreux systèmes comme le contrôle prédictif par modèle (MPC) et les systèmes de contrôle adaptatifs ne fonctionnent que grâce à des méthodes d'optimisation qui équilibrent le fonctionnement des composants internes du système de contrôle.

Au-delà de l'entraînement des réseaux de neurones et du contrôle des systèmes physiques, l'optimisation alimente les systèmes de recommandation, l'allocation des ressources, et tant d'autres systèmes.

Quelques exemples sont :

* Le système de recommandation de films de Netflix

* Le système de suggestion de chansons de Spotify

* Les systèmes de Google pour réduire les coûts de refroidissement des centres de données

* Les systèmes de trading haute fréquence des sociétés de trading quantitatif

Pour conclure ce dernier chapitre, je partagerai ceci :

**C'est la théorie de l'optimisation qui transforme les modèles mathématiques en modèles d'IA qui impactent la vie de millions de personnes dans le monde.**

## Conclusion : Où les mathématiques et l'IA se rencontrent

![Pyramides d'Égypte avec un chameau assis](https://cdn.hashnode.com/res/hashnode/image/upload/v1765002962447/8cdbc79a-5d9c-406d-bad6-2f2e49566b36.jpeg align="center")

[Photo de AXP Photography](https://www.pexels.com/photo/a-camel-lying-in-the-ground-on-the-background-of-pyramids-18991572/)

Lorsque les anciennes civilisations ont gravé pour la première fois des nombres sur des tablettes d'argile, elles n'imaginaient probablement pas que ces symboles permettraient un jour à l'humanité de créer les merveilles scientifiques, technologiques et médicales que nous avons aujourd'hui.

Pourtant, nous y sommes.

Nous sommes dans une ère où les idées mathématiques développées sur de nombreux siècles - voire des millénaires - ont convergé pour créer l'intelligence artificielle.

Tout au long de ce livre, nous avons tracé un chemin des concepts mathématiques les plus basiques à la pointe de l'IA. Nous avons vu comment :

* Les matrices compressent des systèmes complexes en formes simples

* Les dérivées mesurent le changement

* La probabilité nous aide à naviguer dans l'incertitude

* L'optimisation guide les algorithmes vers de meilleures décisions pour apprendre plus vite.

Nous avons également appris comment chaque domaine des mathématiques a aidé à créer des outils responsables de nombreuses choses que nous tenons pour acquises aujourd'hui.

### Les mathématiques sont le fondement de l'IA

![Tableau avec une équation intégrale](https://cdn.hashnode.com/res/hashnode/image/upload/v1766902825228/e14431de-44da-4e26-a646-5d277c16b073.jpeg align="center")

[Photo de Jeswin Thomas](https://www.pexels.com/photo/person-writing-on-white-board-3781338/)

N'oubliez jamais ceci : l'IA n'est pas de la magie pure ou un "être" que nous ne comprenons pas. Ce n'est que la combinaison de nombreuses idées mathématiques fonctionnant très bien ensemble.

Lorsque vous posez une question à ChatGPT ou à tout autre LLM, il génère une réponse. Et dans le processus de génération de cette réponse, il y a des millions de multiplications de matrices qui se produisent en quelques secondes.

Ou, par exemple, lorsqu'une voiture autonome décide de s'arrêter car elle approche d'un passage pour piétons, il y a beaucoup de calculs mathématiques (liés au calcul, à la probabilité et aux statistiques) qui fonctionnent très rapidement pour assurer la sécurité.

La grande chose à propos des mathématiques est que c'est un langage logique commun et standard. Peu importe les antécédents des personnes ou leur lieu de naissance, une dérivée sera toujours une dérivée, et il en va de même pour les concepts clés de l'IA.

De cette façon, les scientifiques et les ingénieurs du monde entier peuvent améliorer le travail des uns et des autres car tout le monde comprend le même langage.

### L'avenir : L'IA sur appareil et la démocratisation de l'IA

![Image d'une puce](https://cdn.hashnode.com/res/hashnode/image/upload/v1766902760109/02b3f00d-a8df-4546-bf41-c1791cdc5f18.jpeg align="center")

[Photo de Steve Johnson](https://www.pexels.com/photo/abstract-image-of-a-microchip-with-heatmap-colors-28767589/)

Un changement qui se produit actuellement est le passage à l'IA en périphérie. C'est-à-dire, une IA qui fonctionne localement sur votre téléphone, votre ordinateur, et vraiment sur tous vos appareils (plutôt que dans des centres de données distants).

De cette façon, la confidentialité est garantie car elle fonctionne localement. Les temps d'attente pour les modèles d'IA diminuent car aucune donnée n'a besoin d'être envoyée. L'IA peut être utilisée hors ligne, et les coûts diminuent.

Et qu'en est-il des immenses centres de données construits dans le monde entier ? Ceux-ci seront utilisés pour plus de produits qui aideront à améliorer la vie de millions de personnes.

À mesure que l'IA devient plus locale et que plus de puissance de traitement est libérée des grands centres de données, de nouvelles innovations en IA apparaîtront, et plus de bénéfices viendront.

De la même manière que dans le siècle dernier, chaque ordinateur a reçu sa propre puce de mise en réseau, chaque appareil aura (et dans certains cas, a déjà) des accélérateurs d'IA.

Et une grande partie de cela sera grâce aux mathématiques que vous avez apprises dans ce livre.

### Réflexions finales

Isaac Newton a écrit : "Si j'ai vu plus loin, c'est en me tenant sur les épaules de géants."

Chaque algorithme que vous utilisez, chaque modèle que vous entraînez, et chaque nouveau théorème que vous apprenez repose sur des siècles de progrès mathématiques. Vous vous tenez maintenant sur les épaules de ces mêmes géants !

Merci d'avoir lu, et bon apprentissage.

Voici le livre complet [Dépôt GitHub avec tout le code](https://github.com/tiagomonteiro0715/The-Math-Behind-Artificial-Intelligence-A-Guide-to-AI-Foundations).

### Remerciements

Tout d'abord, je tiens à remercier [**Guilherme Mendes**](https://www.linkedin.com/in/guilherme-mendes-a416b7206/), actuellement étudiant en master en génie électrique et informatique à l'Université NOVA, spécialisé en théorie du contrôle, pour avoir révisé les détails mathématiques et techniques de la 1ère version de ce livre.

Je suis également reconnaissant envers les organisations qui m'ont donné des opportunités de grandir :

* [NOVA School of Science and Technology](https://www.fct.unl.pt/en)

* [IEEE Portugal Section](https://ieee-pt.org/)

* [Silicon Valley Fellowship](https://www.siliconvalleyfellowship.com/)

* [Northeastern University](https://www.northeastern.edu/)

* [BEST et BEST Almada](https://best.eu.org/index.jsp)

* [Magma Studio](https://magmastudio.pt/)

Un remerciement spécial va à l'équipe éditoriale de freeCodeCamp, en particulier Abigail Rennemeyer, pour leur patience et pour avoir révisé chaque chapitre de ce livre.

Je tiens également à remercier tous les professeurs de NOVA FCT qui m'ont enseigné et guidé tout au long de mon parcours académique, en particulier ceux du Département de génie électrique et informatique.

## À propos de l'auteur

* LinkedIn : [https://www.linkedin.com/in/tiago-monteiro-](https://www.linkedin.com/in/tiago-monteiro-/)

* GitHub : [https://github.com/tiagomonteiro0715](https://github.com/tiagomonteiro0715)

* Email : monteiro.t@northeastern.edu

Je m'appelle Tiago Monteiro, et je poursuis maintenant un master en intelligence artificielle à l'Université Northeastern dans le campus de Silicon Valley (San Jose) avec une bourse basée sur le mérite.

Je ne viens pas des États-Unis. Je suis un ressortissant portugais, né et élevé dans le district de Lisbonne.

Au Portugal, j'ai complété une licence en génie électrique et informatique à l'Université NOVA, l'une des meilleures universités du Portugal.

J'ai écrit plus de 20 articles pour freeCodeCamp, qui ont accumulé plus de 240 000 vues au fil des ans, et j'ai complété la spécialisation en apprentissage profond de DeepLearningAI, enseignée par Andrew Ng.

De plus, j'ai eu le privilège de participer au batch d'hiver 2025 du prestigieux programme Silicon Valley Fellowship.

#### Pourquoi ai-je choisi le génie électrique et informatique ?

Après avoir terminé l'examen national portugais de mathématiques en 12ème année, j'ai choisi le génie électrique et informatique (ECE) pour me challenger et apprendre de nouvelles mathématiques par moi-même.

Le diplôme ECE combinait :

* Mathématiques avancées

* Programmation (de l'assembleur à Python)

* Physique (mécanique classique, électromagnétisme)

#### Qu'ai-je gagné exactement ?

J'ai maîtrisé les compétences nécessaires pour comprendre rapidement la recherche en IA, en particulier après avoir complété la spécialisation en apprentissage profond d'Andrew Ng.

Au Portugal, j'ai également étudié des domaines STEM avancés, y compris, par exemple :

* **Équations différentielles partielles** pour la modélisation de phénomènes réels