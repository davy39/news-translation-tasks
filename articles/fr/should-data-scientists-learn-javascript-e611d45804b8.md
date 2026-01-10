---
title: Les data scientists devraient-ils apprendre JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T21:19:52.000Z'
originalURL: https://freecodecamp.org/news/should-data-scientists-learn-javascript-e611d45804b8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*UTtvUYQAa6heAbiq
tags:
- name: careers
  slug: careers
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Les data scientists devraient-ils apprendre JavaScript ?
seo_desc: 'By Peter Gleeson

  The pros and cons of using the web’s #1 language for data science

  If you have been following the tech landscape in recent years, you have probably
  noticed at least two things.

  For one, you may have noticed that JavaScript is a very p...'
---

Par Peter Gleeson

#### Les avantages et inconvénients de l'utilisation du langage n°1 du web pour la data science

Si vous avez suivi le paysage technologique ces dernières années, vous avez probablement remarqué au moins deux choses.

Tout d'abord, vous avez peut-être remarqué que [JavaScript est un langage très populaire](https://insights.stackoverflow.com/survey/2017#technology-programming-languages) de nos jours. Il gagne en popularité depuis que [Node.js](https://nodejs.org/en/) a permis aux développeurs JavaScript d'écrire du code côté serveur.

Plus récemment, des frameworks tels que [Electron](https://electronjs.org/), [Cordova](https://cordova.apache.org/) et [React-Native](https://facebook.github.io/react-native/) ont permis aux développeurs JavaScript de créer des applications natives pour une large gamme de plateformes.

Vous avez probablement aussi remarqué qu'il y a beaucoup d'excitation autour du domaine de la data science, en particulier du machine learning. Les avancées récentes en théorie et en technologie ont rendu ce domaine autrefois ésotérique beaucoup plus accessible aux développeurs.

Vous pourriez alors vous demander s'ils forment un duo naturel ? Les data scientists devraient-ils envisager d'apprendre JavaScript ?

La plupart des data scientists travaillent avec une combinaison de Python, R et SQL. Si vous êtes nouveau dans le domaine, **ce sont les langages que vous devriez maîtriser en premier**.

Les data scientists peuvent également se spécialiser dans un autre langage tel que Scala ou Java. Il existe [de nombreuses raisons pour lesquelles ces langages sont si populaires](https://medium.freecodecamp.org/which-languages-should-you-learn-for-data-science-e806ba55a81f).

Mais relativement peu de data scientists se spécialisent en JavaScript.

Cependant, étant donné l'ubiquité de JavaScript et la popularité de la data science, dans quelle mesure les data scientists pourraient-ils bénéficier de l'apprentissage, même des bases, de ce langage ? Et qu'en est-il des développeurs JavaScript qui veulent explorer la data science ?

Commençons par examiner quelques objections importantes, puis passons en revue quelques arguments en faveur.

#### Contre

* **Fonctionnalité** — JavaScript n'a tout simplement pas la gamme de packages de data science et de fonctionnalités intégrées comparé à des langages comme R et Python. Si cela ne vous dérange pas de réinventer la roue, cela pourrait être moins problématique. Mais si vous devez exécuter des analyses plus sophistiquées, vous manquerez rapidement d'options.
* **Productivité** — Un autre avantage des écosystèmes étendus de Python et R est qu'il existe de nombreux guides et tutoriels pour presque toutes les tâches de data science que vous souhaitez accomplir. Pour JavaScript, ce n'est pas vraiment le cas. Vous mettrez probablement plus de temps à comprendre comment résoudre un problème de data science en JavaScript qu'en Python ou R.
* **Multithreading** — Il est souvent utile de traiter de grands ensembles de données ou [d'exécuter des simulations en parallèle](https://medium.freecodecamp.org/solve-the-unsolvable-with-monte-carlo-methods-294de03c80cd). Cependant, Node.js n'est pas adapté aux tâches intensives en calcul, liées au CPU. Pour de telles tâches, des langages comme Python, Java ou Scala ont l'avantage sur JS. Mais, consultez [le projet Napa.js de Microsoft](https://github.com/Microsoft/napajs#napajs). Il fournit un runtime JavaScript multithread qui peut compléter Node.js.
* **Coût d'opportunité** — Peut-être que la principale raison pour laquelle les data scientists n'apprennent pas beaucoup de langages au-delà de Python et R est due au « [coût d'opportunité](https://en.wikipedia.org/wiki/Opportunity_cost) ». Chaque heure passée à apprendre un autre langage est une heure qui aurait pu être investie dans l'apprentissage d'un nouveau framework Python ou d'une autre bibliothèque R. Tant que ces langages dominent le marché de l'emploi en data science, il y a plus d'incitations à les apprendre. Et parce que la data science est un domaine en évolution rapide, il y a toujours quelque chose de nouveau à apprendre.

#### Pour

* **Visualisation** — JavaScript excelle dans la visualisation de données. Des bibliothèques comme [D3.js](https://d3js.org/), [Chart.js](https://www.chartjs.org/), [Plotly.js](https://plot.ly/javascript/) et [beaucoup d'autres](https://www.codewall.co.uk/the-best-javascript-data-visualization-charting-libraries/) rendent la création de visualisations de données puissantes et de tableaux de bord vraiment facile. Consultez [quelques excellents exemples de D3](https://github.com/d3/d3/wiki/Gallery) !
* **Intégration produit** — De plus en plus d'entreprises utilisent des technologies web avec une pile basée sur Node pour construire leur produit ou service principal. Si votre rôle en tant que data scientist vous oblige à travailler en étroite collaboration avec les développeurs de produits, il ne peut pas faire de mal de « parler » le même langage.
* **ETL** — Les pipelines de traitement de données sont généralement implémentés dans un langage généraliste, comme Python, Scala ou Java. JavaScript n'est souvent pas considéré. Cependant, cela pourrait être injuste. Le module de système de fichiers de Node, « fs », fournit une excellente API qui vous permet d'appeler des opérations de système de fichiers standard soit de manière synchrone, soit asynchrone. Node s'intègre également bien avec [MongoDB](https://www.mongodb.com/) et de nombreux autres systèmes de bases de données populaires. L'[API Streams facilite grandement le travail avec des flux de grandes données](https://medium.freecodecamp.org/node-js-streams-everything-you-need-to-know-c9141306be93) — un autre avantage potentiel pour l'ETL. Comme mentionné ci-dessus, pour le multithreading et le traitement parallèle, consultez [le projet Napa.js de Microsoft](https://github.com/Microsoft/napajs#napajs).
* **Tensorflow.js** — Qui a dit que JS ne pouvait pas faire de choses cool en machine learning ? Début 2018, [Tensorflow.js a été publié](https://medium.com/tensorflow/introducing-tensorflow-js-machine-learning-in-javascript-bf3eab376db). Cela apporte le machine learning aux développeurs JavaScript — à la fois dans le navigateur et côté serveur. [Tensorflow](https://www.tensorflow.org/) est une bibliothèque populaire de machine learning, développée par Google et rendue open source en 2015. Reconnaissance de gestes, reconnaissance d'objets, composition musicale... vous l'appelez, vous pouvez probablement l'avoir. La meilleure chose que vous puissiez faire maintenant est [de jeter un coup d'œil à quelques démos](https://github.com/tensorflow/tfjs/blob/master/GALLERY.md).

### Conclusion

Alors, les data scientists devraient-ils apprendre JavaScript ?

Apprendre JavaScript ne nuira pas à votre CV. **Mais ne l'apprenez pas en remplacement d'autres langages.**

En tant que premier langage, le meilleur conseil est d'apprendre soit Python, soit R. Vous devriez également devenir à l'aise avec l'utilisation d'un langage de base de données, comme SQL ou MongoDB.

Cependant, une fois que vous êtes familiarisé avec les bases, vous pourriez vouloir vous spécialiser davantage. Peut-être souhaitez-vous apprendre [Apache Spark](https://spark.apache.org/) pour travailler avec des ensembles de données géants et distribués. Ou peut-être préféreriez-vous apprendre un autre langage comme Scala, MATLAB ou Julia.

Pourquoi ne pas envisager JavaScript ? Il se révèlera précieux si vous souhaitez vous spécialiser dans la visualisation de données, ou si votre rôle vous oblige à travailler en étroite collaboration avec un produit construit en utilisant JavaScript ou une technologie connexe.

Les capacités de machine learning de JavaScript progressent rapidement. Pour certains cas d'utilisation, il est peut-être déjà une alternative solide aux langages habituels de la data science.

En fin de compte, la décision est à la fois pratique et personnelle. Cela dépend des aspects de la data science que vous trouvez les plus intéressants et des opportunités de carrière qui vous excitent le plus.

Mais avec [les tendances actuelles](https://magenta.tensorflow.org/demos/), une chose est sûre. Au cours des années à venir, JavaScript ouvrira plus de portes qu'il n'en fermera.