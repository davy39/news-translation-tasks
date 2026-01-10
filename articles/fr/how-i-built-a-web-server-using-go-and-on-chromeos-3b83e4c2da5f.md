---
title: Comment j'ai construit un serveur web en utilisant Go — et sur ChromeOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-03T05:34:46.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-web-server-using-go-and-on-chromeos-3b83e4c2da5f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*jHeP1Jefk_56SFZY.jpg
tags:
- name: golang
  slug: golang
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai construit un serveur web en utilisant Go — et sur ChromeOS
seo_desc: 'By Peter Gleeson

  by Peter Gleeson

  How I built a web server using Go — and on ChromeOS

  Linux →ChromeOS →Android →Linux Emulator


  _Image via [WikiMedia](https://upload.wikimedia.org/wikipedia/commons/6/69/Wikimedia_Foundation_Servers-8055_35.jpg"
  rel="...'
---

Par Peter Gleeson

par Peter Gleeson

# Comment j'ai construit un serveur web en utilisant Go — et sur ChromeOS

#### Linux → ChromeOS → Android → Émulateur Linux

![Image](https://cdn-media-1.freecodecamp.org/images/K51bxKRPq0Q86V3WxHzT5MFchCLYKr1q-H89)
_Image via [WikiMedia](https://upload.wikimedia.org/wikipedia/commons/6/69/Wikimedia_Foundation_Servers-8055_35.jpg" rel="noopener" target="_blank" title=")_

« Pourquoi diable as-tu acheté un Chromebook pour le développement web ? » est une question qu'on me pose occasionnellement. Les gens ne semblent pas croire que je suis capable de m'enseigner le développement web full-stack sur une machine commercialisée pour sa simplicité et sa facilité d'utilisation.

Je dois admettre que lorsque j'ai acheté cette machine avant Noël, je ne m'attendais pas à des miracles. Tant qu'elle était livrée avec un éditeur de texte et un navigateur internet, je la voyais comme un moyen bon marché et portable d'apprendre les bases du développement web front-end et de regarder YouTube en déplacement. J'étais également convaincu par le concept du « cloud computing » (ce truc est l'avenir).

Il s'avère que j'ai été agréablement surpris par les capacités de cette petite machine. Elle démarre extrêmement rapidement, a une excellente autonomie de batterie, et avec l'aide de l'omniprésent « cloud », elle fait pratiquement tout ce que vous attendez d'une autre machine. De plus, le modèle que j'ai choisi est équipé d'un écran tactile qui se plie dans une variété de positions yoga pour vous donner une tablette ou un « tente », ou toute autre configuration que vous aimez, ce qui, si rien d'autre, a l'air cool.

Au cours des dernières semaines, cependant, je me suis davantage intéressé au développement back-end (motivé en partie par une relation tumultueuse entre moi et CSS). J'avais lu qu'il était possible d'installer Ubuntu Linux sur un Chromebook (si je comprends bien, ChromeOS lui-même est essentiellement construit sur un noyau Linux sous-jacent). Je pourrais encore le faire, mais cela semble être un processus légèrement complexe qui nécessite de passer en mode développeur, et efface le stockage local et désactive toutes les fonctionnalités de sécurité pour lesquelles ChromeOS est connu. J'ai décidé de chercher une alternative.

Et j'en ai trouvé une qui fonctionne remarquablement bien. Vous voyez, Google a récemment apporté des applications Android à certains modèles de Chromebook — et mis à part quelques problèmes de conception/UX, tout ce qui fonctionne sur votre téléphone Android devrait fonctionner en douceur sur ChromeOS. Une telle application que j'ai installée est [Termux](https://termux.com/) — un émulateur Linux pour Android, sans besoin de root. Je m'amuse avec depuis quelques jours, et pour tout dire, je suis très impressionné. [Fredrik Fornwall](https://www.freecodecamp.org/news/how-i-built-a-web-server-using-go-and-on-chromeos-3b83e4c2da5f/undefined) a fait un travail incroyable.

J'ai commencé avec une paire d'[articles](https://medium.freecodecamp.com/building-a-node-js-application-on-android-part-1-termux-vim-and-node-js-dfa90c28958f) écrits par [Aurélien Giraud](https://www.freecodecamp.org/news/how-i-built-a-web-server-using-go-and-on-chromeos-3b83e4c2da5f/undefined) — et bam ! Avant d'avoir fini mon café du matin, j'avais un serveur Node.js et une base de données NeDB en cours d'exécution localement sur mon Chromebook — pas besoin de mode développeur effrayant ! Si vous avez un appareil Android, je vous recommande vivement de mettre en signet le tutoriel d'Aurélien et de l'essayer. Vous aurez un serveur Node.js en cours d'exécution sur votre téléphone en quelques minutes.

Maintenant, je m'en sors très bien avec Node, mais je suis également intéressé à essayer quelques autres langages côté serveur — pour voir quelles sont les options avant de me concentrer sur l'un d'eux. Un langage que j'ai lu est [Go](https://tour.golang.org/welcome/1), introduit par Google en 2009. Il s'en sort plutôt bien ces derniers temps et gagne en popularité — en fait, il a été nommé [Langage de Programmation de l'Année 2016](http://insights.dice.com/2017/01/10/go-tiobe-programming-language-2016/).

Go est similaire à certains égards à des langages comme C et C++, et sa conception a effectivement été influencée par eux. Cependant, une motivation principale pour créer Go en premier lieu était une aversion pour la complexité de ces langages bien établis. Par conséquent, Go est intentionnellement un langage beaucoup plus simple à utiliser.

#### À quel point est-il plus simple ?

Par exemple, il n'y a pas de boucle « while » en Go. Non, en ce qui concerne les boucles, vous n'avez qu'un seul choix : la boucle « for ».

```go
//basiquement une boucle 'while' :
for i < 1000 {
  //quelque chose
  i++
}
```

L'inférence de type est optionnelle. Vous pouvez déclarer et initialiser une variable de manière longue, ou prendre un raccourci et assigner le type implicitement.

```go
var x int = 2

//est la même chose que :

x := 2
```

Les instructions « if » et « else » sont assez simples :

```go
x := 5

if x > 10 {
  fmt.Println("Supérieur à 10")
} else {
  fmt.Println("Inférieur ou égal à 10")
}
```

Go est également rapide à compiler et vient avec toutes sortes de packages utiles disponibles dans la bibliothèque standard, qui est bien documentée en ligne. Il a été utilisé dans un certain nombre de [projets](https://en.wikipedia.org/wiki/Go_(programming_language)#Projects_using_Go), y compris certains par des noms bien connus tels que Google, Dropbox, Soundcloud, Twitch et Uber.

J'ai raisonné que s'il est assez bon pour eux, cela vaut probablement la peine de jeter un coup d'œil. Pour toute autre personne faisant ses premiers pas dans le développement back-end, j'ai préparé un petit tutoriel, basé sur mes expériences avec Go en utilisant Termux. Si vous avez un appareil Android, ou même un Chromebook avec accès au Play Store, alors installez et exécutez Termux, et nous sommes prêts à partir (ÉDIT : jeu de mots non intentionnel).

Si vous avez un appareil Linux conventionnel, n'hésitez pas à vous joindre à nous également ! Les instructions pour le programme serveur lui-même devraient fonctionner parfaitement sur [toute plateforme prenant en charge Go](https://golang.org/doc/install).

#### Commencez avec Go avec Termux

Termux, comme toute autre application Android, est très simple à télécharger et à installer. Il suffit de chercher dans le Play Store, et d'appuyer sur INSTALLER. Une fois prêt, ouvrez-le. Vous devriez avoir une belle interface de ligne de commande vide qui vous regarde. Je vous recommande fortement d'utiliser un clavier physique (soit intégré, soit connecté par micro-USB ou Bluetooth), mais si vous n'en avez pas sous la main, j'ai entendu de bonnes choses sur une autre application Android appelée Hacker's Keyboard.

Comme couvert dans le tutoriel d'Aurélien de l'année dernière, Termux vient avec très peu de choses préinstallées. Exécutez les commandes suivantes dans le terminal :

```
$ apt update
$ apt upgrade
$ apt install coreutils
```

Bien. Tout est à jour, et coreutils vous aidera à naviguer dans le système de fichiers un peu plus facilement. Vérifions où nous en sommes dans l'arborescence des répertoires.

```
$ pwd
```

Cela devrait retourner un nom de chemin, montrant où vous vous trouvez actuellement dans le répertoire. Si nous ne sommes pas déjà là, naviguons vers le dossier « home », et voyons ce qu'il y a à l'intérieur :

```
$ cd $HOME && ls
```

Ok, créons un nouveau répertoire pour notre tutoriel Go, et naviguons dedans. Ensuite, nous pouvons créer un nouveau fichier, appelé « server.go ».

```
$ mkdir go-tutorial && cd go-tutorial
$ touch server.go
```

Si nous tapons « ls », nous verrons ce fichier dans notre répertoire. Maintenant, obtenons un éditeur de texte. Le tutoriel d'Aurélien vous présente Vim, et si vous préférez l'utiliser, alors faites-le. Un éditeur un peu plus « débutant-friendly », que j'utiliserai ici, s'appelle nano. Installons-le, et ouvrons notre fichier server.go :

```
$ apt install nano
$ nano server.go
```

Super ! Maintenant nous pouvons commencer à taper autant de code que nous le souhaitons. Mais avant de le faire, installons le compilateur Go, car nous en aurons besoin pour que notre code soit utile. Quittez nano avec Ctrl+X, et depuis la ligne de commande, tapez :

```
$ apt install golang
```

Maintenant, retournons dans nano, et commençons à écrire notre code serveur !

#### Construire un serveur web simple

Nous allons écrire un programme simple qui lance un serveur, et sert une page HTML qui permet à l'utilisateur d'entrer un mot de passe pour se connecter et voir un message de bienvenue (ou un message du type « Désolé, essayez à nouveau » si le mot de passe est incorrect). Dans nano, commencez avec ce qui suit :

```go
//Construire un serveur web

package main

import (
  "fmt"
  "net/http"
)
```

Ce que nous avons fait, c'est créer un package. Les programmes Go s'exécutent toujours dans des packages. C'est une façon de stocker et d'organiser le code, et cela vous permet d'appeler des fonctions d'autres packages facilement. En fait, c'est la prochaine chose que nous avons écrite. Nous avons dit à Go d'importer le package 'fmt', et le package 'http' du répertoire 'net' dans la bibliothèque standard. Cela nous donne accès à des fonctions qui nous permettent de jouer avec l'I/O formaté, et les requêtes et réponses HTTP.

Maintenant, mettons ce truc en ligne. Quelques lignes plus bas, écrivons le code suivant :

```go
func main() {
  http.ListenAndServe(":8080", nil)
  fmt.Println("Le serveur écoute sur le port 8080")
}
```

Comme en C, C++, Java, etc., les programmes Go commencent avec une fonction 'main()'. Nous avons dit au serveur d'écouter les requêtes sur le port 8080 (bien que vous soyez libre de choisir un autre numéro), et d'imprimer un message nous indiquant que c'est ce qu'il fait.

Cela suffira pour l'instant ! Sauvegardons le fichier (Ctrl+O), quittons (Ctrl+X) et exécutons notre programme. À la ligne de commande, tapez :

```
go run server.go
```

Cela demandera au compilateur Go de compiler et d'exécuter le programme. Après une courte pause, le programme devrait s'exécuter. Vous verrez probablement le message suivant :

```
Le serveur écoute sur le port 8080
```

Brillant ! Votre serveur écoute les requêtes sur le port 8080. Malheureusement, il ne sait pas quoi faire avec les requêtes qu'il reçoit, car nous ne lui avons pas dit comment répondre. C'est la prochaine étape. Interrompez le programme serveur avec Ctrl+C, et rouvrez server.go dans nano.

#### Envoyer une réponse

Nous avons besoin que le serveur « gère » les requêtes, et écrive des réponses appropriées. Heureusement, le package 'http' que nous avons importé rend cela facile à faire.

Pour des raisons de lisibilité, insérons le code suivant entre l'instruction import() et la fonction main(). Nous pourrions simplement continuer sous la fonction main(), cependant, et tout irait bien. Faites-le à votre manière !

Quoi qu'il en soit, écrivons une fonction de gestion.

```go
func handler(write http.ResponseWriter, req *http.Request) {
  fmt.Fprint(write, "<h1>Bonjour !</h1>")
}
```

C'est une fonction qui prend deux arguments, _write_ et _req_. Ceux-ci sont assignés aux types _ResponseWriter_ et _*Request_, qui sont définis dans le package 'http'. Nous demandons ensuite au serveur d'écrire un peu de HTML en réponse.

Pour utiliser cette fonction, nous devons l'appeler dans la fonction main(). Ajoutez le code en **gras** ci-dessous :

```go
func main() {
  http.ListenAndServe(":8080", nil)
  fmt.Println("Le serveur écoute sur le port 8080")
  http.HandleFunc("/", handler)
}
```

La ligne que nous avons ajoutée appelle HandleFunc() du package 'http'. Cela prend deux arguments. Le premier est une chaîne de caractères, et le second fait référence à la fonction handler() que nous avons écrite il y a un instant. Nous demandons au serveur de gérer toutes les requêtes à la racine web « / » avec la fonction handler().

Enregistrez et fermez server.go, puis depuis la console, exécutez à nouveau le serveur.

```
go run server.go
```

À nouveau, nous devrions voir le message de sortie, nous indiquant que le serveur écoute les requêtes. Eh bien, pourquoi ne pas lui envoyer une requête ? Il suffit d'ouvrir votre navigateur web et de visiter [http://localhost:8080/](http://localhost:8080).

Les Chromebooks ont tendance à être assez opiniâtres sur le navigateur que vous devriez utiliser, mais j'ai trouvé que Chrome était quelque peu peu coopératif lorsqu'il s'agissait de se connecter à des ports localhost. L'installation de l'application Mozilla Firefox pour Android depuis le Play Store a résolu ce problème.

Alternativement, si vous souhaitez rester entièrement dans Termux (et pourquoi pas ?), alors essayez Lynx. C'est un navigateur basé sur du texte qui existe depuis 1992. Il n'y a pas d'images, pas de CSS, et certainement pas de JavaScript. Pour les besoins de ce tutoriel, cependant, il fait très bien le travail. Installez et exécutez avec :

```
$ apt install lynx
$ lynx localhost:8080
```

![Image](https://cdn-media-1.freecodecamp.org/images/6KUO7hAwFDm0knvu19WM-KLlIIA7FOi8AhO9)
_La page d'accueil de Medium, telle que vue dans le navigateur Lynx s'exécutant dans Termux._

Si tout va bien, vous devriez être accueilli dans votre navigateur de choix avec un en-tête disant « Bonjour ! » Si ce n'est pas le cas, retournez dans nano et révisez server.go. Les erreurs que j'ai faites lors du premier essai incluaient l'utilisation d'accolades {} au lieu de parenthèses pour l'instruction import(). Il y avait aussi quelques virgules égarées se faisant passer pour des points (peut-être devrais-je utiliser Ctrl+Alt+'+' pour augmenter la taille de la police dans Termux).

#### Le site web le plus exclusif au monde

Notre serveur répond maintenant aux requêtes HTTP avec une belle ligne courte de HTML. Pas exactement le prochain Facebook, mais un pas de plus que ce que nous avions avant. Rendons-le un peu plus intéressant.

Pour résumer : nous allons créer une page qui demande à l'utilisateur un mot de passe. Si le mot de passe est incorrect, l'utilisateur reçoit un message d'avertissement lui disant cela. S'il est correct, alors l'utilisateur reçoit un grand message disant « Bienvenue ! » Comme c'est votre propre serveur sur votre propre machine, et que vous seul connaîtrez le mot de passe, ce sera un site web très exclusif.

Tout d'abord, rendons la réponse HTML un peu plus intéressante. Retournez à la fonction `handler()` que nous avons écrite précédemment. Collez tout le code en **gras** à la place de ce qui s'y trouve déjà (c'est tout sur une ligne). Attention aux guillemets ! J'ai commencé et terminé la chaîne avec des guillemets doubles, et utilisé des guillemets simples dans la section HTML. Assurez-vous d'être cohérent.

```go
func handler(write http.ResponseWriter, req *http.Request) {
  fmt.Fprint(write, "<h1>Connexion</h1><form action='/log-in/' method='POST'> Mot de passe :<br> <input type='password' name='pass'><br> <input type='submit' value='Go!'></form>")
}
```

Lorsque nous exécutons le serveur, le HTML devrait rendre la page suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/rjWaD53ByNuT1mBUBtC5uDDHrzLFWcCUs0MW)
_Premier plan : Mozilla Firefox pour Android ; Arrière-plan : Lynx pour Termux_

Maintenant, je suis conscient que j'assume une certaine familiarité avec HTML ici. Brièvement, ce que nous avons est un en-tête et un formulaire. L'attribut 'action' du formulaire est appelé '/log-in/' et sa méthode est définie sur POST. Il y a deux champs de saisie : un pour l'entrée du mot de passe, et un autre pour soumettre le formulaire. Le champ de mot de passe est nommé 'pass'. Nous devrons nous référer à ces noms plus tard.

Alors, que se passe-t-il si nous entrons un mot de passe et le soumettons ? Eh bien, nous faisons une autre requête HTTP ('/log-in/') au serveur, donc nous devons écrire une autre fonction qui gère cette requête. Retournez à Termux, et ouvrez server.go dans votre éditeur de texte de choix.

Nous allons créer une autre fonction (personnellement, je l'écrirais entre handler() et main(), mais faites ce qui vous convient). C'est une autre fonction pour gérer les requêtes HTTP — cette fois, pour les requêtes '/log-in/', qui sont faites chaque fois que l'utilisateur soumet le formulaire que nous avons créé précédemment.

```go
func loginHandler(write http.ResponseWriter, req *http.Request) {
  password := req.FormValue("pass")
  if password == "let-me-in" {
    fmt.Fprint(write, "<h1>Bienvenue !</h1>")
  } else {
    fmt.Fprint(write, "<h3>Mauvais mot de passe ! Essayez à nouveau.</h3>")
  }
}
```

Comme avant, cette fonction a deux arguments, _write_ et _req_, qui sont assignés aux mêmes types que définis dans le package 'http'.

Nous créons ensuite une variable appelée _password_, que nous définissons égale à la 'valeur' du champ de saisie du formulaire de requête appelé 'pass'. Remarquez l'assignation de type implicite avec l'utilisation de ':=' ? Nous pouvons faire cela parce que la valeur du champ de mot de passe sera toujours envoyée sous forme de chaîne de caractères.

Ensuite, nous avons une instruction 'if', utilisant l'opérateur de comparaison '==' pour vérifier si _password_ est identique à la chaîne de caractères 'let-me-in'. C'est bien sûr ainsi que nous définissons le mot de passe correct. Vous pouvez changer cette chaîne de caractères en ce que vous voulez.

Si les chaînes de caractères sont identiques, vous êtes connecté ! Pour l'instant, nous imprimons un message d'accueil ennuyeux. Nous allons changer cela dans une minute.

Sinon, si les chaînes de caractères ne sont pas identiques, nous imprimons un message 'essayez à nouveau'. Encore une fois, nous pourrions rendre cela un peu plus intéressant. Pour commencer, il serait utile que le formulaire de mot de passe soit toujours disponible pour l'utilisateur. Ajoutez le code suivant en **gras**. Ce n'est rien d'autre que le même HTML de formulaire de mot de passe que précédemment.

```go
func loginHandler(write http.ResponseWriter, req *http.Request) {
  password := req.FormValue("pass")
  if password == "let-me-in" {
    fmt.Fprint(write, "<h1>Bienvenue !</h1>")
  } else {
    fmt.Fprint(write, "<h1>Connexion</h1><form action='/log-in/' method='POST'> Mot de passe :<br> <input type='password' name='pass'><br> <input type='submit' value='Go!'></form><h3 style='color: white; background-color: red'>Mauvais mot de passe ! Essayez à nouveau.</h3>")
  }
}
```

J'ai également ajouté un style simple au message 'essayez à nouveau'. Totalement optionnel, mais pourquoi pas ? Faisons de même pour le message 'bienvenue' :

```go
func loginHandler(write http.ResponseWriter, req *http.Request) {
  password := req.FormValue("pass")
  if password == "let-me-in" {
    fmt.Fprint(write, "<h1 style='color: white; background-color: navy; font-size: 72px'>Bienvenue !</h1>")
  } else {
    fmt.Fprint(write, "<h1>Connexion</h1><form action='/log-in/' method='POST'> Mot de passe :<br> <input type='password' name='pass'><br> <input type='submit' value='Go!'></form><h3 style='color: white; background-color: red'>Mauvais mot de passe ! Essayez à nouveau.</h3>")
  }
}
```

Presque terminé ! Nous avons écrit notre fonction loginHandler(), mais il n'y a aucune référence à celle-ci dans notre fonction main(). Ajoutez la ligne de code suivante en **gras** :

```go
func main() {
  http.ListenAndServe(":8080", nil)
  fmt.Println("Le serveur écoute sur le port 8080")
  http.HandleFunc("/", handler)
  http.HandleFunc("/log-in/", loginHandler)
}
```

Voilà ! Nous avons maintenant dit au serveur que s'il reçoit une requête '/log-in/' (ce qui sera le cas chaque fois que l'utilisateur cliquera sur le bouton de soumission), il doit utiliser la fonction `loginHandler()` pour faire une réponse. Nous avons terminé ! Le code complet dans server.go devrait ressembler à quelque chose comme ceci :

```go
//Construire un serveur web
package main
import (
  "fmt"
  "net/http"
)

func handler(write http.ResponseWriter, req *http.Request) {
  fmt.Fprint(write, "<h1>Connexion</h1><form action='/log-in/' method='POST'> Mot de passe :<br> <input type='password' name='pass'><br> <input type='submit' value='Go!'></form>")
}

func loginHandler(write http.ResponseWriter, req *http.Request) {
  password := req.FormValue("pass")
  if password == "let-me-in" {
    fmt.Fprint(write, "<h1 style='color: white; background-color: navy; font-size: 72px'>Bienvenue !</h1>")
  } else {
    fmt.Fprint(write, "<h1>Connexion</h1><form action='/log-in/' method='POST'> Mot de passe :<br> <input type='password' name='pass'><br> <input type='submit' value='Go!'></form><h3 style='color: white; background-color: red'>Mauvais mot de passe ! Essayez à nouveau.</h3>")
  }
}

func main() {
  http.ListenAndServe(":8080", nil)
  fmt.Println("Le serveur écoute sur le port 8080")
  http.HandleFunc("/", handler)
  http.HandleFunc("/log-in/", loginHandler)
}
```

Enregistrez et quittez nano, et depuis la ligne de commande, demandons au compilateur Go de construire notre serveur. Cette commande compile le programme une fois, et nous permet de l'exécuter quand nous le souhaitons par la suite.

```
go build server.go
```

Donnez-lui un moment ou deux pour compiler, puis entrez la commande suivante :

```
./server
```

Vous devriez obtenir le message habituel « écoute », indiquant que le serveur est à l'écoute des requêtes. Maintenant, si vous allez dans le navigateur et accédez à [http://localhost:8080](http://localhost:8080) (ou quel que soit le numéro de port que vous avez choisi), on vous demandera d'entrer le mot de passe. Si nous l'entrons incorrectement, nous obtenons ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/apRZvOUndaRkNES29ss84xDVMk6V5B04BUrG)
_Non_

Alors que si nous entrons le mot de passe correct :

![Image](https://cdn-media-1.freecodecamp.org/images/6drLLWCu2Y5oFzu4hCocIzgIMYm9arbp3p2j)
_Firefox semble un peu plus enthousiaste que Lynx…_

#### Remarques de conclusion

Si vous avez lu jusqu'ici, j'espère que vous avez apprécié le tutoriel et que vous l'avez trouvé utile. Je l'ai conçu pour les lecteurs dans une position similaire à la mienne — un peu nouveaux dans le domaine du développement web et intéressés à en apprendre davantage sur son fonctionnement côté serveur, en coulisses.

Bien sûr, la simple page de connexion que nous avons créée ici a encore un long chemin à parcourir avant d'être quelque chose à écrire à la maison. Vous n'écririez pas vraiment le HTML dans les fonctions de gestion comme nous l'avons fait ici (le package html de Go a quelques options de modélisation sympas que je vais explorer), ni ne définiriez le mot de passe correct dans une instruction 'if'. Il serait beaucoup mieux d'avoir une base de données de mots de passe (et de noms d'utilisateur), que vous interrogeriez chaque fois que le serveur reçoit une requête de connexion.

À cette fin, Termux offre un package SQLite, ainsi que divers packages de base de données disponibles dans Node.js. Une extension intéressante à ce tutoriel serait de créer une base de données de noms d'utilisateur et de leurs mots de passe, et de permettre l'ajout de nouveaux utilisateurs. Vous commenceriez par ajouter un autre champ de saisie, et en modifiant la fonction loginHandler().

J'ai déjà exprimé mon opinion sur Termux — c'est remarquable, et j'ai hâte qu'il ne fasse que s'améliorer à mesure que plus de packages deviennent disponibles. En plus de Go et Node.js, j'ai réussi à écrire et compiler/exécuter des programmes simples en C, C++, CoffeeScript, PHP et Python 3.6, et il y a encore d'autres langages que je n'ai pas encore explorés (quelqu'un s'intéresse à Erlang/Lua/PicoLisp ?).

Quant à Go, ma première rencontre a été positive. J'aime son accent sur la simplicité, et j'aime la syntaxe, et la documentation est à un niveau accessible, mais qui me pousse à développer ma compréhension. Pour ce que vaut l'opinion d'un débutant relatif sur le sujet, cela ressemble à un croisement entre C++ et Python. Dans une certaine mesure, c'est probablement exactement ce qu'il est censé être !