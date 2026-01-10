---
title: Comment Construire un Site WordPress Localement - Ce Que Vous Devez Savoir
subtitle: ''
author: Jim Campbell
co_authors: []
series: null
date: '2021-02-22T19:22:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-wordpress-website-locally
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/ilya-pavlov-OqtafYT5kTw-unsplash.jpg
tags:
- name: WordPress
  slug: wordpress
seo_title: Comment Construire un Site WordPress Localement - Ce Que Vous Devez Savoir
seo_desc: WordPress is the most popular content management system in the world. Whether
  you are an experienced developer using the tech that powers 38% of all websites
  or you are just getting started in WordPress, building locally on your computer
  is a low-cos...
---

WordPress est le système de gestion de contenu le plus populaire au monde. Que vous soyez un développeur expérimenté utilisant la technologie qui alimente 38 % de tous les sites web ou que vous débutiez avec WordPress, construire localement sur votre ordinateur est un moyen peu coûteux, favorable aux tests et rapide de créer des sites WordPress.

## Que signifie construire localement ?

Un "environnement de développement local" ou "développer localement" signifie simplement héberger les fichiers du site web sur votre ordinateur plutôt que sur les serveurs d'un hébergeur web.

Vous le faites peut-être déjà. De nombreux programmeurs [développent des applications backend localement](https://forum.freecodecamp.org/t/developing-backend-applications-locally/147374).

Si vous débutez dans le développement web, vous avez peut-être construit quelques sites de base avec HTML et CSS en utilisant des éditeurs de texte comme [Atom](https://atom.io/), [Sublime](https://www.sublimetext.com/), ou [Visual Studio Code](https://code.visualstudio.com/). Ces sites simples sont déjà hébergés localement.

Lorsque vous commencez à exécuter du code plus avancé qui nécessite l'utilisation de PHP, JavaScript et SQL, vous avez besoin d'outils plus avancés que nous aborderons plus tard.

## Pourquoi devrais-je construire un site WordPress localement ?

Avant de passer aux outils dont vous avez besoin pour construire un site WordPress localement, examinons rapidement pourquoi vous devriez le faire.

Je parlais récemment avec un autre développeur web, Daniel, qui construit tous ses sites localement. Il a commencé par construire des sites simples en HTML et CSS et construit également des sites WordPress plus avancés.

Ses principales raisons de construire localement, que je trouvais excellentes, sont :

1. **Installation rapide** - il n'est pas nécessaire d'attendre un fournisseur d'hébergement ou de configurer un nom de domaine. Je travaille pour plusieurs petites entreprises et le fait de pouvoir rapidement sortir une maquette de design est un énorme avantage du développement local.
2. **Faible coût** - l'hébergement et les noms de domaine peuvent être coûteux. Développer localement est gratuit !
3. **Pas besoin de nom de domaine** - si vous n'êtes pas fixé sur un nom de domaine, vous pouvez toujours commencer à construire localement. Cela offre une grande flexibilité et vous évitera les tracas de la migration de votre site WordPress.
4. **Tests faciles** - lorsque vous développez localement, vous pouvez expérimenter plus facilement avec des plugins, des thèmes et du développement personnalisé. Pas de soucis si vous cassez votre site. Vous êtes la seule personne qui peut voir et utiliser le site, alors allez vite et cassez des choses !
5. **Vitesse du site** - lorsque vous mettez à jour votre site, vous n'avez pas besoin d'attendre qu'un serveur rende la page. C'est comme naviguer sur internet avec des vitesses instantanées.

## Comment Construire un Site WordPress Localement

Maintenant que vous avez décidé de construire votre site WordPress localement, vous avez besoin de l'aide d'un outil pour construire votre site.

Ces outils installeront un **logiciel de serveur web**, **PHP**, et une **gestion de base de données SQL** sur votre ordinateur. Installer tout cela séparément sur votre ordinateur peut être confus, donc ces outils vous faciliteront la vie et vous permettront de commencer à construire plus rapidement.

Voici deux outils utilisés pour développer WordPress localement et les étapes nécessaires pour commencer.

### DevKinsta

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-110.png)

DevKinsta est un logiciel gratuit fourni par Kinsta, lancé en janvier 2021. Je l'ai récemment utilisé pour lancer un site et il était incroyablement facile à utiliser.

Il rend la création et le développement de sites locaux rapides et faciles pour les débutants. DevKinsta installe Nginx, MariaDB, et plus encore avec un seul clic.

Il faut environ 2 minutes pour l'installer et commencer à construire votre site local, développer des thèmes, expérimenter avec des plugins, et faire du développement PHP personnalisé.

Puisqu'il s'agit d'un outil fourni par un hébergeur, lorsque vous êtes prêt à mettre le site en ligne, il est envoyé à Kinsta. Pour cette raison, vous ne devriez utiliser cet outil que si vous choisissez d'héberger votre site WordPress avec Kinsta. J'héberge actuellement 20 sites pour moi et mes clients sur Kinsta et je les trouve incroyables.

### XAMPP

%[https://www.youtube.com/watch?v=h6DEDm7C37A]

L'utilisation de XAMPP nécessite plus d'étapes que DevKinsta, mais vous en apprendrez beaucoup sur les services et bibliothèques qui doivent être en cours d'exécution pour supporter votre site WordPress.

XAMPP est un package open source qui est gratuit et facile à installer. La distribution Apache contient MariaDB, PHP et Perl. Une fois que vous avez téléchargé et installé le logiciel, vous aurez accès à l'application du panneau de contrôle XAMPP.

En utilisant le panneau de contrôle XAMPP, vous pouvez exécuter le serveur web Apache comme votre serveur local et MySQL comme votre serveur de base de données. Vous devrez "Démarrer" les modules Apache et MySQL à partir de ce panneau pour transformer efficacement votre ordinateur en serveur. Voilà - vous avez un serveur !

En plus de XAMPP, vous devrez télécharger WordPress depuis WordPress.org. Extrayez le fichier zip dans **.../XAMPP/htdocs/{ici}**. Avec MySQL et Apache activés, vous devriez maintenant pouvoir accéder à votre site depuis un navigateur à l'adresse **https://localhost/wordpress/**. Voilà - vous avez les fichiers principaux de WordPress !

Aller à l'URL ci-dessus vous invitera à suivre l'assistant d'installation de WordPress avec une autre installation technique cruciale - la base de données.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-111.png)

L'application phpMyAdmin est préinstallée avec XAMPP. Vous pouvez y accéder à l'adresse **https://localhost/phpmyadmin/**. C'est ici que vous créerez votre base de données en utilisant une interface plus simple que vous connaissez peut-être déjà.

Cliquez sur **Bases de données** puis sur **Créer** pour ajouter rapidement une nouvelle base de données. Voilà - vous avez la base de données dont vous avez besoin !

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-112.png)

Retournez à votre site local à l'adresse **https://localhost/wordpress/** et entrez les informations de votre nouvelle base de données, en utilisant "root" comme nom d'utilisateur et sans mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-113.png)

