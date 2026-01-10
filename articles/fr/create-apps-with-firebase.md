---
title: Comment créer des applications avec Firebase
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-04-01T00:10:02.000Z'
originalURL: https://freecodecamp.org/news/create-apps-with-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/firebase.png
tags:
- name: Firebase
  slug: firebase
- name: youtube
  slug: youtube
seo_title: Comment créer des applications avec Firebase
seo_desc: "Firebase is a platform developed by Google for creating mobile and web\
  \ applications. \nWe just published a course on the freeCodeCamp.org YouTube channel\
  \ that will teach you how to use Firebase. This is the perfect course for beginners.\
  \ \nAfter learnin..."
---

Firebase est une plateforme développée par Google pour la création d'applications mobiles et web.

Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org qui vous apprendra à utiliser Firebase. C'est le cours idéal pour les débutants.

Après avoir appris les bases de Firebase, vous apprendrez comment intégrer Firebase avec différents Frameworks JavaScript.

Cybernatico a développé ce cours. Il possède une grande expérience de travail avec Firebase.

Voici les sections couvertes dans ce cours :

* Comment configurer Firebase et se connecter à une application front-end
* Authentification Firebase avec différentes méthodes
* Opérations CRUD Firebase
* Firebase Storage pour stocker des fichiers
* Requêtes Firebase Firestore pour filtrer les données
* Écouteur en temps réel Firebase dans la base de données Firestore
* Hébergement Firebase
* Firebase avec différents frameworks JavaScript

Regardez le cours complet ci-dessous ou sur la chaîne YouTube de freeCodeCamp.org (4 heures de visionnage).

