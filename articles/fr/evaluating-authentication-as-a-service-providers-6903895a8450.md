---
title: Comment choisir le meilleur fournisseur d'authentification en tant que service
  pour votre entreprise
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-14T23:43:50.000Z'
originalURL: https://freecodecamp.org/news/evaluating-authentication-as-a-service-providers-6903895a8450
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GiwpKyF5sjUV3ObYeEjkrg.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment choisir le meilleur fournisseur d'authentification en tant que
  service pour votre entreprise
seo_desc: 'By Jeff Okawa

  Have you ever wondered how to choose an authentication service provider?

  We are amid a growing trend of using federated identifiers to provide authentication
  to the websites we use everyday.

  We can log in to countless applications using...'
---

Par Jeff Okawa

Avez-vous déjà pensé à la manière de choisir un fournisseur de services d'authentification ?

Nous sommes au milieu d'une tendance croissante à utiliser des identifiants fédérés pour fournir une authentification aux sites web que nous utilisons quotidiennement.

Nous pouvons nous connecter à d'innombrables applications en utilisant nos comptes de réseaux sociaux, nos comptes professionnels ont tous des capacités SSO, et nous pouvons même nous connecter aux sites web gouvernementaux en utilisant nos identifiants de banque en ligne.

Conceptuellement, l'authentification (et le SSO) est simple, mais il est difficile et coûteux de la mettre en œuvre correctement. Bien que les entreprises se soient traditionnellement concentrées sur la création de fonctionnalités, elles doivent désormais également se concentrer sur la réduction de la contention d'inscription des utilisateurs sans exposer l'application à des vulnérabilités. Tout comme les plateformes d'infrastructure cloud (comme AWS) permettent désormais aux entreprises de se concentrer sur la création d'applications, nous voyons la même chose se produire avec l'authentification.

L'authentification en tant que service (ou fournisseurs de services d'authentification) fournit des services d'authentification et de gestion des utilisateurs pour les applications.

Ils ne sont pas seulement un fournisseur d'identité, mais fournissent des pages de connexion utilisateur configurables (ou widgets), des fonctionnalités de déconnexion, des identités fédérées avec des comptes de réseaux sociaux, des bases de données utilisateur et un certain degré de gestion des utilisateurs. Ils ont des capacités prêtes à l'emploi pour prendre en charge les protocoles d'authentification courants tels que SAML et OpenID Connect.

Les clients entreprises souhaitant le SSO peuvent souvent tirer parti de configurations faciles en un clic avec des applications tierces comme JIRA, Office 365 et Salesforce grâce à l'utilisation de SAML2.

#### Quels sont vos objectifs ?

Parfois, la mise en œuvre de systèmes d'authentification pour une application peut sembler réinventer la roue. Le concept d'authentification en tant que service (AaaS) tente de résoudre ce problème, mais il y a des choses à considérer avant de choisir un fournisseur (ou de décider de déployer une solution personnalisée).

