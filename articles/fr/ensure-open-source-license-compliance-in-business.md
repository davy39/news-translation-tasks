---
title: Comment garantir la conformité des licences open source dans votre entreprise
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2024-03-05T11:01:08.000Z'
originalURL: https://freecodecamp.org/news/ensure-open-source-license-compliance-in-business
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/romain-dancre-doplSDELX7E-unsplash.jpg
tags:
- name: business
  slug: business
- name: open source
  slug: open-source
seo_title: Comment garantir la conformité des licences open source dans votre entreprise
seo_desc: "If you're using open source code in your operations, you'll want to manage\
  \ things properly or potentially face legal issues, financial penalties, and damage\
  \ to your reputation. \nYou don't need a law degree to avoid problems, but you should\
  \ definitely..."
---

Si vous utilisez du code open source dans vos opérations, vous voudrez gérer les choses correctement ou potentiellement faire face à des problèmes juridiques, des pénalités financières et des dommages à votre réputation. 

Vous n'avez pas besoin d'un diplôme en droit pour éviter les problèmes, mais vous devriez définitivement vous familiariser avec quelques principes de base.

Cet article provient de mon guide d'étude complet pour l'examen LPI Open Source Essentials [cours Udemy](https://www.udemy.com/course/complete-lpi-open-source-essentials-exam-study-guide/?referralCode=05B999CE18EF4D6E243C) et [livre](https://www.amazon.com/dp/B0CK3Q8DCF). Vous pouvez également consulter la version vidéo ici :

%[https://youtu.be/u3zGMRAPAiI]

Nous commencerons par quelques bonnes pratiques :

* Réalisez un inventaire de tous les logiciels open source utilisés dans votre flux de travail commercial, y compris les bibliothèques tierces et les dépendances. Cela vous aidera à identifier les licences et les conditions d'utilisation associées à chaque logiciel. Vous voudrez également mettre en place un système pour suivre les licences et leurs conditions d'utilisation. Cela peut inclure l'utilisation d'outils ou de logiciels qui identifient automatiquement les logiciels open source et leurs licences associées.
* Créez une politique de licence qui décrit les procédures et les directives pour l'utilisation des logiciels open source dans votre flux de travail commercial. Cette politique doit être communiquée à tous les employés et les parties prenantes impliquées dans le processus de développement logiciel.
* Utilisez uniquement des licences open source approuvées qui respectent votre politique de licence. Cela peut vous aider à éviter les problèmes juridiques et à garantir la conformité avec les réglementations.
* Surveillez les changements apportés aux licences de logiciels open source et les mises à jour pour garantir une conformité continue. Cela peut inclure l'abonnement à des notifications ou alertes concernant les changements de licence et la mise à jour de votre inventaire de licences en conséquence.
* Documentez toutes les étapes prises pour garantir la conformité avec les licences open source, y compris les examens de licence, les approbations et les renouvellements. Cette documentation peut vous aider à démontrer la conformité en cas d'audit ou de défi juridique.

Cela semble être beaucoup de travail. Eh bien, vous pourriez envisager de créer un Open Source Program Office. Voyons comment cela fonctionne.

## Open Source Program Offices (OSPO)

Un OSPO est une unité organisationnelle ou une équipe au sein d'une entreprise ou d'une organisation qui est responsable de la gestion des logiciels open source et de leur utilisation au sein de l'organisation.

Un OSPO aide les organisations à gérer efficacement l'utilisation des logiciels open source en fournissant des directives, des politiques et des procédures qui garantissent la conformité juridique et réglementaire, une utilisation appropriée et une contribution à la communauté open source. 

L'OSPO peut également aider les organisations à établir une direction stratégique pour l'utilisation de l'open source, y compris l'identification des opportunités de collaboration avec d'autres organisations ou la contribution à des initiatives industrielles.

Typiquement, un OSPO est responsable de veiller à ce que l'organisation respecte les termes des licences open source, y compris la compréhension des obligations de licence, le suivi de l'utilisation des licences et la gestion des risques de conformité. Il travaillera également à :

* Établir des relations avec la communauté open source, contribuer à des projets et promouvoir les contributions internes aux projets open source
* Développer et mettre en œuvre des politiques et des cadres de gouvernance qui guident l'utilisation des logiciels open source par l'organisation
* Développer et exécuter des plans stratégiques pour l'utilisation des logiciels open source au sein de l'organisation
* Fournir une formation et une éducation aux employés et aux parties prenantes sur l'utilisation des logiciels open source, y compris la conformité, la gouvernance et l'engagement communautaire.

Il existe des outils commerciaux utiles qui peuvent aider à simplifier l'administration de vos ressources logicielles.

## Software Package Data Exchanges (SPDX)

Un Software Package Data Exchange, par exemple, est un format standard pour échanger des données liées aux packages logiciels, y compris les licences open source, les droits d'auteur et d'autres informations connexes. 

SPDX est destiné à simplifier le partage d'informations entre les développeurs, les fournisseurs de logiciels et d'autres parties prenantes dans la chaîne d'approvisionnement logicielle. SPDX fournit un langage commun pour décrire les packages logiciels et leurs licences associées, facilitant la compréhension des conditions d'utilisation et la conformité aux obligations de licence.

Le but principal de SPDX est de promouvoir la conformité des licences et de faciliter la gestion des logiciels open source. SPDX permet aux développeurs et aux organisations d'identifier facilement les composants logiciels open source dans leurs produits logiciels et de suivre les obligations de licence associées à chaque composant.

## Le Software Bill of Materials

Un Software Bill of Materials (SBOM) est une liste de tous les composants et dépendances qui constituent une application ou un système logiciel. Le SBOM fournit des informations sur les composants du logiciel, tels que les bibliothèques open source, les composants logiciels commerciaux et le code propriétaire. 

L'objectif d'un SBOM est d'améliorer la transparence et la responsabilité dans les chaînes d'approvisionnement logicielles en fournissant un inventaire détaillé des composants logiciels utilisés dans un produit.

Un SBOM inclut généralement des informations sur la version, la licence et l'origine de chaque composant. Un SBOM peut aider à identifier les vulnérabilités de sécurité dans un système logiciel. En fournissant une liste complète de tous les composants logiciels, les développeurs et les équipes de sécurité peuvent plus facilement identifier et traiter les risques de sécurité. 

Un SBOM peut également aider à garantir la conformité avec les licences open source et d'autres exigences légales en fournissant des informations sur les licences associées à chaque composant. Et un SBOM peut aider à gérer les risques de la chaîne d'approvisionnement en fournissant une visibilité sur les composants logiciels utilisés dans un produit. En sachant quels composants sont utilisés et d'où ils proviennent, les entreprises peuvent plus facilement évaluer les risques associés à chaque composant et prendre des décisions éclairées sur leur utilisation.

Nous devrions également prendre le temps de parler des avocats. Ou, au moins, des choses qui pourraient exciter les avocats. Par quoi je veux dire que les modèles économiques open source peuvent comporter des risques juridiques, y compris des risques liés à la responsabilité du produit et aux réglementations d'exportation. Il est important pour les entreprises qui utilisent ou distribuent des logiciels open source de comprendre ces risques et de prendre des mesures appropriées pour les gérer.

## Responsabilité du produit

La responsabilité du produit est un concept juridique qui rend les fabricants ou distributeurs de produits responsables de tout préjudice causé aux consommateurs par des défauts dans les produits. Lorsqu'une entreprise utilise ou distribue des logiciels open source dans le cadre de ses produits, elle assume la responsabilité de tout défaut dans le logiciel qui pourrait causer un préjudice aux consommateurs. Cela pourrait entraîner des réclamations juridiques pour responsabilité du produit, ce qui peut être coûteux et dommageable pour la réputation de l'entreprise.

Pour gérer les risques de responsabilité du produit associés aux logiciels open source, les entreprises doivent mettre en œuvre des processus efficaces d'assurance qualité pour garantir que le logiciel est exempt de défauts et répond aux normes de l'industrie. Les entreprises doivent également travailler en étroite collaboration avec leurs équipes juridiques pour comprendre les implications juridiques de l'utilisation et de la distribution de logiciels open source, y compris les risques potentiels de responsabilité du produit.

Les réglementations d'exportation sont un autre domaine de préoccupation pour les entreprises qui utilisent ou distribuent des logiciels open source. Les réglementations d'exportation sont des lois et des réglementations qui régissent l'exportation de biens et de technologies d'un pays à un autre. Ces réglementations peuvent restreindre l'exportation de certains types de technologies ou exiger que les entreprises obtiennent des licences ou des certifications avant d'exporter certains types de produits.

Comme toute autre technologie, les logiciels open source peuvent être soumis à des réglementations d'exportation. Les entreprises qui utilisent ou distribuent des logiciels open source doivent être conscientes de ces réglementations et s'assurer que leur utilisation et leur distribution de logiciels open source respectent toutes les lois et réglementations applicables.

## Fusions et acquisitions

Une autre chose juridique : les fusions et acquisitions peuvent avoir un impact significatif sur l'utilisation des logiciels open source au sein des organisations. Lorsque deux entreprises fusionnent ou qu'une entreprise en acquiert une autre, elles peuvent avoir des approches différentes de l'utilisation des logiciels open source et des politiques et pratiques différentes pour gérer les licences et la conformité open source. Cela peut créer des défis et des risques liés à l'intégration des logiciels open source.

Un impact potentiel est que l'entreprise acquéreuse peut devoir effectuer une diligence raisonnable pour comprendre les pratiques de licence et de conformité open source de l'entreprise acquise. Cela peut être un processus complexe et long, surtout si l'entreprise acquise possède un portefeuille logiciel large et diversifié. L'entreprise fusionnée peut également devoir concilier différentes approches des licences et de la conformité open source. Par exemple, si une entreprise a une approche plus permissive des licences open source que l'autre, l'entreprise fusionnée peut devoir développer une nouvelle politique ou approche qui prend en compte les deux approches.

Les fusions et acquisitions peuvent également avoir un impact sur l'utilisation des logiciels open source en termes de développement de produits et d'innovation. Par exemple, si l'entreprise acquéreuse possède une pile technologique ou un processus de développement différent de celui de l'entreprise acquise, elle peut devoir intégrer ou remplacer les composants open source utilisés par l'entreprise acquise. Cela peut entraîner des retards et des coûts supplémentaires.

Et n'oubliez pas que les fusions et acquisitions peuvent également avoir un impact sur la communauté open source. Si une entreprise qui est un contributeur actif à un projet open source est acquise, la nouvelle entreprise peut changer son approche du projet ou réduire ses contributions. Cela peut avoir un impact négatif sur le projet et la communauté qui le soutient.

## Conclusion

En résumé ? Construire des logiciels peut être amusant et rentable et peut changer la vie des gens de manière positive. Mais, si vous n'êtes pas prudent, cela peut également vous causer beaucoup de problèmes. 

Prenez donc le temps de vous éduquer sur vos responsabilités commerciales et de conformité. 

_Cet article provient de mon cours_ [_Complete LPI_](https://www.udemy.com/course/complete-lpi-open-source-essentials-exam-study-guide/?referralCode=05B999CE18EF4D6E243C) Open Source _Essentials Study Guide_. _Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_