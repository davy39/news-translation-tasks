---
title: Qu'est-ce que la stéganographie ? Comment cacher des données dans des données
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2023-07-13T17:15:06.000Z'
originalURL: https://freecodecamp.org/news/what-is-steganography-hide-data-inside-data
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-cottonbro-4966171.jpg
tags:
- name: Cryptography
  slug: cryptography
- name: cybersecurity
  slug: cybersecurity
- name: data
  slug: data
seo_title: Qu'est-ce que la stéganographie ? Comment cacher des données dans des données
seo_desc: 'Ladies and Gentlemen, welcome to the world of Spies 🕵️.

  In the movie Uncharted (great movie by the way), Tom Holland and his brother have
  a secret form of communication. They would write a message on a plain postcard with
  special ink that became inv...'
---

Mesdames et Messieurs, bienvenue dans le monde des espions 🕵️.

Dans le film Uncharted (un excellent film au passage), Tom Holland et son frère ont une forme secrète de communication. Ils écrivaient un message sur une carte postale ordinaire avec une encre spéciale qui devenait invisible, puis l'envoyaient à l'autre personne. 

De l'extérieur, cela ressemblait à une autre vieille carte postale ordinaire. Mais si un briquet était allumé juste derrière le papier, l'encre réapparaissait et un nouveau message était découvert 🔥. 

C'est l'un des trucs les plus cool pour cacher des informations vus dans les films. Mais que se passerait-il si nous pouvions faire cela sur des ordinateurs ?

Eh bien, il s'avère que nous pouvons plus ou moins le faire. En utilisant la stéganographie.

**Avertissement : Ce concept peut être utilisé à la fois pour le bien et le mal. Le contenu de cet article est à des fins éducatives uniquement et ne doit pas être utilisé pour faire des farces, ou nuire aux personnes et aux infrastructures.**

Et avec cela en tête, voici ce que nous allons explorer dans cet article :

1. Qu'est-ce que la stéganographie ?
2. Types de stéganographie – Texte, Image, Vidéo, Audio, Réseau
3. Stéganographie d'image en utilisant Steghide

## Qu'est-ce que la stéganographie ?

La stéganographie est l'art de cacher des données secrètes en pleine vue. Cela semble un peu contre-intuitif, mais vous seriez surpris de voir à quel point c'est efficace. 

Cacher des choses comme le code source, les mots de passe, les adresses IP et d'autres informations confidentielles dans des images, de la musique ou d'autres fichiers aléatoires tend à être le dernier endroit où quelqu'un penserait à les trouver.

Vous devez noter que la stéganographie et la cryptographie ne sont pas mutuellement exclusives l'une de l'autre. L'une peut contenir des éléments de l'autre ou des deux. Par exemple, vous pourriez effectuer de la stéganographie avec un algorithme de chiffrement ou un mot de passe, comme vous le découvrirez bientôt.

## Types de stéganographie

Il existe divers types de stéganographie, et nous en examinerons cinq dans ce tutoriel.

### Stéganographie de texte

Cette forme implique de cacher un message dans un texte. Une méthode courante pour cela est la substitution. Elle implique de remplacer certains caractères par d'autres et ensuite de les substituer pour récupérer les données originales. 

Par exemple, prenez le texte suivant.

```markdown
Thi follow eng tixt contaens a sicrit missagi

```

Cela n'a pas vraiment de sens, n'est-ce pas ? Mais que se passerait-il si nous remplacions les i par des e et les e par des i ?

```markdown
The follow ing text contains a secret message

```

Je pense que c'est un peu plus facile à lire. C'est un exemple assez simple, mais il en existe des beaucoup plus compliqués et même certains que vous pourriez inventer vous-même.

### Stéganographie d'image

Franchement, c'est mon préféré. Cela implique de cacher des données derrière des images numériques. Il existe diverses techniques pour la stéganographie d'image qui incluent la technique du bit le moins significatif, le masquage et le filtrage, et la transformation par codage et cosinus. 

Jetez un coup d'œil aux deux images ci-dessous et repérez la différence :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-75.png)
_Groot sur Linux § Crédit : Mercury_

