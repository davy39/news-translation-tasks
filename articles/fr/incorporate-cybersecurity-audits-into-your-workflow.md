---
title: Comment intégrer les audits de cybersécurité dans votre flux de travail
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-03-22T16:25:10.000Z'
originalURL: https://freecodecamp.org/news/incorporate-cybersecurity-audits-into-your-workflow
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-pixabay-39584.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: penetration testing
  slug: penetration-testing
- name: Security
  slug: security
seo_title: Comment intégrer les audits de cybersécurité dans votre flux de travail
seo_desc: "The word \"audit\" describes any process designed to review and assess\
  \ a system's current state, capacity, and integrity. \nAn internal audit is a review\
  \ process initiated and carried out by an organization itself. External audits are\
  \ often performed by..."
---

Le mot "audit" décrit tout processus conçu pour examiner et évaluer l'état actuel, la capacité et l'intégrité d'un système. 

Un audit _interne_ est un processus de révision initié et réalisé par une organisation elle-même. Les audits _externes_ sont souvent effectués par ou pour le compte d'entités bancaires ou d'organismes de réglementation gouvernementaux tels que les autorités fiscales.

## Audits de sécurité : quel est l'intérêt pour vous ?

En théorie du moins, tous les audits technologiques partagent quelques objectifs communs. Ils visent à confirmer que vos systèmes fonctionnent avec des niveaux de sécurité et d'efficacité acceptables, et qu'ils sont conformes à toutes les normes applicables. 

Le but n'est pas seulement de s'assurer que toutes les bonnes cases sont cochées, mais de rechercher réellement les problèmes cachés afin de pouvoir les corriger.

Dans ce contexte, vous devriez considérer la conformité aux Frameworks réglementaires comme la norme de sécurité des données de l'industrie des cartes de paiement "Payment Card Industry Data Security Standard" (connue sous le nom de PCI-DSS) ou la loi américaine sur la portabilité et la responsabilité de l'assurance maladie "Health Insurance Portability and Accountability Act" (HIPAA) comme des opportunités précieuses. 

Si vous pouvez légitimement passer ces normes, vous pouvez alors être assez confiant quant au fait que vous faites réellement ce que vous pouvez pour protéger la confidentialité et la sécurité des données que vous gérez. Et plus important encore, que vos systèmes sont raisonnablement sécurisés contre les menaces courantes.

