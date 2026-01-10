---
title: Pourquoi vous pourriez vouloir déplacer vos charges de travail hors du cloud
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-11-29T21:24:11.000Z'
originalURL: https://freecodecamp.org/news/why-you-might-want-to-move-your-workloads-out-of-the-cloud
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/pexels-pixabay-52531.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
seo_title: Pourquoi vous pourriez vouloir déplacer vos charges de travail hors du
  cloud
seo_desc: 'Is a public cloud like AWS or Microsoft''s Azure the right place to host
  every deployment workload at every stage of its life? To be honest, I once thought
  that that was true – at least 95% of the time.

  But things have changed. Even though new service...'
---

Un cloud public comme AWS ou Microsoft Azure est-il le bon endroit pour héberger _toutes_ les charges de travail de déploiement à _chaque_ étape de leur cycle de vie ? Pour être honnête, je pensais autrefois que c'était vrai – au moins 95 % du temps.

Mais les choses ont changé. Même si de nouveaux services sont ajoutés à AWS, par exemple, presque chaque semaine, nous avons eu amplement le temps de comprendre comment les choses fonctionnent généralement. Il est donc logique d'écouter lorsque les administrateurs et les leaders de l'industrie partagent leurs expériences.

Dans cet article, je compte partager quelques raisons importantes pour évaluer et, peut-être, repenser vos stratégies de déploiement. Il n'existe certainement pas une seule approche qui convienne à tout le monde, mais chacun doit au moins considérer le tableau d'ensemble.

_Cet article est extrait de mon cours Pluralsight : [The IT Ops Sessions: Why Some Companies Are Moving OUT of the Cloud](https://pluralsight.pxf.io/PyqkVQ)._

## Quel est le "problème" avec le cloud ?

Alors, que nous disent les experts ? Le numéro un semble être que, une fois que votre entreprise atteint une certaine échelle, les coûts d'exploitation du cloud commencent à peser lourd. Et cette fameuse "complexité réduite" dont tout le monde parle ? Pas tant que ça.

Plongeons un peu plus profondément.

Lorsque tout ce que vous avez en cours d'exécution est un site web sur une seule instance Linux et quelques données stockées dans un couple de buckets S3, vous ne remarquerez à peine les factures mensuelles.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/slide-10-3.png)
_Une zone de disponibilité AWS avec une seule instance EC2 et deux buckets S3_

Mais une fois que la demande de vos utilisateurs commence à augmenter et que la possibilité de perdre certaines de vos données ou même une panne d'une heure vous empêche de dormir, alors vous devrez jeter un nouveau regard sur les chiffres.

Vous voyez, une fois que votre application nécessite une haute disponibilité, cette instance unique ne suffira plus. Vous aurez besoin _au moins_ d'une deuxième instance hébergée dans une zone de disponibilité différente.

Mais maintenant que votre front-end est distribué, vous aurez besoin d'une base de données dédiée à haute disponibilité fonctionnant quelque part que chacune de vos instances peut accéder en temps réel. Sur AWS, cela signifiera une instance RDS. Et elles ne sont pas gratuites.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/slide-11.png)
_Deux zones de disponibilité AWS avec des instances EC2 répliquées_

Prévoyez-vous des transferts de données significatifs entre vos serveurs et vos utilisateurs ? Comptez sur des coûts réseau supplémentaires _et_ sur des types d'instances optimisées pour le réseau plus coûteux. Le partage de vos instances avec d'autres clients AWS ne suffit pas à vos exigences de sécurité ? Alors vous pouvez ajouter les coûts continus des hôtes dédiés.

Vous pouvez l'essayer vous-même sur le pratique [AWS Pricing Calculator](https://calculator.aws/#/) : il ne faudra pas longtemps avant que vos coûts n'atteignent des dizaines, voire des centaines de milliers de dollars chaque mois.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/aws_calculator-1.png)
_Le résultat d'une estimation typique du calculateur de prix AWS_

