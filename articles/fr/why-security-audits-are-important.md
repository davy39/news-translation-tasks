---
title: Pourquoi les audits de sécurité sont importants
subtitle: ''
author: P S Mohammed Ali
co_authors: []
series: null
date: '2025-03-19T20:20:20.430Z'
originalURL: https://freecodecamp.org/news/why-security-audits-are-important
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742397497226/ec06b7c2-1a2a-4eb1-bbaa-4c1d40e4e60e.png
tags:
- name: Security
  slug: security
- name: '#cybersecurity'
  slug: cybersecurity-1
seo_title: Pourquoi les audits de sécurité sont importants
seo_desc: 'In this digital world, companies rely on the latest technology to run their
  businesses, and the risk of cyber attacks is high.

  Every product, whether it’s software or an application, should go through some sort
  of security testing process. These chec...'
---

Dans ce monde numérique, les entreprises s'appuient sur les dernières technologies pour gérer leurs activités, et le risque de cyberattaques est élevé.

Chaque produit, qu'il s'agisse d'un logiciel ou d'une application, devrait subir un processus de test de sécurité. Ces vérifications révèlent si le produit est sûr ou vulnérable aux menaces.

Les tests de pénétration sont une méthode courante pour tester les processus ou les produits, mais ils sont généralement conçus de manière plus spécifique avec un produit particulier en tête. En revanche, un audit de sécurité complet a une portée plus large et couvre plus de terrain que les tests de pénétration seuls.

Dans cet article, vous apprendrez ce qui est impliqué dans un audit de sécurité standard et comment ces processus peuvent aider à maintenir la sécurité de votre logiciel. À la fin, vous aurez une meilleure idée de la manière dont les audits de sécurité peuvent aider à améliorer la posture de sécurité globale d'une organisation.

## Qu'est-ce qu'un audit de sécurité ?

Un audit de sécurité est une revue globale des contrôles de sécurité, des politiques, des normes et des procédures d'une organisation, basée sur un ensemble d'attentes prédéfinies.

Ces attentes prédéfinies sont dérivées des normes de l'industrie telles que PCI DSS (Payment Card Industry Data Security Standard), qui est un cadre obligatoire pour les organisations traitant des transactions par carte de crédit. De même, HIPAA (Health Insurance Portability and Accountability Act) se concentre sur la confidentialité et la protection de vos informations de santé, ce qui en fait un élément essentiel pour les entreprises qui gèrent des données liées à la santé.

Outre ces normes, politiques et cadres, les audits de sécurité examinent également les composants de l'infrastructure et vérifient les sauvegardes d'applications ou les mécanismes de récupération pour s'assurer que les données sont protégées en cas de perte de données accidentelle ou malveillante.

Le résultat de l'audit peut aider à informer l'entreprise de sa posture de sécurité actuelle et fournit également des détails sur les vulnérabilités possibles et les menaces de conformité.

Généralement, les audits de sécurité sont réalisés par un groupe d'experts en sécurité. Ils planifient l'audit bien à l'avance pour s'assurer qu'il interrompe le moins possible les activités quotidiennes de l'entreprise.

Il existe deux types d'audits de sécurité :

1. Audit interne

2. Audit externe

Dans cet article, nous discuterons des audits internes. La principale différence entre les deux processus est que les audits internes sont réalisés par des personnes appartenant à l'organisation, tandis que les audits externes sont réalisés par une équipe de sécurité extérieure à l'organisation.

## Éléments d'un audit interne (flux de processus)

Un audit de sécurité bien structuré offre de la transparence et garantit une approche systématique pour évaluer l'efficacité des politiques et procédures de sécurité en place.

Le processus d'audit interne suit généralement ces cinq étapes :

1. Établissement des objectifs

2. Réalisation d'une évaluation des risques

3. Complétion d'une évaluation des contrôles

4. Évaluation de la conformité

5. Communication aux parties prenantes

Pour comprendre les éléments d'un audit interne plus en détail, décomposons le processus en travaillant sur une étude de cas. Cela vous montrera comment une entreprise ou une équipe peut planifier un audit interne en utilisant une approche systématique.

## Étude de cas d'audit de sécurité

Afin de comprendre ce processus plus clairement, considérons un site web de commerce électronique appelé « walkGen.com » comme exemple.

**Étude de cas :** Il existe un site web de commerce électronique nommé **walkGen.com** qui vend principalement des chaussures via leur site web. Les clients peuvent commander en se connectant avec leur nom d'utilisateur et mot de passe et peuvent payer en utilisant une carte de crédit/débit ou UPI. Pour créer une meilleure expérience utilisateur, le site demande le nom, l'âge, le genre et la localisation de l'utilisateur pour des informations et un design personnalisés.

Avec ces informations en tête, réalisons un audit de sécurité pour le site web.

### Étape 1 : Établir les objectifs

Cette première étape consiste à identifier tous les actifs et services critiques nécessaires au fonctionnement du site web. Vous devrez également définir un ensemble d'attentes conformes aux normes de l'industrie.