Cet article est tiré de mon [cours d'Introduction à la Cybersécurité](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://www.youtube.com/watch?v=HiHHrTpon3Q&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO&]

## Audits de sécurité : comment fonctionnent-ils

À toutes fins utiles, un audit de sécurité formel implique l'inspection et le test de tous les systèmes qui pourraient avoir un impact sur la sécurité d'une manière ou d'une autre. 

Vous pourriez, par exemple, être tenu de démontrer :

* Que vos données au repos et en transit sont toujours cryptées
* Que tous les serveurs et postes de travail impliqués dans votre entreprise sont correctement corrigés (patched)
* Que vos réseaux bloquent l'accès à tous sauf aux utilisateurs nécessaires
* Que les fournisseurs tiers dont vous utilisez les opérations et les produits respectent également les normes de sécurité nécessaires
* Que vous disposez d'un protocole efficace pour les sauvegardes régulières des données
* Que vous disposez de plans d'intervention et de récupération d'urgence formels – et testés –

Même si c'est un gouvernement ou une banque qui vous pousse à le faire – et même si la mise en conformité totale est très coûteuse – les objectifs fondamentaux sont bien alignés avec vos propres intérêts, ce n'est donc certainement pas une perte de temps totale.

## Outils d'audit de sécurité

Laissez-moi décrire rapidement trois catégories d'outils d'audit. 

### Traitement et analyse des journaux système (logs)

Que votre pile d'infrastructure réside dans le cloud, sur site ou les deux, au fil du temps, vous allez régulièrement générer des gigaoctets de données ennuyeuses. 

La seule façon de donner un sens à ce désordre est de le diffuser via des scripts d'analyse capables de filtrer le bruit généré par des millions d'événements normaux et de trouver les événements graves. Les bons systèmes de surveillance des journaux (qui incluent Splunk, Nagios, Syslog-ng et Datadog) peuvent être configurés pour envoyer des alertes lorsque des problèmes potentiels sont détectés, ou même déclencher des corrections automatiques.

Si vous gérez quelque chose de plus complexe qu'un site Web WordPress et quelques ordinateurs portables, vous aurez probablement besoin d'un type de processus de surveillance. Une forme de surveillance de bas niveau est un système de détection d'intrusion (IDS). 

Un IDS est un logiciel que vous installez sur un serveur dont la fonction est de surveiller en permanence l'état des fichiers système et de configuration prédéfinis. Si un fichier cible est mis à jour ou supprimé – ce qui pourrait indiquer une activité non autorisée – l'IDS enverra une alerte à un ou plusieurs administrateurs. Une fois que vous avez peaufiné votre IDS pour qu'il ne vous envoie pas de faux positifs gênants tout le temps, il peut constituer une première ligne de défense efficace.

L'installation et la configuration d'un logiciel IDS peuvent être beaucoup plus faciles que vous ne le pensez. Les packages populaires incluent Snort et Security Onion.

### Tests d'intrusion (Pen testing)

Un testeur d'intrusion (pen tester) est généralement un consultant indépendant embauché par une organisation pour tenter de pirater ses systèmes _internes_. 

En d'autres termes, les testeurs d'intrusion reçoivent une autorisation légale explicite pour faire exactement ce que feraient les pirates criminels – sans causer de dommages permanents, bien sûr. 

En utilisant des suites de logiciels d'attaque comme OWASP ZAP ou Metasploit, les testeurs d'intrusion recherchent puis exploitent les vulnérabilités des systèmes d'une organisation. Plus un testeur peut pénétrer loin, plus les vulnérabilités découvertes sont dangereuses et plus vous aurez de travail à faire pour les corriger.

Les tests d'intrusion sont coûteux et parfois même perturbateurs. Mais pas autant que de subir les mêmes intrusions par un véritable pirate malveillant. 

Une autre forme de test d'intrusion consiste à diviser vos administrateurs et ingénieurs en attaquants (red team) et défenseurs (blue team) pour des simulations d'attaque. Les équipes s'affrontent pour tester la robustesse de vos défenses.

Le déploiement d'un test d'intrusion complet peut être complexe. Le plus souvent, les organisations font appel à des prestataires tiers pour planifier et réaliser un test.

### Évaluations de vulnérabilité

Il s'agit d'une forme de test d'intrusion moins invasive. Plutôt que d'essayer de pénétrer dans vos réseaux et serveurs, les testeurs de vulnérabilité scanneront votre réseau de l'extérieur à la recherche de ports ouverts et de logiciels non patchés. Ils fouilleront également Internet à la recherche d'informations que vos employés pourraient avoir laissées par inadvertance sur des plateformes publiques et qui pourraient fournir des indices sur des identifiants actifs ou la "recette secrète" utilisée par vos applications logicielles. 

Comment cela pourrait-il fonctionner ? Eh bien, il existe des logiciels gratuits (comme OpenVAS et Burp Suite) qui, par exemple, récolteront des données à partir d'offres d'emploi que vous auriez pu publier sur LinkedIn – en particulier à partir des sections « compétences requises ». 

De tels logiciels peuvent également surveiller les publications publiques des membres de votre équipe, en évaluant les sujets d'intérêt dans leurs questions et réponses sur Stack Overflow. Si ces informations circulent, vous voudrez le savoir.

## Conclusion

Les audits de sécurité sont d'une importance capitale. Que vous les réalisiez pour satisfaire à des exigences réglementaires ou pour protéger vos actifs – ou les deux – vous devez absolument les prendre au sérieux.

**Cet article et la vidéo qui l'accompagne sont des extraits de [mon cours d'Introduction à la Cybersécurité](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). Et il y a bien d'autres ressources technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com)**