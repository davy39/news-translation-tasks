---
title: Comment un graphique à bulles révèle les meilleures villes où vivre aux États-Unis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-02T11:03:26.000Z'
originalURL: https://freecodecamp.org/news/how-a-bubble-plot-can-reveal-the-best-places-to-live-in-the-us-e2054c844062
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HffpBV9kNhHCBT0D77zm3w.png
tags:
- name: Life Hacking
  slug: life-hacking
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Real Estate
  slug: real-estate
- name: 'tech '
  slug: tech
seo_title: Comment un graphique à bulles révèle les meilleures villes où vivre aux
  États-Unis
seo_desc: 'By Zhen Liu

  In this article, I’ll show you some exciting facts about American cities, the value
  of bubble plots in deciding which city to live in, and how to create those plots.

  Are you thinking about investing in real estate in 2018? Moving to a new...'
---

Par Zhen Liu

Dans cet article, je vais vous montrer quelques faits passionnants sur les villes américaines, la valeur des graphiques à bulles pour décider dans quelle ville vivre, et comment créer ces graphiques.

Envisagez-vous d'investir dans l'immobilier en 2018 ? Déménager dans une nouvelle ville ? Lorsque vous envisagez ces décisions, vous devez peser différents facteurs comme le taux de chômage, le prix du logement, la taille de la ville, la sécurité, etc. Même avec toutes ces données et quatre graphiques en barres correspondants, vous serez toujours perplexe en regardant ce tableau. Vous essaierez de trouver les meilleurs candidats, mais ces facteurs racontent des histoires différentes... Cela semble être un problème complexe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YJKL-SBnPHPO5Eb69w-eGQ.png)

Alors, existe-t-il un moyen de visualiser tous ces facteurs en 1 graphique et de les comparer TOUS ? Oui, nous pouvons utiliser un graphique à bulles !

#### _Qu'est-ce qu'un graphique à bulles ?_

Un graphique à bulles est un type de graphique qui affiche plus de deux dimensions de données (par rapport aux graphiques de dispersion traditionnels). En plus de tracer un point sur un plan X-Y, il utilise la taille, la couleur ou la forme du point pour afficher plus de dimensions.

Nous utilisons **le taux de chômage comme axe X, le prix médian des logements comme axe Y**, et **la population des villes comme taille des points**. Cela fait une bonne troisième dimension. La couleur est attribuée aléatoirement à chaque ville.

### La meilleure ville des États-Unis où vivre est... (attendez)

![Image](https://cdn-media-1.freecodecamp.org/images/1*wyVxxjaM_oQF0utG6__cog.png)

Gagnante : **Nashville !**

Autres recommandations : **Austin, Omaha, Milwaukee, Dallas, Minneapolis, Denver et Aurora.**

Elles ont un faible taux de chômage (et donc une plus grande chance de trouver un emploi), et un faible prix des logements, car elles se trouvent dans le coin inférieur gauche du graphique. Que signifie cela ?

**Cela signifie que vous pouvez faire vos choix en fonction de ce graphique.**

Par exemple, si vous considérez que le taux de chômage est plus important et que vous ne vous souciez pas des prix plus élevés des logements, alors Honolulu, Oakland, Boston et San Diego sont de bons candidats.

### Et si on ajoutait la sécurité comme autre facteur ?

Bien sûr. Ajoutons la sécurité comme quatrième facteur (les trois autres facteurs sont toujours le prix des logements, le taux de chômage et la population). Au lieu d'attribuer aléatoirement une couleur à une ville, nous utilisons **l'échelle de couleur pour le crime** (taux de criminalité pour 100 000 personnes). **Rouge** signifie plus de criminalité et **bleu** signifie moins.

#### Le résultat change-t-il ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*hjgKmyxuTeXeNTyxE9shiA.png)

Oui ! Si la sécurité est très importante pour vous, alors Milwaukee pourrait ne pas être un si bon choix parmi les recommandations précédentes (même si elle se trouve dans le coin inférieur gauche du graphique).

**Maintenant, vous voyez la puissance d'un graphique à bulles :** la capacité de démontrer plusieurs facteurs en un seul graphique 2D. Si vous n'avez que des graphiques en barres pour ces facteurs, il est difficile d'identifier les villes avec une combinaison idéale de facteurs. Le graphique à bulles a essentiellement créé une "fonction objective visuelle" pour vous aider à optimiser un problème de prise de décision à plusieurs variables.

### **Comment le taux de chômage et le prix des logements évoluent-ils au fil du temps ?**

Nous pouvons créer un graphique de mouvement interactif pour ajouter le temps comme dimension (de 2013 à 2017) afin de voir comment ces facteurs évoluent pour ces villes au fil du temps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yYFcThB3pQ8wxPODrP4ZgQ.gif)

