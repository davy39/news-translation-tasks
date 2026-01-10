---
title: 'Naviguer dans les eaux des graphiques (pt. 2) : une comparaison des bibliothèques
  de graphiques JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T17:35:00.000Z'
originalURL: https://freecodecamp.org/news/charting-the-waters-pt-2-a-comparison-of-javascript-charting-libraries-96e9fb79b856
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sOgqVGUuzDv1O8HtWw8wFA.png
tags:
- name: D3.js
  slug: d3js
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Naviguer dans les eaux des graphiques (pt. 2) : une comparaison des bibliothèques
  de graphiques JavaScript'
seo_desc: 'By Mandi Cai

  A deep dive into D3.js, Dygraphs, Chart.js, and Google Charts


  The code for the charts I created in the header image is up on GitHub.

  When I began creating charts and visualizing data, the only things I knew were “Consider
  Canvas for lar...'
---

Par Mandi Cai

#### Une plongée profonde dans D3.js, Dygraphs, Chart.js et Google Charts

![Image](https://cdn-media-1.freecodecamp.org/images/1*sOgqVGUuzDv1O8HtWw8wFA.png)

Le code des graphiques que j'ai créés dans l'image d'en-tête est disponible sur [GitHub](https://github.com/mandicai/boscc-charts).

Quand j'ai commencé à créer des graphiques et à visualiser des données, les seules choses que je savais étaient « Considérez [Canvas](https://canvasjs.com/) pour les grands ensembles de données » et « [D3](https://d3js.org/) est magique ». Je n'avais aucune idée qu'il existait tout un écosystème de bibliothèques de graphiques. Ces bibliothèques sont gratuites, disponibles et complètes avec des exemples et de la documentation.

Plus important encore, chaque bibliothèque a ses propres avantages et inconvénients en ce qui concerne la variété des graphiques, la courbe d'apprentissage, le niveau de personnalisation et l'interactivité prête à l'emploi. Alors, comment décider ?

Je vais comparer quelques bibliothèques de graphiques JavaScript populaires dans cet article, spécifiquement [**D3.js**](https://d3js.org/)**, [Dygraphs](http://dygraphs.com/)**, [Chart.js](https://www.chartjs.org/) et [**Google Charts**](https://developers.google.com/chart/). Attendez-vous à apprendre comment créer un graphique JavaScript, une comparaison de haut niveau entre les bibliothèques sur les facteurs susmentionnés (variété des graphiques, personnalisation, etc.), et le cas d'utilisation que je perçois comme le mieux adapté à chaque bibliothèque.

Mais d'abord, une brève introduction sur la raison pour laquelle la visualisation des données devient de plus en plus importante. Vous pouvez passer directement à la comparaison côte à côte (`Ctrl+F` « Comparons ! »).

![Image](https://cdn-media-1.freecodecamp.org/images/0*nb6xvXcMDMDhEM0Z)

![Image](https://cdn-media-1.freecodecamp.org/images/0*ZhBuvIhsgEOET25q)

![Image](https://cdn-media-1.freecodecamp.org/images/0*_pP_224BUyY5ZhEY)
_Source : [Wait But Why](https://www.nytimes.com/interactive/2018/08/04/upshot/up-birth-age-gap.html" rel="noopener" target="_blank" title="">The Upshot</a>, <a href="http://rhythm-of-food.net/" rel="noopener" target="_blank" title="">The Rhythm of Food</a>, et <a href="https://waitbutwhy.com/2016/01/horizontal-history.html" rel="noopener" target="_blank" title=")_

### **Pourquoi tracer et visualiser des données ?**

J'ai toujours considéré les visualisations de données comme un meilleur moyen d'**apprendre** et d'**impliquer** un public. Tout le monde n'est pas naturellement doué pour absorber des informations par le texte. Mes yeux se troublent en essayant d'extraire des chiffres d'un bloc de mots. Le texte suppose également que vous êtes familier avec la langue dans laquelle il est écrit. J'ai eu du mal avec les lectures de manuels à l'université. Il est plausible que les non-anglophones aient également eu du mal.

En revanche, chaque fois que je tombais sur un diagramme magnifique et clarificateur au milieu de piles d'informations, je saisissais immédiatement les concepts et je m'en souvenais mieux aussi.

Nos esprits ne sont pas câblés pour comprendre rapidement et en profondeur de gros blocs de texte ou des piles de lignes Excel. Mais ce en quoi ils excellent, c'est la reconnaissance de la similitude, de la symétrie, des connexions entre les objets et de la continuité, qui sont les fondements de la visualisation de données. Pensez aux principes de la Gestalt.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6mBvVtXeImAn7u9KM3MMQg.jpeg)
_Principes de la Gestalt (Source : [FusionCharts](https://www.fusioncharts.com/blog/how-to-use-the-gestalt-principles-for-visual-storytelling-podv/" rel="noopener" target="_blank" title="))_

Voici un extrait de certaines données du [Bureau of Labor Statistics](https://www.bls.gov/lau/#tables) sur les taux de chômage dans les comtés des États-Unis (représentés par un code FIPS) en 2016.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U_fs8Blf5QypSWvE6Phq3Q.png)
_Source : [Bureau of Labor Statistics](https://www.bls.gov/lau/#tables" rel="noopener" target="_blank" title=")_

Pour repérer des tendances ou détecter des anomalies, une personne moyenne passerait un temps considérable à fixer ces données. Elle pourrait scanner chaque ligne et réécrire des chiffres sur une autre feuille de papier. Pas idéal.

Mais si nous visualisons les données sous forme de carte géographique, comme Mike Bostock l'a fait dans son [carnet Observable](https://beta.observablehq.com/@mbostock/d3-choropleth) :

![Image](https://cdn-media-1.freecodecamp.org/images/0*u9tFdrMr4u-gLJqU)
_Source : [D3 Choropleth](https://beta.observablehq.com/@mbostock/d3-choropleth" rel="noopener" target="_blank" title=")_

Vous pouvez immédiatement voir les points chauds de chômage élevé. Au lieu d'heures, vous avez maintenant détecté des modèles intéressants en **quelques secondes.** Cette différence de temps de compréhension peut faire la différence entre abandonner un ensemble de données apparemment « incompréhensible » ou, au contraire, _poursuivre votre enquête_. La création de visualisations précises et accessibles permet également aux spectateurs de repérer des incohérences ou des lacunes dans l'ensemble de données, ce qui **rend les données plus responsables**.

### **L'anatomie d'un graphique**

Avant de passer à la comparaison des bibliothèques, je pense que l'« anatomie » de base d'un graphique JavaScript mérite un aperçu. En travaillant avec ces bibliothèques, j'ai remarqué que toutes, sauf D3*, adoptaient le même modèle pour générer des graphiques.

1. Importez la bibliothèque de graphiques dans le HTML.
2. Créez une `<div>` avec un identifiant ID, tel que « my-first-chart ».
3. Récupérez et chargez les données dans le JS. Vous pouvez également définir les données directement dans le JS. Assurez-vous d'avoir lié ce fichier JS dans le HTML.
4. Passez les données, le conteneur `<div>` et un objet d'options à une fonction de génération de graphique.
5. Certaines bibliothèques, comme Google Charts, nécessitent d'appeler `draw()` pour dessiner le graphique généré.
6. Servez le code sur un serveur Python avec `http-server -c-1 -p 8000` et voyez votre premier graphique sur `localhost:8000`.

**Exemples**

* [Exemple basique Dygraphs](http://dygraphs.com/tutorial.html)
* [Exemple basique D3.js](http://bl.ocks.org/d3noob/b3ff6ae1c120eea654b5)
* [Exemple basique Chart.js](https://www.chartjs.org/docs/latest/)
* [Exemple basique Google Charts](https://developers.google.com/chart/interactive/docs/quick_start)

*D3 a été principalement utilisé pour les graphiques, mais c'est plus une collection de boîtes à outils qu'une bibliothèque de graphiques standard. Voir [cet article](https://medium.com/@mbostock/why-you-should-use-d3-ae63c276e958) pour une meilleure explication.

### **Comparons !**

Lors du choix d'une bibliothèque, j'aime commencer par ces questions d'évaluation :

* Quelle est la courbe d'apprentissage ? (qualité de la documentation, complexité du code)
* Dans quelle mesure puis-je personnaliser mes graphiques ?
* La bibliothèque est-elle activement soutenue ?
* Quels types de données cette bibliothèque accepte-t-elle ?
* Quels modes d'interactivité sont proposés ?
* La bibliothèque propose-t-elle des graphiques réactifs (responsive) ?

### **Courbe d'apprentissage**

![Image](https://cdn-media-1.freecodecamp.org/images/1*dgKyUbyk0tJAnZuMvflftw.png)

Dygraphs, Chart.js et Google Charts ont des courbes d'apprentissage relativement faibles. Ils sont parfaits si vous devez créer des graphiques en quelques heures.

D3 a la courbe d'apprentissage la plus élevée, et la raison en est le contrôle de bas niveau et précis qu'il offre. C'est plutôt une bibliothèque bien écrite de fonctions d'aide avancées. D3 peut théoriquement être utilisé en conjonction avec d'autres bibliothèques de graphiques.

Pour explorer un peu plus loin, j'ai créé le même graphique avec les 4 bibliothèques en utilisant les données météo de Boston de [meteoblue](https://www.meteoblue.com/en/weather/forecast/week/boston_united-states-of-america_4930956). Le code est sur [GitHub](https://github.com/mandicai/boscc-charts).

![Image](https://cdn-media-1.freecodecamp.org/images/1*LEm2V03A5QWMO5e47ahWtw.png)
_Rangée du haut : D3, Dygraphs, Rangée du bas : Chart.js, Google Charts_

… et j'ai enregistré les lignes de code nécessaires pour créer chaque graphique :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OUK3WpJ8DQW8Hh4vh8XGqQ.png)

Les lignes de code confirment la comparaison initiale des courbes d'apprentissage. D3 nécessite nettement plus de lignes pour mettre en place un graphique de base, mais offre plus de possibilités de personnalisation.

### **Personnalisation**

![Image](https://cdn-media-1.freecodecamp.org/images/1*lwbxOc-JhaKcvIrbUJuigQ.png)

D3 brille dans le domaine de la personnalisation. La granularité et la modularité de D3 sont précisément la raison pour laquelle les designers et les développeurs le privilégient comme support pour des visualisations époustouflantes et uniques. [Chart.js](https://www.chartjs.org/docs/latest/configuration/) et [Google Charts](https://developers.google.com/chart/interactive/docs/customizing_charts) offrent de nombreuses options qui peuvent être passées à une fonction génératrice, telles que la taille de la police de la légende et l'épaisseur d'une ligne.

### **Développement actif**

![Image](https://cdn-media-1.freecodecamp.org/images/1*iFA6LDP2UzQokxhM9d_Jog.png)

Je définis le développement d'une bibliothèque comme la fréquence des versions et la réactivité des mainteneurs de la bibliothèque aux problèmes signalés et aux suggestions d'amélioration. Une communauté d'utilisateurs large et solidaire est également un plus. L'utilisation encourage le changement sain et la responsabilité à mesure que l'écosystème JavaScript évolue.

En regardant les dépôts GitHub respectifs, j'ai découvert que les versions et les problèmes résolus pour Dygraphs et Google Charts étaient plus sporadiques que pour D3 et Chart.js. D3 ne s'arrêtera pas de sitôt. Son créateur et ses contributeurs ont récemment publié une version majeure (v5.0) en 2018. Ils contribuent toujours activement à la communauté de la visualisation. La dernière version de Chart.js a également eu lieu assez récemment en 2018. La version a abordé des problèmes et des améliorations. Ils sont documentés en détail dans les notes de version.

### **Types de données**

![Image](https://cdn-media-1.freecodecamp.org/images/1*4eaY8zfk3cQmnCagiTWSXw.png)

Cela parle de soi-même. Fait amusant : j'ai utilisé la [bibliothèque fetch](https://github.com/d3/d3-fetch) de D3 pour récupérer les données. J'ai utilisé d'autres bibliothèques pour les tracer. D3 dispose de fonctions fetch pour presque tous les formats de données courants utilisés dans la visualisation de données.

### **Interactivité**

![Image](https://cdn-media-1.freecodecamp.org/images/1*L8m_dlLsbGHUrEytWwKakA.png)

Dygraphs, Chart.js et Google Charts ont tous des fonctionnalités d'interactivité prêtes à l'emploi, comme les info-bulles, le zoom et les événements. Il est difficile d'introduire des interactions hautement personnalisées car chaque bibliothèque est très encapsulée. Avec D3, vous acceptez que des interactions complexes et uniques soient possibles. Le compromis est que les interactions simples, comme une info-bulle, doivent également être construites de toutes pièces.

### **Réactivité (Responsiveness)**

![Image](https://cdn-media-1.freecodecamp.org/images/1*RT1nSrhty8S5VSOrMpPF4A.png)

Chart.js et D3 proposent des graphiques réactifs dès la sortie de la boîte (pour D3, spécifiez une `viewBox` au lieu de `width` et `height` pour le conteneur `svg`). Dygraphs et Google Charts nécessitent un travail supplémentaire pour créer des graphiques réactifs, comme l'ajout de `position: relative` au conteneur du graphique ou le redessin du graphique lors de `$(window).resize()`.

[Graphique réactif Dygraphs](http://dygraphs.com/tests/resize.html) (inspectez les conteneurs de graphiques pour voir les classes CSS)

[Fil de discussion Stack Overflow sur les graphiques Google réactifs](https://stackoverflow.com/questions/8950761/google-chart-redraw-scale-on-window-resize)

### **Idéal pour ?**

Enfin et surtout, j'ai listé le cas d'utilisation pour lequel je pense que chaque bibliothèque est la mieux adaptée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*l0EZD0RSsxBzOw9stODUVA.png)
_Toutes les captures d'écran proviennent de la section des exemples respectifs de chaque bibliothèque_

D3 vaut la peine d'y investir du temps si vous **a) avez besoin d'une visualisation hautement personnalisée** et/ou **b) voulez des fonctions d'aide à utiliser en conjonction avec d'autres bibliothèques.**

J'ai apprécié Dygraphs pour les séries temporelles car l'utilisateur peut parcourir la série et **voir la date et le point correspondant par défaut**. Vous pouvez également [mettre en évidence des périodes spécifiques](http://dygraphs.com/gallery/#g/highlighted-weekends) et [sélectionner des plages de temps](http://dygraphs.com/gallery/#g/range-selector).

Chart.js vous permet de créer des graphiques **simples et esthétiques** qui s'intègrent parfaitement à la page lors du chargement.

Enfin, Google Charts offrait la **plus grande variété de graphiques prêts à l'emploi**, par rapport aux autres bibliothèques. En plus des graphiques standard, Google Charts prend également en charge les [cartes géographiques](https://developers.google.com/chart/interactive/docs/gallery/geochart), les [treemaps](https://developers.google.com/chart/interactive/docs/gallery/treemap), les [diagrammes de Sankey](https://developers.google.com/chart/interactive/docs/gallery/sankey), etc.

### **3, 2, 1 … récapitulatif !**

Nous avons couvert les nombreuses raisons pour lesquelles **la visualisation de données est puissante**, la **structure et les étapes de base** pour créer un graphique à l'aide d'une bibliothèque de graphiques, et une **comparaison point par point** de 4 bibliothèques JavaScript populaires.

L'étape la plus importante après avoir sélectionné une bibliothèque et généré quelques visualisations est de **communiquer**, puis d'**itérer**. Montrez vos graphiques aux autres et demandez-leur ce qu'ils peuvent et ne peuvent pas interpréter. Écoutez leurs commentaires et continuez à peaufiner vos graphiques. Ce sont des outils pédagogiques, et les outils pédagogiques doivent constamment évoluer avec le contenu et les spectateurs.

Merci de votre lecture !

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

Le code des graphiques que j'ai créés est disponible sur [GitHub](https://github.com/mandicai/boscc-charts).

Voici les [diapositives de présentation](https://www.slideshare.net/MandiCai/visualizing-your-data-in-javascript) qui ont mené à cet article.

Si vous voulez en savoir plus sur Bokeh et D3, consultez [Naviguer dans les eaux : entre Bokeh et D3](https://medium.freecodecamp.org/charting-the-waters-between-bokeh-and-d3-73b3ee517478).

Si vous avez des suggestions ou des commentaires, laissez un commentaire.