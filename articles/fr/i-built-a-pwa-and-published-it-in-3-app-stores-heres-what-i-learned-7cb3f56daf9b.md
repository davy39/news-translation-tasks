---
title: J'ai créé une Progressive Web App et je l'ai publiée dans 3 magasins d'applications.
  Voici ce que j'ai appris.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-26T03:06:44.000Z'
originalURL: https://freecodecamp.org/news/i-built-a-pwa-and-published-it-in-3-app-stores-heres-what-i-learned-7cb3f56daf9b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xpelf7JVxaQryjTK.png
tags:
- name: Entrepreneurship
  slug: entrepreneurship
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: J'ai créé une Progressive Web App et je l'ai publiée dans 3 magasins d'applications.
  Voici ce que j'ai appris.
seo_desc: 'By JudahGabriel Himango

  One month of work, several hundred dollars, and lots of red tape.

  I recently published Chavah Messianic Radio, a Pandora-like music player, as a Progressive
  Web App and submitted it to the 3 app stores (Google Play, iOS App St...'
---

Par JudahGabriel Himango

#### Un mois de travail, plusieurs centaines de dollars et beaucoup de paperasserie.

J'ai récemment publié [Chavah Messianic Radio](https://messianicradio.com/), un lecteur de musique similaire à Pandora, en tant que Progressive Web App et je l'ai soumis aux 3 magasins d'applications (Google Play, iOS App Store, Windows Store).

![Image](https://cdn-media-1.freecodecamp.org/images/62wLkOAc65vJn5o0GBCuKCBtEQhVZZZKb-8n)

![Image](https://cdn-media-1.freecodecamp.org/images/gUOEhRj9hddNR96-lkQ-h1b6Cdzyi59x3V1c)

![Image](https://cdn-media-1.freecodecamp.org/images/e16fvva-1318NaMEUXmI-785IT9AT7krylho)

Le processus a été à la fois douloureux et éclairant. Voici ce que j'ai appris.

### Pourquoi ?

Tout d'abord, vous pourriez vous demander, « Pourquoi même mettre votre application dans les magasins d'applications ? Vivez simplement sur le web ouvert ! »

La réponse, en un mot, est que **c'est là que se trouvent les utilisateurs**. Nous avons formé une génération d'utilisateurs à trouver des applications dans des magasins d'applications propriétaires, et non sur le web libre et ouvert.

Pour mon application web, il y avait 2 grandes raisons de se retrouver dans le magasin d'applications :

1. La demande des utilisateurs
2. Les restrictions des applications web par les plateformes mobiles hostiles d'Apple

Demande des utilisateurs : Mes utilisateurs me demandent depuis des années, « Y a-t-il une application pour Chavah ? Je ne la vois pas dans le magasin. »

Ils posent cette question parce que nous avons formé les utilisateurs à chercher des applications dans des magasins d'applications propriétaires.

Ma réponse à mes utilisateurs a été jusqu'à présent,

> _« Oh, vous n'avez pas besoin d'une application, allez simplement sur le site web depuis votre téléphone ! Ça marche ! »_

Mais je mentais un peu.

Les vraies applications web ne fonctionnent que plus ou moins sur mobile. Ce qui m'amène à la deuxième raison : les restrictions des applications web par les plateformes mobiles hostiles d'Apple.

Les fournisseurs de plateformes mobiles, comme Apple, sont _totalement cool_ avec les applications qui utilisent votre téléphone à son plein potentiel. Accédez à votre localisation, jouez de l'audio en arrière-plan, obtenez vos coordonnées GPS, jouez plus d'une chose à la fois, et plus encore.

Apple est totalement cool avec ça.

**Mais seulement si vous payez Apple 99 $/an pour le privilège.**

Si vous voulez faire l'une de ces choses dans une vieille application web régulière, eh bien, bon sang, Apple ne se contentera pas de vous les refuser, il _vous empêchera même de demander la permission_.

Pour mon application de lecteur de musique similaire à Pandora, cette [horrible panne est apparue de nombreuses manières](http://debuggerdotbreak.judahgabriel.com/2016/12/13/its-almost-2017-and-html5-audio-is-still-broken-on-ios/).

Des petites choses comme « iOS Safari ne vous laisse pas jouer de l'audio sans d'abord interagir avec la page » à des choses majeures et bloquantes comme « iOS Safari ne vous laisse pas jouer la chanson suivante si votre application est en arrière-plan ou si votre écran est éteint. »

Oh, plus des anomalies visuelles étranges comme [taper dans une zone de texte et voir votre texte apparaître ailleurs sur l'écran](https://stackoverflow.com/questions/46339063/ios-11-safari-bootstrap-modal-text-area-outside-of-cursor).

Donc, pour rendre mon application musicale HTML5 réellement fonctionnelle et opérationnelle sur les appareils mobiles des gens, il était nécessaire de transformer mon PWA en une application dans le magasin d'applications.

### Barrières à l'entrée

Dans un monde idéal, la publication de votre application web dans les magasins d'applications ressemblerait à ceci :

* Votre hébergeur Web/Cloud ou votre fournisseur d'intégration continue
* Vous avez publié une Progressive Web App. Publier dans les magasins d'applications ?

☑ iOS App Store

☑ Google Play

☑ Windows Store

(Ou alternativement, comme [Microsoft expérimente](https://www.windowscentral.com/first-batch-windows-10-progressive-web-apps-here), votre PWA apparaîtra simplement automatiquement dans le magasin d'applications lorsque Bing l'explorera.)

Mais hélas, nous ne vivons pas dans ce monde idéal. Au lieu de cela, nous devons traiter avec toutes sortes de BS natifs propriétaires pour faire entrer nos applications web dans les magasins.

Chacun des magasins d'applications a une barrière à l'entrée : à quel point il est difficile de prendre une application web existante et de la mettre dans le magasin d'applications.

Je liste certaines des barrières ci-dessous.

### Coût

* **Apple** : 99 $/an pour avoir votre application listée dans le magasin d'applications iOS.
* **Google** : Frais uniques de 25 $ pour lister votre application dans le Google Play Store.
* **Microsoft** : Gratuit !

Ne me faites pas payer pour rendre mon application disponible à vos utilisateurs. Mon application enrichit votre plateforme. Sans de bonnes applications, votre plateforme sera abandonnée.

Apple comprenait cela autrefois. Lorsqu'il a introduit l'iPhone pour la première fois, Steve Jobs était catégorique : HTML5 était l'avenir et les applications seraient simplement des applications web. [Il n'y avait pas de SDK natif pour l'iPhone](https://9to5mac.com/2011/10/21/jobs-original-vision-for-the-iphone-no-third-party-native-apps/) pour les tiers. Apple a depuis abandonné cette vision.

Google a demandé des frais symboliques de 25 $ une seule fois. Probablement pour éviter les spammeurs et réduire le nombre d'applications vraiment nulles entrant dans le magasin.

Microsoft semble déterminé à simplement augmenter le nombre total d'applications dans son magasin d'applications, quelle que soit la qualité.

**Gagnant** : Microsoft. Il est difficile de battre gratuit.

### Ajout de fonctionnalités natives

Dans un monde idéal, je n'aurais pas à écrire une seule ligne de code supplémentaire pour que mon application web s'intègre à l'OS. Ou, comme Steve Jobs [l'a dit en 2007](https://9to5mac.com/2011/10/21/jobs-original-vision-for-the-iphone-no-third-party-native-apps/),

> _« Le moteur complet de Safari est à l'intérieur de l'iPhone. Et donc, vous pouvez écrire des applications Web 2.0 et Ajax incroyables qui ressemblent exactement et se comportent exactement comme des applications sur l'iPhone. Et ces applications peuvent s'intégrer parfaitement aux services iPhone. Elles peuvent passer un appel, envoyer un email, chercher un lieu sur Google Maps. »_

> _-Steve Jobs, 2007_

Pour moi, cela signifie que mon application web joue de l'audio en arrière-plan en utilisant l'audio HTML5 standard ; cela fonctionne très bien sur tous les OS.

Mon application web déclare ce qui est en train de jouer, et les OS le détectent, affichent les informations sur la chanson en cours de lecture sur l'écran de verrouillage.

Mon application contrôle l'audio en utilisant l'API audio HTML5 standard ; l'OS le détecte et fournit des contrôles de lecture/pause/suivant/volume/barre de piste sur l'écran de verrouillage.

Mais malheureusement, nous ne vivons pas dans ce monde idéal. Toutes les choses listées ci-dessus ne fonctionnent pas réellement « out of the box » sur les 3 plateformes.

Mon application web doit jouer de l'audio en arrière-plan. Et charger des URL depuis mon CDN. Cela semble raisonnable, non ? Et en bonus, comment afficher les informations sur la chanson en cours de lecture sur l'écran de verrouillage ? Et contrôler l'audio (lecture/pause/suivant, etc.) depuis l'écran de verrouillage ? À quel point est-ce difficile ?

Trois approches très différentes ont été adoptées ici :

* **Apple** : Nous ne donnons pas aux applications web un moyen de déclarer de telles capacités ; vous devrez écrire un wrapper natif (par exemple, avec Cordova) pour interagir avec l'OS.
* **Google** : Le web FTW ! Créons [un nouveau standard web](https://developers.google.com/web/updates/2017/02/media-session) qui montre l'audio et les contrôles depuis l'écran de verrouillage. Audio en arrière-plan ? Bien sûr, allez-y !
* **Microsoft** : Nous allons injecter notre API propriétaire, window.Windows.*, dans votre espace de noms global JavaScript et vous pouvez l'utiliser pour faire les choses que vous voulez faire.

En entrant dans plus de détails ici pour chaque magasin :

Pour le magasin d'applications iOS, votre application web doit-elle jouer de l'audio en arrière-plan ? [Utilisez un plugin Cordova](https://github.com/danielsogl/cordova-plugin-background-audio). Besoin d'afficher la chanson en cours de lecture sur l'écran de verrouillage ? [Utilisez un plugin Cordova](https://github.com/leon/cordova-plugin-nowplaying). Besoin de contrôler la chanson en cours de lecture depuis l'écran de verrouillage ? [Utilisez un plugin Cordova](https://github.com/leon/cordova-plugin-remotecommand). Vous voyez l'idée. Basiquement, Cordova trompe Apple en lui faisant croire que vous êtes une application native. Et puisque vous n'êtes pas une application web dégoûtante, Apple vous laisse faire toutes les choses que les applications natives peuvent faire. Vous avez juste besoin de trucs natifs — des plugins Cordova — pour vous laisser faire cela.

Pour Google Play, c'est bien que je puisse simplement écrire du code JS pour faire fonctionner cela ; aucun plugin Cordova n'est requis ici. Bien sûr, ce JS ne fonctionnera nulle part ailleurs que sur Chrome sous Android... mais hé, peut-être un jour (dans un monde idéal !) tous les navigateurs mobiles implémenteront ces API web... et le monde vivra en harmonie. Je suis presque prêt à sortir quelques airs de l'utopie hippie de John Lennon.

Pour le Windows Store, voulez-vous jouer de l'audio en arrière-plan ? Désolé ! C'est-à-dire, à moins que vous ne déclariez vos intentions dans notre fichier manifeste de capacités propriétaires (facile) _ET_ que vous implémentiez cette interface média propriétaire en utilisant [window.Windows.SystemMediaTransportControls](https://stackoverflow.com/questions/49240479/enabling-background-audio-in-my-windows-store-html5-app?rq=1) (pas si facile). Sinon, nous vous mettrons en sourdine lorsque votre application passera en arrière-plan.

**Gagnant** : Google. Je veux pouvoir simplement écrire du JavaScript, et laisser l'OS détecter les indices de mon application.

**Deuxième** : Windows. Je peux toujours écrire du JavaScript classique, mais je dois parler à une API JS Windows propriétaire qui a été injectée dans mon processus lors de l'exécution sur Windows. Pas terrible.

**Perdant** : Apple. Ils ne se soucient pas des applications web. En fait, c'est pire que cela. On a l'impression qu'ils sont réellement _hostiles_ aux applications web. iOS Safari est le nouveau Internet Explorer 6. Il a pris du retard dans presque tous les standards web, surtout autour des Progressive Web Apps. Cela est probablement pour des raisons commerciales : les applications web perturbent leur racket de 99 $/an + 33 % d'achats intégrés. Donc, pour faire fonctionner mon application web sur leur plateforme, je dois essentiellement prétendre que je suis une application native.

### Enregistrement dans l'App Store

Soumettre votre PWA au magasin d'applications nécessite un enregistrement, une vérification de l'entreprise, et plus de paperasserie. Voici comment les 3 magasins d'applications s'en sont sortis :

* **Apple** : Vous devez prouver que vous êtes une entreprise légale et enregistrée. Cette vérification n'est pas faite par nous — mais [par un tiers](http://www.dnb.com/), qui peut ou non connaître votre entreprise.
* **Google** : Vous voulez votre application dans notre magasin ? Cool pour nous.
* **Microsoft** : Vous voulez votre application dans notre magasin ? Cool pour nous.

Le plus gros point de douleur pour moi a été de me faire vérifier en tant qu'entreprise légale par Apple.

Tout d'abord, je suis allé sur le site et je me suis inscrit au programme pour développeurs d'Apple. J'ai rempli mon nom et les informations de mon entreprise. (À part : je suppose qu'Apple ne vous laisse pas soumettre une application à moins d'avoir une entreprise enregistrée et légale ?)

Je clique sur suivant.

« Les informations que vous avez entrées ne correspondent pas à votre profil D&B. »

Mon... quoi ?

Un peu de recherche sur Google a montré que « profil D&B » est Dun et Bradstreet. Je n'avais jamais entendu parler de ce groupe auparavant, mais je découvre qu'Apple les utilise pour vérifier les détails de votre société légale.

Et apparemment, mon profil D&B ne correspondait pas à ce que j'avais mis dans mon enregistrement Apple Dev.

Je fais plus de recherches sur Google et je trouve les forums de développement Apple jonchés de posts similaires. Personne n'avait de bonne réponse.

Je contacte le support Apple Dev. 24 heures plus tard, je suis contacté par email me disant que je devrais contacter D&B.

![Image](https://cdn-media-1.freecodecamp.org/images/t16Xm1QZET5YPeKUbdJEma2DHqYalp61elEv)

Je décide de les contacter... mais Apple dit qu'il faudra jusqu'à quelques jours pour qu'ils répondent.

À ce stade, je pense à abandonner toute l'idée.

En attendant que le support D&B me recontacte, je décide d'aller sur le site D&B, de vérifier mon identité et de mettre à jour les informations de mon entreprise que, je suppose, ils avaient prises à partir des dossiers d'enregistrement gouvernementaux.

Ai-je mentionné à quel point c'est nul ? Je veux simplement lister mon application web existante dans le magasin. S'il vous plaît, aidez-moi.

Je vais sur D&B pour mettre à jour mon profil d'entreprise. Surprise ! Ils ont un bug JavaScript dans leur logique de validation qui m'empêche de mettre à jour mon profil.

Heureusement, je suis un développeur compétent. Je clique pour mettre un point d'arrêt dans leur JavaScript, je clique sur soumettre, je change le drapeau isValid à vrai, et voilà ! J'ai mis à jour mon profil D&B.

Retour à Apple Dev —> essayons à nouveau. Enregistrer mon entreprise...

« Erreur : Les informations que vous avez entrées ne correspondent pas à votre profil D&B. »

VOUS ÊTES EN TRAIN DE ME FAIRE UNE BLOQUE.

Parler à Apple à nouveau. « Oh, cela peut prendre 24 à 48 heures pour que les informations D&B mises à jour arrivent dans notre système. »

Vous savez, parce que les informations numériques peuvent prendre 2 jours pour voyager du serveur A au serveur B. Soupir.

Deux jours plus tard, j'essaie de m'enregistrer... finalement ça marche ! Maintenant, je suis dans le programme Apple Developer et je peux soumettre des applications pour examen.

**Gagnant** : Google et Microsoft ; les deux ont pris tout au plus 5 minutes pour s'enregistrer.

**Perdant** : L'enregistrement Apple Developer était lent et douloureux. Il a fallu environ une semaine pour s'enregistrer réellement avec leur programme de développeurs. Il a fallu que je contacte le support de 2 entreprises différentes. Et il a fallu que je _débogue le code JavaScript sur un site web tiers_ juste pour pouvoir passer leur validation côté client boguée, afin que mes informations soient transmises à Apple, afin que je puisse soumettre mon application au magasin. Wow, juste... wow.

S'il y a une grâce salvatrice ici pour Apple, c'est qu'ils ont un programme pour les organisations à but non lucratif 501c3, où les organisations à but non lucratif peuvent se faire dispenser des frais annuels de 99 $. J'en ai profité. Et peut-être que cette étape supplémentaire a compliqué les choses.

### Emballage, construction et soumission de l'application

Une fois que vous avez une application web, vous devez effectuer une sorte de magie pour la transformer en quelque chose que vous pouvez soumettre pour examen dans l'App Store.

* **Apple** : Tout d'abord, achetez un Mac ; vous ne pouvez pas construire une application iOS sans un Mac. Installez XCode et ces outils de construction et frameworks, acquérez un certificat de notre programme de développeurs, créez un profil sur un site séparé appelé iTunes Connect, liez-le avec le certificat que vous avez généré sur le centre de développeurs Apple, puis soumettez en utilisant XCode. Simple comme un, deux, trois... trente-sept...
* **Google** : Téléchargez Android Studio, générez un certificat de sécurité à travers celui-ci, puis emballez-le en utilisant le Studio. Téléchargez le package sur le site Android Developer.
* **Microsoft** : Générez un package .appx en utilisant ces outils de ligne de commande gratuits, ou Visual Studio. Téléchargez sur le site Microsoft Dev Center.

La bonne nouvelle est, **il existe un outil gratuit pour faire la magie de transformer votre application web en packages d'applications**. Cet outil gratuit génial s'appelle [PWABuilder](https://www.pwabuilder.com/). Il analyse une URL, vous dit ce que vous devez faire (par exemple, peut-être ajouter quelques icônes d'écran d'accueil à votre manifeste web PWA). Et en 3 étapes d'assistant, il vous permet de télécharger des packages qui contiennent toute la magie :

* Pour Windows, il génère réellement le package .appx. Vous pouvez littéralement prendre cela et le soumettre sur le site Windows Dev Center.
* Pour Google, il génère une application Java wrapper qui contient votre application web PWA. À partir d'Android Studio, vous construisez ce projet, ce qui génère le package Android qui peut être téléchargé sur le site Android Dev Center.
* Pour Apple, il génère un projet XCode qui peut être construit avec XCode. Ce qui nécessite un Mac.

Une fois de plus, Apple a été le plus douloureux de tous. Je n'ai pas de Mac. Mais vous ne pouvez pas construire le projet XCode pour votre PWA sans un Mac.

Je ne veux pas payer plusieurs milliers de dollars pour publier mon application gratuite dans le magasin d'applications d'Apple. Je ne veux pas payer pour le privilège d'enrichir la plateforme iOS d'Apple.

Heureusement, [MacInCloud](http://macincloud.com/) coûte environ 25 $/mois, et ils vous donnent une machine Mac avec XCode déjà installé. Vous pouvez vous y connecter à distance en utilisant Windows Remote Desktop, ou même via une interface web.

Ce n'était pas suffisant de simplement construire le projet XCode et de le soumettre. J'ai dû générer un certificat de sécurité sur le site Apple Developer, puis créer un nouveau profil d'application sur un site séparé, iTunes Connect, où vous soumettez réellement le package.

Et ce n'était pas tout : puisque Apple est hostile aux applications web, j'ai dû installer des frameworks spéciaux et ajouter des plugins Cordova qui permettent à mon application de faire des choses comme jouer de l'audio en arrière-plan, ajouter la chanson actuelle à l'écran de verrouillage, contrôler le volume de la chanson et le statut de lecture depuis l'écran de verrouillage, et plus encore.

Cela a pris au moins une semaine de bidouillage pour faire fonctionner mon application avant de pouvoir la soumettre au magasin d'applications.

**Gagnant** : Microsoft. Imaginez ceci : vous pouvez aller sur un site web qui génère un package d'application pour votre application web. Et si ce n'est pas votre truc, vous pouvez télécharger des outils de ligne de commande qui feront le travail. Personne de l'interface graphique ? Le Visual Studio gratuit fonctionnera.

**Deuxième** : Google. Nécessite Android Studio, mais il est gratuit, fonctionne pour tout le monde, et était suffisamment simple.

**Perdant** : Apple. Je ne devrais pas avoir à acheter un ordinateur propriétaire — un Mac de plusieurs milliers de dollars — afin de construire mon application. L'enchevêtrement du centre de développeurs Apple -> iTunes Connect semble être une tentative d'un manager déconnecté de pousser iTunes sur les développeurs. Cela devrait simplement faire partie du site du centre de développeurs Apple.

### Test de l'application

Une fois que vous avez enfin fait toutes les incantations magiques pour transformer votre application web existante en un package d'application mobile, vous voulez probablement l'envoyer aux testeurs avant de publier votre application sur les masses non lavées.

* **Apple** : Pour les tests, vous faites installer Test Flight sur l'appareil iOS de vos testeurs. Ensuite, vous ajoutez l'email du testeur dans iTunes Connect. Le testeur recevra une notification et pourra tester votre application avant qu'elle ne soit disponible dans le magasin d'applications.
* **Google** : Dans le centre de développement Android, vous ajoutez les adresses email des testeurs. Une fois ajoutées, ils peuvent voir votre version alpha/bêta dans l'App Store.
* **Microsoft** : Je ne l'ai pas réellement utilisé, donc je ne commenterai pas.

**Gagnant** : Match nul. L'application Test Flight d'Apple est simple et rationalisée. Vous pouvez contrôler l'expiration alpha/bêta simplement du côté administrateur. Google n'était pas loin derrière ; c'était assez indolore, ne nécessitant même pas une application séparée.

### Examen de l'application

Une fois que votre application est prête pour le grand public, vous soumettez votre application pour examen. L'examen est effectué à l'aide d'une liste de contrôle programmatique (par exemple, avez-vous une icône de lancement ?) et par de vraies personnes (« votre application est un clone de X, nous la rejetons »)

* **Apple** : Avant la soumission, XCode vous avertit des problèmes potentiels pendant la construction. L'examen de l'application par un humain prend environ 24 à 48 heures.
* **Google** : Il y a quelqu'un ? Android Studio ne m'a pas informé de problèmes potentiels, et mon application a été approuvée en quelques minutes après la soumission. Je ne pense pas qu'un être humain ait réellement regardé mon application.
* **Microsoft** : Lors de la soumission, un examen programmatique rapide a détecté un problème concernant les mauvais formats d'icônes. Après avoir réussi, un humain a examiné mon application en 4 jours.

**Gagnant** : Apple.

Bien sûr, en tant que développeur, j'aime le fait que mon application était instantanément dans le Google Play store. Mais c'est seulement parce que, je suppose, elle n'a pas réellement été examinée par un humain.

Apple avait le temps de réponse le plus rapide pour un examen humain réel. Les mises à jour ont également passé l'examen en 24 heures.

Microsoft était irrégulier ici. L'examen initial a pris 3 ou 4 jours. Une mise à jour ultérieure a pris 24 heures. Ensuite, une autre mise à jour, où j'ai ajouté la plateforme XBox, a pris encore 3 à 4 jours.

### Conclusion

C'est douloureux et coûteux de prendre un PWA existant et de le rendre fonctionnel sur les plateformes mobiles et de le lister dans l'App Store.

**Gagnant** : Google. Ils ont rendu cela le plus facile pour entrer dans le magasin d'applications. Ils ont rendu cela le plus facile pour s'intégrer à la plateforme native, en tentant de standardiser les API web que les plateformes OS peuvent détecter (bonjour, le magnifique navigator.mediaSession)

**Deuxième** : Microsoft. Ils ont rendu cela le plus facile pour saupoudrer votre application web de magie, la transformant en un package qui peut être soumis à leur magasin. (Cela peut être fait gratuitement en utilisant le site [PWABuilder](http://pwabuilder.com/) !) L'intégration à leur plateforme signifie utiliser l'espace de noms JavaScript window.Windows.* auto-injecté. Pas mal.

**Perdant** : Apple. Ne me forcez pas à acheter un Mac pour construire une application iOS. Ne me forcez pas à utiliser des wrappers natifs pour m'intégrer à votre plateforme. Ne me forcez pas à bidouiller avec des certificats de sécurité ; laissez vos outils de construction les créer pour moi, et les stocker automatiquement dans mon compte Dev Center. Ne me forcez pas à utiliser 2 sites différents : Apple Dev Center et iTunes Connect.

Dernières réflexions : Le web gagne toujours. Il a vaincu Flash. Il a tué Silverlight. Il a détruit les applications natives sur le bureau. Le navigateur est la plateforme cliente riche. L'OS est simplement un lanceur de navigateur et un communicateur matériel.

Le web gagnera aussi sur le mobile. Les développeurs ne veulent pas construire 3 applications séparées pour les principales plateformes. Les entreprises ne veulent pas payer pour le développement de 3 applications.

La réponse à tout cela est le web. Nous pouvons construire des applications web riches — des Progressive Web Apps — et les emballer pour tous les magasins d'applications.

Apple en particulier a un incitatif pervers à arrêter le progrès du web. C'est le même incitatif que Microsoft avait à la fin des années 90 et au début des années 2000 : il veut être _la_ plateforme pour les bonnes applications. Les PWA sapent cela ; elles fonctionnent partout.

Ma sagesse logicielle est la suivante : les PWA finiront par gagner et dépasser les applications mobiles natives. Dans 5 à 10 ans, les applications iOS natives seront aussi courantes que les applications Win32 C. Apple ira en traînant les pieds, en gardant iOS Safari à la traîne, en bloquant le progrès des PWA là où ils le peuvent. (Même leur récent « support » des PWA dans iOS Safari 11.1 [handicapent réellement les PWA](https://news.ycombinator.com/item?id=16826852).)

Ma suggestion aux plateformes d'applications mobiles est d'accepter l'inévitable et soit d'ajouter automatiquement des PWA de qualité à votre magasin d'applications, soit de permettre aux développeurs de soumettre facilement (par exemple, gratuitement, et en 3 clics ou moins) un PWA à votre magasin.

Lecteurs, j'espère que cela a été un aperçu utile des PWA dans les App Stores en 2018.

Avez-vous soumis un PWA à un magasin d'applications ? J'adorerais entendre votre expérience dans la section des commentaires. Et vous pouvez lire plus de mes articles de blog [sur mon blog](http://debuggerdotbreak.judahgabriel.com).