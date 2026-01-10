---
title: Comment utiliser Keycloak pour la gestion des identités et des accès
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2025-01-23T13:59:09.428Z'
originalURL: https://freecodecamp.org/news/keycloak-identity-and-access-management
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737640179567/36b76fb3-3e9f-4124-a4d5-bb7d11428a6c.png
tags:
- name: authentication
  slug: authentication
- name: IAM
  slug: iam
- name: keycloak
  slug: keycloak
- name: SSO
  slug: sso
- name: single sign on
  slug: single-sign-on
seo_title: Comment utiliser Keycloak pour la gestion des identités et des accès
seo_desc: Whether your deployment requires logins from hundreds of thousands of end
  users or just a few remote admins, there's no escaping the need to properly control
  access to your infrastructure. And integrating those logins with industry-standard
  tools lik...
---

Que votre déploiement nécessite des connexions de centaines de milliers d'utilisateurs finaux ou simplement de quelques administrateurs distants, il est impossible d'échapper à la nécessité de contrôler correctement l'accès à votre infrastructure. Et l'intégration de ces connexions avec des outils standard de l'industrie comme LDAP et Active Directory peut réduire la quantité de travail nécessaire pour vous lancer.

Keycloak est une solution de gestion des identités et des accès (IAM) open source, prête pour l'entreprise, qui est scalable, extensible et robuste. Et elle ne nécessite pas beaucoup de maintenance pour lancer une implémentation simple.

Cet article vous présentera la technologie et les moyens par lesquels elle peut intégrer une authentification conforme aux meilleures pratiques dans votre infrastructure.

*Note sur les contributions de Hitachi à Keycloak :*

Takashi Norimatsu travaille pour Hitachi et est le mainteneur officiel de Keycloak depuis fin 2021. Hitachi contribue activement à Keycloak depuis au moins 2018.

[Hitachi semble faire davantage stratégiquement avec l'open source en général](https://www.hitachi.com/New/cnews/month/2024/11/241108.html) et Keycloak en particulier. Je crois qu'un soutien corporatif fort et continu dans le cadre d'un projet open source est un signe positif, mais à tout le moins, vous devriez être conscient du soutien corporatif pour Keycloak lors de votre évaluation.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737406737359/1fc95289-7777-4c9f-a651-00bd8a44b517.png align="center")

## Prise en main de Keycloak

Je vais commencer par un bref "guide de démarrage rapide". Comme vous pouvez le voir sur cette capture d'écran, Keycloak fonctionne parfaitement sur plusieurs plateformes. Et leur [documentation produit est excellente](https://www.keycloak.org/guides).

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737406768154/a84122e2-1e72-43a8-86f2-aeaddd0c3a3b.png align="center")

Mais voici une syntaxe Docker très simple en une seule commande qui créera une instance Keycloak entièrement fonctionnelle sur votre machine locale :

```bash
docker run -p 8080:8080 \
     -e KC_BOOTSTRAP_ADMIN_USERNAME=admin \
     -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:26.0.7 start-dev
```

C'est tout. Après une minute ou deux, vous pouvez ouvrir l'interface d'administration dans votre navigateur en utilisant la variation appropriée de :

