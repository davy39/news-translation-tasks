---
title: Une histoire basée sur les données d'Airbnb
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-27T00:22:23.000Z'
originalURL: https://freecodecamp.org/news/a-data-driven-story-of-airbnb-25e6c5be8973
coverImage: https://cdn-media-1.freecodecamp.org/images/0*PTkrnracmwpkL44M
tags:
- name: airbnb
  slug: airbnb
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Travel
  slug: travel
seo_title: Une histoire basée sur les données d'Airbnb
seo_desc: 'By Akshaj Verma

  Users on AirBnB can book a place to stay in over 34,000 cities across more than
  190 countries. The goal of this blog post is to analyze the data, identify problems
  and opportunities, and come up with insights to increase revenue. This...'
---

Par Akshaj Verma

Les utilisateurs d'Airbnb peuvent réserver un logement dans plus de 34 000 villes à travers plus de 190 pays. L'objectif de cet article est d'analyser les données, d'identifier les problèmes et les opportunités, et de proposer des insights pour augmenter les revenus. Ces données proviennent de [Kaggle](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings/data). Si vous êtes intéressé par des projets similaires, consultez mes autres articles de blog [ici](https://medium.com/@akshajverma.oo7).

_Pourquoi Airbnb ?_

Eh bien, je voulais travailler sur un ensemble de données du monde réel avec des implications réelles et un peu de prétraitement. Airbnb était l'ensemble de données le plus intéressant que j'ai trouvé. Alors, c'est parti.

Importer les bibliothèques.

Importer l'ensemble de données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7iJE0oM86yO4FSSKdu7wCg.png)
_Data frame [Image[1]]_

### Prétraitement

Convertir au format date-heure en utilisant lubridate. Remplacer le genre `-unknown-` par NA.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UQEwoq5hF8BWwJyrDut2Xg.png)
_Résumé de df [Image [2]]_

* Les valeurs NA dans la colonne `date_first_booking` indiquent que l'utilisateur n'a pas réservé de chambre.
* Les valeurs NA dans la colonne `age` signifient que l'utilisateur n'a pas spécifié son âge. Nous pouvons remplir des valeurs factices dans la colonne `age`.
* Les valeurs NA dans la colonne `gender` signifient que l'utilisateur n'a pas spécifié son genre.

**Notez** qu'il y a 95 688 valeurs NA dans la colonne genre et 117 763 valeurs remplies. Ainsi, notre analyse basée sur la démographie du genre pourrait ne pas être entièrement correcte dans le monde réel.

Nombre de valeurs NA dans chaque colonne du data frame.

```
colSums(is.na(train_users_2))
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Szdo-TSw4gaj6VGekehAGQ.png)
_Nombre de NA [Image [3]]_

La colonne `age` contient des valeurs inférieures à 18 et supérieures à 80. En fait, `age` contient des valeurs aussi grandes que 104 et 2014. Nous allons leur attribuer des valeurs NA.

Pour remplir les valeurs NA dans la colonne `age`, nous allons calculer la moyenne et l'écart type de la colonne `age`. Ensuite, nous allons générer _n_ nombres sous forme d'entiers aléatoires entre la moyenne et l'écart type pour remplir les valeurs NA. _n_ est le nombre de valeurs NA dans la colonne `age`.

Créer une nouvelle colonne appelée `age_brackets` et l'ajouter au data frame.

Enfin, nous allons ajouter 2 nouvelles colonnes au data frame.

* La première colonne est `time_first_active_to_booking`, qui est égale au nombre de **jours** entre `date_first_booking` et `timestamp_first_active`.
* La deuxième colonne est `time_signup_to_booking`, qui est égale au nombre de **jours** entre `date_first_booking` et `date_account_created`

Voir le nombre de NA par colonne.

```
colSums(is.na(train_users_2))
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*T0sn8BDjySyLEACQfOSbVw.png)
_Nombre de NA [Image [4]]_

* Comme vous pouvez le voir dans le tableau ci-dessus, seules les colonnes `date_first_booking`, `time_first_active_to_booking` et `gender` ont des valeurs NA. C'est tout à fait normal.
* Les valeurs NA dans la colonne `date_first_booking` signifient que l'utilisateur n'a pas encore réservé d'hôtels.
* Les valeurs NA dans la colonne `gender` signifient que l'utilisateur n'a pas spécifié son genre. `time_first_active_to_booking` est dérivé de `date_first_booking`, donc il aura des valeurs NA.

