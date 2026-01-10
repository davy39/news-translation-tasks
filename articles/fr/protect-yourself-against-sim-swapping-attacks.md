---
title: Comment se protéger contre les attaques par échange de SIM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-02T20:05:26.000Z'
originalURL: https://freecodecamp.org/news/protect-yourself-against-sim-swapping-attacks
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/pexels-photomix-company-887751.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: Comment se protéger contre les attaques par échange de SIM
seo_desc: "By Megan Kaczanowski\nWhat is a SIM swap?\nSIM swapping is when a hacker\
  \ convinces your cell phone carrier to switch your phone number to a different SIM\
  \ - one that they own. \nThis is a relatively normal thing for a retail employee\
  \ to do, which means t..."
---

Par Megan Kaczanowski

### Qu'est-ce qu'un échange de SIM ?

L'échange de SIM est une technique utilisée par un pirate pour convaincre votre opérateur de téléphonie mobile de transférer votre numéro de téléphone vers une autre carte SIM, qu'il possède. 

C'est une opération relativement normale pour un employé de magasin, ce qui signifie qu'une demande d'échange ne suscite généralement pas de soupçons. (Imaginez que vous avez acheté un nouveau téléphone et que vous devez transférer votre service mobile pour continuer à recevoir des textos et des appels sur votre nouvel appareil). 

Cela ne nécessite aucune connaissance technique de la part du pirate, juste une carte SIM et un appel téléphonique à votre opérateur. Curieux de savoir à quel point c'est facile ? Regardez [cette vidéo](https://www.youtube.com/watch?v=lc7scxvKQOo) d'une femme qui pirate un compte d'opérateur téléphonique en moins de 2 minutes. 

Même si l'opérateur réalise que l'action demandée est inhabituelle, les pirates corrompent souvent les représentants du service client avec des pots-de-vin allant jusqu'à 100 $ par échange (ce qui est une forte incitation pour des employés qui gagnent environ 10 $/heure). 

Une fois l'échange effectué, il est très difficile de l'inverser, car votre téléphone ne fonctionnera plus. De plus, vous devrez probablement vous rendre en personne chez votre opérateur pour prouver que l'échange était incorrect et que vous êtes le propriétaire du compte. 

En outre, jusqu'à ce que vous puissiez le faire, un pirate peut intercepter tous vos appels téléphoniques et messages, y compris les codes d'authentification basés sur SMS pour la 2FA et les options de réinitialisation de mot de passe par texto. Cela pourrait permettre à l'attaquant d'accéder à vos comptes en ligne ou de vous faire chanter avec des informations glanées à partir de messages texte et d'appels téléphoniques.

## Des échanges de SIM ont-ils déjà eu lieu ?

