---
title: OWASP API Security Top 10 – Sécurisez vos APIs
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-08-30T19:27:18.000Z'
originalURL: https://freecodecamp.org/news/owasp-api-security-top-10-secure-your-apis
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/owaslp.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: youtube
  slug: youtube
seo_title: OWASP API Security Top 10 – Sécurisez vos APIs
seo_desc: 'The OWASP API Security Top 10 is a standard reference guide highlighting
  the most critical web API vulnerabilities to help developers and organizations understand
  and mitigate potential security threats.

  We just published a course on the freeCodeCamp...'
---

Le OWASP API Security Top 10 est un guide de référence standard mettant en évidence les vulnérabilités les plus critiques des APIs web pour aider les développeurs et les organisations à comprendre et à atténuer les potentielles menaces de sécurité.

Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org qui vous enseignera chaque risque de sécurité et les techniques pour fortifier vos APIs contre les potentielles menaces.

Corey Ball a développé ce cours. Il est devenu l'un des principaux experts en sécurité des APIs et est l'auteur de Hacking APIs.

Voici les sections de ce cours :

### Objectifs du cours

* Qu'est-ce que le OWASP API Security Top 10
* Qu'est-ce que l'OWASP
* Comment le Top 10 est-il compilé ?
* Mappé aux sources externes
* Mises à jour du OWASP API Security Top 10

### Le Top 10

* API1:2023 - Autorisation de niveau objet cassée
* API2:2023 - Authentification cassée
* API3:2023 - Autorisation de niveau propriété d'objet cassée
* API4:2023 - Consommation de ressources non restreinte
* API5:2023 - Autorisation de niveau fonction cassée
* API6:2023 - Accès non restreint aux flux métier sensibles
* API7:2023 - Falsification de requête côté serveur
* API8:2023 - Mauvaise configuration de sécurité
* API9:2023 - Gestion incorrecte de l'inventaire
* API10:2023 - Consommation non sécurisée des APIs

### Au-delà du Top 10

* Injections
* Journalisation et surveillance insuffisantes
* Faille de logique métier

