---
title: Principe du moindre privilège – Définition et signification en cybersécurité
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2022-11-30T18:23:15.000Z'
originalURL: https://freecodecamp.org/news/principle-of-lease-privilege-meaning-cybersecurity
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cover.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Principe du moindre privilège – Définition et signification en cybersécurité
seo_desc: 'Information technology has made a profound impact on our lives over the
  last three decades. It has helped us create global businesses, transform industries,
  and build powerful connections.

  But it has also led to increased risks in security and privac...'
---

La technologie de l'information a eu un impact profond sur nos vies au cours des trois dernières décennies. Elle nous a aidés à créer des entreprises mondiales, à transformer des industries et à établir des connexions puissantes.

Mais elle a également conduit à une augmentation des risques en matière de sécurité et de confidentialité. Les particuliers et les entreprises sont vulnérables aux cyberattaques plus que jamais. Les récentes violations de données (et la faillite éventuelle) de diverses entreprises nous ont montré l'importance de disposer de mécanismes de défense cyber solides.

Étant donné le coût des équipes de cybersécurité internes, la plupart des petites entreprises sont exposées à un risque de violation de données. Comme l'a dit l'ancien directeur du FBI Robert S. Mueller, « Il n'existe que deux types d'entreprises : celles qui ont été piratées et celles qui le seront ».

Alors, quelle est la solution évolutive et rentable que les entreprises peuvent commencer à mettre en œuvre ? Nous pouvons commencer par une : le Principe du moindre privilège.

## Qu'est-ce que le Principe du moindre privilège ?

Le principe du moindre privilège (PoLP) est la pratique consistant à limiter l'accès aux ressources pour les membres d'une organisation. En termes simples, si quelqu'un n'a pas besoin d'accéder à une ressource, il ne devrait pas y avoir accès.

Malgré cette déclaration logique, le PoLP est rarement mis en œuvre. Chaque personne dans une organisation ne devrait avoir que suffisamment de permissions pour accomplir ses fonctions de travail particulières. Ni moins, ni plus.

Peu importe le niveau de compétence ou de confiance d'un membre. Le principe du moindre privilège est l'ingrédient vital pour la sécurité d'une entreprise. Avec les gouvernements insistant pour que les violations cyber soient rendues publiques, le bon contrôle d'accès est le seul moyen pour les entreprises de se protéger contre les dommages monétaires et réputationnels.

## Comment mettre en œuvre le Principe du moindre privilège

Alors, comment une organisation peut-elle mettre en œuvre le PoLP ? Voici cinq façons de commencer.

### Gestion des accès basée sur les rôles

Gérer l'accès pour les utilisateurs individuels est un défi en soi. Ajouter la sécurité à cela le rend encore plus difficile. C'est là que l'accès basé sur les rôles peut aider à accomplir ces deux objectifs.

Les membres de l'organisation peuvent être regroupés en classes en fonction de leurs fonctions de travail – par exemple, Développeurs, Administrateurs système et Professionnels des ressources humaines. Chaque groupe peut avoir son propre ensemble de permissions pour les ressources organisationnelles.

Cela rend la mise en œuvre des contrôles d'accès plus évolutive. Ajouter/supprimer des utilisateurs sera une question de les ajouter à leurs groupes respectifs. L'accès basé sur les rôles élimine également le besoin de révoquer l'accès individuel aux services lors des changements de personnel.

### Authentification multifacteur (MFA)

La MFA est une autre façon de mettre en œuvre un accès sécurisé aux services organisationnels. L'utilisation de la MFA rend plus difficile l'utilisation des identifiants des employés pour accéder aux actifs critiques de l'entreprise.

Il existe trois types de méthodes MFA :

* Ce que vous savez (mots de passe, numéros de code PIN)
* Ce que vous avez (badge, authentification par smartphone)
* Ce que vous êtes (empreinte digitale et autres identifiants biométriques)