Je ne suggère certainement pas que ces coûts sont injustes ou qu'ils ne sont pas justifiés. AWS et d'autres grands fournisseurs de cloud travaillent très dur pour vous donner autant d'informations que vous aurez besoin pour comprendre ce que vous dépenserez et même comment vous pouvez dépenser moins. Mais il est indéniable que la location de nombreuses ressources de calcul peut devenir très coûteuse.

## À quoi ressemble la répatriation du cloud ?

Maintenant, imaginez ce que cela pourrait signifier d'appliquer toutes ces exigences pour répondre aux besoins d'une entreprise de l'envergure de Dropbox ou même de X – par lequel, bien sûr, je veux dire Twitter – tous deux ayant rapatrié au moins une partie de leur infrastructure cloud.

Dites ce que vous voulez sur Twitter (et tout le monde a quelque chose à dire), mais ils [ont très récemment annoncé](https://twitter.com/XEng/status/1717754398410240018) que leur réorganisation cloud a conduit à une réduction de 60 % de leur stockage de médias basé sur le cloud et que leurs coûts de traitement des données cloud ont chuté de 75 %. Globalement, les estimations suggèrent qu'ils dépensent désormais environ 60 millions de dollars de moins chaque année sur les services AWS.

Mais ce n'est même pas la partie la plus impressionnante. Parce qu'ils ont apporté ces changements en même temps qu'ils _réduisaient_ leur effectif de 75 %. Et, bien qu'il y ait eu beaucoup de chaos et de pagaille divertissants sur la plateforme, il y a eu peu, voire aucun, de pannes de service notables.

Non seulement ils ont réduit leur utilisation du cloud, mais ils semblent l'avoir fait sans encourir de "pénalité de complexité" – ce qui, bien sûr, les aurait obligés à _augmenter_ leurs embauches et autres dépenses. Par exemple, ils prétendent économiser 13,9 millions de dollars de plus par an en reconfigurant leur épine dorsale réseau.

Naturellement, je ne pourrais pas vous lancer de telles idées sans vous avertir sérieusement de ne jamais essayer cela vous-même à la maison. Ou peut-être même au travail. Ce qui semble avoir fonctionné pour X pourrait ne pas être adapté à votre organisation.

Mais je peux vous dire avec certitude qu'il ne s'agit pas _uniquement_ de X dont nous parlons ici. 37 Signals – les créateurs de Basecamp et Hey – s'attendent à économiser environ 7 millions de dollars sur les cinq années suivant leur retrait d'AWS en 2022.

La société de renseignement de marché IDC a noté que, selon son expérience, la répatriation du cloud a été visible depuis les premiers jours du cloud. Ils prétendent avoir vu une répatriation à un certain niveau dans environ 70 ou 80 pour cent des entreprises chaque année.

Mais nous ne parlons pas nécessairement d'abandonner complètement le cloud. Il s'agit plutôt de comprendre quelles charges de travail appartiennent au cloud et lesquelles doivent être sur site ou dans des installations de colocation.

En règle générale, le cloud est un excellent endroit pour tester de nouvelles charges de travail et lisser les types de demande imprévisibles que vous voyez dans les premiers déploiements. Mais à mesure que vous grandissez, les coûts du cloud pourraient augmenter au point où, pour au moins certains services, vous pouvez le faire moins cher "chez vous".

Et gardez à l'esprit que les migrations vers le cloud qui n'ont pas été suffisamment planifiées et exécutées ou qui ont tout misé plutôt qu'une forme de déploiement hybride sont susceptibles d'échouer avec le temps. Une préparation et une planification appropriées sont cruciales.

Comme l'a dit un rapport d'Andreessen Horowitz : "Vous êtes fou si vous ne commencez pas dans le cloud ; vous êtes fou si vous y restez."

À partir de là, votre travail consistera à évaluer votre profil de déploiement actuel et, s'il y a des éléments qui doivent être améliorés, commencer à cartographier votre plan de répatriation.

_Il y a beaucoup plus de bonnes choses technologiques disponibles pour vous à travers les livres et les cours disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)