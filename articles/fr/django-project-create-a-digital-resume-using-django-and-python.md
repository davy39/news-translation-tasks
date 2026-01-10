---
title: Projet Django – Créer un CV Numérique avec Django et Python
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-10-26T17:15:47.000Z'
originalURL: https://freecodecamp.org/news/django-project-create-a-digital-resume-using-django-and-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/djangoresume.png
tags:
- name: Django
  slug: django
- name: youtube
  slug: youtube
seo_title: Projet Django – Créer un CV Numérique avec Django et Python
seo_desc: "Django is a popular web development framework that uses Python. \nWe just\
  \ published a course on the freeCodeCamp.org YouTube channel that will help you\
  \ improve your Django skills by teaching you how to create a digital résumé using\
  \ Python and Django.\n..."
---

Django est un framework populaire de développement web qui utilise Python.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous aidera à améliorer vos compétences en Django en vous apprenant à créer un CV numérique en utilisant Python et Django.

Bobby Stearman a développé ce cours. Bobby a créé de nombreux cours populaires sur sa propre chaîne YouTube.

Pour ce cours, Bobby a collaboré avec un designer pour fournir aux téléspectateurs un modèle de CV numérique gratuit. Vous apprendrez à personnaliser le modèle et à utiliser Django pour créer un backend dynamique.

Une excellente page de CV peut vous aider à obtenir des emplois. Et utiliser Django pour le backend vous permettra d'ajouter du contenu à la page sans mettre à jour le HTML.

Le cours est divisé en quatre sections principales :

* Sélection et téléchargement d'un modèle
* Démarrage d'un Projet Django
* Modification du Frontend
* Création du Backend

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/0oSsLbh_Kv4) (1,5 heure de visionnage).

