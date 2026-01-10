---
title: Terminologie du RGPD en anglais simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-23T07:57:35.000Z'
originalURL: https://freecodecamp.org/news/gdpr-terminology-in-plain-english-6087535e6adf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6hCZUnZq19I_UvHv4sIp9w.jpeg
tags:
- name: data
  slug: data
- name: '#gdpr'
  slug: gdpr
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Terminologie du RGPD en anglais simple
seo_desc: 'By Alex Ewerlöf

  My team builds the technologies for some of the highest traffic newsrooms in Sweden
  and Norway. Part of the revenue comes from selling ads. Ads sell best when personalised,
  and for personalization you need data. Internet’s default bus...'
---

Par Alex Ewerlöf

Mon équipe développe les technologies pour certaines des salles de rédaction les plus fréquentées en Suède et en Norvège. Une partie des revenus provient de la vente de publicités. Les publicités se vendent mieux lorsqu'elles sont personnalisées, et pour la personnalisation, vous avez besoin de données. Le modèle économique par défaut d'Internet est basé sur les publicités. Le RGPD a de grandes implications pour les entreprises en ligne comme les salles de rédaction.

Mais voici la partie intéressante — le Règlement Général sur la Protection des Données (RGPD) impose des restrictions sur les données qui peuvent être collectées, comment elles peuvent être utilisées, et pendant combien de temps elles peuvent être stockées.

Cet article vise à démystifier les termes clés du RGPD afin que tout le monde puisse comprendre ce sujet intéressant. Si vous êtes européen ou avez des utilisateurs européens, vous devez comprendre le RGPD.

> TL;DR; il s'agit d'un énorme changement dans la manière dont les données personnelles sont collectées, passant de « par défaut » à « opt-in ». Plus quelques autres avantages.

Voici une vidéo qui résume le tout à un niveau basique :

Avant de commencer, une rapide mise en garde : je ne représente pas mes employeurs actuels ou précédents sur mon blog personnel. Les informations fournies ici sont purement basées sur mes propres recherches et ne reflètent pas nécessairement les politiques, la stratégie ou la mise en œuvre du RGPD de mon entreprise.

### Un peu de contexte

Le RGPD est entré en vigueur le 25 mai. Malgré le fait qu'il complique la vie des développeurs et des marketeurs, il s'agit en réalité d'un très bon accord pour les utilisateurs finaux. Le RGPD empêche les entreprises de collecter des informations dont elles n'ont pas besoin (strictement parlant).

Bien qu'il commence par le mot « Général », le RGPD est en réalité une loi de l'Union Européenne (UE) qui s'applique à :

1. Les entreprises basées dans l'UE
2. Les entreprises qui collectent des données personnelles auprès de citoyens européens.

Peut-être que ce « Général » est une bonne chose, car une grande partie d'Internet est européenne !

