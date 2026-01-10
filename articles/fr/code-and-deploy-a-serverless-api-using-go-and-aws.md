---
title: Coder et déployer une API Serverless avec Go et AWS
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-02-01T22:24:50.000Z'
originalURL: https://freecodecamp.org/news/code-and-deploy-a-serverless-api-using-go-and-aws
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/maxresdefault.jpeg
tags:
- name: serverless
  slug: serverless
- name: youtube
  slug: youtube
seo_title: Coder et déployer une API Serverless avec Go et AWS
seo_desc: 'Creating a serverless API can often be a better choice than coding a backend
  in Node.js, Laravel, Spring Boot, or some other backend framework.

  We just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to code and dep...'
---

Créer une API serverless peut souvent être un meilleur choix que de coder un backend en Node.js, Laravel, Spring Boot ou un autre framework backend.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à coder et déployer une API serverless en utilisant Go et AWS.

Vous apprendrez à créer une pile serverless AWS complète en utilisant le langage de programmation Go. Ce cours couvre à la fois le codage et le déploiement d'une pile serverless simple en utilisant API Gateway, Lambda et DynamoDB.

Voici les sections de ce cours :

* Installation du projet
* Fichier principal
* Reste du code
* Tests
* Déploiement

Regardez le cours complet ci-dessous ou [sur la chaîne YouTube freeCodeCamp.org](https://youtu.be/zHcef4eHOc8) (2 heures de visionnage).

%[https://youtu.be/zHcef4eHOc8]

## Transcription

(générée automatiquement)

Le langage de programmation Go peut être utilisé pour déployer des piles serverless sur AWS dans ce cours.

Akhil Sharma vous apprendra à coder et déployer une pile serverless complète avec des fonctions CRUD de base sur AWS en utilisant Go.

C'est une pile serverless complète.

Exact, donc vous utilisez DynamoDB serverless, vous utilisez Lambda serverless à nouveau, et ensuite nous utiliserons API Gateway, serverless.

Maintenant, API Gateway nous aide à permettre à n'importe qui dans le monde d'interagir avec notre fonction lambda, n'est-ce pas.

Donc nous allons déployer ces trois choses.

À partir de la console AWS, n'est-ce pas, nous allons utiliser la console AWS, puis nous ferons les paramètres pour ces trois choses.

Et nous allons déployer tout cela.

Et n'importe qui dans le monde peut utiliser notre fonction lambda.

Donc c'est plus comme un scénario du monde réel.

Donc je suis dans un terminal maintenant.

Et vous n'avez pas vraiment besoin de garder ce projet dans votre route Go.

Parce que c'est Golang.

Un point 12.

Et de toute façon, ils avaient, vous savez, go mod dedans, que nous allons faire de toute façon, ici, go modern, il s'occupe de tout.

Je veux dire, vous n'avez pas vraiment besoin de faire quoi que ce soit manuellement.

D'accord.

Donc ici, nous allons dire, nous allons créer un répertoire d'abord, nous allons dire, Go server less, et YT.

D'accord, et nous allons cd dedans.

Go serverless tack YT.

Pour yt est essentiellement YouTube, je fais ce projet pour YouTube spécifiquement.

D'accord, et ici, je vais dire go mod dedans.

Et qui est essentiellement github.com/akil/go server less.

Donc c'est mon projet.

Il a initialisé go mod pour moi, go mod est essentiellement comme mon fichier package json.

Si vous venez d'un arrière-plan Java, il aura toutes mes dépendances pour moi, vous savez, facilement listées.

Donc maintenant, ce que je peux faire, c'est simplement ouvrir ce projet, et l'éditeur de code, qui est VS code, dans mon cas, juste comme un pointeur, n'est-ce pas, j'utilise windows à l'intérieur de Windows, j'ai quelque chose appelé WsL.

À l'intérieur, j'utilise Ubuntu 20.04.

Et j'utilise différentes versions de open pour écrire Stan pour cette vidéo particulière, j'utilise over in 20.04.

Et dans mon open 20.0.

Par exemple, j'ai VS code configuré.

D'accord.

Maintenant, je ne veux pas installer beaucoup d'extensions pour appeler parce que je sais que quand je vais commencer à taper, je vais commencer à écrire beaucoup de code.

Je vais faire quelques erreurs, n'est-ce pas, avec Golang.

Je vais faire quelques erreurs, mais je vais les corriger.

Mais ne vous inquiétez pas, je n'ai pas d'extensions, parce que je ne veux pas, vous savez, gonfler mon instance.

Parce que ce n'est qu'une des instances que j'utilise.

Sur mon PC Windows.

Pour over two, j'ai, comme 1015 différentes versions de Uber, n'est-ce pas.

Donc si vous avez besoin d'aller en ligne, d'ailleurs, le fichier main.go est votre fichier principal dans le projet.

Et c'est ainsi que vous commencez le fichier main.go, vous dites package main et vous dites import.

Et parce que vous allez importer certains packages, n'est-ce pas ? Pas tout ce que vous allez avoir.

À l'intérieur de go Lang go.

Lang est très modulaire, vous devez installer beaucoup de packages externes, et beaucoup de, vous savez, packages qui viennent avec le charbon, et vous devez spécifiquement dire que, vous savez, ce package vient de cola.

Et donc les packages tiers que nous allons utiliser seront principalement autour de lambda.

D'accord, donc nous allons en parler dans un moment.

Et puis la chose la plus importante ici sera toujours func main, parce que c'est votre point d'entrée dans le programme, n'est-ce pas, le func main.

Maintenant, avant de commencer à écrire quoi que ce soit dans le fichier main.go, ce que je vais faire, c'est essayer de créer, comme une structure de projet très simple, j'ai besoin du dossier build, n'est-ce pas, parce que je vais garder ma build de ce projet entier dans mon dossier build.

Et c'est, je vais le zipper, et puis je vais le prendre ce fichier zip à mon lambda, désolé, ma console AWS lambda.

D'accord, donc c'est pourquoi j'ai besoin du dossier build.

Et j'ai besoin de mon dossier CMD, parce que c'est là que je garde habituellement mon main, pas désolé, pas dans la build, mais dans mon dossier CMD, je garde mon fichier main.co.

D'accord, et puis vous aurez un dossier de package.

Donc si vous travaillez avec Golang, avant cela, comme le type de structure très standard, n'est-ce pas, rien, rien de nouveau.

Donc le package, comme vous le savez déjà, aura des gestionnaires, des gestionnaires pour gérer les API.

Et puis vous aurez, j'aurai un dossier pour l'utilisateur.

Je vais vous expliquer pourquoi je fais cela.

Et puis j'ai une fonction de validation très simple où je vais la garder dans un dossier appelé validateurs.

validateurs.

Désolé.

C'est tout.

Oui, donc dans les validateurs, je vais avoir juste un petit fichier de Pedley comme cinq, six lignes de code, je pense.

Il va juste être comme un email valide juste pour vérifier si mon email est valide pour l'utilisateur.

Et ici dans mon utilisateur, j'aurai un fichier appelé user.co.

D'accord, et mon gestionnaire, c'est là que réside ma logique principale.

Donc c'est un projet très court, très petit, les gestionnaires, je vais juste avoir deux fichiers, j'aurai API response.go, parce que j'ai besoin de ce fichier pour ma passerelle API, je vais le construire, vous comprendrez ce que c'est.

Et puis c'est handlers.co.

Bien ? Maintenant, mon fichier user.go est une sorte de combinaison de mes modèles, et de mes, presque comme mes contrôleurs aussi, vous savez, donc j'ai des gestionnaires.

Mais vous savez, le fichier user.go aura beaucoup de code, qui parle de ma base de données, d'accord, parle directement à ma base de données.

Donc j'aurai ces modèles comme ces structs aussi, en même temps, nous aurons des fonctions de modèle, celles-ci.

Donc des fonctions de base de données en même temps, je vais me diriger vers votre fichier main go.

Et func main, je pense que ce que je vais faire, c'est commencer par cet endroit, n'est-ce pas, une fois que j'ai été enseigné, obtenir l'environnement AWS région.

Donc la région AWS est très importante, parce que c'est là que votre lambda ira et se fixera.

Bien.

Donc avec AWS, si vous avez beaucoup travaillé avec AWS, vous savez qu'il a différentes régions, n'est-ce pas.

Donc mon AWS particulier est considéré comme configuré avec l'Inde, qui est l'Asie Pacifique Sud un.

Donc si vous avez utilisé le CLI et que l'installation est, ce sera génial.

Sinon, aussi, je ne pense pas que vous devriez avoir un problème, n'est-ce pas.

Mais essayez simplement et essayez de configurer un CLI.

C'est très facile, juste un processus de cinq minutes.

Et ce sera très simple pour vous de suivre avec toutes mes autres vidéos aussi, parce que dans mes autres vidéos, c'est un prérequis.

Donc comment créez-vous une session ? Donc vous direz session dot new session.

Maintenant, si je l'appelle old, qui est ici, n'est-ce pas, donc j'ai besoin de l'avoir ici.

C'est le package, n'est-ce pas ? Et si j'appelle session ici, session est quelque chose que AWS lambda me donne, AWS me donne désolé, donc je vais dire github.com/now.

En regardant la documentation pour les packages AWS, en même temps, vous pouvez le faire sinon, au cas où vous êtes le type de personne qui veut, comme savoir exactement quel package vous installez, parce que je suis ce type de personne, je veux installer des packages supplémentaires, n'est-ce pas.

Donc si vous êtes comme moi, vous, vous voulez peut-être ouvrir, comme je l'ai fait, vous voulez peut-être ouvrir le SDK AWS, il s'appelle donc je vais dire AWS slash AWS SDK pour go, vous voulez, nous voulons ouvrir la documentation.

Et ici vous verrez qu'il sera juste slash session.

D'accord, et pour créer la nouvelle session, vous direz AWS dot config et la parenthèse qui sera des accolades, vous direz région, AWS taut string et direz que vous passerez la région d'accord.

D'accord, bien.

Et puis, comme vous le savez, avec tout ce qui concerne Golang, chaque fois que nous n'avons pas, nous obtenons généralement deux choses, n'est-ce pas, nous obtenons la chose que nous cherchons, qui est la session d'oreille qui viendra de la fonction de session, n'est-ce pas, ou désolé, la fonction de nouvelle session, qui fait partie du package de session que nous avons ici.

Et nous obtenons l'erreur.

Donc avec go Lang, vous devez gérer les erreurs, et c'est une manière très propre et nette de gérer les erreurs car à chaque étape vous savez d'où cela vient et vous pouvez le gérer là-même.

Donc s'il y a une erreur, retournez simplement et je veux créer une variable appelée Dinah client qui pour mon DynamoDB et point new et comment vous créez un nouveau client direz AWS session parfait que vous venez de créer ici.

Donc vous avez créé la session et ensuite nous dirons lambda point start et handler.

Donc cela, vous ne comprenez peut-être pas maintenant, pas de problème.

Donc d'abord, nous voulons DynamoDB Comment obtenez-vous DynamoDB vous l'obtenez comme ceci, il dira github.com/aws/aws SDK go slash service slash Dynamo DB.

D'accord, donc vous avez session vous avez DynamoDB et vous voulez AWS lui-même et le premier endroit où nous dirons github.com slash AWS SDK co slash class.

Pour obtenir cette fonction lambda ou désolé, le package lambda, qui a la fonction Start, vous avez besoin de la fonction Start, ou vous ferez est que vous direz github.com/aws/aws Lambda go slash lambda.

Cool.

Jusqu'à présent, tout va bien.

C'est ce dont j'avais besoin, vous savez.

Et j'ai besoin de quelque chose appelé le handler, dont nous parlerons.

D'accord, pour l'instant, je crée une constante appelée table name.

Stable name est lambda user.

Je vais dire lambda in go user.

Et maintenant, il est temps de créer mon handler, qui est ceci, essentiellement.

Donc je passe par handler là.

Dans mon handler, ce que je fais, c'est que j'ai une requête.

Essentiellement, j'accepte certaines choses, n'est-ce pas.

Et cette fonction, et je retourne certaines choses, et elle a une certaine définition.

Donc qu'est-ce qu'elle accepte ? Elle accepte events dot API, Gateway proxy.

requests.

Donc vous vous demandez ce qu'est events ? Exact ? Donc events est essentiellement ce que Go Lang.

lamda nous donnera donc je viendrai ici.

Et je vais dire github.com/aws/aws, lambda go slash events.

Parfait.

Et l'autre chose que cela accepte est star events dot API.

D'accord, à une réponse proxy.

Désolé, je voulais dire que cela accepte une requête, retourne une réponse.

Je ne suis pas sûr de ce que j'ai dit avant cela.

Ce que j'essaie de dire ici, c'est que, vous savez, c'est une fonction qui accepte quelque chose et retourne quelque chose, évidemment accepte les requêtes, évidemment retourne une réponse, n'est-ce pas ? Pas de complication là.

C'est ce que vous voulez faire.

Et ce que vous ferez ici, c'est que vous basculerez la méthode HTTP.

Donc vous direz switch, insérez request dot HTTP method.

Donc quelles sont les méthodes que vous avez ? Vous avez get POST, PUT et DELETE ? C'est tout ce que vous avez.

Donc pour chaque méthode d'historique différente, nous voulons appeler une fonction différente.

Comment faites-vous cela ? Donc vous direz switch.

Donc nous avons déjà basculé, n'est-ce pas ? Nous avons déjà basculé.

C'est comme, il est 8h30 ici, donc je suis un peu endormi.

Je m'endors habituellement à 23h.

Mais d'une manière ou d'une autre, je suis endormi plus tôt, parce que je me suis réveillé très tôt.

J'ai rejoint cette classe d'arts martiaux qui, vous savez, me fait me réveiller à 5h ces jours-ci.

Donc vous aurez quelque chose appelé handlers.

Bien ? Et d'où viendront ces handlers ? C'est essentiellement ces handlers que vous voulez importer.

Donc qui sont essentiellement votre propre création, votre, vous savez, les handlers ou vos propres créations dirons github.com/kill/go server less, righty slash packets slash handlers.

Cool.

Donc vous dites à go Lang que c'est mon projet github.com/search Go to go serverless whitey ? Et dites que j'ai un dossier appelé package au lieu de j'ai un package appelé handlers.

Bien ? Et handlers le fichier.

En haut de ce fichier, vous direz package handlers et il appartient au dossier handlers, puis go Lang comprend, d'accord, c'est de quoi nous parlons.

D'accord.

C'est le format.

Je veux dire, bien que le nom du dossier et le nom du package doivent être les mêmes.

Je vous le fais juste savoir, au cas où vous ne le sauriez pas.

Je veux dire, je suis assez sûr que vous le saviez, mais je veux juste m'en assurer.

Donc vous avez des requêtes, un nom de table et un client Dinah, bien ? Donc vous avez envoyé cela à cette fonction appelée handlers dot get user, sur laquelle nous travaillerons dans un moment.

Donc c'était votre cas get.

Maintenant, vous avez plus de cas, bien, vous avez, selon la méthode HDB, donc vous avez post, vous aurez put, et vous aurez Delete.

Pour post, vous verrez return handlers dot create.

User.

Encore une fois, vous passerez request, virgule, nom de table, virgule, client Dyna.

Pour put, vous passerez écrit, et lawyers dot update user request, virgule, désolé, request, virgule, nom de table, virgule, client diner.

Et pour delete, processus deux handlers dot delete user.

Et la même chose que vous passez les mêmes choses, virgule, client Dinah.

Et après delete, vous donnerez simplement un défaut.

Si vous travaillez avec des instructions de cas de commutation, vous connaissez évidemment ce défaut, n'est-ce pas ? Et essayez de garder l'orientation identique.

Cela n'affectera pas.

Mais juste comme une bonne habitude, vous savez, je veux dire, je ne le fais pas beaucoup de fois.

Mais j'essaie de le faire ces jours-ci.

D'accord.

Donc par défaut, vous voulez appeler cette fonction appelée unhandled.

Method, qui est à nouveau dans votre fichier handlers ou package handlers.

Et c'est l'ensemble du tableau.

Je veux dire, je ne pense pas que nous manquons quelque chose.

Nous avons le package OS ici, nous avons des événements lambda AWS session DynamoDB.

Oui, il y a un autre package.

En fait, si vous regardez la documentation du SDK AWS, alors vous voulez l'importer était SDK, go slash, service slash DynamoDB slash Dynamo DB I face.

Gardez simplement ces packages.

Et ce que je pense que nous devrions faire, c'est que nous devrions simplement dire go mod tidy.

Donc nous obtiendrons tous les packages dont nous avons juste parlé.

Et habituellement, comme beaucoup de fois je fais cela à la fin de la vidéo, n'est-ce pas ? Mais cette fois, je le fais simplement avant.

Parce que beaucoup de gens commencent à paniquer, Hé, vous installez tous ces packages ? Si ce n'est pas le cas, vous n'avez pas exécuté la commande go might go more tidy.

Ou vous faites tellement d'erreurs, mec, en tapant.

Pourquoi ne pas installer quelques extensions, je vous ai expliqué pourquoi ne pas installer des extensions, n'est-ce pas.

Donc, avec Golang, je veux dire, ce qui se passe, c'est que, vous savez, nous venons généralement d'un arrière-plan JavaScript, et puis nous pensons que, oh, vous savez, si vous faites toutes ces erreurs, et le programme complet va planter, et il sera difficile de le résoudre avec go Lang.

Golang est très différent des autres langages de programmation, n'est-ce pas ? Faites autant d'erreurs que vous voulez.

Et une fois que vous exécutez le programme, Golang va vraiment tout gérer pour vous, il vous dira quelle ligne, quel est le problème, c'est assez intelligent.

Bien ? Ce n'est pas comme vos autres langages de programmation réguliers comme JavaScript.

Ici, une chose que nous avons oubliée était de créer le client de données en premier lieu, n'est-ce pas, donc le client a dans la variable, et la définition du type de variable le client de données est, donc quel type de temps ils seront.

C'est pourquoi nous utiliserons cela ou peut-être des ifs, n'est-ce pas, nous dirons dot Dynamo.

Dynamo DB.

API.

Assurez-vous simplement de bien faire cela.

Très bien.

Donc c'est votre fichier principal, votre fichier principal est complet.

Et maintenant vous voulez commencer à gérer les gestionnaires.

Donc ici, puisque ces deux fichiers appartiennent au même dossier, appelez les gestionnaires.

Nous voulions que les deux soient des gestionnaires de packages.

Bien ? Donc nous dirons, package handler yours.

Bien.

C'est clair.

Maintenant, j'espère et après avoir écrit le package, vous dites import et puis vous avez votre fonction principale pour dans ce cas, cette fonction principale de ce fichier s'appelle API response, accepte certaines choses, retourne certaines choses et a une définition de fonction.

Qu'est-ce qu'elle accepte ? Elle accepte status, qui est int et body, qui a une interface.

Qu'est-ce qu'elle retourne ? Elle retourne l'événement start, API gateway proxy response, virgule error.

Très bien.

Pour importer, vous direz et codage slash JSON github.com/aws/headress, lambda Gqo slash events.

D'accord.

Tout ce que nous faisons avec cela, c'est essentiellement définir la réponse, n'est-ce pas ? Donc nous dirons response est égal à events dot API gateway response.

Et la réponse, vous définissez simplement les en-têtes.

Très standard.

Parce que la façon dont nous allons configurer ces en-têtes est quelque chose que nous avons déjà vu tant de fois.

C'est essentiellement le type de contenu et l'application JSON.

Donc nous disons que nous retournons JSON de notre fonction lambda, rien d'extraordinaire.

Donc nous dirons response dot status code est égal à status.

Et donc, vous êtes comme 400, ou 300, ou quelque chose comme ça.

Et puis vous direz String body, virgule JSON dot Marshall.

Donc vous êtes, si vous avez été avec Golang, vous savez déjà qu'il s'agit de marshalling et de marshalling, désolé, Golang ne comprend pas JSON par lui-même.

Donc il a besoin de l'aide de JSON marshalling, qui fait partie de ce package encoding slash JSON.

Et donc chaque fois que vous envoyez du JSON, depuis postman dans post postman, ou peut-être le terminal, où que vous envoyiez du JSON, il faut essentiellement que coolant le comprenne, et aussi les informations que Golang produit pour qu'il devienne JSON, et l'envoie comme une réponse qui a aussi besoin, vous savez, d'aide, go Lang lui-même avec des bateaux.

Donc c'est ce qu'on appelle le marshalling et le unmarshalling.

Il y a des centaines de vidéos à ce sujet.

Sur YouTube, vous pouvez vérifier, rien de fantaisiste ou rien de compliqué.

Vous devez le faire dans, vous savez, presque tous les autres langages, n'est-ce pas, qui ne sont pas JavaScript, comme Java et Python, tous ces langages, vous devez faire quelque chose comme ça, n'est-ce pas ? Parce que tout langage qui n'est pas JavaScript ne comprend pas JSON, par défaut, parce que JSON est la notation d'objet JavaScript.

Donc c'est votre réponse API à go.

D'accord, c'est tout.

Je veux dire, il n'y a pas grand-chose qui se passe ici dans ce fichier.

Mais l'autre fichier dans les gestionnaires, package gestionnaires, c'est là que nous allons passer du temps parce que, évidemment, il y aura beaucoup de choses qui se passent ici, n'est-ce pas.

Donc les fonctions principales qui seront généralement là seront basées sur notre fichier main.go.

Donc main, le fichier Go nécessite la fonction get user, create user, update, user, delete user et la méthode anonyme.

méthode non gérée, désolé.

Donc ce sont les fonctions que, évidemment, vous devez créer, n'est-ce pas ? Donc nous dirons get user.

Et il dira Create User.

Il dira Update user et delete users.

Update user et delete user.

D'accord, donc ici.

La dernière fonction que nous voulons garder ici est unhandled.

Method.

Bien ? Donc, par exemple, si quelqu'un utilise la méthode patch, parce que nous gérons, get POST, PUT, delete, si quelqu'un utilise patch, alors nous dirons que, hey, ce n'est pas géré, n'est-ce pas.

Donc nous dirons unhandled method, accepte certaines choses, retourne certaines choses et donc, définition de fonction.

D'accord, donc c'est, en général, à quoi votre fichier handles va ressembler.

Et ce que nous pouvons faire, c'est que nous pouvons travailler sur notre fichier is email validated, valid file Donc nous dirons package validators.

Et il y a un package que vous obtenez avec go Lang.

Il s'appelle regular expressions.

Et nous créons simplement une fonction simple où nous disons simplement si l'email est valide ou non, n'est-ce pas, vraiment simple.

Tout ce qu'il fait, c'est accepter une chaîne d'email.

Et retourne un booléen, comme, vrai ou faux.

Nous prendrons une variable appelée Alex email, nous utiliserons la fonction d'expression régulière, le package d'expression régulière.

Et si vous regardez la documentation des expressions régulières, comme je l'ai devant moi, allez sur la documentation officielle de Golang et consultez le package d'expressions régulières de dragon, je vous recommande vivement de l'ouvrir si vous le souhaitez, car c'est ce que j'ai fait ici, dans mon autre écran, nous utiliserons la fonction appelée must compile.

Et je vais copier et coller une chaîne d'expression régulière ici.

Vous n'avez pas vraiment besoin de comprendre ce que cela fait, vous l'obtenez directement de la documentation.

Mais si vous voulez vraiment savoir, en gros, vous vérifiez simplement si vous savez que les nombres sont entre A et Zed A à Z, et zéro à neuf, ce genre de choses, n'est-ce pas ? C'est tout ce qu'il fait.

Et il vérifie également le symbole at.

Bien.

Mais évidemment, s'il est quelque part, il doit avoir une annonce, n'est-ce pas.

Donc ces genres de choses, juste une vérification de validation d'email de base se passe là, vérifiez la documentation de l'expression régulière si vous voulez vraiment comprendre ce que fait cette expression régulière, d'accord.

Mais si vous voulez gagner du temps, copiez et collez-le comme je viens de le faire.

Et maintenant, nous voulons vérifier la longueur de l'email.

Si l'email, si une autre femelle n'a pas trois, ou la longueur de l'email est supérieure à 254 ou Arex, la variable email, ne correspond pas à la chaîne.

Alors vous retournerez simplement false.

Bien, donc cela retourne soit vrai soit faux.

Si ces conditions ne sont pas remplies, alors vous retournez false, sinon vous retournez true, ce qui signifie que tout est bien.

Et l'email est valide.

Bien ? Évidemment, si ce n'est pas correct, cela ne fonctionne pas correctement.

Si la longueur est plus grande, la longueur est inférieure, nous dirons que l'email n'est pas valide.

Sinon, je vous dirai que vous pouvez changer ces nombres comme vous le souhaitez.

Mais je les ai gardés à trois et 254.

D'accord, changez-le sur votre test.

Donc maintenant, nous allons dans notre fichier user.go.

Et nous allons simplement ajouter un niveau très élevé de 10 000 pieds, je vais simplement configurer ce fichier.

Maintenant, ce que je veux qui se passe, c'est que pour mes gestionnaires, comme le contrôle de domaine, vous savez ce qui ira dans le fichier principal vers notre, vous savez, vers cette fonction, essentiellement.

Et cette fonction appelle la fonction Get User et create user, update user.

Et toutes ces fonctions sont, comme vous le savez, mentionnées dans les gestionnaires, n'est-ce pas.

Et à partir des gestionnaires, des gestionnaires, vous appellerez les fonctions dans votre fichier user.co.

Et ces fonctions seront en fait les fonctions de base de données qui parlent réellement à la base de données, n'est-ce pas.

Donc chaque fonction que vous avez ici, à l'exception de la méthode unhandled, parce qu'elle ne fait pas grand-chose, ces quatre fonctions crud que nous avons, elles ont une fonction équivalente dans votre fichier user.go, une fonction complète comme une fonction un à un dans votre fichier user go qui parle à la base de données.

D'accord, donc faisons cela.

Créons ces fonctions.

Donc premièrement, comme vous le savez, lorsque nous commençons un fichier, nous importons certaines choses.

Et puis ici, je vais aussi vouloir définir certaines variables, certaines erreurs que je veux définir.

Donc les fonctions que je veux avoir ici et mon fichier user.go, qui aura une relation un à un avec ces quatre fonctions, la première fonction sera appelée, je l'appellerai fetch user.

Donc cela signifie que ma fonction Get User est appelée par mes gestionnaires.

Et cette fonction appellera dans mon fichier user.go, la fonction fetch user, qui obtient directement l'utilisateur de la base de données elle-même, la base de données, dans ce cas étant DynamoDB.

D'accord, donc elle accepte certaines choses, retourne certaines choses et a une définition de fonction simple.

La deuxième fonction que je veux avoir est pour obtenir plusieurs utilisateurs en fait, donc je vais dire func fetch users.

De manière similaire, cela ressemblera beaucoup.

Ensuite, je veux avoir une fonction create.

Donc nous aurons create user et ensuite il a update user, vous devez simplement continuer à regarder ici et ensuite créer ces fonctions.

Ensuite, vous avez la loi ainsi que delete user, bien, donc vous viendrez ici, bien, si cela ne se supprime pas, alors vous n'avez pas besoin de retourner quoi que ce soit de spécifique, vous pouvez simplement retourner une erreur.

C'est pourquoi le retour ici est juste une erreur.

Bien ? Et c'est à peu près tout.

Donc nous avons réussi à une fonction, toutes celles-ci, mais il y a une fonction supplémentaire qui est juste fetch users.

D'accord, donc nous verrons où obtenir où l'utiliser.

Donc d'un point de vue à 10 000 pieds, c'est votre fichier user.go, et c'est votre fichier handlers.

Donc ce que nous allons faire, c'est commencer avec la fonction Nora handlers, et en même temps, nous allons commencer à travailler sur nos fonctions user.co.

Et ici, vous allez tous évidemment importer certaines choses, n'est-ce pas.

La première chose dont j'ai besoin est net slash HTTP.

Ensuite, j'ai besoin de mon événement lambda.

Donc je vais dire github.com/ad/aws, lambda go slash events.

Maintenant, il est possible que je les importe, mais vous ne comprenez pas pourquoi je les importe.

Donc vous pourriez être confus.

Donc maintenant, il y a deux façons de le faire.

L'une est quand j'écris réellement le code, et ensuite j'utilise ce paquet d'événements quelque part, et ensuite je viens et je l'importe.

Ou je sais, vous savez, lesquels j'ai besoin.

Donc je vais simplement les importer dès le début.

Donc je pourrai les utiliser plus tard.

Donc je fais juste cela.

Donc essayez de ne pas être confus, parce que nous allons réellement utiliser ces packages dans juste deux, trois minutes.

Ne vous inquiétez pas, vous savez pourquoi nous les importons, nous allons les réutiliser.

Donc soyez patient.

Slash AWS.

Bien.

Ce sont les mêmes packages que nous utilisons déjà dans notre fichier main.go.

Et nous dirons github.com/aws/check it go slash service slash, no DB slash Dynamo DB I face.

Super.

Une chose dont j'ai besoin ici, parce que je voudrais appeler ces fonctions, comme je vous l'ai dit, n'est-ce pas, je veux appeler cette fonction.

Donc c'est pourquoi je veux importer ce package utilisateur et mon fichier handlers.

Comment pourrais-je faire cela ? Je dirais github.com/achill/go, server less writing slash package, slash user.

Donc à l'intérieur du package, à l'intérieur du package utilisateur, nous l'avons importé ici.

D'accord, et ensuite avant de commencer, ces fonctions que je veux définir une variable très variable appelée error method not allowed.

Est égal à method not allowed ? Et pourquoi ai-je besoin de créer cela ? Parce que d'abord, nous allons travailler sur cette fonction unhandled method, n'est-ce pas ? Donc c'est pourquoi vous voulez appeler cette fonction.

Donc ici, cela retourne et event API gateway event.

Donc il dira API, Gateway proxy response, virgule, error.

Bien, donc nous allons envoyer une réponse d'ici, ou cela enverra une erreur.

Et ici, nous dirons return pay API response, la réponse que vous voulez envoyer est HTTP dot.

Lorsque nous disons HTTP, nous parlons du package d'histoire, n'est-ce pas, status.

Method, not allowed, virgule.

Header method not allowed, que nous avons juste défini ensemble, n'est-ce pas ? C'est ce que vous dites.

Donc vous dites que nous avons, vous savez, quelque chose pour get post put in place, mais nous n'avons pas quelque chose pour patch, donc patch ou toute autre méthode que quelqu'un veut utiliser.

Donc si vous obtenez quelque chose comme ça, comme une méthode de gestion non gérée, donc vous enverrez une réponse disant que, hey, ce mètre n'est pas autorisé.

D'accord.

Et je veux créer une autre variable, mais c'est en fait une struct, n'est-ce pas ? Donc c'est un corps d'erreur.

Et je vais l'utiliser beaucoup, donc soyez patient avec moi quant à la raison pour laquelle je le crée.

Cette struct a une variable appelée error message, string.

Error, virgule, omit empty.

Maintenant pour votre get user.

Vous avez he accepte quelque chose et vous tournez quelque chose avant que je ne vous obtienne, qu'acceptez-vous ? Que voulez-vous, que fait la fonction get you obtenez une requête de postman, la requête que vous obtenez fait partie d'un paquet d'économies.

Donc vous pouvez dire events dot API gateway request, virgule table name, qui est string, virgule, Dyna client, dot Dynamo DB API.

Et qu'est-ce qu'il retourne ? retourne la réponse, évidemment.

Donc nous dirons events, dot API gateway, proxy response, virgule, Irish.

Direct.

Et en fait, ces deux choses, n'est-ce pas, allait accepter et allait retourner va être utilisé par toutes les fonctions.

Donc ce que vous faites, c'est que vous copiez et vous collez simplement ici pour CREATE USER pour update user, ainsi.

Et pour delete user ainsi.

Génial.

Donc nous avons fait beaucoup de travail.

Maintenant, je veux commencer à travailler sur les définitions de fonctions pour toutes ces fonctions.

Bien, donc la première chose que vous direz, c'est email, request dot query, string parameters.

Donc si vous avez deviné, ce qui se passe ici, c'est que vous voulez obtenir l'utilisateur mais en utilisant l'email ID de cet utilisateur.

Donc pour ma requête, vous aurez vos paramètres de chaîne de requête, qui passeront un email et que nous allons capturer dans une variable appelée email.

Et puis nous vérifierons la longueur.

Donc nous dirons si la longueur de l'email est supérieure à zéro, alors vous obtiendrez un seul utilisateur.

Donc nous dirons user dot fetch user, que nous venons de créer ensemble, n'est-ce pas ? Nous n'avons pas créé la définition.

Mais vous savez de quelle fonction je parle.

C'est dans mon package utilisateur, qui a été importé ici déjà.

Donc fetch user va prendre l'email, le nom de la table et le client donneur.

Et je vais capturer cela dans le résultat, ou quand il y aura une erreur.

Et s'il y a une erreur, je vais gérer l'erreur.

Donc je vais dire si l'erreur n'est pas égale à nil.

Return API response a été dot, status, bad request.

Virgule, ou body.

Donc le corps de tout le monde est une struct que j'ai déjà définie.

Et dans notre corps, je veux passer AWS dot string error dot error.

Et sinon, vous direz hello, DB dot, tout va bien.

Donc nous dirons status.

D'accord ? Si tout se passe bien, et vous passerez le résultat de cette fonction.

Maintenant, si vous voulez plusieurs utilisateurs, vous direz user dot fetch users, même chose, ils auront le nom d'un client.

Et ce que vous ferez, c'est que vous utiliserez à nouveau le résultat et l'erreur pour capturer les valeurs provenant de cette fonction.

Et s'il y a une erreur, et vous vérifierez si l'erreur n'est pas égale à nil, vous retournerez la réponse API, en disant HTTP dot status, bad request parce qu'il y a une erreur, n'est-ce pas ? Et vous enverrez le corps de l'erreur, comme nous l'avons fait plus tôt, le corps de l'erreur est une struct que nous avons déjà définie.

C'est le corps de l'erreur que nous envoyons, qui est essentiellement du JSON.

Et ici, le corps de l'erreur.

À l'intérieur, nous allons envoyer, vous allez envoyer un WS dot string, header dot.

Compris ? Mais si tout s'est bien passé, et qu'il n'y a pas eu d'erreur, alors nous allons retourner la réponse API et HTTP dot status.

D'accord.

Commerce result Donc le gutsier de base get user.

Maintenant, ce que nous pouvons faire, c'est que nous pouvons travailler sur nos fonctions fetch user et fetch users, ces deux fonctions dans notre fichier user.co.

Ou nous pouvons travailler sur notre fonction CREATE USER dans nos gestionnaires.

Donc je pense que je vais faire le premier, je vais travailler sur fetch users, et je vais travailler sur fetch user, laissez-moi juste vérifier si tout est enregistré, oui, tout est enregistré parfaitement.

Je dois juste continuer à m'assurer que sinon, vous savez, je finis par faire une longue vidéo quand rien n'a été enregistré.

Et cela conduit à un gros problème.

D'accord, donc avant de faire quoi que ce soit avec les utilisateurs, je veux d'abord créer un utilisateur.

Donc comme je l'ai dit, ce fichier est un mélange de ce fichier modèle que vous créez habituellement, où vous définissez la structure de l'apparence de l'utilisateur.

Donc je vais dire user struct.

Email.

Maintenant, puisque cette struct utilisateur est petite, et nous n'avons pas plusieurs stocks, comme si c'était un e-commerce, par exemple, alors vous auriez eu des utilisateurs et des commandes et vous savez, tous ces différents comme produits et tant de stocks différents, n'est-ce pas.

Donc vous devriez avoir comme un dossier Models séparé pour tous ces différents modèles.

Et puis vous aurez, vous auriez, vous savez, des fonctions de base de données séparément, et des contrôleurs ou quelque chose comme ça, n'est-ce pas.

Mais puisque nous n'avons pas cela, nous avons un projet très petit, qui n'a que des utilisateurs et des utilisateurs eux-mêmes, c'est une struct très petite, parce que vous avez juste email, prénom et nom de famille.

Vous n'avez pas trop ici, n'est-ce pas, vous pouvez combiner les contrôleurs et les modèles dans le même fichier.

Maintenant, l'email va être une chaîne qui va dire JSON.

Et vous dites, comme ceci JSON email, parce que pour les besoins de Gulags, il sera email avec un E majuscule, alors que JSON où il est stocké, il sera email avec un e minuscule.

Donc vous devez payer un telco comme ça, vous savez, il y a deux versions, l'une, la version JSON, l'autre est la version que Golang comprend, parce que Golang ne comprend pas JSON, comme je vous l'ai déjà dit.

Donc c'est pourquoi nous devons aussi utiliser un peu de marshalling et de unmarshalling.

Pour le faire comprendre et interagir avec JSON.

D'accord, donc vous aurez le prénom et le nom de famille.

Et puis ce que nous allons faire, c'est que nous allons créer notre fonction fetch user, ce qu'elle accepte.

Donc si vous allez réellement dans les gestionnaires, vous verrez que la fonction fetch user accepte email, nom de table, client donneur.

Donc nous allons dire ici, email, et nom de table, qui est string.

Et votre client Dinah, qui est de type, vous savez déjà que dB, I face dot DynamoDB API.

Et il retourne simplement un utilisateur.

Évidemment, je veux dire, vous récupérez l'utilisateur, vous retournez cet utilisateur particulier ou vous retournez une erreur, si rien ne fonctionne.

Vous définissez une variable appelée input.

Et c'est de type DynamoDB dot get item input.

Donc nous allons devoir définir la clé sur laquelle notre fonction de base de données va s'exécuter pour trouver cet utilisateur particulier.

Et vous savez déjà que l'utilisateur sera formé pour la base de données en fonction de l'email ID.

Donc nous prenons un email id, vous prenez un email ID, et ensuite nous voulons trouver l'utilisateur qui est associé à cet email id.

D'accord, donc direct.

Nous allons dire DynamoDB dot attribute value.

Et nous allons dire email parce que nous voulons exécuter une requête sur email.

Donc email est égal à s égal à AWS dot string, désolé, à l'intérieur de cette parenthèse, nous allons passer email.

Maintenant, la chaîne est une fonction qui nous est donnée par le package AWS Aerospike.

C'est quelque chose que nous allons devoir importer ici.

D'accord.

Et de même avec DynamoDB.

Donc nous allons aussi devoir importer le package DynamoDB.

Donc venez ici sur votre import, et d'abord appelé encoding slash JSON, parce que comme je vous l'ai dit, Golang ne comprend pas JSON par défaut.

Donc vous aurez besoin du package encoding slash JSON pour utiliser les fonctions de marshalling et de unmarshalling et j'ai aussi besoin du package errors.

Ensuite, je veux mettre la main sur les événements.

Nous allons les utiliser bientôt.

Pour envoyer des réponses et les habituels.

Comme vous pouvez le voir, j'ai besoin de DynamoDB et j'ai besoin d'AWS.

Donc, obtenons ceux-ci.

Donc je vais dire AWS slash AWS SDK, go slash AWS et aussi github.com/aws/aws SDK go slash Dynamo DB.

Et ce que je vais aussi faire, c'est aussi obtenir ce package particulier.

Oui, laissez-moi faire cela pour l'instant.

Donc je vais dire github.com/aws/aws est un cas appelé slash service slash, Dynamo.

dB slash Dynamo DB.

I face.

D'accord.

Maintenant, en revenant ici, vous avez déjà passé cela.

Et après cette parenthèse, vous devez spécifier le nom de la table dans laquelle cette fonction va s'exécuter.

Donc nous allons utiliser la fonction de chaîne régulière à nouveau, pour passer le nom de la table.

Et après cette parenthèse, vous voulez utiliser votre client de données pour enfin commencer à obtenir l'élément.

L'entrée est essentiellement la requête que vous avez créée, n'est-ce pas, et get item est la fonction que vous obtenez un client d'erreur.

Et vous allez capturer cette fin de résultat et d'erreur.

Donc, pratique standard, s'il y a une erreur, nous allons l'avoir sur l'en-tête bientôt, retourner nil pour la valeur et nous allons retourner errors dot new error failed to fetch record.

Donc vous devez vous demander, d'où vient cette erreur ? Probablement jamais vu cette erreur, n'est-ce pas ? Parce que c'est une nouvelle erreur que j'ai créée moi-même.

Comment puis-je créer mes propres erreurs, je peux créer mes propres erreurs comme ceci.

Donc error failed to fetch record est égal à fail to fetch record.

Et de même, je peux définir n'importe quelle erreur que je veux dans cette variable définie comme une variable, n'est-ce pas ? Donc vous avez, vous savez, créé une requête qui est similaire à MongoDB, n'est-ce pas, vous avez créé une requête basée sur l'email, parce que vous voulez rechercher cet email afin de pouvoir récupérer l'utilisateur et vous avez exécuté la fonction get in get item pour DynamoDB.

Et vous avez passé la requête à celle-ci, et vous l'avez reçue dans quelque chose appelé résultat ou vous avez reçu une erreur.

S'il y a une erreur, vous gérez l'erreur.

Mais si le résultat est correct et que rien ne s'est vraiment passé, alors vous feriez quelque chose, n'est-ce pas.

Mais avant cela, nous allons créer une variable appelée item et elle sera essentiellement un nouvel utilisateur.

Et ici, vous direz error est égal à Dynamo DB attribute.on.

Martial map.

D'accord, donc DynamoDB attribute est un autre.

Au fait, si vous n'avez pas ouvert DynamoDB et AWS SDK, go, documentation, faites-le, car je l'ai ouvert sur mon autre écran, vous pouvez le faire aussi.

Et alors tout aura beaucoup plus de sens, car ce sont des packages réels à l'intérieur de ce package principal.

Bien ? Donc je les utilise.

Et une fois que vous aurez parcouru la documentation, vous comprendrez où utiliser lequel, ou si vous ne vous souciez vraiment pas de cela, vous pouvez simplement continuer à suivre ce que je fais.

Mais je recommande simplement que vous le lisiez car vous savez, tout aura plus de sens.

Ici, j'ai besoin de ce package, bien fait, qu'est-ce que l'attribut ? Cela m'aide à dé-marshaller l'utilisateur.

Donc d'abord, laissez-moi écrire tout le code.

Donc je vais dire result, désolé, pas ici.

Il per record dira result, dot item, virgule item.

Et cette erreur si cette erreur n'est pas égale à nil, ce que nous voulons faire, nous voulons retourner nil, virgule, errors dot nao error, failed to on Marshall record.

Donc vous devez vous demander ce qui se passe ici, n'est-ce pas ? Lorsque vous obtenez les données de votre DynamoDB en utilisant la fonction get item dans result.

Vous voulez dé-marshaller les données dans un utilisateur réel, que le front-end peut comprendre comme un JSON de base.

Donc vous utilisez la struct utilisateur et et vous prenez cela dans une variable appelée item.

Bien ? Donc item est essentiellement une variable de type utilisateur.

Et puis, vous savez, vous voulez les données qui viennent de votre résultat ou item, vous voulez que cela soit dé-marshallé et apporté dans item afin que maintenant ce qui est venu comme JSON devienne, vous savez, le type, qui est utilisateur, qui est compris par go Lang, mais et il est capturé dans une variable appelée item.

Bien ? Donc j'ai essayé de vous expliquer chaque ligne, au cas où vous ne comprenez pas, vérifiez ce qu'est le marshalling et le unmarshalling.

D'accord.

Et si vous avez des confusions, vous pouvez simplement les mettre dans les commentaires ci-dessous.

Je les trierai pour vous.

Mais ce n'est rien de très difficile, n'est-ce pas, nous prenons simplement ce qui vient de DynamoDB, le JSON, et vous le dé-marshalez pour en faire une struct, n'est-ce pas ? Qui est de type utilisateur, qui a email, prénom, nom de famille, quelque chose qui peut être compris par ko lang.

Et vous capturez cela dans une variable appelée item, qui est évidemment de type utilisateur, n'est-ce pas ? Cette struct que nous avons définie.

C'est une pratique standard, je fais cela dans toutes mes autres vidéos aussi, au cas où vous seriez nouveau sur cette chaîne, j'ai des centaines de vidéos sur ko lang, vous pouvez toutes les vérifier.

Comme littéralement des centaines de vidéos sur Cola, n'est-ce pas ? Vérifiez-les, construisez des projets avec moi.

Et vous comprendrez très facilement tout.

Donc si tout s'est bien passé, s'il y avait une erreur, évidemment, vous avez envoyé nil et vous avez envoyé les erreurs.

Mais si tout s'est bien passé, vous retournerez l'item, et ensuite vous retournerez nil pour l'erreur.

Maintenant, vous voudriez aussi travailler sur la fonction fetch users, bien que pluriel fetch users function.

Comment faites-vous cela, vous passez le nom de la table là.

Comme vous pouvez le voir, ici, vous passez en donnant lui ANA client.

Donc Duolingo a été passé, qui est évidemment un type de chaîne pour passer 10 Nine, un client qui est de type, vous savez déjà, Dynamo DB, I face dot DynamoDB API.

Et vous retournez plusieurs utilisateurs.

Comment faites-vous plusieurs utilisateurs, vous retournez essentiellement une tranche d'utilisateurs, lorsque les utilisateurs est la struct que vous avez définie, n'est-ce pas ? Donc vous utilisez une struct, vous faites une tranche de tous ces utilisateurs, et ensuite c'est ce que vous retournez.

J'espère que cela a du sens.

Si vous ne connaissez pas les bases de, de Kulang, comme les tranches et les structs, alors je vous recommande vivement de vérifier les tutoriels de base avant de vous perdre davantage.

Donc je veux utiliser une fonction que DynamoDB me donne, elle s'appelle Scan input.

Pour obtenir l'accès à un nom de table, qui a AWS dot, string, et le nom de table que nous passons déjà ici.

Bien.

Et il dira Dinah client, pensé à scanner et vous voulez scanner l'entrée, la requête que vous venez de créer.

Donc ici, comme vous l'avez vu, nous avions une requête plus élaborée, parce que nous devions obtenir un utilisateur particulier avec un email.

Mais avec fetch users, vous obtenez simplement tous les utilisateurs, vous n'avez pas de requête spécifique qui, vous savez, pour cet email, obtenez un utilisateur particulier en disant, donnez-moi tous les utilisateurs.

Donc vous n'avez pas de requête en tant que telle, vous passez simplement le nom de la table.

Donc c'est quand votre client diner, mais pouvez-vous simplement passer l'entrée, c'est tout.

Et scan est comme get all, vous savez, vous pouvez dire cela.

Donc si vous avez utilisé MongoDB, c'est, vous avez find, find all quelque chose comme cela.

Ici, vous avez juste scan, find et find one vous avez dans MongoDB.

Donc vous avez juste scan, d'accord, scan et get it.

Donc vous faites scan pour obtenir tous les résultats.

Et vous allez capturer cela dans une variable appelée result.

Et puis vous allez évidemment, si vous avez une erreur, vous savez que la manière standard de gérer les erreurs est comme ceci.

Vous direz return nil pour la valeur lorsque vous retournez une erreur.

Elle dira errors dot new error, failed to fetch record.

Et, encore une fois, comme nous l'avons fait ici, item définira item, n'est-ce pas ? L'item ici n'est pas seulement un utilisateur, c'est une tranche d'utilisateurs, plusieurs utilisateurs parce que nous obtenons tous les utilisateurs de notre base de données.

Et, encore une fois, la même chose que nous venons de faire ici.

Nous allons faire la même chose ici.

Donc nous allons dire ou faire simplement copier le tout en fait.

Copier et coller.

Mais il y a seulement un petit changement de plus au lieu de result ou item.

Vous aurez result dot items.

Parce qu'évidemment d'AWS, vous obtiendrez plusieurs items, plusieurs utilisateurs, c'est ce que vous obtenez.

Et vous retournez votre item.

Et pour l'erreur, vous retournez.

Cela a du sens.

Donc nous avons fait pas mal de choses, n'est-ce pas, nous avons déjà fait la fonction Get User et la fonction get user avait fetch user et fetch users deux fonctions de votre fichier user.co.

Maintenant, il reste trois fonctions ici, et trois fonctions apparaissent parce que nous avons déjà pris soin de la fonction unhandled method, vous n'avez pas besoin de faire quoi que ce soit de plus ici.

Donc il reste juste trois fonctions ici, trois fonctions ici.

Et tous les autres fichiers sont plus ou moins complets.

Bien ? Donc si vous arrivez jusqu'ici, félicitez-vous, parce que vous avez parcouru un long chemin.

Bien ? Donc maintenant, commençons à réfléchir à la façon dont notre fonction CREATE USER va fonctionner.

D'accord.

Donc pour la fonction CREATE USER, commençons à la construire.

Il ne se passe pas grand-chose, en fait.

Toutes ces fonctions, n'est-ce pas ? Create User, update, user, delete user, elles vont toutes se ressembler beaucoup.

Donc, je vais dire user, parce que vous savez, vous voulez appeler la fonction CREATE USER, le package user, donc nous allons dire user dot create user, qui est cette fonction, c'est ce que vous appelez, n'est-ce pas ? Et vous lui passez trois choses : request, table name, et un client, cela a du sens.

Personne ne répondra à cette fonction, vous voulez capturer cela dans une variable appelée error, désolé, result, et vous obtiendrez une erreur qui sera capturée dans une erreur.

Et vous connaissez le processus à partir d'ici, s'il y a une erreur, ce qui signifie que l'erreur n'est pas égale à nil, vous retournerez API response, HTTP dot, status, bad request, virgule, error body et ce sera le corps de l'erreur.

Tout le monde dans ce cas, d'ailleurs, est, désolé, la struct que nous voulons définir, n'est-ce pas ? Donc c'était dans le corps, c'est AWS dot string, avec un seul ou désolé, string, e RR dot error.

Virgule.

D'accord.

Et vous retournerez API response.

HTTP dot status created.

Virgule result.

Donc si cela signifie qu'il n'y a pas d'erreur, tout se passe bien, alors vous direz qu'il devrait être dot status created.

D'accord.

Et c'est à peu près tout.

C'est tout, en fait, c'est votre fonction CREATE USER, il n'y a rien de plus.

D'accord.

Et puis pour votre fonction update user, très similaire.

Vous appellerez évidemment l'utilisateur, comme vous l'avez fait ici, user dot create, user ici, vous appellerez user dot update user method.

Donc nous dirons, update user.

Et vous passerez trois choses : request, table name et diner client.

Et vous capturerez cela dans result, virgule, header.

Et puis vous vérifierez à nouveau, si error n'est pas égal à nil.

retourner une réponse API a été dot à nouveau, status, bad request, virgule, error body à l'intérieur du body.

Encore une fois, la même chose, c'était une chaîne ou un point.

D'accord, mais si tout s'est bien passé, si l'utilisateur a bien été mis à jour, alors vous retournerez API response.

Et vous direz SDP dot status, okay ? Que tout s'est bien passé, et vous retournerez le résultat.

Donc cela signifie ce qui se passe, ces deux fonctions CREATE USER update user c'est que ces deux fonctions sont appelées.

Cela signifie qu'une grande partie de la logique, la logique principale va se passer dans ces deux fonctions, n'est-ce pas ? Parce que pas grand-chose ne s'est passé dans les gestionnaires.

De même, travaillons sur notre fonction delete user.

Ici.

Vous direz user dot read user, insérez request, virgule, table name virgule Diana client.

Ici aussi, bien que la seule chose que vous apprendrez ici, c'est l'erreur, n'est-ce pas ? Si l'utilisateur n'a pas été supprimé, vous retournerez l'erreur.

Vous n'avez pas besoin de retourner le résultat et le résultat de la fonction delete.

Donc si le résultat n'est pas égal à nil, vous retournerez API response.

Vous savez maintenant ce que nous allons dire, nous allons dire says bad request et nous allons aussi envoyer le corps de l'erreur qui contiendra AWS dot string et l'erreur elle-même.

Mais si tout s'est bien passé, vous voudrez retourner la réponse avec le statut, okay ? Et vous retournerez nil pour l'erreur, d'accord, c'est à peu près tout.

Et oui, c'est tout, je pense que le fichier entier est complet.

Maintenant, nous n'avons plus rien à faire.

J'ai aussi parcouru la documentation du SDK AWS, je ne pense pas qu'il faille faire autre chose dans le gestionnaire.

Donc tout semble bien pour moi.

Et maintenant, nous allons devoir travailler sur notre fichier user of go et toutes ces différentes fonctions qui existent dans un fichier user.go.

Pour votre fonction CREATE USER, tout ce qu'elle va accepter dépend de ce que vous envoyez depuis ici, qui est request a preliminary client.

Donc ici, vous direz request, events dot API gateway proxy request, virgule table name, qui sera string, et puis un client, qui sera vous savez déjà, il pourrait y avoir une interface dot nanodegree API.

Donc qu'est-ce qu'il va retourner, il va retourner l'utilisateur qui a été juste créé, ou une erreur.

Donc ici, la première chose que nous allons faire, c'est que nous allons créer une variable ici, qui est de type user user étant la struct que nous allons définir, cela signifie que vous aurez email, prénom et nom de famille.

D'accord.

Donc commençons par là.

Maintenant, nous allons utiliser vous, pourquoi avons-nous créé cette variable vous, c'est parce que nous voulons capturer ce qui vient de postman.

Donc de postman ou de, disons, le terminal, d'où nous enverrons le JSON de l'utilisateur avec l'email, le prénom et le nom de famille.

Et ces données doivent être dé-marshalées dans vous, afin que Golang puisse les comprendre et également effectuer des opérations dessus.

Donc ce que vous voulez faire, c'est que nous voulons utiliser le package JSON encoding slash JSON pour appeler la fonction unmarshal.

Et ce que vous voulez faire, c'est que vous voulez passer le request dot body à celui-ci.

Virgule ampersand vous si l'erreur n'est pas égale à nil, et aussi ici.

Il a appelé la bonne syntaxe pour l'instruction if.

Et si l'erreur n'est pas égale à null, alors nous allons retourner nil, et nous allons retourner quelque chose pour les erreurs.

Nous allons dire erreur, invalid user data.

Mais nous n'avons pas cette erreur ici, n'est-ce pas ? Nous n'avons pas cette erreur, erreur fail to unmarshal record.

Nous n'avons pas d'erreur, invalid user data, nous avons juste erreur fail to fetch record.

C'est tout ce que nous avons défini.

Maintenant, définissons toutes les autres erreurs.

Laissez-moi définir toutes les autres erreurs dont j'aurai besoin dans ce fichier entier et au début lui-même.

Donc nous allons dire error failed to unmarshal record est égal à fail to unmarshal.

Record et error et add error et valid user data est égal à et valid user data.

invalid email aussi sera là et valid email est égal à invalid email.

Ensuite, nous aurons good not Marshal item et could not delete item so.

Ensuite, nous aurons could not put item donc nous allons dire Could not Dynamo put item as equal to code not Dynamo put item.

Et user already exists.

user does not exist, ou the user does not exist.

Pourquoi ai-je besoin de toutes ces erreurs ? Évidemment, à ce stade, vous auriez compris, je vais juste vous donner un exemple que lors de la création d'un utilisateur, n'est-ce pas, si nous vérifions si cet utilisateur existe déjà, alors nous n'avons pas besoin de créer cet utilisateur.

C'est pourquoi nous avons besoin de ce type d'erreur.

Et si vous voulez, si vous mettez à jour un utilisateur, ou supprimez un utilisateur, nous pouvons utiliser cela, que l'utilisateur n'existe pas.

Donc j'essaie de mettre à jour cet utilisateur, n'est-ce pas ? C'est pourquoi je pense à tous les types de fonctions d'erreur, j'aurai besoin de déclarations d'erreur.

Donc en fonction de cela, je viens de les créer.

Donc en revenant à vos create users, bien, maintenant, nous allons commencer à valider l'email.

Donc nous allons dire validators dot validators est le package que nous avons créé ensemble, bien, celui-ci.

Et la fonction que nous avons créée dans ce package était his email valid.

Et vous est la variable que vous définissez.

Et maintenant, après avoir dé-marshalé, le request que vous avez dans le body body est du request que vous avez obtenu de, disons, postman, ou du terminal en JSON.

Vous avez capturé cela dans vous.

Donc maintenant, vous pouvez maintenant que go Lang peut facilement comprendre vous parce qu'il est dé-marshalé, n'est-ce pas ? Ce n'est pas juste un et plus, donc vous pouvez accéder à vous dot email.

Et vous pouvez exécuter la fonction de validation dessus.

Donc ici, l'orthographe est incorrecte.

Devrais-je quand est-ce que l'email est valide ? Et vous retournerez nil, virgule, errors, dot new error, invalid email.

Bien ? Et la raison pour laquelle j'ai créé cette erreur, c'est parce que je veux voir si cet utilisateur existe déjà, n'est-ce pas ? Donc si l'utilisateur existe déjà, alors vous n'avez pas besoin de le créer.

Donc nous devons lancer une erreur.

Donc nous allons vérifier si l'utilisateur existe déjà, n'est-ce pas ? Donc je ne vais pas mettre ce commentaire, en fait, j'essayais juste de vous le montrer.

Donc pour vérifier si l'utilisateur existe réellement, vous devez exécuter la fonction fetch user, vous allez dire u dot male, virgule table name, virgule Diana client.

Et pour capturer ce qui vient de cette fonction dans current user, et nous ne gérerons pas l'erreur, donc je vais mettre un blanc là.

Donc si current user n'est pas égal à null, cela signifie que cet utilisateur existe, n'est-ce pas ? Si current user n'est pas égal à null, et que la longueur de current user dot email n'est pas égale à zéro, alors vous retournez nil, virgule, errors dot nao error, user already exists.

Et donc tout cela si l'utilisateur existe, mais si l'utilisateur n'existe pas, il dira simplement que l'utilisateur, donc comment le sauvegarder ? Donc d'abord, pour le sauvegarder, évidemment, tout ce que vous avez maintenant dans vous, vous voulez commencer à vouloir commencer à le marshaler, n'est-ce pas ? Pour que DynamoDB puisse le comprendre maintenant.

Donc vous allez dire Dynamo DB, attribute dot Marshall map, vous et vous allez capturer cela dans AV et vous allez vérifier l'erreur.

Donc s'il y a une erreur, nous allons retourner nil.

Et errors dot new error could not Marshal items que vous avez déjà défini, nous avons déjà défini cette erreur, n'est-ce pas ? Et maintenant, vous voulez commencer à créer vos données que vous allez envoyer à DynamoDB.

Donc comment feriez-vous cela ? Vous allez dire DynamoDB dot put Item input item est Av.

Virgule.

table name est AWS dot, string table name.

Et enfin, vous verrez Dana client dot put item, et vous enverrez cet input que vous avez défini ici.

Donc oui, manqué le signe égal par erreur.

Similaire à fetch users, n'est-ce pas, vous avez créé cet input, et ensuite vous appelez la fonction ANA client.

De même, vous faites la même chose ici, vous appelez la fonction put item.

Et vous allez capturer cela dans une variable blank actors blank variable ou, ou vous allez obtenir une erreur d'ici.

Et si l'erreur est là, alors vous allez simplement la gérer très facilement.

Vous allez dire return nil, virgule, errors dot new error, could not timer put item bien ici faded cette erreur déjà.

Mais si tout s'est bien passé, vous voulez simplement retourner l'utilisateur sont nil.

Génial.

Donc c'est votre fonction CREATE USER.

Et maintenant, il vous reste update user et delete user.

Tout le reste a été pris en charge, n'est-ce pas, les gestionnaires sont complets, les réponses API sont complètes, le validateur d'email est complet, et le fichier main.go est complet.

Et je pense que pour notre fichier utilisateur, nous avons importé tous les packages sauf pour les validateurs.

Donc vous avez besoin de validateurs.

Donc vous allez dire github.com, le package validateurs que vous avez déjà créé ? Nous parlons de celui-là.

Donc nous allons dire go serverless yt, slash PKG slash validators.

Il vérifiera aussi ce qui me manque pour les gestionnaires ? Je pense que j'ai déjà importé l'utilisateur.

Et je n'ai pas besoin de plus de packages.

Pour la réponse API.

Je n'ai pas besoin de plus de packages.

Pour son email valide, je n'ai besoin de rien d'autre.

Mon fichier main.go, probablement, j'ai peut-être manqué quelque chose.

Donc il a des gestionnaires a toujours même lamda AWS session DynamoDB DynamoDB est, donc tout est correct, basé sur le SDK AWS, go bien, consultez cette documentation, vous saurez pourquoi j'importe ces packages et comment j'ai utilisé ces fonctions.

Vous savez déjà cela parce que vous l'avez construit avec moi, d'accord.

Ensuite, nous allons revenir ici, encore une fois, dans notre fichier user.co.

Et commençons à travailler sur la fonction update user.

Donc ce qu'elle accepte, accepte request, qui est de type events, et a pensé à l'API gateway requests, virgule table name, qui est string virgule, Dinah client, qui est de type DynamoDB, I face dot DynamoDB.

API retourne un utilisateur, l'utilisateur mis à jour.

Et, ou bien, je veux dire, ou il envoie une erreur.

Et nous allons faire beaucoup de choses qui seront très similaires à la fonction Create User, qui est essentiellement nous créons l'utilisateur.

D'abord, nous avons créé l'utilisateur, n'est-ce pas, qui est la variable u, qui est de type user.

Et nous allons dé-marshaller, comme nous l'avons fait, nous allons dé-marshaller le corps de la requête que vous obtenez.

Donc request dot body, virgule ampersand vous donc par erreur, oui, donc je dois fermer la parenthèse ici, parce que c'est ensemble.

Et cette variable vue.

D'accord.

Et son tunnel nautique, si vous ne voulez pas suivre, vous pouvez simplement copier et coller cette partie, n'est-ce pas ? Je ne copie pas et ne colle pas parce que cette syntaxe peut être nouvelle pour beaucoup de gens.

Parce que c'est DynamoDB, un peu comme travailler avec DynamoDB.

Donc j'écris tout à la main.

Si vous voulez copier et coller, si vous êtes très à l'aise avec DynamoDB, allez-y et faites-le.

Vous n'avez pas besoin de, vous savez, pratiquer avec moi.

Ensuite, vous voulez récupérer l'utilisateur et voir si cet utilisateur existe même.

Donc vous allez dire votre email, virgule, nom de table, virgule, client de données.

Et vous voulez capturer cela dans current user en ajoutant une vérification ou le current user.

Donc si current user n'est pas égal à nil, c'est exactement ce que vous avez fait dans la fonction create aussi.

Et la longueur de current user dot email est égale à zéro alors vous retournerez nil, virgule, errors dot nao error, user does not exist.

Donc pour la fonction CREATE USER, nous vérifiions l'utilisateur associé à cet email, parce que nous voulons voir, vous savez, qu'il existe vraiment, nous ne voulons pas ajouter cet utilisateur.

Mais pour la mise à jour, nous faisons l'inverse, nous vérifions cet utilisateur.

Parce que seulement si cet utilisateur existe, nous pouvons mettre à jour les données pour cet utilisateur, cela a du sens ? Et exactement les mêmes choses que nous allons faire, parce que maintenant vous voulez commencer.

Donc maintenant que l'utilisateur, vous savez, si l'utilisateur n'existe pas, nous allons lancer une erreur.

Mais si l'utilisateur existe, alors vous voulez commencer à mettre à jour la table avec les nouvelles données.

Comment faites-vous cela ? Tout ce que vous avez dé-marshalé maintenant, du JSON au dé-marshalé, à quelque chose que Golang comprend, maintenant vous voulez commencer à le marshaler pour que DynamoDB le comprenne.

Donc vous savez déjà ce que vous voulez utiliser, vous voulez utiliser la fonction marshal map.

Pour lui passer vous, parce que vous venez de le faire marshalé.

Et quel package fait partie de celui-ci, donc il fait partie du package Dynamo DB attribute, nous allons le capturer dans une variable appelée AV ou nous obtiendrons une erreur.

Et maintenant, nous pouvons facilement gérer l'erreur.

Donc si l'erreur n'est pas égale à nil, retournez nil, virgule, errors dot new error could not Marshal it, celui-ci.

Vraiment, vraiment simple.

Maintenant, vous voulez simplement créer votre élément d'entrée et ensuite vous voulez simplement l'appeler et un client de fonction, seulement deux étapes restantes.

Donc vous direz input est égal à ampersand Dyna, plus dB, dot put item input, et l'élément est égal à Av, virgule, le nom de la table sera égal à AWS dot string.

table name.

Et la dernière chose est que vous utiliserez Diana client dot put item et vous passerez l'entrée et si l'erreur n'est pas égale à nil, nil, virgule, errors dot new error could not Dynamo put item return ampersand vous venez.

Maintenant, même ma fonction de mise à jour est complète, tout semble correct.

Et tout ce que je veux faire maintenant, c'est exécuter la commande Gomati pour obtenir tous les packages qui ne sont pas là.

Donc je pense que cela prend un moment, je ne trouve pas mon téléphone de toute façon.

Donc pendant que cela se passe en arrière-plan, nous pouvons commencer à travailler sur la fonction delete user.

Donc comme vous pouvez le voir, tout est installé.

J'avais quelques problèmes en fait.

Comme vous pouvez le voir, et la plupart des problèmes étaient parce que j'avais fait quelques fautes d'orthographe ici au lieu de SDK ajouté un S KD vous savez, donc quelques petites erreurs que j'avais faites.

Assurez-vous simplement de bien les obtenir.

Vous pouvez facilement les obtenir sur la documentation AWS SDK go ou si je mets surtout je vais mettre ce code sur GitHub.

Donc vous pouvez simplement le récupérer de là.

D'accord, cela a du sens ? Récupérez-le simplement de là au lieu de tout taper vous-même parce que j'ai fait quelques erreurs.

Donc c'était, cela prenait un moment.

Mais maintenant, il installe tous ces packages.

Donc votre fichier user.go, tout fonctionne parfaitement, n'est-ce pas ? Comme nous ne savons pas si cela fonctionne parfaitement, mais tout semble parfait pour moi.

Et tous les packages sont en place.

Tout ce que vous avez à faire maintenant, c'est travailler sur votre fonction read user, qui est en fait la fonction la plus, en fait, la plus facile.

Donc elle prend request, events dot API gateway request, virgule table name, qui est de type string client, qui est un type que vous connaissez déjà, vous savez déjà cela.

Dot DynamoDB API.

D'accord.

Donc ce que vous voulez mettre dans la définition de la fonction, vous voulez l'email de l'utilisateur, n'est-ce pas ? Donc request dot, query string parameters, et les paramètres, email, puis vous créerez votre input pour la fonction qui est de type DynamoDB.

Hen dot, delete item input, item, input star DynamoDB dot attribute.

Value.

Essentiellement, vous passez l'email, puis vous trouvez l'utilisateur et vous le supprimez avec l'email qui lui est associé.

Bien ? Rien de compliqué.

Donc vous allez dire AWS dot string.

Et vous passez email à cela.

Après cela, vous allez dire table name.

AWS dot string, passez le nom de la table.

Et maintenant que vous avez votre input prêt, comme nous l'avons fait pour toutes les autres fonctions, vous prenez le client de données, vous appelez la fonction DynamoDB, qui est delete item dans ce cas, et vous passez l'input à celle-ci.

Et put a essentiellement votre requête pour la suppression, qui est l'email ID.

Et vous obtenez l'erreur.

S'il y avait une erreur, nous allons retourner errors dot new error could not delete item.

Parfait.

Sinon, nous retournons simplement null, rien.

Essentiellement, cela signifie que l'utilisateur a été supprimé.

Maintenant, je suis sûr qu'il y a beaucoup d'erreurs.

Parce que je n'utilise aucune extension de vérification de type ou aucune extension go Lang, n'est-ce pas.

Donc il y aura beaucoup d'erreurs ici.

Donc je dois commencer à les résoudre une par une avant de le déployer dans le cloud.

Donc pour trouver ces problèmes et les corriger, je vais me diriger vers mon terminal.

Et je vais me diriger vers le dossier CMD et j'ai un co build main.co et cela commence à me donner des erreurs, n'est-ce pas ? Donc il dit sur ce fichier, ligne numéro huit.

Oui, je peux voir le problème, il doit être doublé.

Bien.

C'est ce qui en fait l'opérateur ou.

Donc vous allez exécuter la commande à nouveau.

Et maintenant vous allez obtenir toutes ces belles en-têtes que nous attendions, n'est-ce pas ? Et maintenant nous voulons commencer à les résoudre une par une.

Donc en commençant par la ligne 37, jusqu'à la ligne 145, trop d'erreurs.

Donc quand il dit trop d'erreurs, cela signifie que même après avoir résolu celles-ci, il vous en donnera beaucoup plus, n'est-ce pas ? C'est pourquoi je ne fais pas vraiment, vous savez, utiliser des extensions, parce que parce que Golang s'occupe de tout, il vous dit quelle ligne exacte, quelle partie, ce qui vous manque, vous n'avez pas besoin de, c'est un jeu d'enfant, n'est-ce pas ? Vous n'avez pas besoin d'appliquer beaucoup de cerveau, résolvez simplement ces problèmes, comme go Lang une fois que vous le faites, et tout fonctionnera.

Donc c'est pourquoi je suis si détendu tout le temps, mec.

Donc si je reviens à votre code, à la ligne 37, quel pourrait être le problème, c'est que je n'ai pas mis de virgule ici et de virgule ici.

problèmes de syntaxe de base, n'est-ce pas ? C'est ce qu'il dit, il dit problèmes de syntaxe de base.

Ici aussi, vous devez mettre une virgule.

Et continuons à mettre des virgules là où, vous savez, je pense qu'il aura besoin de virgules, donc cela a besoin d'une virgule ici, qui est la ligne 58.

Dans mon cas, vous pouvez vérifier où, vous savez, c'est pour vous.

Pour CREATE USER encore, je vais juste mettre une virgule ici juste pour être sûr.

Et je vais mettre une virgule dans la partie input qui est celle-ci.

D'accord, et dans la fonction update user.

Encore une fois, allons dans la zone input.

Ici, j'ai mis les virgules ou je n'ai pas vu de problèmes ici.

Et pour delete, définitivement vous devez mettre une virgule ici aussi bien que ici aussi bien que ici.

Donc maintenant si nous l'exécutons, beaucoup d'erreurs ont disparu, n'est-ce pas ? Et maintenant vous avez quelques autres erreurs.

Il y a aussi quelques erreurs de syntaxe, comme pour les erreurs de syntaxe, et une.

Celle-ci était que vous n'êtes pas capable de vous référer à cette fonction.

Donc essayons de corriger celles-ci aussi, en même temps.

Donc survolez votre code.

Laissez-moi voir la ligne d'abord, la ligne 88, la ligne 88, blah, blah, blah, blah, blah, oui, M est petit, alors que m devrait être grand.

À quoi pensais-je ? Suis-je stupide, vous savez, que je n'ai pas pu ? Que je n'ai pas fait, vous savez, grand, parce que évidemment, la fonction est martial map avec le M majuscule.

Bien ? Donc cela signifie simplement que peu importe à quel point vous êtes stupide, go, Lang s'occupe de tout, n'est-ce pas ? Donc vous n'avez pas besoin d'être le gars le plus intelligent de la planète.

Donc regardons les autres erreurs stupides.

Donc 108, virgule manquante ? C'est une erreur de syntaxe.

Super simple, n'est-ce pas ? Il dit même en attendant une virgule, n'est-ce pas ? Je veux dire, à quel point les déclarations d'édition peuvent-elles être évidentes ? Et puis les gens, vous savez, me disent de télécharger cette extension ? Je, je n'ai pas fait d'extinction, mec.

Go Lang fait tout pour moi.

Et il manque une déclaration après l'étiquette, je me demande si je me demande si je vous manque une déclaration après l'étiquette blah, blah, blah, blah, blah ? Oui, évidemment, le signe physique est éteint.

Et puis 147 147.

mettre une virgule ici, juste après 147.

Et puis inattendu.

Oui.

Trouvé.

Maintenant, exécutons-le.

Maintenant.

Voyons quelques erreurs de plus.

Oui, donc il a trouvé quelques erreurs de plus.

Et maintenant, vous devez aller à la ligne numéro 66, et 76 et 140.

Mais celles-ci ne sont pas des erreurs de syntaxe.

Donc ici, vous devrez réfléchir un peu à la raison pour laquelle il y a une erreur.

Donc dirigez-vous vers votre code à la ligne.

66.

Lignes 66.

Oui, donc il dit, laissez-moi regarder l'erreur, il dit, ne peut pas utiliser results dot result ou items.

Et quelque chose quelque chose quelque chose à faire avec cette fonction appelée on Marshal map.

C'est parce que vous recevez des items, pas un item, vous recevez plusieurs items, n'est-ce pas ? Donc vous ne pouvez pas utiliser la fonction unmarshal map ici, vous allez simplement voir utiliser unmarshal list of maps.

Super simple, mec, super simple.

36, ligne 76.

D'accord, il dit blah, blah, blah, blah, blah, request dot body.

Voyez, il dit request dot body undefined.

Et il dit aussi n'a pas de body avec un B majuscule.

Bien ? Je veux dire, vous n'avez pas, vous pouvez être la personne la plus stupide de la planète et corriger ce problème, parce que vous avez juste dû faire ce B majuscule.

Bien ? Donc c'est à quel point go Lang est intuitif.

Et puis vous allez à la ligne numéro 140.

Ligne numéro 140.

Je veux dire, je peux vous garantir que vous ne pouvez pas faire quelque chose comme ça avec un autre langage, n'est-ce pas ? Il dit qu'il y a un problème avec cette fonction, évidemment, parce qu'il y a une faute d'orthographe ici.

Paramètres.

Tout est corrigé maintenant.

Et maintenant, voyons.

Donc il me donne une autre erreur.

Il dit unmarshal.

Just off map est faux.

Oui, parce que j'ai fait une erreur.

Encore une fois, cela aurait dû être unmarshal list of maps, pas map.

Génial.

Donc maintenant, maintenant que votre fichier user.go est trié comme un IT, il vous montre d'abord les erreurs de syntaxe, vous les avez résolues, puis vous résolvez les erreurs logiques.

Et maintenant, il vous donne quelques problèmes avec le fichier handlers, bien, il vous donne toutes ces erreurs de syntaxe, nous allons les résoudre et il vous donnera quelques erreurs logiques.

Nous allons les résoudre aussi.

Et puis nous sommes bons à partir.

Bien ? Donc nous sommes sur la bonne voie.

Maintenant, revenons à notre code.

Donc quand votre code et commencez à partir de la ligne 19, ligne 19, mettez une virgule ici, ligne pour qu'elle tombe, mettez une virgule ici, il disait qu'il accepte en attendant une virgule de vous, n'est-ce pas ? Et ligne 54.

Virgule, ligne 59 Blah, blah, blah, blah, blah Pratama.

Ligne 62.

60 et 72 et 66 pour virgule 32, virgule.

D'accord ? Maintenant, vous commencez à obtenir les vraies erreurs, n'est-ce pas, les vraies erreurs.

Donc, ligne 22, nous venons de résoudre ce problème sur l'autre fichier ligne 22 Parce que l'orthographe de parameters est incorrecte.

Et maintenant, vous allez vous inquiéter de la ligne neuf, ligne neuf.

Une chose à noter, c'est que c'est la ligne neuf, mais un autre fichier API response serait go.

Donc ouvrez le fichier API responded, go.

Et ici, je peux voir qu'il y a un problème.

D'accord, j'ai corrigé le problème.

C'était essentiellement lié à ces parenthèses.

Et maintenant, il commence à me montrer des problèmes avec le fichier main.go, ce que je veux.

Je veux corriger les problèmes du fichier main.go.

Mais à la ligne 44, ligne 44.

Laissez-moi voir ce qui se passe.

D'accord, oui, je peux le voir, je peux voir le problème, c'est essentiellement que tous les cas doivent être ensemble.

Et par erreur, j'avais écrit cela en dehors de la parenthèse, aussi la parenthèse de commutation, et je l'ai incluse à l'intérieur.

Donc cette erreur devrait aussi disparaître.

Et maintenant, lorsque je fais cela, il a créé le fichier goal build may not go pour moi.

Donc laissez-moi voir si c'est le cas, oui, je peux voir le fichier main, je dois simplement le déplacer ici dans mon dossier build.

Et j'ai frappé le fichier build, sans aucun problème, pas d'erreurs, n'est-ce pas.

Donc maintenant, commençons le processus de déploiement.

Avant de faire quoi que ce soit d'autre, vous devez d'abord créer un fichier zip.

Donc vous allez simplement venir ici, il dira zip moins gr M et build slash main dot zip.

De build slash main.

Donc build est votre dossier main est la build que vous avez créée pour un dossier, et build slash main dot zip sera le fichier zip en utilisant la fonction zip.

Peut-être que dans votre Linux, vous n'avez pas zip, vous devrez l'installer en utilisant sudo.

apt get install zip.

Donc maintenant si nous vérifions ici, nous pouvons voir le fichier main dot zip dans mon dossier build.

Et maintenant, nous sommes prêts à commencer à le télécharger sur lambda, ou ADA plus lambda.

Mais comme vous vous en souvenez, je vous ai dit que j'ai Windows installé sur lequel je fais tourner WsL sur lequel je fais tourner ce open too.

Et par-dessus, j'ai construit ce dossier, n'est-ce pas ? Donc j'ai besoin de pouvoir accéder à ce fichier main dot zip depuis mon windows pour que mon windows puisse installer, comme le télécharger sur ma console AWS code et lambda.

Donc pour cela, je vais faire quelque chose.

Donc pour, afin de m'aider à faire cela, je dois exécuter cette commande explorer dot exe.

Dot.

Maintenant, j'espère qu'il va s'ouvrir.

Oui, il s'est ouvert à cet emplacement pour moi, et je vais copier cela.

Je vais le mettre sur mon bureau.

Génial.

Et maintenant, je peux commencer à le déployer sur ma console AWS.

Donc vous voulez commencer à déployer, mais il y a une chose que je voulais changer, c'est ce nom de table.

Donc je vais garder ce nom de table identique à mon, le nom de mon programme.

Go serverless righty.

D'accord, juste pour la cohérence, parce que nous allons devoir créer cette table dans DynamoDB.

Et laissez-moi juste chercher.

Si j'utilisais l'autre nom de table, donc vous allez simplement control Zed.

Et nous allons juste voir si j'utilisais ce nom de table ailleurs dans un autre fichier.

Cet endroit unique, il n'y a qu'un seul endroit où je l'utilisais.

Donc ici, le nom de la table doit être changé.

Il dira go server less writing.

D'accord, et maintenant, c'est quand nous commençons à déployer.

Donc connectez-vous à votre console et dirigez-vous vers lambda.

Vous devez simplement créer une fonction go server less writing server en utilisant Golang one point x, je pense que nous allons devoir changer les rôles d'exécution, créer un nouveau rôle à partir de la politique AWS demo, cette option est ce que vous devez sélectionner, et le nom du rôle, go serverless, righty execute à partir des modèles, vous devez choisir Simple micro service permissions create function successfully created, right ? Maintenant, vous voulez changer le handler.

Donc comme vous le savez, notre main, le fichier que nous allons télécharger s'appelle le fichier main.

C'est ce que notre build s'appelle, n'est-ce pas.

Donc nous allons devoir changer le handler pour signifier upload le fichier zip et le télécharger, revenir à AWS et aller à DynamoDB.

Pouvez-vous cliquerez sur Create Table Table names table name est ce que vous avez sélectionné ici go server less whitey.

Simple, n'est-ce pas ? Parce que nous avons gardé le même nom pour tout, donc et la clé primaire.

Donc il dit entrer le nom de la clé de partition, je pense que c'est la clé primaire ici est la clé primaire.

La clé primaire dans notre cas est email.

Qui est une chaîne, évidemment.

Et tout le reste est identique.

Et nous pouvons simplement créer la base de données active, elle est maintenant active.

Donc maintenant, nous pouvons passer à l'étape suivante, qui consiste à configurer votre API gateway.

Donc dirigez-vous vers votre API gateway.

Créer une API.

Maintenant pour construire une API REST.

Protocole, testez sélectionnez une nouvelle API ici.

Et maintenant, vous voulez mettre le nom de l'API, qui est cool.

Server less ID.

Et vous créez ensuite l'API.

À partir des Actions pour créer une méthode, sélectionnez n'importe laquelle.

Et ici, vous sélectionnerez le type d'intégration lambda function.

Et vérifiez cette utilisation de l'intégration lambda proxy.

Et vous avez le nom de la fonction lambda ici, qui est go serverless YT.

Et vous devez également vous assurer que cela est vérifié par défaut timeout.

Maintenant, nous devons déployer notre API.

Donc à partir des actions, déployez l'API, sélectionnez un nouveau stage, le nom du stage de staging et déployez.

Donc c'est votre URL que vous obtenez ici.

Que nous allons utiliser maintenant pour tester.

Donc testons-le.

Je m'attends à ce qu'il y ait des erreurs.

Mais faisons-le quand même.

Oh, ça a marché.

Ça a marché.

D'accord.

Donc il a créé cet utilisateur, ce qui est génial.

Restaurant la deuxième commande.

Désolé, cette commande ne se copie pas et ne se colle pas.

Maintenant, en retournant la commande get all users.

Donc nous allons obtenir tous les utilisateurs, un seul utilisateur est S, qui est en train de l'obtenir.

Et puis nous allons obtenir l'utilisateur particulier.

particular user a cet email id, il va obtenir cet utilisateur aussi pour moi, parce qu'il n'y a qu'un seul utilisateur pour l'instant.

Oui, donc cela fonctionne aussi.

Et maintenant, nous allons travailler sur notre fonction put.

Donc sick, il prend mon adresse email et change mon prénom en lalala et mon nom de famille en blah, blah, blah, n'est-ce pas ? Donc c'est fait, vous mettez à jour, cela fonctionne.

Et maintenant, nous devons travailler sur la fonction delete.

Donc si la fonction delete fonctionne, elle ne retournera rien.

Donc nous allons vérifier si cet utilisateur est toujours là, donc nous obtenons tous les utilisateurs.

Cela signifie que delete fonctionne, parce que c'est un tableau vide, n'est-ce pas ? Ce même utilisateur n'est plus là.

Parfait.

Donc cela signifie que tout fonctionne.

J'espère que vous avez apprécié ce tutoriel.

C'est une longue vidéo, je sais qu'il y a beaucoup à suivre.

Il y a beaucoup à apprendre.

Et j'espère que vous l'avez vraiment apprécié.

J'espère que vous avez appris beaucoup dans ce projet.

Et très bientôt, j'aurai un autre projet avec le tag serverless, mais il est un peu plus avancé, nous aurons plusieurs fonctions lambda, nous aurons CloudFormation, nous aurons, vous savez, ces scripts CloudFormation.

Donc tout sera fait via des fichiers YAML, et ensuite AWS CLI.

Et nous utiliserons aussi AWS, Sam pour toute la configuration.

Donc ce sera vraiment compliqué.

Donc assurez-vous d'avoir fait la vidéo AWS lambda, vous savez, et vous avez fait la vidéo serverless.

Et puis lisez un peu plus sur le fonctionnement de serverless et toutes les différentes technologies.

Et cela vous aidera vraiment dans la prochaine vidéo à venir.

Ils seront légèrement plus longs, en fait beaucoup plus longs, et ils auront comme un projet beaucoup plus compliqué, n'est-ce pas.

Donc le but de cela est où c'est comme un projet serverless monolithique, n'est-ce pas ? Ce sera un projet de microservices serverless, il y aura API gateway CloudFormation.

Ils auront beaucoup plus de technologies.

Je vais utiliser AWS, Sam pour toute l'écriture de tous les fichiers de configuration.

En tout cas, donc j'espère que vous l'appréciez et abonnez-vous à la chaîne si vous ne l'avez pas déjà fait.

Et il y a des centaines de vidéos sur go Lang sur ma chaîne, vérifiez-les.

Et je partage aussi quelques conseils sur, vous savez, votre carrière de développeur.

Donc continuez à regarder cela aussi.

D'accord, donc à bientôt et connectez-vous avec moi sur LinkedIn.

Il y a le lien LinkedIn dans ma boîte de description ci-dessous.

Merci.