Pour notre site web walkGen.com, les actifs critiques que nous devons considérer incluent les données des clients, les détails des transactions et les détails de l'infrastructure tels que le serveur d'hébergement, la base de données, etc.

En gardant ces points de données initiaux à l'esprit, voici quelques objectifs possibles :

1. **Renforcer les contrôles d'accès** : Nous voulons nous assurer qu'il existe des politiques strictes d'authentification et d'autorisation pour tous les utilisateurs qui se connectent.

2. **Maintenir des cadres appropriés** : Puisque les clients peuvent payer par carte de crédit, nous voulons nous assurer que le site respecte des normes comme PCI DSS pour la sécurité des paiements.

3. **Sécuriser l'infrastructure** : Les actifs comme les serveurs d'hébergement et les bases de données doivent être protégés contre les cybermenaces et le vol.

Maintenant, les attentes clés sont que nous maintiendrons la conformité avec des normes de sécurité telles que le RGPD (Règlement Général sur la Protection des Données) pour la protection des données des clients ainsi que PCI DSS (Payment Card Industry Data Security Standard) pour les transactions monétaires. Nous devrons également effectuer des mises à jour régulières et des correctifs pour les serveurs et les bases de données.

### Étape 2 : Réaliser une évaluation des risques

L'évaluation des risques nous aide à identifier et à prioriser les menaces qui pourraient éventuellement affecter les actifs critiques de walkGen. Elle aide à catégoriser les risques en fonction de leur gravité et de leur probabilité.

L'identification et la catégorisation des risques seront l'objectif ultime de cette étape, car cela aidera walkGen à mettre en œuvre des mesures de sécurité efficaces pour les risques critiques par rapport aux risques faibles/informationnels.

À partir des actifs et services que nous avons identifiés dans l'étape précédente, les risques possibles pourraient être :

1. **Fuite de données clients** : Exposition des données clients telles que les noms, l'ID email, les adresses de livraison des clients, les détails de paiement, etc.

2. **Attaques de l'homme du milieu** : Interception du trafic du site web entre les utilisateurs connectés et le site web, entraînant le vol des identifiants de connexion, des détails de carte de paiement stockés, etc.

3. **Non-conformité avec PCI DSS** : Échec à respecter les normes requises pour traiter les transactions par carte de crédit de manière sécurisée.

4. **Transactions non autorisées ou détails de paiement volés** : Transactions de paiement effectuées sur des comptes compromis par des cybercriminels.

5. **Vulnérabilités du serveur** : Faiblesses/lacunes dans la configuration du serveur web hébergé, les logiciels tiers ou l'infrastructure du réseau cloud.

6. **Exploits de la base de données** : Exploitation des vulnérabilités présentes dans la base de données par le biais de tests de pénétration comme l'injection SQL, etc.

7. **Mises à jour de correctifs manquantes** : Ignorer/Échouer à appliquer les correctifs de sécurité pour le système d'exploitation ou les applications de walkGen.

> **Note :** Si vous regardez de près, certains de ces risques semblent se chevaucher avec d'autres, et certains peuvent sembler être définis de la même manière. Cela s'appelle la « **chaîne de risques** ». Mais au fond, ils sont différents les uns des autres.

Une fois que nous avons identifié ces risques, l'étape suivante consiste à les prioriser (Critique, Moyen ou Faible) en fonction de divers facteurs tels que la gravité, la probabilité de survenue, les dommages potentiels qui pourraient survenir si la menace se produit, etc.

| Niveau de risque | Risques assignés |
| --- | --- |
| Risque critique | 1. Fuite de données clients 
3. Attaques de l'homme du milieu 
4. Non-conformité avec PCI DSS 
5. Transactions non autorisées ou détails de paiement volés 
7. Exploits de la base de données |
| Risque moyen | 6. Vulnérabilités du serveur |
| Risque faible | 7. Mises à jour de correctifs manquantes |

### Étape 3 : Compléter une évaluation des contrôles

Cette phase garantit que des points de contrôle/contrôles de sécurité sont mis en œuvre pour les risques que nous avons identifiés tout en maintenant les normes de conformité. Si des contrôles de sécurité manquent, l'audit les documente et fournit des mesures préventives optimisées pour protéger le site web WalkGen.

Dans ce scénario particulier, certaines évaluations de contrôle pourraient être :

* Mise en œuvre de l'authentification multifactorielle (MFA) ou de l'authentification à deux facteurs (2FA) en utilisant une demande de mot de passe à usage unique (OTP) à un numéro de mobile enregistré pour prévenir l'exposition accidentelle des données clients.

* Protection des données en utilisant des normes de chiffrement telles que AES (Advanced Encryption Standard)-256 et TLS (Transport Layer Security) 1.3 pour une transmission de données sécurisée, aidant ainsi à éliminer les attaques possibles de l'homme du milieu.

