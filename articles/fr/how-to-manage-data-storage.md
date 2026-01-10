---
title: Comment gérer le stockage des données
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-02-14T19:44:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-data-storage
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-tima-miroshnichenko-6549629.jpg
tags:
- name: data
  slug: data
- name: database
  slug: database
- name: storage
  slug: storage
seo_title: Comment gérer le stockage des données
seo_desc: "We've all been at this 21st Century thing for a while. And by now it's\
  \ pretty clear that data is the big driver of, well, of everything. \nGovernments\
  \ build their policies around economic and population data. Scientists build their\
  \ theories around env..."
---

Nous sommes tous dans cette ère du 21e siècle depuis un certain temps. Et à présent, il est assez clair que les données sont le principal moteur de, eh bien, de tout.

Les gouvernements construisent leurs politiques autour des données économiques et démographiques. Les scientifiques construisent leurs théories autour des données environnementales, physiques et biologiques. Les entreprises construisent leurs plans autour des données de production, de ventes et de comportement des consommateurs.

Cet article a été tiré du livre, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). Si vous préférez regarder ce chapitre sous forme de vidéo, n'hésitez pas à suivre ici :

%[https://youtu.be/JvoguWXO-lg]

Les données sont générées à des rythmes autrefois inimaginables. J'ai lu que les capteurs d'une paire de moteurs General Electric GEnx sur un Boeing 787 Dreamliner génèrent un téraoctet de données chaque jour.

Une seule voiture connectée au réseau (comme une Tesla) pourrait télécharger environ 100 Mo de données liées à la localisation, aux performances et à la maintenance lors d'une journée moyenne.

Multipliez cela par les millions de telles voitures qui seront bientôt en circulation dans le monde, et multipliez _ce_ nombre par les milliers d'autres appareils qui existent, et l'ampleur du "problème" des données devrait être claire.

Vous avez des projets pour ajouter vos propres données à ce flot et vous sentez le besoin de les sauvegarder et de les stocker également ? Vous devrez être capable d'expliquer pourquoi vous en avez besoin afin de savoir comment cela devrait être fait.

Je ne peux pas vous aider avec ce "pourquoi", mais je pense pouvoir vous donner quelques idées utiles sur le "comment".

La _manière_ dont vous stockez les données dépendra de leur apparence au moment de leur production et de la façon dont vous pourriez avoir besoin d'y accéder plus tard. _L'endroit_ où vous stockez vos données dépendra de la quantité de données, de l'impact que leur perte aurait sur vous, et de la fréquence à laquelle vous devrez les extraire et les utiliser. Examinons ces deux variables.

# Formats de stockage de données

Puisque toutes les données ne sont pas créées égales, il sera judicieux de rechercher les outils et environnements qui correspondent le plus étroitement au travail que vous prévoyez de faire. Voici quelques options :

## Tableurs

Ils peuvent être des applications grand public, colorées et attrayantes, mais les tableurs ne sont pas des poids légers en matière de traitement sérieux des données.

Comme nous le verrons plus en détail un peu plus tard, les tableurs ont leurs limites. Mais lorsqu'il s'agit de présenter des données de manière visuellement accessible, d'appliquer des opérations mathématiques, statistiques et financières à ces données, et même d'intégrer des sources de données distantes (comme les cotations boursières), aucun autre outil ne s'en approche.

Les tableurs peuvent importer des données textuelles simples et brutes à partir de fichiers de presque n'importe quelle taille, tant que le texte peut être délimité. C'est-à-dire que les séparations entre les divisions de données doivent être marquées par un caractère cohérent.

Lorsque vous importez les données, vous pouvez spécifier le délimiteur approprié. Les tabulations, les retours à la ligne et les virgules sont des caractères de délimitation courants. En fait, l'acronyme populaire _CSV_ signifie _comma-separated values_ (valeurs séparées par des virgules).

Voici à quoi pourraient ressembler quelques lignes de texte CSV. Notez que la première ligne contient les en-têtes de colonnes. Les tableurs peuvent facilement comprendre comment ceux-ci doivent être traités différemment.

```
Year,Volume,Rate,Growth
2015,56,10,15
2020,90,11,(2)
2022,109,8,12

```

Les tableurs affichent leurs données dans des cellules, qui sont disposées en lignes horizontales et en colonnes verticales. Vous pouvez appliquer des fonctions au contenu de cellules individuelles ou à certaines ou à toutes les cellules d'une colonne ou d'une ligne, et vous pouvez incorporer des valeurs dans des cellules à des emplacements relatifs.

Les ensembles de données dans un tableur peuvent être rendus sous forme de graphiques. Les tableurs peuvent également être utilisés comme des formulaires web où les utilisateurs peuvent saisir des données qui sont sauvegardées pour une utilisation future.

Le tableur le plus populaire est probablement Microsoft Excel, qui fait partie de leur suite Microsoft 365 Office. Mais fonctionnalité pour fonctionnalité, le Calc open source qui vient avec la suite LibreOffice est une alternative viable. Google Sheets est une solution de tableur basée sur le cloud qui peut manquer de certaines des fonctionnalités des autres, mais qui est un outil de collaboration puissant.

## Bases de données

En règle générale, les bases de données ne sont pas conçues pour visualiser les données dans des formats attrayants et intuitifs. Et, par elles-mêmes, elles ne sont pas connues pour les calculs mathématiques complexes non plus. Mais elles peuvent gérer des ensembles de données extra-larges et des relations multi-tables.

Lorsque je dis que les bases de données ne vous aident pas vraiment à visualiser vos données, c'est généralement parce qu'elles sont destinées à être utilisées "derrière" les applications frontales dans des déploiements multi-niveaux.

Par exemple, un site web de commerce électronique affichera des pages web où les utilisateurs peuvent parcourir ce que vous avez à vendre, ajouter des articles à un panier d'achat virtuel et passer à la caisse en utilisant leurs informations de paiement.

La page web elle-même ne fait que dessiner une interface graphique et vous montre où cliquer avec votre souris, mais les informations sur les articles que vous vendez - y compris leur prix et les images associées - sont probablement récupérées à partir d'une base de données backend chaque fois que la page se charge.

De même, vos sélections et, éventuellement, les informations de paiement seront écrites dans une base de données différente. Le processus logiciel qui gère votre expédition pourrait ensuite consulter la base de données de paiement pour l'adresse de livraison. Les bases de données sont présentes à chaque étape, mais personne ne les verra jamais réellement.

L'administration de grandes bases de données pour qu'elles soient efficaces, sécurisées et fiables nécessite une ingénierie sérieuse et, dans certains cas, une énorme quantité d'argent.

Avant de construire votre déploiement de base de données, vous devrez savoir si votre opération nécessite une forte atomicité, cohérence, isolation et durabilité (ACID) et un support pour des requêtes complexes et flexibles. Si c'est le cas, vous pourriez chercher un moteur de base de données relationnelle comme SQL Server, MariaDB ou Aurora d'Amazon.

Ou peut-être avez-vous besoin de performances rapides et préféreriez-vous un environnement plus flexible sans schéma (ce qui suggère que vous seriez mieux avec une solution NoSQL, comme MongoDB ou Redis).

_SQL_, d'ailleurs, signifie _structured query language_ - qui est une syntaxe établie pour utiliser un code similaire à un langage pour interagir avec vos données.

De manière contre-intuitive, selon à qui vous demandez, _NoSQL_ pourrait ne pas signifier _Not SQL_. Certains préfèrent le considérer comme _Not Only SQL_.

## Jupyter Notebook

Ne pensez pas que vous devez consommer vos données en utilisant le même outil qui les stocke. Il est possible, par exemple, d'importer des données existantes qui sont stockées localement ou sur un site distant dans un environnement de calcul interactif comme un Jupyter Notebook.

L'avantage de ce type de configuration est que les données peuvent maintenant être adressées dans le contexte d'un environnement de programmation Python robuste sans toucher - ou potentiellement corrompre - la source originale.

Le JupyterLab open source est une ressource populaire pour travailler avec de grands ensembles de données en utilisant Python. Vous pouvez télécharger et construire votre propre JupyterLab ou l'exécuter à distance via un fournisseur de cloud comme le service Elastic Map Reduce d'Amazon, ou les Azure Notebooks de Microsoft.

Pour des ensembles de données particulièrement grands - surtout ceux qui résident déjà dans le cloud - une plateforme cloud existante peut avoir du sens.

# Dispositifs de stockage de données

Bien que ce ne soit pas tout à fait aussi simple, disons qu'il existe quatre grandes catégories de supports de stockage de données :

* Bande magnétique sur bobines ouvertes, cartouches ou cassettes
* Optique incluant le Compact Disk (CD) et le Digital Video Disc (DVD)
* Supports magnétiques dans des boîtiers de 2,5 et 3,5 pouces - incluant les disques durs
* État solide incluant les disques SSD dans des boîtiers de 2,5 et 3,5 pouces, les cartes SD et les clés USB

Quelques systèmes de bandes magnétiques peuvent encore exister ici et là, mais les jours où l'on copiait laborieusement et lentement de grands ensembles de données sur des bancs de multiples bandes de sauvegarde - et où l'on espérait que la sauvegarde fonctionnerait réellement - sont pratiquement révolus. Croyez-moi : personne ne s'en plaint.

Les CD et DVD suivent la même direction. Leurs capacités maximales ne peuvent rivaliser avec le volume énorme des besoins en données des entreprises d'aujourd'hui, et les consommateurs ne font plus de copies locales de fichiers multimédias volumineux comme ils le faisaient autrefois.

Ce qui laisse les disques magnétiques et les disques à état solide.

Gigaoctet pour gigaoctet, les disques durs sont probablement encore un peu moins chers que leurs équivalents à état solide (bien que la différence de prix se réduise), mais les gains de performance offerts par les SSD sont très perceptibles.

Il y a quelque temps, j'ai réalisé que je pouvais réellement _économiser_ de l'argent en achetant des SSD de plus petite capacité pour mes stations de travail et ordinateurs portables personnels au lieu de disques durs (HDD) de plus grande capacité.

Permettez-moi d'expliquer. La manière dont nous utilisons les données sur nos ordinateurs personnels a changé ces dernières années. Plutôt que de stocker des médias et des archives de logiciels localement, nous sommes beaucoup plus susceptibles de supposer qu'ils seront disponibles en streaming ou en téléchargement chaque fois que nous en avons besoin.

Pour la plupart d'entre nous, des vitesses de téléchargement plus rapides ont rendu "vivre dans le cloud" facile. Nous n'avons donc généralement plus besoin d autant d'espace de stockage.

Le disque SSD de 500 Go branché sur ma station de travail occupée est à peine rempli à moitié - même en tenant compte de la douzaine de machines virtuelles et des nombreuses images ISO que j'ai là. Et le disque m'a coûté moins cher que ce que j'aurais payé pour un disque dur de un ou deux téraoctets.

L'un des rôles principaux du stockage est la sauvegarde des données. Plutôt que de transférer physiquement les sauvegardes entre les supports, l'archivage local des données - en utilisant des supports SSD ou HDD - fonctionne généralement en déplaçant les archives à travers les réseaux.

Le truc est de concevoir un système de sauvegarde qui vous fournit automatiquement des doublons suffisants de vos archives, les fait tourner à travers des cycles de vie appropriés (où, éventuellement, ils sont retirés et détruits), et tout cela sans générer de trafic réseau inutile.

Outre les sauvegardes, vous voudrez souvent partager des données entre les utilisateurs travaillant sur tout votre campus.

Deux outils pour gérer à la fois les sauvegardes et le partage de fichiers sont le stockage en réseau (NAS) et les réseaux de stockage (SAN). Leurs noms similaires suggèrent qu'ils sont dans le même domaine. Croyez-moi : ils ne le sont pas.

## Stockage en réseau (NAS)

Le NAS est un moyen relativement simple et peu coûteux de partager des fichiers sur un réseau local. Il fonctionne via un serveur autonome contenant plusieurs disques de stockage. Les disques seront normalement configurés en tant que réseau redondant de disques peu coûteux (RAID) pour fournir des avantages de redondance et de performance.

Le dispositif NAS se connecte au réseau via des câbles Ethernet et utilise le réseau TCP/IP standard. Les machines clientes du LAN verront les ressources NAS via des protocoles de partage de fichiers standard comme Server Message Block (SMB) et Network File System (NFS).

Les solutions NAS peuvent être idéales pour les petits environnements domestiques ou de bureau, mais le plaisir s'estompera rapidement à mesure que vous grandirez. Les dispositifs NAS eux-mêmes ne sont généralement pas assez puissants pour gérer une charge de travail client trop importante, et travailler avec de grands fichiers sur un réseau Ethernet peut ralentir les choses.

## Réseau de stockage (SAN)

Si les configurations NAS sont "relativement simples et peu coûteuses", les SAN sont complexes et coûteux. Ce n'est pas un hasard s'ils ont été conçus pour les déploiements d'entreprise à grande échelle. Grâce au matériel haut de gamme que vous mettez dans un système NAS, les performances seront excellentes et vous pourrez évoluer beaucoup plus loin.

Plutôt que l'Ethernet, les SAN fonctionnent via des commutateurs Fibre Channel beaucoup plus rapides (ou, parfois, l'iSCSI plus lent). Ils fournissent un stockage basé sur des blocs plutôt que des systèmes de fichiers et sont montés sur des machines clientes comme des disques locaux.

