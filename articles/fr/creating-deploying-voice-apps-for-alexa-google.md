---
title: 'Alexa et Google Home : Comment créer vos propres applications vocales et les
  déployer sur des millions d''appareils dans le monde'
subtitle: ''
author: Akash Joshi
co_authors: []
series: null
date: '2019-08-12T22:03:57.000Z'
originalURL: https://freecodecamp.org/news/creating-deploying-voice-apps-for-alexa-google
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/4x3-2.jpg
tags:
- name: Alexa Skills
  slug: alexa-skills
- name: google home
  slug: google-home
seo_title: 'Alexa et Google Home : Comment créer vos propres applications vocales
  et les déployer sur des millions d''appareils dans le monde'
seo_desc: 'Voice apps completely change the way we interact with the digital world.
  Voice adds another dimension to human-computer interaction that developers are only
  beginning to explore.

  In this article, I will show you how you can use your existing backend ...'
---

Les applications vocales changent complètement la façon dont nous interagissons avec le monde numérique. La voix ajoute une autre dimension à l'interaction homme-machine que les développeurs commencent tout juste à explorer.

Dans cet article, je vais vous montrer comment vous pouvez utiliser votre architecture backend existante et vos API, en les connectant avec vos applications vocales pour offrir une nouvelle expérience à vos clients. Les applications vocales empruntent beaucoup à notre processus de développement général, ne nécessitant pas de ressources de développement séparées.

# Ce que nous construisons

Nous allons construire une application de recherche de super-héros en utilisant l'[API Open Source Superhero](https://akabab.github.io/superhero-api/api/all.json).

J'ai ajouté un wrapper autour de cette API pour la rendre accessible depuis notre application vocale. Vous pouvez trouver le code dans ce gist - [https://gist.github.com/akash-joshi/476ead410a244a48e037c138ba2387b0](https://gist.github.com/akash-joshi/476ead410a244a48e037c138ba2387b0).

Jetez un coup d'œil à l'application terminée ci-dessous :

%[https://youtu.be/5F20v5cIQts] 

Nous allons construire cela pour les applications vocales (Alexa et Google). Nous allons utiliser la plateforme [VoiceFlow](http://voiceflow.com), qui nous permet de construire des applications vocales visuellement.

# Didacticiel Voiceflow

VoiceFlow est un moyen visuel de créer des applications vocales, et est très facile à utiliser et à comprendre.

Tout d'abord, créez un compte là-bas pour commencer.

Après avoir créé un compte, créez un nouveau projet, en lui donnant un nom approprié. Pour les besoins de ce didacticiel, nous avons choisi toutes les régions anglaises comme régions de déploiement.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_1.png align="left")

Vous arriverez sur une toile vierge après cela. Ne soyez pas submergé par toutes les options présentes à l'écran, ce didacticiel vous guidera à travers tous les blocs pertinents requis.

Dans le sous-menu des blocs à gauche, vous verrez plusieurs blocs qui peuvent être utilisés pour construire une compétence Alexa ou Google. Chaque bloc effectue une certaine fonction, et Voiceflow est basé sur la construction d'applications vocales en combinant ces blocs.

### 1. Bloc Parler

Le premier bloc que nous utiliserons est le bloc Parler. Nous l'utiliserons pour faire dire quelque chose à Alexa à l'utilisateur. Faites glisser un bloc parler sur la toile, renommez-le en Introduction et écrivez une introduction appropriée à votre application dans la zone de texte. J'utiliserai "Bienvenue dans Superhero ! Dites le nom d'un héros à rechercher !".

À tout moment, testez votre application en cliquant sur le bouton Lecture.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_2.png align="left")

### 2. Bloc Capture

Le bloc suivant que nous utiliserons est le bloc Capture. Il est utilisé pour capturer des données de la voix de l'utilisateur et les stocker dans une variable.

Tout d'abord, créez une nouvelle variable dans le sous-menu 'Variables' à gauche en tapant un nom et en appuyant sur entrée. Utilisez le nom 'hero' pour l'instant.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_3.png align="left")

Ajoutez un bloc de capture, nommez "Type d'entrée" comme "Actor" et "Capture input To" comme "hero".

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_4.png align="left")

