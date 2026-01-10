---
title: Comment j'ai analysé les données de location de DVD avec SQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-20T21:53:13.000Z'
originalURL: https://freecodecamp.org/news/project-1-analyzing-dvd-rentals-with-sql-fd12dd674a64
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zGw3_fh6s09rpS3ZCxDYDQ.jpeg
tags:
- name: analytics
  slug: analytics
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
seo_title: Comment j'ai analysé les données de location de DVD avec SQL
seo_desc: 'By Okoh Anita

  Introduction

  I recently completed some training in Data Foundation facilitated by Bertelsmann’s
  School of Data Science (in partnership with Udacity). For a personal project, I
  decided to analyze the database for a DVD rental company we ...'
---

Par Okoh Anita

#### Introduction

J'ai récemment terminé une formation en Data Foundation facilitée par l'école de Data Science de Bertelsmann (en partenariat avec Udacity). Pour un projet personnel, j'ai décidé d'analyser la base de données d'une entreprise de location de DVD que nous appellerons **Rent A Film**. Examinons une étude de cas détaillant mon processus et mes résultats.

#### Ensemble de données

J'ai commencé par examiner la base de données. La base de données **DvdRental** contient 15 tables. Voici les différentes tables et une brève description de chacune.

* actor — contient les données des acteurs, y compris le prénom et le nom de famille.
* film — contient les données des films telles que le titre, l'année de sortie, la durée, la note, etc.
* film_actor — contient les relations entre les films et les acteurs.
* category — contient les données des catégories de films.
* film_category — contient les relations entre les films et les catégories.
* store — contient les données des magasins, y compris le personnel gestionnaire et l'adresse.
* inventory — stocke les données d'inventaire.
* rental — stocke les données de location.
* payment — stocke les paiements des clients.
* staff — stocke les données du personnel.
* customer — stocke les données des clients.
* address — stocke les données d'adresse pour le personnel et les clients.
* city — stocke les noms des villes.
* country — stocke les noms des pays.

_Note : J'ai analysé cette base de données en utilisant PostgreSQL. Vous pouvez obtenir des détails pour installer PostgreSQL [ici](http://www.postgresqltutorial.com/install-postgresql/) et télécharger la base de données de location de DVD [ici](http://www.postgresqltutorial.com/postgresql-sample-database/)._

#### Objectif et buts

Dans ce projet, je vais chercher à répondre aux questions suivantes :

1. Quels sont les genres les plus et les moins loués (en demande) et quels sont leurs ventes totales ?
2. Pouvez-nous savoir combien d'utilisateurs distincts ont loué chaque genre ?
3. Quel est le taux de location moyen pour chaque genre ? (du plus élevé au plus bas)
4. Combien de films loués ont été retournés en retard, en avance et à temps ?
5. Dans quels pays **Rent A Film** a-t-il une présence et quelle est la base de clients dans chaque pays ? Quelles sont les ventes totales dans chaque pays ? (du plus au moins)
6. Qui sont les 5 meilleurs clients en termes de ventes totales et pouvons-nous obtenir leurs détails au cas où **Rent A Film** souhaite les récompenser ?