Pour éviter trop d'informations visuelles, je n'ai pas utilisé les données sur la criminalité et j'ai utilisé différentes couleurs pour représenter quelques villes sélectionnées.

La bonne nouvelle est que le taux de chômage pour presque toutes les villes a considérablement diminué (en se déplaçant de droite à gauche). Mais la mauvaise nouvelle est que les prix des logements augmentent assez rapidement (surtout pour San Francisco, San Jose, Los Angeles, New York et Seattle).

Vous voulez créer les graphiques vous-même ? Voici mon code pour les graphiques à bulles et le graphique de mouvement en R. Amusez-vous bien avec les graphiques :)

```
################ Graphique à bulles ################library(data.table)library(ggplot2)library(ggrepel)
```

```
bubble_data <-fread("https://raw.githubusercontent.com/zhendata/Medium_Posts/c007346db1575aca391a6623c87bb5a31a60b365/bubble_plot_merged_city_data.csv",sep=",")
```

```
bubble_plot <- ggplot(bubble_data,                aes(x = Unemployment_Rate, y = Home_Price/1000)) + 
```

```
geom_point(aes(size = Population, fill = Total_Crime),shape=21) +# Créer des 'bulles' en attribuant une taille à une variable #
```

```
scale_fill_continuous(low = "#33FFFF", high ="#FF6699" ) +scale_size_area(max_size = 20)+# Sélectionner l'échelle de couleur des bulles et la taille maximale des bulles #
```

```
geom_text_repel(          aes(label = City),nudge_x = 0,nudge_y = 0.75,size = 6) +# Utiliser geom_text_repel pour éloigner les étiquettes les unes des autres #
```

```
theme_bw()+# Utiliser un fond blanc au lieu du fond gris par défaut #
```

```
ggtitle("Meilleures villes des États-Unis où vivre") +labs(x = "Taux de chômage %", y = "Prix des logements",       size = "Population",fill="Criminalité") +theme(plot.title = element_text(size=25, hjust = 0.5),        axis.title=element_text(size=20, face = "bold"),        axis.text=element_text(size=15)) +# Styliser le titre et les axes #
```

```
scale_y_continuous(name="Prix des logements", breaks = seq(0, 1500, by=250),                       labels=c("0", "250K", "500K", "750K", "1000k",    "1250k", "1500K"))# Rendre l'axe Y plus lisible en remplaçant les nombres scientifiques par "K" #
```

```
print(bubble_plot)
```

```
################# Graphique de mouvement #################library(data.table)library(googleVis)
```

```
motion_data <-fread("https://raw.githubusercontent.com/zhendata/Medium_Posts/c007346db1575aca391a6623c87bb5a31a60b365/motion_chart_merged_city_data.csv",sep=",")
```

```
motion_chart <- gvisMotionChart(motion_data, idvar = "City", timevar = "Year",xvar = "Unemployment Rate",yvar= "Home Price",sizevar="Population")
```

```
plot(motion_chart)# R ouvre automatiquement un onglet dans le navigateur pour vous# Le lecteur Flash doit être activé dans le navigateur 
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*J9UiAP39_gGy14vmn_Qtrw.png)
_Cliquez sur l'icône "⏏" pour activer Flash_

```
######### Données #########"""Les ensembles de données que j'ai utilisés proviennent de Zillow (logements moyens), du programme UCR du FBI, de census.gov (population), du Bureau of Labor (chômage). J'ai fait un peu de nettoyage et de jointure des données pour le format dont j'avais besoin dans cet article, et vous pouvez cliquer sur les liens ci-dessous pour les télécharger."""bubble_plot_merged_city_data.csv, motion_chart_merged_city_data.csv
```

Suivez-moi et donnez-moi quelques applaudissements si vous avez trouvé cela utile !

Vous pouvez également lire mes articles précédents sur la science des données, l'immobilier et la prise de décision :

[**Comment analyser la saisonnalité et les tendances pour économiser de l'argent sur votre bail d'appartement.**](https://medium.freecodecamp.org/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a)  
[_Lorsque je cherchais un nouvel appartement à louer, j'ai commencé à me demander : existe-t-il une stratégie de prise de décision basée sur les données..._medium.freecodecamp.org](https://medium.freecodecamp.org/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a)[**Comment utiliser les données pour prédire le loyer et optimiser la durée de votre bail afin d'économiser de l'argent**](https://medium.freecodecamp.org/https-medium-freecodecamp-org-how-to-predict-rent-and-select-the-best-lease-duration-to-save-money-5cf35145d398)  
[_Dans mon dernier article, nous avons parlé de la manière de choisir le meilleur mois pour signer le bail en fonction de la saisonnalité. Maintenant, combien de temps..._medium.freecodecamp.org](https://medium.freecodecamp.org/https-medium-freecodecamp-org-how-to-predict-rent-and-select-the-best-lease-duration-to-save-money-5cf35145d398)