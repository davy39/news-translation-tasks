---
title: Qualité des données à l'ère de l'I.A.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-21T17:05:40.000Z'
originalURL: https://freecodecamp.org/news/data-quality-in-the-era-of-a-i-d8e398a91bef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mpT-JZf1lnZhAixk_fP7bQ.jpeg
tags:
- name: analytics
  slug: analytics
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: software development
  slug: software-development
seo_title: Qualité des données à l'ère de l'I.A.
seo_desc: 'By George Krasadakis

  Data quality is of critical importance especially in the era of Artificial Intelligence
  and automated decisions. Do you have a strategy?


  _Database clipart from [dumielauxepices](https://dumielauxepices.net/wallpaper-70986"
  rel="...'
---

Par George Krasadakis

#### La qualité des données est d'une importance critique, surtout à l'ère de l'intelligence artificielle et des décisions automatisées. Avez-vous une stratégie ?

![Image](https://cdn-media-1.freecodecamp.org/images/ssFde9l5rMynXaW4k2Mz9Gb0PpGh4Qcb2te0)
_Clipart de base de données provenant de [dumielauxepices](https://dumielauxepices.net/wallpaper-70986" rel="noopener" target="_blank" title=")._

### Les projets intensifs en données ont un point de défaillance unique : la qualité des données

En tant que directeur de [datamine decision support systems](http://www.datamine.gr), j'ai livré plus de 80 projets intensifs en données dans divers secteurs et entreprises de haut niveau. Ceux-ci incluent l'**entreposage de données**, l'**intégration de données**, l'**intelligence d'affaires**, la **performance de contenu** et les **modèles prédictifs**. Dans la plupart des cas, la qualité des données s'est avérée être un facteur critique pour le succès du projet.

Le défi évident dans chaque cas était d'interroger efficacement des sources de données hétérogènes, puis d'extraire et de transformer les données vers un ou plusieurs **modèles de données**.

Le défi non évident était l'**identification précoce** des problèmes de données, qui — dans la plupart des cas — étaient inconnus des propriétaires des données également.

Nous avons stratégiquement commencé chaque projet avec une phase d'évaluation de la qualité des données — ce qui, dans de nombreux cas, a conduit à des modifications de la portée du projet et même à des initiatives et projets supplémentaires de nettoyage des données.

### Qualité des données définie

Il existe de nombreux aspects de la qualité des données, notamment la **cohérence, l'intégrité, l'exactitude** et l'**exhaustivité**. Selon [Wikipedia](https://en.wikipedia.org/wiki/Data_quality), les données sont généralement considérées comme de haute qualité si elles sont « adaptées à [leurs] utilisations prévues dans les opérations, la prise de décision et la planification, et les données sont jugées de haute qualité si elles représentent correctement la construction du monde réel à laquelle elles se réfèrent. »

Je définis la qualité des données comme le niveau de conformité d'un ensemble de données avec une normalité contextuelle.

Cette **normalité** est définie par des règles définies par l'utilisateur et/ou dérivées statistiquement. Elle est contextuelle, dans le sens où les règles **reflètent la logique** de processus métiers particuliers, de connaissances corporatives, de conditions environnementales, sociales ou autres. Par exemple, une propriété de la même entité pourrait avoir différentes règles de validation dans différentes entreprises, marchés, langues ou devises.

Les systèmes modernes doivent prendre conscience de la qualité des données en entrée/sortie. Ils doivent identifier instantanément les problèmes potentiels et **éviter d'exposer** des données sales, inexactes ou incomplètes aux composants/clients de production connectés.

Cela implique que, même s'il y a une situation problématique soudaine entraînant des entrées de données de mauvaise qualité, le système sera en mesure de gérer le problème de qualité et de **notifier proactivement** les bons utilisateurs. Selon la criticité des problèmes, il pourrait également **refuser de servir les données** à ses clients — ou servir les données tout en signalant les problèmes potentiels.

![Image](https://cdn-media-1.freecodecamp.org/images/mubexRhZMCnyoo7UTwMcJmC75FlGdAQr3uC-)
_Icône d'infini cyber de [iconspng](https://www.iconspng.com/image/93060/cyber-infinity" rel="noopener" target="_blank" title=")._

### L'importance de la qualité des données

La qualité des données est d'une **importance critique**, surtout à l'ère des décisions automatisées, de l'IA et de l'optimisation continue des processus. [Les entreprises doivent être axées sur les données](https://medium.freecodecamp.org/the-data-driven-corporation-259b5b84f9c9) et la qualité des données est une condition préalable critique pour y parvenir.

#### **Confusion, confiance limitée, mauvaises décisions**

Dans la plupart des cas, les problèmes de qualité des données expliquent la confiance limitée dans les données de la part des utilisateurs corporatifs, le gaspillage de ressources ou même des **mauvaises décisions**.

Imaginez une équipe d'analystes essayant de déterminer si un point aberrant est une découverte commerciale critique ou un problème de données inconnu/mal géré. Pire encore, imaginez des décisions en temps réel prises par un système incapable d'identifier et de gérer des données de mauvaise qualité qui ont été accidentellement — ou même intentionnellement — introduites dans le processus.

#### **Échecs dus à une faible qualité des données**

J'ai vu de grandes initiatives de Business Intelligence, d'entreposage de données et similaires échouer en raison d'un **faible engagement** des utilisateurs clés et des parties prenantes. Dans la plupart des cas, le faible engagement était le résultat direct d'un **manque de confiance** dans les données. Les utilisateurs doivent faire confiance aux données — s'ils ne le font pas, ils abandonneront progressivement le système, impactant ses principaux KPI et critères de succès.

Chaque fois que vous pensez avoir fait une découverte majeure de données, vérifiez d'abord les problèmes de qualité !

#### Types et symptômes

Les problèmes de qualité des données peuvent prendre de nombreuses formes, par exemple :

* des propriétés particulières dans un objet spécifique ont des valeurs invalides ou manquantes
* une valeur arrivant dans un format inattendu ou corrompu
* des instances en double
* des références ou unités de mesure incohérentes
* des cas incomplets
* des URL brisées
* des données binaires corrompues
* des paquets de données manquants
* des lacunes dans les flux
* des propriétés mal mappées

#### La cause profonde

Les problèmes de qualité des données sont généralement le résultat de :

* de mauvaises implémentations logicielles : bugs ou mauvaise gestion de cas particuliers
* de problèmes au niveau du système : échecs dans certains processus
* de changements dans les formats de données, impactant les sources et/ou les destinations de données

Les systèmes modernes doivent être conçus en supposant qu'à un moment donné, il y aura des flux de données problématiques et des problèmes de qualité inattendus.

La validité des propriétés des données peut être évaluée par rapport à [a] des règles connues et prédéfinies et [b] des règles et motifs dérivés dynamiquement basés sur un traitement statistique.

### Une stratégie pour la qualité des données

Un projet moderne intensif en données implique généralement des flux de données, des processus ETL complexes, une logique de post-traitement et une gamme de composants analytiques ou cognitifs.

Le livrable clé dans de tels scénarios est un pipeline de traitement de données haute performance, alimentant et maintenant au moins un magasin de données. Cela définit un « environnement de données », qui permet ensuite des modèles analytiques avancés, une prise de décision en temps réel, une extraction de connaissances et éventuellement des applications d'IA. Ce qui suit décrit une stratégie pour garantir la qualité des données tout au long de ce processus.

#### Identifier, comprendre et documenter les sources de données

Vous devez identifier vos sources de données et, pour chacune d'elles, documenter brièvement ce qui suit :

1. **Type de données contenues** — par exemple, des enregistrements clients, du trafic web, des documents utilisateurs, des activités provenant d'un appareil connecté (dans un contexte IoT).

2. **Type de stockage** — par exemple, est-ce un fichier plat, une base de données relationnelle, un magasin de documents ou un flux d'événements ?

3. **Périodes** — depuis combien de temps avons-nous des données ?

4. **Fréquence et types** de mises à jour — recevez-vous des deltas, des événements, des mises à jour, des données agrégées ? Tout cela peut avoir un impact significatif sur la conception du pipeline et la capacité à identifier et à gérer les problèmes de qualité des données.

5. **La source des données et les systèmes impliqués** — les données proviennent-elles d'un autre système ? Est-ce un flux continu d'événements ou un processus par lots extrait d'un autre système intégré ? Y a-t-il une saisie/validation manuelle des données impliquée ?

6. **Problèmes de données connus** et limitations peuvent aider à accélérer la phase d'examen initial des données **si** fournis à l'avance.

7. **Les modèles de données impliqués** dans la source de données particulière — par exemple, un modèle ER représentant des clients, une structure de fichier plat, un objet, un schéma en étoile.

8. **Parties prenantes impliquées** — cela est très important afin d'interpréter les problèmes et les cas particuliers et également pour valider l'état global des données, avec ceux qui ont la compréhension la plus profonde des données, de l'entreprise et des processus associés.

![Image](https://cdn-media-1.freecodecamp.org/images/KXylHmRJfqxCGwaTaGjjNjpr-rjjDCaui7eu)
_Clones ordinateur cube données de [pixabay](https://pixabay.com/en/clones-computer-cube-data-2029896/" rel="noopener" target="_blank" title=")._

#### Commencer par le profilage des données

Le **[profilage des données](https://en.wikipedia.org/wiki/Data_profiling)** est le processus de description des données en effectuant une analyse statistique descriptive de base et une synthèse. La **clé** est de documenter brièvement les résultats, créant ainsi une base de référence — un point de référence à utiliser pour la validation des données tout au long du processus.

Le profilage des données dépend du type des données sous-jacentes et du contexte métier, mais dans un scénario général, vous devriez considérer ce qui suit :

1. Identifier les principales **entités**, telles que client, utilisateur, produit, les **événements** impliqués, tels que l'enregistrement, la connexion, l'achat, la **période**, la **géographie**, et autres dimensions clés de vos données.

2. Sélectionner la **période typique** à utiliser pour votre analyse. Cela pourrait être un jour, une semaine, un mois, etc., selon l'entreprise.

3. Analyser les **tendances** de haut niveau impliquant les entités et les événements identifiés. Générer des séries temporelles contre les principaux événements et les principales entités. Identifier les tendances, la saisonnalité, les pics, et essayer de les interpréter dans le contexte de l'entreprise particulière. Consultez le propriétaire des données et capturez/documentez ces « histoires de données ».

4. **Analyser** les données. Pour chacune des propriétés de vos principales entités, effectuer une synthèse statistique pour capturer la **forme** des données. Pour les valeurs numériques, vous pourriez commencer par les bases — min, moyenne, max, écart-type, quartiles — et ensuite éventuellement visualiser la distribution des données. Ayant fait cela, examinez la forme de la distribution et déterminez si elle a du sens pour l'entreprise. Pour les valeurs catégorielles, vous pourriez résumer le nombre distinct de valeurs par fréquence et, par exemple, documenter les x valeurs principales expliquant z% des cas.

5. Examiner quelques **valeurs aberrantes**. Ayant la distribution des valeurs pour une propriété particulière — disons, l'âge du client — essayez de déterminer les valeurs « suspectes » dans le contexte de l'entreprise particulière. Sélectionnez quelques-unes d'entre elles et récupérez les instances réelles des entités. Ensuite, examinez leur profil et leur activité — des utilisateurs particuliers, dans cet exemple — et essayez d'interpréter les valeurs suspectes. Consultez le propriétaire des données pour obtenir des conseils sur ces résultats.

6. **Documenter** vos résultats. Créez un document ou un rapport compact avec une structure claire pour servir de base de référence et de référence de données. Vous devriez ajouter les résultats de chacune des sources de données à ce document unique — avec la même structure, les mêmes références temporelles et les mêmes métadonnées pour garantir une interprétation plus facile.

7. **Examiner, interpréter, valider**. C'est la phase où vous avez besoin de l'apport du propriétaire des données pour fournir une interprétation globale des données, et pour expliquer les cas particuliers, les valeurs aberrantes ou d'autres motifs de données inattendus. Le résultat du processus pourrait être de confirmer l'état des données, d'expliquer les problèmes connus et d'enregistrer de nouveaux. C'est là que des solutions possibles aux problèmes de données connus peuvent être discutées et/ou décidées. De plus, les règles de validation peuvent être documentées.

Dans un **scénario idéal**, le processus de profilage des données devrait être automatisé. Il existe plusieurs outils permettant un profilage rapide des données en connectant simplement votre source de données et en passant par une configuration rapide de type assistant. Le résultat du processus dans de tels scénarios est généralement un rapport interactif permettant une analyse facile des données et le partage des connaissances avec l'équipe.

![Image](https://cdn-media-1.freecodecamp.org/images/ty763uwNNP42a6p5TMPsTsz7CzfIBHjY6UkP)
_Analyse de données de [kissclipart](https://www.kissclipart.com/data-analyze-clipart-data-analysis-31xywg/" rel="noopener" target="_blank" title=")._

#### Établir un magasin de référence de qualité des données

Les objectifs du magasin de référence de qualité des données (DQR) sont de capturer et de maintenir des **métadonnées** et des règles de **validité** concernant vos données, et de les rendre disponibles pour les processus externes.

Cela pourrait être un système hautement sophistiqué pour dériver automatiquement des règles sur la validité de vos données et évaluer en continu les cas entrants (par lots), avec la capacité d'identifier des motifs liés au temps et autres concernant vos données. Cela pourrait être un ensemble de règles maintenues manuellement qui permettent une validation rapide des données entrantes. Cela pourrait être une configuration hybride.

Dans tous les cas, le processus ETL doit pouvoir interroger le magasin DQR et charger les règles et motifs de validation des données, ainsi que les directives de correction. Les règles de validation des données doivent être **dynamiques** plutôt qu'un ensemble fixe de règles ou des morceaux de logique codés en dur.

Le magasin DQR doit également être accessible via des rapports interactifs et des tableaux de bord standardisés — pour permettre aux propriétaires de processus et aux analystes de données de comprendre les données, le processus, les tendances et les problèmes.

**Voir aussi** : [Choisir entre R et Python](https://medium.com/innovation-machine/choosing-between-r-and-python-a-digital-analysts-guide-b7103f80aa4e)

#### Implémenter une validation intelligente des données

Permettez à votre pipeline de **traitement de données** de charger les règles de validation des données à partir du magasin DQR décrit ci-dessus. Le magasin DQR pourrait être conçu comme un sous-système ETL interne ou un service externe à l'ETL. Dans tous les cas, la logique de validation des données ainsi que l'action suggérée doivent être dynamiques pour votre processus ETL.

Le pipeline de traitement des données doit valider en continu les cas entrants (par lots) en fonction de la dernière version des règles de validation.

Le système doit être capable de signaler et éventuellement enrichir les données entrantes originales avec le résultat de la validation et les métadonnées associées, et de renvoyer les informations au magasin DQR. Les données originales sont stockées, avec un signalement approprié par l'ETL, **sauf** indication contraire de la politique de validation actuelle.

Avec cette approche, la qualité des données peut être mesurée et analysée dans le temps, par exemple par source de données, pipeline de traitement. Les rapports interactifs peuvent aider à explorer facilement l'état global du processus ETL et à identifier et explorer rapidement les préoccupations ou problèmes spécifiques de qualité des données.

Le système pourrait également prendre en charge un « Index de Qualité des Données » global. Celui-ci peut prendre en compte plusieurs aspects de la qualité et accorder plus d'importance à des entités et événements spécifiques. Par exemple, un enregistrement de transaction erroné pourrait être bien plus important qu'un hyperlien brisé vers une image.

L'Index de Qualité des Données pourrait également avoir une **élasticité** spécifique — différente selon l'entité et l'événement. Par exemple, cela pourrait permettre des retards dans la réception des données pour une entité particulière, mais pas pour une autre.

Avoir un Index de Qualité des Données global peut aider l'entreprise à mesurer la qualité des données dans le temps et à travers les dimensions clés de l'entreprise. Cela peut également aider à fixer des objectifs et à quantifier l'impact des améliorations potentielles de la stratégie ETL.

> **Voir aussi** : [Comment l'intelligence artificielle change le monde](https://medium.com/innovation-machine/artificial-intelligence-fe713f283cfb)

#### Une couche de notification intelligente

L'ensemble du processus doit être conscient de tout problème de qualité, tendances et changements soudains. De plus, le système doit connaître l'importance — à quel point un problème est critique. Sur la base de cette conscience et d'une couche de configuration intelligente, le système sait quand notifier qui et par quel canal particulier.

Les systèmes modernes doivent être conscients de la qualité des données entrantes et capables d'identifier, de signaler et de gérer les cas erronés de manière appropriée.

> **Lire plus sur l'IA**

> [Intelligence Artificielle : Risques et Préoccupations](https://medium.com/@gkrasadakis/artificial-intelligence-risks-concerns-2a19ba21cfd9)

> [Intelligence Artificielle : l'impact sur l'emploi et la main-d'œuvre](https://hackernoon.com/artificial-intelligence-3c6d80072416)

> [Intelligence Artificielle : Une introduction non technique — définition, applications et impact](https://hackernoon.com/artificial-intelligence-fe713f283cfb)

> [Quoi de neuf sur l'IA, la RA, la RV, les NUI, la Robotique, les Données et la Visualisation, la Blockchain](https://medium.com/innovation-machine/2018-innovation-trends-and-opportunities-8a5d642fd661)