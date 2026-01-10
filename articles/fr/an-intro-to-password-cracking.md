---
title: Comment craquer des mots de passe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-28T05:52:00.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-password-cracking
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c61740569d1a4ca31d0.jpg
tags:
- name: cyber
  slug: cyber-2
- name: cybersecurity
  slug: cybersecurity
- name: fintech
  slug: fintech
- name: information security
  slug: information-security
- name: passwords
  slug: passwords
seo_title: Comment craquer des mots de passe
seo_desc: "By Megan Kaczanowski\nA brief note - this article is about the theory of\
  \ how to crack passwords. Understanding how cybercriminals execute attacks is extremely\
  \ important for understanding how to secure systems against those types of attacks.\
  \ \nAttemptin..."
---

Par Megan Kaczanowski

Une brève note - cet article traite de la théorie sur la façon de craquer des mots de passe. Comprendre comment les cybercriminels exécutent des attaques est extrêmement important pour comprendre comment sécuriser les systèmes contre ces types d'attaques. 

Tenter de pirater un système que vous ne possédez pas est probablement illégal dans votre juridiction (de plus, pirater vos propres systèmes peut [et souvent le fait] violer toute garantie pour ce produit). 

## Commençons par les bases. Qu'est-ce qu'une attaque par force brute ?

Ce type d'attaque implique de tenter à plusieurs reprises de se connecter en tant qu'utilisateur en essayant toutes les combinaisons possibles de lettres, de chiffres et de caractères (à l'aide d'outils automatisés). 

Cela peut être fait soit en ligne (en temps réel, en essayant continuellement différentes combinaisons de nom d'utilisateur/mot de passe sur des comptes comme les réseaux sociaux ou les sites bancaires) ou hors ligne (par exemple, si vous avez obtenu un ensemble de mots de passe hachés et que vous essayez de les craquer hors ligne). 

Le hors ligne n'est pas toujours possible (il peut être difficile d'obtenir un ensemble de mots de passe hachés), mais il est beaucoup moins bruyant. Cela est dû au fait qu'une équipe de sécurité remarquera probablement de nombreuses tentatives de connexion échouées depuis le même compte, mais si vous pouvez craquer le mot de passe hors ligne, vous n'aurez pas de trace de tentatives de connexion échouées.

Cela est relativement facile avec un mot de passe court. Cela devient exponentiellement plus difficile avec un mot de passe plus long en raison du nombre énorme de possibilités. 

Par exemple, si vous savez que quelqu'un utilise un mot de passe de 5 caractères, composé uniquement de lettres minuscules, le nombre total de mots de passe possibles est 26^5 (26 lettres possibles à choisir pour la première lettre, 26 choix possibles pour la deuxième lettre, etc.), soit 11 881 376 combinaisons possibles. 

Mais si quelqu'un utilise un mot de passe de 11 caractères, uniquement en lettres minuscules, le nombre total de mots de passe possibles est 26 ^11, soit 3 670 344 486 987 776 mots de passe possibles. 

Lorsque vous ajoutez des lettres majuscules, des caractères spéciaux et des chiffres, cela devient encore plus difficile et long à craquer. Plus il y a de mots de passe possibles, plus il est difficile pour quelqu'un de se connecter avec succès avec une attaque par force brute.

### Comment se protéger

Ce type d'attaque peut être défendu de plusieurs manières différentes. Tout d'abord, vous pouvez utiliser des mots de passe suffisamment longs et complexes (au moins 15 caractères). Vous pouvez également utiliser des mots de passe uniques pour chaque compte (utilisez un gestionnaire de mots de passe !) pour réduire le danger des violations de données.

Une équipe de sécurité peut verrouiller un compte après un certain nombre de tentatives de connexion échouées. Ils peuvent également forcer une méthode secondaire de vérification comme Captcha, ou utiliser l'authentification à deux facteurs (2FA) qui nécessite un deuxième code (SMS ou email, basé sur une application, ou basé sur une clé matérielle).