### Gestion des accès juste-à-temps

Lorsqu'ils traitent avec un grand nombre de personnel, les employeurs ont souvent du mal à activer et désactiver l'accès. Cela peut devenir une vulnérabilité sérieuse si l'accès à un tiers n'est pas désactivé pendant une longue période.

La gestion des accès juste-à-temps permet aux administrateurs d'accorder un accès temporaire aux ressources. Accorder un accès avec une date d'expiration est le meilleur moyen de protéger les ressources, car cela élimine le besoin de supprimer l'accès une fois la fonction de travail terminée.

### Piste d'audit

Une piste d'audit enregistre chaque action effectuée par chaque employé dans une organisation. Il y a de nombreux avantages à utiliser une piste d'audit lorsqu'il s'agit de déployer des mesures de sécurité basées sur le personnel.

Avoir une piste d'audit aide à prévenir les attaques ainsi qu'à retracer les attaques jusqu'à leur source. Lors des attaques d'ingénierie sociale, les employés de niveau inférieur sont plus vulnérables. En cas de violation du compte d'un employé, les entreprises peuvent éviter d'autres escalades en utilisant une piste d'audit bien définie.

### Politiques de sécurité

Avoir un ensemble de politiques de sécurité est vital pour prévenir les cyberattaques. Ces politiques vont des politiques de mots de passe aux politiques de partage de ressources. Avoir un ensemble de politiques de sécurité documentées aidera également les autres membres à prendre des décisions éclairées.