En réalité, aucun humain sur terre ne peut dire la différence visuelle. Mais si vous regardez de plus près les détails du fichier...

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-76.png)
_Comparaison des images § Crédit : Mercury_

La seule différence est la taille des images. C'est parce que celle de droite cache 260 mots de texte. N'est-ce pas cool ?

### Stéganographie vidéo

Dans la stéganographie vidéo, vous pouvez littéralement cacher des vidéos entières à l'intérieur d'une autre vidéo. Les vidéos sont essentiellement une séquence d'images avec un audio qui joue à mesure que la séquence progresse. Ce type de stéganographie permet à chaque image vidéo de coder une image de celle que vous souhaitez cacher.

Cette technique peut également être utilisée pour cacher du texte comme démontré dans le logiciel [Steganosaurus](https://steganosaur.us) par James Ridgeway. Il montre comment cela fonctionne dans cette [vidéo](https://youtu.be/YhnlHmZolRM).

### Stéganographie audio

Ce type de stéganographie permet d'encoder des messages cachés à l'intérieur d'un fichier audio. Une technique courante utilisée ici est appelée Backmasking. Le Backmasking consiste à cacher un message dans le fichier audio et il ne peut être entendu que lorsqu'il est joué à l'envers.

Le célèbre rappeur, Eminem, a fait du backmasking dans la chanson 'Stimulate' en 2002.

### Stéganographie réseau

Cela est relativement rare, mais néanmoins, c'est une technique dans laquelle les messages sont transmis en les cachant dans le trafic réseau. Les messages pourraient être trouvés dans la charge utile ou les en-têtes des paquets de données lorsqu'ils sont capturés et analysés par le récepteur.

Maintenant, examinons comment faire de la stéganographie d'image.

## Stéganographie en utilisant Steghide

Steghide est un outil open source de stéganographie d'image qui utilise la méthode du bit le moins significatif (LSB) pour cacher des données dans les images. 

Les images sont composées de pixels, qui sont composés de bits. La profondeur de bits détermine combien de couleurs sont présentes dans une image. Plus la profondeur de bits est élevée, plus l'image tend à être colorée.

Ce que fait le LSB, c'est changer le dernier bit de chaque octet (ou pixel) dans l'image en un bit qui représente les données que vous souhaitez cacher. Cela change les données de l'image, mais si c'est fait correctement, ce n'est pas perceptible. Plus la profondeur de bits et la résolution sont élevées, plus de données peuvent être stockées dans l'image.

Maintenant que vous comprenez comment cela fonctionne, jouons un peu à cache-cache (sans jeu de mots 👀).

Tout d'abord, nous aurons besoin de quelques choses :

1. Un système d'exploitation Linux
2. Une connexion Internet
3. Une image
4. Un fichier texte

### Installer Steghide

Tout d'abord, nous devons installer Steghide. Ouvrez votre terminal et exécutez la commande suivante pour le faire :

```markdown
sudo apt install steghide

```

Vous pouvez toujours exécuter `steghide --help` pour obtenir la liste des commandes et voir toutes vos options.

### Préparez votre image

Ensuite, placez une image et un fichier texte dans un répertoire. Mes fichiers sont 'information.txt' et 'image.png'. J'ai également mis du texte dans le fichier à cacher dans l'image plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-77.png)
_Préparation des fichiers § Crédit : Mercury_

Ouvrez à nouveau votre terminal et allez dans le répertoire où vous avez stocké les fichiers. Le mien est dans `~/Documents/steganography_tutorial`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-78.png)
_Recherche des fichiers § Crédit : Mercury_

### Créez une nouvelle image

Ensuite, exécutez la commande suivante pour créer une nouvelle image qui contient le fichier texte que vous souhaitez cacher.

```markdown
steghide embed -ef <data> -cf <image> -sf <stego_image> -v

```

Examinons la commande :

* `steghide` – Nous spécifions l'outil à utiliser
* `embed` – Indique à l'outil que nous voulons intégrer des données
* `-ef` – Fichier à intégrer, spécifie le fichier à cacher
* `-cf` – Fichier de couverture, spécifie l'image de couverture
* `-sf` – Fichier stéganographique, crée une copie de l'image originale avec le fichier intégré
* `-v` – Verbose, nous donne plus d'informations sur le processus

