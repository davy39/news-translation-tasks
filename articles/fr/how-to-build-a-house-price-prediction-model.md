---
title: Comment construire un modèle de prédiction des prix de l'immobilier – Explication
  de la régression linéaire
subtitle: ''
author: Oluwadamisi Samuel
co_authors: []
series: null
date: '2024-02-29T13:25:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-house-price-prediction-model
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Final-House-Price-Cover.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment construire un modèle de prédiction des prix de l'immobilier – Explication
  de la régression linéaire
seo_desc: 'Ever wondered how algorithms predict future house prices, stock market
  trends, or even your next movie preference? The answer lies in a fundamental yet
  powerful tool called linear regression.

  Don''t be fooled by its seemingly simple equation – this ar...'
---

Vous vous êtes déjà demandé comment les algorithmes prédisent les prix futurs des maisons, les tendances du marché boursier, ou même vos préférences de films ? La réponse réside dans un outil fondamental mais puissant appelé régression linéaire.

Ne vous laissez pas tromper par son équation apparemment simple – cet article révélra sa magie, vous donnant les moyens de construire et de comprendre ces modèles, que vous soyez un novice en apprentissage automatique ou un expert chevronné ayant besoin d'un rappel.

Dans cet article, vous obtiendrez des explications cristallines, des conseils pratiques et des applications réelles où vous witnesserez la puissance de la régression linéaire en action.

Alors, attachez votre ceinture et préparez-vous à conquérir le chemin droit et étroit de la régression linéaire ! À la fin de ce guide complet, vous serez équipé pour construire, interpréter et exploiter ces modèles en toute confiance pour vos propres entreprises basées sur les données.

## Table des matières

