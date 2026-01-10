---
title: Mettre le M dans MVP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-31T19:22:06.000Z'
originalURL: https://freecodecamp.org/news/putting-the-m-in-mvp-71e036034ed9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zRZ0I0E2sj9xSYRG95An9Q.jpeg
tags:
- name: business
  slug: business
- name: lean startup
  slug: lean-startup
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Mettre le M dans MVP
seo_desc: 'By Howard Lo

  Years ago, I thought I knew what my minimum viable product (MVP) was. But I was
  wrong, and ended up building way too much.

  Months ago, I thought I knew what my MVP was. But I was still wrong, and ended up
  building too much, but not as mu...'
---

Par Howard Lo

Il y a des années, je pensais savoir ce qu'était mon produit minimum viable (MVP). Mais je me trompais, et j'ai fini par construire bien trop.

Il y a des mois, je pensais savoir ce qu'était mon MVP. Mais je me trompais encore, et j'ai fini par construire trop, mais pas autant qu'avant.

Avec la pratique de la construction de produits, l'estimation de la "viabilité" devient plus facile. Mais vous devez rester vigilant. Sinon, vous disparaitrez dans votre ordinateur portable pendant plusieurs mois, pour émerger avec un produit que personne ne veut.

### **_Quel est le minimum absolu ?_**

Le ciel est la limite en développement. Vous pouvez coder comme un fou. Vous pouvez finir avec le bouton le plus joli et le plus animé du monde. Le piège est que cela semble être un effort valable sur le moment, parce que vous mettez du travail et voyez des résultats.

Mais il y a un concept important appelé rendements marginaux décroissants. À un moment donné, le travail que vous mettez n'aura pas assez d'impact pour compter.

Si vous allez assez loin, le travail que vous mettez n'aura aucun impact. Et si vous n'êtes pas prudent, vous ne remarquerez pas que l'aiguille ne bouge pas jusqu'à ce que vous ayez dépensé beaucoup d'efforts.

Alors, lorsque vous construisez votre startup — ou ajoutez une fonctionnalité majeure à votre startup — comment allez-vous savoir quand arrêter ? À quel moment réaliserez-vous que vous êtes allé trop loin ?

Pour commencer, vous devriez avoir une idée générale de ce que vous pensez être nécessaire et de ce qui ne l'est pas. Vous pouvez organiser ces éléments en deux listes mentales : les incontournables et les agréments.

Une fois que vous avez satisfait votre liste des incontournables, c'est là que vous arrêtez, et voilà, MVP atteint.

> Si vous n'êtes pas gêné par la première version de votre produit, vous l'avez lancé trop tard. — Reid Hoffman

Peu importe à quel point vous avez essayé, vous avez probablement passé trop de temps à travailler sur votre MVP avant de le publier.

Mais combien de temps est trop long ? Je souhaiterais pouvoir vous le dire. Le mieux que je puisse faire est : c'est trop long jusqu'à ce que ce soit trop court.

Bien que je ne puisse pas vous donner une réponse directe, je peux vous dire ce que j'ai appris lors de ma création la plus récente, [Rabbut](https://rabbut.com), qui facilite la création d'une liste de diffusion sur des sites comme Medium.

Après avoir lancé Rabbut, il est devenu évident ce dont nous avions besoin par rapport à ce dont nous n'avions pas besoin. Prenez ce que vous pouvez de l'histoire de Rabbut — je ne fais que transmettre cela en exemple dans l'espoir que cela vous fera réfléchir aux fonctionnalités dont votre MVP peut se passer.

### Ce dont nous n'avions pas besoin :

#### Une interface de mot de passe oublié.

Puisque nous avons des comptes utilisateurs avec des mots de passe, il est raisonnable de penser qu'un jour quelqu'un oubliera son mot de passe (moi y compris). Cela faisait partie de la liste des choses qui devaient absolument être faites, car les gens se fâcheront s'ils ne peuvent pas accéder à leur tableau de bord.

Cela n'a pas été construit simplement parce que je n'ai pas réussi à comprendre comment le configurer. Désolé, premiers utilisateurs !

Rabbut n'avait pas de réinitialisation de mot de passe. Pas même pour les administrateurs — personne dans l'entreprise ne pouvait réinitialiser un mot de passe.

Pour empêcher les gens de se déconnecter lorsqu'ils ferment le navigateur, j'ai réglé les cookies pour qu'ils expirent après un an et j'ai supprimé le bouton "se déconnecter". Je devais gagner autant de temps que possible.

Qu'est-il arrivé ? Rien.

