---
title: Comment faire de la livraison continue avec Vue, Docker et Azure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T00:02:57.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-do-continuous-delivery-with-vue-docker-and-azure-2f1e31fff832
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6HS029y9bDY2lcUlub7ZRw.png
tags:
- name: Docker
  slug: docker
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment faire de la livraison continue avec Vue, Docker et Azure
seo_desc: 'By Burke Holland

  A few weeks ago at ng-conf, I announced the launch of vscodecandothat.com — a project
  I worked on with Sarah Drasner to centralize all of my favorite VS Code tips into
  a collection of short, silent video clips. It’s like a site full ...'
---

Par Burke Holland

Il y a quelques semaines à [ng-conf](https://www.youtube.com/watch?v=Xco-TEI-HU4), j'ai annoncé le lancement de [vscodecandothat.com](https://vscodecandothat.com/?WT.mc_id=deployingvue-medium-buhollan) — un projet sur lequel j'ai travaillé avec [Sarah Drasner](https://twitter.com/sarah_edo) pour centraliser toutes mes astuces préférées de VS Code dans une collection de courtes vidéos silencieuses. C'est comme un site rempli de GIF, sauf sans la charge de 600 mégaoctets et l'onglet du navigateur planté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V69E9qH9mcX-h8Ao_XeBZg.png)

Sarah a conçu et construit le site en utilisant Vue. J'ai assemblé les clips vidéo avec des références excessives aux carlins.

%[https://youtu.be/drXu4L-4Q3I]

Sarah et moi travaillons tous les deux sur l'équipe Azure, donc c'était une bonne occasion pour nous d'utiliser nos propres outils ici chez Microsoft pour travailler avec une application réelle. Dans cet article, je vais décomposer comment nous faisons de la livraison continue avec vscodecandothat.com, et comment vous pouvez le faire vous-même en utilisant les mêmes outils que nous.

Avant de parler de l'installation, je veux définir exactement ce que je veux dire par « livraison continue ».

### Livraison continue ou autre chose

Le terme Livraison Continue fait référence à la facilité, la rapidité et la rationalisation des mises en production. Nous pouvons discuter de la définition exacte du terme, mais rappelez-vous simplement que je suis un développeur front-end, donc mes yeux _peuvent_ se voiler. Je peux ronfler. Mais continuez. Je jure que j'écoute.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MquNEw7qIsb7l7ez_vdRMA.gif)

Pour nos besoins, « Livraison Continue » signifie que le processus de construction et de déploiement du site est entièrement automatisé. Voici à quoi cela ressemble dans la vraie vie :

* Le développeur envoie le code dans la branche master de Github
* Le serveur de build récupère le code depuis Github
* Le serveur de build exécute une build (script npm)
* Le serveur de build crée un conteneur Docker
* Le serveur de build envoie le conteneur Docker au registre
* Burke trouve la source de l'odeur de brocoli dans son bureau
* Le site web récupère le conteneur mis à jour

Vous avez tout compris ? En gros, nous allons automatiser tout ce que vous feriez normalement en tant que développeur, de sorte que l'envoi de code dans Github soit la seule chose dont vous devez vous soucier. Et Dieu sait que c'est [assez difficile comme ça](http://ohshitgit.com/).

%[https://twitter.com/TheLarkInn/status/990464006962982912?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fthelarkinn%2Fstatus%2F990464006962982912%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F923008231689003008%25252FChLxnzy9_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

D'accord, commençons par le début. La première chose que nous devons faire est de regarder l'application pour voir comment elle fonctionne. Et comment elle fonctionne est « Dans un Docker, les gars. »

### Exécuter Vue sur Docker

vscodecandothat.com est entièrement piloté par le front-end. C'est tout du HTML, JavaScript et CSS dans votre navigateur. Dans ce cas, tout ce que nous voulons faire est de servir la page `index.html` depuis le dossier _dist_. Nous utilisons un serveur web nginx.

Lorsque vous servez simplement des actifs statiques, le Dockerfile est très simple...

```
FROM nginx
WORKDIR /app
# Copier les actifs de build statiques
COPY dist/ /app/
# Copier le fichier de configuration nginx
COPY misc/nginx.conf /etc/nginx/nginx.conf
# Tous les fichiers sont en place, démarrer le serveur web
CMD ["nginx"]
```

Sarah a créé un fichier de configuration nginx que nous copions simplement lors de la construction du conteneur. Parce que vous ne voulez pas être dans le business de la configuration de nginx (OMG vous ne voulez pas), Sarah a posté son fichier de configuration [sur un gist](https://gist.github.com/sdras/2bfe545bb4df9a1a8e03b7ba73b086d5).

%[https://twitter.com/geddski/status/505082283917721600?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fgeddski%2Fstatus%2F505082283917721600%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F828768956727042048%25252Fnd_Weyq4_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

J'utilise l'[extension Docker pour VS Code](https://marketplace.visualstudio.com/items?itemName=PeterJausovec.vscode-docker&WT.mc_id=vscodecandothat-medium-buhollan) afin de pouvoir voir et gérer toutes mes images et conteneurs. Je n'ai pas peur du terminal, mais mon cerveau ne peut retenir qu'un certain nombre de flags.

![Image](https://cdn-media-1.freecodecamp.org/images/1*d6oT_mBMiy62By7DCMoRUA.png)

Maintenant, nous avons besoin d'un registre pour pousser le conteneur. Nous allons configurer [Azure Container Services](https://docs.microsoft.com/en-us/azure/container-registry/?WT.mc_id=vscodecandothat-medium-buhollan) (ACR) pour cela.

Vous pouvez créer un dépôt ACR depuis le portail web, mais pour prouver que je n'ai pas peur du terminal, nous allons le faire avec l'[Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest&WT.mc_id=vscodecandothat-medium-buhollan).

Tout d'abord, nous avons besoin d'un groupe pour les ressources. J'ai appelé le mien « vsCodeCanDoThat ».

```
az group create --name vsCodeCanDoThat --location eastus
```

Maintenant, créez le dépôt ACR. J'ai appelé le mien « hollandcr ».

```
az acr create --resource-group vsCodeCanDoThat --name hollandcr --sku Basic
```

Maintenant, nous pouvons pousser notre image en la taguant avec le chemin vers le registre de conteneurs Azure.

```
hollandcr.azurecr.io/vscodecandothat:latest
```

> [Dans la vidéo](https://content.screencast.com/users/burkeholland/folders/Snagit/media/fea2bf7c-bbc1-44de-9712-df5409242a1c/2018-05-02_15-14-44.mp4), vous pouvez me regarder me connecter au registre de conteneurs Azure depuis le terminal. C'est important car votre push échouera si vous n'êtes pas connecté.

D'accord — maintenant nous avons besoin d'un site pour héberger notre conteneur. Pour cela, nous utilisons Azure App Service.

### Création du App Service

Tout d'abord, créez un plan de service Linux. Pour cela, vous avez besoin du nom de votre application et de votre groupe de ressources.

Donc

```
az appservice plan create -n appName -g resourceGroupName --is-linux -l "South Central US" --sku S1 --number-of-workers 1
```

Devient

```
az appservice plan create -n vsCodeCanDoThatSP -g vsCodeCanDoThat --is-linux -l "South Central US" --sku S1 --number-of-workers 1
```

Maintenant, créez l'application web et pointez-la vers le conteneur qui a été poussé vers le registre AKS. Cela prend 4 paramètres.

* Plan de service
* Groupe de ressources
* Nom de l'application (que vous n'avez pas encore défini)
* Image Docker que vous avez poussée précédemment

```
az webapp create -n vsCodeCanDoThatSP -g vsCodeCanDoThatRG -p vscodecandothat -i hollandcr.azurecr.io/vscodecandothat:latest
```

Et c'est tout. Vous obtiendrez une URL en retour, et vous devriez pouvoir l'ouvrir et voir votre site en fonctionnement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hIRBA71rQYN48JtUx39t3A.png)

Maintenant, ce que nous voulons faire, c'est automatiser tout ce que nous venons de faire. Nous ne voulons plus jamais avoir à passer par l'une de ces étapes.

La première chose que nous allons faire est de configurer notre site pour le « Déploiement Continu » depuis notre registre de conteneurs.

Si vous utilisez l'extension App Service pour VS Code, tous vos sites Azure s'afficheront directement dans l'éditeur. Vous pouvez simplement faire un clic droit et dire « Ouvrir dans le Portail ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*YDEY6T-QBDuVYVz3eVVbAg.png)

Sélectionnez l'option de menu « Conteneur Docker »...

![Image](https://cdn-media-1.freecodecamp.org/images/1*LfVbCk3RokfybznGg2fC7Q.png)

Sur cette page, vous verrez le conteneur que vous avez configuré depuis le terminal. Il y a une option en bas pour activer le « Déploiement Continu ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*eUT84plmPQ6qbLN3qdobSA.png)

Lorsque vous activez cette option et cliquez sur « sauvegarder », un webhook sera créé dans votre registre de conteneurs Azure pour ce conteneur spécifique. Maintenant, chaque fois que l'image avec le tag « latest » est mise à jour, le webhook se déclenchera et notifiera App Service qui tirera automatiquement votre image.

Nous avons donc déjà automatisé une partie de cela. Une fois que nous poussons l'image, elle sera déployée. Il n'y a rien que nous devons faire à part la pousser. Mais nous ne voulons pas la pousser. Nous voulons que quelqu'un d'autre le fasse.

Et qui le fera ? Les robots, c'est qui. Ou qui ? OU QUI. Heureusement, je ne suis plus au lycée en anglais. Je l'ai échoué une fois et cela a suffi.

### Configuration d'un serveur de build

C'est à ce moment-là que je vous dis que nous allons utiliser [Visual Studio Team Services](https://www.visualstudio.com/team-services/?WT.mc_id=deployingvue-medium-buhollan&WT.mc_id=vscodecandothat-medium-buhollan) (VSTS). Ensuite, vous dites : « Visual Studio ? Je n'utilise pas .NET ». Et je dis : « Je sais, c'est confus. »

Nous avons besoin d'un système spécifiquement conçu pour automatiser les builds et les déploiements. C'est exactement ce que VSTS est/fait. De plus, il est gratuit pour 5 utilisateurs ou moins (dans un espace de projet) et « gratuit » est le seul mot dans mon langage d'amour. Le seul mot à part « bière ».

[Créez un compte VSTS](https://www.visualstudio.com/team-services/?WT.mc_id=vscodecandothat-medium-buhollan) si vous n'en avez pas. Une fois que vous l'avez fait, vous arrivez sur l'écran du tableau de bord.

À partir de là, vous voulez créer un nouveau projet d'équipe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DQSji2DhaqqWJTNPFNh2vg.png)

Donnez un nom et une description à votre projet que personne ne trouvera utile. Laissez le contrôle de version sur Git.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZVv_w22aLz66pa0Bgk_PPg.png)

L'écran suivant vous donne une URL Git pour envoyer votre code. Mais nous avons déjà Github, alors ignorez simplement cela et sélectionnez l'option « ou construire du code à partir d'un dépôt externe ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*gRKs17VBTOGkndVfF6nT4Q.png)

Autorisez VSTS à Github et sélectionnez le dépôt...

![Image](https://cdn-media-1.freecodecamp.org/images/1*mGMehWVxowKVx9Gw2YAwCQ.png)

L'écran suivant propose de vous aider à commencer avec un modèle. Dans ce cas, nous allons partir d'un processus vide. Parce que nous sommes hardcore comme ça.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Oj1YrEGKpNPqYdpN9sG0SQ.png)

Maintenant, nous allons commencer à ajouter des étapes pour que VSTS effectue la build et le déploiement. Le pull depuis le contrôle de source est déjà en cours, donc la première chose que nous devons faire est d'exécuter `npm install` sur notre code. Pour cela, ajoutez une tâche à la « phase 1 ». Il n'y a qu'une seule phase dans notre build / déploiement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xzQqzeSJmzD2SE-3Dtv3Bg.png)

Recherchez « npm » et ajoutez la tâche npm.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xpXq3R_ybbpEHT2qWNr4fQ.png)

Par défaut, vous obtenez la tâche `npm install`, ce qui est exactement ce que nous voulons. Vous n'avez pas besoin d'ajouter d'options à cette tâche.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ibpx3tqNj_obOO_JipQs2A.png)

Ensuite, nous allons exécuter la commande `npm run build`, qui va construire une instance de production de notre application Vue avec toute sa magie Webpack. Pour cela, ajoutez une autre tâche npm. Cette fois, changez le nom en « npm run build ». Définissez la « commande » sur « custom » et les « commande et arguments » sur « run build ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vmaq_Ap8qQKjHxyCyJZI5w.png)

Super ! Nous avons la build, maintenant nous sommes prêts à la Dockeriser. Ajoutez une nouvelle tâche et trouvez celle de « Docker ».

C'est un grand écran, donc voici l'image et ensuite nous allons passer en revue les points forts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CEdpDsdurnim2O8rk-HLig.png)

* Vous sélectionnez le « Azure Container Registry »
* Spécifiez votre abonnement Azure
* Spécifiez le nom de votre registre (que nous avons créé précédemment)
* Définissez le « Nom de l'image » sur $(Build.Repository.Name)
* Assurez-vous de cocher « Include Latest Tag »

Enfin, nous voulons pousser l'image. Ajoutez une autre tâche Docker. Cette fois, définissez l'« Action » sur « Push an image ». Définissez le « Nom de l'image » sur $(Build.Repository.Name) — exactement comme avant.

**NE SÉLECTIONNEZ PAS L'ACTION « PUSH IMAGES »**. Si vous le faites, votre build échouera et vous accuserez Dieu et toute l'humanité avant de réaliser que vous avez sélectionné la mauvaise action. Ne me demandez pas comment je le sais.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KMy6Gh269uDeHfZdBi2BFg.png)

Et c'est tout pour la définition de la build. Vous pouvez maintenant cliquer sur « sauvegarder et mettre en file d'attente » en haut. Assurez-vous de sélectionner un agent « Hosted Linux Preview ». Les tâches Docker nécessitent l'agent Linux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*13JqFhuyHXeLuJQBGnwcTg.png)

Maintenant, asseyez-vous et attendez qu'une build se lance. Si vous avez tout fait correctement, vous avez maintenant configuré un système de build et de déploiement entièrement automatisé pour une application Vue qui utilise Docker et Azure. C'est le plus de mots à la mode que j'ai jamais réussi à caser dans une seule phrase.

### Déployez et soyez heureux

Cela semble beaucoup à configurer, mais une fois que vous l'avez exactement comme vous le souhaitez, tout ce que vous avez à faire est d'envoyer du code dans votre dépôt Github et tout ce déploiement manuel ? se fait automatiquement. Vos clients vous aimeront. Vos développeurs vous aimeront. Diable — même VOUS pourriez vous aimer.

J'espère que vous trouverez cela utile. Je vais mettre à jour mon CV avec tous ces mots à la mode.