# Services de stockage de données

À mesure que les vitesses de connexion Internet se sont améliorées, il est devenu plus pratique de déplacer au moins certaines archives de données vers le cloud.

Au lieu de sauvegardes locales - qui pourraient être perdues lors d'un événement catastrophique comme un incendie - les données pourraient être régulièrement sauvegardées sur des plateformes en ligne. Une fois là-bas, vous auriez une sauvegarde viable et hors site. Mais, si vous le souhaitez, vous auriez également accès à ces données depuis n'importe où sur terre. Si vous travaillez à distance avec une équipe distribuée, cela peut être utile.

Vous possédez probablement déjà et avez même collaboré sur des documents qui se trouvent sur Dropbox, Microsoft 365 ou Google Drive. Pour la plupart des gens, le point d'interaction principal pour ces services est un navigateur web.

Mais la gestion sérieuse des données - ou même des sauvegardes de fichiers relativement complexes et régulières - ne sont pas pratiques dans un navigateur. Les fournisseurs de cloud computing offrent donc des services de stockage et d'archivage dont l'administration peut être scriptée et automatisée.

Les services de stockage cloud, comme le Simple Storage Service (S3) d'Amazon, fournissent une gestion complète du cycle de vie des archives. Les données qui doivent rester hautement disponibles pourraient, par exemple, être sauvegardées dans la classe de stockage S3 Standard.