Personne n'a oublié son mot de passe pendant 5 mois. Certes, le premier mois n'a pas vu un afflux massif de nouveaux utilisateurs, mais une fonctionnalité qui n'a été utilisée qu'après 5 mois tombe définitivement dans la liste des "pas besoin pour l'instant".

À la marque des 5 mois, un pauvre vieil homme a écrit pour dire qu'il avait oublié son mot de passe et ne savait pas comment accéder à son tableau de bord. Je me suis excusé, lui ai dit que c'était un bug (haha), lui ai demandé de nous donner quelques jours, et j'ai corrigé le site en direct avec un processus de réinitialisation de mot de passe très années 1990.

Vous pouvez consulter [notre interface de réinitialisation de mot de passe](https://rabbut.com/accounts/password/reset/) pour voir à quel point l'ensemble du processus est non poli (vous devrez créer un compte réel d'abord si vous voulez parcourir le flux de travail). Vous remarquerez peut-être aussi qu'elle ressemble étrangement à toutes les autres parties de notre site, car c'est du code recyclé (plus sur ce point plus tard).

#### Conditions d'utilisation et politique de confidentialité

Qu'il soit connu : je ne suis pas avocat. Qu'il soit également connu : ceci est probablement un mauvais conseil et vous ne devriez pas le suivre.

Qu'il soit enfin connu : Rabbut a survécu sans conditions d'utilisation ni politique de confidentialité (pas de poursuites), et vous le ferez probablement aussi, jusqu'à ce que vous deveniez grand.

La vérité honnête est que presque personne ne lit ces documents, même s'ils disent le faire (bien qu'ils le devraient probablement). Et presque personne ne se souviendra de ce que disent les conditions d'utilisation ou la politique de confidentialité, même s'ils ont pris le temps de les lire.

Alors, qui s'en soucie ?

**Quiz !**

1. Savez-vous où se trouvent les conditions d'utilisation et la politique de confidentialité de Medium.com ?
2. Quel est l'âge minimum pour utiliser Medium.com ?

Nous avons ajouté les conditions d'utilisation et la politique de confidentialité pour Rabbut parce que nous avons eu un coup de froid un jour — pas parce que quelqu'un s'en est plaint. Vous n'avez pas besoin de payer des centaines de dollars à un avocat pour en rédiger une pour votre entreprise sans traction si personne ne sait même que vous existez.

Faites cela plus tard, et en attendant, soyez un bon samaritain et soyez prudent avec les informations privées des autres.

#### Tests

C'est là que tous les développeurs vertueux sortiront leurs croix numériques. Vous n'avez pas écrit une suite de tests complète pour votre code ? À bientôt en enfer.

Les tests exécutent votre code à travers une série de... tests... pour s'assurer que tout nouveau code que vous ajoutez n'a pas tout cassé dans votre projet.

Si je pouvais claquer des doigts et avoir tous mes tests écrits, je claquerais des doigts.

Mais si vous pouvez éviter de passer du temps que vous n'avez pas à écrire des tests dès le début, ne les écrivez pas. Surtout si vous êtes le seul développeur, ou si le projet est assez petit. Parce que si quelque chose casse, vous êtes probablement assez familier avec la petite base de code pour savoir comment la réparer, ou revenir en arrière si nécessaire.

Vous n'avez pas non plus besoin de tests si la direction de votre produit est encore flexible. Le pire dans le pivotement est de jeter l'ancien code. Si vous pivotez, vous jetterez probablement la plupart de vos tests aussi.

Une fois que vous avez de la traction ou une grande équipe de développement, vous pouvez écrire tous les tests que votre cœur désire (ou embaucher un ingénieur de test pour le faire pour vous).

Au début, les choses changent vite. Gardez votre code léger pour qu'il puisse changer tout aussi rapidement.

#### Code évolutif

Si cela vous est égal, écrivez du code évolutif. Si vous êtes bloqué sur quelque chose pendant plus d'une demi-heure parce que vous ne trouvez pas de solution qui supportera 100 000 utilisateurs simultanés, écrivez simplement quelque chose de bidouillé/non évolutif et passez à autre chose.

Je ne suis pas le meilleur développeur du monde. Les choses qui sont faciles pour certains développeurs me prennent beaucoup plus de temps qu'elles ne le devraient. Cela inclut l'écriture de code évolutif.

Oui, j'aimerais avoir du code qui ne tombe pas en panne lorsque je passe de 10 utilisateurs à 10 000 000.

Oui, j'aimerais que les développeurs qui rejoindront mon entreprise plus tard s'émerveillent de ma maîtrise du codage et de ma prévoyance divine.