%[https://youtu.be/fgdpvwEWJ9M]

### Transcription

(générée automatiquement)

Firebase est une plateforme de Google pour créer des applications mobiles et web.

Dans ce cours, de Cybernatico, vous apprendrez à utiliser les fonctionnalités de Firebase et à intégrer Firebase avec différents frameworks JavaScript.

Firebase.

Voici les outils de développement nécessaires pour créer une application full stack avec authentification, bases de données, stockage de fichiers, outils de sécurité et analyses, pour construire une réplication full stack avec une documentation facile à utiliser.

À la fin de cette vidéo, nous serons capables d'apprendre l'authentification dans Firebase, le fonctionnement des bases de données, le stockage de fichiers et d'images, les téléchargements (uploads), les mises à jour de données et de bases de données, ainsi que les requêtes Firebase.

Et pour finir, nous apprendrons comment héberger une application sur Firebase.

Nous apprendrons également à utiliser Firebase avec des frameworks comme React, JavaScript, Next ou Angular.

Alors, commençons dès maintenant.

Tout d'abord, laissez-moi créer un projet dans Firebase.

Je vais entrer « Firebase front end ».

Continuer.

Je vous montre depuis le début comment faire tout cela.

Ici, j'ai un bac à sable de code (CodeSandbox), qui a deux entrées : e-mail et mot de passe.

Et attaquons d'abord l'authentification.

Ici, nous avons de nombreuses options comme le mot de passe, l'e-mail, l'authentification par lien e-mail, Google, Apple, Facebook, Twitter, GitHub, Microsoft, Yahoo, et tout le reste.

Laissez-moi vous montrer cela d'abord.

Maintenant, notre projet a été créé.

Créons maintenant une application.

Cliquez sur « Web app » ici.

Entrez le nom, disons « Firebase basics ».

Enregistrer l'application.

Oui, donc ici j'ai une entrée pour l'e-mail et une entrée pour le mot de passe (password).

Et un bouton « Submit ».

Si vous tapez quelque chose ici, cela sera transmis à cet e-mail de nom stocké dans l'entrée correspondante avec sa valeur.

Pour l'e-mail, ce sera l'état des données d'e-mail.

Pour le mot de passe, ce sera le mot de passe.

Nous devons d'abord installer Firebase.

Pour installer Firebase, venez ici et allez dans ce fichier, ajoutez simplement Firebase comme dépendance comme ceci, il sera ajouté.

Et pour une application React.

Pour VS Code, vous devez l'installer en utilisant cette commande : `npm install firebase`.

Maintenant, vous voyez que nous obtenons toutes ces données ici que nous devons importer dans `app.js`.

Créez un fichier ici, `firebaseConfig.js`.

Mettez tout ici, copiez ces éléments et collez-les simplement ici.

Laissez-moi enlever les commentaires.

Pour que ce soit plus clair.

Nous devons exporter cette constante `app`.

Voici les données de configuration. Nous avons la clé API (API key), le domaine d'authentification (auth domain), l'ID, etc.

Nous devons donc l'importer ici.

`import app from './firebaseConfig';`

Maintenant, nous pouvons utiliser Firebase pour cette application ici.

Continuer vers la console.

D'accord, nous ciblons d'abord l'authentification.

Nous devons aller dans l'onglet Authentification, cliquer sur « Get started » ici.

Cela vient avec de nombreux types d'authentification que je vous ai montrés ici : mot de passe, lien e-mail, Google, Facebook et autres.

Nous devons d'abord les activer.

Activons d'abord l'inscription et la connexion par e-mail/mot de passe.

Ajoutez également votre domaine ici.

Laissez-moi ajouter le domaine, le domaine est celui-ci.

Copiez ceci et ajoutez-le ici.

C'est ajouté.

Donc ça va marcher, je suppose.

Maintenant, ce que nous devons faire, c'est importer quelques éléments de l'authentification Firebase.

Comme il est dit ici, importez `getAuth` et `createUserWithEmailAndPassword`.

`getAuth` est une fonction pour vérifier si nous sommes authentifiés ou non.

Et cette fonction `createUserWithEmailAndPassword` est utilisée pour créer un utilisateur.

Laissez-moi le faire.

D'abord, laissez-moi définir l'instance d'authentification.

`const auth = getAuth();` comme ceci.

Dans cette fonction `handleSubmit`, si nous cliquons sur le bouton de soumission, cela sera envoyé à l'intérieur.

Si nous cliquons sur le bouton de soumission, cette fonction s'exécutera : `handleSubmit`.

Dans cette fonction `createUserWithEmailAndPassword`, nous devons passer trois choses.

D'abord, le `auth`.

Voyez, il est passé ici, puis l'e-mail et le mot de passe.

Laissez-moi récupérer l'e-mail depuis notre état de données : `data.email`.

Et `data.password`.

Nous devons enregistrer la réponse dans la console.

Nous utiliserons `then` pour qu'il nous envoie notre réponse.

Pour ajouter la réponse dans les paramètres.

Dans la fonction de rappel (callback), nous pouvons juste dire `console.log(response.user)`.

Mais si cela échoue, si notre connexion échoue, nous pouvons simplement l'attraper en utilisant `catch error`, nous afficherons juste une alerte qui est `error.message`.

Sauvegardez-le.

Maintenant, essayons de nous connecter.

Nous n'avons pas d'e-mail ici.

Alors essayons maintenant.

Entrez l'e-mail, ouvrez d'abord la console et effacez tout cela.

Depuis la console, ajoutez l'e-mail et un mot de passe.

Soumettre.

Voyez, nous lisons toutes ces données ici.

Provider, payload.

D'accord, nous n'avons pas besoin de tout ça, nous avons seulement besoin du jeton d'accès (access token), nous avons besoin du nom d'affichage, de l'e-mail original utilisé pour l'inscription, s'il est vérifié, du numéro de téléphone et tout le reste.

Ici, ce n'est pas vérifié.

Donc si nous rafraîchissons ceci, nous devrions voir cet e-mail ici.

Voyez, il apparaît ici.

Et une chose géniale à propos de ceci est — laissez-moi me connecter ou m'inscrire, je veux dire, avec le même e-mail deux fois.

S'il est présent ici.

Si nous nous inscrivons à nouveau, ou créons à nouveau l'utilisateur, nous verrons une erreur dans l'alerte.

Soumettre.

Voyez, nous lisons que l'e-mail est déjà utilisé.

C'est ainsi que nous créons un utilisateur dans Firebase.

D'accord, la création est faite.

Maintenant, voyons comment se connecter. Nous avons cette méthode, `signInWithEmailAndPassword`.

Alors ajoutez-la simplement ici, remplacez `createUser`.

Et ici aussi, et toutes les autres choses seront les mêmes.

Sauvegarder.

Et maintenant, essayons de nous connecter avec cet e-mail, effacez la console.

Soumettre, vous avez toutes les données ici, qui sont renvoyées par cette réponse.

Mais si nous entrons le mauvais e-mail qui n'est pas présent ici, nous devrions voir une erreur.

Laissez-moi utiliser un mauvais e-mail, `john440@gmail.com`.

Et cliquez sur « Submit ».

Voyez, utilisateur non trouvé car cet utilisateur n'est pas présent dans l'authentification.

Et si nous entrions le mauvais mot de passe ?

Entrons le mauvais mot de passe.

Soumettre.

Voyez, nous recevons toujours une erreur d'identifiant ou de mot de passe.

L'inscription (sign up) et la connexion (sign in) sont faites.

Maintenant, laissez-moi me concentrer sur l'authentification par e-mail ou Google.

Vous pouvez lire la documentation et le faire tout comme je le fais pour toutes les autres méthodes de connexion, car je ne pourrai pas tout vous montrer.

Le dernier ici, laissez-moi juste vous montrer `GoogleAuthProvider` d'abord.

Nous avons donc besoin de `getAuth` et de `GoogleAuthProvider`.

Ensuite, nous devons créer l'instance d'authentification pour le fournisseur Google.

`const googleProvider = new GoogleAuthProvider();`.

Ensuite, nous devons importer une chose de plus, qui s'appelle `signInWithPopup`.

C'est ici.

Nous avons donc trois choses : `getAuth`, `GoogleAuthProvider` et `signInWithPopup`.

Nous avons conçu une fonction ici.

Et nous passerons le `auth` et le nom du fournisseur qui est Google.

Et c'est tout, mais ici aussi nous devons activer le fournisseur Google pour cela et ensuite sauvegarder en utilisant votre e-mail de support projet, sauvegarder.

Il a été créé, donc sauvegardez et cliquez sur le bouton de soumission ici.

Cela devrait ouvrir une fenêtre contextuelle (pop-up) ici.

Si nous essayons, d'accord, ça va marcher.

Voyez le nom.

Et pour le compte e-mail, le fournisseur ici est e-mail.

Si on réessaye, cliquez sur soumettre.

D'accord.

D'accord.

Nous obtenons une erreur parce que nous devons ajouter la méthode ici.

Mais ce domaine personnalisé ne fonctionne pas.

Laissez-moi corriger cela.

Si je copie ceci et que je l'ajoute ici ou que je clique simplement sur le bouton « Share ».

D'accord, copiez simplement le lien web ici.

À partir de là et postez-le simplement ici dans le domaine.

Cliquez sur « Add ».

Et ça devrait marcher maintenant.

Si nous cliquons sur le bouton « Submit », d'accord, domaine non autorisé.

Attendez une seconde, soumettez encore une fois.

D'accord, quel est le problème ici ? Nous n'arrivons pas à déclencher cette erreur.

Soumettez ou rafraîchissez ceci, puis cliquez sur soumettre.

D'accord, maintenant nous l'avons ici.

Laissez-moi vous montrer le pop-up.

Et je pense que vous pouvez le voir aussi.

Cliquez sur OK.

Où est-ce ? Cliquez sur l'e-mail.

Voyez, nous recevons toutes les données ici que nous avions précédemment pour l'inscription par mot de passe, l'e-mail.

Cet e-mail est vérifié, car nous avons utilisé l'inscription Google, et le fournisseur a été changé pour Google.

De même, nous avons GitHub.

Nous avons Facebook, Apple, Twitter, etc. Pour GitHub, nous devons importer le fournisseur `GithubAuthProvider`.

Ensuite, nous devons ajouter... quoi déjà ? Laissez-moi juste ouvrir la méthode de connexion de GitHub.

GitHub, nous devons ajouter l'ID client et le secret, et cela nous renverra le gestionnaire d'authentification (auth handler) que nous devrons coller dans le site GitHub, l'application GitHub.

Si nous allons sur github.com, nous devrions voir les paramètres (settings) ici.

Allez dans les paramètres.

Et allez dans les paramètres de développeur (developer settings) ici.

Applications OAuth pour créer une nouvelle application ici.

Laissez-moi juste ouvrir ce fichier.

Je dois utiliser l'URL d'authentification que vous obtenez d'ici.

Attendez une seconde.

Si nous ajoutons GitHub, celui-ci, nous devons ajouter ceci ici dans l'URL de rappel d'autorisation (authorization callback URL), puis nous devons obtenir l'ID client et le secret.

Vous devrez trouver comment faire.

Sinon, vous pouvez consulter ma vidéo sur l'authentification des données dans la même liste de lecture.

C'est fait.

Nous avons fait l'authentification Google et le mot de passe, la création d'utilisateur et la connexion.

Maintenant, passons aux bases de données.

Pour Firestore, laissez-moi juste aller dans ce Cloud Firestore, puis, d'accord, nous n'avons pas besoin de cela.

Vous pouvez lire la documentation si vous voulez.

Mais je vais vous montrer comment effectuer les quatre opérations pour Firebase Firestore.

Ouvrez Firestore ici dans l'onglet de gauche, puis créez simplement la base de données, démarrez en mode test, puis activez-la.

Maintenant, nous pouvons utiliser Cloud Firestore.

Et ici dans la configuration Firebase, nous devons importer une chose appelée `getFirestore`.

Attendez, laissez-moi d'abord ajouter le dossier `firebase/firestore`.

Nous devons importer `getFirestore` de `firebase/firestore`, puis nous devons créer `const db = getFirestore(app);`.

C'est fait.

De plus, nous devons importer la base de données dans notre `app.js`, car nous devons l'utiliser pour créer la référence à une collection.

Voyez, nous devons créer une collection ici.

Nous pouvons le faire manuellement ici ou depuis l'application React.

Laissez-moi le faire depuis l'application React.

Nous devons supprimer toutes ces choses dont nous n'avons pas besoin pour le moment.

Laissez-moi supprimer cela aussi.

Nous importons deux choses : d'abord le mot-clé `collection`, la fonction pour ajouter une collection à Firebase, puis `addDoc` pour ajouter un document au Firestore de Firebase.

Depuis `firebase/firestore`.

Créons une collection ici.

`const collectionRef = collection(db, 'users');`.

Le nom « users » sera ici dans la collection, il sera affiché plus tard.

Maintenant, nous devons envoyer des données en utilisant la fonction `addDoc`, et elle accepte deux paramètres.

D'abord la référence de la collection.

Et deuxièmement les données.

Laissez-moi en ajouter une de plus.

Ajoutez simplement l'e-mail, ce sera `data.email`, puis ajoutons le mot de passe `data.password`.

Ensuite, nous devons enregistrer notre réponse.

Ou nous pouvons juste dire `.then` pour le succès, alerte.

Et nous pouvons dire « Données ajoutées ».

Mais s'il y a une erreur, nous pouvons juste l'attraper.

Sauvegardez-le.

Maintenant, essayons d'ajouter des données.

Laissez-moi mettre l'e-mail et un mot de passe.

Soumettre cette fonction comme `addDoc` collection.

Ce sera commun dans tous les frameworks comme React ou Angular.

Si nous devons ajouter des données depuis Angular, nous utilisons `addDoc`, si nous devons ajouter des données depuis Svelte ou JavaScript ou React ou Vue.js ou Next.js, nous devons utiliser `addDoc`.

C'est commun à tous les autres frameworks.

Voyez, ces nouvelles données sont maintenant ici, ce nouveau nom de collection Nishan et l'e-mail, le mot de passe.

Laissez-moi en ajouter une de plus.

Ajouté.

Et c'est ici.

Si nous rafraîchissons cette page, je pense que cela devrait y être.

Voyez, nous avons deux collections ici maintenant.

Voyons maintenant comment lire les données.

Nous pouvons créer une fonction pour cela.

`const getData = () => { ... }`.

Pour obtenir des données, nous devons utiliser une fonction appelée `getDocs`.

Cette fonction récupère les données de Firebase.

Pour obtenir des données, nous devons juste passer la référence de la collection ici.

Elle renvoie des données sous forme de réponse, comme tout appel API.

Et ici, nous pouvons juste faire `console.log(response.docs)`.

Nous devons traiter les données car c'est un peu complexe.

Cela prend un paramètre, disons `item`, puis nous devons retourner `item.data()`.

Nous devons appeler la fonction parce que nous ne l'appelons pas si nous la collons ici dans le bouton de soumission.

Nous devrions voir les données ici si nous cliquons sur soumettre.

Impossible de lire la propriété de `map`.

D'accord, je suppose que ce n'est pas `data`, c'est `doc`.

Nous pouvons vérifier ici.

Si nous allons à « Read data ».

D'accord, `getDoc`.

Laissez tomber. Essayons ceci, soumettre.

Je pense que c'est `doc.data()`.

Sauvegardez, soumettez, puis impossible de lire les propriétés de `map`.

Nous passons la référence de la collection et `getDocs`.

Et ensuite nous contrôlons la réponse.

Nous ajoutons deux objets ici, qui sont ces objets, ces deux IDs.

Ajoutons également l'ID.

Enveloppez-le dans des accolades et utilisez l'opérateur de décomposition (spread operator).

Ainsi, il stocke les données et aussi l'ID.

L'ID sera `item.id`.

Sauvegardez.

Essayez maintenant.

Soumettre, voyez, il y a les deux objets avec leurs IDs.

Essayons maintenant de mettre à jour les données.

Nous avons besoin d'une fonction `updateData`.

Celles-ci sont communes, je vous le dis encore une fois.

Ajoutez la fonction au bouton de soumission.

Ici, nous devons importer deux choses.

Nous devons faire `doc` et `updateDoc`.

Nous ne pouvons mettre à jour qu'une seule donnée à la fois.

Dans `updateDoc`, nous devons envoyer l'ID.

Laissez-moi choisir n'importe quel ID ici parmi ces deux.

Et pour aller plus loin, vous pouvez voir mon autre vidéo où j'ai montré comment mettre à jour les données en utilisant le paramètre ID.

C'est juste un truc React classique, pas spécifique à Firebase.

Ce que nous pouvons faire, c'est utiliser la fonction `doc`.

D'abord, nous devons spécifier quel document mettre à jour.

Utilisons cette fonction `doc` que nous venons d'importer, elle prend trois paramètres.

La base de données, le nom de la collection et l'ID.

Laissez-moi choisir l'ID de celui-ci.

Copiez cet ID, nous mettrons à jour ce champ statiquement.

Ajoutez l'ID ici.

Maintenant, le document est sélectionné pour la mise à jour.

Si nous cliquons sur le bouton de soumission, l'e-mail et le mot de passe seront mis à jour.

Ensuite, nous devons appeler `updateDoc` pour le mettre à jour, nous passerons le document à mettre à jour et les nouvelles données.

Ajoutons l'e-mail, disons « ABC » et ajoutons un mot de passe n'importe quoi.

Si c'est réussi, nous pouvons les appeler, ce qui affichera une alerte et dira « Données mises à jour ».

Mais si cela échoue, nous pouvons l'attraper.

Sauvegardez.

Appelons aussi cette fonction `getData`.

Cliquez sur soumettre.

Laissez-moi vérifier d'abord, l'e-mail est celui-ci, d'accord.

Il sera changé en ABC.

Soumettre, mis à jour et si nous vérifions ici, l'e-mail est ABC.

Nous pouvons aussi mettre à jour un seul champ à la fois.

Si nous ne voulons pas de mot de passe, nous pouvons simplement le supprimer ou mettre ce que vous voulez.

Sauvegarder, soumettre.

Ici, ça devrait être ABCD.

Soumettre, mis à jour, l'e-mail est maintenant ABCD.

Et le mot de passe est le même.

C'est ainsi que nous mettons à jour un document.

La quatrième opération est la suppression de document.

Laissez-moi vous montrer ici.

Nous pouvons créer `deleteData` et passer la fonction au bouton.

Nous n'avons pas besoin de passer de données ici, nous avons seulement besoin de passer le document à supprimer.

Laissez-moi obtenir une fonction de plus, connue sous le nom de `deleteDoc`.

Ajoutez simplement la fonction ici.

Nous devons utiliser l'alerte « Données supprimées ».

Sauvegarder.

Et maintenant, vérifions.

Si nous cliquons sur Soumettre.

Celui avec l'e-mail ABCD sera supprimé.

Soumettre.

D'accord, supprimé.

Et voyez, il n'est plus là.

C'est ainsi que fonctionne la fonction de suppression.

Si je veux supprimer cet ID, nous devons copier l'ID et le coller ici.

Soumettre, supprimé.

Et voyez, nous n'avons plus de champs ici, nous avons des données vides dans Firestore.

C'est ainsi que l'ajout, la récupération, la mise à jour et la suppression de documents fonctionnent dans Firebase Firestore.

Toutes les opérations CRUD.

Voyons maintenant le stockage de fichiers (File Storage) pour Firebase Storage.

Nous devons importer ici `getStorage` de `firebase/storage`.

`export const storage = getStorage(app);`.

Et de même, importez le stockage ici.

Nous n'avons pas besoin de la base de données.

Supprimez `handleSubmit`, non pas la fonction mais le contenu de `getData`, `deleteData` et tout le reste.

Laissez-moi créer un champ d'entrée (input).

Sur `onChange`, cela prend un événement et nous appellerons la fonction `handleInput` pour cela.

L'e-mail sera stocké ici dans le `handleInput` et ensuite dans le stockage.

Laissez-moi vous montrer avec le `console.log`.

Le fichier sera ici.

Nous devons utiliser les données (data).

`handleInput`.

D'accord, nous n'avons pas besoin de cela non plus, alors collez-le ici.

Si nous choisissons un fichier, sauvegardez-le, mais nous devons ajouter le type.

Le type sera `file`.

Nous n'avons pas besoin d'espace réservé (placeholder).

Si nous choisissons un fichier, il apparaîtra ici si nous appuyons sur le bouton de soumission.

Laissez-moi choisir un fichier ici, comme « REST API », cliquez sur « Submit ».

Voyez, le fichier est maintenant ici.

Et maintenant, nous devons envoyer le fichier à ce stockage Firebase (Firebase Storage).

Allez dans le stockage ici.

Et activons le stockage.

Il est déjà activé, très bien.

Nous devons importer ce `getStorage` et `ref` ici en haut.

Nous n'avons pas besoin de `getStorage`, car nous l'avons déjà ici.

Nous devons utiliser `ref`.

C'est ce qu'il fait ici, mais nous l'avons fait ici dans le fichier de config Firebase, ensuite nous devons spécifier quelle donnée sauvegarder en utilisant une référence.

Ce devrait être le nom de l'image.

Le nom de l'image devrait être appelé `data.name`, car voyez, le nom de l'image est ici.

C'est fait.

Maintenant, nous devons passer la référence à une fonction.

La fonction est `uploadBytes`.

Mais si nous descendons ici, nous devrions voir une vue claire de toutes les fonctions.

Nous devons utiliser `uploadBytesResumable` à importer de `firebase/storage`.

Ensuite, une autre chose dont nous avons besoin est le `getDownloadURL`. Si notre téléchargement de fichier est réussi, nous obtiendrons une URL dans notre console que nous pourrons simplement envoyer à la base de données.

Comme, disons, si nous avons soumis une photo de profil, alors nous pouvons envoyer le lien à la base de données pour l'avatar.

Nous devons utiliser cette fonction `uploadBytesResumable`.

Créez une instance de cela, elle prend la référence de stockage, le type du fichier.

Ensuite, nous devons juste appeler `uploadTask.on`.

Faisons-le.

Sur le changement d'état (`state_changed`).

Cela prend un URL de rappel.

Et si vous voyez ici, cela prend un paramètre appelé `snapshot`.

Dans le premier callback, nous pouvons calculer la progression du pourcentage de la photo téléchargée, puis en utilisant ces données, nous pouvons créer une barre de progression.

S'il y a une erreur, nous pouvons la gérer.

Laissez-moi juste ajouter ceci ici.

Laissez-moi afficher l'erreur dans la console.

Ensuite, si c'est réussi, si le téléchargement du fichier est terminé, nous pouvons juste appeler la fonction suivante ici qui s'appelle `getDownloadURL`.

Voyez, elle nous renvoie une URL.

Maintenant, si nous rafraîchissons ceci, d'accord, laissez-moi juste essayer.

Nous n'avons aucun fichier dans le stockage alors laissez-moi juste en choisir un.

Si nous soumettons ici, voyez « upload is 0% Done ».

D'accord, une erreur inconnue s'est produite.

Laissez-moi rafraîchissez la page et essayer encore une fois.

Nous passons le stockage ici, très bien.

Toutes les choses sont correctes.

Essayons ceci en utilisant `ref` pour spécifier la référence `data.name`.

Sauvegardez.

Maintenant, essayons de télécharger un fichier.

Cliquez sur soumettre.

Quel est le problème ici ?

Erreur de stockage Firebase.

Pourquoi passons-nous cela, nous le passons ici au stockage.

La référence est correcte, les données et `uploadBytesResumable`, nous utilisons ce fichier.

Quel est le problème ici ?

C'est parce que les règles ne sont pas configurées ici, je pense.

Nous devons aussi vérifier les règles.

Ouvrez les règles.

Et voyez, la règle ici est que nous ne pouvons télécharger un fichier que lorsque nous sommes authentifiés.

Comme nous le sommes, mais nous ne sommes pas authentifiés ici.

Laissez-moi essayer encore une fois, ça va marcher.

Le téléchargement est fait à 100 %.

Et voyez, nous pouvons voir l'URL du fichier dans la console.

Si nous allons sur ce lien ici, c'est l'image que nous avons téléchargée.

Maintenant, vous pouvez utiliser ce lien pour envoyer des données aux bases de données Firebase.

Si nous vérifions ici aussi, rafraîchissez la page.

Voyez, l'image est ici avec le nom, tout ce que vous pouvez utiliser, ainsi que l'emplacement.

Et si nous voulons télécharger le fichier dans un dossier ?

Ici, dans `data.name`, nous pouvons spécifier le dossier dans une variable de type chaîne.

Utilisez d'abord un littéral de gabarit (template literal), puis ajoutez simplement le dossier, disons « images/ », puis le nom de l'image.

Nous enverrons les images dans le dossier « images ».

Si nous essayons encore une fois, choisissez un autre fichier, n'importe lequel, puis soumettez.

Il devrait être téléchargé dans le dossier « images ».

Laissez-moi vérifier ici, rafraîchissez le stockage.

Voyez, c'est dans « images ».

C'est ainsi que Firebase Storage fonctionne dans tous les frameworks : React, Angular, Vue, Svelte, JavaScript, Next, et tout le reste.

Très bien.

Voyons maintenant comment utiliser les mises à jour en temps réel dans Firebase Firestore.

Laissez-moi vous montrer ce que je veux dire.

Nous obtenons les données ici de la fonction `getDocs`.

Si nous ajoutons un nom et un e-mail, soumettez, c'est ajouté, mais ce n'est pas rafraîchi ici.

Pour rafraîchir la page, nous devons le faire manuellement, cliquer sur ceci, et seulement alors nous obtiendrons ce tableau d'objets ici.

À partir de Firebase Firestore, nous devons créer une chose de plus appelée `onSnapshot`.

Importez cette fonction.

Et laissez-moi mettre en commentaire ce `getDocs` pour le moment.

Ce `onSnapshot` écoute les mises à jour en temps réel dans Firebase Firestore.

Ici, nous devons passer la référence de la collection et une fonction de rappel (callback).

Cette fonction de rappel s'exécutera chaque fois qu'il y aura un changement à l'intérieur de Firebase Firestore.

N'importe quel changement, si nous supprimons, si nous mettons à jour ou si nous ajoutons des données.

Elle prend un paramètre appelé, disons, `data`.

Laissez-moi rafraîchir ou formater le code ici.

Réessayons depuis le début.

Rafraîchissez la page.

Nous avons un objet ici.

Si nous ajoutons un autre objet, ces nouvelles données seront ici, ce qui n'était pas le cas auparavant avec la fonction `getDocs`.

Soumettre, voyez, ajouté, et nous écoutons en temps réel.

Si nous en ajoutons un autre, nous avons trois objets ici.

Donc, quand ces données changent ici, cela changera aussi dans l'application front-end.

Si nous supprimons cette collection ou n'importe quel champ, voyons ce qui se passe pour supprimer le document.

Supprimer.

Voyez, ici nous avons aussi rafraîchi la page.

Et nous n'avons plus que deux objets venant de Firestore.

Si on supprimait toute la collection, nous aurions l'objet vide ou le tableau vide là-bas maintenant.

Supprimez ceci.

Voyez, le tableau est maintenant vide, car il est écouté en temps réel.

C'est ainsi que `onSnapshot` fonctionne pour obtenir des données en temps réel de Firebase Firestore.

Voyons maintenant les requêtes Firebase Firestore.

Les requêtes sont utilisées pour filtrer les données en fonction de certains champs comme le nom ou l'âge.

Ici, j'ai ajouté quatre champs qui contiennent le nom, l'âge et l'e-mail.

Filtrons les données en fonction d'eux.

Nous avons besoin du mot-clé `query` de Firebase Firestore.

Et une chose de plus appelée le mot-clé `where`.

Laissez-moi créer une requête.

Ajoutons d'abord la requête d'âge.

Elle prend le paramètre `query`.

Nous allons filtrer les âges inférieurs à 28.

Je pense que nous devrions obtenir les âges 25, 21 et 20.

Le filtre prend la référence de la collection ici comme premier paramètre, puis dans le second paramètre, il prend un `where`, et ici nous définissons la condition.

Nous devons filtrer en fonction de l'âge (`age`), puis nous devons ajouter la condition, si nous voulons qu'il soit égal à, inférieur à ou supérieur à, puis la valeur.

Nous voulons que l'âge soit inférieur à 28.

Ici, mettez « inférieur à » (<), donc si les âges sont inférieurs à 28, ils seront affichés, ensuite nous devons passer cette requête d'âge à la fonction `getDocs`.

Dans notre cas, c'est `onSnapshot`.

À la place de la collection, passez la requête d'âge ici et vous verrez, nous obtiendrons les trois données ici, où les âges sont inférieurs à 28.

Si nous le faisons supérieur à 28 ou égal à, nous ne verrons qu'un seul âge qui est 28 ici, alors laissez-moi vous montrer, rafraîchissez.

S'il est égal à 28, nous ne verrons que cette donnée.

Voyez, nous n'obtenons qu'un seul âge ici.

C'est ainsi que fonctionne le filtre d'âge ou non numérique.

Essayons maintenant de filtrer par requête de nom.

Pour la requête de nom, nous utiliserons « si le nom est égal à Nishant Kumar 4 », alors cela affichera ses données.

Si nous rafraîchissons la page, voyons ce que nous avons ici.

Quelque chose ne va pas.

Si `name == 'Nishant Kumar 4'`, d'accord, nous devons aussi passer la requête ici.

Voyez, nous n'obtenons que le nom parce qu'un seul nom correspond et nous filtrons sur cette base.

Nous pouvons aussi ajouter l'e-mail ou n'importe quel autre champ que nous voulons.

Très bien.

Mettez ceci comme e-mail.

Ensuite, nous pouvons voir cette requête ici.

C'est ainsi que fonctionne une requête dans Firebase Firestore.

Apprenons maintenant à héberger une application web ou un site web sur Firebase Hosting.

J'ai une application React ici, un site web de blog que nous allons héberger.

Première chose à faire : nous devons installer la CLI Firebase (Firebase CLI).

Nous allons juste faire ceci : installer `firebase-tools` ici.

Laissez-moi installer ceci.

Et une chose de plus que je dois faire est de créer un « build » ici.

`npm run build`.

Après ces deux étapes, nous irons de l'avant.

Nous devons attendre que le build soit généré et que les outils Firebase soient installés.

Maintenant que nous avons le build.

Déployons-le.

D'abord, connectons-nous à Firebase en utilisant `firebase login`.

Cela ouvrira une fenêtre dans Chrome, connectez-vous, autorisez ceci et nous sommes connectés à Firebase.

Ensuite, ce que nous devons faire, c'est initialiser le projet.

`firebase init`.

Voulez-vous continuer ? Oui.

Nous voulons l'hébergement (Hosting), appuyez sur espace pour sélectionner l'option et entrez.

Étape suivante : nous voulons que le répertoire public soit « build » car c'est là que se trouve le build.

D'accord, nous n'avons pas besoin de ce build automatique.

Si quelque chose ne va pas, laissez-moi le refaire une fois de plus.

Initialisons-le en utilisant ceci.

Oui, nous voulons le Hosting.

« build » est le dossier public.

Nous voulons une application à page unique (Single Page App). Oui.

Non pour les builds automatiques.

C'est tout, utilisons simplement la commande appelée `firebase deploy` pour déployer ceci.

L'étape est de générer un build d'abord, puis de se connecter, puis d'initialiser, puis de déployer.

Nous avons différentes commandes pour générer le build pour Angular, pour React et pour tout autre framework comme Next.

C'est ainsi que nous procédons ici.

Voyez, il nous donne un lien vers le site web ici.

Ouvrons-le et voyons si nous voyons notre site web ici.

C'est le site web que nous venons d'héberger sur ce lien.

Et c'est ainsi que fonctionne Firebase Hosting.

Maintenant, penchons-nous sur les règles de sécurité Firebase (Firebase security rules).

Si vos règles Firebase ne sont pas définies sur public, cela signifie que n'importe qui peut écrire des données ou les lire.

Donc, même si nous ne sommes pas authentifiés dans Firebase avec un identifiant et un mot de passe, nous pouvons écrire des données ou les lire.

Essayons cela.

Actuellement, nous ne sommes pas connectés.

Nous pouvons aussi supprimer des données de la console.

Voyez, c'est vide pour le moment car les données sont vides ici.

Laissez-moi maintenant ajouter une donnée sans me connecter.

Ajoutez l'e-mail, ajoutez le nom, l'e-mail et un âge, cliquez sur « Add » ici.

Voyez, nous voyons que les données ont été ajoutées.

Et si nous vérifions ici, elles seront ajoutées ici.

Et nous pouvons aussi les lire, ouvrez la console.

Voyez, cela apparaît ici dans la console.

Maintenant, changeons les règles pour qu'elles soient authentifiées, ce qui signifie que nous n'écrirons des données que si nous sommes authentifiés.

Laissez-moi le faire ici.

`allow write: if request.auth != null;`.

Cela signifie qu'il nous permettra de lire ou d'écrire des données quand nous sommes connectés, quand l'auteur de la requête n'est pas nul.

Il devrait y avoir des données à l'intérieur de la requête ou les données que nous obtenons de l'authentification quand nous nous inscrivons ou nous nous connectons.

La deuxième chose à écrire ici est `allow read` dans tous les cas.

Publiez cette règle.

Maintenant, disons, des données sans se connecter, le nom, l'e-mail et l'âge, cliquez sur « Add ».

Voyez, nous recevons ce message indiquant des permissions manquantes ou insuffisantes.

Mais nous pouvons lire les données.

Ouvrez la console, nous obtenons les données ici.

Maintenant, faisons en sorte que la règle de lecture soit également authentifiée.

Faites-le ici comme ceci.

Et vous verrez, nous aurons toujours cette erreur que nous avons eue pour l'opération d'écriture.

Publiez ceci.

Ouvrez la console, nous verrons le message de permission insuffisante.

Rafraîchissez la page, pas connecté.

Voyez, erreur Firebase : permissions manquantes ou insuffisantes.

Cela signifie que nous n'avons pas les permissions pour lire les données car nous ne sommes pas connectés.

Maintenant, essayons de nous connecter, l'e-mail et le mot de passe.

Connectez-vous ici.

Et si nous rafraîchissons la page.

Voyez, nous devrions voir les données ici car cela nous permet de lire après l'authentification.

Maintenant, ajoutons des données après l'authentification, l'e-mail et l'âge.

Cliquez sur « Add ».

Voyez, les données sont ajoutées ici.

C'est ainsi que fonctionne l'authentification.

Une chose de plus ici est de permettre à l'utilisateur de lire ou d'écrire dans aucun cas.

Cela signifie que même si nous sommes connectés, il ne devrait pas nous permettre d'écrire des données.

Nous ajouterons simplement `if false` ici.

Faites-le seulement dans la permission d'écriture.

Cela nous permettra d'écrire des données dans aucun cas, même si nous sommes authentifiés.

Rafraîchissez la page.

Connecté, ajoutons des données.

Voyez, nous n'avons pas la permission d'écrire des données.

C'est ainsi que fonctionnent les règles Firebase Firestore.

Maintenant, gérons les mises à jour de l'état d'authentification en temps réel de Firebase.

Quand nous nous connectons, notre application doit envoyer des données à Firebase indiquant que nous sommes connectés.

Si nous nous déconnectons, notre application doit envoyer des données à Firebase indiquant que nous sommes déconnectés.

Ici, j'ai un champ e-mail et un champ mot de passe, un bouton de connexion et un bouton de déconnexion.

Créons ce `onAuthStateChanged` qui nous écoutera en temps réel.

Utilisez un hook `useEffect`.

Appelez une fonction ici.

Elle prend un paramètre `auth` et une fonction de rappel.

La fonction de rappel nous renvoie des données.

Si je vérifie cette console ici, voyons ce que nous avons au début.

Nous lisons les données ici, car nous sommes maintenant connectés.

Commençons par le début, déconnexion.

Maintenant nous sommes déconnectés ici.

Entrons l'e-mail et le mot de passe.

Si je clique sur « Login », cette fonction `onAuthStateChanged` envoie des données à Firebase indiquant que nous sommes connectés.

Si nous cliquons sur déconnexion, cela enverra des données à Firebase indiquant que nous sommes déconnectés et cela persiste.

Même si nous rafraîchissons la page, cela existera toujours.

À moins que nous ne nous déconnections ou nous nous connections, l'état ne changera pas.

Si je me connecte, nous obtiendrons toutes les données ici.

Mais si nous cliquons sur déconnexion, cela devrait être nul.

Cela signifie que nous sommes maintenant déconnectés.

Laissez-moi vous donner une chose de plus ici.

Vérifiez si les données existent, ou si ce n'est pas nul.

Si nous sommes connectés, nous verrons une alerte indiquant que nous sommes connectés.

Sinon, nous verrons une alerte indiquant que nous sommes déconnectés.

Rafraîchissons la page.

Toujours pareil parce que nous ne sommes pas connectés.

Si nous entrons l'e-mail et le mot de passe, nous verrons que nous sommes connectés maintenant.

C'était tout sur `onAuthStateChanged` dans Firebase, ce qui nous amène à nos mises à jour en temps réel pour créer un fichier appelé `index.js`.

Dans cette première partie, nous apprendrons simplement comment authentifier et utiliser les opérations CRUD pour JavaScript vanille (vanilla JS).

Lions la balise script ici.

Tout d'abord, nous allons apprendre à authentifier et utiliser les opérations CRUD pour JavaScript.

Ajoutons le code intégré ici.

Nous écrirons tout à l'intérieur du corps (body) et mettrons la balise script après le corps car elle doit se charger après.

Commençons par créer une application Firebase ici.

Allez dans la console.

Ajoutez un projet.

Firebase front end.

Créer le projet.

Lançons le fichier ici avec Live Server.

Il tourne ici, mais on ne voit rien parce qu'on n'a rien mis.

Créons deux entrées pour l'authentification.

E-mail et mot de passe.

Donnons-leur un style.

Créez un fichier CSS également.

`index.css`.

Liez le CSS ici.

Donnez à ce div une classe `main`.

Et ici dans le CSS, nous dirons simplement `display: flex`, hauteur `100vh`, etc.

Nous avons maintenant deux champs d'entrée, e-mail et mot de passe.

Ajoutons un bouton.

Soumettre.

Maintenant, récupérons les données de ces entrées.

Récupérons sa valeur.

Lions cette fonction à ce bouton ici.

Sur l'événement `onclick`.

Maintenant, si nous essayons de les afficher dans la console.

Voyons ce que nous obtenons.

Entrez l'e-mail et un mot de passe.

Soumettre.

Voyez, nous obtenons maintenant l'e-mail et le mot de passe dans la console.

Supprimons ce `console.log`.

Créons l'application Firebase.

J'ai ici un guide sur la façon d'ajouter Firebase à la bibliothèque JavaScript.

Utilisez une balise script ici.

Ouvrez cette documentation, je laisserai un lien, copiez ces trois liens CDN et collez-les.

Nous avons ces trois liens.

Le premier est pour l'authentification, le second pour Firestore et le troisième pour l'application (app).

Nous devons utiliser `firebase.initializeApp` dans notre `index.js`.

Initialisons-le en haut.

Ensuite, nous devons ajouter notre configuration ici.

Toutes ces données.

Ensuite, nous devons initialiser notre base de données Firestore et l'authentification.

Faisons-le.

Maintenant, nous pouvons utiliser `auth` pour l'inscription.

Nous devons utiliser `createUserWithEmailAndPassword`.

Attention à la casse (camelCase).

Nous devons passer cet e-mail et ce mot de passe à l'intérieur comme paramètres.

Ensuite, c'est une promesse (promise), donc nous pouvons avoir un bloc `then`.

Ajoutons également un bloc `catch` si cela échoue.

Affichons le code d'erreur.

Essayons cela maintenant.

Mais d'abord, allez dans la console, ouvrez l'onglet Authentification et activez la méthode de connexion par e-mail et mot de passe.

Sauvegardez et c'est fait.

Cliquez sur « Users ».

Vous voyez que nous n'avons aucun utilisateur ici.

Ajoutons-en un.

Entrez l'e-mail et un mot de passe.

Cliquez sur « Submit ».

Voyez, nous obtenons toutes ces données ici.

Si nous rafraîchissons ces données dans la console Firebase, nous verrons notre e-mail ici.

Si nous essayons de créer un compte avec le même e-mail, nous échouerons.

Soumettez.

Voyez, nous recevons ce message indiquant que l'e-mail est déjà utilisé.

Nous pouvons ajouter une alerte ici.

C'est l'inscription. Créons une autre fonction pour la connexion (`login`).

Nous utiliserons les mêmes données et les mêmes champs d'entrée.

Dans la connexion, nous avons besoin d'un autre bouton.

Donnons-lui un style de bouton de connexion.

Ne faites pas attention au design, nous nous concentrons sur la fonctionnalité.

Nous utilisons cette fonction de connexion pour la méthode de connexion.

`auth.signInWithEmailAndPassword`.

Je pense que l'orthographe est correcte.

Cela prend également deux paramètres.

Toutes les choses sont les mêmes, alors copiez simplement ce bloc `then/catch`.

Essayons de nous connecter.

Entrez l'e-mail et le mot de passe et cliquez sur « Sign In », mais ouvrez d'abord la console.

Voyez, nous lisons toutes les données.

Et si nous entrions le mauvais e-mail ? Nous aurons une erreur dans l'alerte.

Voyez, il n'y a pas d'utilisateur correspondant à l'identifiant.

Et si nous mettons le bon e-mail, mais le mauvais mot de passe ?

Voyez, le mot de passe est invalide.

Ça marche bien.

Voyons maintenant comment utiliser les mêmes données vers Firebase Firestore.

Épinglez cette base de données Firestore ici.

Créez la base de données et démarrez en mode test car nous testons.

C'est en cours d'initialisation.

Pendant ce temps, nous pouvons créer une fonction ici.

`const saveData = () => { ... }`.

Nous utiliserons cette méthode pour sauvegarder les données.

Mettons tout ce code en commentaire car nous avons déjà vu comment cela fonctionne.

Ne le commentez pas, nous allons le réutiliser.

Créez un bouton de plus ici.

Nous allons simplement sauvegarder l'e-mail et le mot de passe dans la base de données Firestore.

Ajoutez cette fonction à ce bouton.

Sur `onclick`, appelez `saveData`.

Si nous cliquons sur un bouton ici, cela devrait récupérer l'e-mail et le mot de passe dans notre fonction.

Pour ajouter des données, nous pouvons faire cette chose simple.

Si nous vérifions la documentation ici.

Nous devons d'abord ajouter le nom de la collection.

`db.collection('users').add({ ... })`.

Ensuite, nous utiliserons un mot-clé `add` pour ajouter des données dans la collection.

D'abord l'e-mail, puis le mot de passe.

Si c'est réussi, nous pouvons utiliser notre bloc `then`.

Et si cela échoue, nous utiliserons le bloc `catch`.

D'accord, essayons cela, notre base de données est vide.

Ajoutons un e-mail et un mot de passe.

Si vous ouvrez la console et sauvegardez les données, nous aurons le message « document écrit avec ID ».

Si nous vérifions Firebase Firestore et rafraîchissons, nous devrions avoir les données ici avec ce même ID.

Ajoutons-en une autre.

Voyez, la suivante est ici.

Notre `addDoc` fonctionne correctement.

Voyons maintenant comment lire les données de Firestore.

Ajoutons une fonction ici aussi.

`const readData = () => { ... }`.

Ajoutez le bouton dans le HTML.

`readData`.

C'est très, très simple.

`db.collection('users').get()`.

Nous utilisons un mot-clé `get` ici pour obtenir les données.

Cela nous renverra des données.

Nous pouvons utiliser `.then` pour voir dans la console les données entrantes.

Appelons cela `data`, puis `console.log(data)`.

Si vous ouvrez la console maintenant et cliquez sur le bouton.

`get` n'est pas défini.

Attendez une seconde, quel est le problème ?

D'accord, nous devons utiliser un point ici.

Sauvegardez et vérifiez à nouveau.

Nous recevons ces données ici.

Mais ce n'est pas clair ce que c'est. Laissez-moi filtrer.

`data.docs`.

Nous devons récupérer les documents à l'intérieur.

Voyez, nous lisons ce tableau (array) ici.

Et à l'intérieur de ce tableau, nous devons trouver nos données.

Nous allons mapper ces tableaux.

Cela nous enverra un `item`, puis nous dirons simplement `return item.data()`.

Si nous sauvegardons et vérifions à nouveau, nous devrions obtenir ces objets de tableau pour les deux champs.

Mais le fait est que nous n'obtenons pas l'ID.

Nous devrions obtenir l'ID en ajoutant simplement `id: item.id`.

Voyez cet ID unique pour les deux documents.

C'est ainsi que nous lisons Firebase Firestore.

Maintenant, troisièmement, voyons comment mettre à jour les données.

`const updateData = () => { ... }`.

Nous ajouterons le nom de la collection.

Ensuite, nous devons spécifier l'ID de la collection.

Nous avons deux IDs ici.

Nous pouvons utiliser le mot-clé `doc` et nous devons passer l'ID.

Passez l'ID de celui-ci.

Et ensuite nous devons le mettre à jour.

`update({ ... })`.

Nous devons ajouter les données à mettre à jour.

Changeons d'abord l'e-mail pour qu'il soit autre chose.

Le mot de passe devrait être le même.

Nous mettrons à jour le premier champ.

Nous devons passer cette fonction à un bouton.

Créons un bouton ici.

C'est juste pour vous montrer.

Nous devons obtenir une réponse basée sur une promesse.

Sauvegardez et vérifions maintenant.

Si nous cliquons sur « update one field », cet e-mail devrait être celui que nous avons défini.

Cliquez, d'accord, ce n'est pas défini.

Je suppose que nous devons l'utiliser dans une chaîne de caractères comme ceci.

Essayons encore, « update one field », voyez, mis à jour ici.

Et si nous vérifions ici, cet e-mail est maintenant celui que nous avons changé.

Maintenant, supprimons ce champ.

`const deleteData = () => { ... }`.

Un bouton de plus pour supprimer ce champ.

Et ici aussi, mais supprimons ce champ.

Nous utiliserons `doc` ici.

Et nous utiliserons simplement `delete()`.

Sauvegardez et essayons cela maintenant.

Si nous cliquons sur ceci.

Supprimé.

Et voyez, il n'est plus là.

C'est ainsi que fonctionne la fonction de suppression.

Si je supprime cet ID, nous devons copier l'ID et le coller ici.

Vous devez obtenir l'ID à partir des paramètres.

Pour cette fonction de suppression, passez l'ID d'ici.

Supprimé.

Et voyez, nous n'avons plus de champs ici, nous avons des données vides dans Firestore.

Nos quatre opérations fonctionnent maintenant : créer, lire, mettre à jour et supprimer, ainsi que les méthodes d'inscription et de connexion.

Nous avons fait beaucoup.

Et nous avons fait la base de données Firestore.

La suite est pour Angular.

Tout d'abord, créons un projet Angular.

Assurez-vous d'avoir installé la CLI Angular.

Et pour créer une nouvelle application, nous utiliserons `ng new my-app`.

Changeons d'abord de répertoire vers Angular.

Cela va créer un projet dans ce dossier.

Cela prendra un certain temps.

L'application Angular a maintenant été créée.

Changeons de dossier.

Maintenant nous sommes dans ce dossier.

Il y a tellement de fichiers ici que je ne vais pas vous expliquer.

Mais nous devons installer un paquet ici appelé `@angular/fire`.

C'est le paquet officiel pour Angular.

Il nous demande quelques choses.

Vous pouvez dire oui ou non, peu importe.

Cela va faire des choses intéressantes.

Oui, nous voulons continuer.

C'est la bibliothèque officielle Angular pour Firebase.

Et ils sont là, je vais vous montrer comment utiliser tout cela.

Nous devons attendre qu'il s'installe.

Maintenant, il demande quelques choses ici.

Nous voulons l'authentification ici.

Nous n'avons pas besoin du déploiement.

Nous avons besoin de Firestore.

Entrez, il configurera automatiquement le projet pour l'authentification et Firestore.

Connectez votre compte e-mail.

Oui, c'est mon compte e-mail.

Tous les projets de Firebase ont été listés ici.

Laissez-moi choisir le projet « Firebase front end ».

Oui, nous avons besoin de cette application.

Comment aimeriez-vous appeler votre nouvelle application ?

Attendez une seconde, nous avons fait une erreur.

Nous n'avions pas besoin d'une nouvelle application.

Nous avions déjà une application ici que nous pouvons utiliser.

Projet Firebase front end.

Il télécharge les données de configuration.

Et c'est fait.

Et si nous vérifions notre environnement dans le dossier `src/environments` ?

`environment.ts`, nous verrons nos environnements de stockage, l'ID du projet, toutes ces choses qui viennent de l'aperçu du projet.

Laissez-moi vous montrer.

Si nous descendons, vous voyez, toutes ces choses sont maintenant ici automatiquement.

C'est un soulagement dans les fichiers d'environnement TypeScript de production et de développement.

Maintenant, quand nous redémarrons notre application, `ng serve`.

Allons aux paramètres de la base de données Firestore, allons d'abord à l'authentification.

Attendons que cela commence.

Notre projet a maintenant été lancé, alors ouvrons-le sur `localhost:4200`.

Ouvrez `app.component.html`.

Nous n'avons pas non plus besoin de ce terminal.

Supprimons toutes les données HTML ici.

Et dans le TS, vous verrez que nous recevons tout, tout est importé automatiquement.

Ouvrez `app.component.ts`.

C'est le composant pour ce HTML, donc nous écrivons le HTML d'un côté et ici nous écrivons la logique.

Récupérons d'abord les données.

Mais gérons d'abord l'authentification.

Nous avons besoin de deux champs d'entrée.

E-mail et mot de passe.

Ce que nous pouvons faire, c'est copier l'entrée précédente de cette page.

Copiez simplement ce div et placez-le dans le fichier HTML.

Supprimez les boutons.

Et ajoutons simplement le style de `index.css` et plaçons-le dans `app.component.css`.

Sauvegardez tout.

Maintenant ils sont là, mais pas centrés.

Copiez ces choses et collez-les dans... attendez.

Copiez simplement le nom de la classe `main`.

Et ce sera au centre comme ceci.

Donnons-leur un peu de marge.

Nous n'avons pas de nom de classe ici.

Donnez-leur un nom de classe `input-fields`.

Un peu de marge entre eux.

Nous n'avons pas besoin des étiquettes (labels), supprimez-les.

Donnons maintenant une classe à cette entrée.

Parce qu'il est peut-être difficile pour vous de voir les champs d'entrée ici.

Si ce n'est pas le cas, c'est bien.

Ne confondez pas.

Voici un peu de style.

Faisons-en 100 %.

Pourquoi cela ne fonctionne pas ? D'accord, nous avons aussi besoin d'un point ici.

Si nous rafraîchissons, d'accord, c'est trop moche.

Faisons 300 pixels.

Ça a l'air bien maintenant.

Maintenant, nous avons besoin d'un bouton.

Bouton « Sign In » et un autre pour « Sign Up ».

Donnez-leur une classe aussi.

Nous n'avons pas besoin d'utiliser cela.

Un peu de marge aussi pour nos boutons.

Le curseur est un pointeur.

Nous avons maintenant le bouton de connexion et d'inscription.

Maintenant, nous devons obtenir les données de ces deux champs.

Faisons cela.

J'ai enveloppé tout le code dans une balise `form`.

Et j'utilise ce formulaire de connexion pour la fonction appelée `handleRegister`.

Ici, nous avons `ngModel` dans les deux champs.

Et nous pouvons collecter notre valeur lorsque nous cliquons sur s'inscrire ou se connecter.

Maintenant, ce que nous devons faire, c'est importer quelques éléments.

Importez depuis `@angular/fire/auth`.

`Auth`, `createUserWithEmailAndPassword` et `signInWithEmailAndPassword`.

Laissez-moi décomposer cela.

Et nous devons faire un constructeur ici.

Nous devons créer un type `auth` ici.

Ouvrez la console sur les valeurs.

Ce que nous avons à faire, c'est juste cette chose, qui s'appelle `createUserWithEmailAndPassword`, puis nous devons passer cet `auth` puis l'e-mail.

L'e-mail est `value.email`.

Et la troisième chose est `value.password`.

Pourquoi je ne peux pas taper correctement, très bien, mais nous devons utiliser `this.auth`.

Rendons cela public.

Maintenant, nous pouvons nous inscrire et cela renverra des données.

Nous allons juste les attraper.

La réponse sera de type `any`.

Et nous dirons simplement `console.log(response.user)`.

Mais si cela échoue, nous l'attraperons.

Nous l'afficherons dans une alerte.

Sauvegardez-le.

Inscrivons-nous maintenant.

Dans Firebase, nous avons un e-mail.

Nous pouvons nous inscrire ou nous connecter.

Inscrivons-nous d'abord.

Entrez le mot de passe, inscrivez-vous.

Voyez, l'e-mail est déjà utilisé, nous avons cette erreur ici.

Et si nous nous connectons, ce sera la même chose.

Supprimez le bouton « Sign In ».

Mais si vous vous inscrivez avec un e-mail différent, cela fonctionnera.

Ouvrez la console, effacez-la et changez un peu l'e-mail.

Nous obtenons toutes les données, vous voyez.

Et ce sera mis à jour dans l'authentification Firebase.

Maintenant, ajoutons la connexion.

Copiez la fonction et créez `handleLogin`.

Je vais juste passer la fonction ici.

Nous utiliserons `signInWithEmailAndPassword`.

Il prend les mêmes choses.

D'abord l'authentification, la valeur de l'e-mail et du mot de passe.

C'est fini.

Copions également ce bloc `then/catch`.

Maintenant, essayons de nous connecter.

Entrez l'e-mail et le mot de passe.

Si nous ouvrons la console, cela fonctionnera car nous avons le bon e-mail et le bon mot de passe.

Voyez, cela nous renvoie ces données.

Si nous entrons le mauvais e-mail, nous aurons une erreur dans l'alerte.

Mais si nous entrons le mauvais mot de passe, mais le bon e-mail, nous aurons toujours une erreur.

L'authentification est faite.

Voyons maintenant comment ajouter un document dans la base de données Firestore.

Nous avons besoin de quelques changements.

Disons que le nom de la fonction est `addData`.

Supprimez toutes ces choses et aussi la méthode de connexion précédente.

Nous n'avons pas besoin de cette instance `auth`.

Ensuite, nous devons ajouter ces données à cette fonction.

Si nous avons entré un nom et un mot de passe, ils devraient être ici dans la console.

Maintenant, importons quelque chose ici.

Depuis `@angular/fire/firestore`.

La première chose à importer est `addDoc`.

La seconde est `Firestore` pour initialiser, puis le mot-clé `collection` pour spécifier les collections.

Ajoutez ces choses d'abord, puis dans le constructeur, nous devons ajouter l'instance de Firestore.

`public firestore: Firestore`.

Voyez, nous n'avons qu'un seul document ici, alors ajoutons-en un autre.

Pour ajouter, nous utilisons d'abord `collection`, puis passez cette instance de Firestore.

`this.firestore`.

La deuxième chose qu'elle prend est un nom de collection, donc c'est « users ».

Ensuite, nous devons passer cette instance dans la fonction `addDoc` avec les données que nous voulons ajouter.

Passez l'instance et les valeurs.

Nous pouvons utiliser le bloc `then`.

Nous dirons « données envoyées ».

Mais si cela échoue, nous afficherons le message d'erreur.

Ajoutons un e-mail et un mot de passe.

Données envoyées et vérifions ici.

Nous avons une autre donnée ici.

Nous pouvons ajouter plus de champs, comme le nom.

Nous avons trois champs maintenant.

Si nous l'envoyons, nous aurons notre troisième champ dans le document ici.

Essayons.

Données envoyées, et ce sera ici avec le nouveau champ de saisie.

C'est ainsi que nous ajoutons des données dans Firestore en utilisant Angular.

Maintenant, lisons les documents de Firestore.

Importez la fonction `getDocs`.

Créons une collection dans le constructeur.

Créons une fonction appelée `getData`.

Nous allons juste passer la collection à cette fonction `getDocs`.

Et cela renverra des données.

Appelons le bloc `then`.

Et nous ferons `console.log(response.docs.map(item => item.data()))`.

Qu'est-ce qu'on fait de mal ici ?

Très bien, nous utilisons `item.data()`.

Si nous ouvrons la console, nous devons appeler la fonction ici dans le constructeur.

Nous utiliserons le mot-clé `this` pour la référence.

Voyons la console.

Rafraîchissez, nous obtenons les trois zones ici, vous voyez, mot de passe, e-mail et le nom s'il y en a un.

Maintenant, nous pouvons le stocker dans une variable.

`public data: any[] = [];`.

Et si nous stockons simplement ces données ici, cela fonctionnera.

Nous pouvons juste faire `this.data = response.docs.map(...)`.

C'est stocké dans la variable `data`.

Nous devons juste copier la donnée publique.

Et ici, après le formulaire, nous pouvons boucler sur le tableau.

Utilisons `ngFor`.

`let item of data`.

Ensuite, nous pouvons juste faire `item.name`.

Nous obtenons le nom parce que nous n'en avons qu'un seul.

Si nous mettons l'e-mail, ou ajoutons ceci.

Le premier sera l'e-mail, le troisième sera le mot de passe.

Et nous aurons notre e-mail, le mot de passe et si nous avons un nom, nous l'aurons aussi.

La lecture du document est également faite.

Maintenant, mettons à jour les données.

Nous avons d'abord besoin d'un bouton.

Et cela s'appellera « Update ».

Et créons ou importons deux choses ici, qui s'appelleront `doc` et `updateDoc`.

`doc` sera utilisé pour spécifier quel document mettre à jour.

Mais `updateDoc` sera utilisé pour mettre à jour le document que nous avons choisi.

Créez une fonction appelée `updateData`.

Elle prendra notre ID de type chaîne.

Et nous devons ajouter la fonction à ce bouton.

Sur l'événement `(click)`, `updateData(item.id)`.

Nous devons le recevoir ici.

Si nous affichons l'ID dans la console, nous devrions obtenir l'ID du champ sur lequel nous travaillons.

Essayons de cliquer sur mettre à jour pour ce premier champ.

C'est ici.

Nous n'utiliserons pas d'imports dynamiques, nous allons simplement le mettre à jour statiquement en utilisant les données statiques que nous voulons.

Ce que nous pouvons faire ici, c'est spécifier quel document mettre à jour.

`const dataToUpdate = doc(this.firestore, 'users', id);`.

Elle prend trois paramètres : l'instance de firestore, la collection et l'ID.

Ensuite, nous utiliserons simplement la fonction `updateDoc`.

Et nous passerons deux choses : le document à mettre à jour et les données que nous voulons mettre à jour.

Ajoutons le nom « Ashish ».

Sauvegardez ceci.

Si c'est réussi, nous afficherons une alerte « Données mises à jour ».

Et si cela échoue, nous l'attraperons.

Maintenant, mettons à jour n'importe quel champ.

Ici, nous n'avons pas le nom « Ashish ».

Il sera donc ajouté si nous cliquons sur mettre à jour ici.

Et une chose de plus que nous pouvons faire est d'appeler cette fonction `getData` après la mise à jour car elle rafraîchira alors automatiquement la page.

Nettoyons d'abord les données.

Cliquez, mis à jour et voyez le nom « Ashish » est apparu ici.

Si nous le changeons pour autre chose.

Le nom du troisième champ est mis à jour.

Nous pouvons le changer comme ceci.

Le quatrième est la suppression.

Nous avons également besoin d'un bouton de plus ici.

La fonction s'appellera `deleteData`.

Sauvegardez le fichier et créez une fonction ici.

`const dataToDelete = doc(this.firestore, 'users', id);`.

Nous devons également importer `deleteDoc`.

Nous pouvons faire `deleteDoc(dataToDelete)`.

Et le reste sera fait dans le bloc `catch`.

Récupérons aussi l'ID.

Si je clique sur supprimer ici.

Si on clique sur supprimer, cela devrait être supprimé.

Si on clique sur supprimer pour celui-ci.

Changeons l'e-mail ici, il sera mis à jour.

Nous mettons à jour deux champs.

L'e-mail est maintenant celui que nous voulions.

Et le mot de passe est le même, mais le nom a été changé.

Supprimons ce champ.

Supprimé.

Et il n'est plus là.

Toutes les quatre opérations sont maintenant terminées, ce qu'on appelle les opérations CRUD.

C'était beaucoup sur Angular et comment gérer l'authentification Firebase et les opérations CRUD.

Maintenant, gérons l'authentification Firebase et les opérations CRUD dans React.

Dans le dossier pour React, nous allons simplement taper `npx create-react-app firebase-react`.

Gardez à l'esprit que les noms doivent être en minuscules.

Attendons qu'il finisse.

Notre application React a maintenant été créée.

Ouvrez un terminal et faites `npm install firebase`.

Installez ce paquet.

Ensuite, nous devons créer deux champs d'entrée.

E-mail et mot de passe.

Supprimez les éléments inutiles.

Appliquons un style.

Ajoutons un bouton pour s'inscrire.

Nous avons besoin de deux fonctions dans `App.js`.

`handleInput` et `handleSubmit`.

`handleInput`, nous le ciblerons sur ce champ d'entrée.

`onChange`.

Et dans le bouton de soumission, nous l'ajouterons sur `onClick`.

Créons un état.

Importez `useState` de React.

Ce sera un objet qui contiendra deux propriétés : e-mail et mot de passe, vides initialement.

Ici, nous devons récupérer l'entrée.

Si le nom correspond, nous stockerons la valeur.

Si c'est l'e-mail, et si c'est le mot de passe.

Nous les stockerons dans leurs états respectifs.

Ensuite, nous devons simplement stocker ces données.

Nous devons également stocker les données précédentes.

Laissez-moi vous montrer ce que je veux dire si nous affichons cela dans la console.

Entrez l'e-mail et le mot de passe.

Voyez, nous n'obtenons que le mot de passe, pas l'e-mail.

C'est parce que nous ne définissons que le champ des entrées.

Ce mot de passe écrase l'e-mail.

Pour corriger cela, nous devons passer les données actuelles et les données précédentes.

Maintenant, vérifions.

E-mail et mot de passe.

Oui, maintenant nous voyons que nous lisons l'e-mail et le mot de passe.

Maintenant, nous pouvons l'utiliser dans l'authentification Firestore.

Ajoutons l'authentification.

Importons les deux choses.

Nous avons besoin de l'application et de la base de données.

D'abord, créons-les.

Dans le dossier `src`, créez un fichier `firebaseConfig.js`.

Copiez ces éléments ici.

Nous devons exporter la configuration.

Et nous avons besoin d'une chose de plus : `getFirestore`.

Initialisons également Firestore.

Maintenant, importons ces outils dans le fichier principal.

Importez `app` et `database` depuis `./firebaseConfig`.

Mais nous devons aussi obtenir les éléments d'authentification.

Ouvrez l'onglet Authentification.

Importons d'abord de `firebase/auth`.

`getAuth`, `signInWithEmailAndPassword` pour la connexion et `createUserWithEmailAndPassword` pour la création de compte.

Nous avons besoin de ces trois.

Créez une instance pour l'authentification.

`const auth = getAuth();`.

Dans la fonction de soumission, `handleSubmit`, nous devons juste appeler cette fonction `createUserWithEmailAndPassword`.

Nous passerons cette instance `auth`, puis l'e-mail et le mot de passe.

`data.email`, `data.password`.

Ensuite, nous devons faire le bloc `then`.

Et si cela échoue, nous dirons `error.message`.

Si nous sauvegardons et essayons d'ajouter une entrée.

Si nous nous inscrivons, nous aurons une erreur car nous avons déjà cet e-mail dans l'authentification.

Voyez, e-mail déjà utilisé.

Mais si nous utilisons un e-mail différent.

Et cliquez sur s'inscrire.

Ce sera réussi, nous lisons toutes ces données ici.

Et ici.

Si nous rafraîchissons l'onglet Authentifications, ce sera dans les utilisateurs.

C'est fait.

Maintenant, ajoutons la connexion.

Remplacez cette fonction `createUserWithEmailAndPassword` par `signInWithEmailAndPassword`.

Si nous essayons cela, cela devrait fonctionner, nous obtiendrons les mêmes données ici.

Nous obtenons ces données parce que maintenant nous ne créons pas le compte, nous nous connectons.

Si nous utilisons le mauvais e-mail, nous aurons une erreur.

Mais si nous utilisons le mauvais mot de passe aussi, nous aurons l'erreur de mot de passe.

C'est ainsi que nous gérons l'inscription ou la connexion.

Une chose à vous montrer avant cela est que nous pouvons stocker ce jeton à l'intérieur de notre stockage de session (session storage).

Et nous pouvons l'utiliser pour notre authentification.

Ceux-là sont faits.

Voyons maintenant comment envoyer des données vers Firebase Firestore.

Nous avons besoin de quelques éléments ici aussi.

`collection` et `addDoc`.

Importons depuis `firebase/firestore`.

`collection` sera utilisé pour spécifier une collection et `addDoc` ajoutera des données à l'intérieur de la collection.

Laissez-moi supprimer cela car nous allons juste envoyer des données d'ici.

Nous devons ajouter un champ de plus ici appelé nom (`name`).

Ajoutons-le ici.

Une autre propriété d'objet appelée `name`, vide au début.

C'est fait.

Dans la fonction `handleSubmit`, nous devons utiliser...

D'abord, créons une collection.

Si vous ouvrez la base de données Firestore, nous verrons le nom de notre collection ici : « users ».

Nous devons ajouter le nom de la collection.

Nous avons besoin de la base de données et du nom de la collection.

Utilisons `addDoc`.

Nous passerons l'instance de la base de données et ensuite les données.

Nos données sont `data`.

Passez-les simplement comme ceci.

Et c'est fait.

Si c'est réussi, nous appellerons le bloc `then`.

Indiquant que les données ont été envoyées, sinon nous afficherons l'erreur.

Sauvegardez et maintenant essayons d'entrer le nom, l'e-mail et un mot de passe.

Données envoyées et si nous vérifions ici.

Oui, c'est maintenant enregistré ici.

C'est Michigan Kumar et le même e-mail/mot de passe.

Nous savons maintenant comment ajouter des données.

La suite est de récupérer les données de Firestore.

Nous allons créer un hook `useEffect` et une fonction `getData`.

Ici, nous écrirons notre logique pour obtenir les données.

Nous avons besoin d'une chose de plus appelée `getDocs`.

Nous allons simplement utiliser `getDocs` et passer l'instance ici.

C'est l'instance `dbInstance`.

Cela spécifiera le nom du document et la base de données.

Alors créons simplement un hook `useEffect`, ou vous pouvez le faire comme ça sur le bouton, passez simplement la fonction.

Si on clique sur le bouton, cette fonction s'exécutera, mais nous devons en faire une fonction asynchrone.

Nous devrons attendre (`await`) cela et nous stockerons les données dans une variable.

Et nous pouvons afficher ces données, mais nous devons les mapper.

Ouvrez la console, cliquez sur « Get Data ».

Nous obtenons toutes les données que nous ne pouvons pas lire.

Laissez-moi filtrer.

Nous allons les mapper.

Cela prendra un paramètre `item`, puis nous retournerons simplement `item.data()` et ensuite l'ID de l'item.

Maintenant vérifions, « Get Data ».

Nous obtenons trois objets dans un tableau d'ici.

C'est ainsi que nous récupérons les données de Firebase Firestore.

L'étape suivante est la mise à jour des données.

`const updateData = () => { ... }`.

Pour mettre à jour les données, nous utiliserons simplement une fonction appelée `doc`.

Cela nous indiquera quel champ éditer dans Firestore.

Et ce `updateDoc` éditera.

Nous devons d'abord ajouter le `doc`.

Créons une nouvelle variable.

Cela prendra le `doc` et ici nous passerons trois choses.

La base de données, le nom de la collection et l'ID.

Nous devons spécifier quel document éditer.

Nous allons récupérer l'ID à partir de ces champs.

Créons un nouveau bouton ici en bas.

Mais le truc c'est, d'accord, ce qu'on peut faire, c'est mapper ces données d'abord.

C'est simple aussi.

Créons un état `array` et `setArray`.

Et ensuite, définissez le tableau ici.

Nous allons mapper le tableau ici.

Cela prendra un `item`, vous pouvez écrire ce que vous voulez, cela retournera quelque chose.

Retournons le nom de l'item, l'e-mail, le mot de passe, donc il bouclera à travers ce tableau.

Comme nous l'avons fait dans la version Angular.

Nous avons donc besoin d'un bouton ici aussi.

Bouton `onClick`, cela appellera la fonction `updateData` et nous définirons l'ID.

Récupérez l'ID ici.

Nous n'utiliserons pas d'ID dynamique, nous allons simplement le mettre à jour statiquement.

Nous devons importer `updateDoc` de Firestore.

Nous avons aussi besoin de supprimer le document.

`deleteDoc` devrait être ici.

Nous ferons `updateDoc` et nous passerons les données à mettre à jour et les données à l'intérieur.

Faisons la mise à jour comme ceci.

Changeons d'abord le nom.

Ajoutons l'e-mail pour qu'il soit autre chose.

D'accord, mettons à jour seulement cela.

Et si c'est réussi, nous afficherons un message.

Mais si cela échoue, nous l'attraperons.

Maintenant, cliquez sur le champ de mise à jour ici.

Cet ID sera passé à la fonction.

Et il est juste mis à jour en utilisant cette variable et les données.

Je suppose que vous voyez ce que je veux dire ? Si c'est réussi, nous devrons appeler `getData` pour obtenir les données mises à jour.

Si nous cliquons sur le premier champ, le nom sera changé.

Mis à jour et voyez c'est maintenant Nishan.

Si on en fait « Ashish ».

Le nom du troisième champ est mis à jour.

Nous pouvons aussi obtenir le mot de passe.

Si on change les trois champs, ils seront modifiés.

C'est ainsi que nous téléchargeons des données dans Firestore.

Le quatrième est `deleteData`.

Il suffira de faire `deleteDoc`.

Ici aussi, il prendra l'ID.

Nous devons importer `deleteDoc` ici et nous devrons simplement passer le document à supprimer.

Rien d'autre.

En cas de succès, mettons « Données supprimées ».

Et nous devons passer la fonction et un ID dans le bouton.

Supprimer.

Et au clic du bouton, appelez `deleteData` et passez `item.id`.

Nous avons maintenant un bouton de suppression.

Cela devrait être supprimé.

Et voyez, ce n'est plus là.

Si nous vérifions Firestore.

C'est supprimé en temps réel.

Nous avons ajouté les quatre méthodes des opérations CRUD : ajout, suppression, récupération de données et mise à jour de données.

C'est ainsi que nous effectuons les opérations CRUD dans React, ainsi que les méthodes d'inscription et de connexion avec e-mail et mot de passe.

Vous pouvez également ajouter une autre méthode d'inscription appelée authentification Google ou authentification GitHub.

Et c'est très facile.

Très bien.

Laissez-moi maintenant commenter les commandes de ces codes et les sauvegarder.

Nous pouvons simplement ajouter des données ici et elles apparaîtront en bas.

Si nous entrons le nom, l'e-mail et le mot de passe.

Ajouter des données.

C'est ici.

C'est ainsi que nous faisons toutes les choses dans Firebase et React.

Apprenons à authentifier notre application Next avec Firebase.

Nous utiliserons l'authentification Google et GitHub ainsi que l'inscription par e-mail, nous verrons aussi comment envoyer ou sauvegarder des données.

C'est ce qu'on appelle aussi les opérations CRUD dans une application Next.

Alors, commençons.

La première chose à faire est de créer notre application Next.

`npx create-next-app@latest`.

Donnons un nom à l'application : `next-crud-auth`.

Il télécharge tous les paquets.

Ensuite, ce que nous devons faire, c'est créer une application dans Firebase.

`next-auth-crud`.

Nous n'avons pas besoin d'analyses, créez simplement un projet ici.

Notre projet est en cours de création.

Et ici aussi dans l'application React.

Notre projet Firebase a été créé ici.

Maintenant, ce que nous allons faire, c'est créer une application.

`crud-auth`.

Allons dans ce dossier de projet.

Ici nous avons des pages, nous avons `index` notre page principale, nous avons nos modules node qui contiennent toutes nos dépendances.

Nous avons `package.json` qui contient toute la liste des paquets.

Maintenant, installons Firebase ici.

`npm install firebase`.

Nous avons besoin de cette commande pour que Firebase fonctionne.

Pendant ce temps, créons aussi un fichier ici : `firebaseConfig.js`.

Il contiendra toutes ces données de configuration.

Copiez ces éléments et collez-les ici.

Nous devons exporter cela du dossier.

Maintenant, nous pouvons utiliser cette application dans notre projet.

D'accord, nous devons le faire dans cette page d'accueil.

Mais avant cela, créons un dossier appelé `layouts`.

À l'intérieur, créez un fichier `index.js`.

Cela contiendra notre mise en page pour toutes les pages.

Nous allons créer deux pages.

Une pour l'enregistrement, une pour la page d'accueil.

Nous n'avons pas besoin de Next pour le moment.

Créons deux pages.

Nous avons déjà `index`, qui servira de page d'accueil.

Changeons-le d'abord.

Supprimez tout ce qui se trouve à l'intérieur de la balise `main`.

Sauvegardez.

Et changeons le titre ici : `Next CRUD`.

Définissons maintenant nos méthodes d'authentification.

Cliquez sur « Get Started » ici.

Nous utiliserons e-mail/mot de passe.

Activez ceci.

Sauvegardez.

Ajoutons deux fournisseurs de plus.

Google active.

Sauvegarder.

Ajoutons aussi GitHub.

Nous utiliserons la connexion pour GitHub et Google.

Mais pour cela, nous avons besoin d'un ID client et d'un secret client.

Allez sur github.com et allez dans les paramètres.

Ouvrez les applications OAuth.

Et créons-en une nouvelle.

`crud-auth`.

L'URL de la page d'accueil, faisons-en `localhost:3000`.

Commençons l'application.

`npm run dev`.

Copiez cette URL et mettez-la ici.

Ensuite, nous avons besoin du callback, que nous devrions obtenir de Firebase.

Copiez cette URL d'authentification et collez-la, puis enregistrez l'application.

Elle nous renvoie l'ID client que nous devons utiliser ici.

Et un secret client.

Copiez ce secret client et collez-le, puis sauvegardez.

Nous avons activé l'e-mail et le mot de passe, Google et GitHub.

Très bien, que pourrions-nous faire maintenant ?

Nous sommes maintenant ouverts ici sur `localhost:3000`.

Créons la page des mises en page (layouts).

Avant cela, donnons à cet accueil un titre `h1`.

Il apparaît ici.

Maintenant, créons une autre page, ce devrait être `register.js`.

Une autre pour `login.js`.

Nous avons le composant d'enregistrement et le composant de connexion.

Et dans l'index, nous sommes bien.

Ce que je dois faire, c'est créer une mise en page ici pour la route.

La première chose à faire est d'importer `useRouter` de `next/router`.

Nous n'avons pas besoin d'utiliser React Router car ce n'est pas React, c'est Next.

Et il vient avec son propre routeur.

Nous exportons cette constante `layout`.

Nous avons besoin de `Link` de `next/link`.

Ensuite, nous devons envelopper nos routes dans un lien.

`Link href="/register"`.

Si nous allons à « register ».

Ajoutons un composant ici.

`export default function Register() { ... }`.

Retournons un div, à l'intérieur ajoutons un `h1`.

Sauvegardez, nous allons maintenant sur la page d'inscription.

Nous pouvons voir ce texte ici.

Faisons de même pour la connexion.

Appelons ça « Login ».

Importons les styles de `Home.module.css`.

Ajoutez-le ici.

Nous allons le mettre au centre.

Copiez ce div jusqu'au pied de page (footer) et collez-le ici.

Faites-en « register ».

Et copiez ceci à nouveau et collez-le ici.

Je suppose que nous devons aussi importer `Head`.

Dans la page d'inscription.

Ça marche bien.

Faites de même pour la connexion, changez juste le texte.

Nous devons ajouter l'entrée pour la connexion.

Mais nous devons ajouter le lien pour la connexion.

Et ajoutons « login » ici.

Nous avons le texte de connexion ici.

Ajoutons-en un autre pour la page d'accueil.

Appelons-le « home ».

Et si nous allons à Home, ce sera le texte d'accueil.

D'accord, ce n'est pas trouvé, pourquoi ?

Si nous ouvrons home, c'est `index`.

Changeons-le en `home.js`.

Nous avons maintenant la mise en page ici.

Et nous passons ceci.

Maintenant, nous devons importer ce fichier de config Firebase dans la page d'accueil.

Importez `app` depuis `firebaseConfig`.

Dans la page d'accueil, ça marche bien.

Nous pouvons voir notre pied de page ici.

Créons d'abord notre page d'inscription.

Fermez toutes ces choses.

Dans ce fichier `register.js`, ajoutons le style et les données.

Supprimons le pied de page, nous n'en avons pas besoin ici.

Allez à la page d'inscription.

Importez `app` depuis le fichier de config Firebase.

Ensuite, nous devons créer des entrées de texte.

Entrée pour l'e-mail et le mot de passe.

Donnez à cette entrée un nom de classe `input-box`.

Sauvegardez, stylisons-le un peu.

Dans le fichier `Home.module.css`.

Disons 200 pixels de large.

Utilisons les styles.

C'est maintenant large.

Répétez l'opération pour la deuxième entrée.

Ajoutons une hauteur.

Donnons-leur aussi un peu d'espace.

Marge de 5 pixels.

Maintenant nous avons l'e-mail et le mot de passe.

C'est mieux, on peut taper l'e-mail et le mot de passe.

Maintenant, ce que nous allons faire, c'est créer un état.

E-mail et mot de passe avec `useState`.

Ensuite, nous devons simplement les lire.

Dans l'e-mail, nous devons utiliser l'événement `onChange`.

`setEmail(e.target.value)`.

Et copiez et mettez le même ici.

Mais cette fois, ce devrait être `setPassword`.

Maintenant nous pouvons obtenir notre e-mail et notre mot de passe correctement.

Créons une fonction ici.

`signUp`.

Ensuite, nous devons juste importer la méthode de Firebase.

Depuis `firebase/auth`.

Nous devrons importer deux choses : `getAuth` et...

Quelle est la méthode pour s'enregistrer avec l'e-mail ?

Laissez-moi voir la méthode pour se connecter avec e-mail et mot de passe.

Ce n'est pas « register ».

Laissez-moi chercher la méthode d'inscription Google pour Firebase.

Nous devons utiliser le web. Créer l'utilisateur avec e-mail et mot de passe.

Je l'ai maintenant, nous utiliserons ces deux.

Ensuite, créons une instance d'authentification.

`const auth = getAuth();`.

Copiez `createUserWithEmailAndPassword`, puis vous devez juste passer l'authentification, puis l'e-mail et enfin le mot de passe.

Maintenant, si nous nous sommes inscrits, cela peut nous renvoyer à la page d'accueil.

Nous devons créer une instance de routeur.

Importez `useRouter` de `next/router`.

Ensuite, créez une instance.

Ensuite, nous pouvons juste dire `router.push('/home')`.

Cela nous ramènera vers cette route d'accueil.

Maintenant, nous devons créer un bouton ici.

Bouton « Sign Up ».

Donnons un style au bouton.

`button-sign`.

Dans la classe de bouton, nous dirons simplement 100 pixels.

Ajoutons une hauteur de 35.

Curseur pointeur.

Maintenant, ce que nous pouvons faire, c'est utiliser le bouton d'inscription, ajoutez l'événement `onClick`.

Ajoutez le nom de la fonction `signUp`.

Maintenant, ajoutons notre e-mail ici et notre mot de passe.

Mais avant cela, faites en sorte que le type de mot de passe soit `password`.

Et celui-ci est `email`.

Si on tape un mot de passe ici, il devrait être au format pointillé.

Inscrivez-vous ici.

Voyez, nous sommes maintenant sur la page d'accueil, nous nous sommes inscrits avec succès.

Ouvrez maintenant les utilisateurs dans l'authentification et nous pouvons voir notre e-mail.

Nous devons revenir ici et en créer deux de plus.

Deux options de plus : une pour Google et une pour GitHub.

« Sign up with Google » et « Sign up with GitHub ».

Ajoutons une ligne horizontale rouge entre eux.

Parce que nous utilisons le flexbox, cela est poussé vers le bas.

Très bien, ça ne fait rien.

Maintenant, nous devons utiliser les boutons d'inscription Google et GitHub.

Répétez les styles ici également.

Maintenant nous avons fini, mais le problème est que nous devons utiliser...

D'accord, ça a l'air bien, peu importe.

Nous montrons simplement la fonctionnalité, pas le style de l'application.

Ce que nous devons faire, c'est créer une autre fonction ou deux autres fonctions.

La première sera `signUpWithGoogle`.

La deuxième fonction sera GitHub.

Nous pouvons utiliser une seule fonction pour les deux, mais ce sera compliqué.

Nous devons importer les méthodes pour l'inscription Google et GitHub.

Importons d'abord `GoogleAuthProvider`, puis `GithubAuthProvider`.

Ce sont les deux choses dont nous avons besoin ici.

Nous devons spécifier le fournisseur pour Google.

`const googleProvider = new GoogleAuthProvider();`.

De même pour GitHub.

Pour GitHub, c'est `GithubAuthProvider`.

Dans cette fonction pour Google, nous pouvons utiliser cette fonction appelée `signInWithPopup`.

Et nous devons passer l'authentification et le fournisseur.

Le premier bouton est Google.

Et nous allons enregistrer la réponse.

Nous pouvons faire la même chose ici aussi.

Affichons-le dans la console d'abord.

`response.user`, nous devons obtenir l'ID utilisateur à partir d'ici.

Maintenant, ce bouton d'inscription avec Google, nous devons le mapper dans ce bouton ici.

Au clic sur ce bouton Google.

Et faites de même pour GitHub.

Maintenant, si nous cliquons sur ce bouton Google, cela ouvrira une fenêtre.

Ouvrez d'abord la console pour voir ce que nous obtenons.

Dans les fournisseurs, nous n'avons pas l'e-mail, nous avons juste mon e-mail ici.

Inscrivons-nous à nouveau avec Google.

Nous voyons un pop-up.

Et nous devons utiliser notre e-mail pour nous inscrire.

Cliquez sur votre e-mail.

Et cela nous montrera toutes les données à l'intérieur de l'utilisateur que nous obtenons dans la console : jeton, nom d'affichage, e-mail, si l'e-mail est vérifié ou non.

Et si nous voyons l'authentification Firebase, rafraîchissons.

Le fournisseur est maintenant Google, vous voyez, cela fonctionne bien maintenant.

La chose suivante que nous devons ajouter est GitHub.

Dans ce fournisseur de données, mettez la même méthode ici.

Mais ce fournisseur Google devrait être le fournisseur GitHub.

Copiez cette méthode et ajoutez-la à GitHub.

Au clic de ce bouton GitHub.

Si nous nous connectons à nouveau à GitHub, cliquons sur ce bouton.

Voyez, nous recevons toujours ce pop-up pour GitHub maintenant, pas Google.

Vous voyez, nous lisons que le compte existe avec des identifiants différents. C'est parce que nous utilisons déjà mon e-mail ici.

Nous devons donc d'abord supprimer cela pour que GitHub fonctionne.

Si nous rafraîchissons maintenant et essayons à nouveau, GitHub, cliquez sur votre e-mail.

Ou cliquez sur « Authorize ».

Voyez, ça marche maintenant.

Et si nous ouvrons la console, nous verrons peut-être le fournisseur GitHub ici.

Le nom d'affichage est le même.

Si je rafraîchis ces trois champs, le fournisseur est maintenant GitHub.

Et mon e-mail est maintenant listé ici.

Nous avons fini ici, je suppose, l'authentification est maintenant faite.

La dernière chose à faire est de le pousser vers la page d'accueil.

Si nous nous inscrivons maintenant, nous devrions être sur la page d'accueil.

Inscrivez-vous à nouveau avec Google.

Et ils travailleront car nous avons déjà le même e-mail et nous sommes sur la page d'accueil.

Faisons encore une chose ici pour les opérations CRUD : importez `useEffect` de React.

Ensuite, créez un hook `useEffect` ici en bas des fonctions.

Et nous n'avons pas de tableau de dépendance.

S'il est vide, cela signifie qu'il ne s'exécutera qu'une seule fois lorsque nous chargerons notre page.

Stockons simplement notre jeton à l'intérieur du stockage de session.

C'est une bonne pratique pour l'authentification.

`sessionStorage.setItem('token', response.user.accessToken);`.

Et j'utilise ce stockage de session parce qu'il est détruit quand nous fermons cet onglet.

Donc si nous fermons l'onglet, nous devrions être déconnectés automatiquement.

Faites la même chose ici et là.

Très bien, nous définissons maintenant le jeton à l'intérieur de la session.

Retournez en arrière et connectez-vous à nouveau avec Google ou GitHub ou votre e-mail/mot de passe.

Si vous ouvrez l'onglet Applications, nous devrions voir notre jeton ici.

Nous devons créer une vérification ici d'abord.

Récupérons le jeton du stockage de session quand nous chargeons une application.

`let token = sessionStorage.getItem('token');`.

Vérifions ici si le jeton existe.

S'il n'est pas vide.

S'il y a un jeton ici, nous pouvons simplement nous renvoyer vers la page d'accueil en utilisant `router.push`.

Sauvegardez-le.

Donc, si nous revenons en arrière, nous avons notre jeton ici.

Et si nous essayons de revenir en arrière, nous devrions être renvoyés vers cette page d'accueil, voyez, nous ne pouvons pas revenir dans l'historique car nous avons un jeton à l'intérieur ici.

Faisons la même chose pour la page d'accueil.

Ouvrez cette page d'accueil et créez le même hook qu'auparavant.

Importez `useEffect` de React et c'est fini.

Le routeur n'est pas défini.

Importez d'abord `useRouter` de `next/router`, puis créez une constante `router`.

Ici, nous devons faire quelque chose comme : si nous n'avons pas de jeton, nous allons juste nous renvoyer vers la page d'inscription.

Sauvegardez.

Nous ne pouvons pas revenir en arrière.

Mais essayons de détruire ce jeton maintenant.

Supprimez-le dans l'application de session.

Si nous rafraîchissons la page maintenant, nous n'avons pas le jeton.

Nous ne pouvons donc pas avancer vers la page d'accueil.

Parce qu'il vérifiera si nous avons un jeton ou non.

L'authentification est maintenant terminée.

Passons maintenant aux opérations CRUD en utilisant Next.

Inscrivez-vous à nouveau avec Google.

Nous ferons ces choses dans notre page d'accueil ici, alors ouvrez la page d'accueil.

Créons deux entrées.

Une pour le nom et celle-ci pour l'âge.

Donnons-leur quelques styles.

Copiez le nom de la classe de base et ce style est correct.

Utilisez `styles.inputBox`.

Répétez cela ici une fois de plus.

Supprimons le pied de page car il prend de la place.

Ajoutons également un bouton.

Bouton « Add ».

Maintenant, nous pouvons ajouter des données en utilisant ce bouton.

Nous pouvons juste utiliser le nom de la classe ici aussi pour le bouton que nous avons créé.

Ajoutez le nom de la classe `styles.button` ici.

Sauvegardez.

Nous avons maintenant un bouton ici que nous pouvons utiliser pour ajouter des données à Firebase.

Mais avant tout cela, nous allons stocker les données à l'intérieur de cette base de données Firestore.

Créez la base de données ici, faites-en le mode test.

C'est fait.

Activez-la.

En attendant, importez la fonction depuis `firebase/firestore`.

Importez `getFirestore`.

Et créons un autre export ici pour la base de données.

`export const database = getFirestore(app);`.

Nous avons la base de données Firebase créée ici.

Nous devons importer cela à l'intérieur de la page d'accueil.

Nous importons donc toute l'application et la base de données.

Maintenant, nous devons créer l'instance de la collection.

`const databaseRef = collection(database, 'data');`.

Importons `collection` de `firebase/firestore`.

Ensuite, nous créerons simplement la collection qui prend deux choses : la base de données et le nom de la collection.

Appelons-la « data ».

C'est fini ici.

Nous avons besoin d'une fonction de plus.

Nous devons importer quelques éléments ici.

Autre que la collection, il y a `addDoc`.

Nous devons utiliser `addDoc` pour ajouter des données.

Et nous avons différentes fonctions pour toutes les différentes méthodes.

`addDoc` est utilisé pour ajouter des documents.

Nous allons juste utiliser `addDoc`, et nous dirons simplement, passez cette référence de base de données ici.

Ensuite, l'état du nom et de l'âge.

Nous avons besoin de deux états.

`name`, `setName` et `age`, `setAge` avec `useState`.

Ensuite, nous pouvons simplement récupérer le nom entré ici dans les entrées.

Nous pouvons juste dire `onChange` et cela prendra un paramètre `event`.

Et nous stockerons `event.target.value` à l'intérieur de `setName`.

Et copiez et collez à nouveau, faites cela pour `setAge`.

Si nous tapons quelque chose ici.

Importez `useState` ici.

Maintenant nous pouvons taper quelque chose ici et dans l'âge.

Dans cette entrée d'âge, faisons-en un type de nombre (`number`).

Ajoutez simplement `type="number"`.

Parce qu'on ne peut pas ajouter de caractères alphabétiques ici, on ne peut ajouter que l'âge.

Très bien, faites en sorte que l'entrée soit de type texte pour le nom.

Ajoutons aussi la valeur, ce devrait être l'état appelé `name` et ici `age`.

Maintenant, essayons. Ajoutez simplement le bouton à cette fonction ici.

Sur `onClick`, `addData`.

Maintenant, nous devons passer les données à l'intérieur de cette base de données.

Le nom devrait être l'état `name`.

Et le suivant devrait être l'âge de l'état `age`.

Si c'est réussi, nous utiliserons `then` pour indiquer que les données ont été envoyées.

Nous pouvons afficher une alerte ici.

« Données envoyées ».

Mais si cela échoue, nous pouvons juste utiliser un bloc `catch` pour lancer l'erreur.

Sauvegardez.

Essayons maintenant.

Ce que nous devons faire ici est de vider les valeurs après l'envoi.

Donc nous pouvons mettre `setName('')` et `setAge(null)`.

Maintenant essayons, mon nom Nishant, âge 25, puis ajoutez-le ici.

Données envoyées, cliquez sur OK.

Et ils sont effacés.

Si nous vérifions le Firestore de Firebase, nous devrions obtenir nos données ici, notre nom et notre âge et l'ID du document de la collection.

Cet ID est unique.

Ajoutons-en un autre.

Données envoyées, d'accord.

Et cela devrait être ici.

Si nous rafraîchissons ceci, cela devrait être là.

Vous voyez le deuxième document de collection est ici.

Mais le fait est que nous ajoutons un nombre ici, mais nous servons une chaîne ici.

Nous devons donc convertir ce nom en un nombre.

Enveloppez-le simplement dans `Number()`.

Maintenant, si nous essayons à nouveau.

Cliquez sur ajouter, puis terminez.

Vous voyez, l'âge est maintenant un nombre ici. Ce n'est pas une chaîne.

Notre `addDoc` est fait.

Passons maintenant au document de lecture.

Nous devons importer une fonction ici aussi qui s'appelle `getDocs`.

Et créez une fonction ici.

`const getData = () => { ... }`.

Ensuite, nous devons simplement utiliser cette fonction `getDocs`.

Nous devons passer cette référence de base de données.

Et c'est tout pour obtenir les données.

Nous devons d'abord appeler cette fonction.

Alors, comment appeler cela ? Nous devons l'appeler quand notre page se charge.

Dans ce hook `useEffect`, passez-le simplement.

Nous l'appelons.

Nous devons donc rendre cette fonction asynchrone.

Et l'utiliser, parce que nous utilisons une promesse ici.

Nous pouvons juste dire `.then` pour enregistrer la réponse que nous obtenons.

Voyons la console maintenant.

Et nous obtenons ces données.

Si on rafraîchit.

Mais il y a beaucoup de données à l'intérieur que nous ne pouvons pas lire correctement.

Nous devons donc obtenir les données dans ce format.

Cela devrait être un tableau, celui-ci devrait être un objet.

Et à l'intérieur des objets, nous aurons différentes propriétés de nom et d'âge.

Ce que nous pouvons faire, c'est mapper pour obtenir nos données.

Nous devons mapper ces documents ici.

Cela prend un paramètre, disons `data`.

Retournez les données, et la valeur à l'intérieur des données.

Si nous sauvegardons maintenant, nous obtenons ces trois objets ici, dans un tableau d'objets.

Ajoutons aussi l'ID ici, cet ID de document pour différencier les trois.

Nous devons l'envelopper dans des accolades.

Et nous devons le fusionner avec l'ID, donc nous dirons simplement `id: data.id`.

Maintenant nous pouvons voir notre ID aussi.

Vous voyez, nous avons cet ID ici.

Maintenant, où stocker cela dans un tableau ? Créez un état de tableau.

`fireData` et `setFireData`.

Définissez-le ici.

Maintenant, mappons nos données `fireData` pour voir les données dans notre interface utilisateur (UI).

Après le bouton, nous allons créer un div ici d'abord.

Ensuite, nous devons juste mapper `fireData`.

Nous pouvons juste dire `data` pour itérer, et nous devons retourner des données ici.

Mettons-le dans un div.

Ensuite, nous devons cibler l'objet `data.name`.

La deuxième chose est l'âge.

Sauvegardez.

Et maintenant nous pouvons voir notre nom et notre âge respectivement.

Faisons-en un `h2` car `h1` est trop grand.

Maintenant nous pouvons voir notre nom et l'âge.

Mettons-les sur une seule ligne.

Utilisons `styles.flex`.

Ensuite, dans `Home.module.css`, nous pouvons simplement ajouter ce flex.

`display: flex`.

Aussi `justify-content: space-evenly`.

Très bien, mais ici ce n'est pas régulier alors faites `justify-content: space-between`.

Qu'en est-il du troisième ? Pourquoi n'est-il pas reflété correctement ?

Supprimons tous ces styles prédéfinis ici.

Ajoutons simplement la marge.

Ou disons juste `gap` pour ajouter l'espace entre les éléments flex.

Maintenant nous avons un peu d'espace ici.

Nous avons le nom et l'âge.

Ajoutons aussi le texte « Nom : » et « Âge : » ici.

La lecture est maintenant terminée, ainsi que cette opération de lecture.

Très bien, le nom et l'âge sont récupérés.

Voyons maintenant comment mettre à jour ces champs.

Pour mettre à jour ces champs, nous avons besoin d'un bouton à côté de ces champs ici.

Ajoutez un bouton et donnez-lui un style de bouton que nous avons dans `Home.module.css`.

Si on clique sur ceci, cela doit être envoyé à une fonction.

Créez une fonction ici.

`const updateFields = (id) => { ... }`.

Et nous enverrons l'ID depuis ce bouton.

Sur `onClick`.

Affichons l'ID ici.

Maintenant, ouvrez la console. Si nous cliquons sur le bouton de mise à jour pour le premier champ, nous obtenons l'ID.

Maintenant, mettons à jour les champs.

Nous avons besoin d'une fonction ici d'abord, ce devrait être `doc`.

Et nous devons mettre à jour le document.

`addDoc` nous dira quel champ éditer dans Firestore.

Et ce `updateDoc` éditera.

Nous devons ajouter le document d'abord.

Créons une variable pour le champ à éditer.

Cela prend le `doc` et ici nous passerons trois choses.

La base de données, le nom de la collection.

Et la troisième chose dont nous avons besoin est l'ID.

Nous avons le champ à éditer maintenant.

Ensuite, nous devons simplement utiliser la fonction `updateDoc` et passer ce champ à éditer comme premier paramètre.

Deuxièmement, nous devons importer le nom, puis nous avons l'âge mis à jour.

Si c'est réussi, nous pouvons afficher une alerte « Données mises à jour ».

Mais s'il y a une erreur, nous pouvons l'attraper.

Essayons de mettre à jour.

Si nous cliquons sur mettre à jour ici, c'est mis à jour, mais nous faisons quelque chose de mal.

Attendez une seconde, mise à jour des champs.

Nous faisons cela mal car nous devons ajouter cette fonction comme `getID`.

Nous n'avons pas besoin de cela ici, nous devons le faire sur le bouton Ajouter.

Si nous cliquons sur ceci, nous aurons notre ID.

Nous avions quelque chose de mal ici.

Supprimez ce premier.

Si on rafraîchit, ce sera bien maintenant.

Maintenant nous devons obtenir ce nom et cet âge dans ces champs d'entrée.

Nous devons envoyer le nom et l'âge.

Nous devons les enregistrer dans cette fonction de `getID`.

Dites simplement que le nom est le premier et ensuite nous ajoutons l'âge.

Maintenant, définissons le nom et l'âge à l'intérieur de ces états d'entrée.

`setName(name)` et `setAge(age)`.

Essayons maintenant de mettre à jour, cliquez sur « Update ».

Nous obtenons le nom et l'âge ici, vous voyez.

Mais nous devons faire une chose de plus.

Si nous cliquons sur mettre à jour ici, ce bouton d'ajout devrait être changé en mise à jour.

Créons une valeur booléenne `isUpdate` et `setIsUpdate` avec `useState`, faux au début.

Ensuite, nous mettrons `isUpdate` à vrai lorsque nous cliquons sur le bouton de mise à jour ici.

Sur ce clic de bouton, nous appelons cette fonction.

Définissez simplement cela sur vrai.

Maintenant, si c'est vrai, nous montrerons un bouton de mise à jour au lieu du bouton d'ajout.

Si c'est vrai, il montrera le bouton de mise à jour ou sinon le bouton d'ajout.

Créons une autre fonction pour mettre à jour les données.

`const updateData = () => { ... }`.

Ensuite, nous devons ajouter ce champ à éditer.

Créons aussi une vérification pour l'ID.

Copiez ceci et ajoutez la constante `ID` et `setID` qui devrait être nulle car l'ID est un nombre.

Nous définissons l'ID, le nom et l'âge ici.

Dans ce champ de mise à jour, copiez simplement cette fonction `updateDoc` précédente et nous devons l'ajouter ici.

Enlevez le commentaire et cela fonctionnera.

Ce `updateDoc` prend le champ à éditer et il se met à jour.

Ajoutez le champ de mise à jour à ce bouton.

Essayons maintenant, Nishan et l'âge 24 pour le premier, cliquez sur « Update ».

Et vous verrez le bouton est maintenant changé en « update ».

Cliquez sur « Update », mis à jour.

Et si vous vérifiez ici, d'accord, maintenant, Nishan est le nom.

Ici aussi, il faut ajouter la propriété `Number()` avant l'âge pour le convertir en nombre.

Maintenant si on essaye à nouveau.

Si on en fait 27, cliquez sur « Update », mis à jour.

Et le nombre est maintenant un nombre.

Ça marche bien.

Ce que nous devons faire maintenant est juste de remettre toutes ces données à nul et en chaîne vide si nous avons mis à jour.

Une chose de plus à faire, nous ne pouvons pas voir notre bouton d'ajout ici.

Pour voir le bouton d'ajout, nous devons définir `setIsUpdate` sur faux quand nous chargeons notre application ou quand nous cliquons sur « Add Data ».

Si nous rafraîchissons, c'est ici.

Très bien, laissez tomber.

Pour l'instant nous pouvons mettre à jour.

Et nous pouvons le régler sur faux quand nous avons mis à jour avec succès.

Essayons maintenant, mettons à jour l'âge à 25, cliquez sur « Update ».

Et le bouton est maintenant « add ».

Mais ce numéro n'est pas supprimé d'ici car je ne sais pas ce qui ne va pas avec l'entrée de numéro.

Muttons à jour cette deuxième valeur.

Mis à jour et c'est reflété ici, vous voyez l'âge est 27 et le nom est Nishant.

Maintenant ajoutons la fonction de suppression.

Ajoutez un bouton juste comme cette mise à jour pour supprimer ceci.

Il devrait être ici, ajoutez un bouton de suppression.

Et cela fera la même chose que la mise à jour pour simplement passer l'ID.

Nous n'avons pas besoin du nom et de l'âge, nous devons juste supprimer en utilisant cette fonction `getID` qui lit l'ID ici.

Ensuite, nous devons simplement importer une chose de plus qui s'appelle `deleteDoc` pour supprimer le document.

Créez simplement une fonction pour appeler `deleteDoc`.

Nous devons l'utiliser en premier et passer simplement le champ à éditer.

Nous pouvons enregistrer cette donnée en utilisant `then`.

Et nous allons juste afficher une alerte ici pour dire « données supprimées ».

Ensuite, attrapez l'erreur si elle se produit.

Essayons de supprimer le nom de Nishan et l'âge 25, cliquez sur « Delete » ici.

D'accord.

Nous devons ajouter la fonction ici aussi, dans ce bouton de suppression.

Attendez une seconde.

Pour supprimer, nous n'avons pas besoin d'utiliser `getID`, nous avons juste besoin d'utiliser `getDocument` et de passer l'ID.

Passez l'ID et recevez l'ID et faites-en simplement `ID`.

Rafraîchissez encore.

Et vérifions.

Supprimez le premier champ.

Supprimé ici.

Vous voyez nous n'avons pas le champ de Nishan et l'âge 25.

Mais on peut le voir ici.

Cela signifie que nous avons déjà fini les données.

Quand on clique sur supprimer, on peut juste appeler la fonction `getData` pour cliquer à nouveau.

Maintenant nous ne voyons plus de champs ici.

Nous devons donc mettre la fonction `getData` dans le champ de mise à jour également.

Ici, collez-la après l'alerte.

Dans le champ d'ajout également.

Si on l'ajoute.

Données envoyées et c'est reflété ici.

Ajoutez un autre nom.

Nous avons trois champs.

Maintenant, ajoutons le dernier.

Maintenant nous avons quatre champs.

Et dans ce Firestore, nous avons quatre objets avec des propriétés de nom et d'âge.

Maintenant, essayons de mettre à jour ce champ.

Faites 25, cliquez sur « Update ».

Et cela se passe maintenant en temps réel.

C'est mis à jour correctement.

Mettons à jour Ashish, cliquez sur mettre à jour.

C'est mis à jour en temps réel.

Supprimons Nishant, cliquez ici sur ce bouton de suppression.

Supprimé, et nous ne voyons plus le nom de Nishant ici ni dans Firebase.

Nous avons maintenant fait les quatre opérations : création, lecture, mise à jour et suppression.

Nous avons également ajouté l'authentification ici, donc nous ne pouvons pas revenir en arrière à moins de nous déconnecter.

Créons un bouton de plus.

Le dernier bouton pour la déconnexion ici.

Nous pouvons juste créer un div ici et mettre un bouton à l'intérieur.

Bouton « Log out ».

Créons une fonction ici.

`const logout = () => { ... }`.

Ensuite, nous devons simplement détruire le jeton à l'intérieur de la session.

Ensuite, nous devons simplement naviguer vers notre page d'inscription.

`sessionStorage.removeItem('token');`.

Ensuite nous retournerons à l'inscription.

Maintenant nous devons juste ajouter ce bouton de déconnexion dans la fonction de ce bouton.

Cliquez sur déconnexion.

Maintenant, nous allons à la page d'inscription.

Et maintenant nous pouvons revenir à la page d'accueil.

Parce que nous avons des routes protégées dans Next.js.

Si nous nous inscrivons, seulement alors nous pouvons aller à cette page d'accueil.

Inscrivez-vous avec mon compte e-mail.

Voyez, nous voyons maintenant la page d'accueil ici avec le nom et l'âge et toutes les données.

Encore une chose avant d'aller dormir, je dois créer une autre page pour la connexion.

Créons `login.js`.

Elle existe déjà.

D'accord, nous l'avons déjà ici.

Alors allons à la page de connexion.

Nous pouvons voir le texte de connexion.

Nous devons faire la même chose que ce que nous avons fait pour l'inscription, copiez toutes les données et collez-les dans `login`.

Changez juste un peu de texte ou le titre.

Faites-en « login ».

Ici, nous n'avons pas besoin de `createUserWithEmailAndPassword`, parce que c'est une page de connexion.

Nous devons nous connecter ici.

Laissez-moi vous montrer ce que je veux dire.

Si nous retournons à la page d'inscription.

Ajoutons un e-mail au hasard.

Disons que c'est l'e-mail d'un utilisateur.

Ajoutez un mot de passe, cliquez sur s'inscrire.

Il devrait être ici dans l'authentification Firebase.

Nous avons cet e-mail et le mot de passe.

Si nous essayons maintenant de créer l'utilisateur avec le même compte e-mail, nous ne pourrons pas le créer.

Cela va lancer une erreur.

Ajoutons le même e-mail ici.

Ouvrez la console.

L'e-mail est déjà utilisé, car nous l'avons déjà ici dans cet onglet d'authentification.

Ce que nous devons faire, c'est nous connecter, pas nous inscrire à nouveau avec le même e-mail.

Nous pouvons lancer une erreur avec une alerte.

Disons que l'e-mail existe déjà.

Pour nous connecter, nous devons créer une fonction de connexion.

Se connecter avec Google ou avec un mot de passe.

Remplacez simplement `createUserWithEmailAndPassword` par cette fonction appelée `signInWithEmailAndPassword`.

Maintenant ça va marcher.

Si on rafraîchit ceci, essayons encore.

Ajoutons cet e-mail et le mot de passe, changeons le texte en « log in » ici.

Maintenant cliquez sur s'identifier ici.

Nous devons être sur la page de connexion.

Entrez l'e-mail.

Sign in, vous voyez que nous sommes maintenant connectés ici.

Mais si nous utilisons le mauvais e-mail pour nous connecter, alors que nous ne sommes pas enregistrés correctement, nous aurons une erreur.

Utilisons n'importe quel e-mail non enregistré.

Voyez, nous recevons cette erreur « l'e-mail n'existe pas ».

D'accord, attendez, nous avons ajouté le mauvais message d'erreur.

C'est « l'e-mail n'existe pas ».

Et dans l'inscription, nous devons ajouter ce message d'erreur précédent « existe déjà ».

Mettez-le dans le bloc `catch` ici.

Connectez-vous à nouveau.

Et vous voyez « l'e-mail n'existe pas ».

Parce que nous n'avons pas celui-là ici.

Créons-le sur la page d'inscription.

S'inscrire.

Voyez toutes les données.

Maintenant, que se passe-t-il si nous utilisons le mauvais mot de passe pour nous connecter à nouveau ?

Si nous rafraîchissons, nous devrions être capables de voir le compte ici.

Connectons-nous avec cet e-mail, mais le mot de passe sera faux.

Essayons, nous aurons toujours cette erreur ici car nous n'utilisons pas de messages d'erreur personnalisés ici.

Ou on peut juste dire « impossible de se connecter ».

Si nous obtenons cette erreur parce que nous avons quelque chose de mal dans l'e-mail ou dans le mot de passe.

Sign in.

Vous voyez « impossible de se connecter » parce que je pense que le mot de passe est faux.

Maintenant on peut se connecter ici.

Nous avons fait toutes les fonctionnalités de notre application, de l'authentification aux opérations CRUD.

Je me déconnecte maintenant et je vais dormir.