Regardez le cours complet sur [la chaîne YouTube de freeCodeCamp.org](https://youtu.be/YYe0FdfdgDU) (1,5 heure de visionnage).

%[https://youtu.be/YYe0FdfdgDU]

## Transcription

(générée automatiquement)

Le OWASP API Security Top 10 est un guide de référence standard mettant en évidence les vulnérabilités les plus critiques des APIs web pour aider les développeurs et les organisations à comprendre et à atténuer les potentielles menaces de sécurité.

Dans ce cours, vous apprendrez chaque risque de sécurité et des techniques pour fortifier vos APIs contre les potentielles menaces.

Corey Ball a développé ce cours.

Il est consultant en cybersécurité et un expert de premier plan en sécurité des APIs.

Il est donc la personne idéale pour vous apprendre à sécuriser vos APIs.

Bonjour, communauté freeCodeCamp et bienvenue à l'APIsec University et ce cours sur le OWASP API Security Top 10 et au-delà.

Je m'appelle Dan Barahona.

Je suis le cofondateur de l'APIsec University, et pendant les 90 prochaines minutes, vous apprendrez tout sur le OWASP API Security Top 10, mis à jour en 2023, et nous ajouterons même quelques sujets bonus supplémentaires vraiment importants à connaître.

Votre instructeur pour le cours est mon bon ami, Corey Ball, auteur du livre Hacking APIs et expert bien reconnu dans le domaine de la sécurité des APIs.

Je vous invite à découvrir tous nos cours gratuits sur APIsec University, y compris un cours pratique sur les tests d'intrusion des APIs, un cours d'introduction sur les fondamentaux de la sécurité des APIs, ce cours ici sur le OWASP API Top 10, ainsi qu'un cours sur la conformité PCI, un cours sur la documentation des APIs, et bien d'autres à venir.

Tous les cours sur notre site incluent des quiz pour évaluer vos connaissances, et si vous terminez tout et réussissez le quiz final, nous vous délivrerons un certificat et un badge pour reconnaître votre accomplissement, que vous pourrez également afficher sur votre profil LinkedIn.

Merci encore d'avoir regardé et j'espère que vous apprécierez le cours.

Bienvenue dans le OWASP API Security Top 10 et au-delà.

Dans ce cours, nous plongerons dans les dernières mises à jour du OWASP API Security Top 10, et discuterons d'autres considérations de sécurité significatives au-delà du Top 10.

La première édition du API Security Top 10 a été publiée en 2019, et maintenant OWASP a officiellement publié la version 2023.

Les APIs étant un composant critique du monde numérique moderne, cette liste est d'une importance capitale.

Ce cours met en lumière les vulnérabilités de sécurité des APIs les plus courantes et vise à aider à éduquer la communauté des constructeurs, des briseurs et des défenseurs.

Le cours vous aidera à identifier et à analyser les faiblesses les plus courantes qui affectent les interfaces de programmation d'applications web modernes, ou APIs.

À la fin de ce cours, vous devriez avoir une compréhension des différentes vulnérabilités associées aux APIs, des vecteurs d'attaque impliqués, et de l'impact technique et de la vulnérabilité exploitée.

Alors, à qui s'adresse ce cours ? Ce cours est idéal pour toute personne impliquée dans l'économie des APIs.

Il vise à améliorer les compétences et les connaissances des chasseurs de primes de bogues, des développeurs, des testeurs d'intrusion, des dirigeants organisationnels, et de toute autre personne intéressée par l'apprentissage de la sécurité des APIs.

Avant de suivre ce cours, vous devriez être familiarisé avec les fondamentaux de la sécurité des APIs.

Si vous souhaitez en savoir plus à ce sujet, consultez notre cours sur les fondamentaux de la sécurité des APIs.

Alors, comment fonctionne ce cours ? Lisez, regardez et ou écoutez le contenu fourni dans les modules du cours.

Il est fortement recommandé de prendre des notes, d'explorer les ressources recommandées, de suivre les supports de cours et de compléter les quiz à la fin de chaque module.

Le contenu présenté dans la vidéo devrait être étroitement aligné avec le contenu écrit.

Les vidéos offrent des alternatives visuelles et audibles pour consommer le contenu de ce cours.

Quiz Pendant le cours, des quiz seront utilisés pour valider vos connaissances.

Les quiz sont des tests à choix multiples basés sur les connaissances, basés sur le contenu discuté dans le module donné.

Le cours OWASP API Security Top 10 et au-delà est conçu pour être un cours exigeant qui fixe un niveau élevé.

Pour réussir un quiz ou une évaluation, vous devez répondre correctement à cent pour cent des questions.

La réussite de tous les quiz entraînera l'obtention d'un certificat de réussite.

Ce cours est entièrement gratuit, et vous pouvez obtenir le certificat de réussite en réussissant tous les modules du cours et en réussissant tous les quiz.

Ceux qui souhaitent certifier leurs connaissances peuvent passer l'examen du cours.

L'examen est une évaluation des connaissances de votre capacité à analyser les APIs et à trouver des vulnérabilités.

Les étudiants qui réussissent l'examen obtiendront la certification Certified API Security Analyst ou CASA.

Mise en forme Veuillez noter que tout le contenu en italique sous les sections désignées OWASP est directement issu du OWASP API Security Top 10 2023.

Ce contenu est attribué à l'équipe du projet OWASP API Security et aux contributeurs du projet OWASP API Security.

Toutes les autres sources seront directement référencées.

Aucune modification n'a été apportée au contenu.

Salut à tous.

Brève introduction.

Je m'appelle Corey Ball.

Je suis l'auteur de Hacking APIs, éditeur technique de Black Hat GraphQL, et contributeur au OWASP API Security Top 10 2023.

Je suis également le Chief Hacking Officer pour APIsec University et Senior Manager of Penetration Testing chez Moss Adams.

J'ai plus de 13 ans d'expérience dans le domaine de l'IT et de la cybersécurité dans plusieurs industries.

En plus d'une licence en anglais et philosophie de Sac State, je possède plusieurs certifications dont l'OSCP, CCISO, CISSP, et plusieurs autres.

J'espère que vous apprécierez ce cours.

L'objectif de ce cours est d'aider les étudiants à devenir des professionnels de la sécurité des APIs, et à être capables d'identifier et de réduire les risques de sécurité liés aux APIs.

OWASP API Security Top 10 et au-delà vise à améliorer les compétences des chasseurs de primes de bogues, des développeurs, des testeurs d'intrusion, des dirigeants organisationnels, et de toute autre personne intéressée par l'apprentissage de la sécurité des APIs.

Les objectifs du cours incluent l'introduction à OWASP, le projet de sécurité des APIs, et les changements de la version 2019 à la version 2023.

Cela devrait aider à préparer les étudiants à passer l'examen Certified API Security Analyst ou CASA.

Développer une solide base dans les risques de sécurité des APIs suivants : Autorisation de niveau objet cassée, Authentification cassée, Autorisation de niveau propriété d'objet cassée, Consommation de ressources non restreinte, Autorisation de niveau fonction cassée, Accès non restreint aux flux métier sensibles, Falsification de requête côté serveur, Mauvaise configuration de sécurité, Gestion incorrecte de l'inventaire, Consommation non sécurisée des APIs.

En plus de cela, cela vise à aider à sécuriser les APIs de l'internet et à prévenir les violations de données liées aux APIs.

Enfin, ce cours vise à aider à préparer les étudiants avec des ressources supplémentaires pour un apprentissage et une croissance continus en matière de sécurité des APIs.

Le projet Open Web Application Security, ou OWASP, est une fondation à but non lucratif qui a été créée pour aider à améliorer la sécurité des applications.

La fondation OWASP a été lancée le 1er décembre 2001 et est surtout connue pour sa liste Top 10, ses outils open source et ses autres projets de sécurité.

Le OWASP API Security Top 10 est une liste des risques de sécurité les plus critiques pour les interfaces de programmation d'applications.

Les fondateurs du projet incluent Erez Yalon et Inon Shkedy.

Le OWASP API Security Top 10 a été initialement publié en décembre 2019 et a été motivé par plusieurs facteurs clés.

Le premier était la montée rapide des APIs.

Les APIs alimentent le flux de la ressource la plus précieuse du monde, qui est la donnée.

Une entreprise n'a plus besoin de se spécialiser dans tous les aspects de la création de logiciels.

Au lieu de cela, elles peuvent utiliser les fonctionnalités de logiciels partagés par d'autres entreprises et organisations.

Historiquement, le problème avec cela était la nature déconnectée des différents langages de programmation, les interfaces de programmation d'applications web ont permis une méthode commune pour consommer ou fournir des données à travers l'internet.

Depuis l'adoption généralisée des APIs web, les organisations ont été en mesure de tirer parti de la fonctionnalité.

D'autres applications.

Au lieu de devoir développer des logiciels personnalisés pour les cartes, le GPS, le traitement des paiements, l'authentification, la communication, et bien plus encore, les développeurs peuvent utiliser des APIs pour utiliser la fonctionnalité d'autres applications qui se spécialisent dans ce domaine donné.

Les APIs sont un important facilitateur commercial, ce qui explique l'adoption rapide à l'échelle mondiale.

Deuxièmement, un manque majeur de sécurité.

Le facteur suivant qui a aggravé les effets des deux autres est le fait que les outils et techniques du passé n'étaient pas efficaces pour détecter les vulnérabilités liées aux APIs.

Les outils et techniques utilisés pour les programmes de gestion des vulnérabilités des entreprises, les scanners d'applications web et les outils traditionnels de surveillance de la sécurité du réseau n'étaient pas conçus pour gérer les défis uniques posés par les APIs.

En conséquence, de nombreuses organisations n'étaient pas suffisamment préparées pour se défendre contre les attaques d'APIs, les laissant vulnérables aux violations de données.

Troisièmement, un nouveau vecteur d'attaque principal.

Souvent, en ce qui concerne l'adoption rapide de nouvelles technologies, la sécurité est une réflexion après coup.

Les APIs ne font pas exception.

L'adoption rapide des APIs a conduit à un nouveau vecteur d'attaque qui expose les données et la fonctionnalité des applications.

Les APIs faisant face à l'internet public contournent souvent toutes les mesures de sécurité qui avaient évolué avec les entreprises au cours des dernières décennies.

Un attaquant n'a plus besoin de passer par la chaîne de destruction cyber classique du MITRE en contournant le pare-feu, en obtenant l'accès au réseau, en pivotant vers le système contenant les données, puis en trouvant un moyen d'exfiltrer ces données.

Au lieu de cela, un attaquant peut utiliser une API non sécurisée et avoir un accès direct à ces données sensibles.

En réponse à l'adoption massive des APIs, aux lacunes de sécurité introduites par les fournisseurs d'APIs, et à la nouvelle vague d'incidents de sécurité liés aux APIs, le projet OWASP API Security a publié sa liste Top 10.

La liste Top 10 axée sur les APIs fournit un ensemble complet de directives, de meilleures pratiques et d'outils pour aider les organisations à sécuriser leurs APIs et à se protéger contre les menaces liées aux APIs.

Le projet OWASP API Security est devenu une ressource largement reconnue et respectée pour les professionnels de la sécurité et a aidé à sensibiliser à l'importance de la sécurité des APIs.

Comment le Top 10 est-il compilé ? Comme décrit par Paulo Silva, chef de projet OWASP API Security, la liste OWASP API Security Top 10 2023 est établie par l'équipe du projet sur la base de recherches internes, de données publiques, de plateformes de primes et de nouvelles.

Puisque le projet n'a reçu aucune donnée pendant l'appel à données pendant la fenêtre de deux mois à la fin de 2022, la liste Top 10 a été compilée sur la base des recherches de l'équipe du projet.

Ce n'était pas quelque chose de nouveau ou de différent pour le projet, car comme l'a déclaré Silva, c'est ce qui a été fait en 2019.

Sans ensemble de données reçu de la communauté, l'équipe du projet OWASP a dû compiler des données basées sur des divulgations publiques de plateformes de primes de bogues et d'incidents de sécurité des APIs qui ont fait la une des nouvelles.

Bien que cet ensemble de données ne soit pas aussi idéal que les données compilées directement à partir de tests de centaines de milliers de points de terminaison à travers l'internet, il représente un échantillon de faiblesses réelles des APIs.

Certains problèmes potentiels avec l'application de ces données incluent les programmes de primes de bogues qui incitent certains types de découvertes plutôt que d'autres.

Les programmes de primes de bogues attirent des participants qui représentent un petit échantillon des APIs qui sont réellement dans la nature.

Les incidents dignes d'intérêt laissent souvent les chercheurs en sécurité sans détails techniques spécifiques.

Évidemment, les incidents dignes d'intérêt n'incluent pas toutes les violations et incidents de sécurité qui ne sont pas signalés ou rendus publics.

Cela étant, il y a des leçons à tirer et des risques à connaître basés sur les primes de bogues, les comptes rendus et les incidents de sécurité rendus publics.

Si vous êtes intéressé à en savoir plus sur les sources, voici une liste de sites web courants pour approfondir la recherche sur les primes de bogues.

En plus de ceux-ci, joint à ce module se trouve un extrait JSON de PentesterLand qui contient tous les comptes rendus documentés sur les APIs.

Compilation de comptes rendus de PentesterLand, activité de piratage de HackerOne, comptes rendus de primes de bogues Awesome, tous les liens sont dans le contenu ci-dessous.

De plus, dans le contenu du cours se trouve une liste de certains des incidents d'APIs les plus médiatisés au cours des cinq dernières années, y compris des violations de données et des fuites de l'USPS, Optus, T-Mobile et Toyota.

La liste OWASP API Security Top 10 contient des groupes communs des risques de sécurité les plus critiques à surveiller basés sur ces sources.

Les risques de sécurité des APIs OWASP sont associés à des références à des sources externes.

Ces sources incluent les CWEs, ou Common Weakness Enumeration, d'autres projets OAS, et les directives du National Institute of Standards and Technology, ou NIST.

La plupart des références impliquent des CWEs.

Les CWEs sont une liste de vulnérabilités courantes des logiciels et du matériel développée par la communauté et hébergée par MITRE.

Chaque CWE est identifié par un identifiant unique ou CWEID.

Cet identifiant peut être utilisé pour se référer à une vulnérabilité spécifique.

Consultez le tableau complet des sources externes dans le matériel du cours ci-dessous.

Comprendre les sources externes et comment elles sont associées à un risque donné du OWASP API Security Top 10 vous aidera à obtenir des informations supplémentaires.

Tout au long du cours, des sources externes seront fournies pour les risques du OWASP API Security Top 10.

Ces ressources vous seront fournies pour vous aider à plonger aussi profondément que vous le souhaitez dans le sujet de la sécurité des APIs.

Nous approfondirons ces sujets dans les modules ultérieurs.

Dans la section suivante, nous passerons en revue les mises à jour de la liste Top 10 de 2019 à 2023.

Depuis la publication du OWASP API Security Top 10 en 2019, l'utilisation des APIs a augmenté.

Les violations de données liées aux APIs ont continué et de nouvelles technologies d'APIs ont émergé.

Tout cela a joué un rôle dans la nécessité d'une version mise à jour de la liste Top 10 du projet de sécurité des APIs.

Depuis le Top 10 de 2019, plusieurs événements ont démontré l'importance de maintenir la liste à jour et pertinente.

Les attaques contre les APIs sont constamment en hausse.

Akamai a signalé avoir vu près de 114 millions d'attaques contre des APIs en une seule journée en 2021.

La valeur marchande mondiale des APIs était évaluée à 2,2 milliards de dollars en 2021 et était prévue pour atteindre 41,5 milliards d'ici 2031.

C'est un taux de croissance de 20 fois en 10 ans.

En 2022, Postman comptait plus de 46 millions de collections Postman, et GitHub comptait 3 millions de dépôts liés aux APIs.

Les APIs continuent d'être rapidement adoptées et les enjeux financiers continuent de grimper.

Le projet OWASP API Security a mis à jour la liste Top 10 pour répondre à certains des changements dans les tendances d'attaque qui ont émergé depuis la version précédente.

Inon Shkedy, chef de projet OWASP API Security, a déclaré que la version OWASP API Top 10 2023 est différente de la version 2019.

"Nous aspirons à suivre les tendances de sécurité pertinentes pour les APIs qui se sont développées ces dernières années.

Si vous essayez de pirater ou de protéger une API développée il y a cinq ans, il serait plus judicieux de se référer à la liste de 2019." À un niveau élevé, lorsque vous comparez le Top 10 de 2019 à celui de 2023, vous voyez que deux risques précédents ont été retirés de la liste, trois sont restés exactement les mêmes, quatre ont été mis à jour, et cinq des risques de 2023 sont nouveaux.

Les deux éléments qui ont été retirés incluaient l'injection et la journalisation et la surveillance insuffisantes.

Ces deux risques n'ont pas été complètement atténués et résolus, mais l'importance de nouveaux risques émergents les a poussés au-delà du Top 10.

La journalisation et la surveillance sont un risque classique du Top 10 de l'OWASP, mais ce n'est pas un élément qui est représenté dans les violations ou les primes de bogues divulguées.

Les attaques par injection sont toujours présentes et de nombreuses APIs web y sont encore sensibles, mais l'adoption de pare-feu d'applications web et la mise en œuvre d'autres techniques d'atténuation ont réduit l'occurrence d'injections notables d'APIs.

Il y avait trois catégories qui sont restées sur la liste.

Autorisation de niveau objet cassée ou BOLA, Autorisation de niveau fonction cassée, ou BFLA, et Mauvaise configuration de sécurité.

BOLA et BFLA sont toujours parmi les risques d'APIs les plus courants et représentent de nombreuses violations dans les divulgations de primes de bogues.

Les APIs continuent d'avoir des problèmes graves en matière de risques d'autorisation.

La catégorie Mauvaise configuration de sécurité contient une large gamme de mauvaises configurations possibles qui peuvent affecter les APIs.

En d'autres termes, cette catégorie est peu susceptible de quitter le Top 10 car elle est un fourre-tout pour de nombreuses vulnérabilités des APIs.

Quatre catégories ont été renommées.

Le renommage de ces catégories a aidé à simplifier les catégories de risques et à apporter une attention supplémentaire au problème en question.

L'authentification de l'utilisateur cassée est désormais devenue Authentification cassée.

Cette simplification a éliminé l'utilisateur et attire désormais une attention supplémentaire sur l'authentification de l'API dans son ensemble.

La gestion incorrecte des actifs est devenue Gestion incorrecte de l'inventaire.

Ce changement a probablement été fait pour mieux s'aligner sur la terminologie de l'industrie et pour couvrir une gamme plus large de ressources.

Le terme Actifs pourrait ne faire référence qu'à des éléments tangibles valorisés par une organisation, tandis que le terme Inventaire pourrait faire référence à un ensemble plus large de ressources.

Il y avait un total de cinq catégories qui ont été ajoutées au OWASP API Security Top 10 2023 qui n'étaient pas sur la version 2019.

La falsification de requête côté serveur et la consommation non sécurisée des APIs sont complètement nouvelles et n'avaient pas de représentation précédente sur la liste OWASP API Security Top 10 2019.

La falsification de requête côté serveur était représentée sur la liste OWASP Top 10 2021 et a été ajoutée à cette liste sur la base des résultats de l'enquête plutôt que par l'occurrence d'incidents.

Les nouvelles catégories de risques restantes incluaient l'autorisation de niveau propriété d'objet cassée, ou BOPLA, la consommation de ressources non restreinte, et l'accès non restreint aux flux métier sensibles, chacune contenant des éléments de la liste 2019.

Par exemple, BOPLA est une combinaison d'exposition excessive de données et d'affectation massive, et nous approfondirons chacun de ces sujets plus tard dans le cours.

Associées à chaque catégorie de risque de sécurité des APIs OWASP se trouvent des évaluations de risque.

Les évaluations de risque étaient basées sur la méthodologie d'évaluation de risque OWASP.

Le projet fait maintenant référence au cadre d'évaluation de risque OWASP.

Dans le contenu écrit du cours, il y a un tableau démontrant les évaluations de risque utilisées pour le projet de sécurité des APIs OWASP à partir du PDF OWASP API Security Top 10 2019.

L'un de ces facteurs pourrait affecter de manière significative la probabilité globale qu'un attaquant trouve et exploite une vulnérabilité particulière.

Cette évaluation ne prend pas en compte l'impact réel sur une entreprise spécifique.

Le score de risque doit être déterminé par l'organisation donnée, comme le déclare l'équipe du projet.

Le but du OWASP API Security Top 10 n'est pas de faire cette analyse de risque pour vous.

En d'autres termes, le but du OWASP API Security Top 10 n'était pas de réaliser une analyse de risque spécifique pour une organisation donnée, mais de fournir une ligne directrice pour que les organisations prennent en compte les facteurs de risque.

Dans le contenu du cours, vous pouvez voir un tableau contenant les changements apportés aux évaluations de risque de 2019 et 2023.

L'équation classique pour le risque est la probabilité multipliée par l'impact avec chaque score de risque.

L'équipe du projet OWASP API Security a laissé l'impact comme une valeur relative à déterminer par l'entreprise.

De plus, l'équipe du projet inclut une note avec ces scores indiquant que la probabilité de ces scores n'est pas prise en compte.

Ce à quoi nous sommes laissés sont des valeurs qui représentent l'exploitabilité globale, y compris la complexité, l'exploitabilité, la prévalence des faiblesses, la détectabilité des faiblesses et l'impact technique.

Notez que le score global ne correspond pas à un score de risque car des facteurs significatifs tels que l'impact commercial et la probabilité ne sont pas pris en compte.

API1:2023 Autorisation de niveau objet cassée, ou BOLA, est l'une des vulnérabilités les plus prévalentes et graves pour les APIs.

Les vulnérabilités BOLA se produisent lorsqu'un fournisseur d'API ne dispose pas de contrôles suffisants pour faire respecter l'autorisation.

En d'autres termes, les utilisateurs d'API ne devraient avoir accès qu'aux ressources sensibles qui leur appartiennent.

Lorsque BOLA est présent, un attaquant pourra accéder aux données sensibles d'autres utilisateurs.

La description du vecteur d'attaque OWASP indique : "Les attaquants peuvent exploiter les points de terminaison d'API qui sont vulnérables à une autorisation de niveau objet cassée en manipulant l'ID d'un objet qui est envoyé dans la requête.

Les IDs d'objet peuvent être n'importe quoi, des entiers séquentiels, des UUIDs ou des chaînes génériques.

Quelle que soit le type de données, ils sont faciles à identifier dans la cible de la requête, soit par le chemin, soit par un paramètre de requête de chaîne de requête, des en-têtes de requête, ou même comme une partie de la charge utile de la requête." La description de la faiblesse de sécurité OWASP indique : "Cela a été l'attaque la plus courante et la plus impactante sur les APIs.

Les mécanismes d'autorisation et de contrôle d'accès dans les applications web modernes sont complexes et répandus.

Même si l'application met en œuvre une infrastructure appropriée pour les vérifications d'autorisation, les développeurs peuvent oublier d'utiliser ces vérifications avant d'accéder à un objet sensible.

La détection du contrôle d'accès n'est généralement pas adaptée aux tests statiques ou dynamiques automatisés." La description de l'impact OWASP indique : "L'accès non autorisé peut entraîner la divulgation de données à des parties non autorisées, la perte de données ou la manipulation de données.

L'accès non autorisé aux objets peut également entraîner la prise de contrôle totale du compte." Si un point de terminaison d'API n'a pas de contrôles d'accès suffisants, il ne effectuera pas de vérifications pour s'assurer que les utilisateurs ne peuvent accéder qu'à leurs propres ressources.

Lorsque ces contrôles sont manquants, l'utilisateur A pourra obtenir les ressources de l'utilisateur B via des requêtes API.

Les APIs utilisent une sorte de valeur comme des noms ou des nombres pour identifier divers objets.

Lorsque qu'un attaquant découvre l'ID de ressource d'une API, il tentera d'obtenir les ressources lorsqu'il n'est pas authentifié ou authentifié en tant qu'utilisateur différent.

Par exemple, imaginez qu'un utilisateur authentifié Bruce envoie une requête GET à https://herohospital.com/api/v3/users?id=2727 et reçoit une réponse JSON avec ses données, cela ne pose aucun problème.

Bruce devrait pouvoir accéder aux informations de Bruce.

Cependant, si Bruce est capable d'accéder aux informations d'un autre utilisateur, alors une vulnérabilité BOLA serait présente.

Cette faiblesse peut être testée en utilisant d'autres IDs de ressources à la place de 2727.

Supposons que Bruce soit capable d'obtenir des informations sur un autre utilisateur en envoyant une requête à : https://herohospital.com/api/v3/users?id=2728, et reçoit une réponse sur Harvey Dent et son trouble dissociatif de l'identité, alors il y aurait un problème.

En supposant que Bruce utilise toujours son autorisation pour accéder à ces données, ce serait une indication claire que l'API est vulnérable à BOLA.

BOLA n'est pas toujours aussi simple que cet exemple car il y a de la flexibilité dans la manière dont les ressources sont provisionnées et demandées d'une API à l'autre.

Le contenu écrit du cours contient plusieurs exemples de la manière dont les ressources API peuvent être demandées et attaquées.

Dans ces exemples, des tests peuvent être effectués en remplaçant les IDs de ressources en gras par d'autres nombres ou mots.

Bien sûr, dans une requête POST, la ressource pourrait également être demandée dans le corps de la POST.

Si l'utilisateur A peut accéder avec succès aux informations de n'importe quel autre utilisateur, alors il y a une vulnérabilité présente.

Les vulnérabilités BOLA sont les vulnérabilités API les plus courantes et sont facilement exploitables et nécessitent un faible niveau de compétences techniques pour les découvrir.

BOLA peut se présenter sous de nombreuses formes selon la manière dont les ressources sont organisées.

Comme vous pouvez le voir dans le contenu du cours écrit, les ressources peuvent être organisées par un utilisateur, par groupe, ou par une combinaison des deux.

Dans tous ces cas, seuls ceux ayant la permission appropriée devraient être autorisés à récupérer leurs ressources.

Les mesures préventives OWASP indiquent : Afin d'améliorer la sécurité des APIs, il est important de mettre en œuvre des contrôles d'autorisation robustes.

Ces contrôles doivent prendre en compte les politiques des utilisateurs et les hiérarchies de contrôle d'accès basées sur les rôles.

L'objectif principal doit être de s'assurer que les utilisateurs authentifiés n'ont accès qu'aux ressources auxquelles ils sont autorisés à accéder.

L'utilisation d'IDs de ressources moins prévisibles peut augmenter le défi pour un utilisateur ou un attaquant de deviner l'ID de ressource d'autres utilisateurs.

Les développeurs doivent effectuer des tests qui testent spécifiquement les contrôles d'autorisation.

Mettre en œuvre un mécanisme d'autorisation approprié qui repose sur les politiques des utilisateurs et la hiérarchie.

Utiliser le mécanisme d'autorisation pour vérifier si l'utilisateur connecté a accès pour effectuer l'action demandée sur l'enregistrement dans chaque fonction qui utilise une entrée du client pour accéder à l'enregistrement dans la base de données.

Préférer l'utilisation de valeurs aléatoires et imprévisibles, telles que des GUIDS pour les IDs d'enregistrements.

Écrire des tests pour évaluer la vulnérabilité du mécanisme d'autorisation.

Ne pas déployer de changements qui font échouer les tests.

Consultez le contenu écrit du cours pour des ressources supplémentaires sur BOLA.

API2:2023, Authentification cassée, fait référence à toute faiblesse dans le processus d'authentification de l'API.

Toutes les APIs qui contiennent des informations sensibles doivent avoir un mécanisme pour authentifier les utilisateurs.

L'authentification est le processus utilisé pour vérifier l'identité d'un utilisateur d'API.

Qu'il s'agisse d'une personne, d'un appareil ou d'un système.

En d'autres termes, l'authentification est le processus de vérification qu'une entité est bien celle qu'elle prétend être.

Ce processus de vérification est généralement effectué à l'aide d'une combinaison de nom d'utilisateur et de mot de passe, d'un jeton et/ou d'une authentification multifactorielle.

Les vulnérabilités liées à l'authentification se produisent généralement lorsqu'un fournisseur d'API ne met pas en œuvre un mécanisme d'authentification fort ou met en œuvre un processus d'authentification de manière incorrecte.

La description du vecteur d'attaque OWASP pour cela indique que "Le mécanisme d'authentification est une cible facile pour les attaquants puisqu'il est exposé à tous.

Bien que des compétences techniques plus avancées puissent être nécessaires pour exploiter certains problèmes d'authentification, des outils d'exploitation sont généralement disponibles." La description de la faiblesse de sécurité OWASP indique "Les malentendus des ingénieurs logiciels et de sécurité concernant l'authentification, les limites et la complexité inhérente de la mise en œuvre rendent les problèmes d'authentification prévalents.

Les méthodologies de détection de l'authentification cassée sont disponibles et faciles à créer." La description des impacts OWASP indique "Les attaquants peuvent prendre le contrôle complet des comptes d'autres utilisateurs dans le système, lire leurs données personnelles et effectuer des actions sensibles en leur nom.

Les systèmes sont peu susceptibles de pouvoir distinguer les actions des attaquants de celles des utilisateurs légitimes." L'authentification cassée continue d'être un problème de sécurité significatif en raison de politiques de mots de passe médiocres, de mécanismes d'authentification faibles et de mauvaises configurations.

L'authentification des APIs est un processus complexe qui est couramment trouvé avec la plupart des APIs et est nécessairement exposé.

L'impact de l'authentification cassée peut conduire un attaquant à prendre le contrôle des comptes utilisateurs, à compromettre les données personnelles et à effectuer des actions sensibles comme modifier les données de santé de quelqu'un d'autre.

Le processus d'authentification est souvent l'une des premières lignes de défense pour les APIs, et lorsque ce mécanisme est vulnérable, cela peut conduire à une violation de données.

Une politique de mots de passe faible ne protège pas suffisamment les comptes utilisateurs en imposant la création et la gestion de mots de passe forts.

Cela permet aux utilisateurs de créer des mots de passe simples, permet les tentatives de force brute contre les comptes utilisateurs et permet aux utilisateurs de changer leur mot de passe sans demander de confirmation de mot de passe.

De plus, cela permet aux utilisateurs de changer leur email sans demander de confirmation de mot de passe.

Les politiques de mots de passe faibles divulguent également des jetons ou des mots de passe dans l'URL.

Il manque d'authentification pour les requêtes sensibles.

Et en ce qui concerne les requêtes GraphQL, les politiques de mots de passe faibles permettraient de nombreuses tentatives d'authentification dans une seule requête.

Le bourrage d'identifiants est un type d'attaque contre l'authentification où un grand nombre de combinaisons de nom d'utilisateur et de mot de passe sont tentées.

Les identifiants utilisés dans ces types d'attaques sont généralement collectés à partir de violations de données.

Ce type d'attaque permet aux utilisateurs de forcer brutalement de nombreuses combinaisons de nom d'utilisateur et de mot de passe différentes sans restrictions.

Les jetons prévisibles font référence à tout jeton obtenu par le biais d'un processus d'authentification de génération de jeton faible.

Les jetons faibles peuvent facilement être devinés, déduits ou calculés par un attaquant.

Cela serait un problème si une API utilise des jetons incrémentiels ou devinables pour les IDs.

Les JWT sont couramment utilisés pour les processus d'authentification et d'autorisation des APIs.

JWT signifie JSON Web Token.

Les JWT offrent aux développeurs la flexibilité de personnaliser l'algorithme utilisé pour signer le jeton, la clé et le secret utilisés et les informations utilisées dans la charge utile.

Cette personnalisation permet beaucoup de place pour que des mauvaises configurations de sécurité se produisent.

Celles-ci incluent les fournisseurs d'API qui acceptent des jetons JWT non signés, les fournisseurs d'API qui ne vérifient pas les expirations des JWT, les fournisseurs d'API qui divulguent des informations sensibles dans la charge utile JWT encodée, et si le JWT est signé avec une clé faible.

L'authentification des APIs peut être un système complexe qui inclut plusieurs processus avec beaucoup de place pour l'échec.

Il y a quelques décennies, l'expert en sécurité Bruce Schneier a déclaré : "l'avenir des systèmes numériques est la complexité, et la complexité est le pire ennemi de la sécurité." Comme nous le savons des six contraintes des APIs REST, les APIs RESTful sont conçues pour être sans état.

Pour être sans état, les fournisseurs d'APIs ne devraient pas avoir besoin de se souvenir du consommateur d'une requête à l'autre.

Pour que cette contrainte fonctionne, les APIs nécessitent souvent que les utilisateurs subissent un processus d'inscription pour obtenir un jeton unique.

Le jeton généré est ensuite utilisé dans les requêtes ultérieures pour l'authentification et l'autorisation.

En conséquence, le processus d'inscription utilisé pour obtenir un jeton d'API, la gestion des jetons et le système qui génère le jeton pourraient tous avoir leur propre ensemble de faiblesses si le processus de génération de jetons ne repose pas sur un haut niveau d'aléatoire, ou d'entropie, il y a une chance qu'un attaquant puisse créer son propre jeton ou détourner le jeton d'un autre utilisateur.

Les autres processus d'authentification qui pourraient avoir leur propre ensemble de vulnérabilités incluent des aspects du système d'inscription, comme les fonctionnalités de réinitialisation de mot de passe et d'authentification multifactorielle.

Par exemple, imaginez une fonctionnalité de réinitialisation de mot de passe vous demandant de fournir une adresse email et un code à six chiffres pour réinitialiser votre mot de passe.

Si l'API vous permettait de faire autant de requêtes que vous le souhaitez, vous n'auriez besoin de faire que 1 million de requêtes pour deviner le code et réinitialiser le mot de passe de n'importe quel utilisateur.

Un code à quatre chiffres nécessiterait seulement 10 000 requêtes.

Comme il est indiqué dans les mesures préventives OWASP, assurez-vous de connaître tous les flux possibles pour vous authentifier auprès de l'API.

Demandez à vos ingénieurs quels flux vous avez manqués.

Lisez à propos de vos mécanismes d'authentification.

Assurez-vous de comprendre ce qu'ils sont et comment ils sont utilisés.

OAuth n'est pas une authentification et les clés API non plus.

Ne réinventez pas la roue en matière d'authentification, de génération de jetons ou de stockage de mots de passe, utilisez les standards.

Les points de terminaison de récupération d'identifiants et de mot de passe oublié doivent être traités comme des points de terminaison de connexion en termes de force brute, de limitation de débit et de protections contre le verrouillage.

Exigez une réauthentification pour les opérations sensibles, y compris le changement de compte sur notre adresse email et le numéro de téléphone multifactoriel.

Utilisez la feuille de triche OWASP API Authentication.

Vous pouvez la trouver dans le contenu écrit.

Là où c'est possible, mettez en œuvre l'authentification multifactorielle.

Mettez en œuvre des mécanismes anti-force brute pour atténuer le bourrage d'identifiants, les attaques par dictionnaire et les attaques par force brute sur vos points de terminaison d'authentification.

Ce mécanisme doit être plus strict que les mécanismes de limitation de débit réguliers sur vos APIs.

Mettez en œuvre des mécanismes de verrouillage de compte pour prévenir les attaques par force brute contre des utilisateurs spécifiques.

Mettez en œuvre des vérifications de mot de passe faible.

Les clés API ne doivent pas être utilisées pour l'authentification.

Elles ne doivent être utilisées que pour l'authentification du client API.

Consultez le contenu écrit du cours pour des ressources supplémentaires sur l'authentification cassée.

API3:2023 Autorisation de niveau propriété d'objet cassée, ou BOPLA, est une combinaison de deux éléments du OWASP API Security Top 10 2019 : Exposition excessive de données et Affectation massive.

L'exposition excessive de données se produit lorsqu'un fournisseur d'API répond à une requête avec un objet de données entier.

Habituellement, un fournisseur d'API filtrera l'objet de données pour ne retourner que ce qui est demandé.

Lorsque l'objet de données est partagé sans être filtré, il y a un risque accru d'exposer des informations sensibles.

L'affectation massive est une faiblesse qui permet à l'entrée utilisateur de modifier des propriétés d'objet sensibles.

Si, par exemple, une API utilise une propriété spéciale pour créer des comptes administrateur, seuls les utilisateurs autorisés devraient pouvoir faire des requêtes qui modifient avec succès ces propriétés administratives.

Si aucune restriction n'est en place, alors un attaquant pourrait élever ses privilèges et effectuer des actions administratives en modifiant ces propriétés.

Ces deux vulnérabilités impliquaient des problèmes avec l'autorisation des propriétés d'objet, donc elles sont combinées sous le nouveau titre d'Autorisation de niveau propriété d'objet cassée.

Comme il est indiqué dans la description du vecteur d'attaque OWASP : Les APIs tendent à exposer des points de terminaison qui retournent toutes les propriétés des objets.

Cela est particulièrement valable pour les APIs REST.

Pour d'autres protocoles tels que GraphQL, cela peut nécessiter des requêtes élaborées pour spécifier quelles propriétés doivent être retournées.

L'identification de ces propriétés supplémentaires qui peuvent être manipulées nécessite plus d'efforts, mais il existe quelques outils automatisés disponibles pour aider dans cette tâche.

La description de la faiblesse de sécurité OWASP indique que l'inspection des réponses de l'API est suffisante pour identifier les informations sensibles dans les objets retournés, les représentations.

Le fuzzing est généralement utilisé pour identifier des propriétés cachées supplémentaires.

Savoir si elles peuvent être modifiées est une question de création d'une requête API et d'analyse de la réponse.

Une analyse des effets secondaires peut être nécessaire si la propriété cible n'est pas retournée dans la réponse de l'API.

La description des impacts OWASP indique que l'accès non autorisé à des propriétés d'objet privées ou sensibles peut entraîner la divulgation de données, la perte de données ou la corruption de données.

Dans certaines circonstances, l'accès non autorisé à des propriétés d'objet peut entraîner une escalade de privilèges ou une prise de contrôle partielle à complète du compte.

Comme précédemment indiqué, l'Autorisation de niveau propriété d'objet cassée, ou BOPLA, est une combinaison de l'Affectation massive et de l'Exposition excessive de données.

Dans les notes de publication de 2023, le projet de sécurité indique que ces deux vulnérabilités ont été combinées en se concentrant sur la cause racine commune, l'échec de la validation de l'autorisation au niveau des propriétés de l'objet.

Le projet de sécurité des APIs OWASP indique également qu'un point de terminaison d'API est vulnérable si soit le point de terminaison d'API expose des propriétés d'un objet qui sont considérées comme sensibles et ne devraient pas être lues par l'utilisateur, ce qui est une exposition excessive de données, soit le point de terminaison d'API permet à un utilisateur de changer, d'ajouter ou de supprimer la valeur d'une propriété sensible d'un objet, à laquelle l'utilisateur ne devrait pas pouvoir accéder, ce qui est une affectation massive.

L'exposition excessive de données se produit lorsqu'un point de terminaison d'API répond avec plus d'informations que nécessaire pour satisfaire une requête.

Cela se produit souvent dans les cas où le fournisseur s'attend à ce que le consommateur de l'API filtre les résultats.

Lorsque qu'un consommateur demande des informations spécifiques, le fournisseur peut répondre avec toutes sortes d'informations, en supposant que le consommateur supprimera ensuite les données dont il n'a pas besoin de la réponse.

Lorsque cette vulnérabilité est présente, cela peut être équivalent à demander à quelqu'un son nom et à ce qu'il réponde avec son nom, sa date de naissance, son adresse email, son numéro de téléphone et l'identification de toutes les autres personnes qu'il connaît.

Par exemple, si un consommateur d'API demande des informations pour son compte utilisateur et reçoit également des informations sur d'autres comptes utilisateurs, l'API expose des données excessives.

Consultez le contenu écrit pour un exemple de vulnérabilité d'exposition excessive de données.

L'exposition excessive de données est une vulnérabilité d'API très difficile à détecter avec des scanners automatisés.

De plus, cette vulnérabilité contournera souvent tous les contrôles de sécurité en place pour protéger les informations sensibles et transmettra des données sensibles à un attaquant simplement parce qu'ils utilisent l'API.

Pour détecter l'exposition excessive de données, les fournisseurs d'API doivent tester les points de terminaison d'API et examiner les informations envoyées dans la réponse.

L'affectation massive se produit lorsqu'un consommateur d'API inclut plus de paramètres dans sa requête que ce que l'application avait prévu, et l'application ajoute ces paramètres aux variables de code ou aux objets internes.

Dans cette situation, un consommateur pourrait être en mesure de modifier les propriétés d'objet ou d'élever les privilèges.

Par exemple, une application pourrait avoir une fonctionnalité de mise à jour de compte que l'utilisateur devrait utiliser uniquement pour mettre à jour son nom d'utilisateur, son mot de passe et son adresse.

Si le consommateur peut inclure des paramètres supplémentaires dans la requête liés à son compte, tels que le niveau de privilège du compte, ou des informations sensibles comme un solde de compte, et que l'application accepte ces paramètres sans les vérifier par rapport à la liste blanche des actions autorisées, le consommateur pourrait tirer parti de cette faiblesse pour changer ces valeurs.

Imaginez qu'une API est appelée pour créer un compte avec des paramètres pour l'utilisateur et le mot de passe.

L'utilisateur pourrait être hapi_hacker, le mot de passe pourrait être GreatPassword123.

En lisant la documentation de l'API concernant le processus de création de compte, un attaquant pourrait découvrir qu'il existe une propriété supplémentaire, qui est un admin que le fournisseur de l'API utilise pour créer des comptes administratifs.

Un attaquant pourrait ajouter cela à une requête et définir la valeur sur "true".

Si l'API ne nettoie pas l'entrée de la requête, elle est vulnérable à l'affectation massive et un attaquant pourrait utiliser la requête pour créer son propre compte admin.

Sur le backend, l'application web vulnérable ajoutera l'attribut clé-valeur {isAdmin: true} à l'objet utilisateur, et rendra l'utilisateur équivalent à un administrateur pour cette application.

Les mesures préventives OWASP indiquent que lorsque vous exposez un objet en utilisant un point de terminaison d'API, assurez-vous toujours que l'utilisateur doit avoir accès aux propriétés de l'objet que vous exposez.

Évitez d'utiliser des méthodes génériques telles que to_json() et to_string().

Au lieu de cela, sélectionnez des propriétés d'objet spécifiques que vous souhaitez spécifiquement retourner.

Si possible, évitez d'utiliser des fonctions qui lient automatiquement l'entrée du client aux variables de code, aux objets internes ou aux propriétés d'objet.

Autorisez les changements uniquement aux propriétés de l'objet qui doivent être mises à jour par le client.

Mettez en œuvre un mécanisme de validation de réponse basé sur un schéma comme couche de sécurité supplémentaire.

Dans le cadre de ce mécanisme, définissez et appliquez les données retournées par toutes les méthodes d'API.

Gardez les structures de données de retour au strict minimum selon les exigences fonctionnelles de l'entreprise pour le point de terminaison.

Consultez le contenu écrit du cours pour des ressources supplémentaires sur BOPLA.

API4:2023 Consommation de ressources non restreinte est un problème d'API où le fournisseur de l'API n'a pas de garde-fous en place pour prévenir l'utilisation excessive de leur API.

Lorsque qu'il n'y a pas de restrictions pour la consommation de ressources, le fournisseur de l'API pourrait devenir une victime d'une attaque par déni de service, ou subir des coûts financiers inutiles.

La consommation de ressources non restreinte est une version mise à jour de API4:2019, Manque de ressources et limitation de débit.

La description du vecteur d'attaque OWASP indique que l'exploitation nécessite des requêtes API simples.

Plusieurs requêtes concurrentes peuvent être effectuées à partir d'un seul ordinateur local ou par des ressources de calcul en nuage.

La plupart des outils automatisés disponibles sont conçus pour causer un déni de service via des charges élevées de trafic impactant le taux de service de l'API.

La description de la faiblesse de sécurité OWASP indique qu'il est courant de trouver des APIs qui ne limitent pas les interactions des clients ou la consommation de ressources.

Des requêtes API élaborées, telles que celles incluant des paramètres qui contrôlent le nombre de ressources à retourner et effectuant une analyse de la longueur du temps de statut de réponse, devraient permettre l'identification du problème.

La même chose est valable pour les opérations par lots, bien que les agents de menace n'aient pas de visibilité sur l'impact des coûts, cela peut être déduit en fonction de l'activité commerciale du fournisseur de services.

La description des impacts OWASP indique que l'exploitation peut conduire à un déni de service dû à l'épuisement des ressources, mais elle peut également conduire à une augmentation des coûts opérationnels, tels que ceux liés à l'infrastructure en raison d'une demande de CPU plus élevée, d'une augmentation des besoins en stockage cloud, etc.

Le projet de sécurité des APIs OWASP indique qu'une API est vulnérable si au moins l'une des limites suivantes est manquante ou définie de manière inappropriée, soit trop basse soit trop élevée.

Délais d'exécution, mémoire allouable maximale, nombre maximal de descripteurs de fichiers, nombre maximal de processus, taille maximale de fichier de téléchargement, nombre d'opérations à effectuer dans une seule requête client API avec des choses comme le traitement par lots GraphQL, nombre d'enregistrements par page à retourner dans une seule réponse de requête, et limite de dépenses du fournisseur de services tiers.

Chaque requête API a un coût technique et financier lorsque les fournisseurs d'API n'imposent pas de limitations sur la consommation de ressources, il y a un risque accru de déni de service, de déni de service distribué, de coûts financiers inutiles et de dégradation de la qualité de service pour les autres utilisateurs.

De plus, la limitation de débit joue un rôle important dans la monétisation et la disponibilité des APIs.

De nombreux fournisseurs d'API monétisent leurs APIs en limitant les requêtes et en permettant aux clients payants de demander plus d'informations.

RapidAPI, par exemple, permet à certains fournisseurs d'API d'avoir également une infrastructure qui s'adapte automatiquement au nombre de requêtes API.

Dans ces cas, un nombre illimité de requêtes entraînerait une augmentation significative et facilement évitable des coûts d'infrastructure.

Les mesures préventives OWASP indiquent que Docker facilite la limitation de la mémoire, du CPU, du nombre de redémarrages, des descripteurs de fichiers et des processus.

Mettez en œuvre une limite sur la fréquence à laquelle un client peut appeler l'API dans un laps de temps défini.

Informez le client lorsque la limite est dépassée en fournissant le numéro de limite et l'heure à laquelle la limite sera réinitialisée.

Ajoutez une validation côté serveur appropriée pour les paramètres de chaîne de requête et de corps de requête, spécifiquement celle qui contrôle le nombre d'enregistrements à retourner dans la réponse.

Définissez et appliquez la taille maximale des données sur tous les paramètres et charges utiles entrants, tels que la longueur maximale pour les chaînes et le nombre maximal d'éléments dans les tableaux.

Consultez le contenu écrit du cours pour des ressources supplémentaires sur la consommation de ressources non restreinte.

API5:2023, Autorisation de niveau fonction cassée, ou BFLA, est une vulnérabilité où les fonctions de l'API ont des contrôles d'accès insuffisants.

Là où BOLA concerne l'accès aux données, BFLA concerne la modification ou la suppression de ces données.

De plus, une API vulnérable permettrait à un attaquant d'effectuer des actions d'autres rôles, y compris des actions administratives.

Pour illustrer, une API fintech vulnérable à BOLA permettrait à un attaquant de voir ce qu'il y a dans le compte bancaire d'un autre utilisateur, tandis que la même API vulnérable à BFLA permettrait à un attaquant de transférer des fonds des comptes d'autres utilisateurs vers le sien.

La description du vecteur d'attaque OWASP indique que "l'exploitation nécessite que l'attaquant envoie des appels API légitimes à un point de terminaison d'API auquel ils ne devraient pas avoir accès en tant qu'utilisateur anonyme ou utilisateur non privilégié régulier.

Les points de terminaison exposés seront facilement exploités." La description de la faiblesse de sécurité OWASP indique que "les vérifications d'autorisation pour une fonction ou une ressource sont généralement gérées via la configuration ou le niveau de code.

La mise en œuvre de vérifications appropriées peut être une tâche confuse puisque les applications modernes peuvent contenir de nombreux types de rôles, de groupes et de hiérarchies d'utilisateurs complexes.

Il est plus facile de découvrir ces failles dans les APIs puisque les APIs sont plus structurées et l'accès à différentes fonctions est plus prévisible." La description des impacts OWASP indique que "de telles failles permettent aux attaquants d'accéder à des fonctionnalités non autorisées.

Les fonctions administratives sont des cibles clés pour ce type d'attaque et peuvent entraîner la divulgation de données, la perte de données ou la corruption de données.

En fin de compte, cela peut entraîner une interruption de service." L'autorisation de niveau fonction cassée, ou BFLA, est une vulnérabilité où un utilisateur d'un niveau de privilège peut utiliser la fonctionnalité de l'API d'un autre utilisateur, groupe d'utilisateurs ou niveau de privilège.

Les fournisseurs d'API auront souvent différents niveaux de privilèges pour différents types de comptes, tels que les utilisateurs publics, les marchands, les partenaires, les fournisseurs, les administrateurs, et ainsi de suite.

BFLA peut être exploité pour une utilisation non autorisée de fonctions latérales ou d'un groupe de privilèges similaires, ou il pourrait être exploité pour une escalade de privilèges, où un attaquant peut utiliser les fonctions d'un groupe plus privilégié.

Les fonctions API particulièrement intéressantes à accéder incluent celles qui traitent des informations sensibles, des ressources appartenant à un autre groupe, et des fonctionnalités administratives, comme la gestion des comptes utilisateurs.

Si une API a différents niveaux de privilèges, elle peut utiliser différents points de terminaison pour effectuer ces actions privilégiées.

Par exemple, une banque pourrait utiliser /{userid}/account/balance comme point de terminaison pour un utilisateur souhaitant accéder à ses informations de compte, puis utiliser /admin/account/{userid} comme point de terminaison pour un administrateur ayant besoin d'accéder aux informations de compte utilisateur.

Si l'application n'a pas mis en œuvre correctement les contrôles d'accès, un attaquant pourra effectuer des actions administratives et prendre le contrôle d'un compte.

Une API n'utilisera pas toujours des points de terminaison administratifs pour les fonctionnalités administratives.

Au lieu de cela, la fonctionnalité pourrait être basée sur différentes méthodes de requête HTTP comme GET, POST, PUT et DELETE.

Si un fournisseur ne restreint pas les méthodes HTTP, ou verbes, un attaquant peut simplement faire une requête non autorisée avec une méthode différente, ce qui pourrait indiquer une vulnérabilité BFLA.

Lors du test de BFLA, recherchez toute fonctionnalité qu'un attaquant pourrait utiliser à son avantage.

Ces fonctions incluent, sans s'y limiter, la modification des comptes utilisateurs, la suppression des ressources utilisateurs et l'accès à des points de terminaison restreints.

Par exemple, si une API donnait aux partenaires la possibilité d'ajouter de nouveaux utilisateurs au groupe partenaire, mais ne restreignait pas cette fonctionnalité au groupe spécifique, n'importe quel utilisateur pourrait s'ajouter à n'importe quel groupe.

De plus, si un attaquant s'ajoutait à un groupe, il y a de fortes chances qu'il puisse accéder aux ressources sensibles de ce groupe.

Jetez un coup d'œil au contenu écrit du cours pour un exemple d'attaque BFLA.

Les mesures préventives OWASP indiquent que "votre application doit avoir un module d'autorisation cohérent et facile à analyser qui est appelé depuis toutes vos fonctions métier.

Fréquemment, une telle protection est fournie par un ou plusieurs composants externes au code de l'application.

Les mécanismes d'application doivent refuser tout accès par défaut, nécessitant des autorisations explicites à des rôles spécifiques pour l'accès à chaque fonction.

Passez en revue vos points de terminaison d'API contre les failles d'autorisation au niveau des fonctions, tout en gardant à l'esprit la logique métier de l'application et la hiérarchie des groupes.

Assurez-vous que tous vos contrôleurs administratifs héritent d'un contrôleur abstrait administratif qui met en œuvre des vérifications d'autorisation basées sur le groupe ou le rôle de l'utilisateur.

Assurez-vous que les fonctions administratives à l'intérieur d'un contrôleur régulier mettent en œuvre des vérifications d'autorisation basées sur le groupe et le rôle de l'utilisateur." Consultez le contenu écrit du cours pour des ressources supplémentaires sur l'autorisation de niveau fonction cassée.

API6:2023, Accès non restreint aux flux métier sensibles représente le risque qu'un attaquant puisse identifier et exploiter des flux de travail pilotés par API.

Si vulnérable, un attaquant pourra exploiter la structure des requêtes API d'une organisation pour entraver d'autres utilisateurs.

Cette entrave pourrait prendre la forme de spam vers d'autres utilisateurs, d'épuisement du stock d'articles très recherchés, ou d'empêcher d'autres utilisateurs d'utiliser la fonctionnalité attendue de l'application.

C'est une nouvelle addition à la liste du Top 10 de 2023.

La description du vecteur d'attaque OWASP indique que "l'exploitation implique généralement de comprendre le modèle commercial soutenu par l'API, de trouver des flux commerciaux sensibles et d'automatiser l'accès à ces flux, causant ainsi des dommages à l'entreprise." La description de la faiblesse de sécurité indique que "le manque d'une vue holistique de l'API afin de soutenir pleinement les exigences commerciales tend à contribuer à la prévalence de ce problème.

Les attaquants identifient manuellement les ressources ou points de terminaison impliqués dans le flux de travail cible et comment ils fonctionnent ensemble.

Si des mécanismes d'atténuation sont déjà en place, les attaquants doivent trouver un moyen de les contourner." La description des impacts OWASP indique que "en général, aucun impact technique n'est attendu.

L'exploitation pourrait nuire à l'entreprise de différentes manières.

Par exemple, empêcher les utilisateurs légitimes d'acheter un produit ou entraîner une inflation dans l'économie interne d'un jeu.

En ce qui concerne les APIs, un flux est une série de requêtes et de réponses qui mènent à une opération.

Si, par exemple, un flux d'achat pour une application web ne restreint pas l'accès à un processus d'achat, alors un revendeur pourrait automatiser les requêtes pour vider instantanément le stock d'un article.

C'est là que des mécanismes comme un test de Turing public complètement automatisé pour distinguer les ordinateurs et les humains, ou mieux connu sous le nom de CAPTCHA, entrent en jeu.

Si un flux a un mécanisme de capture qui nécessite une interaction humaine, alors la requête automatisée pourrait être interrompue et ralentir les achats automatisés.

Consultez le matériel de cours écrit pour un exemple de flux API utilisé pour aider à construire un bot de notification pour la PS5.

Les clients et/ou les revendeurs en compétition pour acheter la PS5 utiliseraient des flux API pour soit compléter les achats dès que de nouveaux stocks étaient disponibles, soit alerter lors des mises à jour de stock.

Dans l'exemple, un flux API a été utilisé pour vérifier automatiquement les mises à jour de stock et envoyer des alertes par email.

Les mesures préventives OWASP indiquent que la planification de l'atténuation doit être effectuée en deux couches, commerciale et technique.

L'entreprise doit identifier les flux commerciaux qui pourraient nuire à l'entreprise s'ils sont utilisés de manière excessive.

L'ingénierie doit choisir le bon mécanisme de protection pour atténuer le risque commercial.

Certains des mécanismes de protection sont plus simples tandis que d'autres sont plus difficiles à mettre en œuvre.

Les méthodes suivantes sont utilisées pour ralentir les menaces automatisées.

L'empreinte digitale de l'appareil.

Refuser le service aux appareils clients inattendus, tend à faire en sorte que les acteurs de la menace utilisent des solutions plus sophistiquées, donc plus coûteuses pour eux.

Ensuite, la détection humaine utilisant soit CAPTCHA soit des solutions biométriques plus avancées.

Les motifs non humains.

Analyser le flux utilisateur pour détecter les motifs non humains.

Par exemple, l'utilisateur a accédé aux fonctions d'ajout au panier et de finalisation de l'achat en moins d'une seconde.

Envisagez de bloquer les adresses IP des nœuds de sortie Tor et des proxys bien connus.

Sécurisez et limitez l'accès aux APIs qui sont consommées directement par des machines.

Elles tendent à être une cible facile pour les attaquants car elles n'implémentent souvent pas tous les mécanismes de protection requis.

Consultez le contenu écrit du cours pour des ressources supplémentaires sur l'accès non restreint aux flux métier sensibles.

API7:2023, Falsification de requête côté serveur est une vulnérabilité qui se produit lorsqu'un utilisateur est en mesure de contrôler les ressources distantes récupérées par une application.

Un attaquant peut utiliser une API pour fournir sa propre entrée sous la forme d'une URL afin de contrôler les ressources distantes qui sont récupérées par le serveur cible.

Un attaquant pourrait fournir des URLs qui exposent des données privées, scannent le réseau interne de la cible, ou compromettent la cible par l'exécution de code à distance.

SSRF est également le numéro 10 sur la liste OWASP Top 10 2021 et est une menace croissante pour les APIs.

La description du vecteur d'attaque OWASP indique que "l'exploitation nécessite que l'attaquant trouve un point de terminaison d'API qui accède à un URI fourni par le client.

En général, le SSRF de base, lorsque la réponse est retournée par l'attaquant, est plus facile à exploiter que le SSRF aveugle, dans lequel l'attaquant n'a aucun retour sur le succès ou non de l'attaque." La description de la faiblesse de sécurité OWASP indique que "les concepts modernes dans le développement d'applications encouragent les développeurs à accéder aux URIs fournis par le client.

Le manque de validation, ou une validation incorrecte de ces URIs sont des problèmes courants.

Une analyse régulière des requêtes et réponses API sera nécessaire pour détecter le problème.

Lorsque la réponse n'est pas retournée, la détection de la vulnérabilité nécessite plus d'efforts et de créativité." La description des impacts OWASP indique que "une exploitation réussie pourrait conduire à l'énumération des services internes, à la divulgation d'informations, au contournement des pare-feu, ou à d'autres mécanismes de sécurité.

Dans certains cas, cela peut conduire à un déni de service ou à l'utilisation du serveur comme proxy pour cacher des activités malveillantes." SSRF est une vulnérabilité qui se produit lorsqu'une application récupère des ressources distantes sans valider l'entrée utilisateur.

Lorsque qu'un attaquant a le contrôle sur les ressources qu'un serveur demande, il peut alors accéder à des données sensibles, ou pire, compromettre complètement un hôte vulnérable.

L'impact de cette vulnérabilité est qu'un attaquant serait en mesure de tirer parti d'un serveur cible pour effectuer et traiter des requêtes qu'il fournit.

Notez que les paiements de primes de bogues pour SSRF sont déterminés en fonction de l'impact qui peut être démontré avec une preuve de concept.

Plus l'impact démontré est élevé, plus la prime est élevée.

Il existe deux types généraux de SSRF qui valent la peine d'être notés.

SSRF In-Band et SSRF Out-of-Band, également connu sous le nom de Blind SSRF.

In-Band SSRF signifie que le serveur répond avec les ressources spécifiées par l'utilisateur final.

Si l'attaquant spécifie une charge utile telle que google.com à un serveur avec une vulnérabilité In-Band SSRF, le serveur ferait la requête à google.com puis répondrait à l'attaquant avec les informations servies par google.com.

Blind SSRF se produit lorsque l'attaquant fournit une URL et le serveur fait la requête, mais le serveur n'envoie pas les informations de cette URL spécifiée à l'attaquant.

Dans le cas de Blind SSRF, un attaquant aurait besoin de contrôler un serveur web qui capturerait la requête de la cible comme preuve qu'il a été en mesure de forcer le serveur à faire cette requête.

Dans l'exemple de cours In-Band SSRF, un attaquant fait une requête qui inclut une URL.

Celle-ci sera utilisée pour mettre à jour le stock d'un article dans le magasin.

L'attaquant est en mesure de remplacer cette URL de stock d'article par une URL de localhost vers un répertoire avec un mot de passe.

Le serveur est vulnérable et fournit le mot de passe à l'attaquant.

Blind SSRF se produit lorsqu'un serveur vulnérable effectue une requête à partir de l'entrée utilisateur, mais n'envoie pas la réponse à l'attaquant indiquant une attaque réussie.

En d'autres termes, le serveur victime fait la requête à l'URL spécifiée par l'attaquant, mais l'attaquant ne reçoit pas de message direct du serveur victime.

Dans ce cas, pour savoir si la requête a été faite, un attaquant devra avoir un certain contrôle sur le serveur web qui est spécifié dans l'attaque.

Pour des exemples et des démonstrations d'attaques SSRF In-Band et Out-of-Band, consultez le matériel de cours écrit.

La mesure préventive OWASP indique "isoler le mécanisme de récupération des ressources dans votre réseau.

Habituellement, ces fonctionnalités visent à récupérer des ressources distantes et non internes.

Lorsque cela est possible, utilisez des listes d'autorisation des origines distantes des utilisateurs qui sont censés télécharger des ressources, comme Google Drive ou Gravatar, les schémas d'URL et les ports, les types de médias acceptés pour une fonctionnalité donnée.

Désactivez les redirections HTTP.

Utilisez un analyseur d'URL bien testé et maintenu pour éviter les problèmes causés par les incohérences d'analyse d'URL.

Validez et nettoyez toutes les données d'entrée fournies par le client.

Ne renvoyez pas de réponses brutes aux clients." Consultez le contenu écrit du cours pour des ressources supplémentaires sur SSRF.

API8:2023, Mauvaise configuration de sécurité représente un fourre-tout pour de nombreuses vulnérabilités liées aux systèmes qui hébergent les APIs.

Lorsque la sécurité d'une API est mal configurée, cela peut être préjudiciable à la confidentialité, à l'intégrité et à la disponibilité des données du fournisseur d'API.

En raison de la grande variété de failles qui pourraient exister, les impacts d'une mauvaise configuration de sécurité exploitée peuvent aller de la divulgation d'informations à la violation de données.

La description du vecteur d'attaque OWASP indique que "les attaquants tenteront souvent de trouver des failles non corrigées, des points de terminaison courants ou des fichiers et répertoires non protégés pour obtenir un accès non autorisé ou des connaissances sur le système." La description de la faiblesse de sécurité OWASP indique que "la mauvaise configuration de sécurité peut se produire à n'importe quel niveau de la pile API, du niveau réseau au niveau de l'application.

Des outils automatisés sont disponibles pour détecter et exploiter les mauvaises configurations telles que les services inutiles ou les options héritées." La description des impacts OWASP indique que "les mauvaises configurations de sécurité peuvent non seulement exposer des données utilisateur sensibles, mais aussi des détails du système qui peuvent conduire à une compromission complète du serveur." Les mauvaises configurations de sécurité incluent toutes les erreurs que les fournisseurs d'API peuvent commettre dans les systèmes de support d'une API.

Les mauvaises configurations de sécurité sont vraiment un ensemble de faiblesses qui incluent des en-têtes mal configurés, une encryption de transit mal configurée, l'utilisation de comptes par défaut, l'acceptation de méthodes HTTP inutiles, un manque de nettoyage des entrées et des messages d'erreur verbeux.

Par exemple, si la configuration de sécurité de support de l'API révèle une vulnérabilité non corrigée.

Il y a une chance qu'un attaquant puisse exploiter un exploit publié pour facilement compromettre l'API et ses systèmes.

Un manque de nettoyage des entrées pourrait permettre aux attaquants de télécharger des charges utiles malveillantes sur le serveur.

Les APIs jouent souvent un rôle clé dans l'automatisation des processus, alors imaginez pouvoir télécharger des charges utiles que le serveur traite automatiquement dans un format qui pourrait être exécuté à distance ou exécuté par un utilisateur final insoupçonné.

Par exemple, si un point de terminaison de téléchargement était utilisé pour passer des fichiers téléchargés à un répertoire web, cela pourrait permettre le téléchargement d'un script.

Naviguer vers l'URL où se trouve le fichier pourrait lancer le script, entraînant un accès direct à la coque du serveur web.

De plus, un manque de nettoyage des entrées peut conduire à un comportement inattendu de la part de l'application.

Les fournisseurs d'API utilisent des en-têtes pour fournir au consommateur des instructions pour gérer la réponse et les exigences de sécurité.

Des en-têtes mal configurés peuvent entraîner la divulgation d'informations sensibles, des attaques par rétrogradation et des attaques par script inter-sites.

De nombreux fournisseurs d'API utiliseront des services supplémentaires aux côtés de leur API pour améliorer les métriques liées aux API ou pour améliorer la sécurité.

Il est assez courant que ces services supplémentaires ajoutent des en-têtes aux requêtes pour les métriques et peut-être comme un certain niveau d'assurance au consommateur.

L'en-tête X-Powered-By révèle la technologie backend.

Des en-têtes comme celui-ci annoncent souvent le service de support exact et sa version.

Un attaquant pourrait utiliser des informations comme celles-ci pour rechercher des exploits publiés pour cette version de logiciel.

L'en-tête X-XSS-Protection est exactement ce à quoi il ressemble, un en-tête destiné à prévenir les attaques par script inter-sites (XSS).

Le script inter-sites est un type courant de vulnérabilité par injection où un attaquant pourrait insérer des scripts dans une page web et tromper les utilisateurs finaux en cliquant sur des liens malveillants.

Un en-tête X-XSS-Protection avec une valeur de 0 indique aucune protection en place, et une valeur de 1 indique que la protection est activée.

Cet en-tête et d'autres comme lui révèlent clairement si un contrôle de sécurité est en place ou non.

L'en-tête X-Response-Time est un middleware qui fournit les métriques d'utilisation.

Dans cet exemple, dans le matériel de cours écrit, sa valeur représente 566 millisecondes.

Mais si l'API n'est pas configurée correctement, cet en-tête peut fonctionner comme un canal latéral utilisé pour révéler les ressources existantes.

Si l'en-tête X-Response-Time a un temps de réponse constant pour les enregistrements inexistants, par exemple, mais augmente son temps de réponse pour certains autres enregistrements qui existent réellement, cela pourrait être une indication pour un attaquant qu'il est tombé sur ces fichiers.

Par exemple, un attaquant peut déterminer qu'un compte bidon comme /user/account/thisdefinitelydoesnotexist a un temps de réponse moyen de 25 millisecondes.

L'attaquant peut savoir que leur compte existant est /user/account/1021, qui reçoit un X-Response-Time de 510 millisecondes.

Un attaquant pourrait alors envoyer des requêtes en forçant les numéros de compte et examiner les résultats pour voir quels numéros de compte ont entraîné des temps de réponse considérablement augmentés.

Toute API fournissant des informations sensibles aux consommateurs doit utiliser le protocole Transport Layer Security pour crypter les données, même si l'API n'est fournie qu'en interne, en privé ou au niveau partenaire.

Transport Layer Security, le protocole qui crypte le trafic HTTPS, est l'un des moyens les plus basiques pour s'assurer que les requêtes et réponses API sont protégées lorsqu'elles sont transmises sur un réseau.

Une encryption de transit mal configurée ou manquante peut amener les utilisateurs d'API à transmettre des informations API sensibles en texte clair sur les réseaux, auquel cas un attaquant pourrait capturer les réponses et les requêtes avec un Man-in-the-Middle (MITM) et les lire clairement.

Ils n'auraient qu'à intercepter le trafic réseau avec un analyseur de protocole réseau comme Wireshark pour voir les informations communiquées entre un consommateur et un fournisseur.

Lorsque qu'un service utilise des comptes ou des identifiants par défaut, et que les valeurs par défaut sont connues, un attaquant peut utiliser ces identifiants pour usurper le rôle de ce compte.

Cela pourrait leur permettre d'accéder à des informations sensibles ou à des fonctionnalités administratives et potentiellement conduire à une compromission des systèmes de support.

Enfin, si un fournisseur d'API permet des méthodes HTTP inutiles, il y a un risque accru que l'application ne gère pas correctement ces méthodes ou entraîne une divulgation d'informations sensibles.

Parmi toutes les vulnérabilités couvertes dans le Top 10 de l'OWASP, API8:2023 Mauvaise configuration de sécurité est l'une des seules qui peut être détectée par des scanners de vulnérabilités d'applications web.

Des scanners automatisés comme BurpSuite, Nessus, Qualys, OWASP, ZAP et Nikto vérifieront automatiquement les réponses du serveur web pour déterminer les informations de version, les en-têtes, les cookies, la configuration de l'encryption de transit et les paramètres pour voir si les mesures de sécurité attendues sont manquantes.

Les mauvaises configurations de sécurité peuvent également être vérifiées manuellement si vous savez ce que vous cherchez, en inspectant les en-têtes, le certificat SSL, les cookies et les paramètres.

Les mesures préventives OWASP indiquent que le cycle de vie de l'API doit inclure : un processus de durcissement répétable conduisant à un déploiement rapide et facile d'un environnement correctement verrouillé, une tâche pour examiner et mettre à jour les configurations dans toute la pile API.

L'examen doit inclure les fichiers d'orchestration, les composants API et les services cloud et un processus automatisé pour évaluer en continu l'efficacité de la configuration et des paramètres dans tous les environnements.

De plus, assurez-vous que toutes les communications API du client au serveur API et à tous les composants en aval et en amont se font via un canal de communication crypté, qu'il s'agisse d'une API interne ou publique.

Soyez spécifique sur les verbes HTTP auxquels chaque API peut être accessible.

Tous les autres verbes HTTP doivent être désactivés.

Les APIs s'attendant à être accessibles depuis des clients basés sur navigateur doivent au moins mettre en œuvre une politique de partage de ressources cross-origin (CORS) appropriée.

Incluez les en-têtes de sécurité applicables, limitez les types de contenu/les formats de données entrants à ceux qui répondent aux exigences fonctionnelles de l'entreprise.

Assurez-vous que tous les serveurs de la chaîne de serveurs HTTP traitent les requêtes entrantes de manière uniforme pour éviter les problèmes de désynchronisation.

Là où c'est applicable, définissez et appliquez tous les schémas de charge utile de réponse API, y compris les réponses d'erreur pour empêcher les traces d'exception et autres informations précieuses d'être renvoyées à un attaquant.

Consultez le contenu écrit du cours pour des ressources supplémentaires sur les mauvaises configurations de sécurité des APIs.

API9:2023, Gestion incorrecte de l'inventaire représente les risques liés à l'exposition de versions non production et non supportées des APIs.

Lorsque cela est présent, les versions non production et non supportées de l'API ne sont souvent pas protégées par la même rigueur de sécurité que les versions de production.

Cela fait de la gestion incorrecte de l'inventaire une porte d'entrée vers d'autres vulnérabilités de sécurité des APIs.

La description du vecteur d'attaque OWASP indique que "Les agents de menace obtiennent généralement un accès non autorisé via des versions anciennes d'API ou des points de terminaison laissés en fonctionnement sans correctifs et utilisant des exigences de sécurité plus faibles.

Alternativement, ils peuvent obtenir un accès à des données sensibles via un tiers avec lequel il n'y a aucune raison de partager des données." La description de la faiblesse de sécurité OWASP indique que "La documentation obsolète rend plus difficile la recherche et/ou la correction des vulnérabilités.

Le manque de stratégies d'inventaire et de retrait des actifs conduit à l'exécution de systèmes non corrigés, entraînant des fuites de données sensibles.

Il est courant de trouver des hôtes d'API exposés inutilement en raison de concepts modernes comme les microservices, qui rendent les applications faciles à déployer et indépendantes.

Un simple Google Dorking, une énumération DNS, ou l'utilisation de moteurs de recherche spécialisés pour divers types de serveurs connectés à l'internet suffiront à découvrir des cibles." La description des impacts OWASP indique que "Les attaquants peuvent obtenir un accès à des données sensibles ou même prendre le contrôle du serveur.

Parfois, différentes déploiements de versions d'API sont connectés à la même base de données avec des données réelles.

Les agents de menace peuvent exploiter des points de terminaison obsolètes disponibles dans les anciennes versions d'API pour obtenir un accès à des fonctions administratives ou exploiter des vulnérabilités connues." La gestion incorrecte de l'inventaire se produit lorsqu'une organisation expose des APIs qui ne sont pas supportées ou encore en développement.

Comme pour tout logiciel, les anciennes versions d'API sont plus susceptibles de contenir des vulnérabilités car elles ne sont plus corrigées et mises à jour.

De même, les APIs qui sont encore en développement et sont généralement moins sécurisées que leurs homologues de production.

La gestion incorrecte de l'inventaire peut conduire à d'autres vulnérabilités telles que l'exposition excessive de données, la divulgation d'informations, l'affectation massive, la limitation de débit incorrecte et l'injection d'API.

Pour les attaquants, cela signifie que la découverte d'une vulnérabilité de gestion incorrecte de l'inventaire n'est que la première étape vers une exploitation supplémentaire d'une API.

La détection de la gestion incorrecte de l'inventaire peut être testée en utilisant une documentation API obsolète, des journaux de modifications et l'historique des versions sur les dépôts.

Par exemple, si la documentation de l'API d'une organisation n'a pas été mise à jour avec les points de terminaison de l'API, elle pourrait contenir des références à des parties de l'API qui ne sont plus supportées.

Les organisations incluent souvent des informations de version dans les noms de leurs points de terminaison pour distinguer les versions plus anciennes des plus récentes.

Telles que /v1/, /v2/, ou /v3/ et ainsi de suite.

Les APIs encore en développement utilisent souvent des chemins tels que /alpha/, /beta/, /test/, /uat/ et /demo/.

Si vous savez qu'une API utilise maintenant apiv3.org/admin, mais qu'une partie de la documentation de l'API fait référence à apiv1.org/admin, vous pourriez essayer de tester différents points de terminaison pour voir si apiv1 ou apiv2 sont encore actifs.

De plus, le journal des modifications de l'organisation peut divulguer les raisons pour lesquelles v1 a été mis à jour ou retiré.

Si un attaquant a accès à v1, il peut tester celles-ci pour des faiblesses.

En dehors de l'utilisation de la documentation, un attaquant pourrait découvrir des vulnérabilités de gestion incorrecte de l'inventaire par le biais de la devinette, du fuzzing ou du forçage brutal des requêtes.

Le test de la gestion incorrecte des actifs consiste à découvrir les versions non supportées et non production d'une API.

Les fournisseurs d'API mettront souvent à jour les services et la nouvelle version de l'API de diverses manières, telles que api.target.com/v3, ou /api/v2/accounts, ou /api/v3/accounts.

La gestion des versions d'API pourrait également être maintenue en tant qu'en-tête.

Ainsi, vous pourriez voir quelque chose comme Accept: version=2.0, ou Accept api-version=3.

De plus, la gestion des versions pourrait également être définie dans un paramètre de requête ou le corps de la requête.

Ainsi, vous pourriez voir /api/accounts?ver=2.

Ou POST vers API accounts avec versioning égal à 1.0.

Les versions non production d'une API incluent toute version de l'API qui n'était pas destinée à la consommation par l'utilisateur final.

Les versions non production pourraient inclure api.test.target.com, beta.api.com, /api/private, /api/partner ou /api/test.

Dans ces cas, les versions antérieures de l'API peuvent ne plus être corrigées ou mises à jour puisque les versions plus anciennes manquent de ce support.

Elles peuvent exposer l'API à des vulnérabilités supplémentaires et conduire un attaquant à un chemin qui peut être utilisé pour compromettre les données du fournisseur.

Les mesures préventives OWASP indiquent d'inventorier tous les hôtes API et de documenter les aspects importants de chacun d'eux, en se concentrant sur l'environnement API, tel que la production, la mise en scène, le test ou le développement, qui devrait avoir un accès réseau à l'hôte, tel que public, interne ou partenaires et la version de l'inventaire des services intégrés et documenter les aspects importants, tels que leur rôle dans le système, les données échangées et leur sensibilité.

Documentez tous les aspects de votre API, tels que l'authentification, les erreurs, les redirections, la limitation de débit, la politique de partage de ressources cross-origin (CORS), et les points de terminaison, y compris leurs paramètres, requêtes et réponses.

Générez la documentation automatiquement en adoptant des standards ouverts.

Incluez la documentation intégrée dans votre pipeline CI/CD.

Rendez la documentation de l'API disponible à ceux autorisés à utiliser l'API.

Utilisez des mesures de protection externes, telles qu'un pare-feu de sécurité API, pour toutes les versions exposées de vos APIs.

Pas seulement pour les versions de production actuelles.

Évitez d'utiliser des données de production avec des déploiements d'API non production.

Si cela est inévitable, ces points de terminaison doivent recevoir le même traitement de sécurité que ceux de production.

Lorsque de nouvelles versions de l'API incluent des améliorations de sécurité, effectuez une analyse des risques pour prendre la décision des actions d'atténuation requises pour l'ancienne version.

Par exemple, s'il est possible de rétroporter les améliorations sans rompre la compatibilité de l'API, ou si vous devez prendre l'ancienne version, mais appliquer rapidement toutes les clients à passer à la dernière version.

Pour des ressources supplémentaires sur la gestion incorrecte de l'inventaire, consultez les matériaux de cours écrits.

API10:2023, Consommation non sécurisée des APIs est le seul élément de la liste Top 10 qui se concentre moins sur les risques d'être un fournisseur d'API et plus sur les risques d'être un consommateur d'API.

La consommation non sécurisée est vraiment une question de confiance.

Lorsque qu'une application consomme les données d'une API tierce, elle doit les traiter avec une confiance similaire à celle des entrées utilisateur.

Par cela, je veux dire qu'il devrait y avoir peu ou pas de confiance.

Ainsi, les données consommées à partir d'une API tierce doivent être traitées avec des normes de sécurité similaires à celles des entrées fournies par l'utilisateur final.

Si un fournisseur d'API tierce est compromis, alors cette connexion d'API non sécurisée vers le consommateur devient un nouveau vecteur d'attaque pour l'attaquant à exploiter.

Dans le cas d'une connexion d'API non sécurisée, cela pourrait signifier la compromission complète des organisations consommant de manière non sécurisée les données de ce fournisseur d'API.

La description du vecteur d'attaque OWASP indique que "l'exploitation de ce problème nécessite que les attaquants identifient et potentiellement compromettent d'autres APIs ou services avec lesquels l'API cible est intégrée.

Généralement, ces informations ne sont pas publiques ou l'API ou le service intégré n'est pas facilement exploitable." La description de la faiblesse de sécurité OWASP indique que "les développeurs tendent à faire confiance et à ne pas vérifier les points de terminaison qui interagissent avec des APIs externes ou tierces, en s'appuyant sur des exigences de sécurité plus faibles telles que celles concernant la sécurité du transport, l'authentification, l'autorisation, et la validation et l'assainissement des entrées.

Les attaquants doivent identifier les services avec lesquels l'API cible interagit ou s'intègre et éventuellement les compromettre." La description des impacts OWASP indique que "l'impact varie selon ce que l'API cible fait avec les données regroupées.

Une exploitation réussie peut conduire à l'exposition d'informations sensibles à des acteurs non autorisés, à de nombreux types d'injections, ou à un déni de service." La plupart du Top 10 de la sécurité des APIs 2023 concerne les APIs et le fournisseur d'API.

Une API peut souvent servir de chemin de moindre résistance pour un attaquant.

Ainsi, si un attaquant compromettait un fournisseur d'API tiers, alors la connexion de ce tiers à d'autres entreprises pourrait devenir un vecteur d'attaque supplémentaire.

Si cette API est sur une connexion non cryptée, alors un attaquant pourrait capturer des données sensibles en texte clair.

Si cette API tierce n'est pas soumise à des normes de sécurité similaires à celles des APIs faisant face à Internet, elle pourrait également être vulnérable aux injections, à l'autorisation, à l'authentification et à d'autres attaques compromettantes.

La mesure préventive OWASP indique que lors de l'évaluation des fournisseurs de services, évaluez leur posture de sécurité des APIs.

Assurez-vous que toutes les interactions avec les APIs se font via un canal de communication sécurisé.

Validez et nettoyez toujours correctement les données reçues des APIs intégrées avant de les utiliser.

Maintenez et autorisez une liste d'emplacements bien connus vers lesquels les APIs intégrées peuvent vous rediriger.

Ne suivez pas aveuglément les redirections.

Pour des ressources supplémentaires sur la consommation non sécurisée des APIs, consultez les matériaux de cours écrits.

Les vulnérabilités d'injection ont tourmenté les applications web depuis plus de deux décennies.

Elles se produisent lorsqu'un attaquant peut envoyer des commandes qui sont exécutées par les systèmes qui supportent l'application web.

Les formes les plus courantes d'attaques par injection sont l'injection SQL, le script inter-sites et l'injection de commandes du système d'exploitation.

Les APIs sont un autre vecteur d'attaque pour que ces attaques critiques soient communiquées d'un attaquant au système de support, aux bases de données et aux systèmes.

La description du vecteur d'attaque OWASP 2019 indique que "les attaquants alimenteront l'API avec des données malveillantes via tous les vecteurs d'injection disponibles, tels que les paramètres d'entrée directs, les services intégrés, en s'attendant à ce qu'ils soient envoyés à un interpréteur." La description de la faiblesse de sécurité OWASP 2019 indique que "les failles d'injection sont très courantes et sont souvent trouvées dans les requêtes SQL, LDAP ou NoSQL, les commandes OS, les analyseurs XML et ORM.

Ces failles sont faciles à découvrir lors de la révision du code source.

Les attaquants peuvent utiliser des scanners et des fuzzers pour les trouver." La description des impacts OWASP 2019 indique que l'injection peut conduire à la divulgation d'informations et à la perte de données et peut également conduire à un déni de service ou à une prise de contrôle complète de l'hôte.

Les failles d'injection existent lorsqu'une requête est transmise à l'infrastructure de support de l'API et que le fournisseur de l'API ne filtre pas l'entrée pour supprimer les caractères indésirables.

En conséquence, l'infrastructure pourrait traiter les données de la requête comme du code et les exécuter.

Lorsque ce type de faille est présent, un attaquant pourra mener des attaques par injection comme l'injection SQL, l'injection NoSQL et l'injection de commandes système.

Lorsque ces attaques par injection réussissent, l'API livre une charge utile non nettoyée directement au système d'exploitation exécutant l'application ou une requête à sa base de données.

En conséquence, si un attaquant envoie une charge utile contenant des commandes SQL à une API vulnérable utilisant une base de données SQL, l'API transmettra les commandes à la base de données, qui les traitera et les exécutera.

Il en va de même pour les bases de données NoSQL vulnérables et les systèmes affectés.

Les messages d'erreur verbeux, les codes de réponse HTTP et le comportement inattendu de l'API peuvent tous être des indices pour un attaquant et seront une indication qu'ils ont découvert une faille d'injection.

Par exemple, si un attaquant envoyait OR1 00 DAS comme adresse dans un processus d'inscription de compte.

L'API pourrait transmettre cette charge utile directement à la base de données SQL backend, où l'instruction or 1 equals 0, qui échouerait car 1 n'est pas égal à 0, provoquant une erreur SQL.

Une erreur dans la base de données backend pourrait apparaître comme une réponse au consommateur.

Dans ce cas, l'attaquant, qui est le consommateur, pourrait recevoir une réponse comme, Error equals you have an error in your SQL syntax.

Mais, toute réponse directement de la base de données ou du système de support servira d'indicateur clair qu'il y a probablement une vulnérabilité d'injection.

Les vulnérabilités d'injection sont souvent complétées par d'autres faiblesses comme un mauvais nettoyage des entrées.

Les failles d'injection peuvent avoir des impacts sérieux en fournissant à un attaquant la capacité de manipuler un système ou une base de données de support d'API.

La découverte de failles d'injection nécessite de tester rigoureusement les points de terminaison de l'API et de prêter attention à la manière dont l'API répond, puis de concevoir des requêtes qui tentent de manipuler les systèmes backend.

Les attaques par injection existent depuis des décennies, il existe donc de nombreux contrôles de sécurité standard qui peuvent être utilisés pour protéger les fournisseurs d'API contre elles.

Les mesures préventives OWASP 2019 indiquent que la prévention de l'injection nécessite de garder les données séparées des commandes et des requêtes.

Effectuez une validation des données en utilisant une bibliothèque unique, fiable et activement maintenue.

Validez, filtrez et nettoyez toutes les données fournies par le client ou d'autres données provenant de systèmes intégrés.

Les caractères spéciaux doivent être échappés en utilisant la syntaxe spécifique pour l'interpréteur cible.

Préférez une API sûre qui fournit une interface paramétrée.

Limitez toujours le nombre d'enregistrements retournés pour prévenir la divulgation massive en cas d'injection.

Validez les données entrantes en utilisant des filtres suffisants pour n'autoriser que des valeurs valides pour chaque paramètre d'entrée.

Définissez des types de données et des motifs stricts pour tous les paramètres de chaîne.

Pour des ressources supplémentaires sur l'injection d'API, consultez le contenu écrit du cours.

La journalisation et la surveillance sont une couche nécessaire et importante de la sécurité des APIs.

Afin de détecter une attaque contre une API, une organisation doit avoir une surveillance en place.

Sans une journalisation et une surveillance suffisantes, un fournisseur d'API fonctionne dans l'obscurité, et les attaques contre les APIs sont garanties de passer inaperçues jusqu'à ce qu'il soit trop tard.

La description du vecteur d'attaque OWASP 2019 indique que "Les attaquants profitent d'un manque de journalisation et de surveillance pour abuser des systèmes sans être remarqués." La description de la faiblesse de sécurité OWASP 2019 indique que "Sans journalisation et surveillance, ou avec une journalisation et une surveillance insuffisantes, il est presque impossible de suivre les activités suspectes et d'y répondre en temps opportun." La description des impacts OWASP 2019 indique que "Sans visibilité sur les activités malveillantes en cours, les attaquants ont tout le temps pour compromettre complètement les systèmes.

Les journaux peuvent révéler des schémas dans l'utilisation des APIs et peuvent être utilisés comme preuve pour comprendre comment une API est abusée.

La journalisation et la surveillance fournissent une trace d'audit des activités et sont souvent requises à des fins de conformité." Une partie importante de la journalisation est de s'assurer que les journaux ont une intégrité et ne peuvent pas être altérés par un attaquant.

La surveillance d'une API aidera les fournisseurs à détecter les activités suspectes et les comportements anormaux des utilisateurs.

Cela aide les fournisseurs à pouvoir prendre des mesures pour contrer les attaques.

La journalisation et la surveillance sont essentielles pour améliorer les performances et la sécurité des APIs.

Les mesures préventives OWASP 2019 indiquent de journaliser toutes les tentatives d'authentification échouées, les accès refusés et les erreurs de validation d'entrée.

Les journaux doivent être écrits en utilisant un format adapté pour être consommé par une solution de gestion des journaux et doivent inclure suffisamment de détails pour identifier l'acteur malveillant.

Les journaux doivent être traités comme des données sensibles et leur intégrité doit être garantie au repos et en transit.

Configurez un système de surveillance pour surveiller en continu l'infrastructure, le réseau et le fonctionnement de l'API.

Utilisez un système SIEM pour agréger et gérer les journaux de tous les composants de la pile API et des hôtes.

Configurez des tableaux de bord et des alertes personnalisés permettant de détecter et de répondre plus tôt aux activités suspectes.

Pour des ressources supplémentaires sur la journalisation et la surveillance insuffisantes, consultez le contenu écrit du cours.

Les vulnérabilités de logique métier sont des faiblesses au sein des applications qui sont uniques aux politiques et fonctionnalités d'un fournisseur d'API donné.

L'exploitation de la logique métier a lieu lorsqu'un attaquant utilise la confiance mal placée ou les fonctionnalités d'une application contre l'API.

L'identification des vulnérabilités de logique métier peut être difficile en raison de la nature unique de chaque entreprise.

L'impact de ces vulnérabilités peut varier en fonction de la gravité de la politique ou de la fonctionnalité vulnérable.

Ma description du vecteur d'attaque pour ces vulnérabilités de logique métier est unique à chaque application et exploite le fonctionnement normal prévu des processus métier d'une application.

Elles nécessitent souvent une connaissance spécifique de la fonctionnalité de l'application et du flux des transactions ou des données.

Puisque ces vulnérabilités sont spécifiques à la logique métier de chaque application, il n'existe pas d'approche universelle pour les identifier.

Ma description de la faiblesse de sécurité indique que les vulnérabilités de logique métier surviennent lorsque les hypothèses et les contraintes d'un processus métier donné ne sont pas correctement appliquées dans les structures de contrôle de l'application.

Cela permet aux utilisateurs de manipuler la fonctionnalité de l'application pour obtenir des résultats qui sont préjudiciables à l'entreprise.

Ces faiblesses se produisent généralement lorsque les développeurs ne parviennent pas à anticiper les diverses façons dont les fonctionnalités d'une application peuvent être mal utilisées ou lorsqu'ils ne considèrent pas le contexte plus large des règles métier.

Cela est souvent dû à un manque de compréhension complète de la logique métier de l'application, à un manque de validation des entrées ou à des vérifications d'autorisation de niveau fonction incomplètes.

Ma description des impacts indique que les vulnérabilités de logique métier peuvent causer une variété d'impacts techniques en fonction de la faille spécifique dans les systèmes impliqués.

Ces impacts peuvent aller de l'accès non autorisé aux données ou à la fonctionnalité à un contournement total des contrôles du système.

Les vulnérabilités de logique métier, également connues sous le nom de failles de logique métier, ou BLFs, sont des fonctionnalités prévues d'une application que les attaquants peuvent utiliser de manière malveillante.

Par exemple, si une API dispose d'une fonctionnalité de téléchargement qui indique aux utilisateurs de ne télécharger que certains types de charges utiles encodées, mais ne valide pas réellement ces charges utiles encodées, un utilisateur pourrait télécharger n'importe quel fichier tant qu'il est encodé.

Cela permettrait aux utilisateurs finaux de télécharger et potentiellement d'exécuter du code arbitraire, y compris des charges utiles malveillantes.

Les vulnérabilités de ce type proviennent généralement de l'hypothèse que les consommateurs d'API suivront les instructions, seront dignes de confiance ou n'utiliseront l'API que d'une certaine manière.

Dans ces cas, l'organisation dépend essentiellement de la confiance comme contrôle de sécurité en s'attendant à ce que le consommateur agisse de manière bienveillante.

Malheureusement, même les consommateurs d'API bien intentionnés commettent des erreurs qui pourraient conduire à une compromission de l'application.

La fuite de l'API partenaire Experian en 2021 était un excellent exemple d'un échec de confiance de l'API.

Un certain partenaire d'Experian était autorisé à utiliser l'API d'Experian pour effectuer des vérifications de crédit, mais le partenaire a ajouté la fonctionnalité de vérification de crédit de l'API à son application web et a involontairement exposé toutes les requêtes de niveau partenaire aux utilisateurs.

Cette requête pouvait être interceptée lors de l'utilisation de l'application web du partenaire, et si elle incluait un nom et une adresse, l'API Experian répondrait avec le score de crédit de l'individu et les facteurs de risque de crédit.

L'une des principales causes de cette vulnérabilité de logique métier était qu'Experian faisait confiance au partenaire pour ne pas exposer l'API.

Un autre problème avec la confiance est que les identifiants comme les clés API, les jetons et les mots de passe sont constamment volés et divulgués.

Lorsque les identifiants d'un consommateur de confiance sont volés, le consommateur peut devenir un loup déguisé en mouton et semer le chaos.

Sans des contrôles techniques solides en place, les vulnérabilités de logique métier peuvent souvent avoir l'impact le plus significatif, conduisant à l'exploitation et à la compromission.

La documentation d'une API peut être un signe révélateur d'une vulnérabilité de logique métier.

Des déclarations comme les suivantes devraient être des indications de potentielles failles de logique métier.

N'utilisez la fonctionnalité x que pour effectuer la fonction y.

Ne faites pas x avec le point de terminaison y.

Seuls les administrateurs doivent effectuer la requête X.

Ces déclarations peuvent indiquer que le fournisseur de l'API fait confiance à ce que les utilisateurs finaux ne feront aucune des actions découragées comme indiqué.

Un attaquant désobéira facilement à de telles demandes pour tester la présence de contrôles de sécurité techniques.

Une autre vulnérabilité de logique métier survient lorsque les développeurs supposent que les consommateurs utiliseront exclusivement un navigateur pour interagir avec l'application web et ne captureront pas les requêtes API qui se produisent en arrière-plan.

Il suffit qu'un attaquant intercepte les requêtes et modifie la requête API avant qu'elle ne soit envoyée au fournisseur.

Cela permettrait à l'attaquant de capturer des clés API partagées ou d'utiliser des paramètres qui pourraient avoir un impact négatif sur la sécurité de l'application.

Par exemple, considérons un portail d'authentification d'application web qu'un utilisateur utiliserait normalement pour s'authentifier à son compte.

Supposons que l'application web émette une requête d'authentification API qui inclut le nom d'utilisateur et le mot de passe ainsi qu'un paramètre de requête, multi factor equals true.

Il y a une chance qu'un attaquant puisse contourner l'authentification multifactorielle en modifiant simplement le paramètre à false.

Le test des failles de logique métier peut être difficile car chaque entreprise est unique.

Les scanners automatisés auront du mal à détecter ces problèmes, car les failles font partie de l'utilisation prévue de l'API.

Vous devez comprendre comment l'entreprise et l'API fonctionnent, puis considérer comment un attaquant pourrait utiliser ces fonctionnalités à son avantage.

Une méthode de test des failles de logique métier consiste à étudier la logique métier de l'application avec un état d'esprit adversarial et à essayer de briser les hypothèses qui ont été faites.

Mes mesures préventives pour les failles de logique métier incluent les éléments suivants.

Utilisez une approche de modélisation des menaces.

Comprenez les processus et flux de travail métier que votre API prend en charge.

Identifiez les menaces potentielles, les faiblesses et les risques pendant la phase de conception qui peuvent aider à découvrir et à atténuer les vulnérabilités de logique métier.

Réduisez ou supprimez les relations de confiance avec les utilisateurs, les systèmes ou les composants.

Les vulnérabilités de logique métier peuvent être utilisées pour exploiter ces relations de confiance, conduisant à un impact plus large.

Une formation régulière peut aider les développeurs à comprendre et à éviter les vulnérabilités de logique métier.

La formation doit couvrir les pratiques de codage sécurisé, les vulnérabilités courantes et comment identifier les problèmes potentiels pendant les phases de conception et de codage.

Mettez en œuvre un programme de prime aux bogues, des tests de pénétration tiers ou une politique de divulgation responsable.

Cela permet aux chercheurs en sécurité, qui sont un cran en retrait de la conception et de la livraison d'une application, de divulguer les vulnérabilités qu'ils découvrent dans les APIs.

Pour des ressources supplémentaires sur les vulnérabilités de logique métier, consultez le matériel de cours écrit.

Et cela conclut le cours sur le OWASP API Security Top 10 et au-delà.

J'espère que vous l'avez apprécié.

Et si vous souhaitez obtenir un badge et un certificat pour ce cours, veuillez vous inscrire sur apisecuniversity.com, passer les quiz, et nous serons heureux de vous délivrer votre certificat.

Et pendant que vous y êtes, assurez-vous de consulter nos autres cours, y compris les tests d'intrusion des APIs, les fondamentaux de la sécurité des APIs, et plus encore.

Nous organisons également de nombreux webinaires avec des experts en APIs de divers secteurs, disciplines et géographies.

Vous verrez ceux-ci listés sur notre site web et sur notre chaîne YouTube.

Veuillez vous abonner.

Merci d'avoir regardé, et j'espère vous revoir bientôt.