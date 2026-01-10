---
title: 'Seoul Bike : Comment j''ai redessiné le système de vélos en libre-service
  de la ville de Séoul'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-14T11:44:17.000Z'
originalURL: https://freecodecamp.org/news/seoul-bike-case-study-6ac4172f7188
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ks-DGwKBq0Sm847-Xlmp2w.jpeg
tags:
- name: Design
  slug: design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Travel
  slug: travel
- name: UX
  slug: ux
seo_title: 'Seoul Bike : Comment j''ai redessiné le système de vélos en libre-service
  de la ville de Séoul'
seo_desc: 'By Martin Totev

  Frustration with the current app drove me to create my first UX case study.

  As a beginner in UX design, a great way to learn something new is through practice.
  This case study was an amazing opportunity to start my journey. With this ...'
---

Par Martin Totev

#### La frustration suscitée par l'application actuelle m'a poussé à créer ma première étude de cas UX.

En tant que débutant en design UX, la pratique est un excellent moyen d'apprendre. Cette étude de cas était une occasion incroyable de commencer mon parcours. Avec cet objectif en tête, j'ai contacté un ancien de mon université ayant une grande expérience professionnelle dans le domaine et je lui ai demandé son aide et son mentorat.

Nous nous sommes rencontrés un dimanche dans un café quelque part à Séoul et avons commencé à travailler. J'ai apporté mon vieil ordinateur portable Samsung (finalement remplacé par un Macbook) et un petit carnet à notre première rencontre.

Pendant quelques semaines, j'ai esquissé et dessiné, essayant de comprendre l'application et la manière dont le service était conçu. J'ai trouvé des problèmes provenant du service lui-même, d'autres du design de l'application. Mais ne nous éloignons pas du sujet de cet article.

### Qu'est-ce que « Seoul Bike » ?

