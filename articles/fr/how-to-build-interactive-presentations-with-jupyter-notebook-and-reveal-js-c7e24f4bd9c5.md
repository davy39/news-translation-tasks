---
title: Comment abandonner PowerPoint et créer de meilleures diapositives avec Jupyter
  et Reveal.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-10T00:33:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-interactive-presentations-with-jupyter-notebook-and-reveal-js-c7e24f4bd9c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MvyDoOEprAO-lbSuInyA0w.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment abandonner PowerPoint et créer de meilleures diapositives avec
  Jupyter et Reveal.js
seo_desc: 'By Dat Tran

  In this article, I will introduce jupyter2slides — a little side project of mine
  that lets you easily create beautiful and interactive presentation slides using
  Jupyter Notebook and reveal.js.

  Here’s what it looks like:


  _[http://interact...'
---

Par Dat Tran

Dans cet article, je vais vous présenter [jupyter2slides](https://github.com/datitran/jupyter2slides) — un petit projet parallèle qui vous permet de créer facilement des diapositives de présentation belles et interactives en utilisant [Jupyter](http://jupyter.org/) Notebook et [reveal.js](http://lab.hakim.se/reveal-js/#/).

Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Hmu8ZyI3NJJWvVEWZlWAg.gif)
_[http://interactive-slides.cfapps.io/](http://interactive-slides.cfapps.io/#/" rel="noopener" target="_blank" title=")_

Et voici le PDF correspondant, généré avec [DeckTape](https://github.com/astefanutti/decktape) :

### Ma motivation pour construire cela

Microsoft PowerPoint est génial. C'est comme un couteau suisse pour les consultants, et vous pouvez créer de belles diapositives avec.

En revanche, quand il s'agit de code, PowerPoint est nul. La solution est d'utiliser reveal.js. Vous pouvez utiliser le markdown pour mettre en évidence le code, et c'est réactif. Mais comme [LaTeX](https://www.latex-project.org/), cela peut être fastidieux.

Une autre façon d'utiliser reveal.js est via Jupyter, qui offre de nombreux avantages :

* Édition dans le navigateur pour le code avec coloration syntaxique automatique, indentation et complétion par tabulation
* Possibilité d'exécuter du code avec les résultats des calculs attachés au code qui les a générés (programmation lettrée)
* Prise en charge du [Markdown](https://en.wikipedia.org/wiki/Markdown) et de nombreux formats multimédias tels que HTML, LaTex, audio et images
* Prise en charge des widgets interactifs pour manipuler et visualiser les données
* Utilisation d'outils de la [PyData stack](https://www.numfocus.org/) comme Matplotlib, Numpy et Bokeh ainsi que d'autres comme [Plotly](https://plot.ly/) et [Folium](https://folium.readthedocs.io/en/latest/)

Pour utiliser reveal.js avec Jupyter, vous créez un notebook et utilisez [nbconvert](http://nbconvert.readthedocs.io/en/stable/) pour obtenir des diapositives reveal.js. Mais le design standard est ennuyeux :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kq3-BczjCXej2BMu-u4Qyw.png)
_Consultez [IPython Slides Viewer](http://slideviewer.herokuapp.com/" rel="noopener" target="_blank" title=") pour d'autres exemples "par défaut"._

### Ma solution

J'ai travaillé sur un projet qui vous permet de générer de belles diapositives de présentation. L'ensemble du code est sur [mon dépôt GitHub](https://github.com/datitran/jupyter2slides). Sous le capot, il utilise toujours `nbconvert` avec reveal.js, mais je l'ai étendu en :

* Ajoutant un thème personnalisé avec un design plus épuré
* Activant le [plugin title footer](https://github.com/e-gor/Reveal.js-Title-Footer) par défaut
* Activant les numéros de diapositives par défaut
* Ajoutant un modèle de notebook Jupyter avec des exemples comme des diapositives de couverture et de diviseur, la syntaxe markdown, et plus encore
* Rendant plus facile le déploiement de la présentation sur [Cloud Foundry](https://www.cloudfoundry.org/) en utilisant [Flask](http://flask.pocoo.org/) et le buildpack Python
* Incluant l'option d'exporter les diapositives en PDF en utilisant [DeckTape](https://github.com/astefanutti/decktape)

### Comment commencer

Pour créer votre propre présentation, clonez le [dépôt sur GitHub](https://github.com/datitran/jupyter2slides) et suivez son readme.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WEgwvN_yuy0-gsgAAmIKIw.gif)
_Clonez le [dépôt](https://github.com/datitran/jupyter2slides" rel="noopener" target="_blank" title=") pour commencer._

J'espère que ce projet vous sera utile à l'avenir. J'ai hâte de voir d'autres personnes utiliser ce modèle lors de conférences comme [PyData](https://pydata.org/). Je suis ouvert à tout retour pour améliorer les designs des diapositives et aux contributions des autres au code.

Si vous avez trouvé cet article utile, donnez-moi un high five 🖐️ pour que d'autres puissent le trouver aussi, et partagez-le avec vos amis. Suivez-moi ici sur Medium (Da[t Tran)](https://medium.com/@datitran) ou sur Twitter (@d[atitran)](https://twitter.com/datitran) pour rester à jour avec mon travail. Merci d'avoir lu !