Avant de commencer les analyses, j'ai d'abord essayé de comprendre le MER (Modèle Entité-Relation) de cette base de données, également connu sous le nom de Schéma. Voici le Schéma ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Re5gkP7yWnJhl7p84eVLeVRxixkh9Po284s0)
_[SCHÉMA DE LOCATION DE DVD](http://www.postgresqltutorial.com/postgresql-sample-database/" rel="noopener" target="_blank" title=")_

Vous pouvez consulter mon code sur mon profil GitHub [ici](https://github.com/anitaokoh/DVD-RENTAL).

#### Analyse

Pour répondre à la première question **"Quels sont les genres les plus et les moins loués (en demande) et quels sont leurs ventes totales ?"**, j'ai d'abord identifié les tables que je devrais joindre, qui sont :

> **Category > film_Category > film > inventory > rental > customer > payment**

Voici la requête que j'ai utilisée pour extraire les données et répondre à la question :

![Image](https://cdn-media-1.freecodecamp.org/images/7-yaKfFB753y7H0NeIdgYtR6c-WMlrjSJJ9d)

![Image](https://cdn-media-1.freecodecamp.org/images/ooD0kn6JsTwZ9XfabDd8nIfsaYHY0eiOAjGz)

**Insights**

À partir du tableau ci-dessus, nous pouvons tirer 3 principaux insights :

* **Rent A Film** propose 16 genres disponibles.
* La catégorie sport semble être le genre le plus loué en termes de nombre de fois où il est loué, et il a également les ventes totales les plus élevées en termes d'argent.
* La catégorie musique est le genre le moins loué en termes de nombre de fois où il est loué et a les ventes totales les plus basses en termes d'argent.

**Question 2 : Pouvez-nous savoir combien d'utilisateurs distincts ont loué chaque genre ? En bref, oui, nous pouvons.**

Les tables à joindre sont les suivantes :

> **Category > film_Category > film > inventory > rental > customer**

Voici ma requête pour cette question :

![Image](https://cdn-media-1.freecodecamp.org/images/8MxaJS0364pwezbp8P-RXTjQ6nLBnqjgiq9v)

![Image](https://cdn-media-1.freecodecamp.org/images/TK2anW8Y-xEhWWToXXcEVVvraLIL5vkiElfp)

**Insights**

Je voulais savoir combien de clients distincts ont loué chacun des genres. Une chose fascinante dans la requête est que, bien que le genre musique ait le moins de locations totales, il n'a pas le moins de clients distincts ayant loué le genre. Le genre voyage détient ce record.

En prenant du recul et en reliant les insights dérivés des questions 1 et 2, nous pouvons dire que le genre voyage a été reloué plus de fois que le genre musique.

Et bien sûr, le genre sport a le plus grand nombre de clients distincts ayant loué le genre.

**Question 3 : Quel est le taux de location moyen pour chaque genre ?** (du plus élevé au plus bas)

Les tables à joindre sont les suivantes :

> **Category > film_Category > film**

Voici ma requête pour cette question :

![Image](https://cdn-media-1.freecodecamp.org/images/wqh-5F-ZpUE1sd3FMMouuxnqpR683paYZtyv)

![Image](https://cdn-media-1.freecodecamp.org/images/jUeVY4Iomda2s1OfWaFqGqhmVPM8LTShibZf)

**Insights**

J'ai vérifié si le nombre de fois qu'une catégorie a été louée avait un lien avec le taux de location moyen de chaque genre. À partir du tableau ci-dessus, nous pouvons facilement conclure que le taux de location moyen n'est peut-être pas un facteur.

Bien que le genre jeu ait le taux de location moyen le plus bas, il fait partie des cinq genres les plus loués. Étonnamment, le genre Musique n'est pas le plus cher — Action l'est, même si le genre action est l'un des genres les plus loués.

Nous pouvons dire en toute sécurité que la plupart des clients sont amateurs de films liés au sport et sont le moins intéressés par les films musicaux.

**Question 4 : Combien de films loués ont été retournés en retard, en avance et à temps ?**

Les tables à joindre sont les suivantes :

> **film > inventory > rental**

![Image](https://cdn-media-1.freecodecamp.org/images/Wk0iyxP6WpwbQLGhZNpz09J38baFiMYMvWDz)

![Image](https://cdn-media-1.freecodecamp.org/images/xe6Cg0xlQER5aZZRc0dAyp-B76gf73MHQZew)

**Insights**

Le statut de retour des films est sans doute l'un des aspects les plus importants à surveiller dans une entreprise de location de DVD. D'après la requête ci-dessus, 48 % des films sont retournés plus tôt que la date d'échéance, tandis que 41 % des films sont retournés en retard et 11 % arrivent à temps.

Il pourrait y avoir un certain nombre de facteurs expliquant pourquoi cela pourrait se produire, comme la distance d'expédition de ces films depuis les magasins, ce qui pourrait être totalement hors du contrôle des clients, etc. *Nous devrions approfondir les données pour comprendre le problème.*

Cependant, il est sage de noter qu'un pourcentage important de films sont retournés en retard. Introduire une pénalité pour les retours en retard pourrait être une source de revenus supplémentaire et, en retour, décourager les retours en retard.

Mais une telle décision ne peut avoir de sens que si nous savons pourquoi le problème se produit.

**Question 5 : Dans quels pays Rent A Film a-t-il une présence et quelle est la base de clients dans chaque pays ? Quelles sont les ventes totales dans chaque pays ?** (Du plus au moins)

Les tables à joindre sont les suivantes :

> **Country > City > Address > customer > payment**

Voir la requête ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/oZfnuGxi1ZsB-TJqS0kTx41mVm1CfOKtvaQD)

![Image](https://cdn-media-1.freecodecamp.org/images/OzlVEmkcz3STrKZ30ZCsPr4gqExcRwjK8DpR)

![Image](https://cdn-media-1.freecodecamp.org/images/G0YGu2nLvUDUe1c-79i5od9yK10gBAH77O6m)

![Image](https://cdn-media-1.freecodecamp.org/images/PhqJRtlIpMfwnnq-qDgd5bX9tohNREX0cNDw)

![Image](https://cdn-media-1.freecodecamp.org/images/ZspQd77D0ahbHZzApXfj-OfsDecw4YJWsUxd)

![Image](https://cdn-media-1.freecodecamp.org/images/bumlck68X66y7788-8f-oIqbGkAQzbxIpIqI)

![Image](https://cdn-media-1.freecodecamp.org/images/GdsPzZEkcaRbpLW7E5rDwL5u5bNLv09fNsep)

![Image](https://cdn-media-1.freecodecamp.org/images/bHNQ8hWQvkNTeTJ0Oza9K1MWzaNBkO7495a-)

**Insights**

**Rent A Film** est présent dans 108 pays, avec l'Inde ayant la plus grande base de clients de 60 clients et les ventes totales les plus élevées en termes d'argent. L'Afghanistan a les ventes totales les plus faibles en termes d'argent, même s'il n'est pas le seul pays avec la plus petite base de clients de 1 client.

**Question 6 : Qui sont les 5 meilleurs clients en termes de ventes totales et pouvons-nous obtenir leurs détails au cas où Rent A Film souhaite les récompenser ?**

Les tables à joindre sont les suivantes :

> **Country > City > Address > customer > payment**

Voir la requête ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/h6oSZOmqcmAkrA9WS0hu0DLdo6Oo9UdZUWbc)

![Image](https://cdn-media-1.freecodecamp.org/images/ivEIz9TpgeeJF5Yc0Cd6gbRZTA5KyN-tYh3S)

**Insights**

En supposant que nous souhaitons récompenser ou envoyer des cadeaux physiques aux meilleurs clients, le tableau ci-dessus montre leurs noms complets, adresses, emails, etc.

Ces informations peuvent être envoyées à l'équipe marketing de l'entreprise afin d'utiliser leur connaissance du domaine pour décider comment les récompenser.

### Conclusion

Dans ce projet, nous avons analysé les données d'une entreprise de location de DVD que nous avons décidé d'appeler **'Rent A Film'** pour trouver des insights sur les clients et leurs préférences. Nous avons obtenu 3 conclusions majeures :

1. L'entreprise a des clients amateurs de sport et il serait conseillé de stocker plus de films liés au sport pour augmenter les ventes totales par rapport aux films liés à la musique. Il serait bon d'augmenter le taux de location moyen des films du genre sport puisque ce n'est pas un facteur majeur dans la location pour les clients. Cela, à son tour, augmente les revenus totaux. Cependant, une analyse plus approfondie doit être effectuée pour conclure sur ce point.
2. Il y a un potentiel pour avoir une source de revenus supplémentaire grâce à des frais sur les retours de films en retard.
3. **Rent A Film** est présent dans 108 pays, avec l'Inde étant le plus grand marché en termes de personnes et de revenus. De plus, 20 % des pays où ils sont présents contribuent à 80 % de la base totale de clients.

_P.S Comme moi, tout le monde peut apprendre à devenir analyste de données et si vous voulez être informé de mon prochain projet ou des mises à jour de mon apprentissage, n'hésitez pas à vous inscrire à ma [newsletter](https://goo.gl/forms/aEbTwhSXRDAUa5tr1)_