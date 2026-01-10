---
title: Pourquoi ne pas simplement externaliser une fonctionnalité ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-19T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/why-not-just-outsource-a-feature
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/0_9xm9ieIbUeSPwdHX.jpg
tags: []
seo_title: Pourquoi ne pas simplement externaliser une fonctionnalité ?
seo_desc: 'By Clark Jason Ngo

  After software release, the application is ready but not industry ready. Third party
  testing is recommended to conform with the industry standards of where the software
  would be used with.

  Why third party testing? Third party testi...'
---

Par Clark Jason Ngo

Après la sortie du logiciel, l'application est prête mais pas prête pour l'industrie. Des tests tiers sont recommandés pour se conformer aux normes de l'industrie où le logiciel serait utilisé.

Pourquoi des tests tiers ? Les tests tiers vérifient les exigences logicielles, détectent les bugs dans le logiciel et évaluent l'acceptation du logiciel (Wang, Zhao, Shi & Zhang, 2013).

Non seulement cela, mais ils sont certifiés et ont l'expertise pour évaluer si le logiciel respecte les normes de l'industrie. De plus, les agences de tests tiers disposent de tests spécialisés et sophistiqués. Tout cela aide non seulement l'entreprise de logiciels, mais aussi l'organisme de régulation ou les régulateurs pour la conformité (comme FERPA, HIPPA, ISO) dans les industries. Enfin, un logiciel ayant été testé par un tiers augmente également la confiance des consommateurs dans le logiciel (Councill, 1999).

Pour des tests rapides et efficaces, décomposez vos différentes fonctionnalités afin de faciliter les tests de certaines fonctions nécessaires pour les tests de conformité. Pour protéger votre propriété intellectuelle, assurez-vous de ne pas exposer le code de votre logique métier. Avec des contrats pour des tests tiers, la révision est approfondie et évitera probablement les failles et permettra à votre agence de tests tiers d'être responsable de tout problème de conformité.

Nous effectuons des tests tiers pour la conformité. Mais au lieu de développer une fonctionnalité nécessitant des tests tiers, pourquoi ne pas simplement utiliser une fonctionnalité tierce conforme que vous pouvez intégrer à votre logiciel ? Par exemple, au lieu de développer votre propre système de paiement par carte de crédit et de faire des tests tiers pour la conformité PCI DSS, pourquoi ne pas utiliser une entreprise qui fournit un service d'intégration de paiement par carte de crédit comme [Stripe](https://stripe.com/) ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*cNgmAxuoNx4Api0e.png)

Stripe est déjà conforme à la norme PCI DSS en étant audité par PCI QSA. Avec ce transfert de responsabilité, l'équipe de régulation de votre entreprise peut se concentrer sur d'autres tâches comme l'amélioration de la transparence et des données de conformité de qualité (EPA testing use of third-party software for CWA compliance monitoring, 2011).

![Image](https://cdn-media-1.freecodecamp.org/images/0*u1v6735qhSmSaWHl.png)

**Références**

Councill, W. T. (1999). Third-party testing and the quality of software components. _IEEE Software_, 16(4), 55–57. doi:http://dx.doi.org.proxy.cityu.edu/10.1109/52.776949

EPA testing use of third-party software for CWA compliance monitoring. (2011). _InsideEPA.Com’s Water Regulation Alert_, Retrieved from [http://proxy.cityu.edu/login?url=https://search-proquest-com.proxy.cityu.edu/docview/922598559?accountid=1230](http://proxy.cityu.edu/login?url=https://search-proquest-com.proxy.cityu.edu/docview/922598559?accountid=1230)

Wang, H., Zhao, G. H., Shi, M. S., & Zhang, F. J. (2013). Analysis of the third party testing of information system software. _Applied Mechanics and Materials_, 427–429, 2325. doi:http://dx.doi.org.proxy.cityu.edu/10.4028/www.scientific.net/AMM.427-429.2325

Zhang, W., Ma, C. X., & Mo, J. S. (2013). The development and application of electricity embedded software testing. _Applied Mechanics and Materials_, 401–403, 1680. doi:http://dx.doi.org.proxy.cityu.edu/10.4028/www.scientific.net/AMM.401-403.1680