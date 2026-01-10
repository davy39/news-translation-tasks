---
title: Comment prédire les loyers et optimiser la durée de votre bail pour économiser
  de l'argent
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-11T01:45:26.000Z'
originalURL: https://freecodecamp.org/news/https-medium-freecodecamp-org-how-to-predict-rent-and-select-the-best-lease-duration-to-save-money-5cf35145d398
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XkBmEX4MUwXSb8eo98TsXg.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Real Estate
  slug: real-estate
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment prédire les loyers et optimiser la durée de votre bail pour économiser
  de l'argent
seo_desc: 'By Zhen Liu

  In my last post, we talked about how to pick the best month to sign the lease based
  on seasonality. Now, how long should you sign the lease for when facing different
  options like 12-month, 15-month, 18-month or longer? Is there any strate...'
---

Par Zhen Liu

Dans mon [dernier article](https://medium.freecodecamp.org/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a), nous avons parlé de la manière de choisir le meilleur mois pour signer le bail en fonction de la saisonnalité. Maintenant, combien de temps devriez-vous signer le bail lorsque vous êtes confronté à différentes options comme 12 mois, 15 mois, 18 mois ou plus ? Existe-t-il une stratégie pour sélectionner la meilleure option afin d'économiser de l'argent ?

Pour analyser cela, j'ai modélisé les données de loyers de 353 villes provenantes de [Zillow](https://www.zillow.com/research/data/#other-metrics) (données au niveau de la ville pour les appartements d'une chambre). Dans cet article, je vais vous montrer comment faire des prédictions de séries temporelles, et quelles villes devraient voir leurs loyers augmenter le plus !

#### Tout d'abord, comment la durée du bail vous aide-t-elle à économiser de l'argent ?

Comme le montre ci-dessous, vous pouvez économiser de l'argent en signant un bail plus long si vous prédisez que le loyer va augmenter dans votre ville. Si le loyer mensuel augmente de 100 $ l'année prochaine, vous économiserez 1 200 $ en signant un bail de 2 ans, puis en le renouvelant année par année.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7bY_4ic8FMaImPsaRZz8Sg.png)

#### Comment prédire si le loyer va augmenter ?

Nous avons observé que le loyer est une série temporelle additive avec une combinaison de saisonnalité, de tendance et de bruit aléatoire.

Modèle additif : Y(t) = Saisonnalité(t) + Tendance(t) + Aléatoire(t)

Nous pouvons décomposer une série temporelle en utilisant la fonction `stl()` de R (stl signifie "décomposition saisonnière et de tendance utilisant le lissage par scatterplot pondéré localement").

```
# Décomposer la série temporelle additive
decomposed_rent <- stl(rent.series, s.window="periodic") # periodic signifie que le facteur de saisonnalité est le même pour chaque année
```

