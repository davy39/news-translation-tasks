---
title: Comment quelqu'un a-t-il obtenu mon mot de passe ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-30T05:46:00.000Z'
originalURL: https://freecodecamp.org/news/how-did-someone-get-my-password-2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d47740569d1a4ca36db.jpg
tags:
- name: cyber
  slug: cyber
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: passwords
  slug: passwords
- name: phishing
  slug: phishing
seo_title: Comment quelqu'un a-t-il obtenu mon mot de passe ?
seo_desc: 'By Megan Kaczanowski

  Have you ever received a ''sextortion'' email telling you that your computer has
  been hacked and warning you that if you don''t pay up, they will release videos
  of an intimate nature to your entire contact list? Did the email includ...'
---

Par Megan Kaczanowski

Avez-vous déjà reçu un email de ['sextorsion'](https://www.forbes.com/sites/zakdoffman/2019/08/05/200m-email-addresses-held-by-sextortion-attackers-is-yours-on-their-list/#4214f11f67e4) vous disant que votre ordinateur a été piraté et vous avertissant que, si vous ne payez pas, ils diffuseront des vidéos de nature intime à votre liste de contacts entière ? L'email contenait-il un ancien mot de passe comme 'preuve' que leurs affirmations étaient vraies ? Vous êtes-vous demandé comment ils avaient obtenu votre mot de passe ?

## Qu'est-ce que le phishing ?

Statistiquement, cela provenait probablement d'un email de phishing. En 2018, 93 % de toutes les violations de données dans le monde ont commencé par une attaque de phishing ou de prétexte.

Les emails de phishing sont extrêmement courants et très efficaces. Ils utilisent des émotions comme la peur et la honte (dans les emails de sextorsion ou les publicités pour 'l'amélioration masculine'), l'urgence (mon patron en a besoin maintenant !), ou la cupidité (J'ai gagné une nouvelle voiture ??). 

Ils peuvent également être envoyés par SMS (SMiShing), par voix (vishing), par email (phishing), et par phishing sur les réseaux sociaux. 

Plus les gens s'adaptent, plus les hackers changent en réponse – leurs tactiques évoluent constamment. 

Généralement, les emails de phishing contiennent un lien ou une pièce jointe. Une fois que vous cliquez sur le lien ou ouvrez la pièce jointe, ils peuvent installer un malware sur votre appareil ou vous tromper en vous faisant entrer vos identifiants sur un faux site (qui ressemble exactement au site réel). Le malware vérifiera s'il peut exploiter des vulnérabilités non corrigées afin d'installer plus de malwares sur votre système (qui peuvent ensuite voler des mots de passe, installer des keyloggers pour enregistrer toutes vos frappes – et donc vos mots de passe ! – et ainsi de suite). 

Une fois que le hacker a volé vos identifiants, il peut faire des choses comme exfiltrer vos données financières personnelles ou les informations de votre compte, ou celles de vos clients si cela se produit sur l'appareil de votre entreprise.

Le phishing mérite un article à part entière, donc si vous êtes intéressé à apprendre comment phisher, consultez [cet article](https://www.pentestgeek.com/phishing/how-do-i-phish-advanced-email-phishing-tactics).

## Comment pouvez-vous empêcher le phishing de vous impacter ?

Se défendre contre le phishing est également difficile. En tant qu'individu, la meilleure chose à faire est de faire preuve de prudence lors de l'ouverture des emails – méfiez-vous des emails qui jouent sur vos émotions, vous demandent de prendre des décisions rapides, ou semblent trop beaux pour être vrais. 

Surveillez les expéditeurs inhabituels (reconnaissez-vous la personne qui vous envoie l'email ? Est-ce la même adresse email qu'elle a utilisée auparavant ?), ou les liens ou pièces jointes inattendus. Si vous n'êtes pas sûr qu'un email soit légitime, confirmez-le avec l'expéditeur via une autre méthode de communication.

Vous devriez également utiliser un logiciel antivirus et de protection des terminaux. La version payante est meilleure que la version gratuite, car elle est mise à jour dès qu'un nouveau malware est identifié. Mais la version gratuite est généralement meilleure que rien. J'aime Malwarebytes pour les ordinateurs portables.

Les équipes de sécurité utiliseront une myriade d'outils :

* des mécanismes de filtrage des emails qui tentent de réduire les emails de phishing et de spam qui atteignent les boîtes de réception des utilisateurs, 
* des mesures comme SPF, DKIM et DMARC qui peuvent aider à fournir une authentification qu'un email dit la vérité sur son origine, 
* des formations de sensibilisation des utilisateurs, 
* et des mécanismes de protection des terminaux. 

Les mécanismes de protection des terminaux peuvent aller de simples antivirus à des agents installés sur chaque appareil. Ceux-ci tenteront d'empêcher l'exécution de malwares connus, d'identifier les comportements inhabituels et d'empêcher l'exécution de processus malveillants en alertant une équipe de sécurité ou en forçant le programme à quitter.

Ainsi, même si l'email passe à travers les filtres et que l'utilisateur ne remarque rien d'anormal, la protection des terminaux empêchera le malware de causer des dommages à la machine.

## Comment quelqu'un a-t-il pu obtenir mon mot de passe ?

Souvent, lorsqu'un hacker pirate une entreprise, il vend les noms d'utilisateur et les mots de passe obtenus sur le dark web. 

> **Surface Web :** Ce que vous pouvez trouver sur Google ou d'autres moteurs de recherche populaires. Cela représente probablement la majeure partie de ce que vous considérez comme l'internet. Comparé au deep web, cela représente une très petite portion d'informations qui sont 'en ligne'.

> **Deep Web :** Des informations qui sont en ligne, mais qui ne sont pas indexées (recherchables) par Google et d'autres navigateurs populaires. Il s'agit d'informations telles que celles contenues dans les bases de données gouvernementales ou universitaires. Souvent, ces informations sont cachées derrière un paywall ou un autre mécanisme de restriction.

> **Dark Web :** Le dark web nécessite certains navigateurs, comme un 'navigateur TOR', pour y accéder. Une partie, bien que pas toute, de ce contenu est illégal. C'est souvent un endroit où les criminels se rassemblent pour discuter sur des forums, vendre des services et des biens illégaux, et parfois des activistes vivant sous des régimes répressifs se rassemblent pour communiquer.

Si vous réutilisiez des mots de passe et des noms d'utilisateur entre différents sites web (particulièrement puisque votre email est probablement utilisé comme nom d'utilisateur pour de nombreux sites web), un hacker pourrait déjà avoir votre nom d'utilisateur et votre mot de passe. 

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screen-Shot-2019-10-04-at-4.06.38-PM.png)
_[https://xkcd.com/792/](https://xkcd.com/792/)_

Le hacker effectuera ensuite ce qu'on appelle le 'bourrage d'identifiants'. Le bourrage d'identifiants est lorsque l'attaquant prend ces noms d'utilisateur et mots de passe et les insère dans un 'vérificateur de compte' automatisé qui essaie essentiellement la combinaison nom d'utilisateur/mot de passe sur de nombreux sites différents à travers l'internet, des connexions aux réseaux sociaux aux comptes bancaires. Si le mot de passe fonctionne, le hacker a maintenant accès au compte et peut vider un compte, vendre les données, etc. 

Pour une meilleure description, consultez la bande dessinée de XKCD ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-27-at-12.56.37-PM.png)
_[https://xkcd.com/2176/](https://xkcd.com/2176/)_

## Comment se défendre contre le bourrage d'identifiants ?

Ne réutilisez pas vos mots de passe. Utilisez un gestionnaire de mots de passe comme [1Password](https://1password.com/) ou [LastPass](https://www.lastpass.com/solutions/business-password-manager). [KeePass](https://keepass.info/) est (à mon avis) moins convivial, mais il est gratuit !

Les gestionnaires de mots de passe peuvent stocker vos mots de passe en toute sécurité et ont souvent des extensions de navigateur et des applications pour remplir automatiquement vos mots de passe sur de nombreux comptes. De plus, vous n'avez qu'à retenir un seul mot de passe principal. Mais votre mot de passe principal donne maintenant accès à tous vos autres mots de passe, alors assurez-vous qu'il est très solide ! 

Ils peuvent également vous aider à générer automatiquement des mots de passe très solides, et certains ont même des coffres pour stocker d'autres informations sensibles (détails de compte bancaire, informations d'assurance, etc.). 

Personnellement, j'utilise 1Password car j'aime l'option de compte familial – si quelqu'un dans votre famille se fait bloquer, quelqu'un d'autre peut réinitialiser le mot de passe de son compte (mais n'aura pas accès à votre coffre individuel). 

Vous pouvez également configurer des alertes gratuites avec [Have I Been Pwned](https://haveibeenpwned.com/). Ce site agrège les informations des violations de données et permet aux consommateurs d'utiliser ces informations pour se protéger. Vous pouvez naviguer vers l'onglet 'Notify Me' en haut et entrer votre adresse email. 

Après avoir confirmé l'adresse email que vous avez entrée (où il fournira votre exposition actuelle), le site vous enverra un email chaque fois que votre email est impliqué dans une violation de données. C'est-à-dire, toute violation dont le site est alerté – leur couverture est très bonne, mais aucune source unique ne contiendra toutes les violations de données divulguées. Ainsi, vous pouvez simplement changer le mot de passe impacté, et vous n'aurez pas à vous soucier de son impact sur vos autres comptes.

Si vous travaillez sur la sécurité pour une grande organisation, un logiciel de gestion des mots de passe d'entreprise (les mêmes entreprises listées ci-dessus fournissent ces services) est une excellente idée, ainsi que des politiques de mots de passe solides (obligation pour vos employés d'utiliser des mots de passe suffisamment solides). Have I Been Pwned propose également un service qui permet au propriétaire du domaine de surveiller les violations impliquant un email du domaine (et c'est gratuit !). 

## Comment les hackers obtiennent-ils des mots de passe ?

Il y a quelques autres possibilités – le 'shoulder surfing', ou simplement vous regarder taper votre mot de passe – bien que cela soit peu probable étant donné que la personne doit vous observer physiquement. 

Ensuite, il y a le vol de mots de passe qui ont été écrits, ou simplement [des photos de mots de passe écrits visibles sur des photos](https://www.businessinsider.com/hawaii-emergency-agency-password-discovered-in-photo-sparks-security-criticism-2018-1). Encore une fois, cela est beaucoup moins probable que les options ci-dessus car cela provient généralement d'une attaque ciblée (qui est intrinsèquement moins courante que les crimes d'opportunité).

Éviter ces deux situations est assez simple – ne laissez pas quelqu'un vous regarder entrer votre mot de passe, et n'écrivez pas votre mot de passe. Utilisez un gestionnaire de mots de passe à la place ! Si vous devez absolument l'écrire, stockez-le dans un endroit où quelqu'un est peu susceptible de chercher ou de trouver par accident. Je suggère le fond d'une boîte de tampons. Beaucoup plus sécurisé qu'un post-it sur votre moniteur.

## Il semble vraiment facile de se faire pirater. Devrais-je m'inquiéter ? 

La chose la plus importante à retenir sur le piratage est que personne ne veut faire plus de travail que nécessaire. Par exemple, entrer par effraction chez vous pour voler votre carnet de mots de passe est beaucoup plus difficile que d'envoyer des emails de phishing de l'autre côté du monde. S'il y a une manière plus facile d'obtenir votre mot de passe, c'est probablement ce qu'un acteur malveillant essaiera en premier. 

Cela signifie que l'activation des meilleures pratiques de base en matière de cybersécurité est probablement le moyen le plus facile d'éviter de se faire pirater. En fait, Microsoft a [récemments rapporté](https://www.zdnet.com/article/microsoft-using-multi-factor-authentication-blocks-99-9-of-account-hacks/) que l'activation de l'authentification à deux facteurs finit par bloquer 99,9 % des attaques automatisées.  

Alors, activez l'authentification à deux facteurs, utilisez un gestionnaire de mots de passe pour générer automatiquement des mots de passe longs, complexes et uniques pour chaque compte, et réfléchissez avant de cliquer ! Évitez de cliquer sur des liens ou des pièces jointes suspects ou inattendus, et restez vigilant.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-27-at-1.18.47-PM.png)
_[https://xkcd.com/538/](https://xkcd.com/538/)_

### 

##