![Image](https://cdn-media-1.freecodecamp.org/images/690m1zOxXGxOynRY0yzJ23OehrWIdOoAWWok)

### Critères

![Image](https://cdn-media-1.freecodecamp.org/images/BCWmPrRoCmu6GKPSRAXX-n0UBeG9muMmGHLM)

Une fois que vous avez établi une liste des considérations importantes pour votre organisation, il est temps de commencer à évaluer les fournisseurs d'authentification en tant que service (AaaSp) sur le marché. Au cours des dernières années, nous avons vu un nombre de fournisseurs AaaS entrer et disparaître. Cela rend le choix du bon AaaS d'autant plus critique. Ils viennent sous toutes les formes et tailles — des petites entreprises avec peu de clients aux grands fournisseurs établis pour les entreprises.

### Confiance et réputation

Confier quelque chose d'aussi important que l'authentification nécessite une grande confiance, il est donc important que le fournisseur choisi soit **réputé** et une **autorité** **de confiance** en matière d'authentification. Considérez si leur architecture a été examinée par d'autres experts en sécurité et examinez les commentaires en ligne sur le fournisseur.

Comme nous l'avons vu avec Stormpath (racheté par Okta en 2017, puis abandonné l'API Stormpath), le fait de s'appuyer sur un fournisseur tiers ouvre le risque d'abandon par le fournisseur. Dans le pire des cas, comme ce fut le cas avec l'acquisition mentionnée ci-dessus, beaucoup se sont retrouvés sans chemin de migration de Strompath vers Okta et ont dû déployer leurs propres systèmes d'authentification.

La taille du fournisseur, la liste des clients et le profil de l'entreprise sont des lignes directrices générales qui peuvent être prises en considération, mais vous prenez toujours un risque. Les petits fournisseurs de démarrage peuvent offrir des incitations significatives, mais leur capacité à disparaître rapidement sans préavis peut en faire un choix risqué. Alternativement, les grands fournisseurs peuvent toujours fermer leurs services si cette ligne de business devient non rentable.

### Utilisateurs cibles

Certains fournisseurs AaaS, comme One Login, se concentrent exclusivement sur le B2E — offrant une expérience SSO pour les employés internes d'une entreprise avec leurs services basés sur le web. Pensez aux pages portails d'entreprise avec des liens vers les ressources RH, le Wiki de l'entreprise, Sharepoint et Salesforce. Auth0 et AWS Cognito sont des fournisseurs servant à la fois le B2E et le B2C et prennent explicitement en charge les clients qui ont des centaines de milliers de clients.

### Verrouillage par le fournisseur

L'intégration avec un AaaS introduit une quantité plus significative d'interdépendance que l'intégration d'une pile d'applications sur une solution basée sur le cloud, car du code spécifique au fournisseur **doit** être écrit pour compléter l'intégration.

Non seulement cela doit être annulé, mais plus de code d'intégration pour le nouveau fournisseur devra être écrit. Passer d'un AaaS à une solution personnalisée est encore plus coûteux, car tout devrait être écrit à partir de zéro.

Contrairement aux changements d'infrastructure, où des portes d'atténuation existent pour réduire l'interruption des utilisateurs, le changement de fournisseurs AaaS aura presque toujours un impact sur les utilisateurs. N'oubliez pas, nous changeons des composants qui interagissent directement avec les utilisateurs finaux.

**Importation de données**
La plupart des fournisseurs AaaS définissent un mécanisme d'importation des utilisateurs dans leur système par importation en masse (où les utilisateurs doivent passer par un flux de réinitialisation du mot de passe) ou par un processus de migration graduelle. Avec la migration graduelle, les identifiants de l'utilisateur sont d'abord validés par rapport à l'ancienne base de données, puis chiffrés et stockés dans la nouvelle base de données. Dans ce cas d'utilisation, les utilisateurs ne sont pas impactés par la migration.

**Exportation de données**
Cette fonctionnalité est particulièrement importante dans le cas où les applications utilisent le stockage de données de l'AaaS. Pour des raisons de sécurité, les fournisseurs AaaS ne publient pas leur algorithme de hachage des mots de passe. Par conséquent, lorsqu'une exportation est requise, tous les utilisateurs doivent initier un flux de réinitialisation du mot de passe.

Si cela ne semble pas assez grave, de nombreux fournisseurs AaaS **NE FOURNISSENT PAS** de fonctionnalité d'exportation de données en masse, ajoutant ainsi une complexité supplémentaire et des étapes manuelles pour migrer les données utilisateur hors d'un AaaS.

**Sous-traitants**
Certains services offerts par les fournisseurs AaaS sont fournis par un autre service tiers. La 2FA/MFA et l'email sont parfois des fonctionnalités qui nécessitent des inscriptions séparées (et un paiement supplémentaire) avec le tiers.

Prenons l'exemple de la 2FA, certains services AaaS ne vous permettent pas de choisir le fournisseur de 2FA sous-jacent et vous obligent à utiliser leur fournisseur préféré. Non seulement vous êtes forcé de vous associer à ce fournisseur, mais vous êtes également forcé de payer leurs tarifs (où des alternatives moins chères sont parfois disponibles).

### Support technologique

**Protocoles**
La plupart des fournisseurs AaaS supportent les principaux protocoles fédérés (OpenID Connect et SAML). D'autres ont des connecteurs supplémentaires permettant des sources de données personnalisées (Microsoft AD ou LDAP) et des configurations faciles pour des applications tierces comme JIRA, Office 365 et Salesforce grâce à l'utilisation de SMAL.

**Intégration**
L'intégration du service AaaS dans votre application peut encore être une tâche significative (surtout si vous exécutez une application héritée). Par conséquent, une considération est de voir si l'AaaS offre des bibliothèques pour votre pile technologique.

Par exemple : La plupart des principaux fournisseurs AaaS, ainsi que les sites web de réseaux sociaux, fournissent des bibliothèques clientes pour demander, consommer et valider divers jetons et documents d'authentification. Si vous exécutez une pile Java, de nombreux services offrent des bibliothèques Java à inclure dans votre projet pour tout traitement backend. Si votre pile est supportée, le processus d'intégration peut être aussi simple que d'ajouter un fichier JS, d'inclure un JAR et de remplir quelques valeurs dans une valeur de propriété.

**Documentation**
Une documentation abondante et bien écrite ainsi qu'un support communautaire faciliteront grandement l'intégration. Certains fournisseurs offrent des projets de démarrage et des exemples pour vous aider à commencer.

**Autres fonctionnalités**
De nombreux services offrent des fonctionnalités supplémentaires telles que le profilage des utilisateurs, l'email et la 2FA/MFA.

### Interfaces utilisateur et flux personnalisables

Les fournisseurs AaaS permettent divers niveaux de personnalisation pour les pages UI, les widgets et les attributs utilisateur. De plus, certains systèmes ont des "hooks" où la personnalisation des flux peut avoir lieu (consultez Auth0 et AWS Cognito pour plus de détails).

Selon votre organisation spécifique, il peut être difficile de trouver un équilibre entre la satisfaction des besoins UX et ce qui est personnalisable (dans la raison) par le fournisseur. Dans certains cas, les flux demandés par l'entreprise peuvent ne pas être supportés par votre AaaS choisi.

#### Une note sur la personnalisation :

Les capacités d'authentification prêtes à l'emploi sont l'un des grands avantages de l'utilisation d'un AaaS. Lorsque les composants pré-construits sont utilisés, l'intégration est incroyablement simple.

D'autre part, une personnalisation poussée de l'UI et des flux augmente le temps et la complexité. Vous pourriez vous retrouver à personnaliser si lourdement et extensivement l'UI et les flux d'authentification que vous **devez** vous demander si ce sera _moins cher_ de déployer une solution personnalisée en interne (en considérant également le coût annuel). La réponse pourrait être **OUI**.

Ma recommandation est de retenir autant de personnalisation que possible dans le cadre de l'AaaS. Cela est particulièrement vrai pour les flux d'authentification et de réinitialisation du mot de passe, car l'ajout de personnalisation à ces composants tend à augmenter la complexité de l'intégration et à créer un verrouillage par le fournisseur.

### Support de développement et de test

#### Environnements de développement, QA et production

Certaines entreprises ont des environnements de développement et de QA isolés. Pour supporter ces exigences, _certains_ fournisseurs AaaS permettent à un seul compte d'avoir plusieurs bases de données d'identité. Malheureusement, ce n'est pas une fonctionnalité universelle et plusieurs comptes avec l'AaaS peuvent être nécessaires pour supporter chaque environnement de test.

#### Test de charge

Tous les systèmes AaaS interdisent les tests de charge non autorisés. Cela peut poser un problème si votre application nécessite un test de charge de bout en bout pour être approuvée pour la production. Dans ce cas, certains fournisseurs AaaS permettent les tests de charge s'ils sont pré-autorisés avant que le test ne commence. Il y a souvent des contraintes strictes et des délais sous lesquels le test doit être exécuté.

De manière plus réaliste, vous devrez probablement implémenter un mécanisme de contournement de connexion pour l'application afin de supporter les tests de charge.

### Tarification

Les modèles de tarification varient considérablement entre les fournisseurs AaaS. Certains fournisseurs offrent des incitations pour les petites organisations en démarrage et ont un niveau le plus bas gratuit ou très abordable. En général, attendez-vous à voir un graphique de prix/utilisateur comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/IYF8Igkb7oZ3CSnlFjfhfYDl4i3T8varqj4L)