Après quelques mois - lorsque vous êtes moins susceptible d'avoir besoin des données, mais devez toujours conserver une copie pour des raisons réglementaires - vous pourriez déplacer votre archive vers la classe S3 Glacier moins chère. Les données dans Glacier sont sécurisées et durables, mais prendraient beaucoup plus de temps à accéder.

Après une année complète, vous pourriez être en mesure de les supprimer définitivement. Mieux encore, il existe des moyens simples d'automatiser la manière dont vos données passent par leur cycle de vie.

Tous les principaux fournisseurs de cloud auront leurs propres services de stockage de données comparables. Naturellement, les prix et les caractéristiques exactes des services différeront les uns des autres. Et, bien sûr, les détails des caractéristiques et des prix changeront souvent.

Il n'est pas toujours pratique de transférer des données vers le cloud via Internet. Les ensembles de données extrêmement volumineux peuvent prendre beaucoup de temps à télécharger, même en utilisant des connexions Internet rapides.

Bien sûr, si vous avez la chance d'avoir une connexion par fibre optique vous offrant un gigaoctet par seconde, alors un téléchargement d'un téraoctet ne prendrait que deux heures et demie environ (en supposant que personne d'autre n'utilise la connexion).

Mais qu'en est-il de 100 To de données (cela vous prendra plus de dix jours) ? Et si vous n'avez que 100 Mo par seconde (plus de trois mois) ? Dans des cas comme ceux-ci, si vous téléchargez des archives de taille jumbo chaque semaine ou si vous avez d'autres utilisations pour votre connexion Internet, alors le téléchargement n'est pas une option.

