---
title: Comment analyser la saisonnalité et les tendances des loyers pour économiser
  sur votre bail
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-29T10:04:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ltPh1YrsG8dK9VnnM9-rzg.png
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Real Estate
  slug: real-estate
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment analyser la saisonnalité et les tendances des loyers pour économiser
  sur votre bail
seo_desc: 'By Zhen Liu

  When I was looking for a new apartment to rent, I started to wonder: is there any
  seasonality impact? Is there a month when the rent is lowest so I can save money
  when I start my lease?

  To tackle this question, I used Zillow’s public data...'
---

Par Zhen Liu

Lorsque je cherchais un nouvel appartement à louer, j'ai commencé à me demander : y a-t-il un impact saisonnier ? Existe-t-il un mois où le loyer est le plus bas pour que je puisse économiser lorsque je commence mon bail ?

Pour répondre à cette question, j'ai utilisé les données publiques de Zillow [ici](https://www.zillow.com/research/data/#other-metrics). J'ai analysé leurs données de location pour les appartements d'une chambre de janvier 2011 à septembre 2017 pour les 100 premières villes américaines classées par taille.

**La réponse courte est OUI**. Vous pouvez économiser de **1000 à 2000 dollars** si vous choisissez le bon mois pour commencer à louer dans certaines villes. En ajustant simplement un modèle de régression linéaire utilisant le temps et le mois pour estimer le loyer, j'ai trouvé des schémas de saisonnalité intéressants pour quelques villes.

**Méthodologie :**

Au niveau macro, **loyer = tendance + saisonnalité**. J'ai ajusté un modèle de régression linéaire pour chaque ville afin de décomposer la tendance et la saisonnalité (en utilisant un cycle de 12 mois).

Modèle : loyer estimé (pour un mois spécifique) = t + t² + m1 + m2 + m3 + … + m12

Variables : **t** et **t²** sont des variables continues pour estimer la tendance ; t est le nombre de mois à partir du mois de début dans une ville. J'ai ajouté t² pour ajuster la tendance quadratique, et vous verrez des courbes claires dans le graphique de Philadelphie ci-dessous.

**m1**, **m2**, … , **m12** sont des variables binaires (0 ou 1) qui indiquent à quel mois appartient un point de données (loyer). Chaque point de données de loyer ne peut être attribué qu'à l'une des variables mensuelles (comme 1). Le reste sera 0.

Après avoir ajusté le modèle ci-dessus pour toutes les villes, j'ai compté combien de coefficients mensuels étaient statistiquement significativement plus élevés que le mois estimé avoir le loyer le plus bas. J'ai considéré les villes avec un compte ≥3 comme ayant un effet de saisonnalité potentiellement important.

Ensuite, j'ai examiné l'ajustement global du modèle pour filtrer les villes avec beaucoup de bruit, et j'ai établi une liste finale des six villes les plus représentatives.

Maintenant, je vais vous montrer ces villes afin que vous puissiez voir le meilleur mois pour commencer à louer. J'ai tracé le loyer simulé par rapport au loyer réel ci-dessous. Vous pouvez voir la différence saisonnière pure (ajustée par la tendance de chaque ville) pour chaque mois dans le coin inférieur droit. Voici comment lire les graphiques :

**Ligne noire** : données réelles de loyer

**Ligne verte** : loyer simulé par le modèle de régression donné le mois et l'année

**Graphique à barres vert en bas à droite** : effet saisonnier pur estimé par le modèle

**Ligne grise** : tendance estimée par le modèle de régression

**Écart saisonnier** : loyer le plus élevé moins loyer le plus bas (la différence estimée entre le point le plus haut et le plus bas du modèle de régression sans effet de tendance)

**Étiquettes numériques** : représentent les mois estimés avoir le loyer le plus élevé (rouge) et le plus bas (bleu)

#### Six villes avec un effet de saisonnalité significatif

Vous économiserez définitivement de l'argent si vous commencez à louer pendant un mois "bas" dans ces villes.

1. **Boston**

Si vous commencez à louer en juin, vous économiserez environ **2484 dollars** par an (207*12) par rapport à un début de bail en novembre. La ligne grise montre une légère tendance à Boston, mais elle n'est pas très significative par rapport au fort facteur saisonnier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*O7j2jme7i-NfCwiCaqclOw.png)

2. **Minneapolis**