Mais tout cela nécessite de rechercher et de comprendre les dernières méthodes de développement efficaces. Et puis-je ajouter, votre utilisation des meilleures pratiques ne sera appréciée par personne d'autre que les développeurs de votre projet (et pour l'instant, c'est probablement juste vous).

Et les meilleures pratiques changent souvent, c'est pourquoi la durée de vie des réponses StackOverflow est si courte. Rester à la pointe est une poursuite rude et sans fin.

Là où vous pouvez — si vous pouvez — écrire du code évolutif. Sinon, faites-le fonctionner, livrez-le, puis inquiétez-vous de l'optimiser plus tard.

#### Un serveur de staging

Nous n'avons pas vraiment utilisé un serveur de staging pour les tests jusqu'à ce que nous devions tester les paiements. Et même alors, nous aurions pu les tester sur notre machine locale (ordinateur portable) en utilisant Stripe.

**Astuce pro :** si vous tenez à votre santé mentale, utilisez Stripe pour tous vos paiements.

Les serveurs de staging sont bien, et ils ne prennent pas trop de temps à configurer. Mais si vous êtes encore dans les premières phases de découverte de l'identité de votre produit, ils ne sont pas nécessaires.

La plupart des développeurs se couchent tard et poussent du code bogué pendant les heures mortes de la nuit et testent sur le serveur en direct. Ce n'est pas la fin du monde si cet utilisateur sur votre site à 4 heures du matin a une expérience diminuée à cause d'une poussée boguée.

#### Commencez gratuitement

Ce n'est pas une stratégie marketing ou une stratégie de tarification.

Commencez gratuitement, car il faut du temps pour tout configurer.

Si vous lancez les paiements, vous aurez besoin d'une page de tarification pour dire aux gens ce qu'ils obtiennent en payant par rapport à ne pas payer. Si vous ne le faites pas, vos utilisateurs contacteront le support et votre équipe de support client (probablement aussi vous) vous détestera, ce qui est nul.

Vous devrez également coder les formulaires de paiement et les systèmes de paiement, ce qui est nul.

Vous devrez configurer HTTPS immédiatement, car la plupart des plateformes de paiement ne vous permettront pas d'accepter de l'argent à moins que vous ne soyez sécurisé.

Ensuite, vous aurez probablement besoin d'un compte bancaire d'entreprise. Les banques sont nulles.

Selon le degré de confiance que vous avez en votre équipe, vous devrez peut-être aussi vous incorporer, ou configurer une "entreprise" officielle. L'incorporation est coûteuse, et nulle.

Sans parler du fait que si vous vous trompez quelque part dans les maths ou le code — comme oublier d'ajouter les frais de port — vous pourriez réellement perdre de l'argent sur vos transactions. Cela m'est arrivé, et c'était vraiment nul.

Tout cela est juste du temps supplémentaire dont vous aurez besoin pour lancer.

Les humains sont allés sur la lune en atteignant d'abord l'orbite. Commencez gratuitement.

#### HTTPS

Vous n'avez pas besoin de sécurité au début.

Avant de mettre vos chapeaux d'étain et de crier "et si je me fais pirater !?", rappelez-vous : **vous devez être populaire avant de vous faire pirater**.

La plupart des pirates veulent le meilleur rapport qualité-prix. Pourquoi pirateraient-ils votre projet obscur avec 10 utilisateurs lorsqu'ils peuvent se concentrer sur des endroits qui ont 100 millions d'utilisateurs ?

Vous souvenez-vous du pirate qui a divulgué une tonne d'intimités de célébrités ? Vous êtes-vous déjà demandé pourquoi il ne s'est pas donné la peine de divulguer les vôtres ?

Un autre exemple est Facebook. Ils n'avaient pas HTTPS jusqu'à ce qu'ils se fassent réprimander et obligés par la FTC, [presque une décennie après leur lancement](http://www.darkreading.com/risk-management/facebook-adopts-secure-web-pages-by-default/d/d-id/1107448). À l'époque, ils avaient des informations sensibles de millions de personnes.

Vous ne serez pas dans le pétrin pendant longtemps, mais HTTPS fait que certains de vos utilisateurs se sentent mieux à propos de votre site. Je ne suggère pas de faire comme Facebook et d'attendre une décennie, mais obtenez HTTPS lorsque vous en avez besoin (paiements) ou lorsque vos utilisateurs — ou la FTC — se plaignent trop.

### Ce dont nous avions réellement besoin

"Ce qui constitue un MVP" change d'année en année. Cela dépend des attentes des gens.

