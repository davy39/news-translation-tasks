---
title: Comment craquer des haches avec Hashcat — un guide pratique de pentesting
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2022-12-08T15:55:26.000Z'
originalURL: https://freecodecamp.org/news/hacking-with-hashcat-a-practical-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/hashcat-1.png
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: Linux
  slug: linux
- name: penetration testing
  slug: penetration-testing
seo_title: Comment craquer des haches avec Hashcat — un guide pratique de pentesting
seo_desc: 'Hashing is one of the pillars of cybersecurity. From securing passwords
  to sensitive data, there are a variety of use cases for hashing.

  Hashing is often confused with encryption. A simple difference is that hashed data
  is not reversible. Encrypted d...'
---

Le hachage est l'un des piliers de la cybersécurité. De la sécurisation des mots de passe aux données sensibles, il existe une variété de cas d'utilisation pour le hachage.

Le hachage est souvent confondu avec le chiffrement. Une simple différence est que les données hachées ne sont pas réversibles. Les données chiffrées peuvent être inversées à l'aide d'une clé. C'est pourquoi des applications comme Telegram utilisent le chiffrement tandis que les mots de passe sont hachés.

Dans cet article, nous allons examiner l'installation et le travail avec [Hashcat](https://hashcat.net/hashcat/). Hashcat est un utilitaire en ligne de commande simple mais puissant qui nous aide à – vous l'avez deviné – craquer des haches.

Nous commencerons d'abord par examiner comment fonctionne le hachage en détail.

> _Note : Tous mes articles sont à des fins éducatives. Si vous utilisez_ ces informations _illégalement et que vous avez des ennuis, je ne suis pas responsable. Obtenez toujours la permission du propriétaire avant de scanner / forcer / exploiter un système._

## Qu'est-ce que le hachage de mot de passe ?

Le hachage est le processus de conversion d'une chaîne alphanumérique en une chaîne de taille fixe en utilisant une fonction de hachage. Une fonction de hachage est une fonction mathématique qui prend la chaîne d'entrée et génère une autre chaîne alphanumérique.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-14.png)
_Comment fonctionne le hachage_

Il existe de nombreux algorithmes de hachage comme MD5, SHA1, et ainsi de suite. Pour en savoir plus sur les différents algorithmes de hachage, [vous pouvez lire l'article ici](https://www.okta.com/identity-101/hashing-algorithms/#:~:text=A%20hashing%20algorithm%20is%20a,and%20decoded%20by%20anyone%20else.).

La longueur d'un hachage est toujours une constante, indépendamment de la longueur de l'entrée. Par exemple, si nous utilisons l'algorithme MD5 et hachons deux chaînes comme « Password123 » et « HelloWorld1234 », le hachage final aura une longueur fixe.

Voici le hachage MD5 pour « Password123 ».

```
42f749ade7f9e195bf475f37a44cafcb
```

Si nous utilisons la chaîne d'entrée « HelloWorld1234 », voici le résultat :

```
850eaebd5c4bb931dbb2bbcf7994c021
```

Il existe un algorithme similaire appelé encodage. Un algorithme d'encodage populaire est base64. Voici comment le même « Password123 » apparaîtra si nous l'encodons avec base64 :

```
UGFzc3dvcmQxMjM=
```

Alors, quelle est la différence entre le hachage et l'encodage ? Lorsque nous encodons une chaîne, elle peut être facilement décodée pour obtenir la chaîne source. Mais si nous hachons une chaîne, nous ne pourrons jamais obtenir la chaîne source (peut-être avec des ordinateurs quantiques, mais c'est un autre sujet de discussion).

Le hachage et l'encodage ont différents cas d'utilisation. Nous pouvons appliquer l'encodage pour masquer/simplifier des chaînes tandis que le hachage est utilisé pour sécuriser des données sensibles comme les mots de passe.

Si les hachages ne sont pas réversibles, comment comparer les chaînes ? Simple – nous comparons les hachages.

Lorsque nous nous inscrivons sur un site web, ils hacheront notre mot de passe avant de le sauvegarder (espérons-le !). Lorsque nous essayons de nous connecter à nouveau, le même algorithme de hachage est utilisé pour générer un hachage pour notre entrée. Il est ensuite comparé avec le hachage original sauvegardé dans la base de données.