Cliquez sur Soumettre et l'écran suivant finalisera votre installation de WordPress. Vous serez invité à choisir un Nom de Site, un Nom d'utilisateur et un Mot de passe. Après cela, vous pourrez accéder à l'arrière-plan de votre site WordPress local à l'adresse **https://localhost/wordpress/wp-admin**.

L'utilisation de XAMPP peut être compliquée. J'ai été incroyablement frustré par certaines de mes installations locales, mais il y a beaucoup d'aide à trouver en ligne.

Passer par l'exercice de configuration d'une installation WordPress locale vous apprendra des aspects importants de la configuration du serveur, de la gestion de la base de données et du fonctionnement des fichiers principaux de WordPress.

Une fois que vous êtes opérationnel, vous pouvez expérimenter et développer sans les limites d'utilisation d'un serveur.

## Conclusion

Développer WordPress localement est quelque chose avec lequel tout développeur WordPress devrait être à l'aise.

Travailler depuis chez soi et ne pas avoir à se déplacer m'a donné un peu de temps supplémentaire dans la journée que j'ai alloué à la construction de sites web. J'ai pu revisiter et réévaluer mon ensemble d'outils de développement local pour créer plus facilement des sites WordPress. J'espère que mes réflexions vous seront utiles.

Nous n'avons couvert que deux outils à utiliser dans cet article. CodeInWP a des outils supplémentaires qu'ils recommandent pour le développement local. Une fois que vous avez choisi une pile de développement local, construit un site WordPress, créé un super design et un logo, et choisi un hébergeur - votre création sera prête pour internet. Bon développement !