Ajoutez un bloc de parole après celui-ci, disant : "Recherche de {hero}. ". Nous utilisons des accolades pour utiliser une variable dans la parole. Assurez-vous de saisir {hero} à la main afin que Voiceflow le détecte comme une variable. C'est une balise qui fait partie d'un langage appelé Speech Synthesis Markup Language (SSML). Vous pouvez en lire plus sur la [page de documentation officielle d'Amazon.](https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_5.png align="left")

### 3. Bloc API

Cliquez sur l'icône Plus sous votre bloc Parler pour ajouter une autre étape au bloc. Ajoutez un bloc d'intégration depuis la liste. Après cela, cliquez sur le bloc d'intégration et configurez les options dans cet ordre :

1. Choisissez une intégration - "Custom API" puisque nous allons utiliser une API personnalisée pour obtenir des données.
    

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_6.png align="left")

2. Je veux - "Make a GET request" puisque nous utilisons une requête GET pour obtenir des données JSON à partir d'une API.
    

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_7.png align="left")

Nous allons utiliser une API personnalisée (`https://super-search-akashjoshi.flexiple.now.sh/?hero=`) pour obtenir les données des super-héros.

Essayez de naviguer vers `https://super-search-akashjoshi.flexiple.now.sh/?hero=superman` dans votre navigateur pour voir quel type de données est retourné par l'API. Remplacez *superman* par n'importe quel héros que vous souhaitez rechercher.

Nous remplaçons le nom du héros par la variable {hero} afin que l'API récupère le héros souhaité correctement.

Collez

`https://super-search-akashjoshi.flexiple.now.sh/?hero={hero}`

dans la barre d'URL. Assurez-vous de taper {hero} vous-même afin que Voiceflow le détecte comme une variable.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_8.png align="left")

Cependant, nous n'avons pas encore terminé. Cliquez sur Test Integration pour tester l'appel API.

La réponse de l'API doit être mappée dans des variables de sortie afin qu'elles soient prononcées à l'utilisateur.

Ajoutez des variables pour name, fullName, born, alignment, work & base depuis la barre latérale des variables.

Copiez le chemin de sortie du fichier JSON en cliquant sur l'onglet de réponse de l'onglet Test Integration et collez-le dans le menu de sortie. Faites cela pour tous les éléments suivants - name, fullName, born, alignment, work & base.

Regardez la courte vidéo ci-dessous pour comprendre comment mapper la sortie JSON avec vos variables Voiceflow :

%[https://youtu.be/fDY_klt08mg] 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_9.png align="left")

Dans l'image ci-dessus, nous pouvons voir que l'intégration a 2 sorties, une sans texte de préfixe, et une avec fail comme préfixe. Celle sans le texte de préfixe est une sortie d'état de succès, et celle avec la sortie fail est lorsque notre appel API échoue.

Ajoutez un bloc de parole disant 'Le héros n'a pas été trouvé' connecté à l'état d'échec. Si l'API réussit et qu'un héros correspondant à la variable {hero} est trouvé, toutes les variables de sortie seront définies avec les valeurs correctes. Sinon, elles seront définies à la valeur par défaut de 0.

### 4. Bloc Si

Ajoutez un bloc si à la toile, et vérifiez si fullName = 0. Si c'est 0, connectez-le au bloc "Non trouvé".

Regardez la courte vidéo ci-dessous pour comprendre comment ajouter des conditions aux blocs Si :

%[https://youtu.be/gmS-NleBtl0] 

Sinon, le héros a été trouvé. Donc, dites le nom du héros en écrivant dans un bloc de parole : "Leur nom de héros est {name}. Leur nom complet est {fullName}. Ils sont nés en {born}. Ils sont {alignment}. Ils travaillent comme {work} depuis {base}. Voulez-vous rechercher un autre héros ?"

Encore une fois, assurez-vous de taper les noms des variables afin que Voiceflow les détecte comme des variables.

Pour effacer les variables après que la compétence soit terminée, ajoutez un bloc "Set" à la toile et définissez fullName à 0. Cette étape est nécessaire, car si les variables ne sont pas effacées, la réponse précédente sera répétée par la compétence !

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_11.png align="left")

### 5. Bloc Choix

Nous ne devrions pas terminer la compétence ici. Nous devrions permettre à l'utilisateur de choisir s'il veut rechercher un autre super-héros. Changez le texte dans le bloc "Non trouvé" pour demander si l'utilisateur veut rechercher plus à la fin.

Ajoutez un bloc Choix à la toile. Le bloc choix nous permet d'effectuer certaines actions en fonction de la voix de l'utilisateur. Ce bloc vérifie si l'utilisateur veut rechercher un autre héros. Entrez des synonymes de Oui pour rechercher davantage.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_11-1.png align="left")

Pour else, ajoutez un bloc Flow, en sélectionnant Stop Flow comme flux.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_12.png align="left")