Cette approche est également ce qui donne lieu à des attaques de hachage. Une manière simple d'attaquer les hachages est d'avoir une liste de mots de passe courants hachés ensemble. Cette liste est appelée une [table arc-en-ciel](https://en.wikipedia.org/wiki/Rainbow_table). Un nom intéressant pour une table de hachages.

Maintenant que nous savons comment fonctionne le hachage, regardons ce qu'est Hashcat.

## Qu'est-ce que Hashcat ?

Hashcat est un outil rapide de récupération de mots de passe qui aide à casser des hachages de mots de passe complexes. C'est un outil flexible et riche en fonctionnalités qui offre de nombreuses façons de trouver des mots de passe à partir de hachages.

Hashcat est également l'un des rares outils qui peut fonctionner avec le GPU. Alors que les CPU sont excellents pour les tâches séquentielles, les GPU ont des capacités de traitement parallèle puissantes. Les GPU sont utilisés dans les jeux, l'intelligence artificielle, et peuvent également être utilisés pour accélérer le craquage de mots de passe.

Voici la [différence entre un CPU et un GPU](https://www.intel.in/content/www/in/en/products/docs/processors/cpu-vs-gpu.html) si vous souhaitez en savoir plus.

D'autres fonctionnalités notables de Hashcat incluent :

* Entièrement open source.
* Prise en charge de plus de 200 algorithmes de hachage.
* Prise en charge de Windows, Linux et Mac.
* Prise en charge du craquage de plusieurs hachages en parallèle.
* Système de benchmarking intégré.

Maintenant que nous savons ce qu'est Hashcat, allons l'installer.

## Comment installer Hashcat

Hashcat est préinstallé dans Kali et Parrot OS. Pour l'installer dans les systèmes basés sur Ubuntu/Debian, utilisez la commande suivante :

```
$ apt install hashcat
```

Pour l'installer sur un Mac, vous pouvez utiliser [Homebrew](https://brew.sh/). Voici la commande :

```
$ brew install hashcat
```

Pour les autres systèmes d'exploitation, une liste complète des instructions d'installation peut être [trouvée ici](https://hashcat.net/hashcat/https://hashcat.net/hashcat/).

Une fois l'installation terminée, nous pouvons vérifier le menu d'aide de Hashcat en utilisant cette commande :

```
$ hashcat -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-15.png)
_Menu d'aide de Hashcat_

En plus de Hashcat, nous aurons également besoin d'une liste de mots. Une liste de mots est une liste de termes couramment utilisés. Cela peut être une [liste de mots de mots de passe](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt), une [liste de mots de noms d'utilisateur](https://github.com/danielmiessler/SecLists/blob/master/Usernames/Names/names.txt), une liste de mots de sous-domaines, et ainsi de suite.

Une liste de mots de mots de passe populaire est [rockyou.txt](https://github.com/teamstealthsec/wordlists/blob/master/rockyou.txt.gz). Elle contient une liste de mots de passe couramment utilisés et est populaire parmi les testeurs de stylo. Vous pouvez trouver la liste de mots Rockyou sous /usr/share/wordlists dans Kali Linux.

## Comment travailler avec Hashcat

Maintenant que nous savons ce que sont le hachage et Hashcat, commençons à craquer quelques mots de passe.

Avant de craquer un hachage, créons quelques hachages avec lesquels travailler. Nous pouvons utiliser un site comme [Browserling](https://www.browserling.com/tools/all-hashes) pour générer des hachages pour des chaînes d'entrée.

Créons deux hachages : un hachage MD5 et un hachage SHA1 pour la chaîne « Password123 ». J'utilise un mot de passe faible pour vous aider à comprendre à quel point il est facile de craquer ces mots de passe.

Voici les hachages générés pour les chaînes d'entrée.

```
MD5 hash -> 42f749ade7f9e195bf475f37a44cafcb
SHA1 hash -> b2e98ad6f6eb8508dd6a14cfa704bad7f05f6fb1
```

Nous pouvons stocker ces hachages sous les noms md5.txt et sha1.txt pour les utiliser lorsque nous travaillons avec Hashcat.

Pour craquer un mot de passe en utilisant Hashcat, voici la syntaxe générale.

```
$ hashcat -m value -a value hashfile wordlist
```

Décortiquons la syntaxe. Nous avons utilisé deux drapeaux, `-m` et `-a`. Le drapeau `-m` est utilisé pour spécifier le type de hachage et le drapeau `-a` est pour spécifier le mode d'attaque. Vous pouvez trouver la [liste des types de hachage et des modes d'attaque ici](https://hashcat.net/wiki/doku.php?id=hashcat).

Craquons d'abord notre hachage md5. Nous allons craquer ce hachage en utilisant le mode Dictionnaire. Il s'agit d'une attaque simple où nous fournissons une liste de mots (RockYou) à partir de laquelle Hashcat générera et comparera les hachages.

Nous pouvons spécifier le mode de hachage comme « md5 » en utilisant la valeur 0. Mais Hashcat peut également identifier le type de hachage automatiquement pour les algorithmes de hachage courants.

Pour le mode d'attaque, nous utiliserons le mode dictionnaire (0) en utilisant le drapeau `-a`. Voici la commande complète :

```
$ hashcat -m 0 -a 0 md5.txt rockyou.txt
```

Hashcat trouvera rapidement la valeur du hachage, dans ce cas, « Password123 » :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-16.png)
_Craquage MD5 de Hashcat_

Cela semble simple, n'est-ce pas ? Maintenant, craquons notre hachage SHA. La valeur du mode de hachage pour SHA1 est 100. Voici la commande :

```
$ hashcat -m 100 -a 0 sha1.txt rockyou.txt
```

Et voici la sortie de Hashcat :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-17.png)
_Craquage SHA1 de Hashcat_

Hashcat prend en charge presque tous les algorithmes de hachage avec divers modes d'attaque. Regardons quelques modes d'attaque et voyons comment ils fonctionnent.

### Attaque par dictionnaire (-a 0)

Comme nous l'avons vu dans notre exemple ci-dessus, une attaque par dictionnaire est effectuée en utilisant une liste de mots. Une attaque par dictionnaire est également l'option par défaut dans Hashcat. Plus la liste de mots est bonne, plus les chances de craquer le mot de passe sont grandes.

### Attaque par combinateur (-a 1)

L'attaque par combinateur essaiera différentes combinaisons de mots de notre liste de mots. Par exemple, si notre liste de mots contient les mots « pass », « 123 » et « hello », Hashcat générera la liste de mots suivante.

```
passpass
pass123
passhello
123pass
123123
123hello
hellopass
hello123
hellohello
```

Comme vous pouvez le voir, l'utilisation d'une simple liste de mots peut nous donner un certain nombre de combinaisons. Cette attaque est idéale si nous connaissons certains termes qui pourraient être utilisés dans le mot de passe. Gardez à l'esprit que, plus la liste de mots initiale est grande, plus la liste de mots finale devient compliquée.

### Attaque par masque (-a 3)

L'attaque par masque est similaire à l'attaque par dictionnaire, mais elle est plus spécifique. Les approches par force brute comme les attaques par dictionnaire peuvent prendre beaucoup de temps pour craquer un mot de passe. Mais si nous avons des informations concernant le mot de passe, nous pouvons les utiliser pour accélérer le temps nécessaire pour craquer le mot de passe.

Par exemple, si nous connaissons la longueur du mot de passe et quelques caractères qui pourraient être dans le mot de passe, nous pouvons générer une liste de mots personnalisée avec ces caractères.

L'attaque par masque est hors de portée pour cet article, mais vous pouvez [en savoir plus sur les attaques par masque ici](https://hashcat.net/wiki/doku.php?id=mask_attackhttps://hashcat.net/wiki/doku.php?id=mask_attack).

En plus de ces types d'attaques courants, il existe d'autres modes d'attaque dans Hashcat. Cela inclut le mode hybride, l'attaque par permutation, l'attaque basée sur des règles, et ainsi de suite. Chacun de ces modes peut être utilisé pour des cas d'utilisation spécifiques et pour accélérer le craquage de mots de passe.

## Comment se défendre contre Hashcat

La première et évidente étape est de définir des mots de passe forts. Plus le mot de passe est fort, plus il est difficile à craquer. Vous pouvez vérifier si votre mot de passe a été [exposé sur Internet ici](https://haveibeenpwned.com/).

Une méthode plus efficace consiste à [ajouter des sels aux hachages de mots de passe](https://www.freecodecamp.org/news/why-a-little-salt-can-be-great-for-your-passwords/). Un sel est une chaîne supplémentaire ajoutée au mot de passe existant afin que le hachage généré soit différent du hachage normal d'une chaîne.

Par exemple, si une chaîne « sdf909 » est ajoutée à un mot de passe « Password123 », les attaques par table arc-en-ciel échoueront immédiatement car elles n'ont pas de hachages avec le sel ajouté.

Pour craquer un mot de passe salé, l'attaquant doit connaître à la fois les valeurs de hachage et de sel. Cela rend plus difficile le craquage des hachages en utilisant des méthodes telles que les tables arc-en-ciel.

Nous pouvons renforcer davantage le salage en utilisant des sels dynamiques au lieu de sels statiques. Nous pouvons écrire une fonction qui génère une valeur de sel pour chaque chaîne, rendant exponentiellement plus difficile le craquage d'un mot de passe salé.

Vous pouvez [lire cet article](https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/) pour en savoir plus sur le fonctionnement des sels dans le hachage des mots de passe.

## Résumé

Le hachage est la méthode d'utilisation d'une fonction mathématique pour générer une chaîne aléatoire. C'est une fonction à sens unique et aide à sécuriser des données telles que les mots de passe des utilisateurs.

Hashcat est un outil puissant qui aide à craquer les hachages de mots de passe. Hashcat prend en charge la plupart des algorithmes de hachage et peut fonctionner avec une variété de modes d'attaque.

Pour renforcer la sécurité et protéger les hachages contre les attaques, utilisez des mots de passe forts et des sels avant de hacher les mots de passe.

_Aimé cet article ? Rejoignez_ [_Stealth Security Weekly Newsletter_](https://tinyletter.com/stealthsecurity) _et recevez des articles livrés dans votre boîte de réception chaque vendredi. Vous pouvez également_ [_vous connecter avec moi_](https://www.linkedin.com/in/manishmshiva/) _sur Linkedin._