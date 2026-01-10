---
title: Comment concevoir des graphiques horribles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T10:07:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-terrible-graphs-3b213d909387
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JoT-0M2YUb95dcHWIrMY3Q.jpeg
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment concevoir des graphiques horribles
seo_desc: 'By Michelle Jones

  Warning: contains graph violence

  Graphs are used to present information in a visual, summary format. They can be
  used instead of tables. Used successfully, graphs reduce the amount and complexity
  of data used in sentences. Hopefully...'
---

Par Michelle Jones

#### ⚠️ Avertissement : contient de la violence graphique

Les graphiques sont utilisés pour présenter des informations sous une forme visuelle et synthétique. Ils peuvent être utilisés à la place des tableaux. Utilisés avec succès, les graphiques réduisent la quantité et la complexité des données utilisées dans les phrases. Espérons que cet article vous donne des outils supplémentaires pour décider quels graphiques (ne pas) utiliser.

La personne qui a travaillé le plus dur et le plus longtemps dans le domaine de la conception de graphiques est **Edward Tufte**. J'ai inclus un lien vers son site web sous Ressources.

Tout le monde qui me connaît bien sait aussi deux informations clés. Je déteste les camemberts et je déteste les histogrammes mal faits. J'ai pris des graphiques de rapports publics pour illustrer mes propos. J'ai également tiré les exemples de différentes disciplines, pour montrer que la mauvaise conception de graphiques est partout.

Enfin, j'ai délibérément choisi des rapports où le concepteur de graphiques n'est pas identifié, ou il y a plusieurs auteurs. Le but de cet article n'est pas de nommer et de honte des individus, et le concepteur n'a généralement pas beaucoup à dire dans le processus d'approbation de la publication. Les gestionnaires et/ou les réviseurs pairs ont décidé que ces graphiques étaient acceptables à utiliser.

### Camemberts

