---
title: Qu'est-ce que DevSecOps ? Comment sécuriser un site web ou une application
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-12-14T14:08:56.000Z'
originalURL: https://freecodecamp.org/news/what-is-devsecops
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/maxresdefault.jpeg
tags:
- name: Application Security
  slug: application-security
- name: Devops
  slug: devops
- name: youtube
  slug: youtube
seo_title: Qu'est-ce que DevSecOps ? Comment sécuriser un site web ou une application
seo_desc: "Every day major companies have vulnerabilities exploited in their software.\
  \ It is important to learn how to protect your applications against data breaches.\
  \ \nIn this article you all about DevSecOps and web security.\nThere is a video\
  \ course that goes ..."
---

Chaque jour, de grandes entreprises voient des vulnérabilités exploitées dans leurs logiciels. Il est important d'apprendre à protéger vos applications contre les violations de données. 

Dans cet article, vous en apprendrez davantage sur DevSecOps et la sécurité web.

Il existe un cours vidéo qui accompagne cet article. L'article se concentre sur les définitions et la théorie. Le cours vidéo vous montrera également comment tirer parti des vulnérabilités web courantes, comment corriger ces vulnérabilités et comment utiliser les outils DevSecOps pour vous assurer que vos applications sont sécurisées. 

Vous pouvez regarder le cours vidéo ci-dessous ou sur la chaîne [YouTube de freeCodeCamp.org](https://youtu.be/F5KJVuii0Yw).

%[https://youtu.be/F5KJVuii0Yw]

Merci à [Snyk](https://snyk.io/) pour avoir fourni une subvention qui a rendu possible le développement de ce tutoriel et de ce cours vidéo.

## Qu'est-ce que DevSecOps ?

[DevSecOps](https://snyk.io/series/devsecops/) fait référence à l'intégration des pratiques de sécurité dans un modèle de livraison de logiciels DevOps. Dans un modèle DevSecOps, les objectifs de sécurité sont intégrés dès que possible dans le cycle de vie du développement logiciel et les considérations de sécurité sont importantes tout au long du cycle de vie.

Pour vraiment comprendre DevSecOps, il peut être utile de d'abord comprendre DevOps et également les vulnérabilités.

### Vulnérabilités

Commençons par les vulnérabilités. Le but de la sécurité est de protéger contre les vulnérabilités, alors comprenons les différents types et ensuite je discuterai de DevOps.

Le coût moyen d'une violation de données en 2020 était de 3,86 millions de dollars et les coûts mondiaux de la cybercriminalité devraient atteindre 6 billions de dollars d'ici la fin de cette année. On estime que 90 % des applications web sont vulnérables au piratage et que 68 % de celles-ci sont vulnérables à la violation de données sensibles.

En 2020, il y a eu plus de 1000 violations de données aux États-Unis selon le Centre de ressources sur le vol d'identité. Plus de 155,8 millions d'individus ont été affectés par des expositions de données. 

![Image](https://www.freecodecamp.org/news/content/images/2021/11/statistic_id273550_cyber-crime_-number-of-breaches-and-records-exposed-2005-2020.png)

### Vulnérabilité vs. Exploit vs. Menace

Lorsqu'on pense à la sécurité, il est important de comprendre la différence entre une vulnérabilité, un exploit et une menace.

Une **vulnérabilité de sécurité** est un défaut de code logiciel ou une mauvaise configuration du système que les pirates peuvent utiliser pour obtenir un accès non autorisé à un système ou à un réseau. Une fois à l'intérieur, l'attaquant peut exploiter les autorisations et les privilèges pour compromettre les systèmes et les actifs.

Un **exploit** est la méthode utilisée par les pirates pour exploiter une vulnérabilité. Un exploit est généralement un logiciel personnalisé ou une séquence de commandes. 

Il existe même des kits d'exploits qui peuvent être intégrés dans des pages web compromises où ils scannent en continu les vulnérabilités. Dès qu'une faiblesse est détectée, le kit tente immédiatement de déployer un exploit, comme injecter un logiciel malveillant dans le système hôte.

Une **menace** est l'événement réel ou hypothétique dans lequel un ou plusieurs exploits utilisent une vulnérabilité pour monter une attaque. 

![vulnérabilités et exploits de sécurité](https://res.cloudinary.com/snyk/images/w_550,h_438,c_scale/v1/wordpress-sync/Vuln-diagram-2-1-e1574424713592/Vuln-diagram-2-1-e1574424713592.png)

Seule une petite partie des vulnérabilités connues sera utilisée pour pirater un système. Les vulnérabilités qui présentent le plus grand risque sont celles qui ont une probabilité plus élevée d'être exploitées et doivent donc être celles qui sont prioritaires.

## Types de vulnérabilités de sécurité

Les vulnérabilités de sécurité peuvent être trouvées dans tous les différents domaines liés aux logiciels. Voici quelques vulnérabilités de sécurité courantes dans les applications et les sites web.

Il existe deux listes importantes différentes de faiblesses dans les applications web. La première liste est créée par le projet Open Web Application Security Project (OWASP). Ils ont une liste populaire appelée [OWASP Top 10](https://owasp.org/www-project-top-ten/) qui présente les vulnérabilités les plus couramment exploitées.

La deuxième liste est [CWE](https://cwe.mitre.org/), ou Common Weakness Enumeration, qui est une « liste développée par la communauté des types de faiblesses logicielles et matérielles courantes qui ont des répercussions sur la sécurité ». Cette liste est gérée par la société MITRE, une société à but non lucratif qui exploite des centres de R&D financés par le gouvernement fédéral. Ils créent le CWE-25 qui est leur liste des 25 faiblesses logicielles les plus dangereuses.

Dans le CWE-25, il existe 3 principaux types de faiblesses de sécurité des applications et des sites web :

1. Défenses poreuses
2. Gestion risquée des ressources
3. Interaction non sécurisée entre les composants

## 1. Défenses poreuses

Une faiblesse des défenses poreuses est celle qui pourrait permettre aux utilisateurs de contourner ou de falsifier les processus d'authentification et d'autorisation. L'authentification vérifie l'identité de quelqu'un qui tente d'accéder à un système tandis que l'autorisation est l'ensemble des permissions d'accès et d'utilisation attribuées à l'utilisateur.

Les exemples de faiblesses des défenses poreuses incluent :

* Codage faible des mots de passe
* Identifiants insuffisamment protégés
* Authentification manquante ou à facteur unique
* Permissions héritées de manière non sécurisée
* Sessions qui n'expirent pas en temps opportun

Tous ces types de vulnérabilités de défense poreuse peuvent permettre aux pirates d'accéder avec succès à des ressources sensibles.

Les exploits qui tirent parti de ces vulnérabilités peuvent inclure :

* Attaques par bourrage d'identifiants
* Détournement d'ID de session
* Vol d'identifiants de connexion
* Attaques de l'homme du milieu

## 2. Gestion risquée des ressources

Une autre catégorie de vulnérabilités est la gestion risquée des ressources telles que la mémoire, les fonctions et les frameworks open source. 

Ces vulnérabilités incluent :

* **Écriture ou lecture hors limites (aka débordement de tampon) :** L'application peut être trompée pour écrire ou lire des données au-delà de la fin ou avant le début du tampon mémoire prévu.
* **Traversée de chemin :** Permet aux attaquants d'accéder à des noms de chemin qui leur permettent d'accéder à des fichiers en dehors des répertoires restreints. Je montrerai un exemple de cela plus tard.

L'exploitation de ces vulnérabilités permet aux pirates de prendre le contrôle d'une application, d'endommager des fichiers ou d'accéder à des informations sensibles.

## 3. Interaction non sécurisée entre les composants

De nombreuses applications aujourd'hui envoient et reçoivent des données à travers une large gamme de services, de threads et de processus. La manière dont différents composants interagissent entre eux peut introduire des vulnérabilités.

Les faiblesses qui exposent une application web ou un site web de cette manière incluent :

* **Cross-site scripting ou XSS :** Lorsque les entrées utilisateur ne sont pas gérées de manière sécurisée, cela ouvre la possibilité à des attaques XSS qui permettent aux attaquants d'injecter des scripts côté client dans des pages web consultées par d'autres utilisateurs. Il s'agit d'une vulnérabilité très courante.
* **Cross-site request forgery (CSRF) :** Vérification incorrecte de la légitimité et de l'authenticité d'une requête apparemment légitime et authentique. Ces attaques sont souvent montées via des vecteurs d'ingénierie sociale tels que des e-mails frauduleux qui trompent un utilisateur pour qu'il clique sur un lien, qui envoie ensuite une requête falsifiée à un site ou à un serveur où l'utilisateur a déjà été authentifié.

Si les applications et les sites web ne mettent pas correctement en œuvre les contrôles de sécurité pour l'interaction entre les composants, cela les rend vulnérables aux attaques par porte dérobée, aux attaques par script, aux vers, aux chevaux de Troie et à d'autres exploits qui déploient du code malveillant pour semer le chaos dans l'infrastructure, les données et les systèmes.

### Vulnérabilités les plus courantes

Entre les listes OWASP-10 et CWE-25, il est clair que le contrôle d'accès rompu est la principale vulnérabilité. 94 % des applications ont une forme de contrôle d'accès rompu.

Le contrôle d'accès garantit que les utilisateurs ne peuvent pas agir en dehors de leurs permissions prévues. Si cela n'est pas configuré correctement, cela peut conduire à une divulgation, une modification ou même une destruction non autorisée de données.

### DevOps

Maintenant, parlons de DevOps, qui est une partie importante de DevSecOps.

DevOps est un concept dont on parle et écrit depuis longtemps, et de nombreuses définitions de DevOps ont émergé. 

DevOps est essentiellement un ensemble de pratiques qui combine le développement logiciel (Dev) et les opérations informatiques (Ops). Il vise à raccourcir le cycle de vie du développement des systèmes et à fournir une livraison continue avec une qualité logicielle élevée.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-59.png)
_Pipeline DevOps_

La plupart des organisations DevOps modernes dépendront d'une combinaison de systèmes d'intégration continue et de déploiement/délivrance continue, sous la forme d'un [pipeline CI/CD](https://snyk.io/learn/what-is-ci-cd-pipeline-and-tools-explained/). Dans le cadre du cycle de vie, une variété de tests de sécurité automatisés et de validation peuvent être effectués, sans nécessiter le travail manuel d'un opérateur humain. Et tout cela fait partie du cycle de vie du développement logiciel.

Voici un exemple de flux DevOps courant. Tout d'abord, un développeur écrit du code et le pousse vers un dépôt. À ce moment-là, le pipeline CI/CD commence. Il y a des tests automatisés, puis une version est construite et finalement déployée en production. Il y a des tests à chaque étape pour assurer la qualité du code. Dans ce modèle, la sécurité n'est parfois considérée qu'au moment de déployer en production.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-57.png)

DevSecOps suit un flux similaire, mais ajoute des considérations de sécurité automatisées tout au long du processus. La sécurité est intégrée avec DevOps. DevSecOps codifie les objectifs de sécurité dans la structure globale des objectifs.

Le bouclier représente tous les endroits où nous testons la sécurité. Différents outils sont utilisés pour différentes étapes et je parlerai de certains des outils spécifiques plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-58.png)

DevSecOps doit être considéré comme la continuation naturelle de DevOps, plutôt que comme une idée ou un concept séparé. 

Les activités conçues pour identifier et idéalement résoudre les problèmes de sécurité sont injectées tôt dans le cycle de vie du développement d'applications, plutôt qu'après la sortie d'un produit. Cela est accompli en permettant aux équipes de développement d'effectuer de nombreuses tâches de sécurité de manière indépendante dans le cycle de vie du développement logiciel (SDLC).

Pour intégrer les objectifs de sécurité dès le développement d'une application, commencez avant que la première ligne de code ne soit écrite. La sécurité peut s'intégrer et commencer une modélisation efficace des menaces lors de la conception initiale du système, de l'application ou de l'histoire utilisateur individuelle. L'analyse statique, les linters et les moteurs de politique peuvent être exécutés chaque fois qu'un développeur vérifie le code, garantissant que les problèmes évidents sont traités avant que les modifications ne progressent davantage. Plus tard, je vous montrerai comment utiliser un outil pour vérifier le code à la recherche de problèmes de sécurité pendant que vous l'écrivez.

L'analyse de la composition logicielle peut être appliquée pour confirmer que les dépendances open source ont des licences compatibles et sont exemptes de vulnérabilités. Je vous montrerai comment utiliser un outil pour vérifier les dépendances logicielles à la recherche de problèmes de sécurité. Il peut être très utile d'obtenir un retour immédiat sur la sécurité relative du code que vous avez écrit, ce qui aide les développeurs individuels à prendre en charge les problèmes de sécurité.

Une fois le code vérifié, des outils de test de sécurité statique des applications (ou [SAST](https://snyk.io/learn/application-security/static-application-security-testing)) peuvent être utilisés pour identifier les vulnérabilités et effectuer une analyse de la composition logicielle. Les outils SAST doivent être intégrés dans les processus post-commit pour garantir que le nouveau code introduit est proactivement scanné pour les vulnérabilités. Avoir une intégration d'outil SAST en place permet de corriger les vulnérabilités plus tôt dans le cycle de vie du développement logiciel, et cela réduit les risques et l'exposition des applications.

Après la construction du code, vous pouvez commencer à employer des tests d'intégration de sécurité. L'exécution du code dans un bac à sable de conteneur isolé permet des tests automatisés de choses comme les appels réseau, la validation des entrées et l'autorisation. Ces tests font souvent partie des outils de numérisation dynamique des applications (ou DAST). Ces tests génèrent un retour rapide, permettant une itération rapide et un triage de tout problème identifié, causant une perturbation minimale du flux global. Si des choses comme des appels réseau inexpliqués ou des entrées non assainies se produisent, les tests échouent, et le pipeline génère un retour exploitable sous forme de rapports et de notifications aux équipes concernées.

Ensuite, des choses comme la journalisation correcte et les contrôles d'accès peuvent être testées. L'application journalise-t-elle correctement les métriques de sécurité et de performance pertinentes ? L'accès est-il limité au sous-ensemble correct d'individus (ou empêché entièrement) ? 

Enfin, l'application arrive en production. Mais les tests de sécurité continuent. La gestion automatisée des correctifs et de la configuration garantit que l'environnement de production exécute toujours les dernières versions et les plus sécurisées des dépendances logicielles. 

Des techniques et outils spéciaux peuvent être utilisés pour sécuriser les conteneurs. Plus tard, vous apprendrez comment faire cela dans un environnement réel.

L'utilisation d'un pipeline CI/CD DevSecOps aide à intégrer les objectifs de sécurité à chaque phase, permettant de maintenir la livraison rapide. 

L'ensemble de l'approche aide à minimiser les vulnérabilités qui atteignent la production, réduisant ainsi les coûts associés à la correction des failles de sécurité. DevSecOps vise à intégrer la sécurité à chaque étape du processus de livraison, dès la phase de exigences, et à établir un plan pour l'automatisation de la sécurité.

## Iceberg du projet logiciel

Lorsqu'on pense à la sécurité, il faut se rappeler que votre code n'est que la partie émergée de l'iceberg.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-70.png)

Dans un projet logiciel moyen, seulement 10-20 % du code est du code personnalisé. Oui, il est important de s'assurer que votre code personnalisé est sécurisé, mais il y a beaucoup plus à considérer.

80-90 % de nombreuses bases de code sont constituées de code open source, de modules et de bibliothèques. Les frameworks et bibliothèques que vous importez peuvent eux-mêmes importer d'autres frameworks et bibliothèques. Il s'agit de code que vous n'avez pas réellement écrit vous-même. 

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-71.png)
_Le répertoire node_modules d'un projet est souvent massif._

En moyenne, 80 % des vulnérabilités sont trouvées dans les dépendances directes. Peu importe à quel point vous êtes bon pour écrire du code sécurisé si vous importez des dépendances vulnérables.

Ensuite, il y a les conteneurs. Ceux-ci sont souvent constitués de centaines de paquets Linux hérités de sources publiques. Encore une fois, du code que vous n'avez pas réellement écrit vous-même. 

Et n'oubliez pas l'infrastructure en tant que code. Cela ouvre un tas de nouveaux vecteurs d'attaque pour les acteurs malveillants. La mauvaise configuration est la principale vulnérabilité du cloud.

DevSecOps, correctement mis en œuvre, devrait couvrir tous ces domaines.

## L'importance de DevSecOps

### Pourquoi les pratiques DevSecOps sont-elles importantes ?

À mesure que les entreprises grandissent, il y a souvent plus de logiciels, de technologies cloud et de méthodologies DevOps.

Plus de logiciels signifie que plus de risques de l'organisation deviennent numériques, rendant de plus en plus difficile la sécurisation des actifs numériques.

Les technologies cloud signifient que de nombreux risques informatiques et d'infrastructure sont déplacés vers le cloud. Cela augmente l'importance de la gestion des permissions et des accès puisque tout peut être accessible de n'importe où.

Comme vous l'avez vu, DevSecOps intègre la sécurité dans DevOps, permettant aux équipes de développement de sécuriser ce qu'elles construisent à leur rythme, tout en créant une plus grande collaboration entre les développeurs et les praticiens de la sécurité. Les équipes de sécurité offrent une expertise et des outils pour augmenter l'autonomie des développeurs tout en fournissant un niveau de supervision.

### 6 avantages du modèle DevSecOps (par rapport au modèle DevOps traditionnel)

![6 avantages du modèle DevSecOps](https://snyk.io/wp-content/uploads/devsecops-benefits-1-1240x627.png)

1. **Livraison plus rapide :** La vitesse de livraison des logiciels est améliorée lorsque la sécurité est intégrée dans le pipeline. Les bugs sont identifiés et corrigés avant le déploiement, permettant aux développeurs de se concentrer sur la livraison des fonctionnalités.
2. **Posture de sécurité améliorée :** La sécurité est une fonctionnalité dès la phase de conception. Un modèle de responsabilité partagée garantit que la sécurité est étroitement intégrée, de la construction au déploiement, en sécurisant les charges de travail de production.
3. **Coûts réduits :** L'identification des vulnérabilités et des bugs avant le déploiement entraîne une réduction exponentielle des risques et des coûts opérationnels.
4. **Amélioration de la valeur de DevOps :** L'amélioration de la posture de sécurité globale en tant que culture de responsabilité partagée est créée par l'intégration des pratiques de sécurité dans DevOps. 
5. **Amélioration de l'intégration de la sécurité et du rythme :** Le coût et le temps de livraison des logiciels sécurisés sont réduits en éliminant le besoin de rétrofiter les contrôles de sécurité après le développement.
6. **Permettre un plus grand succès global des affaires :** Une plus grande confiance dans la sécurité des logiciels développés et l'adoption de nouvelles technologies permettent une croissance accrue des revenus et une expansion des offres commerciales.

## Conclusion

Il existe une série d'outils qui peuvent aider à sécuriser vos applications et beaucoup d'entre eux sont gratuits. Apprenez-en plus sur la façon de les utiliser dans la vidéo qui accompagne cet article.

%[https://youtu.be/F5KJVuii0Yw]