Il y a une légère tendance à la hausse, mais l'effet de saisonnalité est plus significatif que la tendance. Vos économies annuelles, si vous louez à partir de décembre, peuvent atteindre **1896 dollars** (158*12). En réalité, ce nombre est susceptible d'être légèrement inférieur, car la tendance à la hausse tend à réduire un peu la différence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g-LTRX9KAENiS9i1VdJong.png)

**3. Philadelphie**

Après l'ajustement du modèle de régression pour la tendance en forme de courbe, l'économie annuelle estimée sur le loyer est de **1404 dollars** (117*12). Ce nombre est plus grand pendant la période avec une tendance à la baisse : vous pouvez voir que la distance entre les loyers de janvier et de mai est étirée davantage avant 2014. Les économies estimées sont plus petites lorsque le loyer global a augmenté au cours des dernières années.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nFFdZPnBAU-WfZBgX8zBCg.png)

**4. Chicago**

La tendance globale à Chicago est en fait l'inverse de celle de Philadelphie — elle a augmenté puis diminué. Mais l'effet de saisonnalité est toujours significatif après ajustement pour la tendance. L'économie annuelle estimée est de **1248 dollars** (104*12). Si la tendance à la baisse se poursuit, l'économie sera plus grande — la distance de loyer entre novembre et avril est étirée davantage comme représenté ces dernières années.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ODN13xjLVsENCt9WM0EJdQ.png)

**5. Columbus**

Il y a une tendance à la hausse notable dans les loyers de Columbus, mais l'effet de saisonnalité est également assez significatif. Les économies annuelles estimées sont plus petites après ajustement de l'écart saisonnier pur (89 $) par la tendance à la hausse, donc vous économiseriez environ **720 dollars** (60*12). Mais vous devriez toujours envisager de commencer votre bail en novembre et d'éviter août.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uJ7DZrhZbn5PgxIoU-LDVA.png)

**6. Woodbridge**

Si vous commencez à louer en décembre, vous économiserez environ **948 dollars** (79*12) par an par rapport à une location à partir de juillet. La tendance n'est pas très significative ici, donc c'est toujours la saisonnalité qui détermine le prix du loyer à Woodbridge.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R08gdHIMwHRp8-AeYTZsrg.png)

**Et Seattle, la ville où je vis ?**

L'effet de saisonnalité existe également à Seattle, et il montre une signification dans le modèle de régression. Cependant, la tendance est si forte que la saisonnalité compte presque pas.

Néanmoins, comprendre la saisonnalité pour des villes comme Seattle peut être utile. Bien que vous ne puissiez peut-être pas négocier une réduction de loyer significative en basse saison, vous pourriez demander que les frais de dossier soient supprimés ou quelque chose de similaire.

Mon appartement actuel a supprimé les miens lorsque j'ai commencé mon bail en janvier — décembre a le loyer le plus bas, suivi de janvier. Mais ils pourraient ne pas offrir cet avantage pendant les mois les plus chargés avec des loyers plus élevés, comme mai et juin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g-Odn1rQgGeAIrfq8bgbIw.png)

Une autre ville où la tendance l'emporte sur la saisonnalité est Omaha.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5SWacHouHqUv5kro3ONA_A.png)

Connaître la saisonnalité des loyers dans votre ville peut vous aider à économiser des milliers si vous connaissez le schéma. J'ai fait mon analyse et mes graphiques en utilisant R, mais vous pouvez simplement tracer les données de votre ville dans Excel si vous voulez juste voir s'il y a une tendance ou une saisonnalité notable. Utiliser des données open source pour pirater vos décisions de vie et économiser de l'argent est en fait assez simple.

#### Maintenant, combien de temps devez-vous signer votre bail ?

Supposons que vous avez plusieurs options pour la durée de votre bail. Habituellement, c'est de neuf mois à 18 mois. Savez-vous quelle est la meilleure durée à choisir lorsque vous signez votre bail ? Il y a en fait une autre astuce pour économiser de l'argent lorsque vous choisissez la durée, et je vous montrerai l'astuce et les mathématiques qui la sous-tendent dans mon prochain article.

Donnez-moi quelques applaudissements et partagez cela avec des amis qui pourraient trouver cela utile !

**_Vous pouvez trouver mon code [ici](https://github.com/zhendata/Rent_Seasonality/blob/master/rent_seasonality_zhendata.R)_**.