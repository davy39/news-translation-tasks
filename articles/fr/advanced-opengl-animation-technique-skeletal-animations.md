---
title: Technique d'animation OpenGL avancée – Animations squelettiques avec Assimp
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-03-15T15:37:21.000Z'
originalURL: https://freecodecamp.org/news/advanced-opengl-animation-technique-skeletal-animations
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/opengl.png
tags:
- name: openGL
  slug: opengl
- name: youtube
  slug: youtube
seo_title: Technique d'animation OpenGL avancée – Animations squelettiques avec Assimp
seo_desc: 'If you want your 3D animated characters to move in realistic-looking ways,
  you need to have a good understanding of skeletal animations.

  We just posted a full course on the freeCodeCamp.org YouTube channel well teach
  you how to do skeletal animations...'
---

Si vous voulez que vos personnages animés en 3D se déplacent de manière réaliste, vous devez avoir une bonne compréhension des animations squelettiques.

Nous venons de publier un cours complet sur la chaîne YouTube de freeCodeCamp.org qui vous apprendra comment réaliser des animations squelettiques avec OpenGL et la bibliothèque Assimp.

Etay Meiri a créé ce cours. Etay est ingénieur logiciel chez Intel et un excellent professeur.

Les personnages animés, que ce soit dans les jeux ou les vidéos, semblent plus organiques lorsqu'ils bougent leurs membres d'une certaine manière en marchant, courant ou attaquant. En implémentant correctement l'animation squelettique, les mouvements de vos personnages paraîtront plus vivants.

Dans ce cours, vous apprendrez à utiliser la bibliothèque Open Asset Import (Assimp) pour importer et exporter divers formats de modèles 3D.

D'abord, vous apprendrez à charger des modèles 3D avec Assimp. Ensuite, le cours comprend les parties suivantes :

