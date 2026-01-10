---
title: Comment j'ai utilisé l'analyse de régression pour analyser l'espérance de vie
  avec Scikit-Learn et Statsmodels
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-19T17:25:29.000Z'
originalURL: https://freecodecamp.org/news/regression-analysis-on-life-expectancy
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/us-life-expectancy-drop.jpg
tags:
- name: Data Science
  slug: data-science
- name: Python
  slug: python
- name: '#Regression'
  slug: regression
seo_title: Comment j'ai utilisé l'analyse de régression pour analyser l'espérance
  de vie avec Scikit-Learn et Statsmodels
seo_desc: 'By Black Raven

  In this article, I will use some data related to life expectancy to evaluate the
  following models: Linear, Ridge, LASSO, and Polynomial Regression. So let''s jump
  right in.

  I was exploring the dengue trend in Singapore where there has b...'
---

Par Black Raven

Dans cet article, je vais utiliser des données liées à l'espérance de vie pour évaluer les modèles suivants : Linéaire, Ridge, LASSO et Régression Polynomiale. Alors, plongeons directement dans le sujet.

J'explorais la tendance de la dengue à Singapour où il y a eu une récente augmentation des cas de dengue – surtout dans la [Dengue Red Zone](https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters) où je vis. Cependant, les données brutes n'étaient pas disponibles sur le site web de la NEA.

Je me demandais, la dengue a-t-elle affecté l'espérance de vie des personnes dans un pays en particulier ? Les personnes dans les nations riches vivent-elles plus longtemps ? Quels sont les facteurs affectant l'espérance de vie d'un pays ?

J'ai donc exploré l'espérance de vie et recherché des données sur les aspects (caractéristiques) suivants :