Réinitialiser les niveaux de `gender`. Si vous ne faites pas cela, le niveau `-unknown-` apparaîtra toujours dans les `levels(train_users_2$gender)`. Nous ne voulons pas cela, car nous avons déjà défini toutes les valeurs de genre `-unknown-` à NA.

```
train_users_2$gender <- factor(train_users_2$gender)
```

Nous avons terminé le prétraitement. Ouf. :P

### Analyse exploratoire des données

#### Âge, Genre et Langue

![Image](https://cdn-media-1.freecodecamp.org/images/1*9r5yQfwEZHNPAOZnRK720w.png)
_Âge, genre et langue [Image [5]]_

1. Nous pouvons voir qu'il y a beaucoup de valeurs manquantes pour le genre. La majorité des utilisateurs n'ont pas rempli leurs informations de genre sur la plateforme.
2. Dans le deuxième graphique, nous observons que le groupe d'âge de la majorité des utilisateurs se situe entre 25 et 47 ans, avec le plus d'utilisateurs autour de 30 ans. Cela nous indique que les jeunes et les utilisateurs d'âge moyen sont dominants.
3. Pour une entreprise basée aux États-Unis, il n'est pas surprenant que la langue la plus utilisée sur leur portail/application soit l'anglais.
4. Si nous retirons la langue anglaise du graphique, le chinois (zh) est la langue la plus populaire suivante sur Airbnb, suivie du français et de l'espagnol. Cela suggère qu'Airbnb, après les États-Unis, est vraiment populaire dans les pays/communautés francophones et hispanophones. Le français est principalement parlé en France, donc nous savons que cette application est populaire en France. Mais nous ne pouvons pas en dire autant pour l'espagnol, car l'espagnol est parlé dans de nombreux pays, dont l'Espagne, la Colombie et les États-Unis, parmi beaucoup d'autres.

Ces données, ainsi que la localisation de l'utilisateur, peuvent être utilisées pour identifier quelles régions (à l'intérieur des pays) utilisent quelle langue. Ensuite, peut-être, nous pourrions montrer des publicités ciblées à ces communautés.

#### Âge vs Genre

