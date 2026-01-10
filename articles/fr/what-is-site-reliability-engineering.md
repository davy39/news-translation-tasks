---
title: Qu'est-ce que l'ingénierie de la fiabilité des sites (SRE) ? Un guide pour
  débutants
subtitle: ''
author: Omolade Ekpeni
co_authors: []
series: null
date: '2025-03-26T16:07:59.395Z'
originalURL: https://freecodecamp.org/news/what-is-site-reliability-engineering
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743005263079/95dfe528-a274-4172-8a06-46187c1668eb.png
tags:
- name: SRE
  slug: sre
- name: SRE devops
  slug: sre-devops
- name: Site Reliability Engineering
  slug: site-reliability-engineering
- name: Cloud
  slug: cloud
- name: Devops
  slug: devops
- name: Technical Support
  slug: technical-support
seo_title: Qu'est-ce que l'ingénierie de la fiabilité des sites (SRE) ? Un guide pour
  débutants
seo_desc: 'In today’s digital age, we expect our online experiences to be fast, reliable,
  and always available. But what happens behind the scenes to make our expectations
  a reality?

  The answer is Site Reliability Engineering (SRE). SRE is a discipline that ens...'
---

À l'ère numérique d'aujourd'hui, nous attendons de nos expériences en ligne qu'elles soient rapides, fiables et toujours disponibles. Mais que se passe-t-il en coulisses pour que nos attentes deviennent réalité ?

La réponse est l'ingénierie de la fiabilité des sites (SRE). Le SRE est une discipline qui garantit que vos services en ligne préférés continuent de fonctionner sans accroc, même lorsque les choses tournent mal.

Dans ce guide, vous apprendrez les principes fondamentaux du SRE, comment l'automatisation peut vous aider dans ce processus, comment gérer les échecs, et bien plus encore.

## Table des matières

