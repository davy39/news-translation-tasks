---
title: Les lois de Schofield en informatique – Ce qu'elles sont et pourquoi vous devriez
  les connaître
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2021-06-03T18:46:12.000Z'
originalURL: https://freecodecamp.org/news/schofields-laws-of-computing
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/schofield-cover-1.jpg
tags:
- name: Application Security
  slug: application-security
- name: best practices
  slug: best-practices
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: Security
  slug: security
seo_title: Les lois de Schofield en informatique – Ce qu'elles sont et pourquoi vous
  devriez les connaître
seo_desc: 'Schofield''s Laws of Computing are principles that anyone who works with
  computers should know. They''re focused on data portability, integrity, and security.

  Jack Schofield was a prolific journalist who wrote for The Guardian and covered
  technology fo...'
---

Les lois de Schofield en informatique sont des principes que toute personne travaillant avec des ordinateurs devrait connaître. Elles se concentrent sur la portabilité, l'intégrité et la sécurité des données.

[Jack Schofield](https://wikipedia.org/wiki/Jack_Schofield_(journalist)) était un journaliste prolifique qui a écrit pour The Guardian et a couvert la technologie pendant près de quatre décennies. Pendant cette période, il a écrit trois articles particuliers intitulés "Les lois de Schofield en informatique".

Jack n'a pas créé ces principes d'un seul coup, mais ils étaient plutôt une accumulation de "découvertes" qu'il avait rencontrées tout au long de sa carrière.

Individuellement, les principes ne sont pas spéciaux ou révolutionnaires – en fait, ils sont assez basiques. Cependant, ce sont des leçons précieuses auxquelles vous devriez adhérer, surtout dans un cadre organisationnel.

## La première loi de Schofield en informatique

> "Ne mettez jamais de données dans un programme à moins de pouvoir voir exactement comment les en sortir." – [Jack Schofield](https://www.theguardian.com/technology/2003/jul/24/onlinesupplement.columnists) (2003)

La première loi de Schofield stipule que lorsque vous dépendez d'une organisation, vous devriez vérifier qu'il sera facile de transférer vos données vers une autre organisation.

Les raisons courantes pour lesquelles vous pourriez vouloir changer de fournisseur pourraient être :

* Un changement dans les conditions de service.

* Une autre entreprise avec une vision différente en prend le contrôle.

* Des hausses de prix ou un passage à un modèle économique moins favorable.

* Le service ferme ou le logiciel devient abandonware.

Par exemple :

* LastPass limitant les utilisateurs gratuits à un type d'appareil. ([Plus d'infos](https://wikipedia.org/wiki/LastPass#Reception))

* ArtStation racheté par Epic Games. ([Plus d'infos](https://wikipedia.org/wiki/Epic_Games#Acquisitions))

* Adobe passant à un modèle économique de logiciel en tant que service. ([Plus d'infos](https://wikipedia.org/wiki/Adobe_Creative_Cloud#Criticism))

* Fermeture de Megaupload et saisie par les autorités. ([Plus d'infos](https://wikipedia.org/wiki/Megaupload#2012_indictments_by_the_United_States))

La portabilité des données est une fonctionnalité essentielle pour les logiciels et les services. C'est la solution principale lorsque vous devez éviter les verrouillages par les fournisseurs ou devez budgétiser des processus de migration coûteux.

### Qu'est-ce que le verrouillage par les fournisseurs ?

Le verrouillage par les fournisseurs se produit lorsque les entreprises lient les utilisateurs à leur logiciel. Elles peuvent mettre en place des pratiques pour ajouter des frictions lors de la migration vers des logiciels concurrents.

L'objectif est de contraindre les utilisateurs à rester, même s'il existe de meilleures options pour eux, en rendant les étapes de départ inconfortables, chronophages ou fastidieuses.

Lorsque vous choisissez un logiciel ou des services à utiliser, vous devrez surveiller de telles pratiques. Cela peut prendre diverses formes :

* Ne pas vous permettre d'exporter des données personnelles ou du contenu généré par l'utilisateur.

* Ne pas permettre aux fichiers d'être exportés vers des formats ouverts ou lisibles par l'homme.

* Rendre le logiciel incompatible avec les normes ouvertes existantes.

### Le droit à la portabilité des données

Le [Règlement général sur la protection des données](https://wikipedia.org/wiki/General_Data_Protection_Regulation) (RGPD) a aidé à cela. Il a conduit des entreprises comme Discord, Instagram et Twitter à ajouter des outils automatisés pour que les utilisateurs puissent exporter leur contenu.

L'article 20 du RGPD est le "droit à la portabilité des données", qui est le droit d'avoir les moyens de transférer vos données personnelles d'un responsable de traitement à un format standard que vous pouvez donner à un autre responsable de traitement.

Malgré le fait que le RGPD soit spécifique aux données personnelles, cela a promu la portabilité des données en général, y compris le contenu généré par l'utilisateur. Bien qu'il soit discutable de savoir à quel point il est facile de faire respecter le RGPD en dehors de l'UE, ces outils sont généralement accessibles aux membres d'autres juridictions également.

Si vous représentez une organisation ou un freelance et que vous êtes responsable du choix des logiciels, gardez cela à l'esprit !

## La deuxième loi de Schofield en informatique

> "Les données n'existent vraiment que si vous en avez au moins deux copies." 
> – [Jack Schofield](https://www.theguardian.com/technology/2008/feb/14/email.yahoo) (2008)

Sauvegarder les données est une corvée que la plupart des individus reportent jusqu'à ce qu'il soit trop tard. Mais heureusement, les organisations se sont avérées un peu plus matures à ce sujet.

La deuxième loi de Schofield en informatique suggère que, à moins d'avoir *au moins* 2 copies de vos données, vous devriez les traiter comme si elles n'existaient pas.

Idéalement, vous devriez conserver les deux copies dans des emplacements physiques différents – et par là, je ne veux pas dire des disques différents, mais idéalement des pays ou des continents différents.

Pour les données en votre possession, comme votre bureau, votre ordinateur portable ou vos clés USB :

* Les appareils ou tout votre inventaire pourraient être perdus ou volés.

* Si vous avez un chiffrement complet du disque, vous pourriez oublier votre mot de passe.

* Votre matériel pourrait tomber en panne, entraînant une perte de données.

* Des catastrophes comme des incendies ou des inondations pourraient détruire tout ce qui se trouve sur place.

Cela pourrait même être dû à une erreur de l'utilisateur. Peu importe votre niveau technique, vous pourriez cliquer sur "Écraser" au lieu de "Enregistrer sous", flasher un système d'exploitation sur le mauvais lecteur, ou un développeur pourrait forcer la poussée vers la mauvaise branche après avoir modifié un commit.

Vous devriez toujours être préparé au scénario qui pourrait entraîner une perte de données. Bien que tout le monde n'ait pas de revenus disponibles, les biens physiques sont généralement faciles à remplacer avec suffisamment d'argent, mais des années de données accumulées sont irrécoverables.

### Les données dans le cloud

La deuxième loi de Schofield ne cible pas seulement les données en votre possession, mais aussi les données que vous conservez dans le cloud. Par exemple, vous devriez stocker votre stockage cloud, vos e-mails et votre contenu multimédia dans un deuxième emplacement également.

Cela est particulièrement important lorsque vous utilisez des services qui ne prennent pas la responsabilité de sauvegarder vos données, ou qui ferment votre compte après une période d'inactivité. Cela est courant avec les entreprises qui fournissent des services vraiment gratuits, sans coût et sans suivi, comme les fournisseurs Nextcloud ou Tutanota.

Ne supposez pas que vos données sont en sécurité simplement parce qu'elles sont dans le cloud. Un exemple récent de cela est l'incendie qui a commencé dans l'un des centres de données d'OVH, entraînant la perte de données. OVH Public Cloud fournit des serveurs non gérés, ce qui signifie que l'utilisateur est responsable de la gestion et de la sauvegarde de ses serveurs. ([Plus d'infos](https://wikipedia.org/wiki/OVHcloud#Incidents))

Il existe également le risque de vulnérabilités qui permettent un accès non autorisé à votre compte.

Par exemple, l'année dernière, des pirates ont obtenu l'accès aux outils administratifs de Twitter, ce qui leur a donné accès à de nombreux comptes de haut niveau. En utilisant de tels outils, il aurait été tout aussi facile de supprimer les publications et les médias précédents. ([Plus d'infos](https://wikipedia.org/wiki/2020_Twitter_account_hijacking))

### Synchronisez vos données

Vous pouvez résoudre certains de ces problèmes en utilisant des solutions qui synchronisent vos données entre votre ordinateur et un serveur. Cela offre une protection contre toute défaillance matérielle ou dommage physique.

Les données qui auraient des conséquences néfastes en cas de perte devraient être chiffrées et synchronisées avec le stockage cloud. Certains logiciels comme Bitwarden ou Thunderbird reposent naturellement sur la synchronisation, donc même si le serveur devait disparaître, vous aurez toujours une copie récente sur votre appareil.

Cependant, la synchronisation ne résout pas tous les problèmes – il est idéal d'avoir également une sauvegarde isolée. La synchronisation enverra automatiquement toutes les modifications, y compris les erreurs de l'utilisateur, ou même les modifications apportées par des logiciels malveillants ou des ransomwares. Avoir des sauvegardes régulières sur stockage froid serait pratique pour des cas comme celui-ci.

## La troisième loi de Schofield en informatique

> "Plus il est facile pour vous d'accéder à vos données, plus il est facile pour quelqu'un d'autre d'accéder à vos données." – [Jack Schofield](https://www.theguardian.com/technology/2008/jul/10/it.security) (2008)

Protéger les données a toujours impliqué de trouver un équilibre entre la sécurité et la commodité. Nous voulons que les données soient faciles à accéder pour nous, mais difficiles à accéder pour les autres.

Ce conflit a conduit à des problèmes de négligence des données.

Lorsque vous mettez des données dans le cloud, vous les rendez automatiquement plus faciles à accéder pour les autres. Votre fournisseur de cloud pourrait avoir des vulnérabilités, quelqu'un pourrait deviner votre mot de passe, ou un employé pourrait devenir voyou et compromettre ou vendre vos données.

Vous pourriez être en mesure de blâmer quelqu'un ou d'obtenir une compensation pour l'incident, mais vos données et potentiellement les données de vos clients sont toujours là, et vous seriez celui qui aurait finalement permis que cela arrive.

Augmenter la sécurité tend à être inconfortable, mais ce sont les inconvénients sur lesquels les autres parient lorsqu'ils cherchent à compromettre des comptes :

* [Attaques par force brute](https://wikipedia.org/wiki/Brute-force_attack) – Pari sur des mots de passe courts, car c'est plus rapide à taper.

* [Bourrage d'identifiants](https://wikipedia.org/wiki/Credential_stuffing) – Pari sur la réutilisation des mots de passe, car c'est plus pratique que de gérer plusieurs.

* [Attaques par dictionnaire](https://wikipedia.org/wiki/Dictionary_attack) – Pari sur des mots de passe logiques, car c'est plus facile à rappeler.

De plus, ces attaques reposent sur le fait que les utilisateurs n'activent pas la 2FA, et que les données de l'autre côté ne sont pas obfusquées ou chiffrées.

Vous ou votre organisation devriez utiliser un gestionnaire de mots de passe, imposer la 2FA sur tous les systèmes, et, lorsque cela est possible, chiffrer les données avant de les envoyer à des serveurs tiers.

Mieux encore, supprimez les données qui ne sont plus pertinentes. Il est toujours préférable d'effacer les données plutôt que de s'inquiéter de les protéger.

Cela pourrait inclure les historiques de chat, les e-mails ou les fichiers contenant des informations confidentielles, des mots de passe de réseaux sociaux, et des données de clients ou d'employés. Surtout s'ils ont des mois ou des années et ne sont plus pertinents. Si vous n'en avez pas besoin, personne d'autre n'en a besoin non plus.

## Conclusion

Ces principes ont été établis il y a plus de 10 ans, et s'appliquent plus que jamais aujourd'hui.

La technologie et les normes ouvertes ont évolué, elles sont donc plus faciles à respecter. Mais avec la croissance de l'infrastructure cloud, nous faisons de plus en plus confiance à des tiers pour nos données. Dans de nombreux cas, nous pouvons être trop à l'aise avec l'endroit où elles sont laissées et qui y a accès.

Malheureusement, Jack Schofield est décédé en mars 2020, mais il a soutenu de nombreuses personnes dans la communauté technologique. J'espère qu'en partageant ses expériences, d'autres pourront continuer à apprendre d'elles.

## Meta

Cet article a été discuté sur The Hedge, un podcast sur la technologie et les affaires dirigé par des ingénieurs réseau. Je recommande de l'écouter si vous avez aimé cela, car leurs contributions et leur expérience réelle ajoutent beaucoup de valeur au sujet.

[Contenu intégré](https://rule11.tech/hedge-116/)