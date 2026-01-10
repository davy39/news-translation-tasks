---
title: Principales raisons pour lesquelles votre application mobile est lente et comment
  la corriger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-01T15:29:14.000Z'
originalURL: https://freecodecamp.org/news/top-reasons-why-your-mobile-app-is-slow-and-how-to-fix-it-f0f7ce524934
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AY6UWfeKLTcOmfQWeOq5rQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: servers
  slug: servers
- name: technology
  slug: technology
seo_title: Principales raisons pour lesquelles votre application mobile est lente
  et comment la corriger
seo_desc: 'By Rajput Mehul

  At a time when technology is moving ahead at an express pace and people don’t have
  any patience, you’ve got to remain on the tips of your toes to ensure you retain
  your users.

  It’s true that a majority of end users can’t wait to get a...'
---

Par Rajput Mehul

À une époque où la technologie avance à un rythme effréné et où les gens n'ont aucune patience, vous devez rester sur le qui-vive pour vous assurer de conserver vos utilisateurs.

Il est vrai qu'une majorité d'utilisateurs finaux ne peuvent pas attendre pour obtenir une réponse d'une application mobile. Le temps de chargement idéal pour une application mobile est d'environ **deux** secondes. Cependant, [selon une étude d'Akamai Research](https://wemakewebsites.com/blog/a-1-second-delay-on-your-page-load-can-cause-a-7-reduction-in-conversions-how-do-you-solve-it), pour chaque seconde supplémentaire que l'application consomme, le taux de conversion diminue de 7 %.

Pour ajouter à la misère, les utilisateurs ont tendance à se frustrer et à se mettre en colère s'ils doivent attendre plus longtemps, et ne reviennent jamais sur la même application. Un autre [rapport](http://www.apteligent.com/news-press/latency-impacts-user-experience-48-percent-of-consumers-uninstall-or-stop-app-use-due-to-slow-speeds-crittercism-report-reveals/) révèle que 48 % des clients désinstallent ou cessent d'utiliser une application si elle est lente.

Par conséquent, la première tâche impérative à accomplir est de trouver la cause ou la raison réelle pour laquelle l'application est lente. Une fois que vous avez identifié le problème principal, vous pouvez alors prendre les mesures nécessaires pour résoudre le problème et offrir à vos utilisateurs une expérience améliorée.

Les principaux problèmes qui rendent votre application mobile lente sont :

1. Votre application est obsolète et non supportée
2. Lenteur de la vitesse du serveur
3. Les connexions cryptées ne sont pas optimisées
4. Conversations trop verbales
5. Bibliothèque et kit de développement logiciel défectueux
6. L'application est surchargée de données
7. Latence du réseau

Dans cet article, nous allons aborder chacun de ces problèmes en détail. Alors, commençons.

### 1. Votre application est obsolète et non supportée

Si vous êtes dans le domaine du développement d'applications, vous devez bien savoir à quel point il est important de [mettre à jour votre application à intervalles réguliers](https://www.mindinventory.com/blog/how-would-you-know-when-your-app-needs-a-major-update/). Que vous soyez un développeur d'applications Android ou iOS, vous devez vous assurer que l'application est conçue sur la dernière version du système d'exploitation.

![Image](https://cdn-media-1.freecodecamp.org/images/wjrytijovr1s31oAuMMryMP6CpjUDqfNvuuu)

Par exemple, actuellement, pour Android, il doit s'agir d'Oreo ou de Nougat. Pour iOS, il doit s'agir d'iOS 11 ou 10. Donc, si vous n'optimisez pas vos applications pour qu'elles fonctionnent sur ces plateformes, ou si vous utilisez un framework plus ancien, l'application tend à devenir lente. De plus, les versions plus anciennes des plateformes ne reçoivent pas le support nécessaire de la part du fournisseur, et après une date spécifique, le support s'arrête complètement.

La solution au problème consiste à mettre à jour et optimiser le logiciel et à se tenir au courant des dernières tendances liées au développement et à la conception d'applications. La mise à jour de votre application et son test sur les nouvelles plateformes garantissent également qu'elle est compatible avec les nouvelles versions du système d'exploitation. Cela améliore également les performances de votre application.

Vous recevez toujours des informations mises à jour sur les alertes de sécurité et les corrections de bugs, ce qui accélère la vitesse de l'application.

### 2. Lenteur de la vitesse du serveur

Vous avez probablement rencontré ce message de nombreuses fois - le serveur est hors service ou non connecté. Eh bien, c'est l'une des raisons courantes pour lesquelles certains sites web mettaient beaucoup de temps à se charger, et le même problème se répète ici avec les applications mobiles. Le serveur est lent ou il est surchargé.

![Image](https://cdn-media-1.freecodecamp.org/images/SFIKC4mEEFQMC60WlryQWciksdNSLHw4VcVf)

Il peut y avoir plusieurs raisons pour lesquelles l'infrastructure backend est lente :

* Le serveur peut ralentir en raison de l'infrastructure multi-niveaux sur laquelle fonctionnent la plupart des applications modernes.
* Vous pouvez avoir des problèmes pour accéder aux fichiers depuis le disque, exécuter le code de l'application, ou communiquer instantanément avec les utilisateurs via le chat, etc.

La cause profonde de tous ces problèmes est la même : un serveur surchargé ou surmené. Parfois, le problème peut être lié à la latence d'un autre processus sur lequel votre application s'appuie fortement pour la plupart de ses tâches.

Pour résoudre le problème, vous pouvez adopter quelques approches.

1. Identifier les interactions entre les différents composants de l'application, ce qui est connu sous le nom de Application Dependency Mapping (ADM).
2. Essayez de soulager le serveur en fournissant un serveur proxy inverse supplémentaire. Un proxy inverse offre de nombreux avantages et accélère les requêtes web en fournissant une compression, une terminaison SSL, une mise en cache et d'autres avantages.

En fait, vous pouvez choisir une autre alternative qui consiste à déployer un équilibreur de charge pour aider à distribuer le trafic de manière uniforme.

### 3. Les connexions cryptées ne sont pas optimisées

Les connexions SSL/TLS fournissent un cryptage pour les données en transit et sont cruciales du point de vue du développement d'applications. Ne les négligez donc pas ! Mais elles aussi peuvent créer des problèmes si elles ne sont pas optimisées.

![Image](https://cdn-media-1.freecodecamp.org/images/EkL6LEKy2v0eCnel9RUJV-t7EtZnlbdkCEUv)

Les connexions cryptées non optimisées entraînent une diminution des performances de l'application. Certaines des principales raisons identifiées par les experts sont :

1. Une poignée de main est requise chaque fois que vous ouvrez une nouvelle connexion, ce qui affecte la vitesse.
2. Des problèmes sont rencontrés lors du cryptage des données sur le serveur et du décryptage côté client.

Pour résoudre ces problèmes, les connexions cryptées doivent être optimisées. Cela peut être fait en incorporant HTTP/2 et SPDY qui réduisent la surcharge de connexion avec les clients en ne nécessitant qu'une seule poignée de main pour chaque session.

Vous pouvez également adopter d'autres techniques pour résoudre le problème, telles que l'utilisation d'OpenSSL, de Session Tickets, de la mise en cache de session, etc.

### 4. Conversations trop verbales

Le problème des conversations trop verbales avec le serveur d'application se produit lorsque le client fait plusieurs requêtes pour effectuer une transaction au nom des opérations individuelles au sein de l'application.

Maintenant que la virtualisation a été introduite, cela vous permet de développer une version virtuelle de l'appareil ou de la ressource, comme un appareil de stockage, le serveur, le réseau, ou même le système d'exploitation.

Il se peut que l'équipe serveur ait configuré l'image du serveur migrée automatiquement vers un hôte qui est peu chargé en raison de la virtualisation. Elle peut déplacer l'image du serveur vers un autre emplacement afin qu'elle se trouve à plusieurs millisecondes des serveurs ou du système de stockage sur disque.

Si vous souhaitez résoudre ce problème, vous devez examiner le nombre de requêtes entre les systèmes où il est lié au réseau. Il est également bon de vérifier les retards entre les requêtes.

### 5. Bibliothèque et kit de développement logiciel défectueux

Un développeur d'applications peut être très particulier quant à la garantie de performances de classe mondiale. Cependant, il peut y avoir des problèmes avec les bibliothèques et le kit de développement logiciel (SDK) fournis par le fournisseur qui sont hors du contrôle du développeur.

Vous devez examiner le code des bibliothèques tierces pour voir s'il contient des erreurs ou des bugs. Si les bibliothèques ne sont pas surveillées attentivement, l'application tend à devenir lente.

Quelques exemples de problèmes avec les bibliothèques tierces qui viennent à l'esprit sont :

* Permettre le chargement d'images dans l'application en utilisant les bibliothèques [Picasso](http://square.github.io/picasso/) et [Glide](https://bumptech.github.io/glide/)
* Simplifier le processus de communication entre différentes parties de l'application en utilisant la bibliothèque [Eventbus](https://github.com/greenrobot/EventBus)
* Retrofit, une bibliothèque basée sur Android qui aide à organiser les appels API dans un projet

Assurez-vous d'utiliser des bibliothèques sécurisées, stables et fiables qui ont une grande communauté.

### 6. L'application est surchargée de données

Eh bien, ce n'est pas de la science-fiction et peut être facilement identifié et résolu. L'application devient surchargée de données et le résultat est que l'application ralentit. Si trop de serveurs sont chargés, cela consomme beaucoup de temps. Cependant, ce n'est pas une bonne idée de réduire vos données et de compromettre les fonctionnalités pratiques de votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/yN8VBW50gIT3qyQNEwAZ9hCP94qe75K2-Tz0)

La solution la plus simple et sans aucun doute la meilleure au problème est la compression des données. Que vous ayez des images, des vidéos, des graphiques ou du contenu audio, si vous compressez les données, cela rendra le chargement de votre application plus rapide et vous n'aurez pas à toucher à ses fonctionnalités ou à sa fonctionnalité.

Mais vous devez choisir les normes de compression appropriées en fonction de la taille du fichier et du contenu. Si nous parlons de certaines des méthodes courantes pour compresser ou réduire la taille des données, il existe deux options disponibles. La première est la méthode sans perte et la seconde est la compression avec perte.

1. **Compression sans perte :** Dans cette méthode, le développeur peut restaurer le fichier à sa taille d'origine et il n'y a pas de perte de données lorsque le fichier n'est pas compressé. Ce type de technique de compression de données est utilisé lors de la réduction de la taille des documents texte et des feuilles de calcul.
2. **Compression avec perte :** Dans la deuxième approche, vous supprimez en fait les données de l'application, ce qui n'est généralement pas vraiment noticeable. Cette méthode de compression de données est utilisée pour compresser la taille des fichiers vidéo, audio et graphiques.

### 7. Latence du réseau

La vitesse du réseau peut grandement affecter la vitesse de votre application mobile. Si le réseau est lent, les performances de l'application seront également lentes. Si une application effectue une requête vers un serveur DNS principal inexistant et ne reçoit pas de réponse, elle essaiera le deuxième serveur DNS — mais cela ralentit la vitesse de l'application.

Pour résoudre le problème, vous devez vérifier la vitesse du réseau en permanence et voir quand l'application ralentit.

### Conclusion

Les applications mobiles sont une excellente source pour atteindre votre public cible. Mais si elles ne fonctionnent pas à la hauteur ou deviennent lentes, cela doit être traité rapidement. Il existe différentes raisons pour lesquelles votre application perd en vitesse, vous devez donc identifier le problème exact et le résoudre dès que possible.

Alternativement, vous pouvez utiliser les services d'une entreprise de développement d'applications expérimentée et hautement fiable comme [MindInventory](https://www.mindinventory.com) qui dispose de développeurs experts comprenant l'astuce pour accélérer la vitesse des applications pour faire le travail :)

Si vous avez aimé cette histoire, veuillez cliquer sur le bouton ? et partager pour aider les autres à la trouver !