---
title: Architecture sacrificielle – Comment prendre des décisions difficiles pour
  abandonner et reconstruire des systèmes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-24T19:02:30.000Z'
originalURL: https://freecodecamp.org/news/sacrificial-architecture-make-tough-decisions-to-abandon-and-rebuild-systems
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-wendelin-jacober-1411400.jpg
tags:
- name: Clean Architecture
  slug: clean-architecture
- name: clean code
  slug: clean-code
- name: Productivity
  slug: productivity
seo_title: Architecture sacrificielle – Comment prendre des décisions difficiles pour
  abandonner et reconstruire des systèmes
seo_desc: "By Nahla Davies\nWhen you're working with an application, sometimes it\
  \ no longer makes sense to try to continue and improve what already exists. Instead,\
  \ you need to rethink, restructure, and rebuild. \nMaking the decision to give up\
  \ all the work you a..."
---

Par Nahla Davies

Lorsque vous travaillez avec une application, il arrive que cela n'ait plus de sens d'essayer de continuer et d'améliorer ce qui existe déjà. Au lieu de cela, vous devez repenser, restructurer et reconstruire. 

Prendre la décision d'abandonner tout le travail que vous et d'autres avez investi dans le système existant est un choix difficile pour de nombreux développeurs. Pourtant, une dévotion obstinée au code existant face à des perturbations est un disservice pour les développeurs et les utilisateurs.

Les effets de toute modification à grande échelle d'un système vont bien au-delà du monde du développement. Les remplacements complets de systèmes sont rarement invisibles, ce qui rend également la vie difficile pour les commerciaux et les marketeurs. Ce sont eux qui doivent expliquer aux clients pourquoi un changement aussi radical s'est produit. 

Mais cela ne rend pas les changements moins nécessaires.

Comme pour tant d'autres choses dans la vie, le fait qu'un choix soit difficile et douloureux ne signifie pas qu'il est mauvais. L'évolution peut être un processus violent. Mais l'échec à s'adapter conduit à l'extinction. 

Lorsque les poissons sont sortis de la mer il y a des millions d'années, ils n'ont pas continué à améliorer les nageoires et les branchies. Des systèmes entièrement nouveaux étaient nécessaires pour le mouvement et la respiration. Cela ne signifie pas que les nageoires et les branchies n'étaient pas précieuses ou que leur conception était défectueuse. En effet, leurs conceptions correspondaient parfaitement à leurs objectifs. Mais l'objectif est devenu irrélevant, et ils n'étaient donc plus adaptés à leur environnement actuel. 

Lorsque le moment viendra (et il viendra), vous devez faire un pas en arrière et examiner objectivement la situation. Une autre modification de cette nageoire fonctionnera-t-elle ? Ou ne fera-t-elle que souligner à quel point elle est mal adaptée aux besoins actuels ?

## Choix de conception intelligent ou réaction inévitable ?

Une grande partie de la discussion sur l'architecture sacrificielle tourne autour de la question de savoir si elle doit être un processus de développement proactif plutôt qu'une décision réactionnaire de dernier recours. 

Les développeurs doivent-ils intentionnellement construire des systèmes avec des durées de vie limitées ? Ou doivent-ils construire pour le long terme et apporter des changements à grande échelle uniquement si absolument nécessaire ?