![Image](https://cdn-media-1.freecodecamp.org/images/5S8tNA6GCGEl-ANW7fu20o63I35bZ46Trsdy)
_[Ceci est un camembert très informatif.](https://www.flickr.com/photos/53149458@N08/14124697651" rel="noopener" target="_blank" title=")_

#### Camemberts simples

Le but des camemberts est de montrer comment des catégories mutuellement exclusives et liées contribuent chacune à l'information sur cette catégorie.

Commençons par un exemple simple. Ci-dessous se trouve un camembert contenant seulement deux catégories : masculin et féminin. Les camemberts sont souvent utilisés pour montrer le ratio de sexe, par exemple lors de la présentation des résultats d'enquêtes.

![Image](https://cdn-media-1.freecodecamp.org/images/WzugVHg6rAPsT9IMCqcG6M5OzZNkjDFTq26b)
_[Proportion d'auteurs examinés dans ce journal, 2013.](http://thestellaprize.com.au/the-count/the-stella-count-2013/" rel="noopener" target="_blank" title=")_

**Mais pourquoi utiliser un camembert pour une classification binaire ?** Pour réitérer, les catégories sont mutuellement exclusives. Nous pourrions simplement dire que 49 % des livres examinés avaient des autrices. Il est facile de supposer et de calculer que 51 % étaient écrits par des auteurs masculins.

Le but du site web est de souligner le manque de critiques pour les livres écrits par des femmes. Si vous allez sur le lien, vous verrez une série de 14 camemberts, un pour chaque journal évalué par le Stella Count, pour 2013. Même avec un grand écran, vous devrez faire défiler pour les voir tous. Et le camembert pour The Monthly a les couleurs des catégories inversées — il est difficile de garder une trace de la mise en forme cohérente pour autant de graphiques !

Je pense que l'information serait mieux présentée dans un histogramme. J'ai utilisé [R](https://cran.r-project.org/) pour cela. Les packages que j'ai appelés sont [**ggplot2**](https://cran.r-project.org/web/packages/ggplot2/index.html) et [**ggridges**](https://cran.r-project.org/web/packages/ggridges/index.html). ggridges a été utilisé pour alterner les deux couleurs à travers les barres. Je pense que l'alternance des couleurs améliore la lisibilité du graphique par rapport à n'avoir qu'une seule couleur pour chaque barre. Il y a eu un petit problème que je ne peux pas résoudre, avec l'alternance des couleurs vers le bas, donc j'ai forcé un ordre inverse pour deux barres en utilisant `FillValues`.

```
FemaleAuthors <- data.frame(Publication=c("The Advertiser", "The Age", "Australian Book Review",                                                 "The Australian Financial Review", "Books+Publishing",                                                 "The Courier-Mail","The Daily Telegraph", "Good Reading",                                                 "The Monthly","Sunday Age","Sunday Tasmanian",                                                 "The Sydney Morning Herald","The Weekend Australian",                                                "The West Australian"),                            PropOfFemales=c(49,42,47,15,61,41,46,49,41,49,49,43,35,58))FemaleAuthors <- FemaleAuthors[order(-FemaleAuthors$PropOfFemales, -FemaleAuthors$Publication),]FemaleAuthors$FillValues <- c(rep(c("A","B"),5),"B","A","A","B")
```

```
library("ggplot2")library("ggridges")ggplot(data=FemaleAuthors,aes(x=reorder(Publication, PropOfFemales), y=PropOfFemales, fill=FillValues)) +  geom_bar(stat="identity",            colour="black", width=1) +  scale_y_continuous(breaks=seq(0, 70, by=5),                     limits=c(0,70),                     expand=c(0,0)) +  scale_fill_cyclical(values=c("plum3","orchid2"))+  labs(x="Publication", y="Proportion de livres examinés \navec des autrices")+  coord_flip() +    theme(panel.grid.minor.y=element_blank(),         panel.grid.major.x=element_line(color="gray"),        panel.background=element_blank(),         axis.line = element_line(color="gray", size = 1),        axis.text=element_text(size=10),        axis.title=element_text(size=15),        plot.margin=margin(5,5,5,5),        legend.position = "none")
```

![Image](https://cdn-media-1.freecodecamp.org/images/9AO3F-hvxtVG5cKVbwv8LpHiGrI12aj9QaBB)
_Ma présentation préférée pour ce type de données._

L'information importante de ces 14 camemberts — la représentation des autrices dans les critiques de livres de journaux — est maintenant évidente à première vue.

Pour faciliter l'interprétation, j'ai codé les barres avec des nuances rosées. (Oui, c'est un stéréotype, mais le rose souligne le fait que ce sont les résultats pour les femmes). Les couleurs alternées facilitent le suivi de chaque barre par l'œil. J'ai graphé les données par ordre décroissant de représentation féminine, renforçant le point du Stella Count.

Bien que les proportions exactes ne puissent pas être lues sur le graphique, la ligne de grille à chaque 5 % donne une idée du nombre. Les nombres importants peuvent être mentionnés dans le texte.

#### Camemberts plus complexes

Le camembert ci-dessous a beaucoup de parts et concerne l'expression des gènes. Seules trois des parts sont assez grandes pour contenir du texte. Chaque catégorie est étiquetée avec sa proportion respective.

Une catégorie, « Fonction diverse », ne contenait aucun gène altéré et est montrée adjacente au camembert. Elle flotte dans l'espace. Cependant, parce que cette fonction est située à côté de la part violette, un rapide coup d'œil suggère qu'elle est liée à cette part. La ligne vers « Régulation de l'acide nucléique » montre la catégorie réelle, mais toutes les parts n'ont pas de lignes reliant la catégorie.

![Image](https://cdn-media-1.freecodecamp.org/images/Qx1L7CUR-sGhhHWQ6Edabw3VusTbppb79rBF)
_[Les camemberts se trouvent également dans les articles académiques.](http://www.mdpi.com/2075-4450/4/3/506/htm" rel="noopener" target="_blank" title=")_

Encore une fois, je peux construire un histogramme car toutes les données sont incluses dans le graphique original. En utilisant R, et le package [**RColorBrewer**](https://cran.r-project.org/web/packages/RColorBrewer/index.html) pour obtenir plus de couleurs que celles contenues dans Set3 :

```
GeneExpressionProfile <- data.frame(AlteredGenes=factor(c("Apotosis-associated","Cellular Maintenance & Signalling",                                                          "Chitin Binding","Detoxification","Insect Digestion-related",                                                          "Insect Growth","Insect Immunity", "Insect Metabolism",                                                          "Miscellaneous Function","Nucleic Acid Regulation",                                                          "Stress Response","Virus Replication / Altered Host Physiology",                                                          "Unknown")),                                    PercentAltered=c(1,10,2,4,25,2,4,10,0,5,1,2,34))GeneExpressionProfile <- GeneExpressionProfile[order(-GeneExpressionProfile$PercentAltered),]library("ggplot2")library("ggridges")library("RColorBrewer")ggplot(data=GeneExpressionProfile,aes(x=reorder(AlteredGenes, PercentAltered), y=PercentAltered, fill=AlteredGenes)) +  geom_bar(stat="identity",            colour="black", width=1) +  scale_y_continuous(breaks=seq(0, 50, by=5),                     limits=c(0,50),                     expand=c(0,0)) +  scale_fill_manual(values=colorRampPalette(brewer.pal(12,"Set3"))(13)) +  labs(x="Groupe de gènes", y="Proportion de gènes altérés \nparmi les gènes étudiés")+  coord_flip() +  theme(panel.grid.minor.y=element_blank(),         panel.grid.major.x=element_line(color="gray"),        panel.background=element_blank(),         axis.line = element_line(color="gray", size = 1),        axis.text=element_text(size=10),        axis.title=element_text(size=15),        plot.margin=margin(5,5,5,5),        legend.position = "none")
```

Produit l'histogramme suivant

![Image](https://cdn-media-1.freecodecamp.org/images/BvcxImQgIwEJNpIOzRDu4IS0DP-picc9cypI)
_Je pense que cela est plus facile à interpréter._

### Histogrammes

Comme vous pouvez le voir, j'aime vraiment les histogrammes. Cependant, il existe plusieurs façons de rendre les histogrammes moins interprétables. Ce sont des histogrammes empilés.

#### Histogrammes empilés

Un type d'histogramme empilé utilise des proportions, donc chaque composant à l'intérieur de chaque barre fait un total de 100 %. Ceux-ci peuvent être visuellement complexes, et les messages du graphique ne sont pas toujours clairs pour un lecteur.

![Image](https://cdn-media-1.freecodecamp.org/images/KEzW1mFBja36wyDHJM8iZHzSyLYsPBCJhVgn)
_[Ceci est un histogramme empilé très compliqué.](https://www.researchgate.net/figure/Microbial-composition-of-asthma-and-control-samples-Stacked-bar-chart-shows-different_fig3_281004993" rel="noopener" target="_blank" title=")_

De plus, parce que toutes les barres sont forcées d'avoir la même longueur, les différences dans les nombres qui sous-tendent les proportions sont masquées. Il pourrait alors être trompeur de comparer les proportions relatives entre les barres.

Un facteur qui représente 30 % d'une barre peut ne pas être intéressant si le résultat concerne trois personnes sur dix. Notre interprétation de l'importance changerait si le même pourcentage était basé sur 200 personnes.

Un autre exemple, moins compliqué, est ci-dessous. Il y a deux problèmes principaux avec ce graphique. Premièrement, les barres incluent les pourcentages. C'est une admission que les gens ne peuvent pas interpréter les valeurs à partir de la longueur des sections de barre. Si vous cliquez sur le lien (dans la légende), vous trouverez que **tous** les pourcentages sont listés, pour **toutes** les années, sur la même page sous le graphique.

Pourquoi est-ce mauvais ? Toutes les informations du graphique sont dupliquées dans le texte. Pourquoi inclure l'histogramme ?

![Image](https://cdn-media-1.freecodecamp.org/images/79xlhFqZRSJQUOVnVOzhicxK7cYkW7WFwaVC)
_[Ô Canada, littéralement.](http://www.justice.gc.ca/eng/rp-pr/jr/jr13/fig5l.html" rel="noopener" target="_blank" title=")_

L'utilisation de nombres à l'intérieur des sections de barre semble être relativement courante. Un autre exemple est ci-dessous. Ici, ils ont utilisé un schéma de couleurs clair à foncé pour chaque section. Je pense que les schémas de couleurs dégradés rendent les graphiques plus difficiles à lire. Les schémas de couleurs dégradés sont également difficiles à interpréter lorsque les barres ne sont pas empilées.

![Image](https://cdn-media-1.freecodecamp.org/images/cfLt3LQ56d3JgyywmbmoDc7G2NTWw8nEsmKO)
_[Exemple de l'Australie.](https://www.fwc.gov.au/documents/awrs/awrs-first-findings.pdf" rel="noopener" target="_blank" title=")_

L'autre type d'histogramme empilé est celui où les sections de barre prennent leurs valeurs réelles. Cela donne des barres de hauteurs différentes. L'avantage est que nous pouvons voir les nombres réels. Cependant, le graphique contient toujours beaucoup d'informations, et seules les plus grandes variations de catégories sont évidentes.

![Image](https://cdn-media-1.freecodecamp.org/images/uUxEDjwgJcznGLe71xSB2DLjgLj1tJNDpqZV)
_[Histogramme empilé qui n'est pas redimensionné en proportions.](http://www.hybridcars.com/how-green-cars-can-help-americas-presidents-keep-their-promises/half-the-oil-savings-over-time-bar-graph/" rel="noopener" target="_blank" title=")_

### Mention spéciale : les graphiques 3-D

J'ai mis ceux-ci dans une section séparée pour montrer que la 3-D n'est pas une bonne décision pour les graphiques.

#### Camemberts 3-D

La seule chose pire qu'un camembert 2-D est un camembert 3-D.

![Image](https://cdn-media-1.freecodecamp.org/images/uQkbeH-5ZdknFknyKOq7JMlonsKlrNcBrwuK)
_[En avoir deux ensemble n'est pas deux fois plus informatif.](http://www.budget.gov.au/2011-12/content/overview/html/overview_46.htm" rel="noopener" target="_blank" title=")_

La taille relative des parts est encore plus difficile à interpréter. Parce que le graphique est en 2-D, les parts deviennent inexactes. Utilisons le graphique du bas comme exemple. J'arrondis au million le plus proche dans chaque exemple.

Comparez « Sécurité sociale et bien-être » (122 millions de dollars) avec « Santé » (60 millions de dollars). La part Santé semble-t-elle environ la moitié de la taille de la part Sécurité sociale et bien-être ?

Comparez « Services gouvernementaux généraux » (97 millions de dollars) avec la part Sécurité sociale et bien-être. Les services gouvernementaux généraux représentent environ 4/5 des dépenses de la sécurité sociale et du bien-être, mais le camembert les fait paraître à peu près de la même quantité.

L'ordre des catégories n'est pas clair non plus. Elles ne sont pas dans l'ordre de taille. Elles ne sont pas dans l'ordre alphabétique.

Quelle est la solution ? Encore une fois, la même que pour les camemberts 2-D. S'il y a peu de catégories, un histogramme est une meilleure présentation des données.

Voyons comment le camembert du bas se présente sous forme d'histogramme, en utilisant [R](https://cran.r-project.org/). J'utilise le package **ggplot2** pour faire le tracé, et le package **stringr** pour gérer le retour à la ligne du texte sur les étiquettes des axes.

J'aime la séquence de couleurs et la combinaison de Set3 dans la palette ColorBrewer. J'ai également supprimé l'encombrement du graphique en supprimant la couleur de fond et les lignes de grille superflues. J'ai ordonné les catégories de dépenses par montant décroissant. J'ai enveloppé le texte de l'axe des y pour fournir un meilleur rapport entre la largeur de l'axe des y et la largeur interne du tracé. La légende a été supprimée. J'ai élargi la marge extérieure droite du graphique pour que la valeur finale de l'axe des x ne soit pas coupée.

```
TaxExpenditure <- data.frame(Expenditure.Type=c(factor("Industrie & main-d'œuvre", "Défense", "Sécurité sociale & bien-être",                                                "Services communautaires & culture", "Santé", "Infrastructure, transport & énergie",                                                "Éducation", "Services gouvernementaux généraux")),                             Expenditure.Amount=c(14.843, 21.277, 121.907, 8.044, 59.858, 13.221, 29.870, 96.797))
```

```
library("ggplot2")library("stringr")ggplot(data=TaxExpenditure,aes(x=reorder(Expenditure.Type, Expenditure.Amount), y=Expenditure.Amount,                                fill=Expenditure.Type)) +  geom_bar(stat="identity") +  scale_y_continuous(breaks=seq(0, 125, by=25),                     limits=c(0,125),                     expand=c(0,0)) +  scale_x_discrete(labels=function(x) str_wrap(x, width=20))+  labs(x="Type de dépenses", y="Dépenses (en millions de dollars)")+  scale_fill_brewer(palette="Set3") +  coord_flip() +  theme(panel.grid.minor.y=element_blank(),         panel.grid.major.x=element_line(color="gray"),        panel.background=element_blank(),         axis.line = element_line(color="gray", size = 1),        axis.text=element_text(size=10),        axis.title=element_text(size=15),        plot.margin=margin(5,15,5,5),        legend.position = "none")
```

Le graphique résultant est montré ci-dessous. Les différences relatives dans les dépenses sont beaucoup plus faciles à voir par rapport au camembert.

![Image](https://cdn-media-1.freecodecamp.org/images/tOB5Prt1fnHPdsOfobfljyKTQ-6VXV4ROGp1)

#### Camemberts 3-D éclatés

Les amis ne laissent pas les amis créer des camemberts 3-D éclatés.

![Image](https://cdn-media-1.freecodecamp.org/images/sKOQUXHhAZh8nVNYNrynG5980Hxp3jrRrFN8)
_[Celui-ci a une légende, bien que les parts soient étiquetées.](http://www.tornadoproject.com/cellar/fscale.htm" rel="noopener" target="_blank" title=")_

#### Histogrammes 3-D

Les histogrammes 3-D sont notoirement difficiles à interpréter correctement, car ils tentent de compresser trois dimensions dans un espace 2-D. Les exemples ci-dessous sont particulièrement compliqués, en raison du positionnement du plan zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/IZhNSzihGlKHoNfzz39e6QErL9RRgZ99rqrS)
_[Source](https://www.researchgate.net/figure/Three-dimensional-bar-graph-for-data-from-miniaturized-ISES-for-the-Co-salen-array-A_fig2_280076489" rel="noopener" target="_blank" title=")._

### Plus de suggestions pour de meilleurs graphiques

#### N'utilisez pas de motifs

L'utilisation de la couleur/échelle de gris dans les graphiques est meilleure que l'utilisation de motifs. Les motifs, comme le hachurage, rendent les graphiques plus difficiles à lire.

Exemple 1 :

![Image](https://cdn-media-1.freecodecamp.org/images/WDjLtJU1omeJlIZTA4nH9x8oITDJX6zCcAov)
_[Beaucoup de barres, de lignes, de zones de texte et de rayures diagonales.](https://www.msd.govt.nz/documents/about-msd-and-our-work/publications-resources/monitoring/household-income-report/2017/2017-incomes-report-wed-19-july-2017.pdf" rel="noopener" target="_blank" title=")_

Exemple 2 :

![Image](https://cdn-media-1.freecodecamp.org/images/5e9N7zU9vIys16OzFwBTgoJZTCoALC141Coo)
_[Ceci est un graphique utilisant des données fictives, mais le point est clair.](https://blogs.sas.com/content/graphicallyspeaking/2017/10/30/fill-patterns/" rel="noopener" target="_blank" title=")_

#### Utilisez une palette de couleurs appropriée

Différentes palettes de couleurs sont disponibles pour les graphiques. Toutes ne sont pas bonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/0d9oe5I0vFQHJ7kBhkle5xxDhLWJcxzCblVq)
_[Je ne suis pas sûr de savoir pourquoi SAS a inclus cette capacité.](http://support.sas.com/kb/43/770.html" rel="noopener" target="_blank" title=")_

#### **Utilisez des échelles d'axes appropriées**

Votre axe numérique doit commencer à zéro. Si vos nombres sont très grands, exprimez-les dans un ordre de grandeur approprié, par exemple en utilisant des millions de dollars, ou des milliers d'heures comme base.

Si votre graphique montre alors peu de variation entre les valeurs des catégories, demandez-vous pourquoi un graphique est nécessaire.

Vouliez-vous montrer un changement d'une année à l'autre ? Si oui, vous pourriez graphiquer le pourcentage de changement d'une année à l'autre, au lieu de graphiquer les nombres bruts.

Vouliez-vous souligner l'impact d'un facteur particulier au fil du temps ? Une option est de graphiquer ce facteur et rien d'autre.

#### L'ordre des catégories est important

Aucune règle ne convient à tous pour décider de l'ordre des catégories. Une option, que j'ai utilisée dans mes exemples, est par hauteur. Comment allez-vous décider de votre ordre :

* du plus haut au plus bas ?
* alphabétique par catégorie ?
* un autre ordre ?

L'ordre que vous utilisez dépend de l'information principale dont le client a besoin à partir du graphique.

#### Vérifiez l'exactitude de votre graphique

![Image](https://cdn-media-1.freecodecamp.org/images/5FF2iyjP8TAckxGDsGFaCltYzAKObFZKdqsN)
_C'est plus comme 55/45, mais aucune idée de comment les zones colorées peuvent être si incorrectes._

![Image](https://cdn-media-1.freecodecamp.org/images/TkFFFryYZeqbZiK9KTD7kASTDiuOpIe3AhaS)
_[Je n'ai jamais vu un camembert en couches auparavant.](http://www.jobvine.co.za/what-does-it-take-to-get-a-job-at-google/" rel="noopener" target="_blank" title=")_

#### Envisagez d'utiliser des barres d'erreur

Le graphique ci-dessous provient d'une étude qui a examiné l'effet du THC sur les temps de réaction des sujets et la précision des réponses, en utilisant un stimulus informatisé.

Ils ont inclus des barres d'erreur sur chaque mesure, afin que nous puissions voir d'un coup d'œil si l'un des résultats différait entre les groupes de sujets (placebo versus THC). Seule une palette de couleurs en niveaux de gris a été utilisée, et elle est très efficace.

![Image](https://cdn-media-1.freecodecamp.org/images/gkk5NVU0iLC9-H17YdJ3zwoQtgnOHYMiHL1G)
_[Histogramme simple transmettant beaucoup d'informations.](https://www.researchgate.net/figure/Bar-graphs-showing-average-Reaction-Time-for-congruent-and-incongruent-trials-for_fig1_51760950" rel="noopener" target="_blank" title=")_

### Ressources pour créer de meilleurs graphiques

Le gourou pour créer de meilleurs graphiques est [Edward Tufte](https://www.edwardtufte.com/tufte/). Tous ses livres sont des œuvres d'art, mais pour la présentation des nombres, je recommande [The Visual Display of Quantitative Information](https://www.edwardtufte.com/tufte/books_vdqi).

Un blog que je trouve particulièrement utile est [FlowingData](http://flowingdata.com/). Même si vous ne devenez pas un membre (payant) du site, Nathan est un éditeur prolifique et vous pouvez obtenir des idées à partir de ses publications. Certaines de ces publications sont des graphiques qu'il a réalisés, et d'autres sont des exemples de graphiques bien conçus qu'il a sourcés ailleurs.

_Avertissement : aucun graphique réel n'a été blessé lors de la création de cet article._