```
# Extraire les composants de la série temporellesaisonnalité   <- decomposed_rent$time.series[,1]tendance	   <- decomposed_rent$time.series[,2]aléatoire     <- decomposed_rent$time.series[,3]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*pOSifCkvyN2LLvesF_A8sg.png)
_Le graphique de la série temporelle décomposée du loyer a vérifié que les composants sont additifs, où loyer = Saisonnalité + Tendance + Aléatoire_

Vous pouvez simplement appliquer la fonction `stl()` dans R sur le format de série temporelle des données de loyer pour prédire le loyer des deux prochaines années.

```
# Prédire le loyer pour les 24 prochains mois avec un intervalle de confiance de 95%
fore_rent <- stlf(rent.series, s.window="period", h=24, level = 95)
```

#### Quelles villes ont une augmentation prédite du loyer ?

_*Comment lire les graphiques : La zone en **bande verte claire** après 2018 est l'intervalle de confiance de 95 % de la prédiction du loyer. Le **texte en violet** vous indique combien vous pouvez économiser si vous signez un bail de 2 ans contre 1 an, selon la zone rectangulaire violette délimitée. J'ai utilisé `ggplot2` pour tous les graphiques._

### 1. Zone de la Baie

![Image](https://cdn-media-1.freecodecamp.org/images/1*xx2OynsXjT9euYGLOzCNRQ.png)

L'augmentation mensuelle prédite du loyer à Sunnyvale est la plus grande parmi les 246 villes que j'ai analysées, soit 165 $ (en comparant le loyer de 2018-01 à celui prédit pour 2019-01). Ainsi, signer un bail de 2 ans en janvier 2018 peut vous faire économiser 165*12 = **1 980 $** la deuxième année ; signer un bail de 18 mois peut vous faire économiser 165*6 = **990 $**. Étant donné l'effet de saisonnalité à Sunnyvale, vous devriez également essayer d'éviter de renouveler le bail autour du mois de juillet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ks6lXmPRK_jsaQk00T7DJg.png)

### 2. Denver

![Image](https://cdn-media-1.freecodecamp.org/images/1*gLXQKu8gp8aOfSApU5_mwA.png)

### 3. Sud de la Californie

![Image](https://cdn-media-1.freecodecamp.org/images/1*T7QFELfN2wQSe_ghzijkYg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*m0gtYNI_qtSWXpZshROYJA.png)

### 4. Zone de Seattle

![Image](https://cdn-media-1.freecodecamp.org/images/1*pL4yYcZbfdXY3PiyrKdhdQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*2CgkcLhr-MrvsitBFP3DiQ.png)

### 5. Floride

![Image](https://cdn-media-1.freecodecamp.org/images/1*wsEj6o6zivPOBleX_rbD4w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZxAlZ9_lZQfQ88_Vma1qLw.png)

### 6. Texas

![Image](https://cdn-media-1.freecodecamp.org/images/1*kzDwYdn4AjTvjFAd66USoQ.png)

Pour les 11 villes mentionnées ci-dessus, si un bail de 2 ans n'est pas une option, 18 mois peuvent encore permettre d'économiser beaucoup par rapport à un loyer annuel en augmentation.

Quelles autres villes montrent une forte hausse des loyers ? J'ai tracé un total de 20 villes (y compris les villes mentionnées ci-dessus) pour vous montrer une comparaison des loyers ainsi que l'augmentation des loyers parmi plus de villes.

La **longueur du segment de ligne** de chaque ville représente l'augmentation du loyer, où le point rouge est le loyer en 2018-01 et le point vert est le loyer prédit pour 2019-01.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZfRNJEjyDvOiPfxWatzEsw.png)

D'après le graphique ci-dessus, les loyers de Lakewood (Denver Metro dans le CO) et d'El Cajon (San Diego Metro dans le CA) ne sont pas très élevés parmi les 20 villes, mais le "pas" d'augmentation est plus grand par rapport à d'autres villes avec une fourchette de loyer similaire.

Les villes avec un loyer > 2000 $ et une augmentation significative prédite sont toutes en Californie (Top 4 du graphique). Le loyer y est déjà élevé, et ils deviennent encore plus chers, plus rapidement.

Parmi les 20 premières, il y a 8 villes en Californie, 6 en Floride, 2 dans l'État de Washington, 2 au Texas, 1 à New York et 1 dans le Colorado.

#### Y a-t-il des villes qui ne montrent pas beaucoup de tendance en matière de loyer ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*HPApNP5vlsnuecn8ldeukQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mcw3q3DVsto1ZhDBLbW4tQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*v1rbNlgNjuLOPv1uJ6I6Bg.png)

Pour les villes mentionnées ci-dessus, il n'y a pas d'augmentation prédite. Donc pour les villes avec un effet de saisonnalité très significatif comme Boston et Wilmington, cela n'a pas vraiment d'importance **combien de temps** vous signez le bail ; mais **quel mois** vous le signez.

Le mois avec le loyer le plus élevé à Boston est novembre, tandis qu'à Wilmington, c'est avril.

Si vous êtes curieux de savoir quelles sont les autres villes comme celles-ci, lisez mon [dernier article](https://medium.freecodecamp.org/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a) pour en savoir plus sur les villes avec saisonnalité !

_Trouvez le code R pour les modèles de séries temporelles et la visualisation avec ggplot2 [ici](https://github.com/zhendata/Medium_Posts/blob/master/Rent%20Prediction_zhendata.R)._

Donnez-moi quelques applaudissements et suivez-moi ici si vous trouvez cela utile !