![Image](https://cdn-media-1.freecodecamp.org/images/hT9fXlALI-2P8628qTLrMdU2YtFfqPBPvJKz)
_1ère génération (à gauche) et 2ème génération de Seoul Bike (à droite), un [cadeau de l'ambassade des Pays-Bas à la ville de Séoul](https://www.dutchcycling.nl/news/140-dutch-prime-minister-donates-bikes-to-seoul" rel="noopener" target="_blank" title=")._

[Seoul Bike](https://www.bikeseoul.com/) (ou 따릉이 Ttareungi) est un système de location de vélos automatisé. Comme l'indique le titre en coréen — 서울자전거 따릉이 — 무인대여시스템, c'est un système de vélos publics très bon marché couvrant Séoul. La couverture du système et la possibilité de rendre un vélo à un endroit différent de celui où vous l'avez loué constituent son plus grand avantage par rapport à la concurrence. Seoul Bike connaît actuellement une base d'utilisateurs en pleine croissance.

Il existe 3 générations de vélos qui se ressemblent beaucoup et sont très difficiles à distinguer. Ils sont généralement offerts par de grandes entreprises, mais les informations sur qui a fait un don et combien ont été donnés n'ont pas été mises à jour depuis un certain temps. Samsung a fait don de 3 000 vélos et a installé 300 supports l'année dernière. Certains vélos sont offerts par Naver, Kakao, Woori Bank, et même l'ambassade des Pays-Bas.

Le vélo est assez simple. Il possède 3 vitesses et un siège rétractable spécialement conçu pour ne s'adapter qu'à ces vélos — le vol de selles de vélo est toujours une réalité pour une raison quelconque. Il y a une interface utilisateur à écran tactile avec un seul bouton et un haut-parleur. Il y a aussi un mécanisme de verrouillage pour attacher le vélo à un support Seoul Bike, ou le verrouiller temporairement à un poteau lorsque vous devez le laisser un moment. Au milieu d'un trajet, vous pouvez vérifier depuis combien de temps vous utilisez le vélo, la distance parcourue et le nombre de calories brûlées.

![Image](https://cdn-media-1.freecodecamp.org/images/LJ6cPxZ-eT8Okqgj8w4r5KP9qkKOp769FIKF)
_Interface à écran tactile sur le vélo._

Le service utilise des « _tickets_ » multi-usages qui expirent après un certain temps. Ces « _tickets_ » sont divisés en tickets de courte durée et de longue durée. Un ticket de courte durée est un ticket d'une seule journée qui coûte _1 000 wons_ et expire 24 heures après l'achat. Les tickets de longue durée incluent _7 jours (3 000 wons)_, _30 jours (5 000 wons)_, _180 jours (15 000 wons)_ et _365 jours (30 000 wons)_.

Pour éviter l'accaparement des vélos, la durée par défaut pendant laquelle un utilisateur est autorisé à louer est d'une heure (ticket normal) ou de deux heures (ticket premium). Si vous dépassez une heure (ou deux heures pour le ticket premium), il y a une pénalité de 1 000 wons pour chaque heure supplémentaire. Et lors du retour du vélo, l'utilisateur doit d'abord payer sa pénalité avant de pouvoir louer à nouveau. Ce système de prévention de l'accaparement est assez efficace.

Comme je l'ai mentionné, un ticket est multi-usage — un utilisateur peut donc toujours ramener un vélo à un support et le louer à nouveau. Ainsi, l'accaparement des vélos est toujours possible, tant qu'il y a un support à proximité et que vous avez envie de faire des allers-retours.

![Image](https://cdn-media-1.freecodecamp.org/images/6n7qUIPTRsqjPKsMg3qnajaQu7OjEwfW2P9T)
_Ligne continue : dans l'application ; Ligne pointillée : interface sur le vélo._

Le processus de location se fait uniquement via une application mobile qui, jusqu'à récemment, n'était disponible que sur Android. Et c'est là qu'apparaissent de nombreux problèmes — l'application est trop compliquée, et tout le flux utilisateur est bancal, truffé d'éléments mal placés. Par exemple, pourquoi y a-t-il un bouton de retour sur l'écran principal ? Retourner où ? Et pourquoi l'application manque-t-elle de notifications et d'informations essentielles ?

![Image](https://cdn-media-1.freecodecamp.org/images/jynQ4XvmZSvsyl8Zo0Zcv1C1q5GHmHsgDKy8)
_Le premier écran que vous voyez en ouvrant l'application._

Commençons par la page principale. La page qui vous accueille lors du premier lancement de l'application est assez basique. Vous avez un _bouton de connexion_, un _bouton Station_ qui vous mène à la carte indiquant l'emplacement des supports et le nombre de vélos disponibles. La location n'est pas possible depuis cette page. Ensuite, il y a un _bouton d'achat de ticket_ et un _bouton Ma Page_ qui contient des informations sur vos trajets. Il y a aussi un _bouton Centre d'appel_ pour les cas où vous avez besoin d'aide.

Une chose que vous avez peut-être remarquée est le _bouton de retour_ en haut à gauche de l'écran. Un bouton qui ne mène nulle part. Et un _bouton de menu hamburger_ sur la droite qui force le menu à surgir du côté gauche de l'écran. Pourquoi ?

### Connexion

Le design actuel exige qu'un utilisateur se connecte pour accéder au service. Il existe une option pour mémoriser votre nom d'utilisateur et votre mot de passe. Mais lors de la fermeture de l'application, l'utilisateur est déconnecté, créant cette étape obligatoire de _Page de connexion_ — ce qui peut être fastidieux, surtout si vous êtes pressé. L'écran de connexion devrait être une expérience unique pour une application mobile. Après tout, un téléphone mobile est un appareil personnel qui est rarement laissé sans surveillance.

L'application elle-même ne stocke pas d'informations de carte de crédit ou d'autres données sensibles devant être protégées par une déconnexion automatique obligatoire. Avec l'expérience redessinée, ces données sensibles seront protégées par une demande de mot de passe. Cela ajoutera une couche de protection supplémentaire contre les tiers indésirables.

![Image](https://cdn-media-1.freecodecamp.org/images/w7apQRcBKyYJspSXig2bworfoyf-3XtsWQW9)
_Une fois connecté sur un appareil, le profil est stocké dans l'appareil (ex: Facebook, Daum, Twitter etc.)_

### Écran principal

**Seoul Bike** est un service qui propose la location de véhicules de transport. Par conséquent, la première chose qu'un utilisateur devrait voir est une carte avec les emplacements autour de lui où il pourrait louer. D'un seul coup d'œil à l'écran, l'utilisateur devrait voir le support actuellement sélectionné et les autres supports à proximité. Ceux disponibles et indisponibles devraient être facilement distinguables. Les applications de location de voitures comme [**_Socar_**](https://www.socar.kr/) et [**_Green Car_**](http://www.greencar.co.kr/) montrent à l'utilisateur une carte avec les emplacements proches.

Un problème majeur que j'ai remarqué en utilisant le service pendant une année entière est qu'un certain nombre d'utilisateurs ont tendance à louer un vélo qui est trop loin d'eux. Cela empêche les personnes présentes au support d'utiliser le service. Actuellement, si vous louez un vélo et ne le déverrouillez pas du support dans les 5 minutes, la location est automatiquement annulée. Pour une balade de loisir, attendre 5 minutes n'est pas un si gros problème (bien que personne n'aime attendre dans notre mode de vie actuel effréné). Mais pour quelqu'un qui commence son trajet matinal pour aller au travail, attendre 5 minutes n'est pas une option.

Pour éviter de tels incidents, j'ai conçu le service pour utiliser la géolocalisation des appareils mobiles. Cela permettra de vérifier si l'utilisateur se trouve à moins de 100 mètres du support où il compte louer. Un GPS normal dans un appareil mobile moderne a une précision d'environ 50 mètres — et 100 mètres est, à mon avis, une distance plus sûre pour un GPS. Une distance de 100 mètres signifie que l'utilisateur peut voir le support si rien n'est dans le chemin, et n'a besoin que de quelques secondes pour s'en approcher.

Les données GPS pourraient être utilisées pour améliorer le service en analysant comment les utilisateurs se déplacent avec les vélos, quels sont les pics d'utilisation et quelles zones doivent être gérées à quels moments. Actuellement, de telles données n'existent pas et ne sont pas analysées, et certaines zones où les vélos font partie du trajet matinal ne sont pas gérées correctement.

Ces données pourraient être une excellente source d'information pour le gouvernement municipal lui-même. Elles pourraient s'avérer essentielles pour une ville en constante croissance confrontée à des problèmes de surpopulation et de trafic. Un réseau de vélos abordable et fiable pourrait soulager les autres moyens de transport public, un point sur lequel la ville de Séoul doit se concentrer.

![Image](https://cdn-media-1.freecodecamp.org/images/OwuqSpG6fCPCvshTqtACJmgLd8Hqnc3Qpt18)
_L'écran principal contient d'autres options de location en un seul clic._

Il existe des options manuelles actuellement utilisées dans l'application, telles que la recherche manuelle et le scan de code QR. Elles sont très utiles en cas d'erreur GPS ou si la localisation de l'utilisateur est indisponible. L'utilisateur peut toujours rechercher un support par son numéro unique ou son nom, ou scanner un code QR attaché au support pour utiliser le service. Ces modes sont commutés d'une simple pression sur la barre supérieure. L'écran de recherche contient également vos lieux favoris personnalisés par l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1sqUz9g9w7iaflCXgEw-yMnNv9JlVeAAT4gy)

### Notifications

Habituellement, quand je suis pressé, j'ai une surprise très indésirable de temps en temps. Un message « Vous n'avez pas de ticket, achetez-en un d'abord et réessayez » sort du haut-parleur fixé sur le vélo. Parfois, quand j'ai le plus besoin d'un vélo, il n'y en a aucun au support près de chez moi. Ce n'est pas une surprise que j'apprécie, mais c'est une surprise quand même.

Pour prévenir de tels incidents, certaines informations essentielles devraient être affichées via des notifications push non intrusives. Par exemple — le nombre actuel de vélos à un support favori, le temps restant de votre trajet actuel, et l'expiration imminente d'un ticket. L'utilisateur est invité à sélectionner une certaine plage horaire pour que les fonctionnalités fonctionnent. Cela est nécessaire pour réduire la charge sur les serveurs due aux demandes de mise à jour constantes et à l'utilisation des données mobiles.

Imaginons une personne nommée Zoe. Zoe vit dans une zone où il n'y a pas de bus direct pour la station de métro où elle se rend quotidiennement. La distance à pied est d'environ 14 minutes, mais avec un Seoul Bike, elle peut y être en 5 minutes. Avec la popularité croissante des vélos, elle est souvent obligée de marcher précipitamment parce qu'il n'y a pas de vélos sur le support.

Grâce à cette fonctionnalité, elle ajoute le support de vélos le plus proche à ses favoris. Ensuite, dans les paramètres de l'application, elle active les _notifications_ pour l'_état du support._ De 08h00 à 08h20, elle reçoit des mises à jour sur le nombre de vélos disponibles. Cela l'aidera à planifier à l'avance si elle doit marcher jusqu'à la station de métro et partir un peu plus tôt.

![Image](https://cdn-media-1.freecodecamp.org/images/ehUUsnlkJVCSRjfCubioYMbmeZIIyFasPaVa)

### Menu Hamburger

Le menu « hamburger » est comme la carte de l'application, il emmène une personne d'un point A à un point B avec facilité. En regroupant les fonctionnalités, l'utilisateur peut facilement mémoriser leurs emplacements sur l'écran. En tant que carrefour central de l'application, il peut être utilisé pour informer l'utilisateur d'informations essentielles.

L'un des aspects les plus inconfortables de l'application actuelle est la difficulté de trouver combien de temps il reste sur votre ticket actuel. C'est quelque chose qui devrait être affiché dans un emplacement intermédiaire, qui accompagne l'utilisateur du point A au point B de l'application. Dans mon design, cet emplacement est le menu « Hamburger » sur le côté. Il inclut des informations en temps réel sur le statut du ticket actuel et n'oblige pas l'utilisateur à entrer dans une page spéciale pour le consulter.

![Image](https://cdn-media-1.freecodecamp.org/images/a4hAjEMvjZvdYB7stEgEje2IaiSfOIcgLlM-)
_Prise en charge de la langue anglaise pour les visiteurs étrangers et les expatriés qui ne parlent pas coréen._

### Paiement

Un autre aspect frustrant de l'application est l'étape du paiement du ticket. La Corée, et particulièrement les services en ligne gérés par le gouvernement, sont obsédés par la sécurité. La plupart d'entre eux utilisent un processus de paiement exaspérant. Il y a Active X, l'authentification par téléphone mobile (parfois plusieurs fois) et une tonne d'autres étapes, juste pour dépenser 5 000 wons pour quelque chose.

Je ne compte plus les fois où j'ai renoncé à acheter quelque chose en ligne parce que l'étape du paiement m'avait laissé sans voix. Un processus de paiement doit être sécurisé mais rapide, c'est pourquoi les pages d'« Achat de Ticket » nécessitaient un nouveau modèle. [**_Kakao Pay_**](http://www.kakao.com/kakaopay/) ou [**_Naver Pay_**](http://www.kakao.com/kakaopay/) sont de brillants services de paiement conçus pour être simples et rapides, et cette application en a besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/Cl0i3H2vohSk-J4UyfiAB38X50LRfOK94IDY)
_Moins de complications était l'objectif principal lors de la conception de cette page._

Avec la collaboration de [**_Kakao Pay_**](http://www.kakao.com/kakaopay/) ou [**_Naver Pay_**](http://www.kakao.com/kakaopay/), tout le processus de paiement pourrait être considérablement simplifié. Cela deviendrait une expérience plus agréable, au lieu d'une expérience intimidante qui fait fuir les utilisateurs, et qui parfois ne permet pas du tout aux étrangers de payer. Pour être honnête, cela s'est amélioré, mais il y a encore des limitations.

### Signalement de problème

Entretenir un parc de vélos en pleine croissance nécessiterait une main-d'œuvre très importante qui pourrait dépasser le budget d'un gouvernement local. Au lieu d'une main-d'œuvre massive, les vélos problématiques pourraient être signalés par les utilisateurs.

Actuellement, l'application ne dispose que d'un centre d'appel où vous pouvez demander de l'aide ou signaler un problème avec votre vélo ou tout autre vélo. En raison de l'échelle du service et de la manière dont il est construit, il n'y a aucun moyen de savoir quand le vélo est tombé en panne. Si un vélo tombe en panne pendant que je l'utilise, je pourrais simplement le ramener à un support et le laisser cassé. L'utilisateur suivant pourrait le signaler, mais il n'y a aucun avantage à se donner la peine de le faire. Concevoir un système basé sur des récompenses est ce dont Seoul Bike a besoin.

Malheureusement, je n'ai pas pu trouver de statistiques d'utilisation. Mais le service a une base d'utilisateurs toujours croissante, et j'ai remarqué beaucoup plus de vélos problématiques lors de mes trajets quotidiens.

![Image](https://cdn-media-1.freecodecamp.org/images/qEFpl7yEDlfcTeU8vECr4gJA3O-lXs0rBvmP)

La catégorisation des problèmes les plus fréquents simplifie la page. Non seulement c'est facile pour l'utilisateur final, mais c'est aussi plus facile à enregistrer et pour les ingénieurs de prioriser les tâches. Sous chaque catégorie majeure, il y a des options plus détaillées à portée de main, comme un pneu crevé, une roue voilée ou des rayons cassés, etc. Si le problème ne fait pas partie de ces catégories ou s'il y a quelque chose de supplémentaire que vous voulez expliquer aux ingénieurs, il y a une option de message sous l'onglet « Autre ».

### P.S. Pourquoi passer du vert au bleu et au rouge ?

![Image](https://cdn-media-1.freecodecamp.org/images/Ycl7MYEo4tFhrFtsWTmlxAl9bTkdI9JBF8m4)
_I will Seoul You !_

La ville de Séoul a procédé à un [rebranding](https://brandinginasia.com/i-seoul-you-the-confusing-new-slogan-for-seoul/) très controversé l'année dernière. Mais il y a un manque d'unification entre les services fournis par la municipalité et l'image de marque. Je comprends pourquoi la couleur actuelle de l'application et du logo est le vert — vélo = écologique, écologique = vert. Je pense que nous devrions arrêter de surutiliser la couleur verte dès que quelque chose est étiqueté comme écologique.

Séoul a investi beaucoup d'argent pour redorer son image, et il doit y avoir une cohérence dans l'image de marque de ses services. J'ai donc choisi d'utiliser une dérivation des deux couleurs utilisées dans « **I** •**SEOUL** • **U** ». Un bleu et un rouge légèrement modifiés par rapport à la marque de la ville créent un joli contraste — avec le blanc, le noir et presque toutes les nuances de gris. Ainsi, il devient plus facile de créer une hiérarchie avec les couleurs, même pour les personnes daltoniennes.

L'utilisabilité était mon objectif principal, et ces deux couleurs étaient les mieux adaptées à ce design tout en maintenant la cohérence avec la marque Séoul.

![Image](https://cdn-media-1.freecodecamp.org/images/Dl8sRVv7UTAHq5sJOXMRbP2-tyfNoc94HQbS)
_Le logo qui a mis le feu à la communauté coréenne du design._

![Image](https://cdn-media-1.freecodecamp.org/images/Syo3i-BU7dLHt0ZhCDKbBAcoKVsnaMRtoj4f)
_La cohérence de la marque est quelque chose qui devrait être imposé à travers tous les services de la ville de Séoul._

### Kit UI gratuit

Après avoir travaillé sur ce projet pendant mon temps libre, j'ai été inspiré par deux personnes pour publier le fichier sous forme de kit UI. D'autres personnes peuvent maintenant utiliser ces ressources pour leurs propres designs. L'une des personnes qui m'a inspiré est un ami d'université, qui a travaillé pendant 2 ans à la création d'une police coréenne (Busan Bada/부산바다체) et l'a publiée gratuitement.

Une autre inspiration a été la créatrice d'[_Open Color_](https://yeun.github.io/open-color/) et son interview dans le [_podcast Design Table_](http://itun.es/kr/i6TOib.c) (langue : coréen). Ses vues sur les projets Open Source étaient vraiment inspirantes.

De plus, il y a quelques semaines, l'équipe de Bohemian Coding a sorti Sketch v47 et la fonction _Libraries_ — qui porte les symboles à un tout autre niveau. En partageant mon fichier Sketch avec le monde, j'espère pouvoir aider quelqu'un avec certains des éléments que j'ai créés.

Ce projet a été conçu pour un appareil Android, donc toutes les ressources sont inspirées du Material Design de Google. Mais à l'avenir, je prévois de mettre à jour le fichier avec un design centré sur iOS (je ne peux pas promettre que ce sera fait !). Les symboles et les boutons que j'ai assemblés sont libres d'utilisation. N'hésitez donc pas à les inclure dans vos Sketch Libraries !

### Téléchargez le kit UI gratuit [ici](https://martintotev.github.io/uikit.html).

Pour des aperçus de certains des symboles du fichier, cliquez [ici](https://www.dropbox.com/sh/ttw5sz8nkr4cwol/AADZWctUBhCCRQ84S8VowrkAa?dl=0).

Ce kit UI est gratuit pour un usage personnel et commercial. Si vous utilisez ce kit dans le cadre de votre travail, une mention est grandement appréciée.

**Le design de l'interface lui-même est protégé par le droit d'auteur, veuillez donc ne pas le télécharger sur Dribble ou Behance en prétendant qu'il est le vôtre. Ce ne serait vraiment pas cool. Genre, vraaaaiment pas cool...**

### Santé et continuez à créer !

Vous pouvez me trouver sur [martintotev.github.io](http://martintotev.github.io), me suivre sur Twitter [@martintotevUX](https://twitter.com/martintotev89) ou m'envoyer un e-mail à martintotev89@gmail.com

Un merci spécial à _Sang Hyeon Park_ pour être devenu mon mentor et m'avoir guidé dans le design UX.