Lorsque la commande est exécutée, il vous sera demandé d'entrer un mot de passe. Si vous souhaitez une couche supplémentaire de sécurité, vous pourriez vouloir faire cela. Si vous ne le souhaitez pas, appuyez simplement sur Entrée deux fois. Voici le résultat de ce que j'ai exécuté :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-79.png)
_Intégration des informations § Crédit : Mercury_

### Inspectez le nouveau fichier

Maintenant, examinons le nouveau fichier.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-80.png)
_Comparaison des images côte à côte § Crédit : Mercury_

Il semble n'y avoir aucune différence. Nous pouvons regarder de plus près avec un site appelé [diffchecker.com](https://www.diffchecker.com/image-compare/).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-81.png)
_Comparaison des détails des images § Crédit : Mercury_

### Extrayez les données

Le fichier stéganographique est légèrement plus grand que l'original car il contient des informations. Nous pouvons extraire les données du fichier stéganographique en utilisant la commande ci-dessous.

```markdown
steghide extract -sf <stego_image> -xf <extracted_data>

```

Passons en revue la commande ci-dessus :

* `-sf` – fichier stéganographique, l'image contenant des données cachées
* `-xf` – fichier extrait, le fichier avec les données extraites

Ci-dessous se trouve la capture d'écran de l'exécution de la commande. Le texte extrait est également montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-82.png)
_Extraction des informations § Crédit : Mercury_

Si vous avez extrait le texte, félicitations 🎉🎊. Vous avez réussi à cacher et à extraire le texte de l'image. Vous pouvez faire cela avec un certain nombre de choses, même des livres entiers.

En utilisant un outil différent appelé Stegcore, j'ai caché un fichier texte contenant le nouveau livre de Quincy Larson, « **[Comment apprendre à coder et obtenir un emploi de développeur](https://www.freecodecamp.org/news/learn-to-code-book/)** », derrière une image du livre 📝.

Voici un extrait du livre.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-83.png)
_Un extrait du livre § Crédit : Quincy Larson_

Et comme avant, le texte a été intégré dans une nouvelle image. Voici l'image originale et l'image stéganographique côte à côte.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-84.png)
_L'image originale comparée à l'image stéganographique § Crédit : Mercury_

Et comme prévu, l'image stéganographique est légèrement plus grande que l'originale.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-85.png)
_Les détails des images côte à côte § Crédit : Mercury_

Parler de cacher un livre derrière un livre (mauvaise blague, je sais 🤧). Si vous voulez l'essayer, vous pouvez consulter le dépôt Github [repository](https://github.com/elementmerc/Stegcore) ou l'[application](https://sourceforge.net/projects/stegcore/).

## Conclusion

Vous avez appris ce qu'est la stéganographie et comment la mettre en œuvre en utilisant des outils. Gardez à l'esprit que la stéganographie est un outil et peut être utilisée à la fois pour le bien et le mal. Les entreprises peuvent cacher des informations sensibles en utilisant ces moyens. D'un autre côté, un pirate pourrait l'utiliser pour cacher du code malveillant.

Une fois de plus, ce tutoriel est à des fins éducatives uniquement et doit être utilisé pour aider et défendre les informations contre les pirates informatiques black hat. Restez en sécurité dans la jungle en ligne et bon piratage 🤓.

### **Remerciements**

Merci à [Anuoluwapo Victor](https://twitter.com/Anuoluwap__o), [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Favour Ojo](https://www.linkedin.com/in/favour-ojo-906883199/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), et ma famille pour l'inspiration, le soutien et les connaissances utilisées pour mettre cela ensemble. Je vous apprécie tous.

Si vous voulez des articles similaires à celui-ci, contactez-moi sur [Upwork](https://www.upwork.com/freelancers/~01b1dea916f784d554) ou lisez plus de mes articles [ici](https://flipboard.com/@elementmerc).

Crédit de l'image de couverture : Abstract Data Cube § Crédit : [Shubham Dhage](https://unsplash.com/@theshubhamdhage?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).