* [Taux de Natalité](https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate)
* [Taux de Cancer](https://www.worldlifeexpectancy.com/cause-of-death/all-cancers/by-country/)
* [Cas de Dengue](https://en.wikipedia.org/wiki/Dengue_fever_outbreaks)
* Indice de Performance Environnementale ([EPI](https://epi.envirocenter.yale.edu/epi-topline))
* Produit Intérieur Brut ([PIB](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)))
* [Dépenses de Santé](https://en.wikipedia.org/wiki/List_of_countries_by_total_health_expenditure_per_capita)
* [Taux de Maladies Cardiaques](https://www.worldlifeexpectancy.com/cause-of-death/coronary-heart-disease/by-country/)
* [Population](https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2010)
* [Superficie](https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2010)
* [Densité de Population](https://en.wikipedia.org/wiki/List_of_countries_by_population_in_2010)
* [Taux d'AVC](https://www.worldlifeexpectancy.com/cause-of-death/stroke/by-country/)

La cible est l'[Espérance de Vie](https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy), mesurée en nombre d'années.

Les hypothèses sont :

1. Ce sont des moyennes au niveau des pays
2. Il n'y a pas de distinction entre hommes et femmes

Le code Python est disponible sur mon [GitHub](https://github.com/JNYH/Project-Luther).

## Processus de Science des Données

J'ai utilisé le processus suivant de science des données dans mon analyse :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-96.png)

* collecte de données, nettoyage de données, Analyse Exploratoire des Données
* sélection de caractéristiques, ingénierie de caractéristiques
* sélection de modèles, réglage de modèles et réglage des hyperparamètres
* optimisation de modèles basée sur la métrique de performance sélectionnée

Les outils utilisés pour cette analyse incluent :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-102.png)

* bibliothèques Python, particulièrement [Numpy](https://numpy.org/) et [Pandas](https://pandas.pydata.org/docs/) pour manipuler les structures de données
* [Matplotlib](https://matplotlib.org/) et [Seaborn](https://seaborn.pydata.org/) pour la visualisation
* [Scikit-Learn](https://scikit-learn.org/stable/index.html) et [Statsmodels](https://www.statsmodels.org/stable/index.html) pour l'analyse de régression

## Analyse Exploratoire des Données

Tout d'abord, je vérifie la multicolinéarité entre les caractéristiques.

```py
sns.set(rc={'figure.figsize':(10,7)})sns.heatmap(df.corr(), cmap="seismic", annot=True, vmin=-1, vmax=1)
```

Il semble y avoir une forte colinéarité, indiquée par des cases en rouge foncé et bleu foncé comme vous pouvez le voir dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-58.png)

Par exemple, les pays qui dépensent plus en soins de santé ont un score EPI plus élevé. Lorsque les dépenses de santé sont plus élevées, le taux d'AVC est également plus faible. Et une superficie plus grande donne une population plus élevée.

Qu'en est-il de la corrélation entre les caractéristiques et la cible ? Pour vivre longtemps, vous devriez avoir un faible taux d'AVC, des dépenses de santé élevées, prendre soin de l'environnement et avoir moins de bébés (selon le graphique de corrélation).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_vmjdEhjU0ScLQOxLvtFwMg.png)

Regardons le graphique initial des paires.

```py
sns.pairplot(df, height=1.5, aspect=1.5)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-64.png)

Il semble nécessaire de supprimer les valeurs aberrantes dans de nombreuses caractéristiques, par exemple, les cas de dengue, le PIB, la population, la superficie et la densité de population.

Chaque valeur aberrante est remplacée par la valeur la plus élevée suivante dans la colonne. Après avoir supprimé les valeurs aberrantes, les graphiques sont toujours asymétriques à droite (les points sont très concentrés sur le côté gauche). Cela suggère qu'une transformation pourrait être nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_eAXh2VpB3mLWV-V3ci3ggw.png)

Une autre façon de supprimer les valeurs aberrantes est d'utiliser la fonction LOG, qui aide à répartir les données concentrées à droite.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_9IfppnhjoGbLVuNd5arrNg.png)

# Sélection des Caractéristiques

Pour rechercher des caractéristiques significatives, j'ai supprimé une caractéristique à la fois pour voir son impact sur le modèle de régression simple. En regardant le score R², ces 3 caractéristiques (Taux de Natalité, EPI, Taux d'AVC) sont choisies, car le modèle sera adversely affecté sans elles.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-68.png)

Ensuite, j'ai supprimé les **valeurs aberrantes** et examiné les valeurs p sur **Statsmodels**. J'ai obtenu une caractéristique significative supplémentaire (Densité de Population). Lorsque la valeur p d'une caractéristique est inférieure à 0,05, elle est considérée comme une bonne caractéristique, car j'ai choisi 5 % comme niveau de signification.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-69.png)

Après cela, j'ai appliqué les fonctions **LOG** à toutes les caractéristiques et obtenu 4 caractéristiques significatives supplémentaires (PIB, Taux de Maladies Cardiaques, Population et Superficie).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-70.png)

J'ai également effectué d'autres transformations (Réciproque, Puissance 2, Racine Carrée) mais il n'y a pas eu d'amélioration supplémentaire.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-71.png)

Les caractéristiques peuvent également être sélectionnées en utilisant la fonction **LassoCV** dans **SkLearn**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-72.png)

Enfin, j'ai regardé à nouveau le graphique des paires avec toutes les caractéristiques significatives. Les graphiques de dispersion sont maintenant bien répartis avec certaines tendances claires.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-73.png)

# Sélection du Modèle

Je suis maintenant prêt à ajuster les modèles suivants sur l'ensemble de données d'entraînement :

* Régression [**Linéaire**](https://www.thebalancesmb.com/what-is-simple-linear-regression-2296697) (une ligne droite qui approxime la relation entre les variables dépendantes et la variable cible indépendante)
* Régression [**Ridge**](https://www.datacamp.com/community/tutorials/tutorial-ridge-lasso-elastic-net) (cela réduit la complexité du modèle tout en gardant tous les coefficients dans le modèle, connu sous le nom de pénalité L2)
* Régression [**LASSO**](https://www.datacamp.com/community/tutorials/tutorial-ridge-lasso-elastic-net) (Least Absolute Shrinkage and Selection Operator réduit la complexité du modèle en pénalisant les coefficients du modèle à zéro, par exemple, pénalité L1)
* Régression [**Polynomiale de Degré 2**](https://towardsdatascience.com/polynomial-regression-bbe8b9d97491) (une ligne courbe pour approximer la relation entre les variables dépendantes et la variable cible indépendante)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-74.png)

J'ai également validé leurs performances sur l'ensemble de données de validation. Le modèle de régression linéaire simple semble avoir le potentiel d'être le modèle le plus performant.

Cela est confirmé par **Validation Croisée** en utilisant **KFold** (avec 5 divisions).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-75.png)

Enfin, j'ai vérifié l'erreur résiduelle par rapport aux hypothèses. Les erreurs résiduelles doivent être normalement distribuées avec une variance égale autour de la moyenne zéro. Le graphique Normal Quartile-to-Quartile semble également acceptablement normal.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-76.png)

Étant donné que je n'ai que 250 lignes (données limitées par le nombre de pays dans le monde), j'ai utilisé l'ensemble de données complet pour simuler l'ensemble de données de test (note : cela est fait à des fins académiques, pas pratiques car cela conduirait à une [fuite de données](https://towardsdatascience.com/data-leakage-in-machine-learning-10bdd3eec742)). J'ai utilisé la **Validation Croisée KFold** avec 10 divisions pour évaluer la performance du modèle.

```py
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
kf = KFold(n_splits=5, shuffle=True, random_state = 1)
lm = LinearRegression()
lm.fit(X_train, y_train)
cvs_lm = cross_val_score(lm, X, y, cv=kf, scoring='r2')
print(cvs_lm)
```

Il y a une certaine variation dans les valeurs R² de 0,49 à 0,82, mais le résultat moyen est d'environ 0,69, ce qui est assez satisfaisant.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-77.png)

# Comment interpréter le modèle ?

```py
df = pd.read_csv('df3.csv')
X = df[ ['Birth Rate', 'EPI', 'GDP', 'Heart Disease Rate', 'Population', 'Area', 'Pop Density', 'Stroke Rate'] ].astype(float)
X = np.log(X)
y = df[ "Life Expectancy" ].astype(float)
X = sm.add_constant(X)

model = sm.OLS(y, X)
results = model.fit()
results.summary()
```

Si vous n'êtes pas affecté par les caractéristiques, votre espérance de vie est de 62 ans. Si votre pays a un faible taux de natalité, ajoutez 5 années supplémentaires à votre vie. **Si l'EPI (Indice de Performance Environnementale) est élevé, ajoutez 8 années supplémentaires à votre vie.** Si vous vivez dans un pays riche, ajoutez un demi-an à votre vie. Enfin, pour chaque unité (ou plutôt unité LOG) de diminution du taux d'AVC, 5 années supplémentaires pourraient être ajoutées à votre vie.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-78.png)

# Prochaines Étapes

Je pourrais éventuellement collecter plus de données en élargissant la portée aux villes au lieu des pays, et en explorant d'autres caractéristiques (facteurs) affectant l'espérance de vie. De plus, je pourrais diviser les données en catégories masculines et féminines pour une telle analyse de régression de l'espérance de vie.

Pour conclure, voici quelques insights intéressants :

1. Le Japon a l'espérance de vie la plus élevée (83,7 ans). La République centrafricaine (49,5 ans) et de nombreux pays du continent africain sont en bas de l'échelle. Singapour est classé #5 (82,7 ans).

**2. Prenez soin de l'environnement**. Cela a le plus grand coefficient (impact) sur l'espérance de vie d'un pays.

Le code Python pour l'analyse ci-dessus est disponible sur mon [GitHub](https://github.com/JNYH) – n'hésitez pas à vous y référer.

[https://github.com/JNYH/Project-Luther](https://github.com/JNYH/Project-Luther)

Présentation vidéo : [https://youtu.be/gC2m_lvouu8](https://youtu.be/gC2m_lvouu8)

Merci d'avoir lu.