Connectez la sortie ' 1 ' du bloc Choix à un bloc de parole demandant à l'utilisateur de dire un autre nom de héros, et connectez-le au bloc Capture. Regardez l'image ci-dessous pour comprendre comment cela se fait.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FCC_13.png align="left")

Et nous avons terminé ! Testez votre application en cliquant sur le bouton lecture.

### 6. Déploiement

**a. Alexa**

Pour déployer votre application sur la plateforme Alexa, cliquez sur l'onglet Publier, connectez votre compte développeur Amazon et remplissez les options du formulaire selon la pertinence pour votre compétence (comme la description, le nom de la compétence, etc.)

Assurez-vous de ne pas changer les invocations par défaut qui pourraient casser votre compétence pendant le déploiement et vous obliger à la soumettre à nouveau.

Au cas où vous vous tromperiez dans une partie lors de la soumission, le processus de révision est très utile et ils vous feront savoir ce qui n'a pas fonctionné dans la soumission.

**b. Google**

Cliquez sur le lien d'instruction pour voir [les instructions pour ajouter le fichier Google Assistant à Voiceflow](https://learn.voiceflow.com/articles/2705386-uploading-your-project-to-google-assistant). Après avoir ajouté le fichier, suivez le guide de publication en production depuis [ici](https://learn.voiceflow.com/articles/2712178-deploying-your-google-assistant-project-to-production). Quelques mises en garde dans le processus de déploiement Google :

1. Votre nom d'invocation ne peut pas contenir de mots-clés qui pourraient être utilisés pendant l'invocation. Par exemple, vous ne pouvez pas nommer l'action 'Superhero Search', car 'Search' peut être utilisé comme nom d'invocation.
    
2. Vous devez ajouter une politique de confidentialité personnalisée de Google. Vous ne pouvez pas utiliser celle de Voiceflow car elle mentionne Alexa ou des compétences, ce qui entraînera le rejet de votre action. Vous pouvez utiliser un modèle que j'ai construit [ici](https://docs.google.com/document/d/1ZdI1m-6Vo46vSTeWs4pG8fDHV1n8McWgcZud3TGN5k0). Il contient des instructions sur la façon d'écrire votre politique de confidentialité et où la conserver.
    
3. Le dernier point serait de ne pas utiliser le terme 'Alexa' ou 'skill' à aucun moment dans la description de votre action ou dans l'application. S'il y a des occurrences dans l'application, remplacez-les par quelque chose de plus générique afin que vous puissiez utiliser la même base de code pour Alexa et Google. Remplacez 'Alexa' et 'skill' par 'Google' et 'actions' dans la description et dans des endroits similaires.
    

# Et ensuite ?

Idées d'applications :

Le point intéressant concernant les applications vocales est que vous pouvez les utiliser comme une extension pour vos applications existantes. Par exemple, si vous avez déjà construit une application de messagerie comme [celle-ci](https://blog.flexiple.com/build-a-powerful-chat-application-using-react-hooks/), la plateforme vocale peut être un moyen facile d'envoyer et de lire des messages sur votre application. Pour une plateforme d'écriture de blog, une application vocale peut être un moyen facile de prendre des notes avant de s'asseoir pour écrire un article. Même pour une plateforme de publication de produits comme [ProductHunt](https://producthunt.com) ou [Remote.tools](https://remote.tools), vous pouvez facilement intégrer la voix pour lire la description et d'autres détails sur les produits.

De telles manières, les applications vocales peuvent être utilisées pour améliorer l'expérience utilisateur.

Liens utiles :

[https://getvoiceflow.com](https://getvoiceflow.com)

[https://learn.voiceflow.com/articles/2705386-uploading-your-project-to-google-assistant](https://learn.voiceflow.com/articles/2705386-uploading-your-project-to-google-assistant)

[https://learn.voiceflow.com](https://learn.voiceflow.com)

[https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html](https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html)

J'espère que vous avez aimé cet article. J'ai également écrit un [article plus complet](https://blog.flexiple.com/building-a-web-and-voice-app-ecosystem-amazon-alexa-google-home-react-node/) qui ajoute un frontend basé sur le web à cette application, en faisant un écosystème complet.

Bon codage !