Selon Martin Fowler, qui [a introduit l'architecture sacrificielle il y a sept ans](https://www.infoq.com/news/2014/11/sacrificial-architecture/), l'intégrer dans le processus de conception peut être une bonne idée :

> _"Alors, que signifie choisir délibérément une architecture sacrificielle ? Essentiellement, cela signifie accepter dès maintenant que, dans quelques années, vous devrez (espérons-le) abandonner ce que vous construisez actuellement._   
>   
> _Cela peut signifier accepter les limites des besoins multifonctionnels de ce que vous assemblez. Cela peut signifier réfléchir dès maintenant à des choses qui peuvent faciliter le remplacement lorsque le moment viendra - les concepteurs de logiciels réfléchissent rarement à la manière de concevoir leur création pour soutenir son remplacement élégant. Cela signifie également reconnaître que le logiciel abandonné dans un temps relativement court peut encore fournir beaucoup de valeur."_

Le sacrifice intentionnel peut également être utile lors de la considération de nouvelles fonctionnalités ou applications comme moyen de limiter l'effort global de développement. 

L'utilisation de l'architecture sacrificielle pour les systèmes de preuve de concept peut accélérer le processus de développement vers une implémentation lançable. Comme indiqué dans [le cadre d'architecture Agile de l'Open Group](https://pubs.opengroup.org/architecture/o-aaf/snapshot/Agile_Architecture_Framework.html) :

> _"Lorsque l'objectif est d'obtenir rapidement des retours du marché en expérimentant avec un MVP, l'architecture sacrificielle est une option à considérer, car il ne vaudrait pas la peine de passer trop de temps à concevoir une architecture qui devrait changer si le propriétaire du produit décide de pivoter."_

Cela ne signifie pas pour autant que l'utilisation proactive de l'architecture sacrificielle éliminera le besoin de sacrifices réactifs. Il y aura toujours des changements et des perturbations que vous et votre équipe n'anticipez pas. Et les perturbations mènent souvent à des sacrifices et à des évolutions. 

Pensez simplement à la manière dont la crise pandémique de COVID a perturbé tant d'aspects de la vie quotidienne, de la manière dont les employés travaillent à [la manière dont les écoles enseignent à nos enfants](https://www.freecodecamp.org/news/disrupting-the-status-quo-of-traditional-learning-ef83c694cfd7/).

Il existe également de nombreux exemples moins drastiques. Un effet secondaire de la crise COVID a été l'accélération rapide des entreprises de commerce électronique et des transactions en ligne. 

Mais l'industrie a dû s'adapter aux préoccupations croissantes des consommateurs concernant la confidentialité des données. Toutes les entreprises en ligne dépendent de logiciels avec des fonctionnalités cruciales telles que la facturation en ligne et les paiements. Mais les fournisseurs d'applications et les processeurs de paiement ont dû adapter rapidement les systèmes existants pour garantir la conformité avec les nouvelles normes telles que la norme de sécurité des données des cartes de paiement (PCI-DSS) et le règlement général sur la protection des données de l'Union européenne (GDPR). 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-179.png)
_[Source de l'image](https://interestingengineering.com/best-youtube-channels-for-coding-and-programming)_

De la même manière, le code peut devenir obsolète ou ne pas accomplir ses objectifs. Il arrive que des perturbations dans les pratiques de codage ou les capacités des langages de programmation signifient que vous devez apporter des changements à grande échelle. 

Pensez simplement à eBay, qui a changé son langage de programmation sous-jacent deux fois depuis sa création en 1995. Pourquoi ? Parce que les capacités des langages abandonnés n'ont pas réussi à répondre aux besoins et exigences d'eBay à mesure que l'entreprise grandissait.

## Comment anticiper le sacrifice

Les développeurs ne peuvent pas construire pour éviter complètement le besoin de remplacements, et ils ne devraient pas se concentrer sur cela. Il existe cependant des étapes que vous pouvez suivre pour planifier l'obsolescence.

### Construire en pensant au remplacement

Comme l'a déclaré Fowler, vous pouvez construire du code en gardant à l'esprit qu'il nécessitera un remplacement dans quelques années. Le code obsolète finira par devenir vulnérable à des virus malveillants qui pourraient entraîner le détournement de navigateur ou des ralentissements du système. 

Cela signifie que vous devez considérer à l'avance les limitations du code, y compris la performance et la scalabilité, ainsi que d'autres caractéristiques.

### Minimiser le sacrifice grâce à la modularité

En règle générale, il est plus facile de remplacer de petits morceaux de code que de remplacer une structure entière. 

Tout comme vous n'avez pas besoin de dépenser du temps et de l'argent pour remplacer tout votre toit si une tuile est soufflée, il n'est pas nécessaire de réécrire complètement le code d'un système si la révision d'un module suffit. 

Ainsi, la construction de code modulaire aboutit à une architecture [plus facile à modifier pour les développeurs](https://stackoverflow.blog/2021/03/08/infrastructure-as-code-create-and-configure-infrastructure-elements-in-seconds/) selon les besoins.

Mais la modularité n'est pas toujours une solution efficace, et vous devez être conscient des limites de votre code. Parfois, remplacer trop de pièces peut affaiblir une structure ou la rendre instable. 

De la même manière, plus vous remplacez de modules dans votre code existant, plus il y a d'opportunités pour des problèmes avec le fonctionnement du code dans son ensemble. C'est la ligne de démarcation entre la mise à jour continue pièce par pièce et le remplacement complet.

### Maintenir des normes de qualité

Même lorsque vous décidez intentionnellement de construire du code en sachant que vous le sacrifierez dans un avenir proche, vous devez toujours continuer à vous efforcer de respecter ou de dépasser les normes de qualité de l'entreprise. Après tout, l'architecture sacrificielle sera probablement toujours en production. 

Les besoins peuvent également changer, éliminant les raisons pour lesquelles vous prévoyiez de retirer le code en premier lieu. Un code mal conçu ou mal implémenté [rend également la vie des développeurs plus difficile](https://www.freecodecamp.org/news/clean-coding-for-beginners/) lors de la modification du code. 

Une documentation et une structure de code médiocres entravent également votre capacité à comprendre les connexions entre les morceaux de code, rendant les remplacements et les mises à jour plus difficiles. 

Un code mal conçu peut [également représenter un risque de sécurité significatif](https://hostingdata.co.uk/online-privacy-guide/), permettant peut-être aux pirates d'accéder à des données privées dans lesquelles les entreprises ont tant investi pour protéger.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-180.png)
_[Source de l'image](https://www.altexsoft.com/blog/business/technical-documentation-in-software-development-types-best-practices-and-tools/)_

La qualité est un mantra qui doit toujours être au premier plan, même pour le code jetable.

## Se sacrifier pour le bien commun

Bien que cela puisse sembler banal de citer ce dicton courant, sacrifier votre code peut en effet être pour le bien commun de vos systèmes et de votre entreprise à long terme. 

L'utilisation judicieuse et proactive des architectures sacrificielles peut aider à réduire le temps de mise sur le marché pour de nouvelles fonctionnalités. Et cela peut minimiser l'effort nécessaire lorsqu'un remplacement à grande échelle et non planifié se produit inévitablement.