Oui ! Le technologiste en chef de la FTC a été [piraté de cette manière en 2016](https://www.wired.com/2016/06/even-ftcs-lead-technologist-can-get-hacked/), ainsi qu'un certain nombre de [comptes Instagram](https://mashable.com/2018/08/13/instagram-hack-locked-out-of-account/). Il existe même [un réseau criminel entier](https://www.vice.com/en_us/article/j5bpg7/sim-hijacking-t-mobile-stories) dédié à l'échange de SIM afin de vendre des identifiants Instagram contre des bitcoins, ainsi que d'autres activités criminelles.

## Que peuvent faire d'autre les attaquants par échange de SIM ?

[Une victime a rapporté que,](https://www.wired.com/2012/08/apple-amazon-mat-honan-hacking/)

> EN L'ESPACE d'une heure, toute ma vie numérique a été détruite. D'abord, mon compte Google a été piraté, puis supprimé. Ensuite, mon compte Twitter a été compromis et utilisé comme plateforme pour diffuser des messages racistes et homophobes. Et pire encore, mon compte AppleID a été piraté, et mes pirates l'ont utilisé pour effacer à distance toutes les données de mon iPhone, iPad et MacBook. [...] 
> 
> Si j'avais régulièrement sauvegardé les données de mon MacBook, je n'aurais pas eu à m'inquiéter de perdre plus d'un an de photos, couvrant toute la vie de ma fille, ou des documents et e-mails que j'avais stockés dans aucun autre endroit.

Si votre numéro de téléphone est lié à des comptes en ligne, le pirate peut souvent réinitialiser votre mot de passe par texto, ce qui signifie que le pirate a maintenant accès à tous vos comptes. 

Ils peuvent rapidement réinitialiser le mot de passe de votre adresse e-mail principale, puis utiliser cette adresse e-mail pour déclencher des réinitialisations de mot de passe pour d'autres comptes comme Amazon, la banque en ligne, les sites de médias sociaux, etc.

Voici [un exemple](https://www.wired.com/2012/08/apple-amazon-mat-honan-hacking/), 

> « Le support technique d'Apple m'a confirmé deux fois ce week-end que tout ce dont vous avez besoin pour accéder à l'AppleID de quelqu'un est l'adresse e-mail associée, un numéro de carte de crédit, l'adresse de facturation et les quatre derniers chiffres d'une carte de crédit enregistrée. J'ai été très clair à ce sujet. 
> 
> Lors de mon deuxième appel au support technique d'AppleCare, le représentant me l'a confirmé. « C'est vraiment tout ce que vous devez avoir pour vérifier quelque chose avec nous », a-t-il dit. » 

Toutes ces informations sont relativement faciles à trouver. Les attaquants peuvent rapidement rechercher des adresses sur des sites comme WhitePages et Spokeo, et il existe des [services de recherche d'e-mails dédiés](https://kinsta.com/blog/find-email-address/). 

De plus, Apple accepte n'importe quel numéro de carte de crédit, pas nécessairement celui enregistré. Les quatre derniers chiffres d'une carte de crédit enregistrée sont un peu plus difficiles à obtenir, mais loin d'être impossibles. 

Si un attaquant a déjà compromis votre e-mail principal en réinitialisant le mot de passe, il peut utiliser ces informations pour réinitialiser l'accès à des comptes comme Amazon (qui affichent les quatre derniers chiffres des cartes de crédit enregistrées). Le pirate peut ensuite utiliser ces informations pour accéder à votre AppleID et réinitialiser votre mot de passe, ainsi qu'accéder à toutes vos données sur iCloud. 

Si vous êtes comme beaucoup de gens et que vous stockez des mots de passe ou des données personnelles sur votre téléphone (dans votre application de notes) ou dans votre sauvegarde iCloud, le pirate a maintenant accès à toutes ces informations. Ils peuvent les voler à des fins de chantage ou les supprimer pour le « lulz ». Typiquement, ces informations sont irréversibles.

## Mais je n'ai rien à cacher !

Ce n'est pas seulement une question de données, bien que la plupart des gens n'aimeraient pas voir tous leurs textos, e-mails et photos rendus publics (ou supprimés !). 

Après un échange de SIM, les pirates peuvent passer de grandes commandes sur votre compte Amazon, pirater vos comptes bancaires, vos portefeuilles de cryptomonnaies ou vos comptes de retraite et les vider. Ils peuvent également détourner vos sites de médias sociaux pour diffuser de la désinformation ou des opinions antithétiques aux vôtres (racistes, homophobes ou autrement offensantes).

Ils peuvent détruire votre vie en ligne, puis s'attaquer à vos amis et à votre famille. Souvent, les attaquants utilisent votre e-mail (compromis) pour les contacter et les phisher. 

Certaines de ces actions peuvent être réversibles. Beaucoup ne le sont pas. Une fois que votre identité en ligne a été volée, il est très difficile de prouver aux différentes plateformes en ligne que vous êtes le véritable propriétaire. Cela devient encore plus difficile lorsque vous ne contrôlez pas les moyens de vérification de la plateforme (comme un compte e-mail ou un numéro de téléphone).

## Mais personne ne me ciblerait !

La chose la plus importante à retenir ici est que souvent, ce n'est pas une attaque ciblée contre vous. Il est peu probable que quelqu'un dise : « oh, ciblons cette personne spécifique ». Cependant, les pirates peuvent cibler un compte sans savoir qui est le propriétaire. 

Par exemple, les cibles courantes incluent les comptes de cryptomonnaies ou les identifiants uniques sur les médias sociaux (« les identifiants OG » tels que « @awesome » – des identifiants que vous auriez dû être le premier à revendiquer sur une plateforme particulière).

Ensuite, le pirate traque le propriétaire, échange sa SIM et prend ce qu'il veut. Ce piratage nécessite peu de sophistication technique, de temps et d'argent, et est **extrêmement** lucratif (les identifiants OG se vendent entre 500 et 5000 $ chacun, tandis que le détournement de comptes bancaires ou de retraite peut rapporter des milliers de dollars), ce qui le rend extrêmement populaire parmi les pirates. 

Beaucoup des pirates sur les forums dédiés à l'échange de SIM sont des adolescents. Ils ne pensent souvent pas aux conséquences à long terme de leurs actions et recherchent simplement le plaisir. Ils ne sont pas des acteurs rationnels et n'ont souvent pas à penser à leurs victimes comme à des personnes dont ils détruisent la vie, car ils n'interagissent jamais avec elles. 

C'est aussi un piratage très difficile à poursuivre en justice. L'attribution est extrêmement difficile à déterminer pour les cyberattaques, et le volume élevé d'attaques rend très difficile pour les forces de l'ordre de suivre (en particulier les forces de l'ordre locales, qui sont souvent en retard en matière de sophistication technique et de législation entourant les crimes informatiques). 

Comme l'a noté un agent des forces de l'ordre,

> 
> « Pour les montants volés et le nombre de personnes qui réussissent à le faire, les chiffres sont probablement historiques », a déclaré Tarazi. « Nous parlons de jeunes âgés principalement entre 19 et 22 ans capables de voler des millions de dollars en cryptomonnaies. 
> 
> Je veux dire, si quelqu'un se fait voler 100 000 $, c'est une grosse affaire, mais nous avons maintenant affaire à quelqu'un qui achète une carte SIM à 99 cents sur eBay, la branche sur un téléphone jetable bon marché, passe un appel et vole des millions de dollars. C'est assez remarquable. » – [Source](https://krebsonsecurity.com/2018/11/busting-sim-swappers-and-sim-swap-myths/)

## Recommandations pour tous afin de protéger votre SIM

* Utilisez une méthode de 2FA autre que les SMS, comme une application telle que Google Authenticator ou une clé matérielle comme YubiKey. Vous devriez utiliser cela pour autant de sites que possible qui offrent la 2FA (au minimum, elle devrait être utilisée pour votre adresse e-mail principale).
* Utilisez un [gestionnaire de mots de passe](https://megankaczanowski.com/digital-security/)
* Ajoutez un code PIN à votre forfait de téléphonie mobile (pas efficace à 100 %, mais mieux que rien). Les quatre principaux opérateurs aux États-Unis offrent ce service. De nombreux opérateurs en Afrique (y compris au Mozambique, en Afrique du Sud, au Kenya et au Nigeria), au Royaume-Uni et en Australie ont mis en place des protections permettant aux banques de vérifier si le client a récemment échangé sa SIM lors du traitement d'une transaction (ainsi, s'il y a eu un échange récent de SIM, ils peuvent refuser la transaction). Cela limite les dégâts qu'un attaquant peut causer, mais il est toujours prudent de rester vigilant face à ces types d'attaques.
* Agissez immédiatement si vous remarquez que votre téléphone portable cesse de fonctionner. Appelez votre opérateur de téléphonie mobile depuis un autre appareil et verrouillez vos comptes immédiatement.
* Utilisez des services comme Privacy ou Blur qui fournissent des cartes de crédit/débit à usage unique pour les achats afin d'éviter de lier une seule carte de crédit à de nombreux comptes.

### Recommandations supplémentaires pour les cibles à haut risque :

* Utilisez une clé matérielle pour votre adresse e-mail principale et une 2FA basée sur une application pour les autres comptes. Activez la 2FA pour autant de comptes que possible qui l'offrent.
* Si vous utilisez Gmail comme adresse e-mail personnelle principale, inscrivez-vous à leur [Programme de Protection Avancée](https://landing.google.com/advancedprotection/).
* Ne liez pas votre numéro de téléphone à des comptes – cela permet souvent la réinitialisation du mot de passe par texto sans vous avertir. Si vous devez ajouter un numéro de téléphone à votre compte, configurez un numéro de téléphone séparé avec un service comme MySudo ou Google Voice. N'utilisez pas ce numéro de téléphone pour autre chose.

Merci d'avoir lu – et restez en sécurité.

### Sources/Lectures complémentaires :

* [Comment les failles de sécurité d'Apple et d'Amazon ont conduit à mon piratage épique](https://www.wired.com/2012/08/apple-amazon-mat-honan-hacking/)
* [Démantèlement des échangeurs de SIM et des mythes sur l'échange de SIM](https://krebsonsecurity.com/2018/11/busting-sim-swappers-and-sim-swap-myths/)
* [Comment se protéger contre une attaque par échange de SIM](https://www.wired.com/story/sim-swap-attack-defend-phone/)
* [Les pirates de SIM](https://www.vice.com/en/article/vbqax3/hackers-sim-swapping-steal-phone-numbers-instagram-bitcoin)
* [Les pirates s'introduisent dans les entreprises de télécommunications pour prendre le contrôle des numéros de téléphone des clients](https://www.vice.com/en/article/5dmbjx/how-hackers-are-breaking-into-att-tmobile-sprint-to-sim-swap-yeh)