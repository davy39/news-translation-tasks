---
title: Apprenez à sélectionner la meilleure régression linéaire pour les modèles univariés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-14T16:58:01.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-select-the-best-performing-linear-regression-for-univariate-models-e9d429c40581
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gx5KYR-ldeimGv-Qj-_khA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
- name: shiny
  slug: shiny
- name: statistics
  slug: statistics
seo_title: Apprenez à sélectionner la meilleure régression linéaire pour les modèles
  univariés
seo_desc: 'By Björn Hartmann

  Find out which linear regression model is the best fit for your data

  Inspired by a question after my previous article, I want to tackle an issue that
  often comes up after trying different linear models: You need to make a choice whi...'
---

Par Björn Hartmann

#### Découvrez quel modèle de régression linéaire est le plus adapté à vos données

Inspiré par une question après mon [article précédent](https://medium.freecodecamp.org/learn-how-to-improve-your-linear-models-8294bfa8a731), je souhaite aborder un problème qui survient souvent après avoir essayé différents modèles linéaires : vous devez choisir quel modèle utiliser. Plus précisément, [Khalifa Ardi Sidqi](https://www.freecodecamp.org/news/learn-how-to-select-the-best-performing-linear-regression-for-univariate-models-e9d429c40581/undefined) a demandé :

> « Comment déterminer quel modèle convient le mieux à mes données ? Dois-je simplement regarder le R carré, SSE, etc. ?

> Comme l'interprétation de ce modèle (quadratique, racine, etc.) sera très différente, cela ne posera-t-il pas un problème ? »

La deuxième partie de la question peut être répondue facilement. Tout d'abord, trouvez un modèle qui convient le mieux à vos données, puis interprétez ses résultats. Il est bon d'avoir des idées sur la manière dont vos données pourraient être expliquées. Cependant, interprétez uniquement le meilleur modèle.

Le reste de cet article abordera la première partie de sa question. Veuillez noter que je vais partager **mon approche** sur la manière de sélectionner un modèle. Il existe plusieurs méthodes, et d'autres pourraient procéder différemment. Mais je vais décrire la méthode qui fonctionne le mieux pour moi.

De plus, **cette approche ne s'applique qu'aux modèles univariés**. Les modèles univariés n'ont qu'une seule variable d'entrée. Je prévois un autre article où je vous montrerai comment évaluer les modèles multivariés avec plusieurs variables d'entrée. Pour aujourd'hui, cependant, concentrons-nous sur les bases et les modèles univariés.

Pour pratiquer et vous familiariser avec cela, j'ai écrit une petite application Shiny. Utilisez-la et jouez avec différents ensembles de données et modèles. Observez comment les paramètres changent et devenez plus confiant dans l'évaluation des modèles linéaires simples. Enfin, vous pouvez également utiliser l'application comme cadre pour vos données. Il suffit de [la copier depuis GitHub](https://github.com/bjoernhartmann/linear_model_selection).

![Image](https://cdn-media-1.freecodecamp.org/images/nUC1EEWV9sMPADDjWSEeGTwN3CYdHRASXHsy)
_Cliquez sur l'image pour une version interactive_

### Utilisez le R2 ajusté pour les modèles univariés

Si vous n'utilisez qu'une seule variable d'entrée, la valeur `R2 ajusté` vous donne une bonne indication de la performance de votre modèle. Elle illustre combien de variation est expliquée par votre modèle.

Contrairement au simple `R2`, le `R2 ajusté` prend en compte le nombre de facteurs d'entrée. Il pénalise trop de facteurs d'entrée et favorise les modèles parcimonieux.

Dans la capture d'écran ci-dessus, vous pouvez voir deux modèles avec des valeurs de 71,3 % et 84,32 %. Apparemment, le deuxième modèle est meilleur que le premier. Cependant, les modèles avec des valeurs faibles peuvent encore être utiles car le `R2 ajusté` est sensible à la quantité de bruit dans vos données. Ainsi, ne comparez cet indicateur de modèles que pour **le même** ensemble de données plutôt que de le comparer entre différents ensembles de données.

#### Habituellement, il y a peu besoin du SSE

Avant de continuer, assurons-nous que nous parlons du même SSE. Sur [Wikipedia](https://en.wikipedia.org/wiki/Residual_sum_of_squares), SSE fait référence à la somme des erreurs au carré. Dans certains [manuels de statistiques](https://www.amazon.de/Introductory-Econometrics-International-Jeffrey-Wooldridge/dp/111153439X/ref=sr_1_1?ie=UTF8&qid=1510003022&sr=8-1&keywords=wooldridge+econometrics&dpID=51mK3jyvZ6L&preST=_SX198_BO1,204,203,200_QL40_&dpSrc=srch), cependant, SSE peut faire référence à la somme expliquée des carrés (l'exact opposé). Donc pour l'instant, supposons que SSE fait référence à la somme des erreurs au carré.

Ainsi, le `R2 ajusté` est approximativement `1` — SSE/SST. Avec SST faisant référence à la somme totale des carrés.

Je ne veux pas approfondir les mathématiques derrière cela. Ce que je veux vous montrer, c'est que **le `R2 ajusté` est calculé avec le SSE**. Donc **le SSE ne vous donne généralement aucune information supplémentaire**.

De plus, le `R2 ajusté` est normalisé de sorte qu'il est toujours compris entre zéro et un. Il est donc plus facile pour vous et les autres d'interpréter un modèle inconnu avec un `R2 ajusté` de 75 % plutôt qu'un SSE de 394 — même si les deux chiffres pourraient expliquer le même modèle.

### Jetez un coup d'œil aux résidus ou termes d'erreur !

Ce qui est souvent ignoré, ce sont les termes d'erreur ou les soi-disant résidus. Ils vous en disent souvent plus que ce que vous pourriez penser.

#### Les résidus sont la différence entre vos valeurs prédites et les valeurs réelles.

Leur avantage est qu'ils peuvent vous montrer à la fois l'ampleur ainsi que la direction de vos erreurs. Regardons un **exemple** :

![Image](https://cdn-media-1.freecodecamp.org/images/O65pTa4puX04M4lZvAh3C3czxmF-97ch1vMk)
_Nous ne voulons pas que les résidus varient ainsi autour de zéro_

Ici, j'ai essayé de prédire un ensemble de données polynomial avec une fonction linéaire. L'analyse des résidus montre qu'il y a des zones où le modèle a un biais vers le haut ou vers le bas.

Pour `50 < x < 100`, les résidus sont au-dessus de zéro. Donc dans cette zone, les valeurs réelles ont été plus élevées que les valeurs prédites — notre modèle a un biais vers le bas.

Pour `100 < x < 150`, cependant, les résidus sont en dessous de zéro. Ainsi, les valeurs réelles ont été plus basses que les valeurs prédites — le modèle a un biais vers le haut.

Il est toujours bon de savoir si votre modèle suggère des valeurs trop élevées ou trop basses. Mais généralement, vous ne voulez pas avoir de motifs comme celui-ci.

Les résidus doivent être nuls en moyenne (comme l'indique la moyenne) et ils doivent être également distribués. La prédiction du même ensemble de données avec une fonction polynomiale de `3 degrés` suggère un meilleur ajustement :

![Image](https://cdn-media-1.freecodecamp.org/images/ypW4KJac5RK6BHt4FiDIP9hMjwtrDVV0soGA)
_Ici, les résidus sont également distribués autour de zéro. Suggérant un meilleur ajustement_

De plus, vous pouvez observer si la variance de vos erreurs augmente. En statistiques, cela s'appelle [Hétéroscédasticité](https://en.wikipedia.org/wiki/Heteroscedasticity). Vous pouvez corriger cela facilement avec des [erreurs standard robustes](https://en.wikipedia.org/wiki/Heteroscedasticity-consistent_standard_errors). Sinon, vos tests d'hypothèses sont susceptibles d'être erronés.

### Histogramme des résidus

Enfin, l'histogramme résume l'ampleur de vos termes d'erreur. Il fournit des informations sur la bande passante des erreurs et indique la fréquence à laquelle chaque erreur s'est produite.

![Image](https://cdn-media-1.freecodecamp.org/images/HPdK2U6tSrGaR2fTp9mtZ-1SNeE7W2oRRewr)

![Image](https://cdn-media-1.freecodecamp.org/images/OPHfIqkkwvAuXY5LPR5a5wrfTnf3f2nYL3Y6)
_L'histogramme de droite indique une bande passante d'erreurs plus petite que celui de gauche. Il semble donc être un meilleur ajustement._

Les captures d'écran ci-dessus montrent deux modèles pour le même ensemble de données. Dans l'histogramme de **gauche**, les erreurs se produisent dans une plage de `-338` et `520`.

Dans l'histogramme de **droite**, les erreurs se produisent entre `-293` et `401`. Les valeurs aberrantes sont donc beaucoup plus basses. De plus, la plupart des erreurs dans le modèle de l'histogramme de droite sont plus proches de zéro. Je favoriserais donc le modèle de droite.

### Résumé

Lors du choix d'un modèle linéaire, voici les facteurs à garder à l'esprit :

* Ne comparez les modèles linéaires que pour le même ensemble de données.
* Trouvez un modèle avec un R2 ajusté élevé
* Assurez-vous que ce modèle a des résidus également distribués autour de zéro
* Assurez-vous que les erreurs de ce modèle sont dans une petite bande passante

![Image](https://cdn-media-1.freecodecamp.org/images/JS9yNfP14mUpaltgMLaM-RbKxC7s3OLmoJMC)
_Cliquez sur l'image pour ouvrir l'application_

![Image](https://cdn-media-1.freecodecamp.org/images/g41iHB7GOtG4cyp4QU1Ntwkzh2Vyk5K7p7lU)

Si vous avez des questions, écrivez un commentaire ci-dessous ou [contactez-moi](https://bjoern-hartmann.de). J'apprécie vos retours.