Pour de tels cas, vous pouvez toujours mettre vos données dans le cloud, mais elles devront trouver un autre moyen de transport. AWS, comme il se trouve, offre leurs services Snow Family.

Snowball est un grand dispositif de stockage sécurisé. Il peut être expédié en toute sécurité aux clients d'AWS, chargé de dizaines de téraoctets de données, puis renvoyé. Une fois de retour chez Amazon, les données seront directement téléchargées dans un bucket dans le compte du client. Alternativement, les Snowballs peuvent être gardés sur place et utilisés comme dispositifs de calcul en périphérie.

Le grand frère de Snowball est AWS Snowmobile, un conteneur d'expédition sécurisé de 45 pieds de long capable de gérer des migrations numériques à l'échelle de l'exaoctet.

Le petit cousin de Snowball, AWS Snowcone, est un conteneur robuste de la taille d'une boîte à mouchoirs qui peut gérer huit To de stockage utilisable, ainsi que la possibilité d'instances cloud virtuelles et de connectivité réseau au cloud AWS. En plus de transférer vos données, les Snowcones peuvent être utilisés comme des dispositifs de calcul en périphérie hautement mobiles à part entière.

Et c'est tout pour aujourd'hui. Merci d'avoir lu. Maintenant, espérons que vous comprenez mieux comment nous stockons les données et quelles sont vos options de stockage de données.

_Les vidéos YouTube de tous les dix chapitres de ce livre [sont disponibles ici](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Beaucoup plus de bonnes choses technologiques - sous forme de livres, de cours et d'articles - [peuvent être trouvées ici](https://bootstrap-it.com). Et envisagez de suivre mes [cours sur AWS, la sécurité et la technologie des conteneurs ici](https://www.udemy.com/user/david-clinton-12/).