1. [Prérequis](#heading-prerequisites)
    
2. [Qu'est-ce que la régression linéaire ?](#heading-quest-ce-que-la-regression-lineaire)
    
3. [Pourquoi la régression linéaire est-elle précieuse ?](#heading-pourquoi-la-regression-lineaire-est-elle-precieuse)
    
4. [Concepts clés de la régression linéaire](#heading-concepts-cles-de-la-regression-lineaire)
    
5. [Comment construire votre premier modèle](#heading-comment-construire-votre-premier-modele)
    
6. [Techniques avancées de régression linéaire](#heading-techniques-avancees-de-regression-lineaire)
    
7. [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir installé ce qui suit :

* Python (3.x recommandé)
    
* Jupyter Notebook : ceci est optionnel mais recommandé pour un environnement interactif et aussi pour l'essai et l'erreur (les débutants bénéficieront le plus de cela)
    
* Bibliothèques requises : pandas, NumPy, Matplotlib, seaborn, scikit-learn
    

Vous pouvez installer ces bibliothèques en utilisant `pip install` dans la ligne de commande :

```py
pip install pandas
pip install matplotlib
pip install numpy
pip install seaborn
pip install scikit-learn
```

## Qu'est-ce que la régression linéaire ?

En termes simples, la régression linéaire exploite la puissance des lignes droites.

Imaginez que vous êtes un agent immobilier essayant de prédire le prix d'une maison. Vous pourriez considérer divers facteurs comme sa taille, son emplacement, son âge et le nombre de chambres.

La régression linéaire intervient comme un outil puissant pour analyser ces facteurs et révéler les relations sous-jacentes. C'est une technique statistique puissante qui nous permet d'examiner la relation entre une ou plusieurs variables "indépendantes" et une variable "dépendante".

Dans un ensemble de données sur les prix des maisons, les variables indépendantes sont les colonnes utilisées pour prédire, telles que la "Surface", le "Nombre de chambres", l'"Âge" et l'"Emplacement". La variable dépendante sera la colonne "Prix" – la caractéristique à prédire.

La régression linéaire est la forme la plus simple de régression, supposant une relation linéaire (ligne droite) entre la variable d'entrée et la variable de sortie. L'équation pour la régression linéaire simple peut s'exprimer comme `y = mx + b`, où `y` est la variable dépendante, `x` est la variable indépendante, `m` est la pente et `b` est l'ordonnée à l'origine.

Cela crée une ligne de meilleur ajustement, mais ne vous inquiétez pas trop des mathématiques sous-jacentes. Cependant, c'est important au fur et à mesure que vous avancez dans votre parcours d'apprentissage automatique.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Linear-regression-image.png align="left")

*Graphique de régression linéaire simple*

## Pourquoi la régression linéaire est-elle précieuse ?

* **Interprétabilité :** Contrairement à certains modèles complexes, la régression linéaire fournit des informations claires sur la manière dont chaque caractéristique influence la variable cible. Vous pouvez facilement voir quelles caractéristiques ont le plus fort impact et comment elles contribuent à la prédiction globale.
    
* **Base pour les modèles complexes :** Lorsqu'ils traitent des problèmes plus complexes, les scientifiques des données commencent souvent par la régression linéaire comme modèle de base. Ce modèle simple sert de point de référence pour comparer les performances d'algorithmes plus complexes. Si un modèle complexe n'offre pas de résultats significativement meilleurs que la régression linéaire, il pourrait surajuster inutilement les données.
    
* **Facilité de mise en œuvre :** Comparée à d'autres algorithmes d'apprentissage automatique, la régression linéaire est relativement facile à mettre en œuvre et à comprendre. Cela en fait un excellent point de départ pour les débutants s'aventurant dans le monde de l'apprentissage automatique.
    

Rappelez-vous, la régression linéaire pourrait ne pas être la solution ultime pour chaque problème, mais elle offre une base puissante pour comprendre les données, construire des prédictions et préparer le terrain pour explorer des modèles plus complexes.

Plongeons plus profondément dans les mécanismes de construction et d'interprétation des modèles de régression linéaire.

## Concepts clés de la régression linéaire

Prêt à plonger plus profondément dans les mécanismes de la régression linéaire ? Ne vous inquiétez pas, même sans un doctorat en mathématiques, nous pouvons déverrouiller ses secrets ensemble sans nous enliser dans les termes compliqués.

Que se passe-t-il lorsque vous créez un modèle de régression linéaire ?

* **Trouver la meilleure ligne d'ajustement :** Des lignes sont tracées sur un graphique, avec les caractéristiques sur un axe et les prix sur l'autre. La ligne que nous cherchons est celle qui `s'ajuste le mieux` aux points représentant de vraies maisons, minimisant la différence globale entre les prix prédits et réels.
    
* **Minimiser l'erreur :** Imaginez la ligne comme un `acte d'équilibre`. La pente et la position de la ligne sont ajustées jusqu'à ce que la distance totale entre la ligne et les points de données soit aussi petite que possible (Fonction de coût minimisée). Cette distance minimisée reflète la meilleure prédiction possible pour de nouvelles maisons en fonction de leurs caractéristiques.
    
* **Coefficients :** Chaque caractéristique du modèle obtient un `poids` (Coefficients), comme une quantité spécifique d'un ingrédient dans une recette. En ajustant ces poids, nous changeons la contribution de chaque caractéristique au prix prédit. Un poids plus élevé pour la taille, par exemple, signifie que les maisons plus grandes ont tendance à avoir une influence plus forte sur le prix prédit.
    

Alors, que retirons-nous de cela ?

Une fois que nous avons la ligne de meilleur ajustement, le modèle peut prédire le prix de nouvelles maisons en fonction de leurs caractéristiques. Mais ce n'est pas seulement une question de chiffres – `les poids racontent une histoire`.

Ils révèlent combien, en moyenne, chaque caractéristique change le prix prédit. Un poids positif pour les chambres signifie que, généralement, les maisons avec plus de chambres sont prédites comme étant plus chères.

### Hypothèses et limitations

La régression linéaire suppose que les choses sont globalement simples, comme la relation entre la taille et le prix. Si les choses sont plus complexes, elle pourrait ne pas être le meilleur outil.

Mais c'est un excellent point de départ car elle est facile à comprendre et à interpréter, ce qui en fait un outil précieux pour explorer le monde de la prédiction de données.

Cependant, vous n'avez pas à vous soucier de trouver manuellement la meilleure ligne d'ajustement. L'algorithme choisit la meilleure ligne d'ajustement lors de la création du modèle.

Dans la section suivante, vous apprendrez comment construire votre tout premier modèle de prédiction des prix de l'immobilier.

## Comment construire votre premier modèle

### Comment importer des bibliothèques et charger des données

Si vous êtes nouveau dans les modèles d'apprentissage automatique, les bibliothèques sont importées sous forme d'abréviations dans le seul but d'écrire un code plus court :

```py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Chargez votre ensemble de données (remplacez 'votre_ensemble_de_donnees.csv' par votre fichier)
df = pd.read_csv('votre_ensemble_de_donnees.csv')

# Affichez les premières lignes de l'ensemble de données
df.head()
```

L'ensemble de données est chargé en utilisant la fonction `read_csv` de pandas, puis les cinq premières lignes sont affichées en utilisant `df.head()`.

### Analyse exploratoire des données (EDA)

Les données provenant de différentes sources sont généralement désordonnées, dispersées, elles contiennent des valeurs manquantes et sont parfois non structurées.

Avant de construire un modèle de régression, il est crucial de comprendre les données, et de les nettoyer et les optimiser pour obtenir le meilleur résultat. Pour une explication approfondie, consultez cet article sur le [nettoyage et le prétraitement des données](https://www.freecodecamp.org/news/data-cleaning-and-preprocessing-with-pandasbdvhj/).

Passons en revue les étapes que vous devez suivre avant de construire votre modèle.

#### Vérifier les valeurs manquantes

Les modèles d'apprentissage automatique ne peuvent pas fonctionner lorsqu'il y a des valeurs manquantes dans l'ensemble de données :

```py
df.isnull().sum()
```

Cela vous donnera une liste des colonnes qui ont des valeurs nulles et les lignes elles-mêmes. Il existe différentes façons de traiter cela, telles que :

* Supprimer toutes les lignes avec des valeurs nulles.
    
* Utiliser la moyenne ou la médiane de la colonne pour remplir les valeurs manquantes pour les données numériques.
    
* Remplir les valeurs manquantes avec les données les plus fréquentes pour les données qualitatives.
    

#### Explorer la corrélation entre les variables

```py
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
```

Ce code montrera les relations entre les colonnes des variables indépendantes / variables / caractéristiques, et les variables dépendantes / variables cibles.

Il montrera également quelles colonnes ou caractéristiques déterminent le plus le résultat de la variable cible.

#### Visualiser la relation entre les variables indépendantes et dépendantes

Les graphiques de dispersion peuvent montrer à quel point vos prix prédits s'alignent avec les valeurs réelles. Les graphiques de résidus aident à visualiser les motifs dans les erreurs, révélant les problèmes potentiels.

```py
sns.scatterplot(x='Variable Indépendante', y='Variable Dépendante', data=df)
plt.show()
```

Ce graphique de dispersion montre la relation entre les variables indépendantes et dépendantes et une ligne droite est tracée pour montrer la relation.

### Prétraitement des données

Il s'agit d'une étape cruciale car la qualité des données utilisées pour entraîner le modèle détermine également la précision et l'efficacité du modèle.

Ici, l'ensemble de données est d'abord séparé en X (variable(s) indépendante(s) / caractéristiques) et Y (variable dépendante / Cible) :

```py

# Traiter les valeurs manquantes si nécessaire
df.dropna(inplace=True)

# Diviser les données en caractéristiques (X) et variable cible (y)
X = df[['Variable Indépendante']]
y = df['Variable Dépendante']

# Diviser les données en ensembles d'entraînement et de test (par exemple, 80 % d'entraînement, 20 % de test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Nous traitons les valeurs manquantes en supprimant les colonnes avec des valeurs manquantes / nulles et divisons l'ensemble de données en entraînement et test dans un rapport de 80:20.

### Construction du modèle de régression

Enfin, il est temps de créer et d'entraîner notre modèle de régression linéaire.

Nous créons un modèle en appelant une instance du modèle dans une variable comme montré ci-dessous et nous entraînons le modèle en ajustant l'ensemble de données d'entraînement dans le modèle.

```py
# Créer un modèle de régression linéaire
model = LinearRegression()

# Entraîner le modèle
model.fit(X_train, y_train)
```

### Comment faire des prédictions

Le modèle entraîné est utilisé pour faire des prédictions sur l'ensemble de test. Les prédictions peuvent être faites sur l'ensemble de la colonne de caractéristiques comme montré ci-dessous ou chaque colonne peut être prédite individuellement.

```py
# Faire des prédictions
y_predn = model.predict(X_test)
```

### Comment évaluer le modèle

Évaluer la performance du modèle est une étape importante pour déterminer la précision du modèle et sa réutilisabilité. Nous pouvons vérifier en utilisant des métriques telles que :

* "R-carré" : Cela vous indique à quel point le modèle explique la variation des prix des maisons. Une valeur plus élevée (plus proche de 1) indique un meilleur ajustement.
    
* Erreur quadratique moyenne (MSE) : Cela mesure la différence moyenne entre les prix prédits et réels. Plus c'est bas, mieux c'est.
    
* Score de précision.
    

```py
# Évaluer le modèle
mse = mean_squared_error(y_test, y_pred)
print(f'Erreur quadratique moyenne : {mse}')

# Utiliser le score de précision
model.score(X_test, Y_test)
```

### Comment visualiser les résultats

Visualiser la ligne de régression et les valeurs réelles par rapport aux valeurs prédites :

```py
# Tracer la ligne de régression
plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.xlabel('Variable Indépendante')
plt.ylabel('Variable Dépendante')
plt.show()
```

Considérons un scénario différent où vous voulez flexibiliser vos muscles et prédire le score d'un étudiant (y) en fonction du nombre d'heures qu'il a étudiées (x). Le modèle de régression linéaire pourrait ressembler à ceci :

```py
import numpy as np
from sklearn.linear_model import LinearRegression

# Données d'exemple
heures_etudiees = np.array([2, 4, 6, 8, 10])
scores = np.array([60, 80, 90, 100, 95])

# Redimensionner les données
heures_etudiees = heures_etudiees.reshape(-1, 1)

# Créer un modèle de régression linéaire
model = LinearRegression()

# Ajuster le modèle
model.fit(heures_etudiees, scores)

# Faire des prédictions
predicted_scores = model.predict(heures_etudiees)

the model model.fit(heures_etudiees, scores) # Faire des prédictions predicted_scores = model.predict(heures_etudiees)
```

## Techniques avancées de régression linéaire

Vous avez conquis les bases de la régression linéaire, mais le voyage continue !

Explorons des techniques avancées pour déverrouiller encore plus de puissance et affiner vos modèles.

### Dompter le surajustement – Régularisation

Imaginez un gâteau recouvert de glaçage – impressionnant, mais impraticable.

De même, un modèle avec trop de caractéristiques peut "surajuster" les données d'entraînement, perdant sa capacité à généraliser. Les techniques de régularisation agissent comme des assaisonnements, empêchant cette catastrophe culinaire :

* **L1 (Lasso) :** Réduit certains coefficients à zéro, supprimant effectivement les caractéristiques non importantes.
    
* **L2 (Ridge) :** Réduit tous les coefficients, les empêchant de devenir trop grands.
    

Ces techniques pénalisent les modèles complexes, les poussant vers des solutions plus simples qui généralisent mieux les nouvelles données.

### Ingénierie des caractéristiques – Découvrir des pépites cachées

Toutes les caractéristiques ne sont pas créées égales. Certaines peuvent être redondantes, tandis que d'autres cachent des relations précieuses. L'ingénierie des caractéristiques implique :

* **Sélection :** Identifier les caractéristiques les plus informatives en utilisant l'analyse de corrélation ou des tests statistiques.
    
* **Transformation :** Créer de nouvelles caractéristiques en combinant celles existantes (par exemple, multiplier la superficie et le nombre de chambres pour obtenir la surface habitable totale). Cela vous permet de capturer des relations non linéaires au-delà des capacités du modèle linéaire.
    

En sélectionnant et en transformant soigneusement les caractéristiques, vous pouvez considérablement améliorer les performances de votre modèle.

### Quandaries catégoriques – Encodage et au-delà

Le monde n'est pas toujours en noir et blanc. Que faire des caractéristiques comme "ville" ou "type de propriété" ? Ces variables catégorielles nécessitent un traitement spécial :

* **Encodage one-hot :** Crée des caractéristiques binaires séparées pour chaque catégorie, permettant au modèle d'apprendre leur impact individuel.
    
* **Caractéristiques polynomiales :** Crée de nouvelles caractéristiques en interagissant avec les catégories (par exemple, "ville * type de propriété"), capturant des relations complexes.
    

Comprendre comment gérer les caractéristiques catégorielles déverrouille des informations précieuses à partir de vos données. Consultez [cet article](https://www.freecodecamp.org/news/data-cleaning-and-preprocessing-with-pandasbdvhj/) pour une plongée en profondeur sur la façon de gérer les caractéristiques catégorielles.

### Sélection du modèle – Comment choisir votre champion

Avec cet arsenal de techniques, vous pourriez avoir plusieurs modèles. Comment choisir le meilleur ? Considérez :

* **Complexité :** Les modèles plus simples sont généralement préférés, car ils sont moins sujets au surajustement.
    
* **Performance :** Des métriques comme le R-carré et la validation croisée aident à comparer les modèles de manière objective.
    

Trouver le bon équilibre entre complexité et performance est crucial pour construire des modèles efficaces et généralisables.

Rappelez-vous ! Maîtriser la régression linéaire est un voyage continu. Expérimentez, explorez ces techniques avancées et n'ayez pas peur d'être créatif ! Avec la pratique et la curiosité, vous déverrouillerez le vrai potentiel de cet outil puissant et extrairez des informations précieuses de vos données.

Pour une exploration plus approfondie, consultez la documentation :

* [Documentation Scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
    
* [Tutoriels TensorFlow](https://www.tensorflow.org/tutorials)
    

## Conclusion

Cette exploration de la régression linéaire vous a équipé d'une compréhension robuste de ses concepts de base, du processus de construction de modèles et de ses limitations.

Rappelez-vous, ceci n'est que la fondation. Au fur et à mesure que vous vous aventurez plus profondément, vous rencontrerez des techniques avancées comme la régularisation, l'ingénierie des caractéristiques et la gestion des caractéristiques catégorielles, déverrouillant un pouvoir prédictif encore plus grand.

Embrassez l'esprit d'exploration. Expérimentez, plongez dans les ressources fournies et rappelez-vous que maîtriser la régression linéaire est un voyage continu. Chaque défi surmonté, chaque modèle construit, renforce votre capacité à extraire des informations précieuses des données.

Alors, continuez à apprendre, continuez à construire et déverrouillez le vrai potentiel de cet outil puissant.

Si vous avez trouvé cela utile, connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/samuel-oluwadamisi-01b3a4236?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BnrPfyUsJSmq9apFzoA%2BHuw%3D%3D).