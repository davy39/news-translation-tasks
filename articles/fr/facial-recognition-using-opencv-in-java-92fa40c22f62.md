---
title: Reconnaissance faciale avec OpenCV en Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-25T15:29:37.000Z'
originalURL: https://freecodecamp.org/news/facial-recognition-using-opencv-in-java-92fa40c22f62
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fpDngO6lM5pDeIPOOezK1g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Computer Vision
  slug: computer-vision
- name: Java
  slug: java
- name: opencv
  slug: opencv
- name: technology
  slug: technology
seo_title: Reconnaissance faciale avec OpenCV en Java
seo_desc: 'By Manish Bansal

  Ever since the Artificial Intelligence boom began — or the iPhone X advertisement
  featuring the face unlock feature hit TV screens — I’ve wanted to try this technology.
  However, once I started googling about it, I typically only foun...'
---

Par Manish Bansal

Depuis que le boom de l'Intelligence Artificielle a commencé — ou que la publicité pour l'iPhone X présentant la fonction de déverrouillage par reconnaissance faciale a envahi les écrans de télévision — j'ai voulu essayer cette technologie. Cependant, une fois que j'ai commencé à faire des recherches sur Google, je n'ai généralement trouvé que des exemples de code en Python. Et étant un passionné de Java depuis sept ans, j'ai été démotivé en voyant cela. Par conséquent, j'ai finalement décidé de partir à la recherche de bibliothèques Java open source pour cela.

Actuellement, il existe diverses bibliothèques Java. Mais la plus populaire que j'ai trouvée est [OpenCV](https://github.com/opencv/opencv).

OpenCV est une bibliothèque de vision par ordinateur open source qui possède des tonnes de modules comme la détection d'objets, la reconnaissance faciale et la réalité augmentée. Bien que cette bibliothèque soit écrite en C++, elle propose également des liaisons Java éprouvées.

Cependant, il y a un problème. Dans le cadre de sa version logicielle, elle ne propose que quelques modules (avec des liaisons Java) prêts à l'emploi — et la reconnaissance faciale n'en fait pas partie. Par conséquent, pour l'utiliser, vous devez la compiler manuellement.

**Attendez ! Quoi ? Pourquoi ?**

Oui — la raison invoquée par la communauté OpenCV est que les modules ne sont pas complètement stables. Par conséquent, ils ne sont pas inclus dans la version standard. C'est pourquoi ils les maintiennent dans un dépôt séparé [ici](https://github.com/opencv/opencv_contrib).

Si vous n'avez aucune ou très peu d'expérience en C++ (comme moi), vous devez déjà commencer à avoir le vertige à l'idée de compiler vous-même une bibliothèque C++. Mais ne vous inquiétez pas, je suis là pour vous tenir la main et vous guider à travers ce processus fastidieux. Alors, commençons, voulez-vous ?

### Compiler OpenCV pour Java à partir de zéro

