---
title: Comment l'authentification SSH avec GitHub fonctionne en coulisses
subtitle: ''
author: Vivek Agrawal
co_authors: []
series: null
date: '2025-02-12T18:06:54.737Z'
originalURL: https://freecodecamp.org/news/ssh-authentication-with-github-under-the-hood
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739082652213/aba38efa-117c-4ef7-a844-91599c0a4d62.png
tags:
- name: ssh
  slug: ssh
- name: Security
  slug: security
- name: public-key cryptgraphy
  slug: public-key-cryptgraphy
- name: encryption
  slug: encryption
seo_title: Comment l'authentification SSH avec GitHub fonctionne en coulisses
seo_desc: 'SSH (Secure Shell) is a client-server protocol for connecting and authenticating
  to a remote server.

  Authentication means that the remote server can verify that it’s actually you and
  not somebody else talking on your behalf.

  You may already be using ...'
---

SSH (Secure Shell) est un protocole client-serveur pour se connecter et s'authentifier sur un serveur distant.

L'authentification signifie que le serveur distant peut vérifier qu'il s'agit bien de vous et non de quelqu'un d'autre qui parle en votre nom.

Vous utilisez peut-être déjà l'authentification SSH de GitHub, mais savez-vous comment elle fonctionne réellement ? Dans cet article, vous apprendrez ce qui se passe en coulisses et comment l'authentification SSH fonctionne réellement.

En cours de route, vous comprendrez les concepts fondamentaux de la cryptographie que tout développeur devrait connaître : le chiffrement symétrique, le chiffrement asymétrique, les fonctions de hachage cryptographique et les signatures numériques.

Certains développeurs n'ont généralement pas l'occasion d'apprendre et de comprendre ces fondamentaux de la cryptographie, mais ces concepts vous aideront à long terme. De plus, ils vous aideront à être dans une bien meilleure position pour prendre des décisions de sécurité éclairées pour vos applications web de production.

Alors, attachez vos ceintures et commençons !

### Voici ce que nous allons couvrir :