Le prix par utilisateur est initialement très bas (ou 0 $), ce qui est idéal pour les petites organisations ou les start-ups avec des volumes faibles. Cependant, à mesure que votre base d'utilisateurs grandit, le prix/utilisateur reste constant. Finalement, il commencera à diminuer après un certain point, car vous avez soit atteint le niveau d'utilisation le plus élevé, soit vous êtes en position de négocier les prix.

Le coût peut sembler raisonnable au début, mais une fois que vous êtes verrouillé, une application avec 100 000 utilisateurs actifs par mois pourrait voir une facture annuelle de 150k à 200k !

Si votre application a déjà une base d'utilisateurs de plusieurs centaines de milliers d'utilisateurs, il pourrait être moins cher de déployer votre propre solution ! En plus des frais par utilisateur, il y a souvent des frais pour des services supplémentaires que vous pourriez encourir (à nouveau, 2FA et email).

**B2C**
Négociez le prix si votre application a des périodes d'utilisation intensive. Certains services ont des prix variables par mois en fonction du nombre d'utilisateurs actifs réels, tandis que d'autres fixent le prix par mois en fonction d'une estimation du mois le plus chargé de l'année (peu importe le nombre d'utilisateurs qui utilisent réellement le système). La différence entre ces plans de prix peut être significative.