[Voici une excellente liste de politiques de cybersécurité pour commencer](https://securityscorecard.com/blog/cybersecurity-policy-examples).

## Défis de la mise en œuvre du Principe du moindre privilège

Trouver le parfait équilibre entre sécurité et utilisabilité a toujours été un défi pour les entreprises. Voici quelques défis qui surgiront lors de la tentative de mise en œuvre du PoLP.

### Applications héritées

Les applications héritées seront toujours un défi pour tout praticien de la sécurité. Si l'application appartient à un tiers, cela augmente l'effort nécessaire pour sécuriser une entreprise. Si la transition depuis un service hérité est difficile, les entreprises devraient prendre des mesures pour limiter l'accès administrateur aux utilisateurs non-administrateurs.

Vous devriez également mettre à jour les applications vers leurs dernières versions. La plupart des mises à jour logicielles sont des correctifs de sécurité. Même les applications modernes peuvent avoir des vulnérabilités liées à l'accès si elles ne proviennent pas d'un fournisseur de confiance. Il est important de vérifier chaque application avant qu'elles ne soient déployées dans une entreprise.

### Frustration des employés

La mise en œuvre de politiques de sécurité strictes conduira souvent à la frustration des employés. Cela est dû au fait que plus les protocoles de sécurité sont relâchés, plus le travail d'un employé est facile. Malheureusement, cela entraînera la chute de l'organisation, tôt ou tard.

Une formation régulière en cybersécurité peut aider les employés à comprendre l'importance des pratiques de sécurité. Cette formation peut également aider à sensibiliser à la sécurisation des ressources personnelles comme les mobiles et les ordinateurs portables.

### Manque de sensibilisation

Les employés peuvent devenir conscients des risques cyber grâce à la formation, mais cela ne s'applique pas aux fournisseurs et vendeurs. Les fournisseurs tiers portent souvent de grands risques même si les systèmes d'une entreprise sont sécurisés.

Les entreprises peuvent inviter leurs fournisseurs et vendeurs à des programmes de sensibilisation à la cybersécurité. Mais cela ne garantit pas des pratiques sécurisées, ni n'est évolutif. Des politiques de sécurité tierces solides sont un meilleur moyen de mitiger ces risques externes.

## Avantages du Principe du moindre privilège

Lorsqu'il est correctement mis en œuvre, le PoLP peut fournir un bouclier de sécurité solide pour toute entreprise. Voici quelques-uns des avantages.

### Sécurité des données

L'objectif principal du PoLP est d'éliminer l'escalade de privilèges. La plupart des violations commencent à un niveau inférieur et sont ensuite escaladées par des acteurs malveillants. L'utilisation des pratiques PoLP ralentira les attaquants et donne aux défenseurs une chance de se battre.

### Évolutivité sécurisée

Les entreprises peuvent évoluer en toute confiance si des pratiques PoLP solides sont en place. Heureusement, le PoLP multiplie la posture de sécurité d'une organisation à mesure qu'elle évolue vers plus de ressources. Il est également plus facile de mettre en œuvre le PoLP dans des architectures à petite échelle par rapport à une grande entreprise.

### Conformité réglementaire

Selon la nature de l'entreprise, la conformité réglementaire est obligatoire dans la plupart des pays. Le PoLP est un sujet récurrent dans la plupart des exigences de conformité. Cela inclut la [conformité HIPPA](https://compliancy-group.com/what-is-hipaa-compliance/) pour les prestataires de soins de santé, la [conformité PCI-DSS](https://www.imperva.com/learn/data-security/pci-dss-certification/) pour les gestionnaires de paiements, et bien d'autres.

### Risque tiers réduit

Un fournisseur tiers sera toujours un vecteur d'attaque. Étant donné l'influence limitée d'une entreprise sur les pratiques de sécurité du fournisseur, la préparation est essentielle. S'assurer que les pratiques PoLP sont toujours suivies peut aider à atténuer de nombreux risques externes pour une organisation.

### Amélioration de la réponse aux incidents

Dans la plupart des pays, les PDG sont responsables en cas de violation de la sécurité. En cas malheureux d'un incident cyber, les outils PoLP comme les pistes d'audit feront ou défait une entreprise. Identifier et contenir les incidents est primordial pour protéger une entreprise contre des dommages critiques ou même la faillite.

## Incidents réels

* [La violation de sécurité de Target en 2013](https://www.usatoday.com/story/money/2017/05/23/target-pay-185m-2013-data-breach-affected-consumers/102063932/)
—
Target a dû payer 18,5 millions de dollars de dommages après une violation de sécurité. Des pirates ont obtenu l'accès aux systèmes de Target via un fournisseur tiers qui avait accès au réseau de Target.
* [Violation de Solarwinds](https://www.techtarget.com/whatis/feature/SolarWinds-hack-explained-Everything-you-need-to-know)
—
Les attaquants ont obtenu l'accès à l'un des nombreux comptes mondiaux (et entièrement privilégiés) de Solarwinds. Cela a conduit à l'une des plus grandes violations du 21e siècle, affectant même le gouvernement américain.
* [Violation de la NSA par Snowden](https://www.venafi.com/blog/deciphering-how-edward-snowden-breached-the-nsa)
—
Arguablement la violation de sécurité la plus célèbre de tous les temps, Edward Snowden avait un accès de niveau administrateur aux ressources qui lui ont permis de copier 1,7 million de fichiers de la NSA. La NSA a éliminé un certain nombre d'administrateurs système pour améliorer la posture PoLP.

## Résumé

Les entreprises ayant une faible exposition à la cybersécurité négligent souvent les dangers d'une cyberattaque. Les acteurs malveillants peuvent paralyser une entreprise et même faire faillite une entreprise entière.

Le Principe du moindre privilège est la première et la plus importante étape pour sécuriser une organisation. La mise en œuvre du PoLP ne protège pas une organisation contre toutes les cyberattaques, mais l'absence de PoLP la rendra ridiculement facile.

Vous avez aimé cet article ? Rejoignez la **[Newsletter Hebdomadaire Stealth Security](https://stealthsecurity.io/)** et recevez des articles dans votre boîte de réception chaque vendredi. Vous pouvez également [me contacter](https://www.linkedin.com/in/manishmshiva/) sur LinkedIn.