Dans les années 90, un site web MVP était probablement juste du texte brut avec une seule publicité pop-up. Aujourd'hui, un MVP doit satisfaire une foule avec des normes plus élevées. Voici donc quelques choses que vous devriez faire, en plus d'éviter les pop-ups :

#### Expérience utilisateur et votre front end

Vous pouvez écrire du code de merde. Votre serveur peut être maintenu par des élastiques et de la gomme à mâcher. Mais vos utilisateurs ne devraient jamais le sentir.

Si votre page web met 20 secondes à charger, corrigez-la. MVP ou non, si cela affecte l'utilisabilité, cela compte.

En matière de MVP, l'UX est l'exception, car les produits "viables" doivent avoir l'air polis, au minimum. Les gens aujourd'hui s'attendent à ce que même les applications bêta soient fonctionnelles et non frustrantes. Blâmez tous ces surdoués qui vous ont précédé.

Gardez votre design simple, pour avoir moins à coder et moins à concevoir. Récemment, le look propre/plat est à la mode, donc cela devrait être facile.

Vous n'avez pas besoin d'animations fantaisistes ou d'œufs de Pâques interactifs, mais vous devriez passer un peu de temps sur votre front end pour qu'il ait l'air et se sente moderne.

Utilisez des frameworks CSS prêts à l'emploi et esthétiques comme Bootstrap pour réduire le temps de développement.

Réutilisez les composants HTML aussi souvent que possible, tant que cela ne conduit pas à la confusion. Réutilisez les designs de boutons, les formulaires et autres composants.

Votre MVP n'aura pas l'air comme dans vos rêves, mais c'est un luxe pour la version 2.0+.

Trompez vos utilisateurs en leur faisant croire que votre application est plus polie qu'elle ne l'est réellement.

#### Organisez votre base de données

Cela peut sembler un "agrément" pour beaucoup de gens, mais je pense que c'est nécessaire même pour un MVP, car cela vous évitera beaucoup de maux de tête à l'avenir.

Je déteste migrer des données ou apporter des changements chirurgicaux plus tard. C'est angoissant, risqué, et la plupart du temps, il est difficile de voir ce qui se passe (contrairement au front end ou au design).

Des données désorganisées et fragmentées peuvent ralentir votre site (UX), rendre le développement très douloureux (Expérience Développeur), et compliquer chaque étape que vous entreprenez par la suite.

Je prends du temps supplémentaire pour réfléchir à la manière de stocker mes données de manière à ce que cela ait du sens pour mon produit actuel et tout pivot prévisible.

Vous ne voulez pas en faire trop dans la conception du schéma, mais sérieusement — ne faites pas les choses à moitié pour votre base de données. Faites-les complètement.

### Que la Force soit avec vous

La vérité est — oui, je révèle la vérité après que vous ayez tout lu — vous ne saurez pas jusqu'à ce que vous l'ayez fait. Il vaut mieux manquer de peu que de perdre du temps à faire un travail qui n'aura pas d'importance.

Et vous ne saurez pas ce qui n'a pas d'importance à moins de manquer de peu.

Ne vous inquiétez pas de l'embarras, car même si vos photos nues étaient divulguées, vous êtes probablement un rêveur semi-anonyme comme le reste d'entre nous, et personne ne s'en souciera. Il y a un conseil de startup là-dedans quelque part.

Enfin, peu importe à quel point vous ratez votre MVP...

( •_•)  
( •_•)>⌐■-■

... vous pouvez toujours en parler après.

(⌐■_■)

_J'ai créé [rabbut.com](https://rabbut.com/?ref=h0), un outil qui vous permet de collecter des emails ici sur Medium (et ailleurs). Oh, regardez, en voici un maintenant :_

[**Vous cherchez mes anciennes histoires ? J'en ai quelques-unes. Ici.**](https://powered.by.rabbut.com/s/lbYA?c=10)  
[Chercher des histoires anciennes est un vrai casse-tête sur Medium. Cliquez ici pour un raccourci._powered.by.rabbut.com](https://powered.by.rabbut.com/s/lbYA?c=10)

_Aussi, je donne quelques copies de mon eBook sur le lancement d'une startup. Particulièrement utile pour les personnes qui ne savent pas comment lancer une startup :_

[**Les 10 premières personnes à s'abonner obtiennent mon eBook gratuit.**](https://powered.by.rabbut.com/e/wNXK?c=0)  
[Comment lancer votre startup en tant qu'inconnu._powered.by.rabbut.com](https://powered.by.rabbut.com/e/wNXK?c=0)

_Man, ces trucs [rabbut](https://rabbut.com/?ref=h00) sont partout maintenant. Je me demande où on pourrait en obtenir un..._