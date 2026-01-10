---
title: Mise à l'échelle horizontale vs. verticale – Comment mettre à l'échelle une
  base de données
subtitle: ''
author: Sophia Iroegbu
co_authors: []
series: null
date: '2022-06-09T15:26:24.000Z'
originalURL: https://freecodecamp.org/news/horizontal-vs-vertical-scaling-in-database
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Tech-Blog-Cover.png
tags:
- name: vertical
  slug: vertical
- name: database
  slug: database
- name: Horizontal
  slug: horizontal
- name: scalability
  slug: scalability
- name: scaling
  slug: scaling
seo_title: Mise à l'échelle horizontale vs. verticale – Comment mettre à l'échelle
  une base de données
seo_desc: "Data Scalability\nData scalability refers to the ability of a database\
  \ to manipulate changing demands by adding and removing data. In this way, the database\
  \ grows at the same pace as the software. \nVia scaling, the database can expand\
  \ or contract the ..."
---

## Évolutivité des données

L'évolutivité des données fait référence à la capacité d'une base de données à manipuler des demandes changeantes en ajoutant et en supprimant des données. De cette manière, la base de données croît au même rythme que le logiciel. 

Via la mise à l'échelle, la base de données peut étendre ou réduire la capacité des ressources du système pour soutenir l'utilisation fréquemment changeante de l'application.

**Il existe deux façons de mettre à l'échelle une base de données :**

* Mise à l'échelle horizontale (scale-out)
* Mise à l'échelle verticale (scale-up)

Dans cet article, nous examinerons les deux méthodes de mise à l'échelle et discuterons des avantages et des inconvénients de chacune pour vous aider à choisir.

## Mise à l'échelle horizontale

Cette approche de mise à l'échelle ajoute plus de nœuds de base de données pour gérer la charge de travail accrue. Elle diminue la charge sur le serveur plutôt que d'étendre les serveurs individuels. 

Lorsque vous avez besoin de plus de capacité, vous pouvez ajouter plus de serveurs au cluster. Un autre nom pour cette méthode de mise à l'échelle est **l'évolutivité horizontale**.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/scaling-out.jpg)

### Avantages de la mise à l'échelle horizontale :

* Elle est facile à mettre à niveau
* Elle est simple à implémenter et coûte moins cher
* Elle offre des outils flexibles et évolutifs
* Elle permet une mise à l'échelle illimitée avec l'ajout illimité d'instances de serveur
* La mise à niveau d'une base de données mise à l'échelle horizontalement est facile – il suffit d'ajouter un nœud au serveur

### Inconvénients de la mise à l'échelle horizontale :

* Tout bug dans le code deviendra plus complexe à déboguer et à comprendre
* Les frais de licence sont élevés car vous aurez plus de nœuds sous licence
* Le coût du centre de données augmentera considérablement en raison de l'espace, du refroidissement et de l'alimentation supplémentaires requis

### Quand utiliser la mise à l'échelle horizontale :

Si vous traitez avec plus de mille utilisateurs, il est préférable d'utiliser ce système de mise à l'échelle car lorsque les serveurs reçoivent plusieurs requêtes d'utilisateurs, tout se mettra à l'échelle correctement.

Il ne plantera pas non plus car il y a plusieurs serveurs.

## Mise à l'échelle verticale

L'approche de mise à l'échelle verticale augmente la capacité d'une seule machine en augmentant les ressources dans le même serveur logique. Cela implique l'ajout de ressources comme la mémoire, le stockage et la puissance de traitement au logiciel existant, améliorant ainsi ses performances. 

Il s'agit de la méthode traditionnelle de mise à l'échelle d'une base de données. Un autre nom pour cette approche est **l'évolutivité verticale**.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/02vertical-scaling-software-scalability.jpg)

### Avantages de la mise à l'échelle verticale :

* Le coût du centre de données pour l'espace, le refroidissement et l'alimentation sera moindre
* Il s'agit d'un logiciel rentable
* Il est facile à utiliser et à implémenter – l'administrateur peut facilement gérer et maintenir le logiciel
* Les ressources pour cette approche sont flexibles

### Inconvénients de la mise à l'échelle verticale :

* Le coût peut être faible, mais vous devrez payer une licence chaque fois que vous mettez à l'échelle
* Le matériel coûte plus cher en raison des serveurs haut de gamme
* Il y a une limite à la quantité que vous pouvez mettre à niveau
* Vous êtes limité à un seul fournisseur de base de données, et la migration est difficile, ou vous devrez peut-être tout recommencer

### Quand utiliser la mise à l'échelle verticale :