* De plus, [mettre en œuvre des outils SIEM](https://www.freecodecamp.org/news/how-to-create-a-python-siem-system-using-ai-and-llms/) (Security Information and Event Management) pour la journalisation des événements afin de prévenir les attaques de l'homme du milieu.

* La compromission de compte se produit souvent par des attaques par force brute lorsque l'attaquant effectue plusieurs tentatives de connexion en essayant de deviner le mot de passe d'un utilisateur. Sur le site web walkGen, un plugin de sécurité a été mis en œuvre pour bloquer les multiples tentatives de connexion.

* ![Plugin de sécurité](https://cdn.hashnode.com/res/hashnode/image/upload/v1742237464615/aba6bb18-48dd-40d1-8d27-681711077ef9.png align="center")

* Comme indiqué dans la "chaîne de risques", les risques de non-conformité avec PCI DSS et les transactions non autorisées ou les détails de paiement volés tombent dans la même catégorie. Nous pouvons atténuer ces risques en activant une autorisation appropriée lors des transactions de paiement et, plus important encore, en désactivant l'option "Se souvenir de ma carte" par défaut, ce qui réduit considérablement le risque.

* Les vulnérabilités du serveur et les mises à jour de correctifs manquantes tombent également dans la même catégorie de risques basés sur l'humain. Ces risques sont atténués en fournissant des mises à jour périodiques et des rappels à la personne responsable des serveurs walkGen. Il est très probable que les clouds d'hébergement tels qu'Azure, AWS ou Google Cloud Platform (GCP) aient des vulnérabilités de serveur, que nous pouvons éviter en les maintenant à jour avec leurs dernières versions.

Cette phase nous aide à comprendre la posture de sécurité réelle pour protéger le site web contre les attaques en temps réel.

### Étape 4 : Évaluer la conformité

Généralement, cette phase est simplement une continuation de la phase précédente. Mais dans un audit, un poids égal est donné aux risques et à la conformité. Cela signifie que nous devrons effectuer une revue de conformité séparée pour toutes les mesures prises pour atténuer les risques.

Les réglementations de l'industrie et les normes de sécurité telles que le RGPD, PCI DSS, les meilleures pratiques en cybersécurité et ISO 27001 (Système de Management de la Sécurité de l'Information) sont applicables à WalkGen. Évaluer si ces normes sont maintenues et suivies est important – sinon le site web pourrait faire face à des menaces ou à des amendes lourdes pour non-conformité.

Ces cadres sont des cadres généraux et fondamentaux qui doivent être respectés par presque toutes les entreprises, quel que soit leur modèle de fonctionnement. Mais il existe certains cadres qui sont plus spécifiques aux entreprises comme WalkGen.

Un cadre spécifique pour walkGen serait ISO 22301 (Système de Management de la Continuité des Activités - SMCA), qui aide à garantir que walkGen peut continuer ses opérations pendant les cyberattaques (si cela se produit). Il garantit également que l'entreprise crée des plans de reprise après sinistre et d'atténuation des risques pour se préparer au pire scénario.

> **Note :** Si un contrôle de sécurité est efficace pour atténuer le risque mais n'est toujours pas conforme aux réglementations, il est considéré comme un signal d'alarme en matière de sécurité.

À ce stade, 95 % de l'audit est terminé. Les membres de l'équipe réalisant l'audit devraient avoir une compréhension claire des risques gérés, du modèle de sécurité fonctionnel, des cadres mis en œuvre et des protocoles de sécurité que WalkGen respecte.

### Étape 5 : Communiquer aux parties prenantes

Cette phase conclut le processus d'audit pour walkGen et fournit les résultats de l'audit aux équipes de sécurité pertinentes et aux membres du conseil d'administration, tels que les fondateurs et le PDG. Ce rapport les aide à comprendre les résultats et à déterminer les prochaines étapes pour le site web, y compris le montant du financement qui devrait être alloué aux mesures de sécurité nécessaires.

Le rapport pour les équipes de sécurité contiendra de nombreuses nuances techniques, telles que la portée du site web, la manière dont les vulnérabilités sont identifiées (avec des extraits de code), et un guide détaillé de chaque vulnérabilité. En revanche, le rapport pour les personnes non techniques, y compris potentiellement les fondateurs et les PDG, fournira des informations de haut niveau sur l'audit et les lacunes en matière de sécurité.

Typiquement, le rapport d'audit de WalkGen fournit des informations telles que :

* Un résumé des risques identifiés et des menaces gérées

* Les cadres de sécurité mis en œuvre

* L'état de conformité : Des déclarations telles que "WalkGen respecte les normes de l'industrie comme le RGPD et ISO 22301."

* Recommandations et étapes suivantes, incluant les améliorations de sécurité suggérées, les exigences budgétaires de sécurité et les plans d'action respectifs pour WalkGen.

## Conclusion

Les entreprises devraient réaliser des audits de sécurité régulièrement. Chaque fois, elles devraient comparer les résultats actuels avec ceux de l'audit précédent pour vérifier les analyses et l'état de sécurité de l'organisation.

J'espère que cet article vous a donné une meilleure idée de ce qui est impliqué dans un audit de sécurité et pourquoi ils sont nécessaires pour les entreprises à réaliser régulièrement. Il est important pour les entreprises de rester résilientes face aux cybermenaces, de réduire les risques potentiels et juridiques, et de maintenir la confiance des clients dans ce monde numérique en évolution.