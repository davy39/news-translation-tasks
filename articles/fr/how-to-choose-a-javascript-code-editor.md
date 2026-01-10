---
title: Comment choisir le meilleur éditeur JavaScript pour le développement web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-03T20:31:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-a-javascript-code-editor
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/cover-4.jpg
tags:
- name: Developer Tools
  slug: developer-tools
- name: editor
  slug: editor
- name: JavaScript
  slug: javascript
seo_title: Comment choisir le meilleur éditeur JavaScript pour le développement web
seo_desc: 'By Arthur Puszynski

  There are a number of options for developers who are looking for a good JavaScript
  editor that provides a more efficient and pleasant working environment.

  Leading JavaScript code editors share many of the same great major features...'
---

Par Arthur Puszynski

Il existe de nombreuses options pour les développeurs qui recherchent un bon éditeur JavaScript offrant un environnement de travail plus efficace et agréable.

Les principaux éditeurs de code JavaScript partagent de nombreuses fonctionnalités majeures que vous pourriez attendre, notamment l'autocomplétion, l'intégration Git et la prise en charge des plugins. Mais ce sont les petits détails qui peuvent rendre un éditeur plus adapté qu'un autre pour un développeur donné.

Une fois que vous êtes à l'aise avec un éditeur de code et familiarisé avec le flux de travail qui vous rend plus efficace, il peut être difficile de changer d'éditeur, car vous devrez réapprendre les raccourcis pour optimiser vos processus de développement.

Même si vous devenez plus efficace à long terme, il y a toujours une barrière importante à l'entrée lors du changement, il est donc judicieux d'investir un peu de temps au départ pour choisir le meilleur éditeur pour vos besoins.

Passons en revue certaines des options d'éditeurs les plus populaires.

## [Visual Studio Code](https://code.visualstudio.com/)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-38.png)

VSCode de Microsoft est gratuit, open-source et assez léger à l'installation. C'est l'éditeur de facto pour les développeurs JavaScript débutants, en partie parce qu'il est préchargé avec un bon ensemble de fonctionnalités qui ne nécessitent pas de plugins supplémentaires. VSCode est également populaire et peut être idéal pour les utilisateurs plus avancés qui doivent commencer rapidement.

Une fonctionnalité unique de VSCode est qu'il peut être utilisé via le navigateur. Ainsi, le même environnement que vous obtenez sur le bureau est possible en déplacement en utilisant votre tablette. Un [code-server](https://github.com/cdr/code-server) doit être configuré sur un réseau auquel vous pouvez accéder pour que cette fonctionnalité fonctionne, mais c'est très pratique une fois configuré.

**Astuce** : En travaillant sur un grand projet dans un autre IDE où le processus de construction peut prendre un certain temps, j'ouvre souvent le gros fichier JS de sortie dans VSCode et je le modifie pour tester instantanément un changement dans le navigateur avant de l'appliquer. VSCode gère ces gros fichiers sans problème.

Git est intégré à l'IDE, mais l'intégration n'est pas aussi robuste que dans certains autres éditeurs. Par exemple, les utilisateurs de WebStorm préfèrent l'expérience de push/merge à celle de VSCode.

Vous pouvez installer de nombreuses fonctionnalités supplémentaires dont vous pourriez avoir besoin sous forme d'extensions, dont il existe des milliers. Mais toutes ne sont pas des fonctionnalités réelles. Les extraits de code sont mélangés avec les fonctionnalités et les modules complémentaires, ce qui peut prendre du temps à examiner et à trouver les meilleures options à ajouter. Si vous rencontrez un problème, VSCode dispose d'une immense communauté d'utilisateurs ; quelqu'un a probablement eu le même problème et l'a résolu.

Si vous n'êtes pas prêt pour un IDE payant complet avec toutes les fonctionnalités, et que vous n'êtes pas suffisamment familiarisé avec tous les plugins et fonctionnalités dont vous pourriez avoir besoin, c'est le point de départ logique.

## [Atom](https://atom.io/)