* Partie 1 : Rigging, Skinning et Animation de modèles 3D
* Partie 2 : Mappage des sommets du modèle aux os
* Partie 3 : Matrices de transformation
* Partie 4 : Intégration des matrices Assimp dans la classe Skinned Mesh
* Partie 5 : Intégration des données d'animation dans la classe Skinned Mesh

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube de freeCodeCamp.org](https://youtu.be/GZQkwx10p-8) (2 heures de visionnage).

%[https://youtu.be/GZQkwx10p-8]

### Transcription

(générée automatiquement)

Dans ce cours OpenGL de niveau intermédiaire, Etay Meiri vous enseignera l'animation squelettique à l'aide de modèles 3D.

Bonjour, je m'appelle Etay, et je vous souhaite la bienvenue dans ce cours sur l'animation squelettique en OpenGL.

Si vous avez une certaine expérience avec OpenGL et que vous voulez apprendre à charger des fichiers de modèles 3D animés tels que le format FBX, utilisé dans Unity, alors ce cours est fait pour vous.

Le cours est composé de deux sections principales.

Dans la première, nous apprenons à charger des modèles à l'aide de la bibliothèque Assimp.

Et la deuxième section est en fait composée de cinq parties, où nous implémentons l'animation squelettique étape par étape. Je considère que le matériel présenté ici est de niveau intermédiaire.

Vous devriez donc être familier avec les transformations 3D courantes, la configuration des tampons de sommets (vertex buffers) et d'indices (index buffers), ainsi que l'écriture de shaders pour réaliser un éclairage de base.

Si vous avez besoin d'une mise à niveau sur ces sujets, vous trouverez des tutoriels de niveau débutant sur ma chaîne YouTube et sur mon site web, ainsi que des ressources d'autres créateurs. Bien sûr, vous trouverez des liens dans la description de la vidéo ci-dessous. Le langage de programmation du cours est le C++.

Vous devriez donc être familier avec celui-ci.

Mais ne vous inquiétez pas, vous n'avez pas besoin d'être un expert en C++.

J'utilise des éléments très basiques tels que les classes, et rien de trop complexe provenant de C++20 ou autre.

En termes de système d'exploitation :

J'utilise Linux comme système de développement principal.

Mais vous pouvez aussi utiliser Windows. Bien sûr, vous trouverez toutes les sources sur GitHub, et j'inclurai également des solutions Visual Studio.

Alors, sans plus attendre, commençons.

Bienvenue sur OGLDev. Il est assez clair qu'il y a une limite à la complexité d'un modèle créé manuellement.

Une pyramide, ça va.

Un cube, ça va aussi.

Mais lorsqu'il s'agit de modéliser quelque chose du monde physique, vous avez besoin d'aide.

C'est pourquoi nous avons des logiciels comme Blender, Maya, 3ds Max et bien d'autres outils qui vous permettent de créer des modèles dans un environnement 3D sophistiqué.

Avec de nombreux outils de support qui aident les artistes modeleurs à créer les mondes et objets 3D incroyables auxquels nous sommes habitués dans les jeux modernes.

Le logiciel de modélisation se charge de calculer la position, les coordonnées de texture et tout autre attribut de sommet dont vous pourriez avoir besoin.

Il regroupe également les sommets en triangles et gère les indices correspondants.

Et enfin, le logiciel de modélisation sauvegarde toutes ces données dans un fichier afin que vous puissiez charger le modèle dans votre jeu ou application et le manipuler en utilisant OpenGL ou toute autre API 3D.

Cela ne vous surprendra probablement pas de savoir que, puisqu'il existe de nombreux logiciels de modélisation 3D, nous avons également de nombreux formats de fichiers de modèles.

En voici une liste partielle.

Si vous voulez charger ces fichiers de modèles dans votre jeu, vous pouvez soit écrire votre propre chargeur personnalisé, soit utiliser une bibliothèque existante pour cela.

Si vous aimez tout écrire de zéro, vous êtes libre d'écrire votre propre analyseur (parser).

Mais ma recommandation est d'opter pour une solution existante car cela vous fera gagner beaucoup de temps.

Dans cette vidéo, nous allons utiliser l'Open Asset Import Library, ou Assimp, qui est une bibliothèque gratuite et open-source très facile à utiliser et qui supporte de nombreux formats de fichiers.

Assimp se charge d'analyser le fichier du modèle, qui peut d'ailleurs être textuel ou binaire, et le charge dans sa propre structure de données native en mémoire.

Ce que nous devons faire, c'est utiliser cette structure de données afin de remplir les tampons de sommets et d'indices d'OpenGL.

Charger les textures qui pourraient également être présentes et configurer la disposition des attributs de sommets.

Commençons par installer Assimp, et nous avons plusieurs options ici.

Selon le système d'exploitation.

J'inclurai les instructions pour tout ce que vous allez voir dans la description de la vidéo.

Si vous êtes sur Linux Ubuntu, vous pouvez simplement exécuter la commande suivante pour installer Assimp.

Si vous voulez compiler Assimp vous-même, vous devrez cloner le dépôt suivant.

Allez dans le nouveau répertoire et exécutez `cmake .`. Si vous n'avez pas CMake installé, vous pouvez facilement l'installer via `sudo apt install cmake`.

À ce stade, vous pourriez rencontrer diverses difficultés, principalement dues à des paquets manquants.

Dites-le moi dans les commentaires et j'essaierai d'aider autant que possible.

Vous pouvez également utiliser le forum de support sur la page GitHub.

Si CMake se termine avec succès, vous pouvez exécuter `make` puis `sudo make install` pour terminer l'installation.

Maintenant, vous devez intégrer Assimp dans votre processus de compilation.

Comme vous le savez probablement, j'utilise des scripts bash simples pour compiler mes sources.

Dans ces scripts, j'utilise `pkg-config` pour obtenir les paramètres de compilation et de liaison (link).

Ainsi, tout ce que j'ai à faire est d'ajouter `assimp` comme paramètre à la commande `pkg-config --cflags` pour obtenir le répertoire d'inclusion et `pkg-config --libs` pour obtenir la commande de liaison.

Les résultats des deux commandes sont fournis comme paramètres à g++ ci-dessous.

`pkg-config` est très pratique car son comportement est adapté à la distribution sur laquelle il s'exécute, ce qui le rend très flexible.

Sur Windows, vous avez également deux options : vous pouvez utiliser les binaires fournis avec mon dépôt de sources ou vous pouvez compiler les sources vous-même.

Malheureusement, il semble que les binaires pré-compilés pour Windows ne soient plus disponibles sur le site web d'Assimp.

D'accord, donc si vous voulez utiliser les binaires que j'ai créés, vous pouvez aller dans le répertoire `ogldev`, descendre vers `windows` ici.

Et dans le répertoire `lib`, vous trouverez ce fichier `assimp-vc142-mt.lib`, c'est la bibliothèque à laquelle vous devez vous lier. C'est une version "release" d'Assimp et vous avez également besoin de la DLL pour l'exécution, qui se trouve dans ce répertoire `dll`.

C'est le même fichier mais avec l'extension `.dll`.

Et vous aurez également besoin de tous les en-têtes que nous avons ici dans `ogldev/include`, nous avons `assimp`.

Et ce sont tous les en-têtes de cette bibliothèque enregistrés ici.

C'est la dernière version au moment actuel.

Maintenant, si vous voulez compiler les sources vous-même, vous devez les récupérer via Git.

J'utilise TortoiseGit.

Et j'ai expliqué comment l'installer dans un tutoriel précédent, celui sur le support Windows, vous pouvez donc le trouver là-bas.

Ce que vous devez faire, c'est un clic droit dans un répertoire puis `git clone`.

Et voici l'adresse du site web, qui par défaut ira dans ce répertoire `assimp`.

Je n'ai pas besoin d'appuyer sur OK, car je l'ai déjà récupéré ici.

Entrons à l'intérieur.

Ici, vous pouvez faire Shift + clic droit et aller sur "Ouvrir la fenêtre PowerShell ici".

Et vous aurez également besoin de CMake installé. Tapez simplement `cmake CMakeLists.txt` et lancez-le, cela générera le fichier de solution Visual Studio que nous pouvons trouver ici : `Assimp.sln`.

Ouvrons celui-ci.

Ici, vous pouvez sélectionner si vous voulez la version "debug" ou "release".

Comme je l'ai dit, ce qui est enregistré dans le dépôt de sources `ogldev` est la version "release", et assurez-vous d'utiliser x64.

Ensuite, vous avez juste besoin de faire "build" et "rebuild solution".

Une fois la compilation terminée,

Nous pouvons retourner dans `assimp/lib`.

Et sélectionner "debug" ou "release" selon ce que vous avez utilisé pour compiler, dans ce cas, "release".

Nous avons donc ce fichier ici, qui est exactement celui qui est enregistré dans le dépôt de sources d'origine et aussi dans `/bin`, nous avons la DLL.

Maintenant, allez dans votre projet.

Clic droit, propriétés.

Allons dans "Linker" et "Input".

Et ici, dans les dépendances supplémentaires, nous avons le fichier `assimp.lib`. Vous devrez également vous assurer que dans "C++", "General", vous avez le répertoire d'inclusion ici comme répertoire d'inclusion supplémentaire. J'ai déjà ce répertoire provenant de tous les projets précédents, qui remonte de trois répertoires vers `include` par rapport à l'emplacement du projet.

D'accord, donc si nous allons à l'emplacement du fichier de projet Visual Studio, dans `ogldev/windows/ogldev_vs_2019`.

Nous avons le projet ici.

Nous remontons de trois répertoires.

Et ici nous avons `include`, et voici les en-têtes Assimp.

Ainsi, lorsque nous incluons les en-têtes, nous pouvons simplement écrire cette directive ici car elle référence le répertoire d'inclusion que nous venons de voir.

Nous devons également nous assurer que le fichier DLL est accessible pendant l'exécution.

Retournons donc dans les propriétés du projet, et allons dans "Debugging".

Et ici, on peut voir que j'ai ajouté l'emplacement du répertoire de la DLL juste ici.

Nous pouvons maintenant l'exécuter.

Plongeons maintenant dans le code et j'expliquerai la structure d'Assimp au fur et à mesure.

D'accord, j'ai d'abord créé une classe appelée `BasicMesh` qui représente un modèle chargé à l'aide d'Assimp.

Cette classe est déclarée dans `ogldev_basic_mesh.h` dans le répertoire `include`.

Nous avons plusieurs fonctions publiques et privées ici, ainsi que quelques variables privées.

Nous reviendrons sur ces éléments au fur et à mesure de l'examen de la classe.

Passons maintenant à l'implémentation de cette classe dans `ogldev_basic_mesh.cpp` dans le répertoire `common`.

La première fonction que j'aimerais examiner est `LoadMesh`, qui est une fonction publique prenant le nom du fichier en paramètre et servant de point d'entrée de haut niveau pour tout le processus de chargement.

Le premier appel de fonction à l'intérieur de cette fonction est de déclarer une fonction privée.

Cette fonction efface toutes les structures de données internes de la classe, vous permettant de réutiliser le même objet de classe pour charger un modèle différent.

Nous n'allons pas utiliser cette capacité dans ce tutoriel, donc je vais passer à la suite : régénérer et lier l'objet de tableau de sommets (VAO) pour le modèle actuel.

Nous avons couvert cela dans le tutoriel précédent, alors assurez-vous de le regarder pour plus de détails.

Ensuite, nous générons six objets de tampons OpenGL, et `m_Buffers` est un tableau privé de six entiers non signés.

Dans ce tutoriel, nous allons voir une méthode différente de stockage des sommets.

Ce que nous avons utilisé jusqu'à présent est une méthode connue sous le nom de "tableau de structures" ou AOS (Array of Structures).

L'élément central de cette méthode est une structure qui contient les attributs des sommets tels que la position, les coordonnées de texture, les normales, etc.

Pour stocker plusieurs sommets, nous avons un tableau de cette structure, d'où le nom de tableau de structures.

Ce tableau est chargé dans le tampon OpenGL, ce qui signifie que les attributs sont entrelacés, exactement de la même manière qu'en mémoire CPU.

La seconde méthode, celle que je vais démontrer aujourd'hui, est une "structure de tableaux" ou SOA (Structure of Arrays).

Ici, nous avons un tableau séparé pour chacun des attributs.

D'accord, nous avons donc un tableau de positions, un tableau de coordonnées de texture, et ainsi de plus. Nous pouvons regrouper ces tableaux dans une seule structure.

Comme son nom l'indique (structure de tableaux), les tableaux doivent tous avoir la même longueur.

Ainsi, pour accéder à tous les attributs d'un seul sommet, nous devons utiliser le même indice pour accéder à chacun des tableaux.

OpenGL nous permet d'utiliser les deux méthodes pour construire nos objets 3D.

Nous utilisons une énumération pour accéder à chaque tampon par son nom plutôt que par un numéro obscur.

Ainsi, le premier tampon est le tampon d'indices, nous avons la position à l'indice 1, les coordonnées de texture à l'indice 2, et la normale à l'indice 3. Les vecteurs normaux sont requis pour les effets d'éclairage.

Pour l'instant, ce n'est qu'un emplacement réservé.

Donc, si vous écrivez ce code vous-même, vous pouvez le laisser de côté.

Les deux derniers tampons `WVP_Mat_VB` et `WorldMap_VB` sont également des emplacements réservés.

Ils seront utilisés à l'avenir lorsque nous aborderons l'instanciation.

De retour à `LoadMesh`, nous pouvons voir que nous initialisons tous les tampons en un seul appel à `glGenBuffers`.

Au fait, `ARRAY_SIZE_IN_ELEMENTS` est une macro pratique pour calculer le nombre d'éléments dans un tableau en divisant la taille du tableau par la taille du premier élément, qui doit toujours exister.

Pour accéder aux services d'Assimp, nous définissons un objet de la classe `Importer` qui est définie dans l'espace de noms `Assimp`.

Pour que cela compile, nous devons inclure trois fichiers du répertoire `include` d'Assimp : `Importer.hpp`, `scene.h` et `postprocess.h`. Nous chargeons effectivement le modèle en appelant `importer.ReadFile` en passant le nom du fichier du modèle et la liste des drapeaux (flags) Assimp qui est enveloppée dans cette macro `ASSIMP_LOAD_FLAGS`.

Ces drapeaux nous permettent de modifier le comportement d'Assimp, passons-les rapidement en revue.

D'abord, nous avons le drapeau `triangulate`.

De nombreux outils de modélisation vous permettent de construire des modèles en utilisant des polygones de plus de trois sommets, mais nous devons utiliser des triangles.

Ce drapeau demande donc à Assimp de diviser ces polygones en triangles.

`GenSmoothNormals` est pour l'éclairage.

Gardons-le pour l'instant.

`FlipUVs` inverse les coordonnées de texture le long de l'axe V ou Y de la texture.

C'est quelque chose avec lequel vous devrez peut-être jouer pour que cela fonctionne avec vos modèles, car certains modeleurs vous permettent de contrôler cela lors de l'exportation du modèle.

Et enfin, nous voulons qu'Assimp joigne les sommets identiques et ajuste le tampon d'indices en conséquence.

Cela nous fera gagner de la mémoire.

Il existe de nombreux autres drapeaux disponibles dans l'en-tête `postprocess.h` d'Assimp et vous pouvez trouver la documentation complète en ligne.

C'est d'ailleurs l'une des raisons pour lesquelles Assimp est si flexible.

Si `ReadFile` renvoie `NULL`, alors l'appel a échoué et nous affichons l'erreur en utilisant `importer.GetErrorString`.

Sinon, nous récupérons un pointeur vers un objet de la classe `aiScene`.

Et nous appelons `InitFromScene` pour continuer l'initialisation.

`aiScene` est la structure de données de haut niveau dans la représentation en mémoire du modèle créé par Assimp.

Comme d'habitude, avant de quitter cette fonction, nous délions notre VAO de l'état OpenGL.

Et continuons avec `InitFromScene` qui est définie sous cette fonction.

La manière dont `aiScene` est structurée correspond au comportement de la plupart des modeleurs qui permettent de diviser le modèle en sous-composants.

Cela vous permet d'appliquer une transformation sur un composant sans affecter les autres.

Vous pouvez donc avoir une tête, un bras, une épée, etc.

Si le modèle est divisé en sous-composants, Assimp crée une structure `aiMesh` pour chaque composant.

Cette structure `aiMesh` contient tous les sommets et indices de ce composant.

Le nombre de structures `aiMesh` est donné dans la variable `mNumMeshes` de la classe `aiScene`. Nous réservons un nombre correspondant d'éléments dans notre variable privée `m_Entries`, qui est un vecteur de `BasicMeshEntry`.

`BasicMeshEntry` contient quelques variables que nous devrons maintenir pour chaque `aiMesh`, telles que le nombre d'indices, le sommet de base, etc.

Nous allons les voir bientôt.

Une scène peut également contenir des textures, et Assimp regroupe une ou plusieurs textures dans ce qu'il appelle des matériaux (materials).

Ceux-ci sont stockés dans un tableau de structures `aiMaterial`.

Et la taille de ce tableau est donnée dans `mNumMaterials`.

Nous avons un vecteur correspondant de pointeurs vers notre classe `Texture`, nous y réservons l'espace en conséquence.

Voici le plan : nous allons empiler tous les sommets et indices de toutes les structures `aiMesh` dans les tampons que nous venons de créer, selon leur type (indice, position, coordonnées de texture, etc.).

Cependant, chaque `aiMesh` peut utiliser une texture différente, mais nous ne pouvons pas changer de texture au milieu d'un appel de rendu (draw call).

Cela signifie que nous devons lancer un appel de rendu pour chaque maillage séparément, ce qui nous donnera l'opportunité de changer de texture selon les besoins entre les appels de rendu.

Cela signifie également que nous ne pouvons pas utiliser `glDrawElements`.

Parce que cette fonction ne dessine que les sommets depuis le début du tampon, nous avons besoin d'une fonction plus sophistiquée qui nous permet de dessiner à partir de différents décalages (offsets) au sein du tampon.

Et OpenGL nous fournit une telle fonction de rendu.

D'accord, donc pour allouer réellement de l'espace dans nos tampons d'indices et de sommets, nous devons savoir combien de sommets et d'indices il y a dans l'objet scène entier.

Malheureusement, ces informations ne nous sont pas directement accessibles, nous devons donc les compter.

Nous faisons cela dans la fonction privée `CountVerticesAndIndices`, qui met également à jour le tableau `m_Entries`. Nous avons juste besoin de boucler sur les éléments du tableau `m_Entries` que nous venons de redimensionner.

Pour chaque élément, nous copions l'indice du matériau de la structure `aiMesh` correspondante, nous calculons le nombre d'indices dans le maillage actuel en multipliant le nombre de faces par trois, puisque après triangulation, tous les polygones sont désormais des triangles. Le sommet de base est l'indice du premier sommet du maillage actuel dans nos tampons globaux.

Pour le calculer, nous incrémentons `NumVertices` par le nombre de sommets dans l' `aiMesh`. Nous calculons l'indice de base de manière similaire en incrémentant `NumIndices` par le nombre d'indices du maillage actuel que nous venons de calculer.

Ainsi, par exemple, si nous avons trois maillages avec 100, 200 et 50 sommets, alors le premier maillage est à l'offset 0, le deuxième maillage est à l'offset 100.

Et le dernier est à l'offset 300.

Lorsque nous quittons la fonction, `NumVertices` et `NumIndices` contiennent les totaux pour chaque type.

De retour à `InitFromScene`, nous appelons `ReserveSpace` avec les deux compteurs.

Cette fonction alloue de l'espace dans quatre vecteurs pour les positions, les coordonnées de texture, les normales et les indices.

Ces vecteurs sont des membres privés de la classe, ils seront utilisés pour accumuler tous les sommets de la structure `aiScene`.

Ainsi, nous pouvons charger chaque tampon OpenGL avec un seul appel à `glBufferData`.

De retour à `LoadMesh`, nous appelons `InitAllMeshes`, qui parcourt simplement toutes les structures de maillage Assimp et appelle `InitSingleMesh` pour chacune.

Dans cette fonction, nous remplissons réellement les vecteurs que nous venons de voir avec les données de sommets et d'indices.

Nous faisons cela en parcourant tous les sommets de l' `aiMesh` et en extrayant la position, la normale et les coordonnées de texture de leur emplacement respectif dans l' `aiMesh`.

Notez que ces éléments sont représentés par l'API Assimp `aiVector3D`, qui est très similaire à notre classe vecteur.

Dans le cas de la coordonnée de texture, nous devons également vérifier qu'elle existe, sinon utiliser le vecteur nul à la place. Nous pouvons maintenant remplir nos vecteurs avec ces données.

Notez également que dans le cas des coordonnées de texture, nous n'utilisons que le X et le Y du vecteur 3D. Remplir les indices est très similaire.

Le maillage contient un tableau de triangles appelé `mFaces`.

Chaque structure `aiFace` contient les trois indices, que nous devons ajouter au vecteur d'indices.

La fonction suivante appelée par `InitFromScene` est `InitMaterials`.

C'est ici que nous allouons les textures OpenGL pour les images du modèle.

Les fichiers images sont stockés dans le même répertoire que le fichier principal du modèle.

Donc d'abord, nous devons extraire le répertoire du fichier du modèle.

Cela se fait par une simple analyse du dernier caractère slash.

Nous pouvons maintenant parcourir le tableau des matériaux dans la scène Assimp.

Un matériau est essentiellement un conteneur pour plusieurs textures, et il peut contenir des textures diffuses, spéculaires et ambiantes, ainsi que des éléments comme une carte de hauteur (height map), une carte de normales (normal map), etc.

Ceux-ci sont requis pour des choses plus avancées comme l'éclairage. Pour un texturage de base, nous avons juste besoin de la texture diffuse.

Nous vérifions donc si elle existe en appelant `GetTexture` sur le matériau avec l'énumération `aiTextureType_DIFFUSE`.

Dans le premier paramètre, le second paramètre est zéro car nous ne voulons que la première texture.

Le troisième paramètre est l'adresse d'une variable `aiString`, où le chemin de la texture sera renvoyé s'il existe.

Bien sûr, pour l'instant, nous n'avons pas besoin du reste des paramètres.

Nous y mettons donc des `NULL`.

Si l'appel a réussi, nous construisons le chemin complet du fichier de texture.

À l'intérieur du modèle, le chemin de la texture est relatif à l'emplacement du fichier du modèle.

Maintenant, nous pouvons créer notre objet texture comme d'habitude et le charger.

Revenons à `InitFromScene` pour la dernière fois.

Et l'appel final ici est vers la fonction privée `PopulateBuffers`.

C'est ici que nous préparons les éléments pour utiliser la structure SOA.

Nous commençons par lier le tampon de position à la cible `GL_ARRAY_BUFFER` pour le rendre courant, nous chargeons les données du vecteur dans le tampon en appelant `glBufferData`.

Le nombre d'octets est obtenu en multipliant la taille du premier élément par le nombre d'éléments dans le vecteur.

L'adresse de base est l'adresse du premier élément et nous utilisons `GL_STATIC_DRAW`, car nous ne prévoyons pas de mettre à jour le tampon à nouveau.

Ensuite, nous activons l'attribut de sommet pour la position.

En haut de ce fichier, nous avons des macros pour l'emplacement des trois attributs de sommets.

Ce n'est pas la conception la plus robuste car nous devons garder cela synchronisé avec le shader, mais cela fera l'affaire pour l'instant.

Ensuite, nous configurons la disposition du tampon de position en appelant `glVertexAttribPointer`.

Encore une fois, nous utilisons la macro pour l'indice de l'attribut, nous avons trois flottants ici, `GL_FALSE` car il n'est pas nécessaire de normaliser, et les deux derniers paramètres sont maintenant à zéro.

Précédemment, nous devions mettre ici la taille de la structure de sommet entière, et le décalage de l'attribut actuel à l'intérieur du sommet.

Puisque les positions sont emballées les unes après les autres, nous pouvons maintenant mettre des zéros ici car le pilote sait déjà tout grâce aux trois flottants.

Nous répétons le même processus pour les coordonnées de texture et les normales.

Et chaque fois que nous appelons `glVertexAttribPointer`, le pilote stocke l'adresse du tampon qui est actuellement lié à `GL_ARRAY_BUFFER` pour l'attribut actuel.

Cela permet à chaque attribut de provenir d'un tampon différent.

D'accord, c'est donc la structure SOA (Structure of Arrays).

Enfin, nous remplissons les indices, n'oubliez pas d'utiliser `GL_ELEMENT_ARRAY_BUFFER` pour la cible ici.

Félicitations, nous en avons terminé avec le chargement du modèle.

La seule chose qu'il nous reste ici est bien sûr la fonction de rendu (`Render`). Nous commençons par lier le VAO de ce modèle, ce qui ramène la disposition des sommets que nous venons de créer.

Ensuite, nous parcourons notre tableau interne `m_Entries`, nous récupérons l'indice du matériau, et nous vérifions si nous avons un élément correspondant dans le tableau de textures car il peut y avoir un matériau sans texture diffuse.

S'il y a une texture, nous la lions. `COLOR_TEXTURE_UNIT` est simplement une macro pour `GL_TEXTURE0` que je garde dans `ogldev_engine_common.h`. J'utilise ce fichier afin de garder les tutoriels cohérents.

Maintenant vient la partie intéressante.

Au lieu de `glDrawElements`, nous utilisons `glDrawElementsBaseVertex` qui nous permet de dessiner des sous-régions des tampons de sommets et d'indices.

Le premier paramètre est `GL_TRIANGLES` comme d'habitude.

Le deuxième paramètre est le nombre d'indices du maillage actuel, que nous avons calculé lors du chargement du modèle.

Ensuite, le type de données de l'indice, `GL_UNSIGNED_INT` dans notre cas. Ensuite, le décalage vers le premier indice du maillage actuel dans le tampon d'indices.

Ainsi, nous multiplions l'indice de base du maillage actuel par la taille d'un entier non signé.

Afin d'obtenir le décalage, nous devons également le transtyper (cast) en `void*`.

Je pense que c'est dû à un problème historique avec cette fonction.

Le dernier paramètre est le sommet de base pour l'appel de rendu actuel.

Voyez-vous, les indices originaux que nous avons obtenus d'Assimp commençaient à zéro dans chaque structure `aiMesh`, mais nous avons décidé d'empiler tous les sommets dans un seul tampon par attribut.

Cela perturbe l'indexation. Une solution serait d'ajuster chaque indice en fonction de la position de départ du maillage dans notre tampon unique.

Une solution plus simple est d'utiliser ce dernier paramètre ici comme sommet de base.

Ce nombre sera ajouté à chaque indice afin qu'il corresponde au décalage à l'intérieur de notre tampon.

Par exemple, disons que nous avons deux maillages Assimp.

Les indices des deux maillages commencent à zéro, mais chaque maillage se réfère évidemment à son propre ensemble de sommets.

Nous empilons les deux groupes de sommets l'un après l'autre et disons que la taille du premier groupe est de 100.

Ainsi, le sommet de base pour le second groupe sera calculé comme étant 100.

Lorsque nous rendrons le second groupe, nous passerons 100 dans ce dernier paramètre, de sorte que l'indice 0 deviendra 100, l'indice 1 deviendra 101, etc.

Nous avons donc un sous-ensemble d'indices qui commence à un certain décalage à l'intérieur du tampon d'indices.

Et à chaque indice, OpenGL ajoutera automatiquement ce que nous avons mis comme sommet de base.

Tous ces éléments ont déjà été calculés lors du chargement du modèle.

Ils sont donc prêts quand nous arrivons ici.

D'accord, nous avons donc une série d'appels de rendu ici.

Chaque appel de rendu utilise un sous-ensemble des tampons d'indices et de sommets.

Et avant chaque appel de rendu, nous avons l'opportunité de changer de texture.

Voyons maintenant les changements dans le code principal de l'application.

Dans la classe du tutoriel 18, je me suis débarrassé de tous les VAO, VBO et tampons d'indices que j'avais l'habitude de garder ici, ainsi que de l'objet de transformation mondiale.

Au lieu de cela, nous avons juste besoin d'un seul pointeur vers `BasicMesh`.

Dans la méthode `Init`, nous devons appeler le maillage avec le chemin du fichier du modèle.

Dans la fonction de rendu principale, nous effectuons toutes les transformations sur l'objet de transformation mondiale que nous avons dans la classe `BasicMesh`.

Ainsi, si nous avons plusieurs maillages, cela simplifie la conservation de la transformation de chaque maillage à l'intérieur de son propre objet.

De plus, au lieu d'appeler `glDrawElements`, nous avons juste besoin d'appeler la fonction `Render` sur l'objet maillage.

C'est essentiellement tout ce que nous avons à faire ici.

Compilons et lançons ceci.

D'accord, cela ressemble à une araignée.

Mais il y a manifestement quelque chose qui ne va pas ici, n'est-ce pas ? Le problème est que je n'ai pas activé le test de profondeur (depth test).

Sans lui, le tampon de trame (frame buffer) fonctionne comme un canevas ordinaire.

Ainsi, quelle que soit la couleur que vous utilisez en dernier, c'est la couleur que vous allez réellement obtenir sur l'écran final.

Avec des choses simples comme le cube, nous ne pouvions pas voir le problème.

Mais avec des modèles plus complexes, le problème est évident.

J'ai discuté du tampon de profondeur dans l'épisode précédent, donc je ne le répéterai pas ici.

En activant le test de profondeur, nous nous assurons que le pixel le plus proche est rendu.

Quel que soit l'ordre de rendu.

Nous faisons cela en appelant `glEnable` avec la macro `GL_DEPTH_TEST` en paramètre. Nous devons également effacer le tampon de profondeur à chaque image, sinon il contiendra des données parasites de l'image précédente.

Ainsi, dans la fonction de rendu principale, nous ajoutons le bit `GL_DEPTH_BUFFER_BIT` au masque de bits que nous fournissons à l'appel `glClear`.

D'accord les gars, vous pouvez maintenant essayer de charger différents modèles que vous trouvez gratuitement en ligne, ou que vous créez vous-même si vous savez comment faire. Je ne peux pas garantir que ce code est infaillible et fonctionnera pour chaque modèle, il contient probablement encore quelques bugs, n'hésitez pas à me le faire savoir si vous rencontrez un problème.

Bienvenue à nouveau sur OGLDev.

Dans ce tutoriel, nous commençons à examiner l'animation squelettique et comment l'implémenter de manière efficace en OpenGL.

L'animation squelettique, ou skinning, est considérée comme la manière standard d'animer presque toute créature vivante.

Et elle peut également être utilisée pour animer des monstres, des extraterrestres, ainsi que divers types de machines, comme des robots.

C'est donc une technique centrale dans le développement de jeux.

Ainsi, au cours des prochains tutoriels, nous allons l'explorer en profondeur.

Assimp, la bibliothèque que nous utilisons pour charger les modèles, offre un très bon support pour l'animation squelettique à travers plusieurs types de fichiers.

Nous allons donc en profiter.

La manière dont je vais couvrir ce sujet sera très orientée vers la pratique.

Je fournirai une vue d'ensemble du processus et de la technique.

Et ensuite, nous ferons essentiellement des allers-retours entre le code et la théorie.

Nous comprendrons une partie de l'algorithme, puis nous verrons comment l'implémenter en C++ avec OpenGL.

Et ensuite retour à la théorie, etc.

Je vais utiliser Blender comme outil de modélisation.

Par simplicité, j'utiliserai juste le nom Blender.

Mais bien sûr, tous les autres grands outils de modélisation supportent également l'animation squelettique.

Juste pour clarifier, je ne suis pas un artiste.

Mais pour les besoins du développement de cette mini-série,

j'ai passé du temps à étudier Blender car je pense que la familiarité avec l'outil où vous créez et animez le modèle vous donne une meilleure compréhension de la partie développeur dans ce processus.

Prenons maintenant le corps humain.

Comme exemple.

Comme vous le savez probablement, 70 % de notre corps est composé d'eau, c'est pourquoi nous sommes si flexibles. Les os sont enveloppés par la chair et la chair est enveloppée par la peau.

Ainsi, fondamentalement, on peut dire que la peau est portée ou maintenue par les os.

Maintenant, ceci ne va pas être une leçon d'anatomie.

Tout ce que je dis, c'est que l'idée derrière l'animation squelettique est largement empruntée au monde réel.

Tous les modèles que nous avons utilisés jusqu'à présent n'étaient que la représentation extérieure d'un objet du monde réel.

À l'intérieur de l'objet,

il n'y a rien. Dans le contexte de l'animation squelettique, nous appelons le modèle lui-même la peau (skin), c'est pourquoi cette technique est aussi appelée skinning.

Les os constituent le squelette, qui porte en quelque sorte la peau comme dans le monde réel.

Mais comme nous n'avons pas de chair dans notre modèle entre le squelette et la peau, le remplacement que Blender fournit est simplement une liste de sommets qui sont affectés par chaque os.

Cela signifie que lorsque l'os est animé, ou pour le dire dans un langage qui nous est plus familier, lorsqu'il subit une translation et une rotation, la même transformation qui est appliquée à l'os doit être appliquée aux sommets qui sont affectés par lui.

Par exemple, lorsque l'os d'un bras subit une translation et une rotation, la partie du maillage qui représente ce bras subit la même translation et rotation.

Pour suivre le mouvement et la rotation de l'os.

Calculer les transformations qui doivent être appliquées sur les sommets en raison du mouvement des os est l'objectif majeur de cette technique. Il est important de comprendre que seule la peau est rendue, et non le squelette.

Le rôle du squelette et des os est simplement de nous aider à définir la plage de mouvement disponible pour la peau.

Par exemple, l'angle entre le bras et l'avant-bras peut varier entre zéro, "entre guillemets", lorsque les deux membres se touchent, et 180 degrés lorsque l'avant-bras est complètement tendu.

Au-delà, le coude se briserait.

Pas très agréable. Le processus dans Blender consistant à placer les os virtuels à l'intérieur de la peau, à leur donner la longueur appropriée pour s'adapter à la partie spécifique du corps et à les connecter ensemble pour former un squelette s'appelle le rigging.

Le skinning est le processus par lequel vous connectez les sommets au squelette et définissez la mesure dans laquelle chaque sommet est affecté par les os.

La dernière pièce du puzzle est l'animation.

Et c'est là que vous utilisez les contrôles disponibles placés pendant la phase de rigging afin de créer un ensemble d'images clés (keyframes) qui définissent le mouvement des os.

Au fil du temps, l'animation squelettique présente deux caractéristiques principales qui nous aident à imiter le mouvement du monde réel.

D'abord, le squelette définit la hiérarchie des os, la plupart des os auront un parent.

Ainsi, lorsque l'os parent bouge, l'os enfant suit. Cette relation est à sens unique : l'enfant peut bouger sans affecter le parent.

Deuxièmement, chaque sommet peut être affecté par plus d'un os.

Cela signifie que lorsqu'un ou plusieurs os bougent, la transformation des sommets qui sont influencés par ces os doit d'une manière ou d'une autre combiner les transformations de chaque os.

En fait, si vous avez un modèle où chaque sommet est entièrement contrôlé par un seul os, alors ce modèle est probablement celui d'un robot ou de tout autre type de machine.

Une voiture est un exemple simple, vous pouvez utiliser l'animation squelettique pour animer l'ouverture et la fermeture des portières.

La portière est reliée à la voiture par une sorte de joint métallique.

Mais quand la portière s'ouvre, les seuls sommets qui bougent appartiennent à la portière, le reste de la voiture reste exactement là où il est. Ce n'est certainement pas le cas avec les créatures vivantes.

Ici, nous voulons que le modèle se déforme d'une manière qui simulera l'élasticité de la peau.

Ce comportement est le plus évident autour des articulations.

L'animation squelettique nous permet un haut degré de flexibilité en termes de calcul du mouvement de chaque sommet basé sur tous les os qui l'affectent.

Nous faisons cela en assignant un poids (weight) à chaque combinaison d'un os et d'un sommet. Le poids est une fraction entre zéro et un.

Et la somme de tous les poids par sommet doit être de un. Nous effectuons le calcul comme une combinaison linéaire des transformations des os et de leurs poids.

Par exemple, si le poids de deux os affectant un sommet est de 0,5, cela signifie que le sommet est influencé de manière égale par les deux os et son mouvement sera la moyenne du mouvement des deux os.

Si un poids est de 0,9 et l'autre de 0,1, cela signifie que le sommet est probablement beaucoup plus proche du premier os, il suivra donc celui-ci.

Mais il y aura toujours une influence mineure provenant du second os qui pourrait le tirer un peu vers une direction différente.

Blender fournit à l'artiste des outils puissants pour définir les poids des différents os.

La plupart des artistes commenceront probablement par une assignation automatique des poids. Dans cette méthode, Blender calcule les poids en fonction de la distance entre le sommet et chaque os.

L'étape suivante consistera à examiner le résultat et à commencer à corriger, ajuster et peaufiner le modèle à l'aide de la peinture de poids (weight painting).

Le weight painting est une fonctionnalité de Blender où vous augmentez ou diminuez les poids des sommets pour l'os sélectionné en passant dessus avec un pinceau spécial.

Habituellement, l'artiste développera d'abord la peau, puis structurera le squelette à l'intérieur.

C'est logique car les os doivent correspondre aux dimensions de la partie du corps qui sera réellement rendue.

À ce stade, avant que le processus d'animation ne commence,

la posture de la peau est appelée Bind Pose (pose de référence).

C'est très important car toutes les transformations et calculs mathématiques sous-jacents feront référence à la Bind Pose comme position de départ.

Il n'y a aucune restriction quant à l'apparence du modèle en Bind Pose.

Mais la pratique courante consiste à garder le modèle dans ce genre de posture détendue sans trop de flexions au niveau des articulations.

Si vous recherchez "skeletal animation Bind Pose" dans Google Images, vous trouverez de nombreux exemples de cette posture pour des modèles humains ou semi-humains, avec les bras tendus sur les côtés et les jambes droites et détendues.

Lorsque vous effectuez le rendu du modèle sans lui appliquer d'animation, vous devriez l'obtenir en Bind Pose.

Une fois que le rigging et le skinning ont été terminés, le modèle est prêt pour l'animation.

Naturellement, le même ensemble d'os peut être utilisé pour plusieurs ensembles d'animations.

Pensez à toutes les possibilités que le corps humain offre en termes de mouvement et de flexibilité.

Tout cela est réalisé avec seulement 206 os.

Même avec un petit sous-ensemble de ces os dans un modèle humain, vous pouvez toujours implémenter de nombreuses animations.

Par conséquent, chaque ensemble d'animation simulera un certain type d'activité comme marcher, courir, se battre, etc.

Un ensemble d'animation est composé d'une série de transformations qui sont appliquées sur le squelette au fur et à mesure que l'artiste l'anime.

Ces transformations peuvent inclure, comme d'habitude, la mise à l'échelle (scaling), la rotation et la translation.

Dans le cas des humains et de nombreuses autres créatures vivantes, nous ne rencontrerons que de la rotation et de la translation.

Mais la technique elle-même peut également supporter la mise à l'échelle animée des os.

Les transformations seront fournies à intervalles réguliers selon une certaine fréquence d'images (frame rate).

Par exemple, une animation de 10 secondes à 24 images par seconde comprendra 240 ensembles de transformations. Ces ensembles sont généralement très proches.

Ainsi, si la fréquence d'images réelle dans le jeu est supérieure à la fréquence d'images de l'animation, nous pouvons interpoler entre les transformations consécutives et obtenir l'animation finale.

Puisque ces transformations représentent les changements dans l'orientation des os, nous pouvons les appliquer sur les sommets qui sont influencés par ces os et ainsi animer le modèle.

D'accord, c'est assez de théorie pour l'instant.

J'ai omis de nombreux détails dont nous aurons besoin pour l'implémentation complète.

Mais à ce stade, j'aimerais que nous nous salissions un peu les mains avec du code.

Maintenant, l'animation squelettique est supportée par divers types de fichiers.

Et si vous implémentez le chargeur pour un type de fichier spécifique, vous devrez probablement faire en sorte que votre code d'animation squelettique respecte les conventions de ce type de fichier.

Cependant, puisque nous utilisons Assimp, nous avons seulement besoin que notre code respecte les conventions et les spécificités de cette bibliothèque.

Et grâce à cela, nous pourrons supporter de nombreux types de fichiers.

Comme je l'ai dit, nous allons implémenter ces techniques étape par étape avec une approche pratique.

Créons donc un utilitaire simple qui analysera les structures de données créées par Assimp et en extraira les parties pertinentes. Plus tard, nous intégrerons cette logique dans notre application OpenGL.

Maintenant, cet utilitaire n'est pas requis pour l'exécution réelle de l'animation, mais il sera très utile pour le débogage, etc.

Cet utilitaire est composé d'un seul fichier, que j'appelle `assimp_sandbox.cpp`.

Et nous avons également un script de compilation dans le même répertoire appelé `build_assimp_sandbox` pour le compiler, et il est très simple.

Nous avons les drapeaux de compilation ici appelés `CPPFLAGS`.

Et pour l'instant, j'ai inclus seulement `-g` pour GDB afin de le compiler avec des informations de débogage.

Et nous avons également les drapeaux de liaison appelés `LDFLAGS`, qui est un appel à `pkg-config --libs assimp`.

J'utilise souvent `pkg-config` dans mes scripts de compilation afin que mon code puisse, je l'espère, compiler sur autant de machines et de systèmes que possible.

D'accord, donc si vous lancez ceci sur la ligne de commande : `pkg-config --libs assimp`.

Dans ce cas sur ma machine, il vous dit que la commande de liaison est `-lassimp` et sur d'autres systèmes, cela peut générer une commande différente.

D'accord, et la commande de compilation finale est très simple, nous appelons `g++`, le nom du fichier `.cpp`, les drapeaux du compilateur, les drapeaux de liaison, `-o` et le nom du binaire.

D'accord, jetons maintenant un coup d'œil au fichier `.cpp`.

Et au fait, j'ai une vidéo sur le chargement de modèles à l'aide d'Assimp, donc n'hésitez pas à la regarder.

Si vous voulez plus de détails.

Je vais passer en revue les détails majeurs dans cette vidéo.

D'accord, nous devons d'abord inclure ces trois en-têtes pour Assimp.

D'accord, descendons vers le bas.

Et ici nous avons votre fonction `main` standard, nous vérifions le nombre de paramètres ici, il doit être de deux, car il y a un seul paramètre pour cet utilitaire, qui est le nom du fichier du modèle.

D'accord, donc si ce n'est pas le cas, nous quittons simplement l'utilitaire.

Ensuite, nous récupérons le nom du fichier à l'emplacement 1 dans le tableau `argv`.

Et nous définissons un objet de la classe `Assimp::Importer`, qui gère essentiellement tout ce qui concerne l'analyse d'Assimp.

Ensuite, nous appelons `ReadFile` sur l'objet `importer` en utilisant le nom du fichier et le drapeau de chargement pour Assimp que j'ai défini.

Pour plus de commodité ici.

Et c'est assez standard.

Nous l'avons déjà fait, trianguler tous les polygones dans le maillage, générer les normales et joindre les sommets identiques. Nous vérifions les erreurs, et nous appelons `ParseScene` en utilisant l'objet `aiScene` renvoyé par `ReadFile`.

Ainsi, une scène est l'objet principal qui gère toutes nos interactions avec Assimp et elle possède plusieurs fonctions intéressantes, ainsi que des membres auxquels nous pouvons accéder.

Dans ce cas, nous allons directement aux maillages, d'accord, il y a un tableau d'objets `aiMesh`, qui est l'endroit où vivent tous les sommets, ainsi que les indices et les os.

Ainsi, `ParseScene` est très simple, il appelle juste `ParseMeshes` avec l'objet scène.

Et à l'avenir, nous aurons une fonction pour gérer la hiérarchie et les animations.

D'accord, donc cela va grandir et se développer au cours des prochains tutoriels.

Nous avons donc `ParseMeshes` ici.

Et nous commençons par afficher le nombre de maillages dans l'objet scène, que vous pouvez trouver dans l'attribut `mNumMeshes` de la scène.

Ensuite, nous préparons quelques compteurs.

Pour le nombre total de sommets, d'indices et d'os, nous bouclons sur le nombre de maillages, et nous extrayons chaque maillage du tableau de maillages en fonction de l'indice, nous prenons le nombre de sommets, nous calculons le nombre d'indices, qui est le nombre de faces multiplié par trois, car nous avons triangulé tous les polygones, et nous accédons également à `mNumBones`.

D'accord, donc dans la structure `aiMesh`, nous avons un tableau d'os juste ici.

Et nous avons le nombre d'os dans cet attribut, `mNumBones`.

Ensuite, nous calculons le nombre total de sommets, d'indices et d'os, que nous allons afficher à la fin de cette fonction.

Et c'est principalement à des fins informatives, juste pour s'assurer que tout fonctionne correctement.

Les éléments importants ici sont l'appel à `HasBones()`, qui est une fonction booléenne nous indiquant si ce maillage contient des os.

Et ensuite nous appelons `ParseMeshBones` sur le maillage spécifique que nous traitons actuellement.

Alors maintenant, allons à `ParseMeshBones`, qui est ici en haut.

Et c'est aussi très simple, nous bouclons sur le nombre d'os dans ce maillage, et nous appelons `ParseSingleBone`.

Maintenant, si nous lançons ceci tout de suite, et que nous utilisons un modèle qui est enregistré dans mon dépôt, appelé `boblampclean.md5mesh`, qui provient d'ailleurs de Doom 3, vous pouvez voir qu'il nous dit qu'il y a six maillages.

Et voici les noms des maillages.

D'accord, nous avons un corps, un visage, un casque, une grille, une autre grille et un autre corps.

Et pour chaque maillage, nous pouvons voir le nombre de sommets et d'indices.

Et voici la chose importante ici, le nombre d'os. D'accord, donc le corps a 28 os, et le visage n'a que deux os.

Et ces gars-là ont un os, et le dernier en a deux.

D'accord, et si nous le chargeons dans Blender, nous pouvons réellement voir ici sur le côté droit que ces maillages correspondent aux composants du maillage à l'intérieur de Blender.

Nous avons donc la grille que ce gars tient, et nous avons le corps.

D'accord, et cette partie du corps est en fait l'épée, le visage et le casque.

D'accord, voyons maintenant `ParseMeshBones`, qui est juste ici.

Et c'est une simple boucle sur le nombre d'os dans le maillage, et nous appelons `ParseSingleBone` pour chaque os.

À partir de ce tableau, et nous passons également l'indice de l'os que nous verrons plus tard.

Voyons donc ce que nous avons dans cette structure `aiBone`.

Et il n'y a que quatre attributs publics.

D'accord, nous avons le nom de l'os, qui est utilisé à des fins informatives, comme vous l'avez vu dans Blender, vous voulez nommer les os pour pouvoir vous rappeler ce qu'ils sont censés faire.

Et nous avons le nombre de poids ici, qui est en fait le nombre d'éléments dans ce tableau `mWeights`.

D'accord, nous verrons cela dans une seconde, nous avons un attribut appelé `mOffsetMatrix`, qui est une matrice 4x4.

Et il nous dit que cette matrice transforme de l'espace du maillage vers l'espace de l'os en Bind Pose.

D'accord, cela peut sembler un peu intimidant, mais nous verrons comment l'utiliser dans une future vidéo.

Et le dernier attribut est le tableau `mWeights`, qui est de la structure `aiVertexWeight`.

Et cette structure contient juste deux attributs.

D'accord, donc chaque élément de la structure a un `mVertexId`, qui nous indique l'indice du sommet influencé par cet os, et la force de cette influence (`mWeight`), qui doit être comprise entre zéro et un comme nous en avons parlé plus tôt.

Ainsi, dans la fonction `ParseSingleBone`, nous bouclons sur le nombre de poids dans l'os, et nous extrayons l'élément de poids de sommet du tableau `mWeights`, et laissez-moi juste décommenter tous ces appels `printf`, nous affichons essentiellement l'ID du sommet et le poids.

Lançons cela à nouveau.

Et maintenant, nous obtenons la liste des os pour chaque maillage ainsi que les sommets qui sont influencés par eux.

D'accord, nous pouvons voir ici que le premier os, l'os 0, s'appelle `pubis` et le nombre de sommets affectés par cet os est de 190.

Et ici nous pouvons voir tous les indices de ces sommets ainsi que les poids. D'accord.

Nous pouvons voir que ce modèle est en fait très simple.

Ainsi, quand nous parcourons ceci, il semble que lorsqu'un sommet est influencé par deux os, alors le poids de chaque os sera de 0,5 et s'il est influencé par trois os, alors le poids sera d'un tiers, d'accord, donc toujours, le poids pour chaque os sera le même que pour les autres os, d'accord, donc c'est une moyenne.

Et voici l'os suivant qui est le bassin (`pelvis`), 254 sommets, puis la colonne vertébrale (`spine`), et cela continue comme ça.

Le nombre total d'os est donc de 35.

Cela nous amène au premier défi : chaque os est mappé aux sommets qu'il influence, et de nombreux sommets sont influencés par plusieurs os.

Mais l'animation squelettique est implémentée dans le vertex shader, car c'est essentiellement le seul endroit où nous pouvons réellement changer la position d'un sommet.

Par conséquent, ce dont nous avons réellement besoin, c'est d'un mappage inverse de chaque sommet vers les os qui l'influencent.

Cette information doit être fournie au vertex shader, afin que nous puissions calculer la transformation de chaque sommet basée sur tous ces os.

Tout cela et bien plus sera couvert dans le prochain tutoriel.

D'accord, petit récapitulatif.

De la première partie, nous avons créé un petit utilitaire pour charger les éléments liés aux os à partir d'Assimp. Assimp contient le modèle dans une ou plusieurs structures de maillage, et chaque maillage pointe vers un tableau d'os et chaque os pointe vers un tableau des sommets qu'il influence.

Pour chaque sommet, nous avons un indice et un poids, qui est un nombre à virgule flottante entre zéro et un représentant la mesure dans laquelle l'os actuel influence ce sommet.

À la fin de la première partie, je vous ai laissé avec le défi de mapper les sommets vers les os qui les ont influencés.

D'accord, c'était peut-être un peu trop dramatique.

Quoi qu'il en soit, cette vidéo va être très technique, et l'accent sera mis sur l'implémentation de ce mappage et sur la vérification de son bon fonctionnement.

Maintenant, puisque le principe de base de cette mini-série est de travailler étape par étape, nous allons d'abord l'implémenter dans l'utilitaire Assimp, puis transférer cette logique vers l'application principale.

Je veux aussi visualiser la relation entre les os et les sommets.

Ainsi, dans la démo d'aujourd'hui, vous pourrez réellement voir l'effet que chaque os a sur les sommets.

Dans cet exemple, les triangles rouges représentent les sommets qui sont fortement influencés par l'os actuel, et cette influence diminue à mesure que nous passons du rouge au jaune, puis au vert.

Les triangles bleus représentent les sommets qui ne reçoivent aucune influence de l'os actuel.

Vous pouvez appuyer sur la barre d'espace pour passer d'un os à l'autre.

Cette partie du fragment shader n'est pas requise dans l'implémentation finale.

Mais je pense que si vous implémentez cela dans votre propre code, ce sera une bonne étape de débogage, juste pour s'assurer que tout est chargé correctement dans le GPU.

D'accord, revenons donc dans `assimp_sandbox.cpp`.

Et nous commençons par inclure les en-têtes `map`, `string` et `vector` de la bibliothèque standard C++ pour les structures de données dont nous aurons besoin ici.

Ensuite, nous avons une macro qui définit le nombre maximum d'os par sommet. Quatre os suffisent pour mon modèle.

Ajustez donc cela pour qu'il corresponde à vos ressources.

Ensuite, nous avons la structure de données `VertexBoneData` qui contient deux tableaux, un pour les indices de tous les os qui affectent ce sommet.

Et pour chaque os, nous avons également le poids correspondant.

Je passerai le reste de la structure pour l'instant.

Ensuite, nous avons trois nouvelles structures de données, nous avons un vecteur de `VertexBoneData` pour chaque sommet.

C'est essentiellement le mappage des sommets vers les os qui les influencent.

Nous avons un vecteur d'entiers appelé `MeshBaseVertex`.

Oui, la classe `aiScene` contient des maillages, qui contiennent des os, et chaque os référence les sommets du maillage dans lequel il est contenu, comme s'ils commençaient à zéro. Nous allons regrouper tous les sommets dans un seul tableau appelé `VertexToBones`.

Nous voulons donc mapper l'indice de sommet relatif à un indice de sommet global unique.

Et nous faisons cela en calculant un sommet de base pour chaque maillage et en ajoutant l'indice de sommet relatif à cette base.

Enfin, nous avons une map des noms d'os vers leurs indices, car Assimp utilise des chaînes de caractères pour le nom des os.

Mais pour nous, il sera beaucoup plus simple de travailler avec des indices d'os.

Maintenant, descendons vers `main`.

Et nous avons vu cela dans la première partie.

Ainsi, très brièvement, `main` appelle `ParseScene`, qui appelle `ParseMeshes`.

Et ici nous redimensionnons `MeshBaseVertex` en utilisant le nombre de maillages dans la scène.

Ainsi, pour chaque maillage, nous avons un indice de base, que nous devons calculer.

Et nous faisons cela juste ici, le nombre total de sommets est augmenté pour chaque maillage.

Ainsi, avant de l'augmenter pour le maillage actuel, nous sauvegardons le nombre total actuel de sommets comme base, nous redimensionnons également `VertexToBones` en fonction du nombre total mis à jour de sommets, car nous allons avoir besoin de cet espace lorsque nous analyserons le maillage.

Maintenant, ce n'est pas la manière la plus efficace de faire cela.

Mais pour un utilitaire comme celui-ci, c'est correct.

Fondamentalement, ce vecteur est redimensionné encore et encore pour chaque nouveau maillage avec juste assez d'espace pour ce maillage.

Enfin, nous appelons `ParseMeshBones`.

Et vous remarquerez peut-être que j'ai ajouté l'indice du maillage actuel, car nous allons en avoir besoin plus tard.

`ParseMeshBones` n'a pas changé, nous appelons simplement `ParseSingleBone` pour chaque os avec l'ajout de l'indice du maillage dans le premier paramètre.

Dans la première partie, cette fonction affichait simplement tous les sommets affectés par l'os actuel et leurs poids.

J'ai ajouté du code ici pour créer le mappage des sommets vers les os.

D'abord, nous obtenons le `BoneID`, qui est un indice unique pour chaque os.

À l'intérieur de la boucle, nous calculons l'ID global du sommet en ajoutant le `mVertexId` de la structure `aiVertexWeight` à l'ID du sommet de base du maillage actuel, que nous avons défini dans la fonction `ParseMeshes`.

Juste ici.

Chaque maillage a un lot de sommets et les os qui les référencent utilisent des indices qui commencent à zéro, nous voulons empiler tous les indices de tous ces lots ensemble, les uns après les autres, car nous les chargeons ainsi dans le tampon de sommets.

Nous devons donc rendre ces indices uniques.

Ainsi, le premier lot commence à zéro, puis la base du lot suivant commence là où le lot précédent s'est terminé.

Passons à `GetBoneID`, qui mappe le nom de l'os à son indice unique.

Nous avons une map entre une chaîne de caractères et un entier appelée `BoneNameToIndexMap`.

Si le nom existe déjà, nous renvoyons simplement l'indice.

Et sinon, nous définissons le mappage et le `BoneID` s'incrémente simplement automatiquement au fur et à mesure que nous ajoutons des éléments dans la map. Retour à `ParseSingleMesh`.

Maintenant que nous avons l'ID global du sommet, nous l'utilisons pour accéder au tableau `VertexToBones`, qui, je vous le rappelle, est un vecteur de structures `VertexBoneData`.

Et nous appelons `AddBoneData` avec l'indice de l'os actuel et le poids qui provient de la structure `aiVertexWeight`.

Cette fonction cherche un emplacement libre dans le tableau des poids et place l'ID de l'os et le poids dans cet emplacement.

Nous supposons que si le poids est nul, alors cet emplacement est libre car le poids doit être supérieur à zéro pour que l'os influence réellement ce sommet.

Une fois que nous avons trouvé l'emplacement libre et effectué la mise à jour, nous pouvons quitter la fonction. Si nous ne trouvons pas d'emplacement libre, il y aura une assertion car soit vous avez un bug, soit vous devez augmenter le nombre maximum d'os par sommet.

Lançons maintenant ceci sur notre fichier `boblampclean.md5mesh`.

Et vous pouvez voir que nous obtenons l'ID du sommet, l'indice de l'os, le poids et l'indice de l'emplacement où cette information a été enregistrée.

Faisons un peu de magie avec `awk`, récupérons `vertex` et demandons à `awk` d'afficher juste les valeurs de cette ligne.

D'accord, nous avons donc l'ID du sommet à l'indice 3, l'indice de l'os à 5, le poids à 7 et l'emplacement à 9. Ça fonctionne.

Nous pouvons trier cela numériquement par les ID de sommets et nous pouvons voir que le premier sommet est entièrement influencé par l'os numéro 2, le deuxième sommet est influencé par les os 2 et 3.

Et nous avons leurs poids aux emplacements 0 et 1.

Cela semble donc logique.

Le sommet 8 est influencé par 11, 2 et 3.

Cela semble donc correct également.

Si vous voulez, vous pouvez vérifier cela plus en profondeur.

Mais je pense que pour l'instant c'est bon.

L'étape suivante sera d'intégrer cette logique dans notre application OpenGL et de charger réellement les indices et les poids des os par sommet dans un tampon de sommets.

Nous pourrons ensuite y accéder depuis le vertex shader, et faire des choses sympas comme appliquer une couleur à tous les pixels qui sont affectés par un certain os.

Encore une fois, c'est juste pour le débogage mais nous progressons par petits pas et s'assurer à chaque étape que tout fonctionne correctement est très utile.

Pour l'intégration, j'ai copié les fichiers d'en-tête et cpp `ogldev_basic_mesh` dans ce répertoire et je les ai renommés `skinned_mesh.h` et `.cpp`.

Le prochain tutoriel inclura une nouvelle version des mêmes fichiers dans son propre répertoire, vous pourrez donc comparer les deux révisions. `ogldev_basic_mesh` a déjà été couvert dans un tutoriel précédent, je mettrai un lien ci-dessous vers cette vidéo. Pour l'instant, nous allons juste couvrir le code lié à l'animation squelettique.

Cette classe s'appelle `SkinnedMesh`, comme l'en-tête.

Et ici nous avons le nombre max d'os par sommet.

`VertexBoneData` est ici comme une déclaration privée, et c'est la même que dans le sandbox, donc pas besoin d'y revenir, nous allons utiliser un nouveau tampon de sommets pour les os en plus de l'indice, de la position, des coordonnées de texture et des normales, nous avons donc une nouvelle énumération pour le tampon de sommets des os (`BONE_VB`), nous avons les déclarations de trois fonctions que j'ai simplement copiées du sandbox : `LoadMeshBones`, `LoadSingleBone` et `GetBoneID`. J'utilise le mot `Load` au lieu de `Parse` car c'est plus courant.

Dans cette classe, nous avons un vecteur de `VertexBoneData`, encore une fois le même que dans le sandbox, nous allons l'utiliser pour remplir un tampon de sommets pour les os.

Et enfin, la map entre le nom de l'os et son indice.

Passons maintenant au fichier CPP, nous avons deux nouveaux emplacements d'attributs de sommets pour le vertex shader.

Cela permettra à chaque sommet d'accéder à sa liste d'os et aux poids. Assurez-vous de garder ces numéros synchronisés avec le vertex shader.

Dans la fonction `ReserveSpace`, nous redimensionnons le vecteur d'os en fonction du nombre de sommets. D'accord, c'est donc la même chose que pour tous les autres tampons ici.

Dans `InitSingleMesh`, j'ai ajouté un appel à `LoadMeshBones` qui appelle `LoadSingleBone` qui utilise `GetBoneID` pour mapper le nom de l'os à son indice.

D'accord, encore une fois, cela fonctionne de la même manière que dans l'utilitaire Assimp.

Fondamentalement, lorsque le traitement de la structure de scène est terminé, nous avons tout le mappage des sommets vers les os dans ce vecteur `m_Bones`, et ensuite, dans la fonction `PopulateBuffers`, nous lions et allouons le nouveau tampon de sommets pour les os.

Nous avons également activé les deux attributs de sommets pour accéder aux ID d'os et aux poids, nous devons également configurer la disposition correctement.

Ainsi, pour les ID d'os, assurez-vous d'utiliser `GL_INT`, et non `GL_FLOAT` comme tous les autres attributs. Nous avons quatre entiers pour les quatre ID, suivis de quatre flottants, assurez-vous de régler le décalage correctement.

Pour le second attribut, nous avons le nombre max d'os multiplié par la taille d'un ID d'os, nous devrions donc avoir 16 octets ici.

D'accord, quatre os multipliés par quatre octets par entier.

Maintenant, je veux m'assurer que le tampon de sommets des os est rempli et chargé correctement.

Ainsi, dans cette démo, nous allons peindre les triangles qui sont affectés par chaque os en utilisant une couleur spécifique.

Voyons comment faire cela.

Dans le vertex shader, nous avons deux nouveaux attributs d'entrée pour les ID d'os et les poids.

Notez que les ID sont des `ivec4` et non un `vec4` régulier.

Le `vec4` régulier est pour les nombres à virgule flottante et les ID sont des entiers.

Nous devons donc utiliser `ivec4`.

Le vertex shader copie simplement les deux attributs vers le fragment shader.

Nous devons donc également les déclarer comme attributs de sortie.

Ici, nous avons besoin du qualificateur de type `flat`.

Pour la première fois, nous avons l'habitude de laisser le rastériseur interpoler les attributs tels que les couleurs et les coordonnées de texture à travers la face du triangle.

Mais dans le cas des ID d'os, cela n'a aucun sens.

Ainsi, ce qualificateur `flat` dit essentiellement au rastériseur de ne pas interpoler, de simplement copier l'attribut tel quel. Nous avons une déclaration correspondante dans le fragment shader.

Et nous devons utiliser `flat` ici aussi.

Si nous l'oublions, nous obtiendrons une erreur disant que les variables entières doivent être `flat`.

Le reste du fragment shader sera simplement copié d'un tutoriel précédent sur l'éclairage et le seul changement est dans la fonction `main`, nous bouclons sur le nombre d'os et nous vérifions chaque emplacement dans l'attribut des ID d'os.

Si celui-ci est égal à `gDisplayBoneIndex`, qui est un attribut uniforme défini par l'application, nous allons voir cela dans une minute.

Si c'est vrai, nous voulons définir la couleur de sortie et ici, j'ai essayé d'imiter le comportement de Blender.

D'accord, donc dans Blender, si vous allez en mode Weight Paint, vous pouvez basculer entre les groupes de sommets, qui sont essentiellement les os, et alors les sommets bleus ne sont pas du tout affectés par l'os sélectionné.

Le rouge est fortement affecté et le vert et le jaune sont quelque part entre les deux.

J'ai essayé de faire une chose similaire dans le fragment shader, d'accord, ce n'est pas parfait, mais c'est assez utilisable.

Si le poids de l'os actuel est supérieur à 0,7, nous sortons du rouge modulé par le poids car il semble que Blender utilise également le poids pour interpoler la couleur entre 0,4 et 0,6, nous utilisons le vert puis le jaune pour tout ce qui est au-dessus de 0,1.

Si l'indice de l'os n'est pas trouvé pour ce pixel, nous utilisons le bleu.

J'ai également multiplié la couleur d'origine qui provient de l'éclairage par une petite fraction, afin de désactiver son effet sans utiliser zéro, pour que le compilateur ne se plaigne pas, les trucs d'éclairage ne sont pas vraiment utilisés, le code de l'application est assez standard, donc pas besoin de tout passer en revue.

La seule chose à noter ici est que lorsque la barre d'espace est pressée, nous incrémentons l'indice d'os affiché actuel, nous utilisons le modulo pour nous assurer de ne pas dépasser le nombre d'os.

Et ensuite nous définissons cet indice dans le fragment shader.

Le fragment shader a un entier uniforme pour cet indice.

Et c'est ce que nous utilisons pour vérifier l'ID de l'os.

Voyons donc comment cela fonctionne.

L'étape suivante consiste à comprendre les matrices qui contrôlent la transformation des sommets pendant l'animation.

Tout cela et bien plus sera couvert dans le prochain tutoriel.

Dans les parties une et deux, nous avons appris comment charger les informations du squelette à l'aide de la bibliothèque Assimp.

Et nous avons créé un mappage pour que chaque sommet puisse accéder aux os qui l'influencent.

Ainsi qu'aux poids.

Nous avons vérifié l'implémentation à l'aide d'une démo simple qui montre les triangles influencés par l'os sélectionné.

Dans cette vidéo, nous allons étudier les transformations de base de la technique d'animation squelettique.

Rappelez-vous que dans la première partie, nous avons parlé de la façon dont vous créez l'apparence de l'animation dans Blender en utilisant un ensemble d'images clés où vous ajustez l'emplacement et l'orientation des os dans chaque image clé.

Maintenant, si c'était un entretien d'embauche et qu'on vous demandait : "Eh bien, étant donné la façon dont Blender fonctionne, comment implémenteriez-vous l'animation en général ?", alors je suppose que spontanément, vous pourriez dire que vous pouvez sauvegarder la position de tous les sommets dans chaque image.

Et ensuite, pendant l'exécution, rendre simplement un ensemble différent de sommets dans chaque image.

Eh bien, je suppose que cela fonctionnerait.

Mais vous pouvez évidemment voir les inconvénients de cette approche.

Cela ferait probablement exploser la taille de vos fichiers de modèles, ainsi que vos tampons de sommets.

Par conséquent, l'approche adoptée par l'algorithme réel est de sauvegarder un seul ensemble de positions, spécifiquement en Bind Pose dont nous avons parlé dans la première partie.

De plus, nous associons un ensemble de transformations à chaque os, une transformation pour chaque image clé.

Pendant l'exécution, nous effectuons une moyenne pondérée de toutes les transformations qui affectent chaque sommet.

En pratique, Assimp sauvegarde en fait les transformations séparément : un vecteur pour la mise à l'échelle, un autre vecteur pour la translation, et un quaternion pour la rotation.

Nous savons déjà comment créer des matrices de transformation à partir de ces éléments.

Il n'y a donc pas de problème là-bas, nous avons seulement besoin de comprendre comment appliquer ces matrices sur le modèle.

Parce que ce n'est pas si simple.

Il y a une complexité supplémentaire due au fait que nous voulons qu'un os parent affecte l'os enfant, mais pas l'inverse.

Ainsi, si le doigt bouge, cela n'affecte pas la main.

Mais quand la main bouge, évidemment, les doigts bougent aussi.

Pour comprendre comment tout cela fonctionne, nous devons introduire un nouveau système de coordonnées, appelé système de coordonnées de l'os, ou espace de l'os. L'origine du système de coordonnées de l'os se trouve à la base de l'os.

L'os lui-même pointe le long de l'axe Y, et les axes X et Z sont perpendiculaires à l'axe Y et entre eux.

Bien sûr, vous pouvez activer l'affichage de ce système de coordonnées dans Blender en sélectionnant l'armature.

En allant dans l'onglet "Object Data Properties" et dans "Viewport Display", vous avez une case à cocher appelée "Axes".

Nous savons qu'en général, les sommets du maillage sont spécifiés par rapport à un système de coordonnées local.

Ainsi, quelle est la relation entre le système de coordonnées local et le système de coordonnées de l'os ? Eh bien, les os forment une hiérarchie, qui est un graphe simple, il y a une racine (root) au sommet et chaque nœud a zéro ou plusieurs enfants, chaque nœud sauf la racine a un seul parent.

Lors du rigging d'un nouveau modèle, l'artiste désignera un os au cœur du modèle comme racine, les os restants se ramifieront à partir de cette racine et les uns des autres.

Dans le cas d'un modèle humain simple, il est logique d'utiliser la colonne vertébrale comme racine, puis les enfants immédiats seront les quatre membres et le cou.

De là, vous pouvez continuer jusqu'aux doigts. L'espace de l'os de la racine est spécifié par rapport à l'espace local.

Vous pouvez donc considérer l'espace local comme un système de coordonnées primaire avec l'origine (0,0,0) et les axes habituels (1,0,0), (0,1,0) et (0,0,1). La base de l'os racine sera un point dans ce système, tout comme les sommets réguliers, et les axes de l'os racine seront des vecteurs dans ce système.

Dans l'exemple 2D suivant, l'origine de l'espace de l'os de la racine est située à 1 sur le X et 1 sur le Y et les axes de l'espace de l'os sont des vecteurs unitaires arbitraires, les choses deviennent un peu plus complexes.

Lorsque nous passons de la racine de la hiérarchie à ses enfants immédiats, l'espace de l'os des enfants est défini par rapport à la racine plutôt que par rapport à l'espace local.

En revenant à l'exemple, nous pouvons voir la racine de la hiérarchie à 1 sur le X et 1 sur le Y.

Et la base de l'os enfant est également à 1 sur le X et 1 sur le Y mais par rapport à son parent, qui est la racine.

Par rapport à l'espace local, l'os de l'enfant est en fait situé à 2 sur le X et 2 sur le Y.

Dans cet exemple, j'ai aligné les axes des deux espaces d'os avec les axes de l'espace local pour me faciliter le calcul mental.

Mais évidemment, il n'est pas nécessaire qu'il en soit ainsi.

En définissant chaque espace d'os comme une référence à son parent, nous pouvons créer une chaîne de transformations qui va de chaque os jusqu'à la racine de la hiérarchie.

Un changement dans la transformation d'un nœud affectera évidemment tous ses descendants, mais pas ses parents.

Si vous avez besoin d'une intuition sur la façon dont cela fonctionne, vous pouvez prendre le modèle de l'univers comme exemple, vous pouvez tracer l'orbite de la lune autour de la terre dans un système de coordonnées centré sur la terre.

Le parent de ce système de coordonnées est évidemment celui où la Terre orbite autour du Soleil.

Ainsi, si vous voulez calculer l'emplacement de la lune par rapport au soleil, vous devez prendre ses coordonnées dans le système d'origine et les multiplier par la transformation du système d'origine vers le système de coordonnées où le soleil est à l'origine.

L'étape suivante sera de multiplier le résultat par la transformation du système de coordonnées du soleil vers le système de coordonnées où le soleil orbite autour du centre de la galaxie ou quelque chose comme ça.

La transformation finale sera du système de coordonnées de la Galaxie vers le système de coordonnées de l'univers et cela vous donnera les coordonnées de la lune dans l'univers.

Je ne suis pas sûr que les astronomes professionnels approuveraient ce modèle.

Mais je pense que pour nous, c'est correct, en revenant aux os.

Le processus dans l'animation squelettique commence par transformer la position d'un sommet qui est donnée comme d'habitude dans l'espace local, alors que le modèle est en Bind Pose, vers le système de coordonnées d'un os qui l'influence.

De là.

Nous le transformons vers l'espace de l'os du parent et nous continuons jusqu'à ce que nous arrivions à la racine de la hiérarchie.

À la fin du processus, nous sommes de retour dans l'espace local, qui est l'endroit où la racine est définie.

Et nous pouvons continuer vers l'espace de vue comme d'habitude.

Il y a un petit détail ici avec Assimp connu sous le nom de transformation inverse globale (`global inverse transform`), dont vous avez peut-être entendu parler, et j'en parlerai plus tard.

Puisque chaque sommet est souvent influencé par plus d'un os, nous devons en fait faire une moyenne pondérée des transformations de plusieurs os.

Chaque transformation d'os sera calculée de la même manière en remontant de l'os jusqu'à la racine.

En plus de cela, nous devons également ajuster la transformation de chaque nœud.

Au fur et à mesure que le temps progresse, sinon, il n'y aura aucun mouvement. Pour implémenter réellement ce processus,

Assimp nous fournit deux matrices.

La première est appelée la matrice de décalage (`offset matrix`), et elle fait partie de la structure de l'os, qui contient également tous les poids pour les sommets.

Cette matrice transforme de l'espace local directement vers l'espace de l'os, et elle contient déjà toutes les transformations qui vont de la racine jusqu'à l'os.

Ainsi, vous n'avez pas besoin de vous soucier de la hiérarchie.

Lorsque vous utilisez cette matrice.

La documentation officielle dit que la matrice de décalage transforme de l'espace du maillage vers l'espace de l'os en Bind Pose, ce qui revient essentiellement à dire que si vous prenez un sommet dans l'espace local, alors que le modèle est en Bind Pose, et que vous le multipliez par la matrice de décalage d'un os, vous obtiendrez les coordonnées du sommet par rapport à cet os.

Cela signifie que si deux os influencent le même sommet, alors en multipliant la position du sommet par la matrice de décalage de chaque os séparément, vous obtiendrez deux coordonnées différentes par rapport aux deux espaces d'os.

Bien sûr, vous devrez remonter de chaque os vers la racine et calculer la matrice finale pour chaque os.

Si vous transformez le sommet par les deux matrices finales, et en supposant que les deux os bougent, vous obtiendrez deux positions différentes dans l'espace local, c'est pourquoi nous faisons une moyenne pondérée des deux matrices finales pour obtenir une position quelque part entre les deux os.

Pour l'exemple suivant, j'ai créé le squelette le plus simple du monde dans Blender avec la boîte standard à l'origine, et un seul os qui est aligné avec l'axe Y qui est vert.

Comme vous pouvez le voir, l'axe Z de l'os pointe vers le haut, ce qui est en fait le défaut dans Blender. J'ai exporté le modèle dans cette configuration pour rester simple, sinon Blender ajouterait des transformations de son propre système de coordonnées vers celui que nous utilisons.

Et cela compliquerait l'analyse. Retour à notre sandbox Assimp.

Dans la fonction `ParseSingleBone`, j'ai ajouté un appel pour afficher la matrice Assimp en utilisant l'attribut `mOffsetMatrix` de l'os comme paramètre. `PrintAssimpMatrix` est définie plus haut, et elle est très simple, elle affiche juste la matrice proprement.

Lançons maintenant ceci sur le modèle `single_bone.fbx` qui est dans le dépôt Git, nous pouvons voir que nous obtenons la matrice identité comme matrice de décalage.

La raison est, bien sûr, que la base de l'os est à l'origine de l'espace local et les axes de l'espace de l'os sont alignés avec ceux de l'espace local.

Ainsi, transformer de l'espace local vers l'espace de l'os signifie essentiellement ne rien faire, c'est le même système.

Voyons un autre exemple.

J'ai ajouté un os enfant qui prolonge l'os racine le long de l'axe Y, nous pouvons voir dans Blender que l'os racine est situé à l'origine et la fin de l'os est à une unité sur le Y. L'os enfant commence au même endroit et se termine à deux unités sur le Y.

Si nous lançons ceci en utilisant le sandbox, nous pouvons voir que la matrice de décalage du parent est toujours la matrice identité.

Mais la matrice de décalage de l'enfant nous translatera d'une unité le long de l'axe Y négatif.

Et cela a du sens car cet espace d'os est décalé d'une unité sur le Y positif, donc pour transformer un sommet, par exemple, celui-ci juste ici, qui dans l'espace local est à 2 sur le Y vers l'espace d'os de l'enfant, nous devons soustraire une unité du Y parce que le sommet est plus proche de la base de l'os que de l'origine.

J'ai un dernier exemple ici appelé `two_bones_translation_rotation.fbx` où l'os enfant a été tourné de 45 degrés vers le haut et nous pouvons voir que la matrice de décalage de l'enfant est très similaire à une matrice que nous avons développée par le passé.

Je vous laisse donc le soin d'explorer cela comme devoir.

D'accord, j'espère que tout ce qui a été dit jusqu'à présent était clair.

Nous pouvons maintenant jeter un coup d'œil à la deuxième matrice qui se trouve dans la nouvelle section de la scène Assimp.

C'est la hiérarchie des nœuds.

Le nœud représente une entité dans la scène qui a un emplacement et une orientation par rapport à un parent.

Et une entité peut être des maillages, des os, et même des caméras et de l'éclairage, vous pouvez en fait concevoir une scène entière dans Blender et l'exporter avec la caméra et l'éclairage, puis la charger avec Assimp.

Je ferai peut-être une vidéo à ce sujet à l'avenir.

Mais pour l'instant concentrons-nous sur les os.

La hiérarchie des nœuds commence par un seul nœud racine, et chaque nœud comprend un tableau de pointeurs vers zéro ou plusieurs enfants et un tableau de pointeurs vers zéro ou plusieurs maillages.

Cela vous permet d'avoir un seul maillage dans votre fichier de modèle et de le placer à différents endroits dans le monde en utilisant plusieurs nœuds.

Comme vous pouvez le voir, il est très simple de créer le graphe dont nous avons parlé plus tôt.

En utilisant cette structure de nœuds.

Il y a aussi un pointeur vers un seul parent et la matrice appelée `mTransformation`.

Le rôle de cette matrice est de transformer un vecteur vers le système de coordonnées de son parent.

C'est donc comme la transformation du système de coordonnées de la terre vers le système de coordonnées du soleil.

Après avoir multiplié un vecteur de position par la matrice de décalage, nous nous trouvons dans le système de coordonnées de l'os.

L'étape suivante consiste à trouver le nœud correspondant dans le graphe, à appliquer la matrice de transformation de ce nœud et à continuer tout le chemin jusqu'à la racine.

En parcourant l'attribut parent du nœud.

Les os sont mappés aux nœuds.

Simplement en utilisant leurs noms, vous cherchez le nom de l'os dans la hiérarchie des nœuds jusqu'à ce que vous trouviez le nœud avec le même nom.

Explorons la hiérarchie des nœuds en utilisant notre sandbox Assimp.

Dans la fonction d'analyse.

J'ai ajouté un appel à `ParseHierarchy` que je vais maintenant décommenter. Cette fonction prend la scène en paramètre, puis appelle `ParseNode` en utilisant l'attribut `mRootNode` de la scène. `ParseNode` affiche le nombre de maillages et d'enfants dans le nœud ainsi que la matrice `mTransformation` et parcourt le graphe vers le bas en appelant récursivement `ParseNode` sur chacun de ses enfants.

D'accord, testons-le maintenant.

Sur le premier exemple, `single_bone.fbx`, nous pouvons voir que le nœud racine est la matrice identité, il a deux enfants, le cube et l'armature, la matrice de transformation de l'armature permute les axes Y et Z, et inverse également le signe de la coordonnée Y.

D'accord, intéressant.

L'armature contient un nœud appelé `Bone`.

Et vous pouvez voir que la matrice `mTransformation` ici fait exactement l'inverse.

Elle permute à nouveau les axes Y et Z, et inverse le signe de la coordonnée Z, qui était précédemment le Y.

D'accord, donc ils s'annulent essentiellement l'un l'autre.

Si nous multiplions ces matrices ensemble, nous pouvons vérifier que nous obtenons la matrice identité.

J'ai en fait posé une question à ce sujet sur le forum Assimp.

Et je vous tiendrai au courant quand j'aurai une réponse, il y a en fait un nœud supplémentaire ici appelé `Bone_end` qui, je suppose, est pour la queue de l'os, mais il n'y a pas d'os réel pour ce nœud.

Ainsi, la hiérarchie peut inclure des nœuds qui n'ont pas d'os correspondant.

Mais si ces nœuds ont des enfants, alors ils auront un effet sur eux.

Et nous devrons en tenir compte. La transformation de `Bone_end` translate d'une unité sur l'axe Y.

Et cela a du sens, car `Bone_end` définit également un système de coordonnées.

Ainsi, si vous multipliez l'origine de ce système de coordonnées (0,0,0) par cette matrice, vous obtiendrez (0,1,0) qui est l'emplacement de `Bone_end` dans le système de coordonnées de l'os.

C'est donc un exemple trivial, mais il nous aide à ressentir comment la hiérarchie fonctionne.

Si nous lançons ceci sur un modèle réel, comme notre bon vieux `boblampclean`, nous pouvons voir une hiérarchie beaucoup plus complexe.

Nous avons la racine ici, puis la hiérarchie MD5, l'origine, le pubis, le bassin, la colonne vertébrale, le cou et la tête.

Les transformations ici sont trop complexes.

Alors espérons simplement que tout fonctionnera correctement.

L'étape suivante consiste à intégrer les deux matrices dans notre classe `SkinnedMesh`.

Tout cela et bien plus sera couvert dans le prochain tutoriel.

Aujourd'hui, nous allons intégrer les deux matrices que nous avons découvertes dans la vidéo précédente, le décalage (`offset`) et la transformation, dans notre classe `SkinnedMesh`.

Cela comprend deux étapes.

D'abord, nous devons transformer le sommet de l'espace local vers l'espace de l'os en utilisant la matrice de décalage.

Ensuite, nous devons multiplier la position dans l'espace de l'os par la matrice de transformation du nœud et continuer à multiplier tout en parcourant la hiérarchie jusqu'au sommet.

Cela nous ramènera à l'espace local.

Ainsi, nous avons commencé dans l'espace local et nous avons fini dans l'espace local.

Alors, qu'est-ce qui a changé ? Eh bien, fondamentalement rien.

Dans ce tutoriel, nous n'appliquons toujours pas les données d'animation, qui sont ce qui anime réellement le modèle.

Nous appliquons juste les transformations de base calculées quelque part entre Blender et Assimp.

L'attente est donc que nous récupérions le modèle en mode Pose.

Maintenant, rappelez-vous qu'en plus des matrices, nous allons utiliser les poids pour effectuer une moyenne pondérée des transformations.

Ainsi, ce résultat est loin d'être négligeable.

C'est une étape importante sur le chemin de notre destination finale.

D'accord, passons donc en revue les changements dans la classe `SkinnedMesh`.

Et nous commençons par `skinned_mesh.h`, j'ai ajouté une fonction publique appelée `GetBoneTransforms`, cette fonction sera appelée dans la boucle de rendu.

Elle calcule essentiellement toutes les transformations pour tous les os et les renvoie dans un vecteur de matrices, que l'appelant doit fournir en tant que référence.

Chaque os a une seule matrice à laquelle nous pouvons accéder dans le vecteur en utilisant son ID d'os.

Dans l'implémentation finale, cette fonction prend également le temps actuel en paramètre, puis elle renvoie un ensemble différent de matrices à chaque appel, basé sur la posture actuelle du modèle.

Dans ce tutoriel, nous n'en avons pas encore besoin.

Je l'ai donc laissé de côté pour l'instant, dans la section privée, j'ai ajouté une fonction appelée `ReadNodeHierarchy`.

Je parlerai plus en détail de cette fonction quand nous arriverons à l'implémentation de cette classe.

J'ai également ajouté l'objet `Assimp::Importer`, et le pointeur vers l'objet `aiScene` comme attributs privés.

Et la raison est que nous devrons accéder à la hiérarchie dans la scène.

pendant l'exécution, quand j'ai essayé de le faire dans l'implémentation précédente, où l'importateur était une variable locale dans la fonction `LoadMesh`, j'ai eu une erreur de segmentation.

Je suppose donc que nous devons garder l'importateur en vie tout au long de l'exécution.

Et enfin, nous avons une structure appelée `BoneInfo`, qui stocke quelques matrices, nous avons la matrice de décalage de l'os, qui est ici pour un accès facile.

`FinalTransformation` stocke les résultats intermédiaires de toute la chaîne de transformation de sorte que lorsque tout le processus est terminé, nous le récupérons simplement d'ici et le renvoyons à l'application.

Le constructeur de cette classe prend la matrice de décalage en paramètre, il la stocke dans le membre correspondant.

Et il initialise la matrice de transformation à zéro.

Et bien sûr, nous avons aussi un vecteur de structures `BoneInfo`, une structure pour chaque os.

D'accord, cela conclut les changements dans l'en-tête.

Comme toujours, vous pouvez comparer ce fichier à la version précédente, en fait, dans la deuxième partie, parce que dans la troisième partie, nous n'avons touché qu'au sandbox, et vous pourrez voir tous ces changements.

Jetons maintenant un coup d'œil au fichier CPP, nous avons un changement mineur dans la fonction `LoadMesh`.

Au lieu des variables locales pour l'importateur et la scène, nous avons les nouveaux attributs privés dans la classe, nous allons donc les utiliser. Le changement suivant est dans la fonction `LoadSingleBone`.

Après avoir obtenu l'ID de l'os, nous vérifions s'il est égal à la taille du vecteur `m_BoneInfo`.

Si cela s'avère vrai, nous savons qu'il s'agit d'un nouvel os, car les ID d'os sont un index courant.

Dans ce cas, nous créons un objet `BoneInfo` en utilisant la matrice `mOffsetMatrix` de la classe `aiBone` d'Assimp.

Rappelez-vous qu'en plus des poids, la classe `aiBone` possède également cette matrice de décalage.

Après avoir initialisé l'objet `BoneInfo`, nous l'ajoutons au vecteur.

Cela signifie que nous pouvons accéder aux informations de l'os en utilisant l'indice de l'os.

Au bas de ce fichier, nous avons les deux nouvelles fonctions.

D'abord, nous avons `GetBoneTransforms`, qui prend une référence à un vecteur de matrices.

Nous commençons par redimensionner ce vecteur en utilisant le nombre de structures `BoneInfo` que nous avons.

Ensuite, nous initialisons la matrice locale pour qu'elle soit la matrice identité.

Et nous appelons `ReadNodeHierarchy` en utilisant le nœud racine de la scène.

Et cette matrice, après le retour de `ReadNodeHierarchy`, nous devrions avoir les transformations dont nous avons besoin dans le membre `FinalTransformation` du vecteur `m_BoneInfo`.

Tout ce que nous avons à faire est donc de copier ces matrices dans le vecteur fourni par l'appelant.

Jetons maintenant un coup d'œil à la fonction `ReadNodeHierarchy`.

Qui est un peu délicate car c'est une fonction récursive.

Elle prend un pointeur vers un objet `aiNode` et une référence à une matrice parente.

Le premier appel à cette fonction est fait en utilisant le nœud racine de la hiérarchie et la matrice identité.

Nous commençons par créer une matrice de transformation de nœud en utilisant la matrice `mTransformation` du nœud.

Ensuite, nous créons une matrice de transformation globale en multipliant la matrice parente par cette matrice.

Ainsi, nous parcourons réellement le graphe de haut en bas plutôt que du nœud vers la racine, car cette matrice globale va être utilisée dans le calcul de tous ses enfants, donc en allant de haut en bas, nous pouvons la calculer une seule fois.

Notez que nous profitons de la nature associative de la multiplication matricielle, qui nous dit que tant que nous gardons l'ordre des matrices, nous pouvons changer l'emplacement des parenthèses.

Ensuite, nous vérifions si nous avons un os qui correspond au nom du nœud, tous les os ont un nœud correspondant dans la hiérarchie.

Mais il peut y avoir des nœuds sans os, nous avons déjà une map entre les noms d'os et leurs indices.

C'est donc très facile à faire.

Si nous trouvons un tel os, nous mettons à jour sa transformation finale pour qu'elle soit le résultat de la multiplication de sa matrice de décalage par la matrice globale, qui capture essentiellement toute la chaîne du nœud vers la racine.

Enfin, nous parcourons les enfants du nœud actuel, et nous appelons `ReadNodeHierarchy` de manière récursive sur chaque nœud enfant avec la matrice de transformation globale dans le deuxième paramètre.

Ainsi, au fur et à mesure que nous nous enfonçons dans le graphe, cette transformation globale encapsule de plus en plus de matrices `mTransformation`.

Jetons un coup d'œil aux changements dans le code de l'application.

Et c'est très simple.

Dans la fonction de rendu, nous définissons un vecteur de matrices, nous obtenons les transformations d'os du maillage, et nous bouclons sur le vecteur que nous avons récupéré, nous définissons les matrices dans la technique de skinning une par une.

C'est une fonction très simple qui met à jour le tableau uniforme dans le shader, donc je vais passer et vous pourrez y jeter un coup d'œil plus tard.

Le dernier changement est dans le vertex shader, nous avons un nouvel uniforme appelé `gBones`.

C'est un tableau de 100 matrices, assurez-vous que c'est suffisant pour les modèles que vous prévoyez de charger.

Dans la fonction `main`, nous créons une matrice de transformation d'os comme une moyenne pondérée des matrices de tous les os qui influencent le sommet actuel, nous utilisons les ID d'os du sommet pour accéder au tableau uniforme `gBones`.

Jetez un coup d'œil à la deuxième partie si vous ne vous souvenez pas d'où viennent les ID d'os, chaque matrice d'os est multipliée par le poids correspondant, qui est également un attribut de sommet.

Si le nombre d'os est inférieur à quatre, le poids sera nul, donc le calcul n'aura aucun effet.

Nous additionnons les résultats de toutes ces multiplications pour obtenir la transformation d'os finale et nous l'utilisons pour transformer le sommet de l'espace local vers l'espace local à nouveau. Une fois que nous aurons intégré les données d'animation, la position sera différente de l'originale.

Le shader continue comme d'habitude en multipliant la position locale mise à jour par la matrice WVP, il n'y a en fait aucun changement dans le fragment shader.

Cela conclut donc cette vidéo.

La prochaine étape est d'intégrer les données d'animation afin que nous puissions enfin voir quelque chose bouger.

Tout cela et bien plus sera couvert dans le prochain tutoriel.

Bienvenue dans la cinquième et dernière partie de la série de tutoriels sur l'animation squelettique. D'accord, cela signifie essentiellement que nous devons faire fonctionner l'animation d'ici la fin de cette vidéo.

Mais d'abord, faisons une vérification rapide de ce que nous savons déjà sur les structures de données Assimp pertinentes.

La classe `aiScene` possède une liste de maillages et chaque maillage possède une liste d'os pour chaque os.

En plus des poids et de la matrice de décalage, nous avons également un nœud correspondant dans la hiérarchie des nœuds.

Le nœud possède une matrice de transformation qui nous amène au système de coordonnées de son parent.

Dans le tutoriel précédent, nous avons vu comment ces deux matrices fonctionnent ensemble, alors assurez-vous de regarder cette vidéo d'abord.

La classe `aiScene` possède également un tableau de structures `aiAnimation`.

Chaque structure représente la séquence d'animation complète, telle que courir, se battre, ou tout ce que le personnage peut faire.

Il y a quelques attributs liés au temps dans cette structure, nous avons `mDuration`, qui est la durée de l'animation en ticks et `mTicksPerSecond`, qui est essentiellement la fréquence d'images prévue de l'animation définie par l'artiste.

Ainsi, par exemple, si la fréquence d'images est de 30, et que votre jeu tourne à 60 images par seconde, vous devrez interpoler une image supplémentaire entre deux images d'animation consécutives, et vice versa.

Si le jeu est plus lent que le modèle animé, nous devrons sauter des images pour maintenir le rythme prévu de l'animation.

Évidemment, si nous divisons la durée par les ticks par seconde, nous obtenons la durée de l'animation en secondes réelles.

L'attribut le plus important dans `aiAnimation` est un tableau de structures `aiNodeAnim` appelé `mChannels`.

La taille du tableau est donnée dans `mNumChannels`.

Chaque nœud animé dans la hiérarchie possède une entrée correspondante dans ce tableau.

Ainsi, si nous allons dans la déclaration de `aiNodeAnim`, nous pouvons voir qu'elle possède un membre appelé `mNodeName`.

Afin de trouver les données d'animation pour un nœud spécifique dans la hiérarchie, nous avons juste besoin de trouver son nom.

Dans le tableau `mChannels`.

Les paramètres d'animation eux-mêmes sont donnés dans trois tableaux séparés : la position et la mise à l'échelle sont données en vecteurs et la rotation est un quaternion.

Chaque tableau peut théoriquement avoir une longueur différente, c'est pourquoi nous avons `mNumPositionKeys`, `mNumRotationKeys` et `mNumScalingKeys`.

Dans notre exemple, nous avons 140 entrées de position et de rotation, et aucune mise à l'échelle.

Le code doit être flexible.

Pour gérer tous les cas disponibles, `aiVectorKey` et `aiQuatKey` sont en fait une paire d'attributs qui représentent la transformation.

Et le temps auquel cette transformation doit avoir lieu.

Les clés sont garanties d'être triées dans leur ordre chronologique.

Ainsi, chercher le temps actuel signifie simplement parcourir le tableau jusqu'à ce que nous trouvions la plage de temps entre deux clés consécutives dans laquelle se situe le temps actuel.

En supposant que le temps actuel tombera généralement entre deux clés, nous devons interpoler entre les paramètres d'animation de ces deux clés.

Après avoir interpolé les paramètres d'animation, nous combinons la mise à l'échelle, la rotation et la translation en une seule matrice de transformation.

Et c'est essentiellement tout.

Alors maintenant, sautons dans le code et voyons comment l'implémenter réellement.

Cette fois, j'aimerais commencer par le code de l'application où nous avons un changement mineur, à savoir le suivi du temps.

J'ai ajouté un nouvel attribut privé pour le temps de démarrage en millisecondes.

Et lorsque nous avons terminé avec la fonction `Init`, nous l'initialisons en appelant `GetCurrentTimeInMillis`.

Cette fonction est définie dans `common/ogldev_utils.cpp`.

Et vous pouvez voir que nous avons en fait une implémentation différente pour Windows et Linux.

Sur Windows, nous utilisons `GetTickCount` et sur Linux, nous utilisons `gettimeofday`.

Ces deux fonctions sont très simples, et vous pouvez consulter la documentation par vous-même pour plus de détails.

Maintenant, il existe également des minuteries haute résolution que vous pouvez utiliser si vous avez besoin de plus de précision, mais je me contente du niveau de la milliseconde.

D'accord, donc dans la fonction de rendu, nous avons juste besoin d'appeler `GetCurrentTimeInMillis` à nouveau, et de calculer le delta entre le temps de démarrage et le temps actuel, ce qui nous donnera le temps écoulé depuis le lancement de l'application.

Notez que nous divisons le résultat par 1000 ici et le convertissons en flottant.

Ainsi, nous obtenons le temps d'animation en secondes avec des fractions possibles entre les secondes.

Nous fournissons le temps d'animation à `GetBoneTransforms`, afin que nous puissions calculer les transformations correctes pour le point actuel dans le temps.

D'accord, pendant l'enregistrement, j'ai oublié de vous dire que `GetBoneTransforms` doit convertir le temps en secondes en ticks, car Assimp spécifie le temps de début pour chaque image en ticks.

Nous faisons cela en multipliant le temps en secondes par le nombre de ticks par seconde.

Les ticks par seconde peuvent être trouvés dans la structure `aiAnimation`.

Et au cas où cela n'aurait pas été défini par le logiciel de modélisation, nous le fixons à 25 par défaut, ce qui est simplement la valeur que j'ai vue dans les sources d'Assimp.

L'étape suivante dépend de la logique de votre jeu.

Si vous voulez exécuter la séquence d'animation une seule fois, vous devez réinitialiser le temps de démarrage au point où l'animation est censée commencer.

Dans cette démo, je veux que l'animation tourne en boucle.

J'utilise donc `fmod` pour effectuer une opération de modulo sur le temps actuel en ticks et la durée de l'animation.

Cela divise toute l'exécution de la démo en segments de longueur `mDuration`, et dans le temps d'animation en ticks, nous obtenons le temps actuel à l'intérieur de ce segment.

Passons maintenant directement à l'implémentation de la classe `SkinnedMesh`.

Et dans la troisième partie, j'ai mentionné la transformation inverse globale, donc je veux en parler une seconde.

L'idée est que dans certains modèles chargés par Assimp, la matrice de transformation du nœud racine peut en fait être la transformation mondiale de l'objet.

Cela vous permet de placer l'objet dans le monde directement dans Blender.

Dans ce cas, nous devons ramener l'objet dans l'espace local, appliquer l'animation dans l'espace local puis transformer l'objet vers l'endroit où vous voulez qu'il soit.

Afin de faire cela, nous devons inverser la transformation du nœud racine et l'appliquer à la fin de toute la chaîne de transformation.

Ainsi, après avoir chargé le modèle, nous récupérons la matrice `mTransformation` du nœud racine.

Nous la stockons dans un nouvel attribut privé appelé `m_GlobalInverseTransform`, et nous appelons la fonction `Inverse` afin d'inverser cette matrice.

La fonction `Inverse` est définie dans `math_3d.cpp`.

Et c'est une implémentation standard de l'inversion de matrice, que vous pouvez trouver dans de nombreuses ressources en ligne.

Donc rien de spécial ici, la transformation inverse globale est utilisée dans la fonction `ReadNodeHierarchy`, vous pouvez voir que je l'ai ajoutée en tête de la chaîne de transformation.

Ainsi, la transformation finale d'un os est d'abord la matrice de décalage pour aller de l'espace local à l'espace de l'os.

Ensuite, nous avons la transformation globale, qui capture toutes les transformations de nœuds jusqu'à la racine de la hiérarchie, et enfin, la matrice globale inverse.

D'accord, j'espère que cela a du sens.

Revenons maintenant au haut de cette fonction, nous obtenons le temps d'animation en secondes en tant que paramètre de l'application.

La chose suivante que nous devons faire est d'accéder à la séquence d'animation qui nous intéresse.

Dans ce tutoriel, je reste simple.

J'utilise donc la première animation par défaut.

Mais si vous savez que votre modèle a plusieurs animations, vous pouvez chercher celle que vous voulez dans le tableau d'animations.

Ensuite, nous devons chercher à l'intérieur de la structure `aiAnimation` le `aiNodeAnim` qui correspond au nœud actuel.

Et nous faisons cela dans la fonction `FindNodeAnim`, qui est définie juste ici, elle prend la structure `aiAnimation` et le nom du nœud, et elle parcourt simplement les canaux de l'animation jusqu'à ce qu'elle trouve celui qui correspond au nom du nœud.

Dans ce cas, elle renvoie la structure `aiNodeAnim` correspondante.

Tous les nœuds ne sont pas animés.

Et dans ce cas, nous renvoyons `NULL`. De retour à `ReadNodeHierarchy`.

Si des données d'animation ont été trouvées, nous calculons la matrice de transformation.

Pour l'animation, nous allons couvrir le calcul dans un instant.

Mais avant de faire cela, je veux que vous prêtiez attention à quelque chose de très important.

Lorsque le nœud actuel a des données d'animation, nous écrasons la matrice de transformation du nœud qui a été initialisée par la matrice `mTransformation` du graphe.

Et l'explication peut être trouvée dans la documentation qui nous dit que la matrice de transformation calculée à partir de ces valeurs remplace la matrice de transformation originale du nœud à un moment spécifique.

Cela signifie que toutes les clés sont absolues et non relatives à la pose par défaut de l'os.

D'accord, donc si vous vous attendiez à ce que la matrice d'animation soit appliquée par-dessus la transformation du nœud, ce n'est pas le cas. Si le nœud n'est pas animé, nous continuons le processus avec la matrice de transformation du graphe.

Mais s'il a une animation, nous devons écraser cette matrice avec celle que nous allons calculer.

Vous devez donc être prudent ici, sinon vous obtiendrez n'importe quoi.

La matrice de transformation de l'animation est calculée en initialisant trois matrices séparées pour la mise à l'échelle, la rotation et la translation, et en les combinant comme d'habitude en une seule matrice.

Par exemple, voyons comment la matrice de mise à l'échelle est calculée.

Nous préparons un vecteur pour la mise à l'échelle et notez que j'utilise la structure de vecteur d'Assimp ici, `aiVector3D`, nous appelons `CalcInterpolatedScaling` avec le vecteur de mise à l'échelle, le temps d'animation et la structure d'animation du nœud.

Cette fonction commence par vérifier le nombre de clés de mise à l'échelle que nous avons.

S'il n'y a qu'une seule clé, il n'y a pas de place pour l'interpolation, nous renvoyons donc simplement la valeur de la première clé.

S'il y a plus d'une clé, nous devons trouver la clé qui correspond au temps actuel.

Les clés sont triées par temps.

Nous devons donc trouver la première clé dont le temps est supérieur au temps actuel et nous devons interpoler entre cette clé et celle juste avant.

Pour faire cela, nous avons `FindScaling`, qui parcourt toutes les clés de mise à l'échelle dans la structure `aiNodeAnim`, et compare le temps actuel au temps de la clé.

Notez que la boucle `for` commence à zéro et s'arrête à une clé avant la fin, car nous vérifions réellement la clé à `i + 1`.

Et si le temps d'animation est inférieur à ce temps, nous renvoyons l'indice `i`. Retour à `CalcInterpolatedScaling`.

Une fois que nous avons l'indice de la bonne clé, l'indice suivant est celui que nous avons trouvé plus un, nous devons interpoler entre ces deux clés.

Et c'est une interpolation linéaire standard, nous calculons le delta de temps entre les deux clés.

Et le facteur d'interpolation est la plage entre le début de la plage de temps que nous avons trouvée et le temps actuel divisé par la longueur de la plage elle-même.

Ainsi, cela nous donnera un facteur entre zéro et un selon la proximité des bords de la plage.

D'accord, donc si nous sommes très proches du début, le facteur sera proche de zéro et si nous sommes presque à la fin, le facteur sera proche de un. La façon dont nous utilisons réellement le facteur est de récupérer les vecteurs de mise à l'échelle des deux indices, en calculant la différence entre eux.

Et alors le résultat est la valeur de départ plus le produit du facteur et de la différence.

Ainsi, cela nous permet d'interpoler en douceur entre les vecteurs de mise à l'échelle, surtout lorsque le jeu tourne à une fréquence d'images plus élevée que celle pour laquelle le modèle a été conçu à l'origine.

En revenant à `ReadNodeHierarchy`, vous pouvez voir que nous utilisons le vecteur de mise à l'échelle interpolé pour initialiser la matrice de mise à l'échelle standard, le calcul de la rotation et de la translation interpolées est exactement le même.

La seule chose qui mérite d'être mentionnée ici est que l'interpolation des deux quaternions est faite en utilisant la fonction `Interpolate` d'Assimp, qui fait partie de la classe `aiQuaternion`.

Nous normalisons également le quaternion avant de le renvoyer à l'appelant, nous combinons les trois matrices de transformation ensemble dans l'ordre standard que vous pouvez également voir dans la documentation : mise à l'échelle, rotation puis translation.

Et c'est tout.

Cela complète donc la mini-série sur l'animation squelettique.

J'espère que vous avez apprécié autant que moi, n'hésitez pas à cliquer sur le bouton "j'aime", à vous abonner, à commenter ci-dessous et je vous verrai dans le prochain tutoriel.