[Voici](https://null-byte.wonderhowto.com/how-to/gain-ssh-access-servers-by-brute-forcing-credentials-0194263/) un article sur la façon d'exécuter une attaque par force brute.

## Comment pouvez-vous craquer des mots de passe plus rapidement ?

Une attaque par dictionnaire implique de tenter de se connecter à plusieurs reprises en essayant un certain nombre de combinaisons incluses dans un 'dictionnaire' précompilé, ou une liste de combinaisons. 

Cela est généralement plus rapide qu'une attaque par force brute car les combinaisons de lettres et de chiffres ont déjà été calculées, ce qui vous fait gagner du temps et de la puissance de calcul. 

Mais si le mot de passe est suffisamment complexe (par exemple 1098324ukjbfnsdfsnej) et n'apparaît pas dans le 'dictionnaire' (la liste précompilée de combinaisons que vous utilisez), l'attaque ne fonctionnera pas. 

Elle est fréquemment réussie car, souvent lorsque les gens choisissent des mots de passe, ils choisissent des mots courants ou des variations de ces mots (par exemple, 'password' ou 'p@SSword'). 

Un pirate pourrait également utiliser ce type d'attaque lorsqu'il connaît ou devine une partie du mot de passe (par exemple, le nom d'un chien, les anniversaires des enfants, ou un anniversaire - des informations qu'un pirate peut trouver sur les pages des réseaux sociaux ou d'autres ressources open source). 

Des mesures de protection similaires à celles décrites ci-dessus contre les attaques par force brute peuvent empêcher ces types d'attaques d'être réussies.

## Que faire si vous avez déjà une liste de mots de passe hachés ?

Les mots de passe sont stockés dans le fichier /etc/shadow pour Linux et C:\Windows\System32\config pour Windows (qui ne sont pas disponibles lorsque le système d'exploitation est démarré). 

Si vous avez réussi à obtenir ce fichier, ou si vous avez obtenu un hachage de mot de passe d'une autre manière, comme en sniffant le trafic sur le réseau, vous pouvez essayer de craquer les mots de passe 'hors ligne'. 

Alors que les attaques ci-dessus nécessitent de tenter à plusieurs reprises de se connecter, si vous avez une liste de mots de passe hachés, vous pouvez essayer de les craquer sur votre machine, sans déclencher d'alertes générées par des tentatives de connexion répétées et échouées. Ensuite, vous n'essayez de vous connecter qu'une seule fois, après avoir réussi à craquer le mot de passe (et donc il n'y a pas de tentative de connexion échouée). 

Vous pouvez utiliser des attaques par force brute ou des attaques par dictionnaire contre les fichiers de hachage, et vous pouvez réussir en fonction de la force du hachage.

### Attendez une minute - qu'est-ce que le hachage ?

35D4FFEF6EF231D998C6046764BB935D

Reconnaissez ce message ? Il dit 'Salut, je m'appelle megan'

7DBDA24A2D10DAF98F23B95CFAF1D3AB

Celui-ci est le premier paragraphe de cet article. Oui, cela ressemble à du charabia, mais c'est en fait un 'hachage'. 

Une fonction de hachage permet à un ordinateur de saisir une chaîne (une combinaison de lettres, de chiffres et de symboles), de prendre cette chaîne, de la mélanger et de produire une chaîne de longueur fixe. C'est pourquoi les deux chaînes ci-dessus ont la même longueur, même si les entrées des chaînes étaient de longueurs très différentes. 

Les hachages peuvent être créés à partir de presque tout contenu numérique. Basiquement, tout contenu numérique peut être réduit à du binaire, ou une série de 0 et de 1. Par conséquent, tout contenu numérique (images, documents, etc.) peut être haché. 

Il existe de nombreuses fonctions de hachage différentes, certaines étant plus sécurisées que d'autres. Les hachages ci-dessus ont été générés avec MD5 (MD signifie "Message Digest"). Différentes fonctions diffèrent également par la longueur du hachage qu'elles produisent. 

Le même contenu dans la même fonction de hachage produira toujours le même hachage. Cependant, même un petit changement modifiera entièrement le hachage. Par exemple, 

2FF5E24F6735B7564CAE7020B41C80F1

Est le hachage pour 'Salut, je m'appelle Megan'. Juste le fait de mettre la lettre M en majuscule dans Megan a complètement changé le hachage par rapport à celui ci-dessus.

Les hachages sont également des fonctions à sens unique (ce qui signifie qu'ils ne peuvent pas être inversés). Cela signifie que les hachages (uniques et à sens unique) peuvent être utilisés comme une sorte d'empreinte digitale numérique pour le contenu. 

### Quel est un exemple de l'utilisation des hachages ?

Les hachages peuvent être utilisés comme vérification qu'un message n'a pas été changé. 

Lorsque vous envoyez un email, par exemple, vous pouvez hacher l'ensemble de l'email et envoyer le hachage également. Ensuite, le destinataire peut faire passer le message reçu par la même fonction de hachage pour vérifier si le message a été falsifié en transit. Si les deux hachages correspondent, le message n'a pas été altéré. S'ils ne correspondent pas, le message a été changé. 

De plus, les mots de passe sont généralement hachés lorsqu'ils sont stockés. Lorsque l'utilisateur entre son mot de passe, l'ordinateur calcule la valeur de hachage et la compare à la valeur de hachage stockée. De cette façon, l'ordinateur ne stocke pas les mots de passe en texte brut (pour qu'un pirate indiscret ne puisse pas les voler !).

Si quelqu'un est capable de voler le fichier de mots de passe, les données sont inutiles car la fonction ne peut pas être inversée (bien qu'il existe des moyens, comme les tables arc-en-ciel, pour découvrir quel texte brut crée le hachage connu).

### Quel est le problème avec les hachages ?

Si un hachage peut prendre des données de n'importe quelle longueur ou contenu, il existe des possibilités illimitées pour les données qui peuvent être hachées. 

Puisqu'un hachage convertit ce texte en un contenu de longueur fixe (par exemple, 32 caractères), il existe un nombre fini de combinaisons pour un hachage. C'est un nombre très très grand de possibilités, mais pas infini.

Finalement, deux ensembles de données différents produiront la même valeur de hachage. Cela s'appelle une collision. 

Si vous avez un hachage et que vous essayez de passer par chaque valeur de texte brut possible pour trouver le texte brut qui correspond à votre hachage, ce sera un processus très long et très difficile. 

### Cependant, que se passe-t-il si vous ne vous souciez pas de savoir quels deux hachages entrent en collision ?

Cela s'appelle le '[problème des anniversaires](https://en.wikipedia.org/wiki/Birthday_problem)' en mathématiques. Dans une classe de 23 étudiants, la probabilité que quelqu'un ait un anniversaire un jour spécifique est d'environ 7 %, mais la probabilité que deux personnes partagent le même anniversaire est d'environ 50 %. 

Le même type d'analyse peut être appliqué aux fonctions de hachage afin de trouver deux hachages qui correspondent (au lieu d'un hachage spécifique qui correspond à l'autre). 

Pour éviter cela, vous pouvez utiliser des fonctions de hachage plus longues telles que SHA3, où la possibilité de collisions est plus faible.

Vous pouvez essayer de générer vos propres fonctions de hachage pour SHA3 [ici](https://www.browserling.com/tools/sha3-hash) et MD5 [ici](http://onlinemd5.com/).  

Vous pouvez essayer de forcer les hachages par brute force, mais cela prend beaucoup de temps. La méthode la plus rapide pour le faire est d'utiliser des [tables arc-en-ciel](https://www.freecodecamp.org/news/p/ee82d358-9d43-49a8-84a6-8ffca9a3ee1f/www.freecodecamp.org/news/why-a-little-salt-can-be-great-for-your-passwords) pré-calculées (qui sont similaires aux attaques par dictionnaire).

## Cela semble vraiment facile de se faire pirater. Devrais-je être inquiet ?

La chose la plus importante à retenir sur le piratage est que personne ne veut faire plus de travail que nécessaire. Par exemple, forcer les hachages par brute force peut être extrêmement chronophage et difficile. S'il existe un moyen plus facile d'obtenir votre mot de passe, c'est probablement ce qu'un acteur malveillant essaiera en premier. 

Cela signifie que l'activation des meilleures pratiques de base en matière de cybersécurité est probablement le moyen le plus facile de prévenir le piratage. En fait, Microsoft a [récemment rapporté](https://www.zdnet.com/article/microsoft-using-multi-factor-authentication-blocks-99-9-of-account-hacks/) que le simple fait d'activer la 2FA finira par bloquer 99,9 % des attaques automatisées. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-27-at-1.18.47-PM.png)
_[https://xkcd.com/538/](https://xkcd.com/538/)_

**Lectures supplémentaires :**

[Outils populaires de craquage de mots de passe](https://resources.infosecinstitute.com/10-popular-password-cracking-tools/#gref)