**B2E**
Les prix sont toujours fixés à un montant par compte employé. Méfiez-vous des frais minimaux dans les petits caractères !

#### Gestion des utilisateurs et tableau de bord

La plupart des AaaS ont une forme de gestion des utilisateurs de base intégrée dans leurs tableaux de bord d'administration. Dans certains cas, vous pouvez créer des comptes non-administrateurs pour vos représentants du service client ou d'autres associés afin de modifier les identités des utilisateurs.

Donner des comptes administrateurs complets aux employés simplement pour qu'ils aient accès au tableau de bord de gestion des utilisateurs doit être **évité**. Le compte administrateur ne doit être entre les mains que des employés appropriément formés, sinon vous risquez que quelqu'un supprime accidentellement votre base de données utilisateur entière ou expose les identités des utilisateurs.

Que le tableau de bord intégré de l'AaaS réponde ou non à vos besoins dépend des changements d'attributs des utilisateurs quotidiens que votre organisation doit apporter. Assurez-vous que l'AaaS fournit une piste d'audit/de journalisation appropriée conformément aux politiques de votre organisation.

### SLA et service client

Un contact direct avec un gestionnaire de compte du fournisseur n'est pas offert par tous les fournisseurs AaaS. Les niveaux gratuits ou à faible utilisation n'ont souvent accès qu'aux forums communautaires. Certains fournisseurs offrent un support payant, des serveurs dédiés, un accès aux journaux et une conformité HIPAA/PCI à un coût supplémentaire.

La plupart des AaaS offrent le SLA standard de 99,9 % à 99,995 % de temps de fonctionnement, mais cela permet toujours des temps d'arrêt au cours de l'année. Cela peut être important si votre application **doit** être disponible pendant des périodes critiques. Certains AaaS offrent des solutions d'entreprise (déploiements personnalisés) pour garantir une certaine forme de redondance en cas de défaillance du système.

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/H3CZpMrLwvZuPRuzkW1jyGYnok2JCK7luv8c)

Pour les start-ups, les AaaS offrent une solution abordable pour l'authentification afin que vous puissiez vous concentrer sur votre produit. Pour les grandes organisations avec des applications héritées et une base d'utilisateurs établie, vous devez prendre en considération une liste beaucoup plus large de critères pour vous assurer de sélectionner l'AaaS qui répond à vos besoins de migration, d'audit/journalisation et de budget.

En complément, j'ai [écrit une introduction aux identités fédérées et à l'authentification](https://medium.com/@dev78digital/655a160d66cb).