![Image](https://cdn-media-1.freecodecamp.org/images/1*goavdH-aHWSbVeK2DBiyWg.png)
_Distribution de l'âge vs genre [Image [6]]_

En fonction de l'âge, il y a presque aucune différence entre le nombre d'hommes et de femmes qui utilisent Airbnb. Les hommes et les femmes dans la trentaine sont les utilisateurs les plus importants d'Airbnb.

#### Marketing d'affiliation a.k.a Publicités

Avant de commencer à analyser les graphiques, comprenons ce qu'est le marketing d'affiliation.

Le marketing d'affiliation est un type de marketing basé sur la performance dans lequel une entreprise récompense un ou plusieurs affiliés pour chaque visiteur ou client apporté par les efforts de marketing propres aux affiliés. Le marketing d'affiliation devient rapidement un moyen puissant d'augmenter les ventes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jfpMnEsdaFv5Pxb5vih7RA.png)
_Fournisseur d'affiliation et canal [Image [7]]_

Les 2 graphiques montrent la distribution des canaux d'affiliation utilisés par différents fournisseurs d'affiliation.

Le marketing direct effectué par Airbnb lui-même a eu le plus de portée en termes de marketing. Le marketing direct est une forme de publicité où les organisations communiquent directement avec les clients à travers divers médias, y compris les messages texte, les e-mails, les sites web, les publicités en ligne, les lettres promotionnelles et la télévision ciblée.

Google est un fournisseur d'affiliation proche second avec le semi-branding comme canal d'affiliation le plus populaire. Bing, Facebook et Craigslist sont les autres contributeurs "majeurs".

![Image](https://cdn-media-1.freecodecamp.org/images/0*inbmoBh9IOUetxyA.png)
_Marketing direct — Téléphérique [Image [8]]_

#### **Marketing ciblé basé sur l'âge**

Ces graphiques montrent la comparaison de l'utilisation de la plateforme Airbnb en fonction de la démographie de l'âge.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IbllGPnchClgQ1oPGJ__hw.png)
_Marketing ciblé par âge [Image [9]]_

#### **Marketing ciblé basé sur le genre**

Ces graphiques montrent la comparaison de l'utilisation de la plateforme Airbnb en fonction de la démographie du genre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kwZni5Bp6my9whz48rs-SA.png)
_Marketing ciblé par genre [Image [10]]_

1. Plus de femmes que d'hommes sont ciblées par le canal d'affiliation direct.
2. Même chose pour le fournisseur d'affiliation direct.
3. Si nous retirons le canal d'affiliation `direct`, nous observons que le semi-branding et le semi non-branding sont les deux canaux les plus populaires, suivis par l'API et le SEO (Search Engine Optimization). À l'exception du canal API, tous les autres canaux s'adressent à plus de femmes que d'hommes.
4. Google en tant que fournisseur d'affiliation est plus courant chez les femmes que chez les hommes.

![Image](https://cdn-media-1.freecodecamp.org/images/0*BIA5n9ARSjjo7dEW)
_Marketing ciblé [Image [11]]_

#### Application d'inscription et méthode d'inscription

![Image](https://cdn-media-1.freecodecamp.org/images/1*e_Tz_UOdUldQOEVnEznLWQ.png)
_Application et méthode d'inscription [Image [12]]_

1. S'inscrire en utilisant l'email est l'option la plus populaire, suivie par l'inscription en utilisant Facebook. Personne n'aime lier son compte Google à son compte Airbnb.
2. Une majorité écrasante de personnes accèdent à la plateforme Airbnb en utilisant des navigateurs sur leurs ordinateurs, suivis par leur application iOS. Le fait que les utilisateurs d'Android soient moins nombreux que les utilisateurs d'iOS peut sembler étrange, mais rappelez-vous qu'Airbnb est une entreprise américaine avec sa plus grande base d'utilisateurs étant les Américains. iOS est plus populaire aux États-Unis qu'Android.
3. Les gens n'utilisent probablement pas autant l'application. Cela pourrait être parce qu'ils n'aiment pas l'UI ou la fonctionnalité de l'application Android/iOS. Peut-être que la version web offre plus de fonctionnalités et est plus facile à utiliser. Ou les gens ne sont pas conscients de l'application Airbnb.

#### Application et méthode d'inscription basées sur l'âge et le genre

![Image](https://cdn-media-1.freecodecamp.org/images/1*7pN3fVuJrwIlLsa_pep5rw.png)
_Âge et genre d'inscription [Image [13]]_

1. Comme prévu, les personnes âgées n'utilisent pas du tout les smartphones pour utiliser Airbnb. Un grand nombre de personnes dans la vingtaine, la trentaine et la quarantaine utilisent leurs ordinateurs pour accéder à la plateforme Airbnb. On pourrait s'attendre à ce que les adolescents et les jeunes de 20 ans, "tech savvy", utilisent davantage les smartphones, mais ce n'est pas le cas. (Notez qu'il y a beaucoup plus de personnes dans la tranche d'âge des 30 ans. Cette hypothèse pourrait être fausse.)
2. Plus de femmes préfèrent s'inscrire en utilisant leurs ordinateurs tandis que plus d'hommes préfèrent les applications iOS/Android.
3. Beaucoup plus de personnes dans la trentaine préfèrent s'inscrire en utilisant l'email par rapport à Facebook. Un nombre presque étrangement égal de personnes dans la vingtaine et la trentaine préfèrent s'inscrire en utilisant Facebook.
4. Plus de femmes que d'hommes préfèrent utiliser les méthodes d'inscription Facebook et email. Comparée aux deux autres, la méthode d'inscription Google est comme une erreur 404, n'existe pas.

#### Type de premier appareil vs âge et genre

![Image](https://cdn-media-1.freecodecamp.org/images/1*G1u8CZ839C4S3jiDZGuIgQ.png)
_Type de premier appareil - Genre[Image [14]]_

1. Les Macs sont les ordinateurs portables les plus préférés pour accéder à la plateforme Airbnb, suivis par les ordinateurs de bureau Windows. Encore une fois, Apple est extrêmement populaire aux États-Unis.
2. Les iPhones et les iPads sont les deuxièmes appareils les plus largement utilisés pour accéder à la plateforme Airbnb.

![Image](https://cdn-media-1.freecodecamp.org/images/1*naCcqnOMjtuu22rhXZBKLg.png)
_Type de premier appareil - Âge[Image[15]]_

1. Les Macs de bureau sont très populaires parmi les personnes dans la vingtaine et la trentaine pour accéder à la plateforme Airbnb, suivis par les ordinateurs de bureau Windows.
2. Nous observons une tendance à la baisse dans l'utilisation des Macs à mesure que l'âge augmente. Il n'y a pas de disparité entre les Macs de bureau et les ordinateurs de bureau Windows pour les personnes dans la soixantaine.
3. Les smartphones, cependant, deviennent impopulaires à mesure que l'âge augmente.

#### Réservations et comptes au fil des ans

![Image](https://cdn-media-1.freecodecamp.org/images/1*lFSA9eQNF7btIYku_43sEA.png)
_Réservations et comptes [Image [16]]_

1. Le nombre de réservations augmente rapidement chaque année.
2. La chute brutale des réservations pour l'année 2015 est due au fait que nous n'avons des données que jusqu'au 29-06-2015. `filter(train_users_2, date_first_booking >= "2015-06-29")`
3. Pour le nombre de comptes créés, nous n'avons des données que jusqu'au 2014-06-30. `filter(train_users_2, date_account_created >= "2014-06-30")`

#### Nombre de premières réservations par an

![Image](https://cdn-media-1.freecodecamp.org/images/1*zjpdeFl6KFdk6UuSmK162A.png)
_Premières réservations [Image [17]]_

1. Le nombre de premières réservations est à son plus bas autour de janvier. Cela pourrait être parce que l'année vient de se terminer, donc les gens ne voyagent nulle part si tôt. De plus, il fait froid dehors, non ?
2. Le nombre de premières réservations augmente toujours entre les mois de juillet et octobre. Cela pourrait être en anticipation de festivals comme Thanksgiving et Oktoberfest (ou les vacances d'été).
3. Cependant, nous observons une chute brutale du nombre de réservations à partir de juillet 2014 jusqu'en juillet 2015.

> "En juillet 2014, Airbnb a révélé des révisions de conception du site et de l'application mobile et a introduit un nouveau logo. Certains ont considéré que le nouveau logo était visuellement similaire à des organes génitaux, mais une enquête de consommation par Survata a montré qu'une minorité de répondants pensaient que c'était le cas."

Googlez "Airbnb 2014" pour trouver la raison de la chute soudaine du nombre de réservations en 2014.

#### Nombre de comptes créés par an

![Image](https://cdn-media-1.freecodecamp.org/images/1*PE5rAKyRIXCEukOpl4rQsw.png)
_Premier compte [Image [18]]_

1. Ce graphique suit une tendance similaire au graphique précédent.
2. Le nombre de nouveaux (premiers) comptes créés est moins élevé autour de janvier et augmente autour de septembre et octobre.
3. Les gens créent probablement de nouveaux comptes pour réserver ainsi que pour comparer les prix entre autres services.

Airbnb pourrait probablement réduire les prix ou donner plus de réductions et d'offres pendant les mois d'août, septembre et octobre afin que plus de personnes réservent des logements.

#### Temps entre l'inscription et la première réservation basé sur l'âge et le genre

![Image](https://cdn-media-1.freecodecamp.org/images/1*MwrAART4ipCW2ra5LEGBNA.png)
_Réservation — Inscription [Image[19]]_

Les boîtes colorées indiquent l'intervalle interquartile qui représente les 50 % du milieu des données. Les moustaches s'étendent de chaque côté de la boîte. Les moustaches représentent les plages pour les 25 % inférieurs et les 25 % supérieurs des valeurs de données, à l'exclusion des valeurs aberrantes.

1. Une grande majorité de personnes, indépendamment de l'âge et du genre, réservent des chambres le jour où elles s'inscrivent. La valeur médiane est 0.
2. Vous pouvez voir les "valeurs aberrantes" réserver des chambres plus de 1000 jours après s'être inscrites sur la plateforme.
3. Le "temps d'attente" pour les 50 % du milieu des utilisateurs de chaque tranche d'âge tend généralement à diminuer avec l'âge.

#### Temps entre la première réservation et la première activité

![Image](https://cdn-media-1.freecodecamp.org/images/1*l4T9Bprkdg5UdScqaD-9YA.png)
_Réservation — Active [Image [20]]_

1. Le temps entre la première réservation et la première activité des utilisateurs est de 0 ou proche de 0 pour beaucoup de personnes.
2. Il y a des personnes qui ont réservé leur première chambre plus de 100 jours après leur première activité sur la plateforme Airbnb. Dommage.

#### Temps entre la première réservation et l'inscription

![Image](https://cdn-media-1.freecodecamp.org/images/1*gvA4x1b6PpYOV0zeoe9euA.png)
_Réservation — Inscription [Image [21]]_

1. Ici, nous voyons que le nombre de jours est négatif pour un assez grand nombre de personnes. Les gens ont réservé des chambres jusqu'à un an avant de créer un compte. À part cela, les données semblent similaires au graphique précédent.
2. Un énorme nombre de personnes réservent les chambres le même jour où elles s'inscrivent sur la plateforme Airbnb.

Analysons les valeurs négatives. Combien y a-t-il de valeurs négatives ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*D-rYnKE-qUhVWnu5W4zLmw.png)
_Temps négatif [Image [22]]_

Nous voyons qu'il n'y a que 29 valeurs négatives. Cela signifie qu'il y avait 29 utilisateurs qui ont pu réserver leurs chambres sans créer de compte !

Voyons dans quelles années cela s'est produit. Après avoir filtré uniquement les valeurs négatives de `time_signup_to_booking`, c'est-à-dire les personnes qui ont réservé des chambres avant de s'inscrire, nous traçons le graphique suivant. Ce graphique nous indique que les utilisateurs pouvaient s'inscrire avant de réserver sur la plateforme Airbnb de 2010 à 2013.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EmFSzPTsprBzTNidPzG28A.png)
_Compte par an de réservation avant l'inscription [Image [23]]_

La déclaration suivante a été publiée par Airbnb.

> "Jusqu'au début de 2013, il y avait une poignée de flux où un utilisateur pouvait réserver avant de créer entièrement un compte (par la définition de la création de compte que nous utilisons aujourd'hui). Après le début de 2013, cela n'est plus possible."

### Résultats

#### Réservé vs Non Réservé

`NDF` signifie qu'aucune réservation n'a été faite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2PLKtzYL1DrpJImHLoe7ig.png)
_Réservé vs Non Réservé [Image [24]]_

1. Il y a clairement plus d'utilisateurs inertes que d'utilisateurs actifs.
2. Le ratio homme vs femme est à peu près le même pour les utilisateurs qui réservent vs ceux qui ne le font pas. Les valeurs NA, cependant, diffèrent. Il y a beaucoup d'utilisateurs qui ne fournissent pas leur genre et ne réservent aucune chambre.
3. Les personnes dans la trentaine sont les plus nombreuses dans le lot pour la réservation et la non-réservation de chambres. Le ratio **Réservé** : NonRéservé est inférieur à 1 pour les personnes dans la vingtaine, la trentaine et la quarantaine. Alors que le même ratio est plus ou moins constant pour les personnes dans la cinquantaine, la soixantaine et la soixantaine.
4. Comme vous pouvez le voir, un énorme nombre de personnes ne finissent pas par réserver de chambres. Les États-Unis ont le plus grand nombre de réservations après cela. Un grand nombre de ces réservations doivent être nationales, car l'entreprise elle-même est basée aux États-Unis.

Le graphique montre que les personnes dans la vingtaine, la trentaine et la quarantaine sont les clients de base d'Airbnb.

#### Fréquence du pays de destination

![Image](https://cdn-media-1.freecodecamp.org/images/1*o6D-Hmf0iV5egfkQqNHWlg.png)
_Fréquence du pays de destination [Image [25]]_

1. Le plus grand nombre d'utilisateurs inactifs (personnes qui n'ont pas réservé de chambre) sont dans la trentaine.
2. Les femmes voyagent légèrement plus que les hommes en utilisant Airbnb.
3. Après les États-Unis et les pays "autres", la France est la prochaine destination la plus populaire.
4. Plus de femmes voyagent en France par rapport aux hommes, tandis que plus d'hommes visitent le Canada par rapport aux femmes.

Notez que le voyage n'a pas besoin d'être uniquement international. Il peut être à la fois national ou international, car le pays d'origine des utilisateurs n'est pas fourni dans l'ensemble de données.

#### Effet du canal d'affiliation sur le pays de destination

![Image](https://cdn-media-1.freecodecamp.org/images/1*UP2mI1xz1wf_3gAOlRAqgw.png)
_Effet des canaux d'affiliation sur la destination [Image [24]]_

1. Les canaux d'affiliation directs ont joué un rôle majeur pour confirmer les réservations.
2. Le canal d'affiliation semi-branding joue un rôle important pour confirmer les réservations, en particulier aux États-Unis.

#### Effet du fournisseur d'affiliation sur le pays de destination

![Image](https://cdn-media-1.freecodecamp.org/images/1*HA0F0dPpQF5fGzIYTVgi8g.png)
_Effet des fournisseurs d'affiliation sur la destination [Image [25]]_

Après le fournisseur d'affiliation direct, Google joue un rôle important dans la confirmation des réservations.

#### Statistiques mensuelles de réservation basées sur le genre

![Image](https://cdn-media-1.freecodecamp.org/images/1*urQsFGGVWyoqwltIHdFC2Q.png)
_Réservations mensuelles vs genre [Image [26]]_

1. Les femmes ont toujours réservé plus d'hôtels sur Airbnb que les hommes, sauf pour un mois — décembre 2013.
2. Nous pouvons voir le nombre total de réservations atteindre un pic autour de juillet, sauf en 2014 et 2015.

#### Statistiques hebdomadaires de réservation basées sur le genre

![Image](https://cdn-media-1.freecodecamp.org/images/1*W9_6fqIv1SbncelwNMo_Xg.png)
_Réservation hebdomadaire vs genre [Image [27]]_

1. Le nombre de réservations est toujours le plus bas pendant le week-end, c'est-à-dire le samedi et le dimanche.
2. Le nombre de réservations atteint toujours un pic le jeudi et le vendredi. Les gens réservent probablement des chambres pour le week-end le jeudi et le vendredi.
3. Les réservations d'hôtels par les hommes chutent beaucoup le dimanche par rapport au samedi, mais c'est l'inverse pour les femmes.
4. Le nombre de réservations continue d'augmenter du lundi au vendredi pour chuter le week-end.

#### Variation quotidienne du nombre de réservations

![Image](https://cdn-media-1.freecodecamp.org/images/1*Osmuk0J07N7s7bNBcIE1ag.png)
_Réservation quotidienne vs genre [Image [28]]_

Nous observons qu'Airbnb est passé de 0 à 50 réservations par jour en 2010 à près de 200 réservations par jour au début de 2014. Le nombre est ensuite tombé à environ 100 réservations par jour.

### Conclusions

Avant de commencer à travailler sur cela, j'avais quelques idées préconçues sur le type de résultats que j'obtiendrais. Par exemple, je ne m'attendais pas à ce que iOS soit immensément populaire. Plus encore qu'Android.

Sur les 432 millions de smartphones vendus au dernier trimestre 2016, 352 millions fonctionnaient sous Android (81,7 pour cent) et 77 millions sous iOS (17,9 pour cent).

![Image](https://cdn-media-1.freecodecamp.org/images/0*gNLL25B636vyy50f.png)
_Ventes mondiales de smartphones au quatrième trimestre 2016. (Milliers d'unités) [Image [29] crédits : [Gartner](https://www.gartner.com/newsroom/id/3609817" rel="noopener" target="_blank" title=")]_

La chute brutale du nombre d'utilisateurs autour de juillet 2014 était également un peu inattendue. Je veux dire, l'entreprise avait un taux de croissance fantastique jusqu'à ce point. Tout a commencé à aller de mal en pis après cela. Bien que nous n'ayons des données que jusqu'à la mi-2015, qui sait, les réservations ont peut-être repris après cela.

Qui aurait pensé que le nombre de réservations chuterait le week-end ? Certainement pas moi. Mais il s'avère que si vous voulez sortir le week-end, vous devez réserver vos hôtels avant cela. _Mon erreur. :P_

Réserver une chambre avant de créer un compte ? Cette partie m'a pris beaucoup de temps à comprendre. Je pensais que j'avais fait une erreur. Mais quand j'ai finalement googlé, il s'avère que cela était possible avant le début de 2013. Airbnb a corrigé le bug peu après.

L'autre chose qui a retenu mon attention était que les personnes dans la trentaine étaient plus actives sur Airbnb par rapport aux personnes dans la vingtaine. _COMMENT ?_ Je ne m'attendais certainement pas à ce que les personnes dans la soixantaine voyagent, encore moins utilisent Airbnb. *_*

Merci d'avoir lu. _Les suggestions et les critiques constructives sont les bienvenues. :)_ Vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/akshajverma7/). Vous pouvez consulter le code complet [ici](https://rpubs.com/scarecrow21/airbnb-exploratory-analysis).

Vous pouvez également consulter mes autres articles de blog [Analyse exploratoire de l'ensemble de données FIFA 18 en utilisant R](https://towardsdatascience.com/exploratory-analysis-of-fifa-18-dataset-using-r-ba09aa4a2d3c), [Getting Started With Hive](https://towardsdatascience.com/getting-started-with-hive-ad8a93862f1a), et [GgPlot 'Em All | Pokemon on R](https://towardsdatascience.com/exploratory-analysis-of-pokemons-using-r-8600229346fb).