[localhost:8080](http://localhost:8080)

Sur la base des paramètres par défaut de la commande Docker, vous vous connecterez en utilisant admin et admin. Passez quelques minutes à explorer l'environnement pour vous familiariser avec les outils disponibles.

## Ce que Keycloak offre

D'accord. Alors pourquoi avez-vous besoin de Keycloak ? Parce qu'il prend en charge toutes les fonctionnalités requises par les déploiements modernes. Cela inclut l'authentification unique (SSO) pour permettre une authentification transparente sur plusieurs applications et services, OAuth2, OpenID Connect, la conformité au protocole SAML, et les identités fédérées utilisant des configurations LDAP ou Active Directory existantes ou via des connexions de médias sociaux comme Google.

Keycloak incorpore l'utilisation de l'authentification multifacteur (MFA), des mécanismes intégrés de révocation et d'expiration des jetons, une gestion fine des permissions via le contrôle d'accès basé sur les rôles (RBAC), et un chiffrement de bout en bout pour les communications sensibles. La conformité au RGPD, à la HIPAA et à la PCI DSS sont toutes possibles.

Keycloak est livré avec une API RESTful pour les interactions scriptées et programmatiques. Cela encouragera l'automatisation des tâches pour optimiser davantage vos processus d'authentification. Et vos développeurs peuvent créer leurs propres plugins personnalisés pour combler les lacunes d'utilisabilité que vous rencontrez.

## Le cas d'affaires pour Keycloak

Parce que Keycloak est open source, il n'y aura pas de frais de licence à craindre. Mais l'open source vous offre bien plus que simplement "peu coûteux".

Keycloak élimine le verrouillage par le fournisseur, vous permettant de travailler avec n'importe quelle plateforme ou fournisseur de cloud - ou de passer entre eux chaque fois que nécessaire. Il peut également réduire les coûts opérationnels globaux grâce à ses déploiements simplifiés (combien de temps vous a-t-il fallu pour lancer cette image Docker ?), des mises à jour automatisées, et aucune limite ou pénalité de coût même pour des millions d'appels API mensuels ou d'utilisateurs actifs.

Avoir un accès prêt à l'emploi (et gratuit) à l'ensemble complet des fonctionnalités (y compris RBAC et MFA) simplifie également la planification et l'exécution. Il n'y a rien de "plus" efficace que d'avoir à attendre une semaine pour accéder à des fonctionnalités payantes jusqu'à ce que vous obteniez une réponse à votre demande de financement supplémentaire pour le projet. Toutes les fonctionnalités de Keycloak sont à un clic de distance.

Ce graphique radar illustre les différences de fonctionnalités et de fonctionnalités entre Keycloak et ses principaux concurrents commerciaux.

![Différences entre Keycloak, Okta, Auth0 et Azure AD](https://cdn.hashnode.com/res/hashnode/image/upload/v1737407002045/d9a45f49-afbb-4709-a9da-016782d7c6ae.png align="center")

### Points à considérer

Autant Keycloak a à offrir, il ne sera pas le choix idéal pour tous les cas d'utilisation. Et il y a des problèmes dont vous devriez être conscient dès le départ.

Par exemple, bien que le démarrage puisse être facile, la configuration complète, par exemple, du clustering et de la haute disponibilité pour Keycloak peut être complexe pour les équipes sans expérience en gestion des identités. La gestion des problèmes de latence pour des déploiements très importants peut être difficile.

Et bien que la documentation soit généralement excellente, elle peut ne pas traiter pleinement des complexités spécifiques ou des scénarios de cas particuliers. De même, il n'y a pas de ressource au sein de la communauté Keycloak qui offre un soutien garanti. Bien qu'il existe d'excellents fournisseurs tiers.

Il est possible que, parce que vous ne travaillez pas avec un produit commercial, la démonstration de la conformité réglementaire puisse être un peu plus impliquée. Vous devrez peut-être également adapter votre fonctionnalité de journalisation pour vous conformer à diverses exigences de piste d'audit.

Enfin, les environnements personnalisables risquent d'introduire une complexité déstabilisante. Plus vos plugins et implémentations d'API s'éloignent des sentiers battus, plus les chances que quelque chose finisse par casser sont grandes - surtout autour des mises à niveau de version.

## Vos prochaines étapes

Il est toujours utile d'explorer les parcours que d'autres personnes ont pris avec une nouvelle technologie.

Ainsi, [cette page](https://www.redhat.com/en/blog/keycloak-success-stories-from-the-openshift-commons-gathering-amsterdam-2023) inclut des informations sur une étude de cas fascinante impliquant une banque japonaise qui cherchait une solution API et a choisi Keycloak en raison de ses fonctionnalités de sécurité API de haut niveau. La présentation de Yuichi Nakamura [à l'événement OpenShift Commons en 2023](https://youtu.be/jH7-tyrUP9E?si=6gKMdYH-o0LMiYFZ&t=490) donne des détails sur la manière dont la banque a utilisé avec succès Keycloak pour sécuriser leurs API. Nakamura, stratège en chef OSS de Hitachi, a récemment été nommé à la tête du bureau du programme open source de Hitachi (OSPO).

Et [ci-dessous se trouve un compte rendu](https://hossted.com/knowledge-base/case-studies/infrastructure-and-network/security/enhancing-authentication-services-with-freeipa-and-keycloak/) d'une université qui a implémenté Kerberos Single Sign-On (SSO) pour FreeIPA et configuré Keycloak pour se connecter avec FreeIPA. L'université a réussi à réaliser l'authentification des utilisateurs à partir de Keycloak en utilisant l'option SSSD sous "user federation" au lieu de s'appuyer sur Kerberos ou LDAP.

Je ne suis pas étranger à Keycloak moi-même, ayant enseigné un [cours de prise en main de Keycloak sur Pluralsight](https://www.pluralsight.com/courses/keycloak-getting-started). Pour les débutants, ce peut être un bon point de départ. Un essai gratuit de 10 jours est disponible.