%[https://youtu.be/0oSsLbh_Kv4]

## Transcription

(générée automatiquement)

Améliorez vos compétences en Django en construisant un site web de CV numérique.

Bobby Stearman enseigne ce cours, il fournit un modèle de site web de CV gratuit et vous apprendra à programmer le backend en utilisant Django.

Salut tout le monde, probablement du code mort ici.

Et j'ai préparé ce cours aujourd'hui, parce que si vous êtes comme moi, vous avez postulé pour de nombreux rôles de développeur au fil des ans.

Et vous avez réussi certaines fois, mais vous avez manqué la plupart.

Maintenant, c'est parce qu'il y a tant de développeurs talentueux.

Donc vous devez vous démarquer dans la foule, il est absolument primordial que vous le fassiez.

Donc je vais vous montrer aujourd'hui comment numériser votre CV en utilisant Django.

Maintenant, la raison pour laquelle nous utilisons Django est double.

Premièrement, avec Django, vous avez une page d'administration intégrée, qui vous permet de créer, lire, mettre à jour, supprimer des objets.

Donc cela évitera d'avoir à mettre à jour le code source dans votre projet.

Donc nous pouvons ajouter des objets dans la page d'administration, et cela est rendu directement dans le HTML, ce qui est fantastique.

Et deuxièmement, cela nous donne l'occasion de perfectionner nos compétences en Django.

Donc nous allons d'abord lier un modèle, nous avons un modèle que vous pouvez télécharger gratuitement, nous allons ensuite créer le projet Django, nous allons construire le backend et le frontend, et ensuite nous allons tout assembler.

Donc cela prendra un peu plus d'une heure.

Donc c'est sauter directement dedans.

C'est le modèle que nous allons utiliser.

Donc cela a été conçu par James Granger design, un collègue à moi, c'est fantastique.

Il a mis cela ensemble, nous ne facturons personne, vous pouvez accéder à ce modèle dans notre dépôt GitHub, qui est github.com/bobby-decoding/decoding_resume_template.

Donc le modèle de CV de décodage comme je dis complètement gratuit, tout ce que vous avez à faire est de cloner un dépôt et vous aurez accès à celui-ci, je vais vous montrer aujourd'hui comment lier ce modèle à un projet Django.

D'accord, voici à quoi ressemble le modèle tout en haut.

Ici, vous avez un avatar, vous avez une bio ou ce sera une bio, nous avons ensuite un lien pour télécharger un CV, donc nous avons besoin d'une version PDF de votre CV, et nous l'attacherons à un profil utilisateur.

Nous avons des compétences clés, des compétences en codage avec une barre de glissement, nous avons quelques certificats que nous pouvons faire défiler, nous avons une section portfolio, nous avons une section témoignages.

Et nous avons aussi des publications récentes.

C'est la page d'accueil, nous avons une vue liste de portfolio.

D'accord, nous avons une vue liste de blog, qui est presque la même, et une page de contact.

Les pages portfolio et blog auront également des pages de détails.

Et elles seront rendues sur le frontend avec un éditeur de texte riche, que nous ajouterons également à l'administration Django.

Donc ce que nous ajoutons dans un éditeur de texte riche sera rendu directement tel qu'il est vu dans l'administration sur le frontend, ce qui est fantastique.

Comme je le dis, nous créerons des objets dans l'administration Django sans avoir besoin de changer le code source du projet.

D'accord, et ce formulaire Contactez-nous permet aux employeurs potentiels de vous contacter, ajouter le nom, l'email et un message et soumettre.

Super.

Donc c'est le modèle.

C'est ce que nous construirons aujourd'hui dans Django.

Donc la première chose que nous devons faire est d'utiliser un éditeur de texte.

J'utiliserai Visual Code Studio aujourd'hui.

Et cela est ouvert en développement.

Donc la première chose que j'ai ici est un terminal ouvert.

La première chose que nous devons faire est de créer un environnement virtuel.

Maintenant, j'utilise un wrapper d'environnement virtuel.

Donc je peux simplement utiliser la commande make virtual env V et nous appellerons cela resume demo.

D'accord, et cela va créer un environnement virtuel sur ma machine et le lancer.

La raison pour laquelle je sais qu'il est lancé est parce que nous avons cela entre crochets ici.

Donc resume demo.

Donc maintenant que c'est là.

Nous avons maintenant accès à pip.

Donc nous pouvons pip installer Django.

Nous installerons également pillow.

Et nous installerons également Django ck, editor.

D'accord, ce sont les trois dont nous aurons besoin dès le départ.

D'accord, une fois que cela a fini de tout installer, nous démarrerons un projet Django.

Et nous l'appellerons encore une fois comme l'environnement virtuel.

Nous appellerons cela resume demo.

D'accord.

Ne vous inquiétez pas si vous avez cela qui apparaît.

Il vous dit simplement que vous devez mettre à jour PIP, il suffit de coller cela.

Bob est votre oncle, cela a installé la dernière version de PIP.

Donc nous sommes prêts à partir.

Bien ? Donc maintenant nous devons voir D.

Non, nous n'en avons pas besoin, nous devons démarrer un projet.

Donc parce que nous avons installé Django, nous pouvons maintenant accéder à l'administration Django.

Et nous disons démarrer le projet.

Et nous appellerons cela resume.

Demo.

D'accord, c'était démarrer le projet, nous pouvons maintenant voir D dans resume demo.

Le voilà.

Et ouvrons-le dans mon navigateur ici.

Le voilà, vous savez quoi, ouvrons un nouveau dossier.

Pour le filament, nous l'ouvrons simplement ici.

Donc nous n'avons pas toutes les autres choses.

Ouvrons le terminal.

Et nous irons travailler.

Encore une autre commande de virtually every rapper.

Donc nous avons ces pop-ups.

Donc nous appellerons nous exécuterons, resume demo, j'ai l'environnement virtuel en cours d'exécution à nouveau.

Et c'est le répertoire du projet.

Donc lorsque vous démarrez des projets, vous obtenez le fichier manage.py.

Et vous aurez également le répertoire resume, resume demo avec le fichier Dunder init, votre fichier de paramètres ASCII, les URLs et le whisky.

D'accord, donc ce que nous ferons maintenant, nous pouvons accéder à Manage dot p y, ce que nous pouvons faire, nous pouvons Python, manage dot p y was Stein app.

Et nous appellerons cela made.

D'accord.

Et maintenant nous allons faire ce que je vais faire, je vais me référer à mon autre écran, parce que j'ai construit ce projet dans une étape précédente pour m'assurer que tout fonctionne.

Et cela accélère les choses plutôt que de devoir me regarder faire des fautes de frappe et devoir déboguer tout mon code.

Donc je vais déplacer cela d'un autre écran en copiant et en collant, c'est bien et fluide, et nous ne serons pas trop maladroits.

Donc la première chose que nous allons faire est d'ouvrir settings dot p y.

D'accord, et voici à quoi cela ressemble lorsque vous installez pour la première fois le projet Django.

Tout en haut ici, importer OS.

Cela nous permet d'accéder au système d'exploitation, ce projet nécessitera l'utilisation de fichiers statiques.

Donc la raison pour laquelle nous avons O S est parce que nous allons l'utiliser dans une seconde pour joindre le répertoire de base aux nouveaux répertoires de fichiers statiques.

Nous avons cela au base dir qui sera référencé, c'est la clé secrète.

Maintenant dans un environnement de production, vous sécuriseriez cela peut-être dans un EMV de quelque sorte, mais nous ne le ferons pas dans ce tutoriel, le débogage est vrai, les hôtes autorisés sont bons.

Ce que nous devons faire, c'est ajouter main dans nos applications installées, nous devons également ajouter CK editor là.

Cela nous permettra d'utiliser un éditeur de texte riche dans la page d'administration du middleware.

Nous n'avons pas besoin de middleware que je sache, juste double vérification.

Non, nous n'en avons pas besoin, mais nous ajouterons un processeur de contact.

Donc le processeur de contexte ira ici.

Processes dot p y, le contact process P y ressemblera à ceci.

Donc nous importerons le modèle utilisateur ici comme le modèle utilisateur intégré.

Et nous ajouterons simplement un argument clé appelé meat au contexte process.

Et tout cela viendra, vous comprendrez ce qui se passe bientôt.

Nous allons définir dans stop p y, nous pouvons maintenant ajouter ce processeur de contexte au processeur de contexte ici.

Donc nous aurons lu resume demo est contact processes dot project context.

Nous n'avons pas besoin de celui-là.

D'accord, donc maintenant ce contexte ici, donc ce mot-clé mi sera accessible dans les modèles que nous construisons plus tard dans cette démonstration.

Donc l'application whisky, nous n'avons pas besoin de faire quoi que ce soit là.

Nous allons simplement utiliser la base de données SQL lite trois intégrée, vous pourriez la mettre à niveau vers PostgreSQL ou Myos.

QL mais nous n'étions pas dans celui-ci.

Donc lorsque nous faisons les migrations, il y aura un fichier DB SQ lite qui apparaît, mais ne vous inquiétez pas trop de cela.

Nous changerons le N en GB.

Et ce que nous ferons ensuite, c'est que nous ajouterons les fichiers statiques et la route statique et la route média et ce que vous avez.

D'accord, donc je ne vais pas passer en revue ce que nous essayons de faire ici.

Mais essentiellement, nous devons accéder aux fichiers statiques ou aux fichiers statiques, comme les fichiers CSS, les fichiers JavaScript et les images qui ne changent pas.

Bien.

Donc ils se trouvent dans un répertoire statique, nous accéderons à des choses comme les logos, des choses comme les feuilles de style en cascade.

Donc les paramètres ici nous permettent ou indiquent au système où se trouvent ces répertoires et comment ils vont être gérés.

D'accord.

Donc c'est tout.

Nous n'avons pas besoin de faire autre chose pour les paramètres.

Mais nous avons besoin d'un autre fichier ici appelé URLs dot p y.

C'était déjà inutile.

Oui, nous n'en avons pas besoin.

Donc je m'emballe.

Donc tout fichier URLs, p, p y, je vais alors copier tout cela.

Donc nous devons ajouter include path, nous devons apporter les paramètres de django.com.

Et nous devons static de Comp dot URLs dot static.

Et nous ajouterons le chemin signifie cette URL, donc nous n'avons même pas créé cela encore.

Mais nous le ferons dans une seconde.

Mais nous ajoutons cela au motif d'URL.

Donc toutes les URLs dans le fichier main dot URLs que nous créerons dans une seconde, feront alors partie de nos motifs d'URL.

D'accord, nous pourrions l'appeler main namespace equals main.

Donc c'est ce que nous l'appellerons dans l'application dans quelques secondes.

Et puis nous avons cela ici.

Donc si settings dot debug, nous ajoutons alors l'URL statique, et une route statique aux motifs d'URL.

Et nous faisons de même pour l'URL média et la route média.

Donc dans l'environnement de développement, nous aurons simplement un répertoire statique ici.

Et nous aurons un média qui sera appelé fichier média.

Donc lorsque nous sauvegardons un avatar ou une image, il ajoutera un répertoire et ajoutera l'image ou le fichier au répertoire dans le répertoire des fichiers multimédias.

D'accord, donc c'est les URLs là.

Main, ce que nous devons faire, c'est tout de suite nous avons besoin de URLs dot p y, bien ? Donc nous aurons ce fichier.

Et nous le créerons, nous ferons référence aux vues que nous n'avons pas encore créées, mais nous les ajouterons quand même.

D'accord, la raison pour laquelle nous faisons cela est que nous essayons de le faire dans un bon ordre.

Normalement, vous ajouteriez cela après avoir créé les vues, et vous ne créeriez pas les vues tant que vous n'auriez pas ajouté les modèles, mais nous faisons référence à ce fichier dans ce fichier urls.py.

Donc nous apportons le chemin des vues, d'accord, que nous n'avons pas encore créées.

Le nom de l'application est main.

D'accord.

En fait, ce que nous pourrions faire, parce que nous devons peut-être faire quelques migrations, avant de faire cela, donc je vais commenter celles-ci.

D'accord, donc parce que nous n'avons pas produit, nous ne les avons pas encore créées.

De toute façon.

Donc nous commencerons dans l'ordre.

Donc ce que vous commencez, vous commencez avec les modèles, d'accord.

Donc les modèles se traduisent par des tables de base de données, d'accord.

Donc nous créerons un modèle, le nom devient le nom de la table, et les champs deviennent les lignes, désolé, les colonnes, et ensuite pour chaque objet que nous sauvegardons devient chaque ligne dans cette table.

Donc c'est essentiellement ce qu'un modèle Django représente, copie.

Et nous collerons, d'accord.

Donc, nous importons les modèles, et nous importons un modèle utilisateur intégré qui se trouve dans le contrat ou les modèles, nous en avons besoin parce que nous allons l'étendre pour le profil utilisateur.

D'accord, nous l'étendrons en utilisant quelque chose appelé signaux.

Mais nous passerons par cela dans une seconde.

Nous importons ensuite un slugger cinq parce que nous avons besoin d'un slug pour notre blog, et notre portfolio aura ensuite un CKEditor.

Donc Django CK editor est un champ de texte riche.

Donc cela, nous pouvons ajouter ce champ de texte riche au blog et au portfolio.

Donc créer un modèle de compétence.

Nous avons une classe meta, et j'ajoute toujours ceux-ci, pas nécessairement nécessaires par défaut, il pluralisera le nom en l'ajoutant là quand même.

Ce n'est pas la fin du monde.

D'accord, donc le nom est égal à ceci est un champ char.

Donc ceux-ci seront les compétences, donc nous revenons ici.

Ceux-ci seront ces compétences ici.

D'accord, c'est ce que nous essayons de reproduire.

Donc nous voulons des compétences en codage et nous voulons des compétences clés.

D'accord.

Donc nous avons le nom de la compétence, le score.

Donc si c'était une compétence clé, ou désolé, une compétence en codage, nous voudrions le noter car nous voulons que les barres de glissement ici représentent 95 ou 80% de la compétence ou de la connaissance ou de votre expertise dans une certaine compétence, nous avons ensuite une image, la raison pour laquelle nous avons une image ou un champ de feu, parce que c'est un SVG.

Donc ces images ici sont des SPGs.

Donc pour chaque compétence clé, nous voulons une image, d'accord, donc nous ferons cela.

Et c'est une compétence clé, qui est un booléen, donc c'est vrai ou faux.

Donc si c'est vrai, alors cet objet représenterait une compétence clé.

Si c'est faux, il représente une compétence en codage.

Donc nous avons ensuite une fonction de chaîne, et elle retourne simplement self dot name.

D'accord, donc c'est notre modèle de compétence, nous avons ensuite un profil utilisateur.

Donc c'est ce qui étend le modèle utilisateur intégré.

C'est pourquoi nous avons un champ un à un ici.

On delete cascade, nous ne produirons ou créerons qu'un seul profil utilisateur.

Donc ce sera nous en tant que super utilisateur, nous avons un avatar, qui a un champ d'image, c'est pourquoi nous avons apporté pillow upload to et cela créera un répertoire dans les fichiers multimédias appelé Avatar.

Et lorsque nous sauvegardons un fichier là, c'est là que cet avatar ira.

Un titre de bio.

Donc l'idée d'une bio est cette partie ici.

Donc cela apparaîtra là, lorsque nous l'ajouterons aux modèles.

Nous avons ensuite des compétences qui en ont beaucoup trop.

D'accord, donc ce serait beaucoup de ces compétences ici.

Et ensuite nous avons un CV, qui est un champ de fichier, cela sera téléchargé vers un répertoire CV, CV.

Donc chaque fois que vous mettez à jour votre CV sur votre copie papier, vous mettrez à jour cela, le téléchargerez vers ce champ ici, et il sauvegardera la nouvelle copie dans le répertoire.

Et ensuite la fonction ou méthode de chaîne ici retourne simplement le prénom et le nom du modèle utilisateur, nous avons ensuite un profil de contact, qui a un horodatage, qui est ajouté automatiquement.

D'accord, donc c'est un champ de date et d'heure sans nom, email message.

Donc si nous regardons ici, nous allons contacter le nom, l'email, le message.

C'est ce que nous essayons de capturer ici.

Témoignage, nous avons une vignette, c'est pour le témoignage à la maison.

Donc ce que nous essayons de faire est de simplement reproduire tous ces éléments, bien.

Donc c'est nous avons besoin d'un téléphone maintenant, nous avons besoin d'un ici, nous allons avoir le nom de la personne qui a donné un témoignage et le rôle.

Et ensuite nous avons la citation elle-même.

Donc ici nous avons le nom, le rôle, la citation, et est actif, nous ajoutons ce champ booléen est actif, tous ces modèles sont le témoignage avec un portfolio dans un blog, car bien que nous voulions ajouter un témoignage, nous voulons pouvoir l'activer et le désactiver rapidement.

Donc s'il est inactif, nous ne voulons pas qu'il apparaisse sur le site web.

Donc c'est pourquoi nous avons un champ inactif là.

Médias.

Donc la raison pour laquelle nous faisons cela est que si nous pouvons ajouter une image à un modèle de média, cette image est enregistrée dans le fichier multimédia, le répertoire multimédia dans le répertoire des fichiers multimédias, et nous avons alors accès à cette URL lorsque nous créons l'image de l'éditeur de texte riche.

Tout cela aura du sens un peu plus tard.

Mais c'est juste un moyen facile d'accéder aux fichiers statiques dans un modèle.

Lorsque nous nous amusons dans l'administration, ce que je vous montrerai ce que cela signifie bientôt.

Donc son image, la raison pour laquelle nous faisons cela est que vous pourriez techniquement ajouter une URL ici pour une vidéo.

Et ensuite, si cela était faux, ce serait une URL vidéo sûre, économisant d'énormes mp4 dans votre base de données.

Fonction de sauvegarde.

Donc.

Donc si l'URL est vide, alors désolé, si désolé, self URL n'est pas vide, alors son image devient faux.

D'accord, donc ajuster programmatiquement cette image en fonction du champ URL.

Et ensuite nous avons un portfolio.

Donc une date.

Donc c'est la date à laquelle le travail a été fait.

Nom, Description du corps.

Donc c'est important.

C'est le champ de texte riche.

C'est ce que cet éditeur de texte riche que nous mettrons à jour dans la page d'administration, ce que vous voyez est ce que vous obtenez rendu en HTML ou dans le navigateur.

Donc il est vraiment important que vous ayez cela là.

Donc le champ de texte riche est référencé tout en haut de la page ici.

Donc il fait partie de CKEditor dot fields.

Ensuite, nous avons une image qui sera la vignette si vous voulez, téléchargée vers le portfolio.

Mais ensuite, nous avons un slug, qui est un champ de slug et est actif.

Voir le champ de slug est peuplé ici avec la méthode de sauvegarde.

Donc si ce n'est pas self ID, donc essentiellement s'il y a un nouvel objet, nous slug ou phi, le self dot name, ce qu'il fait, c'est que tous les caractères deviennent minuscules et tous les espaces sont ensuite soulignés.

Donc cela devient un slug.

Ensuite, nous avons l'URL absolue ici, donc le portfolio slash slugs, self dot slug, nous faisons exactement la même chose pour le blog.

D'accord, donc le blog est essentiellement le même que le portfolio.

Enfin, parce que le certificat, qui est une date, un nom, un type, une description est actif, rien de fantaisiste ne se passe dans le certificat.

Donc ce sont les modèles, ce que nous ferons ensuite, c'est que nous enregistrerons tous ceux-ci dans notre admin.

Donc nous pouvons y accéder, c'est l'une des parties les plus importantes, nous voulons pouvoir accéder à tous ces modèles dans notre page d'administration.

D'accord, donc ce que nous faisons, c'est que nous les importons tous depuis les modèles, tous les nouveaux modèles ici.

Et ensuite nous utilisons un décorateur admin dot register, nous enregistrons le profil utilisateur, mais ensuite nous ajoutons une classe sous celle-ci appelée User Profile admin.

Ce que cela fait, c'est que cela nous permettra d'afficher.

Cela nous permettra d'afficher les champs que nous voulons sur la page d'administration.

D'accord, donc affichons l'ID utilisateur, nous avons ensuite l'horodatage, le nom, et aussi ici, nous avons des champs en lecture seule.

Donc le slug, nous ne pouvons pas le changer, nous ne voulons vraiment pas le changer parce qu'un slug pourrait être utilisé, vous pourriez envoyer un lien de blog, vous pourriez avoir un backlink quelque part pour une page de blog, et vous ne voulez vraiment pas changer le slug parce que ce lien devient alors inactif.

Donc lorsque le slug est produit, il reste le même quoi qu'il arrive.

Donc nous avons un champ en lecture seule.

Donc c'est ce qui se passe dans l'administration, nous avons ensuite besoin d'un moyen de créer le profil utilisateur en utilisant des signaux.

Donc nous irons dans le nouveau fichier main, signals dot p y.

Et nous ajouterons ce code aux signaux, ce qu'il fait est important, post save le bouton, utilise un modèle, import receiver, qui est un décorateur.

Et ensuite nous apportons le profil utilisateur, que nous venons de créer.

Maintenant, ce que ce signal est, c'est un récepteur.

Donc lorsqu'un objet est créé, lorsqu'un objet utilisateur est créé, Pfizer envoie un signal à ce fichier signals.

P y file, il y a un récepteur qui capte ce signal.

Et ensuite cette fonction est appelée par, donc comme créer des profils, nous apportons comme mots-clés, désolé, arguments, envoyer une instance créée, et ensuite quelques arguments de mots-clés.

Donc si créé, donc si l'objet utilisateur est créé, alors nous voulons créer un profil utilisateur.

Et cela deviendra le profil utilisateur, ces objets créent un nouvel utilisateur, qui est un champ un à un, si vous vous souvenez, est égal à l'instance.

C'est ce qui va être utilisé pour créer le profil utilisateur.

Donc lorsque nous créons un super utilisateur, dans quelques instants, cet utilisateur sera créé, le signal avant cela recevra le signal, Bob est votre oncle, aura un profil utilisateur.

Mais nous devons connecter ce fichier signals.py dans le fichier apps dot p y.

Et comment nous faisons cela, c'est que nous écrasons la méthode ready, nous n'avons pas encore de garçon.

Brillant, d'accord, et ensuite nous devons importer main dot signals.

C'est tout ce que nous devons faire.

Donc lorsque cela va démarrer l'application elle-même, l'application principale, et elle dira simplement, lorsque prêt, alors nous devons apporter des signaux et seulement des signaux, tout fonctionnera.

Donc lorsque l'application est en cours d'exécution, les signaux fonctionnent tous, d'accord ? Ce que nous devons faire ensuite, c'est créer quelques formulaires de modèle.

Donc un formulaire de modèle pour notre formulaire de contact, forms dot P, pourquoi ai-je ajouté le I ai ce fichier.

Et ce que nous ferons et forms oh, effaçons, effaçons cela.

Je vais entrer ici.

Et nous voulons un nouveau fichier, pas un nouveau répertoire.

Donc forms.py collons tout.

Oh, donc je m'excuse, copiez et collez les formulaires importants.

Et nous importons également contact profile, qui est le modèle que nous avons fait dans le fichier models dot p y.

Donc ce sera un modèle pour D'accord, donc nous serons, nous n'avons pas vraiment besoin de ceux-ci, je ne les ai jamais enlevés quand je jouais plus tôt.

En fait, cela vaut la peine de vous le montrer.

Donc sauvegardons cela.

Donc c'est un formulaire de modèle et cela représente un formulaire contre le modèle que nous venons de créer, un formulaire de contact.

Donc ce que vous devez faire, c'est que nous devons créer ces variables, une pour chaque champ que nous voulons dans le formulaire lui-même.

D'accord.

Donc nous avons le nom et ensuite nous voulons que cela ici soit la représentation de ce qui sera rendu dans le HTML sur le frontend, d'accord.

Donc les formulaires, cela est un champ de caractères, longueur maximale égale à 100.

Donc la raison pour laquelle c'est 100 est parce que dans le fichier models, ou est-ce, allons dans Contacts.

Le voilà.

Nom longueur maximale 100.

D'accord.

Donc c'est pourquoi nous faisons cela.

Nous avons ensuite requis Teresa, ce champ est vrai.

Donc cela rendra un élément d'entrée, et il sera requis vrai.

D'accord ? Widget est égal à forms dot text input.

Donc c'est un texte.

Donc l'entrée sera de type égal à texte, puis nous avons quelques attributs.

Donc nous avons un placeholder.

Et dans ce cas, il sera star qui sera rendu dans l'entrée réelle elle-même pour être arrêté pour le nom, point point.

Et ensuite vous pouvez ajouter une classe.

Maintenant, nous n'avons pas vraiment besoin de classe, si vous deviez acheter un modèle, les formulaires que vous avez dans le modèle peuvent avoir certaines classes, c'est là que vous ajouteriez ces classes pour vous assurer que le formulaire qui est rendu sur le frontend est exactement le même que ce qui est dans votre modèle.

D'accord, donc c'est ce que nous avons là.

Nous n'en avons pas vraiment besoin, parce que nous n'utilisons pas Form control dans nos modèles, donc je les supprimerai.

Donc email, champ email, longueur maximale est 254, ce qui est complètement standard pour un champ email.

Et ensuite nous avons un placeholder button got a message.

Maintenant, c'est légèrement différent.

Ce n'est pas une entrée de texte, c'est une zone de texte.

Maintenant, nous voulons six lignes.

Maintenant, cela dépend entièrement de votre modèle.

Dans mon modèle, nous avons six lignes, d'accord, donc c'est pourquoi nous avons six lignes.

Mais vous pourriez en avoir 10, ou autre chose, placeholder est message, puis nous avons une classe meta modèle, qui représente son contact profile dans les champs, nous voulons rendre son nom, email message, c'est notre fichier forms.py, puis ce que nous devons faire, c'est ajouter nos vues.

Donc laissez-moi copier tout cela.

J'irai ici dans notre fichier views.py, et je les y déposerai tous.

D'accord, donc tout en haut ici, j'ai ajouté l'importation des messages.

La raison pour laquelle nous voulons importer les messages est qu'un formulaire, lorsqu'un formulaire est valide.

Et lorsqu'un formulaire est sauvegardé, nous voulons alors rendre un message, de sorte que le message apparaisse et dise merci beaucoup pour la soumission du formulaire ou autre chose.

Donc j'apporte des messages pour faire cela.

De dot models import, et ensuite nous voulons importer tous ces différents modèles.

De Django dot views, import generic, nous allons utiliser les vues génériques, template view, list view, form, view, et ainsi de suite.

Ils sont géniaux.

Ces vues de formulaire intégrées, ce sont toutes des vues basées sur des classes.

Mais elles sont construites spécifiquement pour des tâches qui se produisent régulièrement.

Par exemple, une list view, vous rendez une liste d'objets, donc elle fait tout le travail difficile en arrière-plan.

Donc vous avez, vous pouvez rendre, vous pouvez rendre une page web, ils disent, une form view, avec seulement deux ou trois lignes de code, ce qui est génial.

Vous pouvez également faire des vues basées sur des fonctions.

Mais j'aime utiliser ces vues intégrées.

Elles sont fantastiques.

Donc nous avons index view, ce sera notre page d'accueil.

D'accord, donc nous utilisons generic template view.

Donc nous avons besoin, dans une template view, vous devez ajouter le nom du template.

Donc quel nom, quel template utilisons-nous pour rendre cette vue, dans ce cas, ce sera main index.

Donc ce que nous ferons, c'est que nous avons besoin d'un répertoire dans main, appelé templates.

Dans ce répertoire, nous en avons besoin d'un autre appelé main.

D'accord, dans celui-ci, c'est là que nous ajouterons nos templates.

Nous le ferons sous peu.

Nous n'avons pas besoin de le faire tout de suite.

Nous appelons ensuite la méthode get context data.

Et nous faisons un appel super là et ensuite le contexte, nous pouvons alors ajouter des mots-clés au contexte ici.

Donc témoignages, donc nous voulons des certificats de témoignages, des blogs et un portfolio, ce sont des objets.

Donc ceux-ci seront ajoutés au contexte et nous pouvons les référencer dans les templates afin de pouvoir réellement rendre une liste et faire une boucle for en utilisant des filtres de template et des choses comme ça.

Donc nous appelons les objets de témoignage et nous filtrons tout où is active est égal à true, c'est là que ce champ dans les modèles est vraiment pratique.

Donc dans le témoignage, d'accord, is active, par défaut à true.

Mais si dans l'administration nous cliquons pour qu'il soit faux, alors il n'apparaîtra pas dans le contexte parce que nous filtrons tout ce qui est faux.

Donc is active est égal à true.

Donc seuls les objets true, les objets live, les objets actifs, avec aucun certificat, même chose, blog, même chose, portfolio, même chose et ensuite nous ajoutons ces mots-clés au contexte et ensuite nous retournons le contexte.

Donc maintenant dans index nous pouvons référencer les témoignages, et ce sera une liste d'objets.

Nous pouvons rendre la vue de contact, c'est une vue de formulaire.

Donc vous nommez le template, vous nommez la classe de formulaire, et ensuite une URL de succès.

C'est là que l'utilisateur sera redirigé lorsque le formulaire est valide.

Donc nous appelons ensuite la méthode form valid, passons à travers self et form.

Donc c'est le formulaire, que nous passons, qui est un formulaire de contact, form dot save.

Donc nous sauvegardons l'instance du formulaire.

Et ensuite nous envoyons ce message ici, qui est message dot success.

Et un Texas Merci, nous serons en contact bientôt.

Et c'est ce qui sera affiché sur le frontend, nous avons ensuite une vue de portfolio qui a une list view, le modèle est portfolio, vous devez avoir une page nommée par.

Donc cela ne montrera que 10, ou les 10 premiers objets.

Et ensuite le nom du template, le query set.

Ce que nous faisons là, c'est que nous filtrons le query set est actif vrai.

D'accord, donc seulement les vrais portfolios.

Detail View.

Même chose, sauf que pour cela, ce sera le slug.

Donc nous ajouterons cela dans l'URL.

Donc cela montrera le détail.

Donc pour montrer l'objet qui a le slug dans l'URL elle-même, la vue du blog, identique à la vue du portfolio et une vue de détail du blog est identique à la vue de détail du portfolio.

La seule différence est que nous regardons différents fichiers HTML, d'accord.

Donc ce sont les vues, nous allons sauvegarder cela en regardant mon ce que nous n'avons pas fait, c'est que nous n'avons pas créé de fichier de exigences.

Donc nous allons faire PIP freeze exigences dot txt.

Et créons simplement cela.

Ce sont toutes les exigences pour le projet, nous avons Django, vous pouvez voir Django CK editor, nous avons pillow, parce que nous manipulons des images.

Et ce sont toutes les exigences, des jours heureux.

Donc ce que nous devons faire maintenant, c'est que nous devons faire des migrations.

Donc Python manage.py, make migrations, nous devons ensuite Python manage.py migrate.

Et ensuite nous devons aller Python manage.py.

Créer un super utilisateur, cela permettra ensuite de créer, ils déplaceront cela un peu.

Cela permettra ensuite de créer un super utilisateur, voir cela par défaut à Bobby Bob, mais ils savent de toute façon, Bobby à did coding.com mot de passe, il vous le demandera deux fois, il ne semblera pas que vous tapiez, mais il captera les frappes.

Le voilà.

Donc super utilisateur créé avec succès.

Donc ce que nous ferons, c'est que nous irons Python, manage dot p y, run server.

Dites-moi ce que nous n'avons pas fait, nous n'avons pas décommenté les URLs.

Donc nous avons nous avons connecté les vues.

Mais nous n'avons pas décommenté celles-ci.

Donc je vais le faire rapidement.

Donc de retour sur les URLs ici.

Souvenez-vous, nous connectons cette application main à notre fichier comp URL.

Donc tout ce qui apparaît ici, les URLs spécifiques à main.

Donc le chemin est vide, ce sera notre page d'accueil.

Donc ce sera votre localhost port 8000.

Ce sera un index en tant que vue, car nous utilisons des vues basées sur des classes, vous devez utiliser cette vue, si c'était une vue basée sur une fonction, vous n'auriez pas besoin de ce nom est home.

Donc c'est ainsi que nous y faisons référence dans le modèle.

Donc ce serait main hope, c'est ainsi que nous y ferions référence, je vous le montrerai lorsque nous travaillerons là-dessus sous peu.

Contact view même chose, portfolio view est portfolios, juste pluralisé, puis nous avons ceci qui est important.

Donc c'est la vue de détail.

Donc c'est un portfolio slash slug.

D'accord, donc l'URL aura le slug de cet objet.

Et c'est ainsi que nous le capturons dans la vue de détail.

Même chose pour le blog et le slug du blog.

D'accord, donc ce sont les URLs.

Donc si nous allons maintenant dans notre terminal, nous l'avons ouvert, je devrais simplement pouvoir double-cliquer dessus.

Le voilà.

Ce n'est pas une seconde.

Juste parce que j'ai le serveur qui tourne sur autre chose.

D'accord.

Le voilà.

Bien.

D'accord.

Vous venez d'avoir un aperçu.

Donc j'avais un serveur qui tournait sur le projet précédent ou le projet que je copie.

Donc ce que vous avez vu là est ce que j'avais construit plus tôt.

D'accord, donc rien ne fonctionne parce que nous n'avons pas de modèle là, bien, on s'y attendait.

Donc si nous allons à admin, qui est la page d'administration intégrée, puis nous nous connectons avec les identifiants utilisateur que nous venons d'ajouter, nous y voilà.

D'accord, donc nous avons les modèles d'authentification, c'est celui que nous venons de créer.

D'accord.

Donc donnez-moi un prénom.

Nous aurions pu le faire dans le terminal.

Mais le voilà.

Donc maintenant, nous avons un email, un prénom, un nom de famille, ce signal devrait avoir produit un profil utilisateur, ce qui est super.

Donc c'est le profil utilisateur maintenant.

D'accord, donc c'est choisir un avatar.

Donc ce que nous ferons, c'est aller dans le bureau de développement, j'irai dans celui avec lequel je jouais plus tôt.

Fichiers multimédias, Avatar, utilisons ce titre est back end.

Développeur bio, c'est juste une bio de démonstration.

Et ce que nous ferons ensuite, c'est que nous ajouterons une compétence.

Donc cela peut être Django.

Et je vais mettre cela, pourquoi pas, mettons 100%, ce n'est pas une compétence clé, c'est mes compétences en codage.

Safe, nous aurons la paix, HTML, nous aurons cela à 95.

Sauvegarder, nous aurons CSS, nous aurons cela à 90.

Sauvegarder.

Et ensuite, ce que nous ferons, nous ajouterons un autre, qui sera Java scripts.

Changeons un peu les choses.

Mais 75 disons, nous avons une compétence clé cette fois.

Donc nous avons une personne, nous l'aurons, cela n'a pas vraiment d'importance sur un nombre, leur compétence clé.

Mais ce que nous ferons, nous ajouterons des fichiers multimédias compétences.

Ouvrir sauvegarder, joueur d'équipe, je veux dire, vous pouvez mettre ce que vous voulez dans le vôtre.

C'est juste moi qui le construis, c'est une compétence clé, sauvegarder.

Et nous aurons.

Donc starter aura cela comme icône de compétence clé.

Tous ceux-ci viennent dans leur modèle, d'ailleurs, toutes ces images, et CV.

Donc si je vais dans cela, ce sont ceux que j'ai ajoutés plus tôt.

Donc le voilà.

Sauvegarder.

Donc ce que je fais, c'est que je construis la page d'administration.

Donc c'est l'avantage d'utiliser Jango.

Bien, donc cette page d'administration intégrée nous permet de créer, donc à tout moment, nous pourrions changer l'avatar, à tout moment, nous pouvons changer la bio, donc j'ajoute à la bio.

Oui, donc si vous la sauvegardez, cela deviendra la nouvelle bio.

Donc vous n'avez pas à, lorsque vous obtenez cela dans un environnement de production, vous n'avez pas à aller dans le code source, nous devons faire changer le backend, c'est l'avantage de faire cela.

D'accord, donc nous avons ajouté, ajoutons un témoignage.

Donc choisissez la vignette MIDI files utilisez celle-là, nom, Bobby, Rôle Manager.

C'est une citation de test.

Maintenant, sauvegardez et ajoutez un autre mot, vous savez quoi, nous allons juste passer rapidement par cela, nom Bobby deux, manager deux et citation deux et je ne ferai pas tous ceux-ci parce que ce serait une perte de votre temps.

Bobby trois, manager trois et citation trois, il y a maintenant trois objets.

Donc ce que nous pouvons faire, nous pouvons le rendre inactif, cela n'apparaîtra pas, vous voyez est actif.

D'accord, donc cela ne sera pas rendu sur le frontend.

Mais gardez cela, gardez cela.

Voyez l'avantage là.

Donc j'ai fait le profil utilisateur, le témoignage, les compétences, ils sont tous là.

C'était lorsque nous les ajoutions ici.

Nous avons dû cliquer sur Ajouter et cela l'ajoute à cette compétence parce que c'est un champ de plusieurs à plusieurs.

D'accord.

Encore une fois, vous pouvez changer ceux-ci à tout moment, changer cela en, vous savez, ou pas dans une clé.

Changer CSS en 292.

Par exemple, sauvegarder cela devient 92 D'accord, fichiers multimédias, ajoutons une de ces images.

Ce que je pensais, c'est juste la vignette d'une autre vidéo que j'ai produite.

Image aléatoire Sauvegarder les profils de contact, nous n'en avons pas besoin, les certificats, nous allons juste en ajouter un, n'est-ce pas ? Donc maintenant, maintenant le nom serait, allons-y, Django avancé, cours Free Code Camp description, c'est un test, cette retune.

Cela suffira, nous n'ajouterons pas trois certificats, vous aurez compris.

Et ensuite, ce que nous devons faire, c'est ajouter un profil de blog.

Donc c'est là que l'éditeur de texte riche entre en jeu.

D'accord.

Donc l'auteur, nous pouvons avoir Bobby stemmen nom, nous pouvons avoir cela comme test blog et avoir description, test this group Gen.

Et ensuite, ce que vous pouvez faire, c'est que vous pouvez avoir, vous pouvez juste avoir un deux, c'est un en-tête, et ce que nous mettons ici est ce qui sera rendu, ce que vous voyez est ce que vous obtenez, bien.

Donc c'est une description aléatoire.

Et ensuite, c'est ce que je voulais vous montrer, le fichier multimédia.

Donc ce gars ouvre un autre navigateur, d'accord, retourne dans les fichiers multimédias, cela nous donne accès à cette URL, d'accord pour obtenir cela, c'est l'URL de l'image que nous venons de sauvegarder dans notre base de données, désolé, dans nos fichiers statiques.

D'accord, si nous allons dans le blog, maintenant, ajoutons une image pour jouer avec cela, parfois cela ne se rendra pas correctement sur le frontend.

Mais si vous jouez avec un éditeur de texte riche, vous pouvez le faire fonctionner.

Donc si nous ajoutons une URL d'image, il suffit de coller l'URL que nous venons d'ajouter là, tout le texte de l'image de test.

Dans le média principal, je vais le déplacer là.

Ce n'est pas correct.

Je veux cela.

Copions cela, voilà.

Bien, largeur, nous aurons ceux-ci, ce sont des liens.

Donc si vous mettez simplement 800, vous pouvez y mettre une bordure si vous voulez.

Nous l'alignerons à gauche.

Il y a tout un tas d'autres choses que vous pouvez faire sur leur lien avancé, donc cliquez sur OK.

D'accord, et ensuite nous choisirons une image, ce sera la vignette de l'image.

Donc vous pouvez choisir la même si vous le souhaitez, est actif, sauvegarder.

Pour les filles, nous ajouterons également un portfolio.

Nous ferons exactement la même chose.

Bien.

Donc maintenant, maintenant le nom est le meilleur, la description est la description de test.

Et ensuite nous aurons un en-tête deux en-têtes.

C'est un, cette option est la fin.

Et entre cela, nous ajouterons une image.

Même chose, pas besoin de trop s'embêter avec, mettre 100, je pense, mettre une bordure dessus.

Nous mettrons quatre cette fois et à gauche.

D'accord, choisissez un fun maintenant.

Jours heureux.

D'accord, je pense que nous avons maintenant toutes les pièces.

Donc cela a pris un peu de bidouillage pour tout faire fonctionner en arrière-plan.

Mais aussi, nous devons maintenant voir, je pourrais vraiment dupliquer ces blogs, le blog, donc nous avons blog deux, blog trois, peu importe, mais ce n'est pas grave, vous pouvez le faire dans votre propre temps.

J'ai juste construit le backend d'une manière que je sais que cela va fonctionner.

Et juste si vous suivez, faites cela, obtenez trois blogs, obtenez trois portfolios, et cela aura l'air fantastique sur le frontend.

Donc c'est le backend, essentiellement fait, ce que nous devons faire maintenant, c'est connecter le frontend.

Donc nous avons les templates ici.

Le répertoire pour le CV est ici.

Donc ce que nous devons faire, c'est que nous avons besoin de nos fichiers statiques.

Donc nous les prendrons, nous les copierons et nous les déposerons dans ceci est notre, ceci est le projet d'ailleurs.

Donc nouveau dossier, nous appellerons cela static et nous les collerons simplement là.

D'accord.

Donc ce sont tous les fichiers statiques dont nous avons besoin.

Retour dans le CV et nous voulons ensuite tous ceux-ci, gardez votre doigt sur control.

Sélectionnez-les simplement tous.

Vous n'avez pas besoin de licence, lisez-moi, copiez-les.

Je veux les ajouter à Main templates main, je vais coller.

D'accord, bien que tous les templates, nous devons maintenant les connecter.

D'accord ? Si je viens d'en ouvrir un maintenant, cela va avoir l'air terrible, bien ? D'accord, parce que cela ne sait tout simplement pas ce que sont les fichiers statiques, cela ne sait tout simplement pas ce qui se passe.

D'accord, parce qu'ils sont maintenant dans un projet Django.

Si je les ouvrais dans l'original, cela fonctionnerait, parce que c'est simplement la façon dont cela est connecté.

D'accord.

Donc nous n'en avons pas besoin.

Fermons cela.

Fermons cela.

Il y a, fermons cela.

Retour dans Visual Studio.

Bien.

Donc ce sont maintenant les templates que nous avons mis ensemble.

Nous apporterons notre terme, nous n'avons pas besoin de voir le terme, vous savez quoi ? Je vais le fermer pour l'instant.

Nous n'en avons pas besoin.

Donc c'est le fichier index.

D'accord.

Donc c'est un fichier HTML standard.

D'accord, vous avez head, vous avez body.

Et dans ce body, vous avez une navigation.

Donc nous avons nous avons essayé d'être aussi détaillés que possible, ou aussi utiles que possible sur la documentation de ces fichiers HTML.

Donc c'est la barre de navigation.

C'est le contenu de cette page particulière.

Il y a beaucoup de sections un peu plus bas, en fait, je vais les cacher, ce sera beaucoup plus facile, un peu plus bas, nous avons ensuite le pied de page.

D'accord.

Et ensuite nous avons les scripts, ce sont les scripts du corps, ce sont les scripts ici.

D'accord, rien ne va fonctionner parce qu'il référence des fichiers que Django ne sait tout simplement pas où les trouver.

Donc si j'allais rendre cette page index, donc en fait, allez-y et faites-le.

Donc nouveau terminal, travail sur resume demo, Python manage.py, run server.

Et ce que je vais faire, c'est que je vais simplement ouvrir ce navigateur, bien, donc c'est la page d'accueil, bien ? Donc il a trouvé le index dot HTML, comme le prévoient les vues, il a trouvé le template base, il a juste l'air terrible, parce qu'il ne sait pas ce qu'est un CSS, il ne sait pas ce qu'est un JavaScript.

Et tous les liens sont tous écrasés.

Donc nous devons charger les fichiers statiques.

Et nous devons connecter tout cela.

Donc c'est ce que nous allons faire.

Et la façon de faire cela est que nous avons besoin d'un base html.

Donc nous allons sauvegarder index comme base dot HTML.

Et ce que nous devons faire ensuite, c'est créer un autre répertoire dans Maine.

Nous appellerons cela partials.

Et dans celui-ci, nous aurons besoin d'un nouveau fichier appelé messages dot HTML.

Nous en avons besoin d'un autre ici appelé nav dot HTML.

Ce sera l'élément de navigation.

Fichier, et nous appellerons cela butter HTML.

D'accord.

Donc ce que nous devons faire, c'est que vous devez dissecter ce HTML, afin que nous puissions ensuite utiliser des balises de modèle.

Donc Django dispose d'une gamme de balises de modèle qui vous permettent d'inclure facilement d'autres parties de HTML, ce que vous devez faire est simplement de référencer le chemin.

Donc nous allons de l'avant et faire cela.

Donc tout en haut de la page, ouvrez mes autres projets qui vont à mon base html, ce que vous devez faire, et vous devez écouter, la plupart d'entre eux en fait, c'est de charger le statique.

D'accord, donc cette balise de modèle nous permet d'accéder aux fichiers statiques, qui sont tous les fichiers qui sont maintenant dans ce répertoire, hit OK, le CSS images, JavaScript, d'accord.

Nous descendons ensuite, nous descendons tout le chemin du haut ici.

Donc nous avons l'auteur, qui avait décodé et James Granger design, nous avons ensuite le canonique, que nous devons ajouter le processeur de contexte, si vous vous souvenez dans settings dot P, pourquoi est-ce que nous avons ajouté le processeur de contact ici, mais si vous voyez ici, vous avez toujours accès à la demande.

D'accord.

Donc c'est ce dont nous avons besoin de nous emparer ici.

Donc c'est request dot path.

D'accord, donc c'est ce que vous ajoutez dans le canonique.

En fait, je vais simplement copier cela pour me éviter de m'amuser.

Nous avons ensuite un lien qui est la maison.

Et ensuite ce que nous allons faire, c'est utiliser une URL technique temporaire.

Donc la relation maison, c'est main.

Donc c'est l'application main, et elle est appelée maison, qui est notre page d'index.

Nous avons ensuite dans la description lorsque ces balises SEO sont vraiment dans la tête du fichier HTML, c'est ainsi que je les gère toujours.

J'ajoute un bloc, une balise de modèle et je l'appelle description.

Et cela me permet d'avoir une description d'une page HTML dans l'actualité.

Je vous montrerai ce que je veux dire dans une seconde.

Et ensuite j'en ai un autre pour les mots-clés.

Nous avons l'icône, cette petite icône apparaît en haut du navigateur web.

Et cela essaie de trouver des images.

Mais il ne peut pas trouver d'images parce que les images, où est le chemin que nous devons référencer le fichier statique.

Donc ce que nous ferons, nous lierons cela, nous l'avons donc nous utilisons la balise de modèle statique, nous chargeons le statique en haut ici.

Et ensuite nous référençons le statique ici.

Donc maintenant nous cherchons dans un répertoire statique, dans un répertoire appelé images.

Et nous cherchons icon dot jpg.

Maintenant, dans le statique, nous n'avons pas nous avons des images, d'accord, donc nous cherchons icon, qui est icon.

jpg.

D'accord, donc nous cherchons cela.

C'est ce que nous cherchons.

Jours heureux, et nous avons le statique.

Donc encore une fois, nous cherchons CSS, nous n'avons pas le chemin.

Donc nous devons référencer le statique, encore une fois, avec style css.

Donc ce que nous ferons, c'est que nous ajouterons tous ceux-ci, d'accord.

Et j'ai toujours une balise de modèle de bloc ici.

Et je l'appelle toujours étendre l'en-tête.

Cela nous permet d'utiliser du CSS spécifique à une certaine page dans ce modèle, plutôt que de l'avoir chargé sur chaque page.

C'est très, très pratique de faire cela.

D'accord, nous avons ensuite le corps.

D'accord, donc ce que nous allons faire ici, c'est que je vais copier cela.

Et je vais supprimer l'élément d'en-tête.

Et donc évidemment, celui-ci va faire, bien, d'accord, donc c'est l'en-tête, l'en-tête reste le même sur toutes ces pages.

Ce n'est pas comme si nous avions un, si une page est active, alors elle est mise en évidence.

Nous ne faisons pas cela dans ce modèle.

Donc vous n'avez pas à vous en soucier.

Donc tout cela ici peut être coupé, et peut être fait, déversé dans nav dot HTML.

Donc d'abord, nous aurons load static.

Et ensuite nous déverserons toute cette navigation ici.

D'accord.

Et ensuite dans le base html, ce que nous devons faire, c'est l'inclure, donc utiliser une autre balise HTML, celles-ci incluent, donc nous incluons maintenant main.

Donc c'est l'application main, partial.

Donc le répertoire main, partials nav dot HTML.

Donc nous n'avons pas besoin de tout ce HTML là, CS nous répétons, nous devons également ajouter du code, qui n'est pas dans le modèle, et je crois dans une seconde.

Maintenant est ici, bien ? D'accord.

Donc il y a une balise de modèle IF comme une annonce ici.

Donc c'est juste un peu de code que j'utilise occasionnellement.

Donc si les messages sont rendus au document HTML, donc pour les messages de messagerie, donc si c'est un dictionnaire ou une liste de messages, donc pour chaque message, il rendra un script.

Donc c'est du JavaScript, donc votre script sera une alerte.

Donc cela apparaîtra avec une petite alerte en haut de l'écran avec le message réel.

Dans ce cas, ce sera merci de nous avoir contactés, nous vous recontacterons bientôt.

Donc c'est notre messages, HTML pour revenir dans une base, nous pouvons alors importer ou inclure les messages dans le corps, donc ils apparaissent toujours dans le HTML, puis nous devons faire de même pour tout le contenu et tout le pied de page.

Donc nous revenons à l'état du pied de page, désolé, l'élément du pied de page, nous allons le couper, nous allons le déverser dans le pied de page.

Encore une fois, chargez le statique, n'oubliez pas de le faire.

Parce que vous rencontrerez une erreur.

Et nous allons juste nettoyer un peu, tout ramener.

Oh, le voilà.

Sauvegarder.

Et la base, nous inclurons alors cela, copions cela, c'est le pied de page.

Et ensuite avec le contenu, ce que nous allons faire, c'est que nous allons avoir un bloc.

Donc nous aurons block content.

Et ensuite nous aurons et block.

D'accord, donc c'est important, bien que ce petit bloc là soit ce que nous allons utiliser lorsque nous rendrons le index html.

Donc dans le index html, il contiendra tout ce HTML, le contenu essentiellement, et nous utiliserons une balise de modèle différente dans index pour étendre la base, donc index sera alors une combinaison de ce HTML et du base html.

D'accord, donc nous allons le couper, nous allons mettre en surbrillance le index.

Donc nous allons mettre en surbrillance le index, nous allons tout coller.

Et nous allons le ramener pour le nettoyer un peu.

Le voilà.

D'accord, donc maintenant en haut de cette page, nous aurons besoin d'un tas de choses, que je vais vous montrer ce que nous allons faire ici, copier.

Et nous allons le coller.

Et je vais vous guider pour faire la section.

Un, je veux en bas, juste fermer le bloc.

Et block, sauvegarder, et je vais juste aller du haut, bien.

D'accord, donc nous étendons main base, d'accord, donc lorsque nous rendons la page d'accueil, nous cherchons index html.

Et nous insérons toutes les informations de ce HTML dans les blocs que nous indiquons.

D'accord.

Donc tout ce qui est dans un bloc de contenu sera injecté, nous avons injecté dans ce bloc.

C'est ainsi que cela fonctionne.

D'accord, donc nous allons sauvegarder cela.

En fait, avant de continuer, vérifions simplement ceux-ci, souvenez-vous, il cherche JavaScript.

Ces fichiers JavaScript sont dans un répertoire statique, donc nous allons ajouter le chemin statique.

Donc celui-ci devient static J, s, static J.

S, et ensuite nous ajoutons un pied de page.

Encore une fois, il nous permet d'ajouter JavaScript à certains fichiers HTML que nous ne voulons pas nécessairement charger dans l'ensemble du modèle.

D'accord, dans l'ensemble du modèle, devrais-je dire ? Donc ce bloc de contenu est ce qui sera rendu dans ce bloc ? D'accord.

Ce bloc de titre est ce qui sera rendu dans ? Où est-il ? Ne voit pas le bois pour les arbres ? Comment ai-je même ajouté cela ? Une seconde.

Je n'ai peut-être pas fait.

Je m'excuse.

Donc le titre sera bloqué.

D'accord.

Donc le titre ici, tout ce que nous mettons ici, que nous pourrions mettre did coding dash home, cela sera rendu dans ce bloc là, d'accord, la description qui sera rendue dans ce bloc, et ainsi de suite.

CSS, si nous avions un fichier CSS spécial que nous voulons sur cette page particulière, nous l'ajouterions ici.

Nous voulons JavaScript, nous l'ajouterions là.

Le contenu l'aurait ici.

D'accord.

Tous les contenus ne veulent pas cela.

D'accord, sauvegarder.

Maintenant, la dernière chose que nous devons faire est de changer toutes les images que cela référence, d'accord, donc cela cherche toutes les images ici.

Donc ce que nous allons faire, c'est Ctrl H.

Et ce que nous devons faire, c'est static images slash ce qui fera cela, cela remplacera partout où il trouve des guillemets, des images, une barre oblique, cela remplacera par ce code ici, qui est ce que nous voulons, ce sont neuf occurrences.

Et ensuite avec une partie jpg dot jpg, nous allons simplement faire dot jpg.

Nous faisons cela.

D'accord.

Donc où nous avons juste nous voulons simplement tout remplacer.

Sauvegarder, et je pense que nous avons aussi un SVG.

Oui, le voilà.

SVG s aussi.

Dot SVG et play.

Donc maintenant si nous sauvegardons cela, je pense que c'est tout, je pense.

Donc nous devons faire pour cette page d'index.

Maintenant, nous ne passerons pas en revue chaque page.

Donc ce que nous faisons pour les indices est exactement ce que nous devons faire pour chaque page.

D'accord.

Donc contact, par exemple, et je vous montrerai ce que je veux dire sur contact, et je ne ferai pas tous les autres, parce que vous pouvez le faire vous-même.

Je vais simplement copier ce code de mon autre écran.

Mais je vous montrerai quoi faire avec contact dans une seconde.

Mais si maintenant cela ressemble à ce que le serveur est toujours en cours d'exécution.

Donc nous mettons maintenant cela à jour.

Cela devrait.

Le voilà.

Il cherche le logo, il ne peut pas le trouver parce que nous n'avons pas changé ou nous n'avons pas mis à jour les images dans assez.

Et c'est probablement la même chose en bas ici.

Nous ne l'avons pas fait dans le pied de page non plus.

Mais tout le reste que nous rendons, d'accord, d'accord.

Il a dit qu'il n'y a pas de liens vers le backend pour l'instant, que nous ferons cela dans une seconde.

Donc le pied de page, je ne l'entourerai pas avec le pied de page.

Je vais littéralement juste faire une copie.

Coller.

D'accord, donc ce que j'ai fait, c'est maintenant le pied de page.

Donc j'ai changé tous les liens en statique et je vois que static images.

Ensuite en bas ici, plutôt que de dire 2001, j'ai utilisé une autre balise de modèle appelée net, donc cela aura toujours l'année la plus récente.

Donc si lorsque nous atteignons le premier janvier 2022, il montrera simplement 2022 plutôt que 21.

D'accord, sauvegarder cela, nav fera exactement la même chose, je vais faire une copie.

Encore une fois, vous aurez accès à ce projet depuis GitHub, donc ne vous inquiétez pas trop, vous aurez accès à tout ce code.

Ou un, je n'ai pas changé cela, cet index dot HTML doit en fait changer pour URL main home, sinon, ce lien ne fonctionnera pas.

Mais il cherche le logo, qui est dans le répertoire statique.

Et il ajoute un lien URL à tout cela.

Donc le lien d'accueil en haut de la page, et je serai main home portfolio sera portfolios, blogs, et contact.

Donc tous ces liens fonctionneront maintenant.

Retour dans le navigateur, mettez à jour, cela fonctionne maintenant, si vous cliquez dessus, cela vous ramènera à la maison.

Si vous cliquez sur contact, cela vous emmènera à la page de contact, qui est magnifique.

Donc corrigeons cela rapidement.

Bien que la page d'accueil fonctionne, mais nous faisons exactement la même chose que ce que nous venons de faire sur la page d'index.

D'accord, donc tout cela est exactement la même chose, nous n'avons pas besoin du No Contact page, bien ? Le CSS ne peut pas le trouver, nous devons changer tout cela.

Mais pour me faire gagner du temps, encore une fois, tout ce dont j'ai vraiment besoin, c'est de la section de contexte, bien ? Section de contenu.

Je n'ai pas besoin de n'importe lequel des pieds de page ou autre chose, tout ce dont j'ai besoin, c'est le contenu.

Et si je vais à l'index, et si je copie simplement tout d'ici, allez dans contact et déposez-le ici.

Cela devrait, je n'ai pas besoin de cela.

Cela peut tout revenir un peu comme pour être bien et rangé.

Encore une fois, exactement la même chose que l'index, nous étendons le base html, nous chargeons le statique, et ensuite nous pouvons changer tout cela.

Mais encore une fois, c'est pourquoi j'aime les balises de modèle de bloc.

Donc nous pouvons ajouter ce que nous voulons ici.

Et ce sera le nouveau titre de cette page particulière.

D'accord, CSS scripts.

Et cette section ici, bien, donc concentrons-nous un peu sur cela, parce que c'est assez important.

Donc contactez-nous ci-dessous.

C'est le formulaire que nous avons actuellement.

D'accord, mais nous devons en faire un format Jango.

Donc ce que nous devons faire, c'est ajouter une méthode égale, c'est un post.

Et l'action est l'URL que nous voulons référencer.

Donc c'est contact.

Donc la raison pour laquelle nous mettons cela est parce que dans nos URLs, c'est une URL, donc c'est contact, d'accord, ensuite nous devons utiliser parce que c'est un post, pas une requête get ou autre chose, nous avons besoin ici d'un jeton CSRF, cela ajoutera un élément caché avec un jeton CSRF, qui fonctionnera ensuite, puis, au lieu de ces entrées, ce dont nous avons besoin, c'est simplement de copier la base, puis de référencer le nom.

Donc si je prends ceux-ci, si je les dépose ici.

D'accord, donc plutôt que d'être des entrées, nous rendons maintenant le formulaire.

Maintenant, le formulaire est contact form.

C'est ce que nous avons produit là dans ce forms dot P, pourquoi je suis en train d'importer le champ Name, le champ email, le champ message, nous devons changer cela en message.

Désolé, c'est une erreur de ma part.

C'est ça.

Donc nous devons faire, mais nous devons fermer le bloc, n'oubliez pas de le faire car il y aura une erreur.

Et verrouiller.

C'est le formulaire de contact terminé.

D'accord.

N'avez pas besoin de faire cela.

Tout ce que nous devons faire, c'est simplement double vérifier cela.

Le voilà.

D'accord, donc techniquement, maintenant, si j'allais mettre Bobby stemmen Bobby à the coding.com.

Message, c'est un message de test.

Maintenant, cliquez sur Soumettre, espérons.

Merci.

Nous serons en contact bientôt.

D'accord.

Cela fonctionne.

Si nous allons dans la base de données, allons dans les profils de contact.

Le voilà.

D'accord, c'est très, très utile.

Cela signifie simplement que vous et c'est une autre raison pour laquelle nous utilisons Django, tout employeur, toute personne qui veut vous contacter en utilisant votre formulaire de contact, vous avez un enregistrement de l'horodatage et de qui c'était, quel était le message dans la base de données.

D'accord, fantastique.

Donc retournons dans nos projets.

Nous avons fait index avec OnContact.

Maintenant, concentrons-nous, allons sur le portfolio.

Même chose, n'avez pas besoin de tout ce fatras au-dessus du contenu.

En fait, tout ce dont nous avons besoin, c'est de tout cela, copiez le portfolio, collez-le là, nous fermerons le bloc en bas de la page.

Et nous trouverons le bas de la section de contenu, les scripts, c'est cela, non, c'est le pied de page, ne vous y référez pas.

Et bloc, sauvegarder.

D'accord, donc nous ramenons maintenant cela un peu.

Et cela n'a pas vraiment d'importance.

C'est tout bon.

La seule chose, c'est que nous avons quelques images utilisées ici.

Mais je ne vais pas changer toutes celles-ci.

Ce n'est pas un problème.

Et nous ne connectons pas cela au backend pour l'instant.

Donc je fais simplement les templates comme ils sont.

Donc c'est ce que vous feriez pour chacun d'eux.

Mais ne vous laissez pas trop emporter, car vous devez ajouter quelques balises de modèle Django, comme des boucles for afin que nous puissions réellement rendre des informations réelles.

Donc nous allons faire cela.

Mais je ne vais pas faire le détail pour celui-ci et les blogs ou faire cela à la toute fin, je vais simplement copier et coller et vous guider à travers.

Mais concentrons-nous sur la page d'index.

Donc à la minute, nous avons cela ici.

Donc nous avons changé cette image.

Donc oui, il a montré une photo de moi.

Mais c'est parce que cette image est dans les fichiers statiques, ce que nous devons faire, c'est que nous voulons référencer l'avatar que nous avons sauvegardé contre le profil utilisateur.

Et comment vous faites cela, c'est que vous n'avez pas besoin de référencer le statique, maintenant, vous devez simplement utiliser me, qui est dans le contexte.

Le processeur de contexte dit me, d'accord.

Mais comme les profils utilisateurs, donc nous avons maintenant vu le modèle utilisateur.

Donc nous avons maintenant le profil utilisateur, point avatar, qui est le champ, et ensuite vous voulez l'URL de cela, sauvegarder.

Si nous allons maintenant dans la page d'accueil, ici, allez à la maison, cela montrera toujours juste maintenant ce qu'il fait, nous allons inspecter, il capte maintenant le media avatar.

Donc c'est l'image réelle que nous avons sauvegardée contre le profil plutôt que le fichier est dans un fichier statique, ce qui est exactement ce que nous voulons.

Donc je peux maintenant changer cela dans le profil utilisateur pour une autre image.

Choisissez un fichier.

Et vous savez quoi, je vais simplement le mettre là.

Et sauvegarder le fichier, allez-y.

Le voilà.

Ce n'est pas idéal, mais cela vous donne une idée de ce que nous faisons ici.

Donc choisissez un fichier, allez-y dans l'avatar, chassez cela et sauvegardez à nouveau, Bob est votre oncle, le voilà.

Jours heureux.

Donc ce que nous devons faire ensuite, c'est que nous devons connecter tout cela, tout cela, le fichier CSV ici.

Et c'est ce que nous allons faire maintenant.

D'accord, donc salut, je suis, vous pouvez aller me, points.

Prénom, parce que c'est le profil utilisateur.

Et ensuite vous pouvez utiliser un filtre appelé titre.

Maintenant, si je mets Bobby tout en minuscules dans le backend dans la base de données, cela rendrait une lettre majuscule suivie de minuscules, ce que ce serait, je pense que c'est le titre.

Me dots, user profile, dot title, je pense que je ne vais pas passer par tous ces B parce que vous aurez compris.

Bien.

Donc ce sera mi dot user profile dot bio.

Donc si nous allons maintenant ici, et cliquons sur Mettre à jour, ils l'ont.

Donc Salut, je suis Bobby, un développeur backend.

C'est juste une bio de démonstration, retour dans la base de données, retour dans la bio, point point point point point point, geek plus entrer, ou sauvegarder.

Et mettre à jour.

Le voilà.

C'est ainsi que cela fonctionne, c'est vraiment très pratique.

Donc si nous allons ensuite dans le bouton, donc télécharger, donc ce dont nous avons besoin ici, c'est que nous voulons lier au fichier CSV, qui est lié à notre profil utilisateur.

Donc ce sera me dot user profile.cv dot URL.

Nat devrait maintenant, parce qu'il a un attribut de téléchargement, si je clique dessus, il téléchargera alors mon CSV.

Désolé, vous l'ouvrez et c'est le CV que j'ai sur ce profil.

D'accord, ce qui est vraiment pratique.

Contact, cela dit actuellement contact HTML, nous voulons que ce soit un, j'espère que vous comprenez ce que je fais ici, je passe simplement en revue, et j'ajoute des balises de modèle Django pour nous permettre de changer cela de manière programmatique et de rendre les informations d'une base de données, ce qui est vraiment bien.

Vraiment pratique.

Donc c'est le contact.

Maintenant, ce lien, je l'enregistre au fur et à mesure, ce lien nous emmènera maintenant à la page de contact.

D'accord, et ensuite ce que nous ferons, nous ferons cela rapidement, et ensuite je le copierai de mon autre écran, parce que cela prendra trop de temps.

Donc nous irons dans Oui, nous faisons cela.

En fait, je vais le copier, vous savez quoi, je vais le copier et vous guider à travers ce que j'ai fait.

Donc loin, je prends tout de mon index.

Maintenant, je vais dans ici, je vais tout de là.

Donc tout ce travail que je viens de faire, je vais simplement le copier et le coller de toute façon, parce que c'est déjà fait sur l'autre écran.

D'accord, donc vous savez quoi ? Laissez-moi revenir rapidement.

Avant de faire cela, parce que je veux vous montrer ce que nous remplaçons réellement.

Donc dans cette section, il y a cela, cette section certificats, bien.

Donc c'est un curseur.

Donc c'est un curseur extérieur.

Et ensuite nous avons un curseur de certificat classique qui a été référencé dans le JavaScript, c'est ce qui permet au JavaScript de déplacer ces curseurs, bien.

Donc c'est ce que nous regardons.

Nous avons ensuite le Swiper slide.

D'accord, donc ce sont les éléments.

Donc c'est un certificat, c'est deux, un s3, d'accord ? Eh bien, je ne veux pas de ces trois.

Je veux ceux qui sont dans la base de données, d'accord, donc je ne veux pas d'eux du tout, mais je veux cela, mais plutôt que de montrer ce qui se passe ici, je veux qu'il rende ce qui est dans la base de données.

Donc pour faire cela, nous utiliserions une boucle for ou voir dans dit, Tiff IR cuts, les voilà, à tiff cuts.

Et ensuite nous voulons si si c.is active alors rendre cela, si non, ne rien rendre, bien.

Donc nous allons ensuite fermer le F et le F et le M, fermer le for et le for, d'accord, donc c'est maintenant une boucle for, bien ? Mais ce qui est rendu est chargé, obligez.

Donc ce que nous avons gagné, c'est qu'il n'y a pas de lien pour les certificats, mais vous pourriez, si c'était un blog, vous mettriez la balise de modèle URL.

Donc nous voulons que cela soit C dots, vérifiez simplement le champ.

Les certificats, je pense, sont la bombe ici, le certificat, donc cela pourrait être le titre, ce serait le titre.

Cela serait C dot date dot date, voir dot ? Qu'est-ce que cela va être ? J'avais besoin de nommer le titre, d'accord, c'est le titre, ce serait dans ce cas pour mon exemple, ce serait Free Code Camp.

Et ensuite vous avez cela serait la description.

C dot description.

D'accord, sauvegarder.

Donc maintenant, plutôt que de rendre du charabia, cela rend réellement quelque chose du backend, les certificats.

La raison pour laquelle j'y accède est parce que c'est dans le contexte.

Je l'ai ajouté dans le contexte dans les vues, d'accord, donc si vous allez ici, c'est à quoi j'accède.

D'accord.

Donc ce sont tous les certificats actifs.

Retour dans l'index et sauvegardez cela, j'espère ne pas avoir tout gâché.

Non, au revoir.

Donc cela montre maintenant un d'accord, parce que nous n'en avons qu'un dans la base de données.

Mais si je vais aux certificats et que je clique sur inactif, sauvegardez cela, cela ne rendra rien.

Oui.

Donc vous voyez ce que j'essaie de faire ici ? C'est bien que cela, donc à chaque actualisation, c'est fait, d'accord, donc je ne vais pas passer en revue et faire tout le reste parce que vous pouvez voir ce que nous essayons d'accomplir, vous devez ajouter des boucles for et des balises de modèle if pour rendre les bonnes informations contre ce modèle, d'accord, donc nous allons faire cela et je vais ajouter ce contenu ici.

Coller, sauvegarder, et ensuite le rendre.

Et blog, il faut finir les blocs, ne voulez pas finir les blocs, sauvegarder, revenir.

J'ai dû avoir le bloc de contenu aussi.

D'accord, c'est toujours amusant.

Désolé, je me dépêche.

J'essaie de, le voilà.

Effaçons celui-là, sauvegardons cela, cela devrait maintenant fonctionner.

Le voilà.

Bien.

Donc cela est maintenant tout rendu depuis le backend.

Donc nous allons sauvegarder le certificat, si nous allons changer le HTML en 98.

Sauvegardez cela, mettez à jour 98%.

D'accord.

Et ces leads vont aussi changer.

Donc si je change cela en 50%, vous verrez probablement ce que je veux dire, en fait.

Donc je vais à 50.

Sauvegardez.

Le voilà.

D'accord.

Les joueurs d'équipe, les autodémarreurs regardent différentes images, les certificats.

Nous en avons un dans la base de données, les travaux en vedette, j'ai un témoignages, ou nous avons mis trois là, si vous vous souvenez.

Mais si nous devions en rendre un inactif, par exemple, sauvegardez cela.

Et mettez à jour.

Le voilà.

Nous n'en avons que deux.

D'accord, test blog.

D'accord.

Et si vous deviez cliquer sur Voir tout, ce qu'il fera ensuite, c'est qu'il vous emmènera à la page du blog, mais nous ne l'avons pas encore fait.

D'accord, donc je vais rapidement ajouter tous ces détails de blog.

Donc copiez pour Ghana blog details.

Coller.

Donc ce que nous faisons ici, blog dt, en fait, et nous ferons un blog.

Copiez, et nous irons au blog, juste une page de liste de blog normale.

Sauvegardez, si nous allons et rendons cela maintenant, cela devrait avoir l'air bien.

Le voilà.

D'accord, donc cela rend mon seul blog que j'ai.

Donc c'est une list view, si j'ajoutais un autre blog, il apparaîtrait là, cela a l'air vraiment, vraiment bien.

Donc si je clique sur cela, cela ouvrira la vue des détails du blog.

D'accord, et bien, d'accord, cela n'a pas rendu cela trop bien.

Donc quand je dis que vous devez jouer avec le CKEditor, parce que pour une raison quelconque, il rend certaines des informations incorrectement.

Mais c'est bien.

Vous savez, c'est juste jouer avec les informations là.

Donc nous allons dans les blogs, le profil du blog.

Pourquoi y a-t-il, je me demande à quoi cela ressemble, cela pourrait aider.

C'est la fin, bien, vous pouvez voir ce que j'ai fait.

Maintenant, j'ai juste ajouté quelques morceaux, c'est parce que l'image est probablement trop petite pour l'écran.

Si j'allais la rendre un peu plus grande.

Retour là, modifiez les propriétés de l'image, changez cela en 1000, voyons.

D'accord, sauvegardez.

Le voilà, commence à faire quelque chose de différent maintenant.

D'accord, donc allez jouer avec, ce que vous voyez est ce que vous obtenez avec un éditeur de texte riche, mais cela vous permet simplement de concevoir un blog différent.

Donc tous vos blogs n'ont pas besoin de se ressembler.

Mais vous pouvez utiliser le même modèle, ce qui est génial et un très bon avantage d'utiliser Django ici.

Donc si j'ouvre maintenant cela, tout ce que nous avons fait dans la page de détails du blog.

Nous avons Yeti object dot name, author.

Donc cela a toujours été tiré du backend.

Mais c'est ce qui est important.

D'accord, donc l'objet du corps, si j'allais enlever safe, tout ce qu'il rend est du HTML brut.

Comme cela.

Donc c'est le HTML que l'éditeur de texte riche crée.

Mais parce que nous utilisons le filtre de modèle safe, il rend réellement le HTML en quelque chose de tangible que nous pouvons réellement voir et qui est bien rendu sur le frontend.

Donc si je change cela maintenant en safe, sauvegardez, le voilà.

Et juste pour rigoler, je vais changer la page de détails, copiez celle-ci, où est-elle ? La voilà.

Sauvegardez le portfolio, copiez et sauvegardez le portfolio, donc si je vais maintenant ici et que je vais dans Portfolio, le voilà et que je clique sur les données du portfolio.

Souvenez-vous, c'est bien encore.

C'est parce que l'image que nous avons dans le portfolio, changeons les propriétés de cette image.

Donc mettons cela à 1000.

Et maintenant, cela fonctionnera probablement maintenant.

Le voilà.

Encore une fois, bricoler encore.

Mais alors regardez, si nous devions marquer cela comme actif dans votre portfolio, cela ne fonctionnera pas.

D'accord ? Pour être honnête, cela pourrait encore fonctionner.

Oui.

Vous pourriez également mettre dans la vue que si cela, si la queer, donc si l'objet est marqué comme inactif, alors vous pouvez faire un rendu de redirection, donc vous pouvez rediriger vers la liste des portfolios.

Donc cela ne montrera jamais une URL, mais je ne l'ai pas fait dans cette instance.

Donc c'est tout.

C'est le modèle terminé.

Donc nous avons maintenant un CV numérisé.

Cela est entièrement.

Cela est entièrement fait en Django.

Et nous pouvons changer chaque élément clé de ce CV sans avoir à changer aucun des éléments principaux, aucun du code en arrière-plan.

Donc c'est brillant.

C'est plus ou moins la fin de cela.

Je vais simplement faire un récapitulatif, bien ? Donc ce que nous avons fait ? Nous venons de numériser un CV, bien.

Donc nous avons construit un projet entier en Django, nous avons numérisé notre Word ou PDF, CS, CV ou resume, et nous l'avons mis en ligne.

Donc vous feriez ce site web, vous le mettriez en production, et ensuite vous pourriez envoyer ce lien à un employeur, cela vous aidera à vous démarquer dans la foule.

Et la bonne chose, c'est que parce que nous avons utilisé Django, nous sommes capables d'utiliser la page d'administration intégrée et nous sommes capables de créer, lire, mettre à jour et supprimer tous les éléments du CV, donc vous n'avez jamais à changer le code source.

Maintenant, cela, c'est fantastique, bien ? Donc laissez-moi le changer pour que vous puissiez réellement me voir à nouveau.

D'accord, donc cela, c'est vraiment, vraiment bien.

J'ai vraiment apprécié préparer cette vidéo.

Encore une fois, mon nom est Bobby Stearman, et je suis de did coding.

Veuillez vous abonner à ma chaîne.

Je fais des vidéos comme celle-ci tout le temps.

Avant de terminer la vidéo, je voudrais simplement dire merci à mon collègue, James Granger, qui m'a aidé à mettre ce modèle ensemble, il l'a conçu et sans lui, nous ne pourrions pas le donner gratuitement.

Encore une fois, il peut être trouvé sur mon GitHub, qui est github.com/bobby-decoding/decoding_resume_template, merci beaucoup d'avoir regardé, j'ai apprécié le créer, j'espère.

C'est utile, et je vous verrai dans la prochaine vidéo.

Merci.

Au revoir.