![Image](https://cdn-media-1.freecodecamp.org/images/UPSASYdL1mTRl1Y2WO8wo5ORbKIVlJ0SZ4zp)
_« Oiseaux volant autour d'un bâtiment à moitié construit et d'un chantier de construction » par [Unsplash](https://unsplash.com/@danist07?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">贝莉儿 NG</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Vous pouvez trouver diverses ressources pour des instructions étape par étape comme [celle-ci](https://opencv-java-tutorials.readthedocs.io/en/latest/01-installing-opencv-for-java.html#install-opencv-3-x-under-windows), [celle-là](https://www.learnopencv.com/install-opencv3-on-windows/), et [celle-ci](https://perso.uclouvain.be/allan.barrea/opencv/cmake_config.html). Cependant, aucune d'entre elles n'a parfaitement fonctionné pour moi, car il manquait toujours une chose ou une autre. La plus proche que j'ai trouvée, et qui m'a aidé, est [celle-ci](https://opencv-java-tutorials.readthedocs.io/en/latest/01-installing-opencv-for-java.html#install-opencv-3-x-under-linux). Cependant, vous n'avez pas besoin de vous y référer. Vous pouvez suivre les étapes ci-dessous et tout ira bien.

Tout d'abord, vous devez disposer des logiciels ci-dessous sur votre PC. Ici, je compile une version 64 bits de la bibliothèque car je possède un PC 64 bits. Mais vous pouvez également la compiler pour du 32 bits.

Les logiciels requis sont :

1. [Cmake](https://cmake.org) (j'ai utilisé la version 3.6.0 rc-4).
2. [Ant](https://ant.apache.org) (utilisé en interne pour la création du JAR)
3. MinGW — W64 GCC-8.1.0
4. [JDK 1.8 64 bits](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

**Un mot sur MinGW :** Ici, pour compiler cette bibliothèque, nous avons besoin de compilateurs C++. Vous pouvez utiliser les outils Visual Studio (VS), ce qui est bien mieux. Cependant, je n'ai pas eu le luxe de le faire, car je l'ai compilé sur mon ordinateur portable professionnel et VS est un logiciel sous licence non disponible pour les développeurs Java ici. Par conséquent, j'ai dû utiliser des outils open source, et le meilleur est MinGW (Minimalist GNU for Windows).

De plus, il est très important d'utiliser la version correcte de MinGW. Téléchargez la version [x86_64-posix-seh](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z), car il y a un support des threads dans cette version. Je n'ai pas essayé toutes les autres versions. Mais la version [x86_64-win32-sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-win32/sjlj/x86_64-8.1.0-release-win32-sjlj-rt_v6-rev0.7z) ne fonctionne pas du tout.

Pour donner un peu plus de perspective, la compilation est effectuée par l'utilitaire appelé **make** qui fait partie de MinGW (bin/mingw32-make.exe). make est un exécuteur de tâches pour le C++ comme « Ant » l'est pour Java. Mais le code C++ et les scripts make sont très dépendants de la plateforme. Par conséquent, pour rendre les fichiers distribuables indépendants de la plateforme, l'utilitaire **CMake** est utilisé. CMake génère des scripts make dépendants de la plateforme.

### **Générer des configurations de build à l'aide de CMake**

**Étape 1 :** Téléchargez le zip du code source d' [opencv](https://github.com/opencv/opencv/releases) et d' [opencv_contrib](https://github.com/opencv/opencv_contrib/releases), et extrayez-les dans un répertoire. Ensuite, créez un dossier appelé « build » dans le même répertoire (j'ai créé « build_posix » comme on peut le voir dans les captures d'écran).

**Étape 2 :** Ouvrez CMake. Pointez « where is the source code » vers le dossier opencv extrait. Ensuite, pointez « where to build the binaries » vers le dossier « build » que vous avez créé.

![Image](https://cdn-media-1.freecodecamp.org/images/3w-kaNsw1jy-wgJj27ivlgUpkB3nWbKhmSAg)

**Étape 3 :** Ajoutez le dossier bin du JDK 1.8 64 bits, le dossier bin de MinGW et le dossier bin d'Ant aux variables d'environnement « PATH ». C'est important, car CMake cherchera dans les variables d'environnement pour la configuration. Si cela n'est pas fait, nous devrons configurer CMake manuellement à l'étape 5.

**Si vous avez plusieurs JDK sur votre système et que vous avez déjà un JDK différent dans le « PATH » et que vous ne voulez pas ajouter le JDK 1.8 dans le « PATH », vous pouvez ignorer cela. Mais configurez-le manuellement à l'étape 5.**

**Étape 4 :** Appuyez sur le bouton « Configure », sélectionnez « MinGw Makefiles » et « finish ». Après cela, CMake commencera à configurer votre projet. Cela prendra un certain temps et, une fois la configuration terminée, il affichera les configurations actuellement disponibles.

Au cas où vous vous demanderiez si les configurations générées pour vous sont correctes, vous pouvez vous référer aux journaux qui ont été générés pour moi [ici](https://pastebin.com/50rtPkt6) et comparer.

![Image](https://cdn-media-1.freecodecamp.org/images/1yaCLCiHsbLeyhIyjrWmIfMJfH2VO0bXcdk9)

**Étape 5 :** Vient maintenant la partie la plus importante — modifier les configurations. Tout d'abord, cochez les cases « Grouped » et « Advanced » pour organiser les configurations.

![Image](https://cdn-media-1.freecodecamp.org/images/HNOpUBXPSjKz6lJcJiTQcZxlxLPWVRSD6yKR)

* Vérifiez que ANT_EXECUTABLE (recherchez « ANT_EXECUTABLE » dans la zone de recherche) et les cinq configurations « JAVA » pointent vers le JDK 1.8 64 bits. Si l'étape 3 a été effectuée correctement, alors ce sera correct. Sinon, corrigez-les.

![Image](https://cdn-media-1.freecodecamp.org/images/zKNLlpIu8mRydVeelgHNLs4CevTolRnHxTrP)

* Décochez les cases liées à Python (recherchez « Python ») sous les groupes « BUILD » et « INSTALL » car nous n'avons pas besoin des builds Python.

![Image](https://cdn-media-1.freecodecamp.org/images/zXNIv3AOYlE5jS7KKgBm3Gkp7rBZA2PfrGkS)

* Désactivez « WITH_MSMF » et « WITH_IPP & WITH_TBB ». Ces bibliothèques ne sont disponibles que pour VS.
* Modifiez « OPENCV_EXTRA_MODULES_PATH » sous le groupe « OPENCV » et réglez-le sur le dossier « modules » sous le dossier source « opencv_contrib » que vous avez extrait précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/Vxz1vQr2-CoYNCn2HMyrkN0FjuI6pvTEZlOm)

Après cela, appuyez à nouveau sur le bouton « Configure ». Cela effectuera les configurations finales. Vous pouvez vous référer aux journaux qui ont été générés pour moi [ici](https://pastebin.com/B71iVjQT).

**Note** : Assurez-vous de comparer vos journaux « Configure » générés avec ceux que j'ai partagés dans le pastebin ci-dessus. Si vous trouvez une différence **majeure**, essayez d'abord de corriger vos configurations et appuyez à nouveau sur « Configure ». Sinon, il y a des chances que votre build échoue et qu'il soit plus difficile à déboguer.

**Étape 6 :** Après cela, appuyez sur « Generate ». Cela prendra quelques secondes, puis fermez CMake.

### **Compiler OpenCV**

Maintenant, si toutes les configurations générées ci-dessus sont correctes, cette tâche sera un jeu d'enfant (de 2 à 3 heures !). Ouvrez simplement l'invite de commande, allez dans le dossier « build » et exécutez la commande ci-dessous.

```
mingw32-make.exe  -j5 > buildLogs.txt
```

Ici, `-j5` est ajouté, ce qui demande à l'utilitaire make d'exécuter cinq tâches en parallèle. Cela rendra votre build plus rapide, du moins théoriquement.

De plus, n'oubliez pas d'envoyer les journaux vers un fichier texte. Ceux-ci pourraient devenir trop volumineux, auquel cas la fenêtre de votre invite de commande pourrait les tronquer. Vous en aurez besoin au cas où la compilation échouerait. Vous pouvez vous référer aux journaux de compilation générés dans mon cas [ici](https://pastebin.com/r7RSXSDm).

**Note** : L'ordre des instructions du journal peut ne pas être le même pour vous, car le build se déroule sur cinq threads parallèles.

Une fois le build terminé, vous pouvez vérifier les dossiers « bin » et « lib » à l'intérieur de votre répertoire « build ». Dans « bin », vous aurez tous vos fichiers opencv*.exe et libopencv*.dll ainsi que votre JAR compilé. De plus, « lib » contiendra votre DLL principale (libopencv_javaxxx.dll) ainsi que d'autres fichiers dépendants.

![Image](https://cdn-media-1.freecodecamp.org/images/mIygBsHnPC5flruoL8nFf3yEAF7P96QMYh6l)
_Dossier « bin » après une compilation réussie_

![Image](https://cdn-media-1.freecodecamp.org/images/ORUBTFMX5NhE0AjRxAfiLfoTAW4o3OnDR1VX)
_Dossier « lib » après une compilation réussie_

### Prise en main de l'API de reconnaissance faciale OpenCV

![Image](https://cdn-media-1.freecodecamp.org/images/e3jIAxwvVbVXoR2L0sOeAUQ352nzncBolZYX)
_Photo par [Unsplash](https://unsplash.com/@rawpixel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Maintenant que vous avez compilé la bibliothèque, vous devez d'abord configurer les variables d'environnement, ainsi que la bibliothèque utilisateur, dans Eclipse.

1. Créez une variable OPENCV_JAVA_BIN et pointez-la vers le dossier « bin » généré à l'intérieur de votre répertoire « build ».
2. Créez OPENCV_JAVA_LIB et pointez-la vers le dossier « lib » généré à l'intérieur de votre répertoire « build ».
3. Ajoutez ces deux variables à la variable « PATH ».
4. Ouvrez votre Eclipse et créez une nouvelle bibliothèque utilisateur que vous utiliserez pour votre projet de reconnaissance faciale. Allez dans « Window » > « Preferenc**es** ». Dans le menu, naviguez sous « Java » > « Build Path » > « User Libraries » et choisissez « New… ». Entrez un nom pour la bibliothèque — par exemple, opencv — et sélectionnez la bibliothèque utilisateur nouvellement créée. Choisissez « Add External JARs… », et parcourez pour sélectionner « opencv-3xx.jar » sur votre ordinateur.

Après cela, il n'est **pas nécessaire** de lier la bibliothèque native, car elle a été ajoutée à vos variables « path » à l'étape 3.

Une fois cette configuration terminée, vous pouvez cloner mon dépôt Git [ici](https://github.com/manishbansal8843/Opencv-facerec-java) et importer le projet dans votre espace de travail Eclipse. De plus, vous devrez ajouter le JDK 1.8 ainsi que la bibliothèque utilisateur opencv (que vous venez de créer) à ce projet. Une fois cela fait, vous serez prêt à tester votre bibliothèque OpenCV nouvellement compilée.

Au moment d'écrire ces lignes, il y a trois programmes dans ce projet.

* **HelloWorld** : vous pouvez l'exécuter pour tester si la configuration de votre bibliothèque OpenCV est correcte. Si cela ne fonctionne pas correctement, vous devez régler ce problème **en premier**. Les seuls problèmes que vous rencontrerez à ce stade seront liés aux variables d'environnement du système ou à la configuration de la bibliothèque utilisateur.
* **FaceDetection** : vous pouvez l'utiliser pour tester le module de détection de visage. C'est un module différent de la reconnaissance faciale. C'est un module qui est livré avec la version standard d'OpenCV. Au moment d'écrire ces lignes, nous pouvons fournir une image en entrée au programme, et il détectera tous les visages à l'intérieur de l'image. L'image de sortie comporte des rectangles verts dessinés sur tous les visages détectés.

![Image](https://cdn-media-1.freecodecamp.org/images/TzyLTh-v5ie9SpRVJH2rHyK3OPSpSHpvYWFJ)
_Image d'entrée pour le programme de détection de visage_

![Image](https://cdn-media-1.freecodecamp.org/images/csQYwDeXAiOBbv6AWCOxhlLMvqZ1wyaf0GRz)
_Image de sortie du programme de détection de visage_

* **FaceRecognition :** le module facerec d'OpenCV comprend trois algorithmes :

1. Eigenfaces
2. Fisherfaces
3. Local Binary Patterns Histograms.

Pour les détails techniques sur tous ces algorithmes, vous pouvez vous référer à [cet](https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html) article officiel. À des fins de démonstration, je vais vous montrer comment utiliser l'algorithme Eigenfaces.

Tout d'abord, vous devez [télécharger](http://www.cl.cam.ac.uk/Research/DTG/attarchive/pub/data/att_faces.zip) les données d'entraînement de la base de données de visages. Ces données contiennent dix images différentes pour chacun des 40 sujets distincts (400 images). Pour certains sujets, les images ont été prises à des moments différents, en variant l'éclairage, les expressions faciales (yeux ouverts / fermés, souriant / ne souriant pas) et les détails du visage (lunettes / pas de lunettes). Après les avoir extraites sur votre ordinateur, vous devez préparer un fichier .csv contenant le chemin de chaque image, ainsi que leur étiquette correspondante.

Pour faciliter les choses, j'ai un fichier TrainingData.txt dans mon dépôt Git. Cependant, vous devez modifier le fichier et altérer les chemins des images selon l'emplacement du répertoire sur votre ordinateur.

**Note** : la base de données de visages téléchargée contient des images au format .pgm. Ce format n'est **pas supporté** par Windows. Pour les convertir réellement en .jpg, j'ai ajouté PGMToJPGConverter à mon dépôt. Vous pouvez l'utiliser pour convertir les images et avoir un aperçu réel des données d'entraînement.

Après cela, vous pouvez exécuter le programme de reconnaissance faciale. Voici les étapes effectuées dans le programme :

1. La bibliothèque OpenCV est [chargée](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L20) comme d'habitude.
2. Le fichier .csv est lu, et deux ArrayList sont [créées](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L24). Une pour la matrice d'images et l'autre pour leurs étiquettes correspondantes.
3. Sur les 400 images d'entrée, la dernière entrée de la structure de données de la liste est [supprimée et sauvegardée](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L26-L29) pour tester le modèle entraîné plus tard.
4. Après cela, les 399 images restantes sont utilisées pour [entraîner](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L34) l'algorithme Eigenfaces.
5. Une fois l'entraînement terminé, on demande au modèle de [prédire](https://github.com/manishbansal8843/Opencv-facerec-java/blob/0d56b0a369e33a09e8af52613dbd79afdccad397/src/com/demo/facerecognition/FaceRecognitionEigenFaces.java#L39) l'étiquette de l'image que nous avons supprimée à l'étape 3.

![Image](https://cdn-media-1.freecodecamp.org/images/3h2mUCWnXzKQeFfIMJpFMIGxLoAM80Bp6tP0)
_Sortie du programme de reconnaissance faciale_

Ici, nous pouvons observer que l'algorithme est capable de prédire l'étiquette de notre sujet de test avec une valeur de confiance de 1807. Plus la valeur est basse, meilleure est la prédiction. De même, vous pouvez effectuer cet exercice avec deux autres algorithmes. Le code C++ peut être téléchargé [ici](https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html#fisherfaces-in-opencv) et [ici](https://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html#local-binary-patterns-histograms-in-opencv).

> **Mise à jour (27 déc. 2018)** : Au cas où vous trouveriez la compilation des liaisons Java d'OpenCV pénible, j'ai une bonne nouvelle pour vous. Récemment, j'ai trouvé un moyen plus simple d'obtenir toutes les dépendances OpenCV pour Java. Pour plus de détails, veuillez vous référer à mon [autre article](https://medium.com/@manishbansal8843/face-recognition-using-opencv-in-java-updated-8fc329863e52).

**Félicitations** !! ? Vous êtes arrivé au bout. Et si vous avez aimé ? cet article, cliquez sur le bouton clap ci-dessous ?. Cela compte beaucoup pour moi et cela aide d'autres personnes à voir l'histoire.