1. [Tout d'abord, pourquoi l'authentification est-elle si importante ?](#heading-tout-dabord-pourquoi-lauthentification-est-elle-si-importante)
    
2. [Chiffrement symétrique](#heading-chiffrement-symetrique)
    
3. [Chiffrement asymétrique](#heading-chiffrement-asymetrique)
    
4. [Fonctions de hachage cryptographique](#heading-fonctions-de-hachage-cryptographique)
    
5. [Signatures numériques](#heading-signatures-numeriques)
    
6. [Comment fonctionne l'authentification SSH](#heading-comment-fonctionne-lauthentification-ssh)
    
7. [Conclusion](#heading-conclusion)
    

## Tout d'abord, pourquoi l'authentification est-elle si importante ?

Lorsque nous exécutons `git push`, GitHub doit vérifier que la bonne personne interagit avec GitHub. Imaginez si un attaquant pouvait réussir à faire `git push` en votre nom.

Alors tous vos dépôts seraient sous le contrôle de cet attaquant. Ils pourraient supprimer tout votre code ainsi que tout l'historique des commits.

Cela semble assez dangereux, n'est-ce pas ? Donc, pour vérifier que c'est bien vous qui parlez à GitHub, et non un attaquant, GitHub a plusieurs moyens de vous authentifier.

La méthode la plus largement utilisée pour s'authentifier avec GitHub est l'authentification SSH.

Avant de comprendre comment l'authentification SSH fonctionne en coulisses, nous devrons comprendre les concepts fondamentaux de la cryptographie, à savoir le chiffrement symétrique, le chiffrement asymétrique, les fonctions de hachage cryptographique et les signatures numériques.

Commençons !

## Chiffrement symétrique

Dans les temps anciens, les dirigeants imaginaient diverses méthodes pour communiquer des messages militaires secrets à leurs commandants d'armée.

L'une des premières méthodes, probablement utilisée par les dirigeants grecs anciens et peut-être plus tard par les Romains, impliquait l'utilisation d'une tige de bois cylindrique appelée [**Scytale**](https://en.wikipedia.org/wiki/Scytale).

Avant une invasion militaire, le dirigeant faisait fabriquer deux tiges de bois cylindriques exactement identiques appelées scytales. Ensuite, il donnait une scytale au commandant de l'armée et en gardait une pour lui-même.

![Une scytale avec une bande de cuir enroulée et un message écrit dessus.](https://cdn.hashnode.com/res/hashnode/image/upload/v1734514827027/b4945c3a-64d4-458b-a410-f23b1a08d9ef.png align="center")

Le dispositif fonctionnait en enroulant une bande de cuir autour de la scytale. Après avoir fait cela, le dirigeant écrivait le message sur le dessus de la bande de cuir enroulée de sorte qu'il ne pouvait être lu que lorsqu'il était correctement enroulé à nouveau.

Supposons que la scytale lui permettait d'écrire trois lettres en cercle et cinq lettres en ligne droite le long de sa longueur. La bande de cuir enroulée avec le message `attackfromright` écrit dessus ressemblerait à ceci :

```plaintext
       |   |   |   |   |   |
       | a | t | t | a | c |  |
     __| k | f | r | o | m |__|
    |  | r | i | g | h | t |
    |  |   |   |   |   |   |
```

Après avoir écrit le message sur la scytale, le dirigeant déroulait la bande de cuir et l'envoyait au commandant de l'armée. Une fois déroulée, la bande de cuir aurait le message suivant :

```plaintext
----------------
akrtfitrgaohcmt
----------------
```

Vous voyez donc que même si la bande de cuir était interceptée par un espion ennemi, le message n'aurait aucun sens. N'est-ce pas fascinant ? L'utilisation intelligente d'une tige de bois et d'une bande de cuir a peut-être aidé certains dirigeants anciens à gagner des batailles !

Lorsque la bande de cuir atteignait le commandant de l'armée, il l'enroulait autour de sa propre scytale (qui serait exactement la même que celle du dirigeant), et ensuite le commandant pouvait comprendre le message correctement.

Cette technique de la scytale est en fait un exemple de chiffrement symétrique en pratique.

Le chiffrement est un processus dans lequel le message original est modifié (ou codé) de telle sorte que seul le destinataire prévu peut le décoder et voir le message réel.

Le message original est appelé texte en clair, tandis que le message codé est appelé texte chiffré. Le chiffrement convertit le `texte en clair en texte chiffré` à l'aide d'une clé.

Pour déchiffrer le message, c'est-à-dire convertir le `texte chiffré en texte en clair`, une personne doit avoir accès à cette même clé.

Si nous le comparons à la technique de la scytale, la scytale est la clé. Le dirigeant ne partage la clé (scytale) qu'avec le commandant de l'armée qui doit connaître le contenu du message.

Voici à quoi ressemble le processus de chiffrement :

![Chiffrement avec la scytale comme clé.](https://cdn.hashnode.com/res/hashnode/image/upload/v1734519516607/75c926a3-faec-402a-8bcd-122039f47a01.png align="center")

Le processus de déchiffrement ressemblera à ceci :

![Déchiffrement avec la scytale comme clé.](https://cdn.hashnode.com/res/hashnode/image/upload/v1734519525487/de096889-332c-4482-b2df-b28ce609a8a6.png align="center")

Nous appelons cela le chiffrement symétrique car la même clé est utilisée pour chiffrer et déchiffrer le message.

Cette clé (la scytale) doit être protégée de l'accès ennemi. Si l'ennemi obtient accès à cette clé, alors ils pourront déchiffrer les messages.

Mais il existe un autre type de chiffrement appelé chiffrement asymétrique. Maintenant que vous comprenez le chiffrement symétrique, passons au chiffrement asymétrique.

## Chiffrement asymétrique

Dans le chiffrement symétrique, comme nous l'avons vu ci-dessus, la même clé était utilisée par le dirigeant et le commandant de l'armée pour chiffrer et déchiffrer le message.

Mais dans un chiffrement asymétrique, il y a deux clés (appelées une paire de clés). Parmi les deux clés, l'une est une clé privée et l'autre est une clé publique.

La clé publique peut être partagée avec tout le monde (c'est pourquoi elle est appelée publique). Mais la clé privée doit être gardée secrète ! Elle ne doit jamais être révélée à quiconque.

![La clé publique peut être partagée avec tout le monde. Mais la clé privée doit être gardée secrète.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735200860039/7aca8ffa-c33a-44e5-ab1a-181492ebefd8.png align="center")

L'aspect intéressant du chiffrement asymétrique est que, si un message est chiffré avec la clé publique, alors il ne peut être déchiffré qu'avec la clé privée correspondante. Aucune autre clé ne peut le déchiffrer.

Et cela fonctionne aussi dans l'autre sens. Si un message est chiffré avec la clé privée, alors il ne peut être déchiffré qu'en utilisant la clé publique correspondante.

![Illustration des clés publique et privée liées mathématiquement entre elles.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735120077350/b90901c8-b55c-428a-8eb4-1b8ffa65fa06.png align="center")

Les deux clés - publique et privée - sont liées mathématiquement entre elles. Pendant qu'une chiffrer, l'autre déchiffre.

Juste une petite note que le chiffrement asymétrique est également appelé chiffrement à clé publique. Ces deux termes sont utilisés de manière interchangeable mais ils signifient la même chose.

## Fonctions de hachage cryptographique

Une fonction de hachage cryptographique est conçue pour prendre une entrée de n'importe quelle longueur et produire une sortie de longueur fixe. La sortie de longueur fixe est appelée valeur de hachage.

Un exemple populaire de fonction de hachage cryptographique est SHA-256.

![Calcul SHA-256 de "freeCodeCamp.org"](https://cdn.hashnode.com/res/hashnode/image/upload/v1735030835833/201640c6-13b4-4b2b-9be3-88e245269bd1.png align="center")

L'image ci-dessus montre la valeur de hachage SHA-256 de l'entrée "freeCodeCamp.org". La fonction de hachage cryptographique a trois propriétés qui la rendent très utile (nous verrons comment dans les sections à venir).

Premièrement, il est pratiquement impossible de prendre la valeur de hachage et de déterminer l'entrée à partir de la valeur de hachage.

Par exemple, si nous recevons la valeur de hachage `c9c31315ef2257e4b7698`, il n'y a aucun moyen pour nous de déterminer que l'entrée de la fonction de hachage était "freeCodeCamp.org".

Deuxièmement, si nous passons la même entrée à la fonction de hachage, nous obtenons la même valeur de hachage en sortie.

Si nous passons "freeCodeCamp.org" à nouveau à la fonction de hachage SHA-256, nous obtiendrons la même sortie de hachage que notre appel précédent.

Troisièmement, deux entrées différentes ne partagent jamais la même valeur de hachage. Même le moindre changement dans l'entrée produit une sortie entièrement différente.

Supposons que nous fournissions "freeCodeCamp" comme entrée au lieu de "freeCodeCamp.org" - nous obtiendrions une sortie totalement différente.

## Signatures numériques

Dans votre vie quotidienne, vous pouvez avoir à signer divers documents. Il peut s'agir de documents juridiques, ou du bulletin scolaire de vos enfants, ou peut-être autre chose.

Lorsque votre signature est présente sur le document, elle indique à l'autre partie que c'est vous qui êtes d'accord avec ce qui est écrit sur ce document.

Par la suite, vous ne pouvez pas revenir sur ce qui est écrit sur le document. Correct ?

De même, dans le monde numérique, nous avons des signatures numériques - ou nous pouvons simplement les appeler signatures.

Comprenons comment fonctionnent les signatures à l'aide d'un exemple. Nous avons deux utilisateurs nommés "Alice" et "Bob".

Bob veut transférer de l'argent sur le compte bancaire d'Alice. Donc Bob demande à Alice ses informations de compte bancaire.

![Une illustration montrant les ordinateurs d'Alice et de Bob éloignés l'un de l'autre et le numéro de compte bancaire d'Alice.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735042150046/034d26c5-b33d-4b82-aeb8-173e47cd8e8e.png align="center")

Alice connaît les signatures numériques et décide d'en utiliser une. À la fin, vous comprendrez pourquoi Alice a opté pour une signature numérique.

Avant qu'Alice ne puisse créer une signature numérique, Alice fournit à Bob sa clé publique (et garde la clé privée pour elle-même).

Ensuite, Alice crée une signature numérique et la place à la fin du document.

![Processus de génération de signature numérique.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735041977880/35313148-8820-42d7-b122-3ddf0cbaa723.png align="center")

Une signature numérique est créée en passant d'abord le contenu du document à une fonction de hachage cryptographique comme SHA-256. Dans le cas d'Alice, le contenu du document est son numéro de compte bancaire.

Une fois que nous obtenons la valeur de hachage, elle est chiffrée avec la **clé privée** d'Alice. La sortie de ce chiffrement est la signature qui est placée à la fin du document.

Cela est ensuite envoyé à Bob via Internet.

Lorsque Bob reçoit ce document, il vérifie si la **signature est valide ou non**.

![Processus de vérification de la signature.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735043216695/256f7707-3f40-433f-9b00-c11b27ef01e8.png align="center")

Pour vérifier la signature, Bob déchiffre d'abord la signature avec la clé publique d'Alice. Si vous vous souvenez, Alice a généré la signature en chiffrant la valeur de hachage.

```plaintext
 texte en clair                         texte chiffré  
     |                                 |
     |                                 |
     |                                 |
valeur de hachage --------chiffrer--------> signature
```

Donc, lorsque Bob déchiffre la signature, il obtiendra la valeur de hachage qu'Alice a calculée. Appelons cela la valeur de hachage d'Alice.

```plaintext
 texte chiffré                         texte en clair  
     |                                 |
     |                                 |
     |                                 |
signature --------dechiffrer--------> valeur de hachage
```

Ensuite, Bob prend le numéro de compte bancaire qui est présent sur le document et le passe à la fonction de hachage.

Enfin, Bob compare la valeur de hachage d'Alice (la signature déchiffrée) et la valeur de hachage qu'il vient de calculer. Si les deux valeurs de hachage correspondent, cela signifie que la signature est valide.

D'accord - mais pourquoi avons-nous dû faire tout cela ? Que signifie-t-il si la signature est valide ?

Lorsque la vérification de la signature est réussie, cela prouve deux choses.

Premièrement, cela prouve que le document a été envoyé par Alice uniquement. Personne d'autre n'aurait pu envoyer ce document.

L'assurance que seul Alice a envoyé ce document vient du fait que nous avons pu déchiffrer la signature en utilisant la clé publique d'Alice.

Nous avons appris que si quelque chose est chiffré en utilisant une clé privée, alors il ne peut être déchiffré qu'en utilisant sa clé publique liée.

Donc, si Bob a réussi à déchiffrer la signature en utilisant la clé publique d'Alice, cela signifie qu'elle a été chiffrée en utilisant la clé privée d'Alice, n'est-ce pas ?

Et seul Alice a accès à sa clé privée. Cela signifie qu'Alice est la seule personne qui aurait pu envoyer ce document !

Deuxièmement, cela prouve que le contenu du message n'a pas été modifié par un attaquant lors de la transmission sur le réseau.

Nous avons fait deux choses pour vérifier la signature. Nous avons déchiffré la signature, et elle nous a donné la valeur de hachage qu'Alice a calculée. Et nous avons également haché le numéro de compte bancaire reçu.

Si la valeur de hachage qu'Alice a calculée et la valeur de hachage que Bob a calculée sont les mêmes, cela signifie qu'Alice et Bob ont donné exactement la même entrée à la fonction de hachage.

Et cela signifie que le numéro de compte bancaire qu'Alice a envoyé et que Bob a reçu sont exactement les mêmes.

Si un attaquant avait changé le numéro de compte bancaire avant que le document n'atteigne Bob, alors Bob aurait reçu un numéro de compte bancaire modifié.

Lorsque Bob est allé calculer la valeur de hachage de ce numéro de compte bancaire modifié, la valeur de hachage aurait été différente de ce qu'Alice avait calculé.

Donc, lors de la comparaison de la valeur de hachage d'Alice (signature déchiffrée) et de la valeur de hachage que Bob a calculée, la correspondance échouerait. Et cela empêcherait Bob de transférer de l'argent sur le mauvais numéro de compte bancaire.

Pour conclure, lorsque la signature est vérifiée avec succès, cela signifie que :

1. Le document provient uniquement d'Alice.
    
2. Le contenu du document n'a pas été modifié par un tiers.
    

Maintenant, vous avez appris le chiffrement symétrique, le chiffrement asymétrique, les fonctions de hachage cryptographique et les signatures numériques. C'est génial !

Nous avons construit une base vraiment solide. Maintenant, comprendre l'authentification SSH va être beaucoup plus facile pour vous.

## Comment fonctionne l'authentification SSH

Si vous n'avez pas configuré l'authentification SSH avec GitHub, alors après avoir terminé cet article, vous pouvez suivre [la documentation détaillée de GitHub sur la façon de le faire](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). Pour l'instant, restez ici jusqu'à la fin.

Le point crucial du processus de configuration est que vous créez une paire de clés publique et privée sur votre ordinateur local. Ensuite, vous téléchargez votre clé publique sur votre profil GitHub - et c'est tout !

Après avoir créé notre paire de clés publique-privée, dans Ubuntu, la paire de clés publique-privée est stockée dans le répertoire `~/.ssh`.

![Montrant ma clé publique depuis mon terminal.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735035539565/1f837d9b-9717-44fa-a5e0-5801276113df.png align="center")

L'image ci-dessus montre ma clé publique. J'ai téléchargé cette clé publique sur mon profil GitHub :

![Montrant les paramètres de mon profil GitHub où ma clé publique est téléchargée pour l'authentification SSH avec GitHub.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735035898284/1ef9133a-895b-4847-a7ac-6157fdcc3143.png align="center")

Maintenant, lorsque j'exécute `git push` ou toute autre commande qui veut communiquer avec GitHub, je serai authentifié en utilisant l'authentification SSH.

![L'illustration du processus d'authentification SSH entre le client et le serveur GitHub.](https://cdn.hashnode.com/res/hashnode/image/upload/v1735053545173/6fb293f1-f90a-4b64-b026-082d8676afae.png align="center")

SSH est un protocole client-serveur. Notre ordinateur qui exécute `git push` est le client SSH. GitHub est le serveur SSH.

Le client commence le processus d'authentification en récupérant d'abord notre clé publique que nous avons dans `~/.ssh`.

Le client prépare ensuite un message qui contient notre clé publique. Ensuite, le client génère la signature en utilisant la clé privée correspondante.

La clé publique et la signature sont envoyées à GitHub. À la réception de ce message, GitHub fait deux choses :

Premièrement, il vérifie si la clé publique mentionnée dans le message est connectée à un profil GitHub ou non. Puisque nous téléchargeons notre clé publique sur GitHub, cette étape est validée avec succès.

Deuxièmement, GitHub vérifie la signature en utilisant la clé publique que nous avons téléchargée.

Nous avons appris que si la vérification de la signature s'avère réussie, cela signifie que seule la personne qui est en possession de la clé privée correspondante aurait pu envoyer le message.

Puisque nous sommes les seuls à avoir la clé privée liée à la clé publique téléchargée, cela prouve à GitHub que c'est bien nous qui tentons de communiquer avec GitHub et non un attaquant.

Maintenant, GitHub est sûr à 100 % que nous sommes la bonne personne, nous sommes authentifiés avec succès, et notre `git push` est autorisé à se poursuivre.

Vous voyez, il est devenu si facile de comprendre l'authentification SSH puisque vous avez déjà appris les fondamentaux.

![Une bande dessinée xkcd représentant Cueball réfléchissant à partager sa clé privée. Un geste dangereux !](https://cdn.hashnode.com/res/hashnode/image/upload/v1735120630613/e9a8bbba-3cc4-43e7-8369-865ab377fb87.png align="center")

L'image ci-dessus provient de la populaire [bande dessinée xkcd](https://xkcd.com/1553/). Le personnage là-bas (nommé Cueball) pense à révéler sa clé privée. J'espère que vous savez maintenant pourquoi il est mauvais de révéler votre clé privée.

Si vous révèle votre clé privée, quelqu'un d'autre pourrait s'authentifier sur GitHub en votre nom. Vous ne voulez pas que cela arrive, n'est-ce pas ? ;)

Donc, assurez-vous toujours de garder votre clé privée pour vous seul.

## Conclusion

Si vous avez lu jusqu'ici, alors Félicitations 🥳.

Vous avez appris comment l'authentification SSH fonctionne réellement - lorsque la signature a été vérifiée avec succès par GitHub, cela confirme à GitHub que c'est bien nous qui lui parlons et non un attaquant.

En cours de route, vous avez construit une compréhension fondamentale du chiffrement symétrique, du chiffrement asymétrique, des fonctions de hachage cryptographique et des signatures numériques.

Merci d'avoir été avec moi sur ce sujet, j'espère que vous partez avec de nouveaux apprentissages précieux.

Je mets des idées et des ressources utiles sur mon Twitter. [**Vous devriez me suivre là-bas.**](https://twitter.com/vkwebdev) Je respecterai votre temps.