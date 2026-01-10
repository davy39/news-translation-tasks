---
title: La merveille transformatrice de l'intégration et du déploiement continus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T19:34:15.000Z'
originalURL: https://freecodecamp.org/news/the-life-changing-wonder-of-continuous-integration-and-deployment-97f833505eea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4-J-DJc-kul-ASaFnbTDbg.jpeg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: Microsoft
  slug: microsoft
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: La merveille transformatrice de l'intégration et du déploiement continus
seo_desc: 'By Paul McGillivray

  In the first year or so of Remote, I used Dreamweaver to piece together sites page-by-page.
  When I was done, I’d FTP the results to my hosting provider via my 56k modem, and
  would let them do whatever it was that they needed to do...'
---

Par Paul McGillivray

Durant la première année ou plus de [Remote](https://remote.online), j'utilisais [Dreamweaver](http://www.adobe.com/uk/products/dreamweaver.html) pour assembler les sites page par page. Une fois terminé, je transférais les résultats via FTP à mon hébergeur via mon modem 56k, et les laissais faire ce qu'ils devaient faire pour que le site fonctionne sur le web.

Je n'avais pas besoin de savoir comment cela fonctionnait ; cela fonctionnait simplement. Les fichiers que je téléchargeais écrasaient directement les anciens fichiers. Et si je devais changer quelque chose, j'écrasais directement ces fichiers également. Et si je faisais une erreur et devais revenir en arrière, je devais espérer avoir pensé à sauvegarder sur ce disque dur externe assez récemment, sinon une longue nuit m'attendait !

Trois ou quatre ans plus tard, nous étions une équipe de trois personnes, co-localisant notre propre réseau de serveurs chez [Telehouse](https://www.telehouse.com/) dans les Docklands de Londres. Nos sites étaient pilotés par des bases de données utilisant SQL Server 2000, et le HTML était généré par ASP et VBscript. Lorsque nous mettions à jour un site, nous devions nous souvenir des fichiers que nous avions modifiés dans le cadre de la version, et télécharger ces fichiers.

Après un certain temps, nous avons appris à créer un nouveau dossier pour chaque mise à jour, afin de pouvoir l'utiliser comme site de préparation, jusqu'à ce que nous soyons prêts à passer en production — puis nous travaillions avec IIS et les liaisons de domaine et le DNS pour faire passer le site de préparation en production.

Cela fonctionnait, mais cela était sujet à toutes sortes d'erreurs. Nous pouvions oublier de changer un fichier de configuration pendant le processus de mise en production. Ou quelque chose qui fonctionnait auparavant pouvait soudainement cesser de fonctionner à cause d'un changement que nous avions fait ailleurs dans le projet, et nous n'avions pas pensé à tester cet aspect du site. Et si une correction très rapide était nécessaire, nous cédions souvent à la tentation et téléchargions simplement la correction directement sur le site en production, au lieu d'utiliser un nouveau dossier de préparation.

Nous installions, mettions à jour et gérions les serveurs nous-mêmes. Si un composant du serveur tombait en panne, c'était à nous de le réparer.

Je me souviens d'une fois où l'un de nos serveurs web est tombé en panne — j'ai appelé un ingénieur sur place, qui est devenu mes yeux, ouvrant la machine et me disant ce qu'il voyait. J'ai déduit que l'alimentation avait grillé, et j'ai procédé à une recherche en ligne des magasins de fournitures informatiques près du centre de données pour en trouver un qui avait cette alimentation presque obsolète (le serveur était notre premier, et il commençait à dater). Lorsque j'en ai trouvé un, j'ai payé un coursier à moto londonien pour récupérer l'alimentation et la conduire au centre de données où l'ingénieur attendait pour l'installer. Les sites étaient tous de nouveau en ligne après trois heures très tendues.

Huit ans plus tard, nous étions cinq dans l'équipe et les serveurs virtuels étaient devenus une proposition viable, et, compte tenu des avantages, nous nous sommes lancés. Si j'avais besoin d'un nouveau serveur, je n'avais plus besoin de le commander, d'installer le logiciel, de descendre à Londres et de le visser moi-même dans les racks (bien que je me sois toujours senti assez futuriste chaque fois que je travaillais dans le centre de données). Je n'avais qu'à appuyer sur quelques boutons de ma console [VMWare vCloud Director](https://www.vmware.com/uk/products/vcloud-director.html), et 20 minutes plus tard, le serveur était opérationnel et prêt à l'emploi.

Si j'avais besoin de plus d'espace disque, cela ne signifiait plus de temps d'arrêt pendant que je sortais la machine de ses racks et vissais le disque en place, configurant le RAID (terrifiant) et espérant que tout redémarre proprement. Au lieu de cela, maintenant, je n'avais qu'à cliquer sur quelques boutons de la console en ligne, faire un redémarrage rapide, et le disque était disponible pour moi.

Si une alimentation tombait en panne, l'instance du serveur se déplaçait simplement vers un autre des multiples serveurs lames disponibles, et revenait en ligne en quelques minutes. C'était encore un peu lourd à utiliser, et je devais toujours gérer les mises à jour logicielles et surveiller les ressources telles que le CPU, la RAM et l'espace disque, mais c'était une énorme amélioration.

Nos processus de déploiement n'ont pas beaucoup changé pendant cette transition. Nous sommes devenus plus vigilants concernant nos dossiers de préparation. Au lieu d'utiliser des dossiers appelés 'dev' et 'live' — qui devenaient immédiatement confus lorsque nous avions besoin d'une nouvelle version ('dev 2', ou 'new live', devenant plus tard 'live final', 'live final 2', etc.), nous avons utilisé une numérotation de version de publication pour les dossiers à la place — 'v1', 'v1.5', 'v2', etc. Le processus était plus robuste, ainsi que notre connaissance croissante de la manière d'éviter les pièges courants pour garder nos sites en ligne et sans erreur, mais l'erreur humaine était toujours possible, et faire de petites mises à jour était encore une opération assez majeure si nous devions le faire correctement sans les raccourcis sujets aux erreurs.

Alors que nous passions à des applications de niveau entreprise et à des applications mobiles, nos processus de déploiement sont devenus plus sophistiqués. Les applications en ligne nécessitaient plusieurs fichiers de configuration, et les applications mobiles avaient de nombreuses étapes de construction et de déploiement, avec des fichiers batch, des scripts serveur, et toutes sortes de configurations manuelles pour obtenir le produit final. Une grande partie des connaissances dont nous avions besoin pour ces processus était conservée dans la tête des développeurs qui en avaient besoin, et le problème avec cela est que si ces développeurs partaient, ces connaissances pouvaient partir avec eux.

Mais la technologie évolue à un rythme vertigineux, et chez Remote, nous aimons suivre ce rythme.

En 2017, maintenant une équipe Agile de développeurs, designers et chefs de projet, l'entreprise est méconnaissable par rapport à ses humble débuts et le Cloud est partout. Nous avons transféré la plupart de nos applications vers [Microsoft Azure](https://azure.microsoft.com) — la flexibilité de l'App Service est stupéfiante. Nous pouvons lancer un nouveau service, lui dire s'il s'agit de .NET, .NET Core, PHP, ou de n'importe quelle autre variante de code avec laquelle nous travaillons, et configurer les choses habituelles que nous configurerions dans IIS, mais sous une forme simple.

Nous pouvons ajouter l'application au plan de service, où toutes les applications partagent la mémoire allouée, le CPU, etc., rendant les ressources au pool lorsqu'elles ne sont pas nécessaires. Le Service se connecte à Azure SQL, qui se comporte de manière similaire, partageant les ressources avec son pool, et réduisant les ressources lorsqu'elles ne sont pas nécessaires. Un tableau de bord personnalisable fournit des graphiques de l'utilisation des ressources sur toutes les applications et services, et nous pouvons isoler un service et le déplacer dans son propre pool de ressources en quelques clics, sans temps d'arrêt.

Si une application se trouve sous une demande plus lourde que d'habitude, Azure peut 'Scaler', et créer une nouvelle instance copiée de l'application en temps réel, partageant le trafic des visiteurs entre les deux, trois, quatre, ou dix copies de l'application selon les besoins — lorsque la demande redescend, les instances copiées disparaissent également. Tout cela pendant que je dors.

Tout notre contrôle de version est géré avec Git. Plus besoin de fouiller dans les sauvegardes pour trouver une version précédente d'un fichier. Nous revenons simplement à la version du code source à un moment où le fichier était en place, et apportons les modifications nécessaires. Les nouvelles modifications sont fusionnées en douceur et facilement avec le tronc 'master', souvent suivant une 'pull request', où les pairs peuvent examiner et commenter de nouvelles sections de code avant qu'elles ne soient autorisées à rejoindre la source principale. Et lorsque ce code est validé dans le master, oh doux délice...

L'intégration et le déploiement continus sont pour moi le développement le plus excitant de ces dernières années. Je valide mon code dans le tronc master, et VSTS reconnaît que le code a été changé. Immédiatement, il exécute ma liste de tâches — il prend le code complet, télécharge les packages [NuGet](https://www.nuget.org/) pertinents, construit la solution, exécute nos tests unitaires pour s'assurer que tout fonctionne toujours comme il se doit, et une fois que tout est bien, il publie le projet entier dans un dossier de préparation et le préchauffe afin que lorsque nous visitons le site pour la première fois, nous n'ayons pas à attendre qu'il se charge. Une fois que nous avons soumis le site de préparation à une série de tests manuels QA pour être sûrs que nous en sommes satisfaits, un simple clic de souris échange les emplacements de préparation et de production, rendant nos nouvelles mises à jour en ligne sans aucun temps d'arrêt pour les visiteurs du site web. Et la version de production précédente est maintenant conservée en préparation, au cas où nous aurions besoin de revenir en arrière rapidement.

C'est brillant, c'est simple, cela élimine de nombreuses, nombreuses possibilités d'erreur humaine, et c'est tellement plus rapide. Et avec des constructions plus compliquées, ces scripts et fichiers batch peuvent être programmés dans le déploiement — plus de listes de contrôle et de choses à retenir, juste une validation Git, et le projet est déployé. Nous avons un contrôle finement détaillé sur la manière dont la construction se fait, et ce qui se passe pendant cette construction, et l'ordre des tâches peut être modifié comme nous le souhaitons. On a l'impression d'avoir atteint une sorte d'utopie technologique.

Bien sûr, la configuration n'est pas toujours complètement simple et prête à l'emploi. Une application en ligne qui utilise des ID de session, par exemple, devra être recodée pour utiliser quelque chose comme le Cache Azure Redis pour conserver ces états, afin qu'ils soient accessibles depuis plusieurs instances, et ne soient pas perdus lorsque l'App Service change de serveurs.

Dans Azure, tout est volatile et un site qui contient des fichiers utilisateur tels que des images ou des documents doit être reprogrammé pour conserver ces fichiers sur des lecteurs de stockage virtuel partagés, afin que lorsque le CD échange les emplacements de déploiement, les derniers fichiers ne soient pas échangés également. Mais, c'est facile à faire et les avantages sont immenses.

Rester dans l'écosystème Microsoft pour l'ensemble du cycle de développement présente également d'énormes avantages — Nous développons en utilisant [Visual Studio](https://www.visualstudio.com), et hébergeons nos dépôts Git sur [VSTS](https://www.visualstudio.com/team-services/), où nous avons également migré notre processus de gestion de projet, afin que nous puissions travailler sur un problème, relier les validations Git à celui-ci, et voir dans quelle version le problème a été résolu, le tout dans le même logiciel. Les pull requests permettent à d'autres développeurs de passer en revue et de commenter le code depuis Visual Studio, qui peut également gérer les pulls et les validations Git. Nous pouvons configurer CI/CD dans Azure et ensuite apporter des modifications plus granulaires à cette configuration dans VSTS, tout cela très rapidement et de manière transparente.

Je peux même recevoir un message [Slack](https://slack.com/) lorsqu'une construction est terminée, ou, plus important encore, lorsqu'elle échoue ; nous créons une nouvelle branche Git pour chaque problème sur lequel nous travaillons, puis validons cette branche dans le tronc, afin que nous obtenions un retour immédiat du système CI si quelque chose est cassé, et un retour immédiat du client, qui peut accéder au site de préparation — plus besoin d'attendre deux semaines pour une version officielle, où nous devions alors fusionner toutes nos branches de développement dans le master en une seule fois — un vrai cauchemar — au lieu de cela, un déploiement régulier, progressif et sûr. La capacité pour les clients à donner un retour aussi instantané signifie qu'ils peuvent voir sur quel élément d'un projet nous travaillons et donner un retour précoce, afin que nous puissions mettre en œuvre les ajustements nécessaires tôt dans le cycle de vie.

On a vraiment l'impression que nous sommes arrivés à un point où ce type d'automatisation fournit une couche juteuse d'immédiateté, d'interaction et d'intelligence qui a toujours été nécessaire pour gérer ces processus, et le résultat est une énorme amélioration en termes de fiabilité, de vitesse et de qualité. J'approfondirai les détails de toutes ces technologies dans de futurs articles, mais pour l'instant, voici le brave nouveau monde ; j'en suis un résident très heureux.

Publié à l'origine sur [remote.online](https://remote.online/journal/the-life-changing-wonder-of-continuous-integration-and-deployment).