![Image](https://www.freecodecamp.org/news/content/images/2019/11/image-36.png)

L'éditeur gratuit Atom a été développé par GitHub. Il s'agit en fait d'une version spécialisée du navigateur chromium convertie en éditeur de texte et de code source. En interne, il utilise Node.js pour la prise en charge des plugins.

Une pléthore de plugins sont disponibles pour toutes les fonctionnalités que vous pourriez souhaiter, cependant, il n'est pas aussi performant dès la sortie de la boîte. Vous devez rassembler un certain nombre de plugins pour construire l'environnement de développement afin d'être aussi efficace que possible. Si vous travaillez avec JavaScript, voici quelques plugins essentiels pour Atom pour commencer :

* atom-typescript
* file-icons - pour colorier et attribuer des icônes à différents types de fichiers
* atom-beautify
* linter

**Astuce** : Activez le package autosave qui sauvegardera les modifications lorsque le focus est perdu. Il est désactivé par défaut.

Plusieurs utilisateurs peuvent travailler sur le même fichier en même temps, chacun avec plusieurs curseurs à l'écran, via le plugin teletype. Vous pouvez utiliser cela pour du mentorat, du codage en binôme ou de la collaboration. Cette fonctionnalité distingue Atom des autres éditeurs.

L'intégration Git est bien implémentée, comme vous pourriez vous y attendre de la part d'un logiciel GitHub. Également utile est un plugin git-plus qui vous permet d'exécuter des commandes git via des raccourcis clavier sans utiliser le terminal git.

Atom est personnalisable au point où vous pouvez éditer un fichier .less pour ajuster les couleurs de l'IDE, ce qui est bien si vous aimez ajuster chaque détail de votre environnement. Vous pouvez exécuter un script .coffe au démarrage qui peut être utilisé pour changer rapidement le comportement de l'éditeur.

Vous pouvez écrire des plugins en JavaScript contre une API d'éditeur bien documentée. La possibilité de créer vos propres fonctionnalités et comportements est agréable à avoir, si le besoin se présente.

L'expérience d'édition est fluide et vous pouvez l'améliorer avec d'autres plugins comme minimap, mais il y a un certain temps d'investissement initial nécessaire pour le configurer avec toutes les fonctionnalités que vous souhaitez. L'avantage est que les fonctionnalités dont vous n'avez pas besoin ne prendront pas de temps de chargement, ce qui ralentit l'expérience. Cependant, vous pouvez rencontrer une certaine lenteur momentanée lors du chargement de gros fichiers ou du changement d'onglets.

J'ai initialement aimé l'idée d'éditer les styles CSS pour personnaliser l'environnement de l'IDE, ou au moins avoir la possibilité si je voulais un jour créer mes propres thèmes. Cela semble amusant, mais en pratique, créer des thèmes qui incluent de nombreuses variables ne sont pas des projets triviaux. Heureusement, il existe de nombreux plugins de thèmes polis disponibles en téléchargement.

Atom est un éditeur solide et il sera un choix parfait pour de nombreux développeurs.

## [Sublime Text](https://www.sublimetext.com/)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-34.png)

Sublime Text est un éditeur payant, mais une version d'essai gratuite est disponible. Il n'est pas préchargé avec de nombreux plugins au départ, mais bien sûr, ils sont disponibles pour répondre à tous les besoins que vous pourriez avoir. Certains packages comme SideBarEnhancements pour renommer, déplacer, copier et coller devraient probablement être intégrés au bundle de base, mais vous pouvez les télécharger pour activer cette fonctionnalité.

Similaire à Atom, il peut prendre un peu de temps pour tout configurer. Mais une fois en marche, l'expérience est très fluide. La sauvegarde lors de la perte de focus est également disponible.

Sublime Text est agréable car il est léger, ce qui le rend très rapide à charger et à travailler avec de grands projets ou fichiers. La fonctionnalité "goto anything" se distingue car elle peut être utilisée avec des noms de fichiers, des symboles et des numéros de ligne. La plupart des IDE fournissent des fonctionnalités similaires sous une forme ou une autre, mais pouvoir les combiner et rechercher avec des requêtes comme "fileName@functionName" est assez agréable.

Sélectionner une variable sélectionne toutes les occurrences de cette variable et la renommer renomme toutes les occurrences automatiquement, donc cette tâche courante devient une expérience très rationalisée.

À bien des égards, Sublime Text est très similaire à Atom. Mais Sublime Text a l'avantage avec de meilleures performances générales et une réactivité, qui est superbe.

## [VIM](https://www.vim.org/)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-39.png)

Vim est également un éditeur de texte gratuit et très configurable. À l'origine nommé vi et premier éditeur de texte développé pour Unix, il a ensuite été étendu en un éditeur plus riche en fonctionnalités nommé Vim. Il est disponible sur la plupart des distributions Linux.

Vim dispose de capacités de recherche robustes et de mise en évidence de la syntaxe, et il est super léger, donc il peut performant même avec des fichiers très volumineux. Mais il nécessite un certain travail pour le configurer et le préparer à l'utilisation.

Une interface graphique est disponible, mais ce n'est pas l'interface par défaut pour Vim. Même l'activation de la prise en charge de la souris nécessite une certaine action pour la faire fonctionner. Par défaut, il s'agit d'un mode clavier que certains peuvent préférer pour accéder à chaque contrôle et fonctionnalité via des raccourcis.

Cela dit, Vim peut être votre IDE parfait si vous passez un peu de temps à apprendre les tenants et aboutissants du logiciel et à configurer tous les comportements et fonctionnalités que vous souhaitez. Si vous êtes à court de temps et ne pouvez pas faire l'investissement initial pour régler les choses, Vim peut ne pas être le meilleur choix pour vous.

## [WebStorm](https://www.jetbrains.com/webstorm/)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-40.png)

WebStorm a été développé par JetBrains et se distingue des autres en tant que véritable IDE JavaScript, car il dispose de toutes les fonctionnalités intégrées dès la sortie de la boîte. L'environnement de développement pour différentes plateformes comme React, Angular, Vue.js, etc. est transparent. Vous pouvez déboguer des scripts node, et exécuter des tests sur un serveur intégré. Vous pouvez également exécuter et déboguer des scripts npm via une interface en arborescence. Et il ne nécessite aucun plugin pour cela.

Cependant, des plugins sont disponibles pour certaines fonctionnalités rares qui ne sont pas intégrées directement dans le logiciel. Un plugin qui n'était pas inclus par défaut était une fenêtre de division édition/aperçu markdown. Mais pour la plupart, tout ce dont vous pourriez avoir besoin est déjà là. Le bon côté de cela est que vous découvrirez des fonctionnalités dont vous ne saviez pas qu'elles existaient et à quel point il est agréable de les avoir.

Les fichiers se sauvegardent automatiquement au fur et à mesure que vous travaillez dessus par défaut. Lorsque vous utilisez une autre application qui ne fait pas cela, la sauvegarde manuelle semble très primitive en comparaison. Bien que ce ne soit pas unique à WebStorm, l'implémentation est un peu plus agréable.

Certaines personnes peuvent ne pas toujours faire confiance à l'intégrité de la pile d'états d'annulation ctrl-z, mais dans WebStorm, il y a un système VSC intégré qui fait essentiellement un commit chaque fois qu'un fichier est sauvegardé. Cela est interne et est séparé de vos commits git. Les fichiers se sauvegardent au moins chaque fois que la fenêtre de contenu du fichier perd le focus. Donc, si vous travaillez un certain temps sans commiter dans git et que vous devez revenir en arrière ou voir un état précédent après votre dernier commit, ce n'est pas un problème.

**Astuce** : Ctrl-shift-flèche haut/bas vous permet de déplacer des lignes ou des blocs de code vers le haut ou vers le bas tandis que l'éditeur gère automatiquement les virgules/accolades de bloc.

Lorsque vous travaillez sur des projets qui ont de nombreux fichiers, faire défiler l'arborescence des fichiers à la recherche d'un fichier spécifique peut vous ralentir. Mais si l'un de ces éléments est déjà ouvert et en focus, cliquer sur l'icône de cible fait défiler la vue de l'arborescence du projet vers ce fichier. C'est très pratique.

Quelques inconvénients sont qu'il n'est pas gratuit. Et parfois, il peut être gourmand en mémoire avec des projets très volumineux. Cela s'est amélioré au fil des ans et le contenu des fichiers est indexé en interne de sorte que la recherche dans de grands projets est très rapide. Une mise à jour récente inclut également une amélioration significative de la vitesse de démarrage.

## Conseils généraux de productivité pour les éditeurs

Le raccourci de duplication de ligne/sélection (dans WebStorm : ctrl-d, dans Atom : ctrl-shift-d, mais ils peuvent tous le faire) est l'un de mes préférés et peut faire gagner beaucoup de temps dans de nombreux scénarios de codage.

Cela peut arriver de temps en temps où vous avez une liste d'éléments et devez modifier le premier (ou certains) caractère de chaque ligne, par exemple de '.' à ',', mais la recherche-remplacement n'est pas pratique à utiliser. WebStorm permet alt-clic pour placer plusieurs curseurs afin de faire les mêmes modifications à plusieurs endroits. Pourtant, je trouve l'approche suivante plus rapide dans certains scénarios :

* Placez votre curseur après le premier point, et commencez à faire le changement manuellement.
* Appuyez sur backspace, virgule, flèche bas. Ayez un doigt sur chaque touche, et répétez les pressions en commençant lentement puis en accélérant au fur et à mesure. Une fois que vous avez le motif, vous pouvez accélérer jusqu'à parcourir une liste de 200 lignes en un rien de temps.

C'est presque comme jouer une mélodie sur un piano (aussi vite que vous pouvez). Vous pouvez faire cela avec des listes numérotées également. Écrivez la première ligne sans le numéro, dupliquez la ligne 9 fois, et faites le même processus sauf que vous avez un doigt qui appuie sur un numéro suivant chaque fois. Commencez les 10 lignes suivantes avec un '1' et faites le même processus en ajoutant un chiffre après chaque '1'.

Si vous cherchez sur Google "[nom de l'éditeur] cheatsheet", vous pouvez obtenir un résumé rapide des utilisateurs pour les configurations ou raccourcis importants de l'éditeur que vous essayez. Imprimez-le et lisez tous les raccourcis pour prendre conscience des nouvelles fonctionnalités et fonctionnalités auxquelles vous pourriez ne pas être exposé autrement.

Envisager comment les actions mises en évidence peuvent améliorer vos processus actuels sera bénéfique. Si vous en voyez une qui peut aider, mettez une marque à côté afin que la prochaine fois que vous serez dans cette situation, il soit facile de vous en souvenir. Même si vous l'utilisez rarement et principalement au début, avoir une référence rapide à portée de main peut réduire la friction pour en apprendre davantage sur votre éditeur et peut faire gagner du temps en changeant de contexte et en recherchant à l'avenir.

Je vais jusqu'à trouver la version PDF, l'imprimer et la plastifier pour référence future, mais pour certains, un marque-page ou une capture d'écran peut également fonctionner.

## Conclusion

Si vous êtes un débutant espérant apprendre JavaScript et utiliser un environnement de développement poli pour commencer, VSCode est le choix évident car il est facile à utiliser avec de nombreuses fonctionnalités solides intégrées.

Pour les développeurs plus expérimentés qui savent exactement ce qu'ils veulent, Sublime et Atom peuvent être préférables car ils vous donneront un contrôle complet sur votre environnement de développement. Vous pouvez choisir parmi des milliers de fonctionnalités (packages) à installer et garder le démarrage de l'application et l'utilisation des ressources exempts d'extras dont vous n'avez pas besoin ou que vous ne voulez pas. Passer un peu de temps avec chacun vous aidera à faire le bon choix.

Pour les utilisateurs chevronnés qui se sentent à l'aise en utilisant uniquement le clavier pour travailler sur des projets, vous pouvez être plus efficace avec Vim que avec tout autre éditeur. Économiser le temps qu'il faut pour que votre main se déplace entre le clavier et la souris s'additionnera, mais il faudra un certain temps pour maîtriser ce processus !

Enfin, si vous ne voyez pas d'inconvénient à maintenir un abonnement payant et que vous n'êtes pas préoccupé par les limitations de mémoire ou de CPU de votre machine de développement, WebStorm vous permettra de démarrer rapidement, quel que soit le JavaScript, les transpileurs ou les processus de construction avec lesquels vous travaillez. Il offre un environnement très pratique pour travailler.

J'utilise personnellement WebStorm comme mon IDE principal, mais j'utilise toujours régulièrement VSCode pour éditer des fichiers individuels ou très volumineux lorsque la performance est une priorité.

Si vous avez aimé cet article, envisagez de consulter [JSCharting](https://jscharting.com/), une bibliothèque de graphiques JavaScript pour les développeurs. Vous pouvez également consulter des articles de blog supplémentaires [ici](https://jscharting.com/blog/).