![Image](https://cdn-media-1.freecodecamp.org/images/1*jS0wmtrioU6pGFsVO6sS7g.gif)
_Utilisation mondiale d'Internet sur 24 heures ([wikipedia](https://en.wikipedia.org/wiki/Global_Internet_usage" rel="noopener" target="_blank" title="))_

Le mot « Règlement » dans RGPD signifie qu'il doit être appliqué dans son intégralité à travers l'UE.

À long terme, cela conduit à la **protection de la vie privée dès la conception**. Il s'agit d'un principe qui exige l'inclusion de la protection des données dès le début de la conception des systèmes, plutôt qu'en tant que réflexion après coup.

### Terminologie courante

Voici une liste des termes les plus courants du RGPD :

* Une **personne concernée** est une personne (comme vous et moi) dont les données personnelles sont traitées par un responsable du traitement (comme une entreprise ou un service que nous utilisons).
* Un **responsable du traitement** est une organisation qui collecte des données auprès des résidents de l'UE. Il détermine les finalités, les conditions et les moyens du traitement des données personnelles.
* L'entité qui effectue le traitement réel des données est appelée un **sous-traitant** — un exemple pourrait être un fournisseur de services cloud.
* Le **traitement** implique toute opération effectuée sur des données personnelles, qu'elle soit ou non automatisée. Cela inclut la collecte, l'utilisation, l'enregistrement, l'alimentation d'algorithmes de machine learning (lisez [comment le ML est affecté par le RGPD](https://www.oreilly.com/ideas/how-will-the-gdpr-impact-machine-learning)), et ainsi de suite.

### Le RGPD pour les utilisateurs

Vos **données personnelles** sont toute information qui peut être utilisée pour vous identifier directement ou indirectement. Par exemple : votre nom, votre adresse, votre photo, votre adresse e-mail, vos coordonnées bancaires, vos publications sur les réseaux sociaux, vos informations médicales, ou une adresse IP de votre ordinateur ou mobile.

Ces données sont généralement utilisées pour le **profilage**, dans lequel des processus automatisés évaluent, analysent ou prédisent votre comportement. Par exemple, connaître votre âge signifie que vous serez exposé à des publicités ciblant votre groupe d'âge. Cela est également vrai pour les données que vous ne donnez pas explicitement à une entreprise, comme votre adresse IP, qui sera utilisée pour deviner votre localisation.

Maintenant que le RGPD est en vigueur, les entreprises ont des limitations sur les données personnelles qu'elles peuvent collecter et sur la durée pendant laquelle elles peuvent les stocker. Elles doivent justifier pourquoi elles en ont besoin.

#### Quand les entreprises ONT BESOIN du consentement de l'utilisateur

Le responsable du traitement (entreprise) ne peut pas simplement collecter les données des utilisateurs. Ils doivent d'abord demander votre permission ou consentement.

Le consentement doit être explicite pour les données collectées et pour les finalités pour lesquelles les données sont utilisées. Le consentement est donné librement (si vous dites « non », l'entreprise doit toujours vous servir aussi bien que possible sans vos données). Le consentement ne doit pas être considéré comme donné librement si la personne concernée n'a pas de choix réel ou libre ou est incapable de refuser ou de retirer son consentement sans préjudice. Le consentement doit être spécifique et explicite sur les données collectées et la manière dont elles sont traitées. L'utilisateur a le droit **de retirer son consentement à tout moment**, mais plus important encore, **il doit être aussi facile de retirer son consentement que de le donner**.

Les entreprises ne peuvent plus vous forcer à cocher une case qui dit « J'accepte tous les termes et conditions et les politiques de confidentialité ». C'est pourquoi vous avez reçu ces e-mails de nombreux sites web vous informant de leurs politiques avant la date limite du 25 mai.

Le domaine du consentement RGPD a un certain nombre d'implications pour les entreprises qui enregistrent les appels par habitude. Les avertissements typiques « les appels sont enregistrés à des fins de formation et de sécurité » ne suffiront plus à obtenir un consentement présumé pour enregistrer les appels.

#### Quand les entreprises N'ONT PAS BESOIN du consentement de l'utilisateur

Il doit y avoir une base légale raisonnable pour collecter une donnée précise. Selon le [site du RGPD](https://www.gdpreu.org/the-regulation/key-concepts/legitimate-interest/), cela peut être lorsque :

* Le traitement est nécessaire à l'exécution d'un contrat auquel la personne concernée est partie ou pour prendre des mesures à la demande de la personne concernée avant la conclusion d'un contrat.
* Le traitement est nécessaire au respect d'une obligation légale à laquelle le responsable du traitement est soumis.
* Le traitement est nécessaire pour protéger les intérêts vitaux de la personne concernée ou d'une autre personne physique.
* Le traitement est nécessaire à l'exécution d'une mission d'intérêt public ou relevant de l'exercice de l'autorité publique dont est investi le responsable du traitement.
* Le traitement est nécessaire aux fins des intérêts légitimes poursuivis par le responsable du traitement ou par un tiers, sauf si ces intérêts sont surmontés par les intérêts ou les [droits fondamentaux](https://en.wikipedia.org/wiki/Charter_of_Fundamental_Rights_of_the_European_Union) et les libertés de la personne concernée, qui nécessitent une protection des données personnelles, en particulier si la personne concernée est un enfant.

Le principal avantage du RGPD est qu'il [donne le contrôle](https://gdpr-info.eu/chapter-3/) aux utilisateurs pour :

1. Effacer leurs données quand ils le souhaitent (également connu sous le nom de [Droit à l'oubli](https://en.wikipedia.org/wiki/Right_to_be_forgotten)). Les demandes de **suppression de données** ne s'arrêtent pas au responsable du traitement. Si des sous-traitants tiers sont impliqués, ils doivent également cesser de traiter les données et les effacer. Je suppose qu'il y aura une norme API de facto pour cela, mais jusqu'à présent, c'est plus ad-hoc et dépend de la manière dont les services communiquent entre eux. Je suis sûr qu'à l'avenir, il y aura des services où vous leur donnez vos informations personnelles et ils vérifieront des milliers de services en ligne pour vous fournir un rapport agrégé des sites qui ont vos informations. Les entreprises doivent fournir un moyen de vérifier si elles ont des données pour un utilisateur particulier (sans nécessiter d'inscription). Trivia : cela est essentiellement en contradiction avec le fonctionnement de la Blockchain ! Lisez plus sur [les implications du RGPD pour la Blockchain ici](https://medium.com/@alexewerlof/gdpr-for-blockchain-f73744b9be34).
2. Posséder leurs données ! Les personnes concernées (utilisateurs) peuvent télécharger et voir leurs données et comment elles sont traitées. De plus, le responsable du traitement doit informer la personne concernée sur les détails du traitement, tels que les finalités du traitement, avec qui les données sont partagées, et comment elles ont été acquises. Cela s'appelle le **droit d'accès** ou **droit d'accès du sujet**. Les données personnelles [ne peuvent pas être transférées vers des pays en dehors de l'Union Européenne](http://ec.europa.eu/justice/data-protection/international-transfers/index_en.htm) sauf s'ils garantissent le même niveau de protection des données.
3. Transférer leurs données vers des concurrents. Cela est bon pour la concurrence et finalement les utilisateurs gagnent. Les données doivent être fournies par le responsable du traitement dans un format électronique standardisé et couramment utilisé. Plus de verrouillage ! Cela est connu sous le nom de **portabilité des données**. Cela ouvrira probablement un tout nouveau segment commercial pour la conversion des formats de données d'un responsable du traitement à un autre.
4. Mettre à jour/corriger leurs données. Les personnes concernées ont le droit de demander aux responsables du traitement de corriger immédiatement les données (publiques ou privées) qui sont invalides.

Je trouve personnellement l'annonce de **violation de données** incroyable.

Le responsable du traitement est tenu, en vertu d'une obligation légale, de notifier à l'autorité de contrôle compétente toute violation de données sans retard indu, sauf si la violation est susceptible d'entraîner un risque pour les droits et libertés des personnes concernées.

Les individus doivent être notifiés si un impact négatif est déterminé. Il y a un maximum de 72 heures après avoir pris connaissance de la violation de données pour faire le rapport. De plus, le sous-traitant devra notifier le responsable du traitement sans retard indu après avoir pris connaissance d'une violation de données personnelles.

Vous vous souvenez [quand Yahoo a gardé sa violation secrète pendant deux ans](https://www.washingtonpost.com/news/the-switch/wp/2016/11/10/yahoo-discovered-hack-leading-to-major-data-breach-two-years-before-it-was-disclosed/?noredirect=on&utm_term=.4782fea5e3e5) ? Eh bien, plus maintenant !

### Le RGPD pour les gouvernements

Puisque le RGPD est une grande affaire, les gouvernements sont impliqués pour protéger leurs citoyens et faire respecter les réglementations. Il y a deux termes à comprendre :

* Les **autorités nationales de protection des données** ([DPA](https://www.whitecase.com/publications/article/chapter-14-data-protection-authorities-unlocking-eu-general-data-protection)) sont désignées par chaque pays de l'UE pour mettre en œuvre et faire respecter la loi sur la protection des données, et pour offrir des conseils. **Autorité de contrôle** (SA) [est un autre nom](https://www.i-scoop.eu/supervisory-authorities-consistency-and-data-protection-authorities-dpas/#What_is_a_Data_Protection_Authority_or_DPA_in_the_scope_of_the_GDPR) pour DPO. Comme indiqué dans le chapitre 16, les DPA ont des pouvoirs de contrôle significatifs, y compris la capacité d'imposer des amendes substantielles. Elles sont également le lieu où aller en cas de violation de la législation sur la protection des données (dans le cadre du RGPD pour les citoyens de l'UE) et pour des conseils et des questions spécifiques et/ou de l'assistance du point de vue des organisations.
* Un **délégué à la protection des données** ([DPO](https://www.whitecase.com/publications/article/chapter-12-impact-assessments-dpos-and-codes-conduct-unlocking-eu-general-data)) est un employé du responsable du traitement (entreprise) qui est officiellement chargé de veiller à ce qu'une organisation soit consciente de ses responsabilités en matière de protection des données et s'y conforme. Plus d'informations à ce sujet dans la section suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q6HO-CQ7tHOUAd0s9tG6xA.png)
_DPA & DPO_

Chaque membre de l'UE a un établissement principal où les décisions clés sur le traitement des données sont prises.

### Le RGPD pour les entreprises

La limite supérieure des amendes pour violation du RGPD est assez élevée : jusqu'à 20 millions d'euros, ou jusqu'à 4 % du chiffre d'affaires annuel mondial de l'exercice financier précédent... selon le montant le plus élevé !

Les entreprises qui collectent des données ont la responsabilité et l'obligation de mettre en œuvre et de démontrer qu'elles se conforment au RGPD. Cela s'appelle la **conformité**.

Les entreprises doivent tenir un journal de qui a accédé à quelles informations pour lorsque les autorités demandent un audit. Les enregistrements des activités de traitement doivent être maintenus, y compris les finalités du traitement, les catégories impliquées et les délais prévus.

Les enregistrements doivent être mis à la disposition de l'autorité de contrôle sur demande. La partie intéressante est que même si le traitement réel est effectué par une autre entreprise (un sous-traitant au nom du responsable du traitement), c'est toujours l'entreprise qui collecte les données qui porte la responsabilité principale.

Cette toute nouvelle gamme d'exigences est suffisamment compliquée pour créer un nouveau titre de poste : délégué à la protection des données (DPO) ! Il s'agit d'un rôle de leadership en matière de sécurité de l'entreprise responsable de la supervision de la stratégie et de la mise en œuvre de la protection des données pour garantir la conformité.

Ils doivent également :

* Éduquer l'entreprise et les employés sur les exigences importantes de conformité
* Être le point de contact entre l'entreprise et les autorités de contrôle
* Surveiller et fournir des conseils sur les efforts de protection des données dans toute l'entreprise
* Garder une trace de toutes les activités de traitement des données dans l'entreprise, y compris la finalité de toutes les activités de traitement, qui doit être rendue publique sur demande
* Répondre aux demandes des utilisateurs concernant l'utilisation de leurs données, le droit à l'effacement des données et les questions concernant les mesures que l'entreprise a mises en place pour protéger leurs informations personnelles
* Identifier et réduire les risques pour la vie privée des entités en analysant les données personnelles traitées et les politiques en place pour protéger les données, ce qui s'appelle **l'évaluation d'impact sur la protection des données**. Le RGPD [impose une EIPD](https://www.itgovernance.co.uk/privacy-impact-assessment-pia) pour être réalisée lorsque le traitement des données est susceptible d'entraîner un risque élevé pour les droits et libertés des personnes physiques.

Le DPO doit avoir une équipe de soutien et sera également responsable du développement professionnel continu pour être indépendant de l'organisation qui l'emploie, effectivement en tant que « mini-régulateur ».

Si une entreprise a plusieurs établissements dans l'UE, elle aura une seule autorité de contrôle en tant qu'autorité principale, basée sur l'endroit où les principales activités de traitement des données ont lieu.

### Le RGPD pour les développeurs

Puisque le RGPD impose la **protection de la vie privée dès la conception**, il affecte l'architecture logicielle et sa mise en œuvre. Par exemple, nous ne pouvons plus conserver de journaux d'informations sensibles (comme mentionné précédemment, les adresses IP sont considérées comme des informations personnelles). Cela rend le traçage des bugs un peu plus difficile.

Les paramètres de confidentialité doivent donc être définis à un niveau élevé par défaut. Nous devons donc nous assurer que les cases à cocher qui exposent les données personnelles ne sont pas cochées par défaut.

Si le Cloud est utilisé pour le stockage des données, seul le propriétaire des données, et non le service cloud, doit détenir les clés de déchiffrement.

Nous ne pouvons pas stocker les données plus longtemps que nécessaire. Les colonnes de la base de données doivent avoir une **date limite de conservation des données** qui spécifie quand les données doivent être supprimées.

Les informations personnellement identifiables doivent être **pseudonymisées** de manière à ce qu'elles ne puissent plus être liées (ou « attribuées ») à une seule personne concernée sans l'utilisation de données supplémentaires.

Lisez plus sur [les techniques de pseudonymisation dans mon nouvel article](https://medium.com/@alexewerlof/gdpr-pseudonymization-techniques-62f7b3b46a56).

### Exceptions au RGPD

À quoi bon une loi si elle n'est pas faite pour être enfreinte ? Ne vous emballez pas trop pour vos droits, car les cas suivants ne sont pas couverts par le règlement :

* Interception légale, sécurité nationale, armée, police, justice
* Analyse statistique et scientifique pour la recherche
* Les personnes décédées sont soumises à la législation nationale
* Il existe une loi dédiée aux relations employeur-employé. Le RGPD a été développé avec un accent sur les réseaux sociaux et les fournisseurs de cloud, mais n'a pas suffisamment pris en compte les exigences pour le traitement des données des employés.
* Traitement des données personnelles par une personne physique dans le cadre d'une activité strictement personnelle ou domestique

### Remerciements

Merci à ma collègue [Ioana Norgen](https://www.linkedin.com/in/ioanadodu/) pour la relecture de cet article avant sa publication. Toutes les erreurs éventuelles sont encore les miennes.

### Sources

* Un [glossaire](https://www.eugdpr.org/glossary-of-terms.html) des termes du RGPD
* [Techniques de pseudo-anonymisation](https://gdpr.report/news/2017/11/07/data-masking-anonymisation-pseudonymisation/)
* [Wikipedia](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)
* [Délégué à la protection des données](https://digitalguardian.com/blog/what-data-protection-officer-dpo-learn-about-new-role-required-gdpr-compliance)

### Lectures intéressantes

* [ePrivacy](https://en.wikipedia.org/wiki/EPrivacy_Regulation_(European_Union)), un ensemble de réglementations connexes qui sont également appliquées en même temps que le RGPD. Il cible toute entreprise qui fournit une forme de service de communication en ligne, utilise des technologies de suivi en ligne, ou s'engage dans le marketing direct électronique (par exemple, les opérateurs de télécommunications et les services de communication en ligne comme Skype et WhatsApp). Son aspect le plus important est la protection contre les SMS/emails de spam et les appels marketing.
* Un [excellent guide sur le RGPD pour les développeurs](https://techblog.bozho.net/gdpr-practical-guide-developers/) et quelques [belles diapositives](https://techblog.bozho.net/gdpr-developers-presentation/)
* Belitsoft a créé [une excellente checklist pour les entreprises sur le RGPD](https://belitsoft.com/gdpr-compliance-checklist) bien que tous les éléments de la checklist ne soient pas une exigence du RGPD et certains comme l'authentification à deux facteurs soient plus une bonne pratique.
* [Comment le RGPD affecte les cookies utilisés pour le suivi](https://techblog.bozho.net/tracking-cookies-gdpr/)
* Le paquet de réforme de la protection des données comprend également [une directive distincte sur la protection des données](http://eur-lex.europa.eu/eli/dir/2016/680/oj/eng) pour la police et le secteur de la justice pénale qui fournit des règles sur les échanges de données personnelles aux niveaux national, européen et international.
* [Facebook et Google frappés par 8,8 milliards de dollars de poursuites le premier jour du RGPD](https://www.theverge.com/2018/5/25/17393766/facebook-google-gdpr-lawsuit-max-schrems-europe)
* [Protection de la vie privée dès la conception](https://en.wikipedia.org/wiki/Privacy_by_design)

> Le fond du problème est : le RGPD est un droit évident. L'Europe a été pionnière dans son établissement, mais cela devrait être un droit mondial. Parlez-en avec vos amis, collègues et législateurs si vous souhaitez bénéficier de la même protection et du même choix que les Européens.

Si vous avez aimé cela, vous pourriez apprécier : [la programmation est le meilleur travail jamais](https://medium.com/@alexewerlof/what-s-cool-about-being-a-programmer-5a1e58efeee6) et [comment je me tiens au courant de la technologie](https://medium.com/@alexewerlof/how-i-learn-new-tech-cb79db19c818).