L'approche de mise à l'échelle verticale est faite pour vous si vous avez besoin d'un système avec une cohérence unique des données.

Si vous ne voulez pas vous soucier de l'équilibrage de la charge de travail du serveur, la mise à l'échelle verticale est la meilleure option.

## Différences entre la mise à l'échelle verticale et horizontale

<table>
<thead>
<tr>
<th style="text-align: left">Verticale</th>
<th style="text-align: left">Horizontale</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">La licence coûte moins cher</td>
<td style="text-align: left">La licence coûte plus cher</td>
</tr>
<tr>
<td style="text-align: left">Cette méthode augmente la puissance du serveur avec des serveurs individuels supplémentaires</td>
<td style="text-align: left">Cette méthode augmente la puissance du serveur avec le serveur existant</td>
</tr>
<tr>
<td style="text-align: left">Ces données sont présentes sur un seul nœud et sont mises à l'échelle via un multicœur</td>
<td style="text-align: left">Cela est basé sur le partitionnement de chaque nœud contenant une seule partie des données</td>
</tr>
</tbody>
</table>

## Quelle méthode de mise à l'échelle est la meilleure pour votre application ?

Lorsque vous choisissez comment mettre à l'échelle votre base de données, vous devez considérer ce qui est en jeu lorsque vous mettez à l'échelle verticalement ou horizontalement. 

Maintenant, nous allons examiner certains facteurs à considérer pour vous aider à choisir quel système de mise à l'échelle est le meilleur pour votre application :

### Équilibrage de charge

Le système de mise à l'échelle verticale est le meilleur pour équilibrer les charges car vous avez un seul serveur (mise à l'échelle verticale), et il n'est pas nécessaire d'équilibrer votre charge. La mise à l'échelle horizontale nécessite que vous équilibriez la charge de travail de manière uniforme.

### Point de défaillance

Le système de mise à l'échelle horizontale dispose de plus d'un serveur, donc lorsqu'un serveur tombe en panne, le suivant prend le relais. Cela signifie qu'il n'y a pas de _point de défaillance unique_, ce qui rend le système résilient.

Mais dans le système de mise à l'échelle verticale, il n'y a qu'un seul serveur, donc une fois que le serveur tombe en panne, tout passe hors ligne.

### Vitesse

En termes de vitesse, le système de mise à l'échelle verticale est plus rapide car, puisqu'il fonctionne sur un seul serveur, le système de mise à l'échelle verticale dispose d'une _communication interprocessus_ – c'est-à-dire que le serveur communique en interne et c'est rapide. 

Le système de mise à l'échelle horizontale dispose d'appels réseau entre deux serveurs ou plus. Cela est également connu sous le nom d'_Appels de Procédure à Distance (RPC)_. Les RPC sont lents, cependant.

### Cohérence des données

Lorsque vous traitez avec des serveurs, vous devez vous assurer que les données stockées sont cohérentes lorsque les utilisateurs finaux envoient une requête. 

Le système de mise à l'échelle verticale est cohérent en termes de données car toutes les informations sont sur un seul serveur. Mais le système de mise à l'échelle horizontale est mis à l'échelle avec plusieurs serveurs, donc la cohérence des données peut être un énorme problème.

### Limites matérielles

Le système de mise à l'échelle horizontale se met à l'échelle correctement car le nombre de serveurs que vous utilisez pour une requête est linéaire par rapport au nombre d'utilisateurs dans la base de données ou le serveur. Le système de mise à l'échelle verticale, en revanche, a une limitation car tout fonctionne sur un seul serveur.

Lorsque vous choisissez un système pour mettre à l'échelle votre base de données, assurez-vous de faire une liste des avantages et des inconvénients des informations dans cet article. Cela vous aidera à décider laquelle utiliser.

## Conclusion

L'évolutivité d'un modèle de cloud computing est la capacité à augmenter ou à réduire rapidement et instantanément une capacité informatique. Savoir comment fonctionnent les deux types de mise à l'échelle est crucial car cela joue un rôle massif dans la gestion de votre base de données ou de votre serveur.

Récapitulatif rapide...

* Le rôle d'un serveur est d'augmenter sa capacité à gérer la charge de travail accrue, appelé **mise à l'échelle verticale**.
* Le rôle d'un système est d'ajouter de nouveaux nœuds pour gérer la charge de travail distribuée, appelé **mise à l'échelle horizontale**.
* Le système de mise à l'échelle horizontale se met à l'échelle correctement à mesure que le nombre d'utilisateurs augmente.
* Le système de mise à l'échelle verticale est plus rapide grâce à sa capacité de communication interprocessus.

Merci d'avoir lu !