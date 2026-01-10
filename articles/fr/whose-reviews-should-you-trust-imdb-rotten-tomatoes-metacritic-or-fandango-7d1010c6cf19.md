---
title: À quelles notes devez-vous faire confiance ? IMDB, Rotten Tomatoes, Metacritic
  ou Fandango ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-10T20:33:35.000Z'
originalURL: https://freecodecamp.org/news/whose-reviews-should-you-trust-imdb-rotten-tomatoes-metacritic-or-fandango-7d1010c6cf19
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xHF26U0WHM9YuBWo9V7AAQ.jpeg
tags:
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: film
  slug: film
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: À quelles notes devez-vous faire confiance ? IMDB, Rotten Tomatoes, Metacritic
  ou Fandango ?
seo_desc: 'By Alex Olteanu

  A data scientist investigates


  Should you watch a movie? Well, there are a lot of factors to consider, such as
  the director, the actors, and the movie’s budget. Most of us base our decision off
  of a review, a short trailer, or just by...'
---

Par Alex Olteanu

#### Un scientifique des données enquête

![Image](https://cdn-media-1.freecodecamp.org/images/5FXQgGL4Cm-GsuaU0ZxtTG5eTaXl126UeQho)

Devez-vous regarder un film ? Eh bien, il y a beaucoup de facteurs à considérer, comme le réalisateur, les acteurs et le budget du film. La plupart d'entre nous basent notre décision sur une critique, une courte bande-annonce ou simplement en vérifiant la note du film.

Il y a quelques bonnes raisons pour lesquelles vous pourriez vouloir éviter de lire des critiques ou de regarder une bande-annonce, bien qu'elles apportent beaucoup plus d'informations qu'une simple note.

Premièrement, vous pourriez vouloir éviter complètement les spoilers, peu importe leur taille. Je comprends cela !

Deuxièmement, il se pourrait que vous souhaitiez une expérience non influencée du visionnage de ce film. Cela s'applique généralement uniquement aux critiques, qui sont parsemées de cadres, comme « ce film parle de la complexité de l'univers » ou « ce film ne parle pas vraiment d'amour ». Une fois ces cadres encodés dans votre mémoire à court terme, il est vraiment difficile de les empêcher d'interférer avec votre propre expérience du film.

Une autre bonne raison est que si vous êtes fatigué ou pressé, vous ne voudrez peut-être pas lire une critique, encore moins regarder une bande-annonce de 2 minutes.

Ainsi, une note numérique de film semble être une bonne solution dans plusieurs situations, pour beaucoup de gens.

Cet article vise à recommander **un seul site web** pour obtenir rapidement une note de film précise, et offre une argumentation robuste et basée sur les données pour cela.

### Critères pour « le meilleur »

Faire une telle recommandation revient beaucoup à dire « c'est le meilleur endroit pour chercher une note de film », ce qui est une déclaration évaluative, reposant sur certains critères utilisés pour déterminer ce qui est mieux, ce qui est pire ou le pire, et ce qui est le meilleur, dans ce cas. Pour ma recommandation, j'utiliserai un seul critère : une distribution normale.

Le meilleur endroit pour chercher une note de film est de voir dont les notes sont distribuées selon un **modèle** qui ressemble le plus, ou est identique, au modèle d'une distribution normale, qui est la suivante : étant donné un ensemble de valeurs situées dans un certain intervalle, la plupart d'entre elles se trouvent au milieu de celui-ci, et les quelques autres aux extrémités de cet intervalle. Généralement, voici à quoi ressemble une distribution normale (aussi appelée distribution gaussienne) :

![Image](https://cdn-media-1.freecodecamp.org/images/xpZ08ZSfL7xiXjVVhCoRQ38uj9phIG1qgQMy)
_Une distribution normale (ou gaussienne) des notes de films signifie qu'il y a quelques notes basses, beaucoup de notes moyennes et quelques notes élevées. Une distribution normale idéale signifie le meilleur dans ce contexte._

Quel est le raisonnement derrière ce critère ? Eh bien, d'après ma propre expérience composée de plusieurs centaines de films, je peux dire que j'ai vu :

* quelques films exceptionnels que j'ai regardés plusieurs fois
* quelques films vraiment affreux, qui m'ont fait regretter le temps passé à les regarder
* et une multitude de films moyens, dont je ne me souviens même plus de l'intrigue pour la plupart.

Je crois que **la plupart** des gens — qu'ils soient critiques, cinéphiles ou simplement des spectateurs occasionnels — ont eu une expérience similaire.

Si les notes de films expriment effectivement la qualité des films, alors nous devrions voir le même modèle pour les deux.

Étant donné que la plupart d'entre nous évaluent la majorité des films comme étant de qualité moyenne, nous devrions voir le même modèle lorsque nous analysons les notes de films. Une logique similaire s'applique pour les mauvais et les bons films.

![Image](https://cdn-media-1.freecodecamp.org/images/QQND2-WyhoTpVRq2L6yWMN8-zZV0zD4SQqiM)
_Chaque barre est censée correspondre ici à une note (elle peut aussi correspondre à un intervalle de notes). Plus la barre est haute, plus le nombre de films avec cette note est grand._

Si vous n'êtes pas encore convaincu qu'il devrait y avoir une telle correspondance entre les modèles, pensez à la distribution des notes pour un seul film. Comme beaucoup de gens notent le film, ce n'est pas un acte de foi de supposer que le plus souvent, il y en aura beaucoup avec des préférences similaires. Ils seront généralement d'accord pour dire que le film est soit mauvais, moyen ou bon (je quantifierai plus tard ces valeurs qualitatives). De plus, il y en aura quelques autres qui évalueront le film avec l'une des deux autres valeurs qualitatives.

Si nous visualisions la distribution de toutes les notes pour un film individuel, nous verrions très probablement qu'un seul groupe se forme dans l'une des zones correspondant à une note basse, moyenne ou élevée.

Étant donné que la plupart des films sont considérés comme moyens, le groupe autour de la zone moyenne a la plus grande probabilité de se produire, et les deux autres groupes ont une probabilité plus faible (mais toujours significative). (Notez que toutes ces probabilités peuvent être quantifiées en principe, mais cela nécessiterait beaucoup de données et aurait le potentiel de transformer cet article en un livre.)

La moins probable serait une distribution uniforme dans laquelle il n'y a pas de groupes, et les préférences des gens sont presque également réparties entre les trois valeurs qualitatives.

Étant donné ces probabilités, la distribution des notes pour un échantillon suffisamment grand de films devrait être une distribution avec un groupe épais dans la zone moyenne, bordé de barres de hauteur décroissante (fréquence), ressemblant ainsi à une distribution normale.

Si vous avez trouvé tout cela difficile à comprendre, considérez cette illustration :

![Image](https://cdn-media-1.freecodecamp.org/images/cU0uQm-YvnPahuzMF8aJfyQg3k6G1EY6xBy8)
_Veuillez noter la distinction entre « probable » et « très probable »._

### IMDB, Rotten Tomatoes, Fandango ou Metacritic ?

Maintenant que nous avons un critère à utiliser, plongeons dans les données.

Il existe de nombreux sites web qui proposent leurs propres notes de films. J'en ai choisi seulement quatre, principalement en fonction de leur popularité, afin de pouvoir obtenir des notes pour des films avec un nombre acceptable de votes. Les heureux gagnants sont [IMDB](http://www.imdb.com/), [Fandango](http://www.fandango.com/), [Rotten Tomatoes](https://rottentomatoes.com/) et [Metacritic](http://www.metacritic.com/).

Pour les deux derniers, je me suis concentré uniquement sur leurs types de notes emblématiques — à savoir le **tomatomètre** et le **metascore** — principalement parce que ceux-ci sont plus visibles pour l'utilisateur sur chacun des sites web (ce qui signifie qu'il est plus rapide de les trouver). Ces notes sont également partagées sur les deux autres sites web (le metascore est partagé sur IMDB et le tomatomètre sur Fandango). En plus de ces notes emblématiques, les deux sites web ont également un type de note moins mis en avant où seuls les utilisateurs peuvent contribuer.

J'ai collecté des notes pour certains des films les plus votés et critiqués en 2016 et 2017. Le jeu de données nettoyé contient des notes pour 214 films et peut être téléchargé depuis [ce dépôt Github](https://github.com/mircealex/Movie_ratings_2016_17).

Je n'ai pas collecté de notes pour les films sortis avant 2016, simplement parce qu'un léger changement est survenu dans le système de notation de Fandango peu après [l'analyse de Walt Hickey](https://fivethirtyeight.com/features/fandango-movies-ratings/), à laquelle je ferai référence plus tard dans cet article.

Je suis conscient que travailler avec un petit échantillon est risqué, mais au moins cela est compensé par l'obtention de la capture la plus récente des distributions des notes.

Avant de tracer et d'interpréter les distributions, laissez-moi quantifier les valeurs qualitatives que j'ai utilisées précédemment : sur une échelle de 0 à 10, un film **mauvais** se situe quelque part entre 0 et 3, un film **moyen** entre 3 et 7, et un film **bon** entre 7 et 10.

Veuillez noter la distinction entre qualité et quantité. Pour garder cela discernable dans ce qui suit, je ferai référence aux notes (quantité) comme étant basses, moyennes ou élevées. Comme avant, la qualité du film est exprimée comme mauvaise, moyenne ou bonne. Si vous vous inquiétez du fait que le terme « moyenne » soit le même, ne vous en faites pas, car je veillerai à éviter toute ambiguïté.

Maintenant, jetons un coup d'œil aux distributions :

![Image](https://cdn-media-1.freecodecamp.org/images/OY6-02GDtcQxYXXNlOfW5lXjbJqIpaZzGXma)
_Chaque note a ses particularités. Pour IMDB et Fandango, chaque barre correspond à une plage de 0,5, et pour les deux autres, la plage d'une barre a une valeur de 5._

À première vue, on peut remarquer que l'histogramme du metascore (c'est ainsi que l'on appelle ce type de graphique) ressemble le plus à une distribution normale. Il a un groupe épais dans la zone moyenne composé de barres de hauteurs irrégulières, ce qui rend le sommet ni émoussé ni pointu.

Cependant, elles sont plus nombreuses et plus hautes que les barres dans chacune des deux autres zones, qui diminuent en hauteur vers les extrémités, plus ou moins progressivement. Tout cela indique clairement que la plupart des metascores ont une valeur moyenne, ce qui est exactement ce que nous cherchons.

Dans le cas d'IMDB, la majorité de la distribution se trouve également dans la zone moyenne, mais il y a un biais évident vers les valeurs moyennes les plus élevées. La zone des notes élevées ressemble à ce que l'on s'attendrait à voir pour une distribution normale **dans cette partie** de l'histogramme. Cependant, la caractéristique frappante est que la zone représentant les notes basses est complètement vide, ce qui soulève un grand point d'interrogation.

Initialement, j'ai mis la faute sur le petit échantillon, pensant qu'un plus grand lui rendrait plus justice. Heureusement, j'ai pu trouver [un jeu de données prêt à l'emploi sur Kaggle](https://www.kaggle.com/deepmatrix/imdb-5000-movie-dataset) contenant les notes IMDB pour 4 917 films différents. À ma grande surprise, la distribution ressemblait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/cKfNBNpTCB1pue2w-yX7QiOaCCL1ELZ-m9XM)
_Cette similitude renforce la confiance quant à la représentativité du plus petit échantillon._

La forme de la distribution ressemble presque à celle de l'échantillon avec 214 films, à l'exception de la zone des notes basses, qui est dans ce cas faiblement peuplée de 46 films (sur 4917). La majorité des valeurs se trouve toujours dans la zone moyenne, ce qui rend la note IMDB digne d'être considérée pour une recommandation, bien qu'il soit clairement difficile de rivaliser avec le metascore, avec ce biais.

En tout cas, ce qui est vraiment formidable avec ce résultat, c'est qu'il peut être utilisé comme un argument solide pour soutenir la thèse selon laquelle l'échantillon de 214 films est assez représentatif de l'ensemble de la population. En d'autres termes, il y a maintenant une plus grande confiance que les résultats de cette analyse seraient les mêmes — ou au moins similaires — aux résultats obtenus si absolument toutes les notes de films des quatre sites web étaient analysées.

Avec cette confiance accrue, passons à l'examen de la distribution des notes de Fandango, qui ne semble pas avoir beaucoup changé depuis l'analyse de Hickey. Le biais est toujours visible vers la partie supérieure du spectre des notes de films, où se trouvent la plupart des notes. La zone pour la moitié inférieure des notes moyennes est complètement vide, tout comme celle pour les notes basses. On peut facilement conclure que la distribution est assez éloignée de mon critère. Par conséquent, je ne la considérerai pas davantage pour une éventuelle recommandation.

(Je promets que le calvaire du défilement vers le haut prendra bientôt fin. Il est beaucoup plus facile de [comparer les distributions](https://fr.wikipedia.org/wiki/Petits_multiples) si elles sont placées les unes à côté des autres, plutôt que d'être dispersées dans l'article.)

Enfin, la distribution du tomatomètre est étrangement uniforme et semblerait encore plus plate sous une stratégie de regroupement différente (une stratégie de regroupement est définie par le nombre total de barres et leurs plages ; vous pouvez jouer avec ces deux paramètres lorsque vous générez un histogramme).

Cette distribution n'est pas facile à interpréter dans ce contexte, car le tomatomètre n'est pas une note classique, mais représente plutôt le pourcentage de critiques qui ont donné une critique positive à un film. Cela le rend inadapté au cadre qualitatif mauvais-moyen-bon, car il rend les films soit bons, soit mauvais. En tout cas, je suppose qu'il devrait toujours se résumer à la même distribution normale, avec la plupart des films ayant une différence modérée entre le nombre de critiques positives et négatives (donnant ainsi de nombreuses notes de 30 % à 70 % de critiques positives), et quelques films ayant une différence significativement plus grande, dans un sens ou dans l'autre.

Étant donné la dernière considération et la forme de la distribution, le tomatomètre ne répond pas à mon critère. Il **pourrait** être qu'un échantillon plus grand lui rendrait plus justice, mais même ainsi, si je devais le recommander, je le ferais avec quelques réserves en raison du système de notation positif ou négatif vague.

À ce stade de l'analyse, je pourrais dire qu'en regardant les distributions, ma recommandation est le metascore.

Cependant, la distribution d'IMDB semble également digne d'être considérée, surtout si vous ajustez un peu les intervalles de notation pour les trois catégories qualitatives (intervalles que j'ai définis moi-même, plus ou moins arbitrairement). De cette perspective, recommander le metascore principalement par un examen visuel est clairement insuffisant.

Je vais donc essayer de délimiter entre ces deux en utilisant une méthode **quantitative**.

L'idée est d'utiliser la variable Fandango comme référence négative, puis de déterminer quelle variable, entre la note IMDB et le metascore, est la moins corrélée avec elle (j'appelle ces variables car elles peuvent prendre différentes valeurs — par exemple, le metascore est une variable car il prend différentes valeurs, selon le film).

Je vais simplement calculer quelques coefficients de corrélation, et la variable avec la plus petite valeur sera ma recommandation (j'expliquerai ensuite comment fonctionnent ces coefficients de corrélation). Mais avant cela, laissez-moi brièvement justifier le choix de la variable Fandango comme référence négative.

### Les utilisateurs de Fandango aiment trop les films

Une raison de ce choix est que la distribution des notes de films de Fandango est la plus éloignée de celle d'une distribution normale, avec ce biais évident vers la partie supérieure du spectre des notes de films.

L'autre raison est le nuage de suspicion autour de Fandango laissé par [l'analyse de Walt Hickey](https://fivethirtyeight.com/features/fandango-movies-ratings/). En octobre 2015, il était également perplexe face à une distribution similaire et a découvert que sur le site web de Fandango, les notes numériques étaient toujours arrondies à la demi-étoile supérieure suivante, et non à la plus proche (par exemple, une note moyenne de 4,1 pour un film aurait été arrondie à 4,5 étoiles, au lieu de 4,0).

L'équipe de Fandango a corrigé le système de notation biaisé et a dit à Hickey que la logique de notation était plutôt un « bug logiciel » sur leur site web, pointant vers un système non biaisé sur leur application mobile. (Plus d'informations à ce sujet dans [l'article de Hickey](https://fivethirtyeight.com/features/fandango-movies-ratings/).) L'ajustement a changé certains paramètres statistiques pour le mieux, mais pas assez pour me convaincre de ne pas travailler avec la variable Fandango comme référence négative.

Voici à quoi ressemble le changement :

![Image](https://cdn-media-1.freecodecamp.org/images/J4-L8cpNLahQbmhmlSrphB9gBe2pUrkLDSUi)
_J'ai normalisé tous les autres types de notes pour correspondre à ceux de Fandango — je les ai convertis en un système de notation de 0 à 5, puis j'ai arrondi les valeurs converties au 0,5 le plus proche. L'acronyme « FTE » signifie FiveThirtyEight, la publication en ligne pour laquelle Hickey écrit._

Maintenant, zoomons sur Fandango :

![Image](https://cdn-media-1.freecodecamp.org/images/svsm-uIkn-7xcDGurSEtPdSJlXXmORfoO4n2)
_Les barres bleues représentent l'année 2017, et les rouges l'année 2015._

### Entre le metascore et la note IMDB, lequel est le moins corrélé avec la note Fandango ?

Le moins corrélé avec la note Fandango est le metascore. Il a une valeur de **Pearson r** de 0,38 par rapport à Fandango, tandis que la note IMDB a une valeur de 0,63.

Maintenant, laissez-moi expliquer tout cela.

Lorsque deux variables changent, prenant différentes valeurs, elles sont corrélées s'il y a un modèle correspondant aux deux changements. Mesurer la [corrélation](http://www.mathsisfun.com/data/correlation.html) signifie simplement mesurer dans quelle mesure il existe un tel modèle.

L'une des façons de réaliser cette mesure est de calculer le Pearson r. Si la valeur est +1,0, cela signifie qu'il y a une corrélation positive parfaite, et si elle est de -1,0, cela signifie qu'il y a une corrélation négative parfaite.

Le degré de corrélation entre les variables diminue à mesure que le Pearson r approche de 0, des deux côtés négatif et positif.

Visualisons mieux cela :

![Image](https://cdn-media-1.freecodecamp.org/images/dcM7DKZMC-dJFgSIaUw3jDQLegizZwcDaMwB)
_Les notes peuvent être tracées sur un graphique. Chacun des petits points qui ensemble forment les formes ci-dessus pourrait décrire les notes de deux variables (par exemple, Fandango et IMDB) pour un film spécifique. Crédit image : Denis Boigelot (source : [Wikipedia](https://fr.wikipedia.org/wiki/Corr%C3%A9lation_et_d%C3%A9pendance#/media/Fichier:Correlation_examples2.svg))._

Maintenant, pour mettre l'abstraction ci-dessus en contexte, si nous comparons comment les valeurs pour deux types de notes changent — disons celles de Fandango et d'IMDB — nous pouvons déterminer le degré auquel il y a un modèle correspondant aux deux changements.

Étant donné les coefficients de corrélation mentionnés précédemment, il y a un modèle entre Fandango et IMDB dans une plus grande mesure que pour Fandango et le metascore. Les deux coefficients sont positifs, et, à ce titre, la corrélation est dite positive, ce qui signifie que lorsque les notes de Fandango augmentent, les notes d'IMDB tendent également à augmenter, plus que les metascores.

En d'autres termes, pour une note donnée de film sur Fandango, il est plus probable que le metascore soit plus différent de celle-ci que la note IMDB.

### Le verdict : utilisez le metascore de Metacritic

En résumé, je recommande de vérifier le metascore chaque fois que vous cherchez une note de film. Voici comment cela fonctionne, ainsi que ses inconvénients.

En bref, le metascore est une moyenne pondérée de nombreuses critiques provenant de critiques réputés. L'équipe de Metacritic lit les critiques et attribue à chacune un score de 0 à 100, qui est ensuite pondéré, principalement en fonction de la qualité et de la source de la critique. Vous pouvez en savoir plus sur leur système de notation [ici](http://www.metacritic.com/faq#item11).

Maintenant, je veux simplement souligner quelques inconvénients du metascore :

* Les coefficients de pondération sont confidentiels, donc vous ne verrez pas dans quelle mesure chaque critique a compté dans le metascore.
* Vous aurez du mal à trouver des metascores pour des films moins connus sortis avant 1999, l'année où Metacritic a été créé.
* Certains films récents dont la langue principale n'est pas l'anglais ne sont même pas listés sur Metacritic. Par exemple, les films roumains [Two Lottery Tickets (2016)](http://www.imdb.com/title/tt5700224/?ref_=nv_sr_1) et [Eastern Business (2016)](http://www.imdb.com/title/tt5610362/?ref_=nv_sr_2) ne sont pas listés sur Metacritic, alors qu'ils le sont sur IMDB, avec des notes.

### Quelques mots de plus

En résumé, dans cet article, j'ai fait une seule recommandation sur l'endroit où chercher une note de film. J'ai recommandé le metascore, basé sur deux arguments : sa distribution ressemble le plus à une distribution normale, et il est le moins corrélé avec la note Fandango.

Tous les éléments quantitatifs et visuels de l'article sont reproductibles en Python, comme le montre [ce lien](https://nbviewer.jupyter.org/github/mircealex/Movie_ratings_2016_17/blob/master/Mv_ratings_project.ipynb).

Merci d'avoir lu ! Et bon cinéma !