---
title: La mise à jour vers macOS Sierra rendra vos clés SSH inutilisables et vous
  bloquera hors de vos propres serveurs.
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2016-10-11T00:54:24.000Z'
originalURL: https://freecodecamp.org/news/upgrading-to-macos-sierra-will-break-your-ssh-keys-and-lock-you-out-of-your-own-servers-f413ac96139a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4BPoUrWcf67bdaKyZPARMg.png
tags:
- name: Apple
  slug: apple
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: La mise à jour vers macOS Sierra rendra vos clés SSH inutilisables et vous
  bloquera hors de vos propres serveurs.
seo_desc: 'Do not upgrade to macOS Sierra if you have a cloud server (AWS, Digital
  Ocean, etc.) Read this post first. It will walk you through safely updating to Sierra
  and updating your SSH keys.

  Like many developers, I got a notice from Apple bugging me to in...'
---

Ne mettez pas à jour vers macOS Sierra si vous avez un serveur cloud (AWS, Digital Ocean, etc.). Lisez d'abord cet article. Il vous guidera pour mettre à jour en toute sécurité vers Sierra et mettre à jour vos clés SSH.

Comme beaucoup de développeurs, j'ai reçu une notification d'Apple me demandant d'installer son nouveau macOS Sierra. J'ai cliqué sur « me rappeler demain » pendant quelques jours. Puis j'ai finalement cédé une nuit avant d'aller me coucher.

Quand je me suis réveillé, je n'étais plus en mesure d'accéder aux serveurs de Free Code Camp. Il m'a fallu un certain temps pour réaliser ce qui s'était passé. Heureusement, [BerkeleyTrue](https://www.freecodecamp.org/news/upgrading-to-macos-sierra-will-break-your-ssh-keys-and-lock-you-out-of-your-own-servers-f413ac96139a/undefined) n'avait pas encore mis à jour et a pu ajouter mes nouvelles clés SSH.

Il s'avère qu'Apple a décidé de forcer discrètement tout le monde à utiliser des clés RSA de 2048 bits, ce qui a été une légère gêne pour certains et une panique confuse pour d'autres.

Si vous vous demandez pourquoi les clés RSA sont plus sécurisées que les anciennes clés DSA, [elles ne le sont pas intrinsèquement](http://security.stackexchange.com/a/5100). Mais les clés DSA ne peuvent généralement être que de 1024 bits, tandis que les clés RSA peuvent être plus longues, ce qui est le cas avec les clés RSA de 2048 bits par défaut de Sierra. Ces bits supplémentaires rendent ces nouvelles clés substantiellement plus difficiles à craquer.

Configurons votre nouvelle clé SSH RSA de 2048 bits.

### Étape #1 : supprimez votre ancienne clé et créez une nouvelle

Tout d'abord, vérifions que vous avez bien besoin d'une nouvelle clé.

Ouvrez votre terminal et tapez :

```
ssh-keygen -l -f ~/.ssh/id_rsa.pub
```

Si l'invite répond avec une chaîne commençant par « 2048 SHA256 », vous avez terminé et n'avez pas besoin de prendre d'autres mesures.

Sinon, créez une nouvelle clé en exécutant :

```
ssh-keygen -t rsa
```

L'invite devrait répondre avec :

```
Generating public/private rsa key pair.Enter file in which to save the key (/Users/freecodecamp/.ssh/id_rsa):
```

Vous pouvez simplement appuyer sur Entrée pour l'enregistrer à l'emplacement par défaut. Notez que cela écrasera votre ancienne clé (inutilisable).

```
Enter passphrase (empty for no passphrase):
```

Vous pouvez laisser ce champ vide ou ajouter un mot de passe pour un peu plus de sécurité (et beaucoup plus de frappe).

Ensuite, vous obtiendrez un « art » aléatoire qui semble toujours avoir la forme d'un sapin de Noël :

![Image](https://cdn-media-1.freecodecamp.org/images/1*NkRrhr4WF93hhtIKS2eIrg.png)
_Ceci a été créé pour cet article — ce n'est pas celui que j'utilise._

Assurez-vous maintenant que votre clé a les bonnes permissions d'accès en exécutant :

```
sudo chmod 600 ~/.ssh/id_rsa
```

Vous pouvez vérifier le contenu de votre clé publique en exécutant :

```
cat ~/.ssh/id_rsa.pub
```

Ce qui devrait retourner quelque chose comme :

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDijWK+s3ybgzEdaJ5LneNU11BsIyoNS51SV11Vi5auPJW9+Ji6OUSJ9OguZh4T019ULyFF/Qq66fhH9TvMzw80lTNoChgTRMpjs2+Qg75yTINKSde+Gv4TK6UvNw6EINORcTpb32Im9hgtdTj6WqJ/hCbSltv7IfFZU5ChV7SxTaoNZTa9M5H3N8YdQ/aGt3puh222Cq5DTjV8fRWaNVvjVQRe/huHAHEzEUr1T/eTlXtoFtGeC1z+pLfYllVzizoS7tyuUksfgqox1jJJMpaZ25V/R/p/MDUc936za/8zgB8OQFRBbrP6JvXXN99DLcvs9coz9vfb2GCVrhxi1aJ5 quincy@FreeCodeCamp
```

Vous devrez placer cette clé sur votre serveur. Pour vous assurer de copier tout son contenu, je vous recommande de la copier directement dans votre presse-papiers en exécutant :

```
pbcopy < ~/.ssh/id_rsa.pub
```

### Étape #2 : ajoutez votre nouvelle clé publique à votre serveur

Si vous pouvez vous connecter en SSH à votre serveur sans votre clé, essayez d'obtenir un accès en utilisant un mot de passe si vous en avez un.

Sinon, vous devrez demander à quelqu'un d'autre qui a accès au serveur de le faire pour vous.

Si vous avez désactivé l'accès par mot de passe à votre serveur (ce que de nombreux experts recommanderaient pour des raisons de sécurité), vous pourrez peut-être [réactiver temporairement l'accès par mot de passe](http://jeffreifman.com/2016/10/01/fix-macos-sierra-upgrade-breaking-ssh-keys/).

Une fois que vous avez un accès root à votre serveur — en supposant qu'il s'agit d'un serveur Linux — vous devez simplement exécuter cette commande :

```
nano ~/.ssh/authorized_keys
```

Cela ouvrira votre fichier de clés autorisées en utilisant l'éditeur de texte minimaliste « nano » qui est inclus avec la plupart des distributions Linux. Ou vous pourriez utiliser Vim.

Ensuite, collez votre clé SSH publique de tout à l'heure. Appuyez sur contrôle+o pour enregistrer vos modifications, puis contrôle+x pour quitter nano.

Déconnectez-vous de votre serveur. Vous êtes maintenant prêt à essayer de vous connecter en utilisant votre nouvelle clé SSH.

### Étape #3 : connectez-vous en SSH à votre serveur

Exécutez cette commande pour vous connecter en SSH, en remplaçant root@0.0.0.0 par les informations de connexion et l'adresse IP de votre serveur :

```
ssh -i ~/.ssh/id_rsa root@0.0.0.0
```

Vous devriez obtenir un accès SSH normal à votre serveur, sans avoir besoin de saisir un mot de passe.

Félicitations ! Vous êtes de retour là où vous étiez hier, sauf qu'Apple ne vous ennuiera plus pour mettre à jour votre système d'exploitation. ?

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps. ?**