* [SRE : Plus que simplement résoudre des problèmes](#heading-sre-est-plus-que-simplement-resoudre-des-problemes)
    
* [Combler le fossé entre le développement et les opérations](#heading-combler-le-fosse-entre-le-developpement-et-les-operations)
    
* [Les principes fondamentaux du SRE](#heading-les-principes-fondamentaux-du-sre)
    
    * [Se concentrer sur la disponibilité et la fiabilité](#heading-se-concentrer-sur-la-disponibilite-et-la-fiabilite)
        
    * [Adopter l'automatisation](#heading-adopter-lautomatisation)
        
    * [Mesurer tout](#heading-mesurer-tout)
        
    * [Travailler avec les développeurs](#heading-travailler-avec-les-developpeurs)
        
    * [Apprendre de l'échec](#heading-apprendre-de-lechec)
        
* [Le rôle du SRE : Un équilibre délicat](#heading-le-role-du-sre-un-equilibre-delicat)
    
* [Pourquoi l'automatisation est importante](#heading-pourquoi-lautomatisation-est-importante)
    
* [Points clés à retenir pour toute personne impliquée dans les services numériques](#heading-points-cles-a-retenir-pour-toute-personne-impliquee-dans-les-services-numeriques)
    
* [Conclusion](#heading-conclusion)
    

## SRE : Plus que simplement résoudre des problèmes

Le SRE va au-delà de la réaction aux pannes. Il s'agit d'une approche proactive pour construire et maintenir des systèmes fiables. Vous pouvez le considérer comme un mélange des opérations informatiques traditionnelles, de l'ingénierie logicielle et d'une quête incessante d'automatisation.

Vous avez peut-être entendu parler du SRE en même temps que du DevOps, alors différencions-les. DevOps est un ensemble plus large de principes visant à améliorer la collaboration et l'automatisation tout au long du cycle de vie du développement logiciel. L'ingénierie de la fiabilité des sites (SRE), en revanche, est une mise en œuvre spécifique de ces principes DevOps, avec un fort accent sur les aspects opérationnels de l'exploitation de systèmes à grande échelle et hautement fiables.

Imaginons une entreprise de logiciels qui souhaite adopter DevOps. Elle pourrait commencer le processus en favorisant une meilleure communication et des objectifs communs entre ses équipes de développement (qui écrivent le code) et ses équipes d'exploitation (qui exécutent le code en production). De plus, elles pourraient mettre en place des pipelines d'intégration continue et de livraison continue (CI/CD) pour automatiser le processus de construction, de test et de déploiement des logiciels. Cela s'aligne sur l'accent mis par DevOps sur des cycles de publication plus rapides et une collaboration améliorée.

Au sein de cette entreprise orientée DevOps, l'équipe SRE pourrait être spécifiquement chargée d'assurer la fiabilité de leur plateforme de commerce électronique. Ils prendraient les principes généraux de DevOps et les appliqueraient aux défis opérationnels rencontrés avec une vision d'ingénierie logicielle.

Par exemple, ils pourraient :

* définir et mesurer les objectifs de niveau de service (SLO)
    
* développer et mettre en œuvre des systèmes automatisés de surveillance et d'alerte
    
* créer une infrastructure auto-réparatrice et des playbooks de réponse aux incidents automatisés
    
* collaborer avec les équipes de développement dès le début du cycle de vie du développement logiciel pour garantir la fiabilité
    
* mener des revues post-incident sans blame pour tirer des leçons des échecs
    
* et suivre et automatiser le "toil".
    

### Combler le fossé entre le développement et les opérations

Comme vous pouvez le voir, le SRE est étroitement lié à DevOps. L'une des façons dont le SRE met en œuvre les principes DevOps est de combler le fossé entre le développement et les opérations. Les SRE peuvent le faire de plusieurs manières.

Tout d'abord, les SRE partagent la responsabilité avec les équipes de développement pour la fiabilité et les performances des applications en production. Cela aide à favoriser un environnement collaboratif et garantit que les préoccupations opérationnelles sont prises en compte tout au long du cycle de vie du développement logiciel.

Les SRE fournissent également des commentaires précieux aux équipes de développement sur la base de leur expérience opérationnelle. Ils comprennent comment le logiciel est conçu et comment il fonctionne réellement en production. Cette perspective unique leur permet d'identifier les problèmes potentiels dès le début et de suggérer des améliorations au code, à l'architecture ou au processus de déploiement.

Et enfin, les SRE et les équipes de développement travaillent ensemble vers des objectifs communs, tels que l'amélioration de la fiabilité du système, l'augmentation de la fréquence des déploiements et la réduction du temps de récupération. Cet alignement garantit que tout le monde travaille vers les mêmes objectifs.

## Les principes fondamentaux du SRE :

### **Se concentrer sur la disponibilité et la fiabilité**

Les SRE visent à atteindre des objectifs spécifiques de niveau de service (SLO), qui sont des cibles mesurables pour le temps de fonctionnement et les performances.

**Scénario** : Un site de commerce électronique populaire, utilisé intensivement pendant les heures de bureau au Nigeria, fixe un SLO de 99,9 % de temps de fonctionnement pour son service de catalogue de produits. Cette norme élevée signifie que le service est censé être disponible presque tout le temps.

Pour comprendre à quel point cela permet peu de temps d'arrêt, décomposons-le :

1. **Pourcentage de temps d'arrêt** : Un temps de fonctionnement de 99,9 % signifie que le temps d'arrêt autorisé est de 100 % - 99,9 % = 0,1 %.
    
    * **Minutes dans une journée** : Il y a 24 heures dans une journée, et chaque heure a 60 minutes, donc il y a 24 x 60 = 1440 minutes dans une journée.
        
    * **Minutes dans un mois moyen** : En supposant un mois moyen de 30 jours, il y a environ 30 x 1440 = 43 200 minutes dans un mois.
        
    * **Temps d'arrêt autorisé en minutes** : Pour trouver 0,1 % des minutes dans un mois, nous calculons (0,1 / 100) x 43 200 minutes = 0,001 x 43 200 minutes = 43,2 minutes.
        

Par conséquent, un SLO de temps de fonctionnement de 99,9 % pour le service de catalogue de produits signifie qu'il peut être indisponible pendant un maximum d'environ 43 minutes par mois. L'équipe SRE surveille en permanence la disponibilité du service à l'aide d'outils qui suivent les taux de réussite des requêtes et la latence. Si la disponibilité chute en dessous de 99,95 % (un indicateur avancé), l'équipe SRE est alertée pour enquêter et remédier avant que le SLO ne soit violé.

**Exemple** : Une plateforme de banque en ligne au Nigeria a un SLO pour la latence du traitement des transactions : 99 % des transactions doivent être complétées en moins de 500 millisecondes. Les tableaux de bord SRE suivent cette métrique en temps réel. Si la latence commence à augmenter, indiquant un problème de performance potentiel, les SRE enquêtent pour déterminer si cela est dû à des goulots d'étranglement de la base de données, à la congestion du réseau au Nigeria, ou à des inefficacités du code de l'application.

### **Adopter l'automatisation**

L'automatisation est au cœur du SRE. Elle réduit le travail manuel, améliore la cohérence et accélère la résolution des problèmes.

**Scénario** : Lorsqu'un nouveau serveur est provisionné pour une application, un SRE a automatisé l'ensemble du processus à l'aide d'outils d'infrastructure-as-code (comme Terraform ou Ansible). Cela inclut la configuration du système d'exploitation, l'installation des logiciels nécessaires, la mise en place des agents de surveillance et le déploiement du code de l'application.

Auparavant, cela impliquait plusieurs étapes manuelles prenant des heures et sujettes à des erreurs humaines. Maintenant, cela est complété de manière cohérente en quelques minutes.

**Exemple** : Pendant les heures de pointe (par exemple, autour de l'heure du déjeuner au Nigeria lorsque de nombreuses personnes sont en ligne), la charge sur un cluster de serveurs web augmente. Un SRE a mis en place des règles d'auto-scaling qui ajoutent automatiquement plus de serveurs au cluster lorsque l'utilisation du CPU dépasse un certain seuil et les suppriment lorsque la charge diminue. Cette mise à l'échelle automatisée garantit que le service reste réactif sans intervention manuelle.

### **Mesurer tout**

Les SRE s'appuient sur des données et des métriques pour comprendre le comportement du système et identifier divers domaines d'amélioration.

**Scénario** : Pour une application de covoiturage populaire à Lagos, les SRE suivent un large éventail de métriques au-delà du simple temps de fonctionnement. Ces métriques sont souvent appelées indicateurs de niveau de service (SLI), qui sont des mesures quantitatives des performances d'un service.

Exemples :

1. **Latence des requêtes** : Le temps qu'il faut pour qu'un utilisateur demande un trajet et obtienne une confirmation.
    
2. **Taux d'erreurs** : Le pourcentage de demandes de trajet ou de transactions de paiement qui échouent.
    
3. **Utilisation des ressources** : Utilisation du CPU, de la mémoire et du disque des serveurs.
    
4. **Performance des requêtes de la base de données** : Le temps qu'il faut pour les opérations de la base de données.
    
5. **Métriques d'engagement des utilisateurs** : La fréquence d'utilisation des fonctionnalités clés.
    

Ces SLI sont cruciaux pour déterminer si le service atteint ses objectifs de niveau de service (SLO) - les valeurs ou plages cibles pour ces indicateurs (par exemple, 99 % des demandes de trajet doivent avoir une latence inférieure à 200 ms). Les métriques sont visualisées sur des tableaux de bord, permettant aux SRE de comprendre la santé du système et d'identifier les corrélations entre différents indicateurs, les aidant finalement à déterminer si les SLO sont atteints ou sont à risque.

**Exemple** : Après avoir déployé une nouvelle version de leur application mobile, les SRE surveillent de près les indicateurs de performance clés (KPI) comme le nombre d'utilisateurs actifs à Lagos, le temps moyen pour compléter une réservation, et la fréquence des plantages signalés par les utilisateurs au Nigeria. Ces données les aident à identifier rapidement si la nouvelle version a introduit des régressions de performance ou de stabilité.

### **Travailler avec les développeurs**

Les SRE collaborent étroitement avec les équipes de développement pour garantir que les applications sont conçues pour la fiabilité.

**Scénario** : Lorsque les développeurs conçoivent une nouvelle fonctionnalité pour leur base d'utilisateurs nigérians impliquant un traitement de données significatif, les SRE sont impliqués dès la phase de conception.

Ils fournissent des conseils sur la manière de construire la fonctionnalité de manière fiable et scalable, suggérant des modèles comme les disjoncteurs, les nouvelles tentatives et la gestion appropriée des erreurs.

Cette collaboration proactive aide à prévenir les problèmes de fiabilité d'être intégrés dans l'application. Les SRE peuvent également participer aux revues de conception, fournissant des informations opérationnelles et soulevant des préoccupations concernant les points de défaillance potentiels.

**Exemple** : Avant le lancement d'une grande campagne marketing au Nigeria, qui devrait augmenter considérablement le trafic, les SRE travaillent avec l'équipe de développement pour effectuer des tests de charge sur l'application. Cela aide à identifier les goulots d'étranglement potentiels et les domaines d'optimisation avant la véritable augmentation des utilisateurs.

Les SRE fournissent des informations sur la capacité du système et suggèrent des modifications de code ou des ajustements d'infrastructure pour gérer la charge anticipée. Les SRE peuvent analyser les résultats des tests de charge avec les développeurs, fournissant des informations sur la capacité du système et suggérant des modifications de code, des optimisations de base de données ou des ajustements d'infrastructure pour gérer la charge attendue. Ils peuvent également développer conjointement des règles de surveillance et d'alerte spécifiques au trafic attendu de la campagne.

### **Apprendre de l'échec**

L'échec est inévitable. Les SRE utilisent des revues post-incident pour analyser les échecs, identifier les causes profondes et mettre en œuvre des mesures préventives.

**Scénario** : Une panne critique s'est produite sur une passerelle de paiement utilisée par de nombreuses entreprises nigérianes. Après la restauration du service, l'équipe SRE mène une revue post-incident sans blame. Ils recueillent toutes les données pertinentes (journaux, métriques, chronologies, enregistrements de communication) et analysent collaborativement la séquence des événements, les causes sous-jacentes (qui peuvent impliquer une combinaison de bugs logiciels, d'erreurs de configuration et de surveillance insuffisante) et l'impact sur les utilisateurs.

Le résultat de la revue est un document détaillé décrivant les causes profondes et une liste d'éléments actionnables avec des responsables et des délais pour prévenir des incidents similaires à l'avenir (par exemple, améliorer la surveillance pour une métrique spécifique, mettre en œuvre une nouvelle stratégie de retour en arrière, corriger un problème de gestion de la configuration).

**Exemple** : Un incident mineur s'est produit où un point de terminaison API spécifique est devenu lent pendant une courte période pendant les heures de pointe à Lagos. Même si l'impact était minimal, l'équipe SRE mène toujours une revue post-incident légère.

Ils analysent les journaux et les métriques pour comprendre pourquoi le ralentissement s'est produit (peut-être une augmentation temporaire de la charge de la base de données) et identifient les mesures préventives potentielles, telles que l'optimisation de la requête de la base de données ou l'ajustement des limites de ressources.

L'élément actionnable pourrait être de créer un nouveau tableau de bord spécifiquement pour les performances de ce point de terminaison API, avec une date d'achèvement cible et attribué à un SRE spécifique (responsable). Par la suite, l'équipe suivra et s'assurera que le tableau de bord remplit son objectif.

Les SRE reconnaissent que les systèmes échoueront, et l'objectif n'est pas de prévenir toutes les défaillances, mais de minimiser leur impact. Les SRE peuvent y parvenir grâce à :

1. **Surveillance** : Les SRE mettent en œuvre un suivi en temps réel de la santé et des performances du système, ce qui leur permet de détecter les problèmes dès le début.
    
2. **Journalisation** : Ils utilisent des enregistrements détaillés des événements du système pour l'analyse, l'investigation, le débogage et la résolution des problèmes, ce qui est essentiel pour comprendre la cause profonde des défaillances.
    
3. **Alerte** : Les SRE configurent des notifications automatisées lorsque les métriques du système s'écartent des seuils attendus, leur permettant de répondre rapidement aux problèmes potentiels.
    
4. **Réponse aux incidents** : Ils établissent des procédures structurées et documentées pour répondre et résoudre les incidents, garantissant une approche coordonnée et efficace.
    
5. **Revues post-incident** : Les SRE mènent une analyse approfondie des incidents pour identifier les causes profondes et prévenir les récidives, traitant chaque incident comme une opportunité d'apprentissage. Cela est un aspect crucial de l'amélioration continue.
    

## Le rôle du SRE : Un équilibre délicat

Les SRE sont confrontés au défi d'équilibrer les besoins opérationnels quotidiens avec les initiatives d'ingénierie à plus long terme. Cet "équilibre délicat" est crucial pour maintenir la stabilité d'un système et sa capacité à évoluer et à s'améliorer.

Les SRE passent généralement leur temps dans deux domaines clés, chacun nécessitant un ensemble de compétences et une concentration différents :

### **Responsabilités opérationnelles (50%) :**

Les responsabilités opérationnelles d'un SRE sont assez vastes. Elles impliquent généralement de répondre aux incidents et aux pannes, ce qui est une partie centrale de tout rôle opérationnel. Les SRE sont souvent de garde, ce qui signifie qu'ils sont disponibles pour traiter les problèmes urgents en dehors des heures de travail régulières.

Ils gèrent également les escalades, ce qui signifie prendre en charge les problèmes complexes ou critiques que d'autres équipes ne peuvent pas résoudre.

Les SRE fournissent également un support aux clients internes et externes, ce qui peut impliquer le dépannage de problèmes, la réponse à des questions et la fourniture de conseils.

Ces responsabilités nécessitent de solides compétences en résolution de problèmes, une réflexion rapide et la capacité de rester calme sous pression.

### **Responsabilités d'ingénierie (50%) :**

Les responsabilités d'ingénierie sont ce qui distingue vraiment les SRE. Les SRE sont responsables de l'automatisation des tâches manuelles, ce qui est crucial pour augmenter l'efficacité et réduire les erreurs.

Ils développent également des systèmes de surveillance et d'alerte, ce qui implique de concevoir et de mettre en œuvre des outils pour suivre la santé du système et notifier les équipes des problèmes potentiels.

Les SRE contribuent à améliorer la fiabilité et les performances du système en identifiant et en traitant les goulots d'étranglement, en optimisant le code et en mettant en œuvre les meilleures pratiques.

Ils contribuent au développement de logiciels avec un accent sur les préoccupations opérationnelles, ce qui signifie qu'ils travaillent avec les développeurs pour s'assurer que les applications sont conçues pour la scalabilité, la maintenabilité et la résilience.

Ces responsabilités nécessitent de solides compétences en programmation, une compréhension approfondie de l'architecture du système et une approche proactive de la résolution de problèmes.

## Pourquoi l'automatisation est importante

L'automatisation est un outil important que les SRE utilisent pour atteindre leurs objectifs opérationnels et d'ingénierie. Il ne s'agit pas de remplacer les ingénieurs humains, mais de les habiliter à travailler plus efficacement.

Il existe plusieurs domaines clés où l'automatisation est vraiment importante :

1. **Réduire le "toil"** : Les SRE utilisent l'automatisation pour éliminer les tâches répétitives et manuelles, souvent appelées "toil". Cela libère leur temps pour se concentrer sur un travail plus stratégique, tel que l'amélioration de la conception du système et la mise en œuvre de nouvelles fonctionnalités.
    
2. **Améliorer l'efficacité** : L'automatisation peut considérablement accélérer les processus comme les déploiements, les retours en arrière et la réponse aux incidents, ce qui conduit à des temps de récupération plus rapides et à une réduction des temps d'arrêt.
    
3. **Améliorer la fiabilité** : En automatisant les processus critiques, les SRE peuvent réduire le risque d'erreur humaine, qui est une cause courante de pannes et d'autres problèmes.
    
4. **Acquérir une compréhension plus approfondie** : Chaque fois qu'un SRE automatise un processus, il acquiert une compréhension plus approfondie du système, conduisant à des améliorations ou à des améliorations supplémentaires. Ce processus itératif d'automatisation et d'apprentissage est central dans l'approche SRE.
    

## Points clés à retenir pour toute personne impliquée dans les services numériques :

1. **La fiabilité est une fonctionnalité** : Traitez la fiabilité comme une exigence majeure, et non comme une option.
    
2. **L'automatisation est essentielle** : Adoptez l'automatisation pour réduire le "toil" et améliorer l'efficacité.
    
3. **Prenez des décisions basées sur les données** : Utilisez des métriques pour comprendre le comportement du système et, en retour, guider les améliorations.
    
4. **La collaboration est la clé** : Favorisez une collaboration étroite entre les équipes de développement et d'exploitation.
    
5. **Concentrez-vous sur l'amélioration continue** : Adoptez une culture d'apprentissage et d'amélioration continus.
    

## Conclusion

Vous avez maintenant acquis une compréhension fondamentale de l'ingénierie de la fiabilité des sites et de ses principes fondamentaux centrés sur la disponibilité, l'automatisation, la mesure, la collaboration et l'apprentissage à partir des échecs. Vous avez également appris comment elle joue un rôle crucial dans le bon fonctionnement des services numériques sur lesquels nous comptons chaque jour.

Si vous avez trouvé ce tutoriel utile et souhaitez rester connecté pour plus d'informations sur l'ingénierie de la fiabilité des sites, vous pouvez me suivre sur [Twitter](https://x.com/OmoladeEkpeni), vous connecter sur [LinkedIn](https://www.linkedin.com/in/omolade-ekpeni-b7b431188/), ou me contacter par email à omolade.ekp@gmail.com.