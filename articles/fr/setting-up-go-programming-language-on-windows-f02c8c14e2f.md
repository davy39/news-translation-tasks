---
title: Comment installer Go pour Windows — un guide rapide et facile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T20:56:25.000Z'
originalURL: https://freecodecamp.org/news/setting-up-go-programming-language-on-windows-f02c8c14e2f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2kWUABWRtX3H8y5f.
tags:
- name: Go Language
  slug: go
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment installer Go pour Windows — un guide rapide et facile
seo_desc: 'By Linda Gregier

  Another great language to add to your full-stack developer tool belt is the simple
  and productive general-purpose programming language of Go.

  Through a project started in 2007, Go came to fruition through the efforts of some
  Google p...'
---

Par Linda Gregier

Un autre langage formidable à ajouter à votre ceinture d'outils de développeur full-stack est le langage de programmation généraliste simple et productif qu'est Go.

À travers un projet commencé en 2007, Go a vu le jour grâce aux efforts de certains programmeurs de Google. Ils ont pris grand soin dans la conception de Go pour le rendre clair et cohérent dans ses fonctionnalités linguistiques et ses bibliothèques standard, rendant Go facile et _amusant_ à utiliser.

C'est du open-source à son meilleur... mais n'oubliez pas : il est sensible à la casse !

![Image](https://cdn-media-1.freecodecamp.org/images/1*zkig49mHmtgZkGu3KcEngw.png)
_Avatars d'installation de Go_

Alors commençons avec le système d'exploitation Microsoft Windows 10. Vous verrez à quel point c'est vraiment facile — seule une connaissance de base de GitHub et de l'invite de commande est requise. Bien sûr, il existe d'autres moyens d'installer et d'exécuter le programme, mais avec une expérience limitée en codage, j'ai trouvé que cet ensemble d'instructions était le plus facile à comprendre et à suivre.

Assurez-vous de suivre ces étapes dans leur intégralité ainsi que dans le **bon ordre (comme indiqué)** pour éviter d'avoir à désinstaller Go et passer quelques heures à résoudre les problèmes liés à l'installation.

### Phase 1 : Installez les éléments suivants dans cet ordre

1. Comme Go utilise souvent des dépôts open-source (GRATUITS !), assurez-vous d'installer d'abord le package Git [ici](https://git-scm.com/download/win).
2. Accédez au site d'installation de Go [ici](https://golang.org/doc/install). Téléchargez et installez le dernier ensemble Go 64 bits pour le système d'exploitation Microsoft Windows.
3. Suivez les instructions du programme d'installation de Go.
4. Exécutez l'invite de commande sur votre ordinateur en recherchant « cmd ». Ouvrez la ligne de commande et tapez : « go version »
5. La sortie après avoir entré _go version_ devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-j7JjyJSN3DqxEdO4lrjTw.png)

### Phase 2 : Création de votre espace de travail Go

Tout d'abord, confirmez vos binaires Go : allez dans le Panneau de configuration de votre ordinateur, puis dans Système et sécurité > Système > Paramètres système avancés, et dans le volet de gauche, cliquez sur l'onglet Avancé. Ensuite, cliquez sur Variables d'environnement en bas à droite. Assurez-vous que Path sous Variables système contient la variable « C:\Go\bin ».

Ensuite, créez votre espace de travail Go. Celui-ci sera dans un dossier séparé et nouveau de l'endroit où les fichiers d'installation de Go sont enregistrés. Par exemple, vos fichiers d'installation de Go ont été enregistrés sous le chemin C:\Go et vous créez votre espace de travail Go sous C:\Projects\Go

Dans votre nouveau dossier d'espace de travail Go, configurez trois nouveaux dossiers :

![Image](https://cdn-media-1.freecodecamp.org/images/1*I3BO4S6FQ6keH6o75ATuBg.png)
_bin, pkg, src_

### Phase 3 : Créer la variable d'environnement GOPATH

Créez la variable GOPATH et référencez votre nouvel espace de travail Go. Retournez dans votre Panneau de configuration et accédez à Système, puis à Variables d'environnement. Ensuite, sous Variables système, cliquez sur Nouveau.

À côté de Nom de la variable, entrez « GOPATH », et à côté de Valeur de la variable, entrez « C:\Projects\Go »

![Image](https://cdn-media-1.freecodecamp.org/images/1*EdndcOEfhY8DWreAWXjung.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ErNq0vYJQeTJadnJZczBtw.png)

Pour vérifier que votre chemin a été correctement défini, entrez « echo %GOPATH% » sur la ligne de commande.

### Phase 4 : Test et vérification

Vous êtes maintenant prêt à vérifier que tout fonctionne correctement en ouvrant la ligne de commande et en tapant : `go get github.com/golang/example/hello`

Attendez que le code soit entièrement implémenté (cela peut prendre quelques secondes), puis entrez ce qui suit dans la ligne de commande : `%GOPATH%/bin/hello`

Si l'installation a réussi, vous devriez obtenir le message de retour suivant : « Hello, Go examples! »

![Image](https://cdn-media-1.freecodecamp.org/images/1*EXG3IKaDbFqJ3qMpD_n08Q.png)

J'espère que vous réussirez. Et si vous rencontrez des erreurs ou des messages confus, commentez ci-dessous avec les résultats de cette ligne de commande : « go env »

L'inspiration pour cet article est venue des ressources en ligne suivantes, qui étaient très faciles à comprendre et utiles lors de l'installation de Go sur mon système d'exploitation Windows :

[L'article visuellement simple et stylistique de Wade Wegner](http://www.wadewegner.com/2014/12/easy-go-programming-setup-for-windows/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*z6i4jwGkvPE3S21x_PmvMw.png)

Et maintenant, vous êtes prêt à devenir un « Gopher » !