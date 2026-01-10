---
title: Comment créer une application monopage avec Vue.js, Vuex, Vuetify et Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T17:02:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-single-page-application-using-vue-js-vuex-vuetify-and-firebase-838b40721a07
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VDDEC608yRol_u0vPWTFeA.png
tags:
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: Comment créer une application monopage avec Vue.js, Vuex, Vuetify et Firebase
seo_desc: 'By Jennifer Bland

  How to install Vue and build an SPA using Vuetify and Vue Router


  Meal Prep application

  Do you want to learn how to use Vue.js? Want to create a realistic website using
  Vue.js? In this tutorial, I will teach you how to create a meal...'
---

Par Jennifer Bland

#### Comment installer Vue et créer une SPA avec Vuetify et Vue Router

![Image](https://cdn-media-1.freecodecamp.org/images/ILyG32WSBeAF7QsZth4PitrmS2KLY0ynVn6Q)
_Application de préparation de repas_

Vous voulez apprendre à utiliser Vue.js ? Vous voulez créer un site web réaliste avec Vue.js ? Dans ce tutoriel, je vais vous apprendre à créer un site web de livraison de repas en utilisant Vue, Vuex, Vue Router, Vuetify et Firebase.

Ce tutoriel est présenté sous forme d'une série d'articles qui vous guidera de l'installation de Vue pour la première fois à la création d'un site web de livraison de repas entièrement fonctionnel. L'image d'en-tête ci-dessus montre le site web que nous allons créer.

Ce tutoriel est divisé en une série de quatre parties. Voici les liens vers chaque partie de la série :

[Partie 1 : Installer Vue et créer une SPA avec Vuetify et Vue Router](https://medium.com/p/838b40721a07)

[Partie 2 : Utiliser Vue Router](https://medium.com/p/fc5bd065fe18)

[Partie 3 : Utiliser Vuex et accéder à l'API](https://medium.com/p/f8036aa464ad)

[Partie 4 : Utiliser Firebase pour l'authentification](https://medium.com/p/d9932d1e4365)

Ce tutoriel est adapté à tous, quel que soit votre niveau de compétence. Je suppose uniquement que vous avez des connaissances en ES6.

Commençons.

### Installation de Vue

La création d'une nouvelle application avec Vue.js se fait via leur interface de ligne de commande (CLI). Vous devrez d'abord installer le CLI avec cette commande :

```bash
npm install -g @vue/cli
```

Le drapeau -g indique à npm d'installer le CLI globalement. Une fois installé, le CLI peut être accessible en utilisant la commande `vue` dans le terminal. L'exécution de cette commande affichera les commandes disponibles :

![Image](https://cdn-media-1.freecodecamp.org/images/aof9G4eutveVpZNaCX1a5rEMHyylsMgzwWRl)
_Options de commande Vue._

**_NOTE:_** _Si vous avez lu d'autres articles sur Vue, vous pourriez voir qu'ils parlent d'une installation du CLI avec cette commande :_

```bash
npm install -g vue-cli
```

_Cela installait l'ancienne version du CLI Vue. Au moment de la rédaction de ce tutoriel, la version actuelle du CLI Vue est la version 3. Pour installer la dernière version, utilisez la première commande que j'ai donnée._

#### Création de notre application de préparation de repas

Maintenant que nous avons installé le CLI, l'étape suivante consiste à créer l'échafaudage de notre application Vue. Depuis votre terminal, entrez cette commande :

```bash
vue create meal-prep
```

Le CLI Vue posera une série de questions pour déterminer comment échafauder votre application. À la première invite, vous devez sélectionner « Manually select features ».

![Image](https://cdn-media-1.freecodecamp.org/images/ciV5iHwN6znhgK8Uh6HKxBKiAaoJke8RczfR)
_Sélection manuelle des fonctionnalités lors de la création de l'application Vue._

Ensuite, nous serons invités à sélectionner les fonctionnalités que nous voulons installer pour notre application. Pour ce tutoriel, sélectionnez Babel, Router, Vuex et Linter/Formatter.

![Image](https://cdn-media-1.freecodecamp.org/images/58j9tMl0DeMUb9NC6TACVbeoE5mhIDYAfLRh)
_Ajout de Babel, Router, Vuex et Linter à notre application_

Ensuite, vous serez invité à répondre à une série de questions.

Pour le linter, j'ai sélectionné _Prettier_ et j'ai choisi de _Lint on save_. J'ai sélectionné que les fichiers de configuration doivent être placés dans mon fichier package.json au lieu de fichiers de configuration séparés.

Voici les options que j'ai sélectionnées :

![Image](https://cdn-media-1.freecodecamp.org/images/zvHNgQ9SpZalEvDyl6mSM5E9oj7Ygd2a0CZg)
_Options sélectionnées pour l'application Vue_

Le CLI Vue échafaudera notre application en utilisant les fonctionnalités que vous avez sélectionnées. Comme je lui ai dit de créer une application nommée « meal-prep », il créera un nouveau dossier avec ce nom.

Une fois que le CLI a créé avec succès l'application, il vous donnera la commande pour changer dans le répertoire nouvellement créé et la commande que vous devrez exécuter pour démarrer votre application :

![Image](https://cdn-media-1.freecodecamp.org/images/qfITbx6hfhE3znFQV49F4GjtYEPEKioRFdah)
_Le CLI Vue a créé avec succès notre application._

#### Démarrage de notre application

Pour démarrer notre application, nous devrons nous rendre dans le répertoire meal-prep et exécuter la commande `npm run serve`. Voici à quoi ressemble notre application :

![Image](https://cdn-media-1.freecodecamp.org/images/bRNk-GcCDW-4lhpwg3wEjbE9NgfImcTEFMFj)
_Application Vue par défaut._

Vue a échafaudé une application SPA pour nous et installé Vue Router et Vuex. Nous pouvons voir le Vue Router en action en cliquant sur _About_ dans le menu en haut de la page. Cela charge la page _About_.

![Image](https://cdn-media-1.freecodecamp.org/images/JnFgQsKusfP7ewxM3PLWoF2FgGCEDeRd4w6x)
_Page À propos de notre application._

#### Ajout de Vuetify

Vuetify est un framework de composants de design matériel. Il est similaire à Bootstrap. Vuetify fournit 80+ composants de design matériel que nous pouvons utiliser pour styliser notre SPA dans Vue.

Pour ajouter Vuetify à notre application, allez d'abord dans votre terminal et arrêtez le serveur. Ensuite, ajoutez Vuetify à notre application avec cette commande :

```bash
vue add vuetify
```

Vous serez invité à répondre à une série de questions. Je vais choisir de ne pas utiliser le modèle pré-construit car je veux garder la structure créée par l'application Vue par défaut. Pour le reste des questions, j'ai pris les valeurs par défaut.

Voici mes réponses aux questions :

![Image](https://cdn-media-1.freecodecamp.org/images/Aaqh5ap3wIMuENDi2sScliXAuLb0iRydHlRg)
_Options sélectionnées lors de l'installation de Vuetify._

#### Configuration de Prettier

Lors de la création de notre application Vue, j'ai sélectionné l'utilisation de Prettier pour le linting. J'ai également sélectionné d'avoir les paramètres de configuration installés dans le fichier package.json. Je veux prendre le temps maintenant de configurer Prettier pour utiliser mes paramètres préférés.

Dans votre éditeur de code, ouvrez le fichier package.json. Dans ce fichier, vous verrez les paramètres par défaut qui ont été créés pour eslint. Juste après l'objet _eslintConfig_ et avant l'objet _postcss_, je vais ajouter des paramètres pour configurer Prettier. Je vais définir l'indentation à 4 espaces et utiliser des guillemets simples. (**Notes :** _si vous préférez une indentation de 2 espaces et/ou utiliser des guillemets doubles, vous n'avez pas besoin d'ajouter cette modification_.)

Voici le paramètre Prettier que j'ai ajouté à mon fichier package.json :

![Image](https://cdn-media-1.freecodecamp.org/images/A9MbIJc4qNkxoTCS6GMXEyd7uc2Ry9oxJ9e7)
_Configuration de Prettier dans le fichier package.json._

Ensuite, je veux reconfigurer tous les fichiers pour utiliser mes nouveaux paramètres Prettier. Cela signifie changer toutes les indentations de 2 espaces à 4 espaces et changer les guillemets doubles en guillemets simples. Heureusement, Vue fournit un script de lint qui corrige automatiquement tous ces problèmes pour moi.

Depuis le terminal, exécutez cette commande :

```bash
npm run lint
```

Cela lintera tous les fichiers et les changera selon mes nouveaux paramètres Prettier. Cette commande vous donnera une liste de tous les fichiers qui ont été corrigés automatiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/ngE7S1LqNnDFTMyJvb-tRzoHNl1vlz7UH-WK)
_Lint a corrigé automatiquement tous les fichiers pour nous._

#### Stylisation de la page d'accueil de notre application

Nous allons utiliser Vuetify pour styliser notre application. Vous pouvez trouver plus de détails sur tous les composants d'interface utilisateur que Vuetify offre [ici](https://vuetifyjs.com/en/).

Toutes les applications utilisant Vuetify doivent être enveloppées avec <v-app>. Ouvrez le fichier App.vue et supprimez tout le code dans le template et tous les styles. Votre App.vue devrait ressembler à ceci :

```js
<template>
    <v-app>
        <v-content transition="slide-x-transition">
            <router-view></router-view>
        </v-content>
    </v-app>
</template>

<script>
export default {
    name: 'App'
};
</script>

<style>
</style>
```

Ce code enveloppe notre application dans la balise <v-app> que Vuetify nécessite. À l'intérieur de cette balise se trouve la balise <v-content>. À l'intérieur se trouve la balise <router-view>. La balise router view affichera la page actuelle sur laquelle vous vous trouvez. Lorsque nous sommes sur la page d'accueil, elle affichera la vue d'accueil. Lorsque nous naviguons vers la page à propos, elle affichera la vue à propos.

### Création de la page d'accueil

Ouvrez ensuite le fichier Home.vue situé dans le dossier views. Nous allons nous débarrasser du code qui s'y trouve. Supprimez tout le contenu dans le template. Supprimez la commande d'importation pour HelloWorld et le commentaire. Supprimez l'objet components.

Voici ce que nous allons créer pour la page d'accueil :

![Image](https://cdn-media-1.freecodecamp.org/images/X25t5q8bwBy5k7WTjirjivD7gfFb8kLwdSHB)
_La page d'accueil pour l'application de préparation de repas_

#### Navigation de l'application

La première chose que nous allons commencer est la navigation. Je vais créer un nouveau composant Vue juste pour la navigation. Dans le dossier components, créez un nouveau fichier appelé `AppNavigation.vue`.

Notre navigation devra fonctionner sur de nombreuses tailles d'écran différentes. Sur les grands écrans comme un ordinateur portable ou un bureau, nous afficherons un menu en haut de l'écran. Sur les petits appareils comme un téléphone mobile, nous afficherons l'icône traditionnelle du menu hamburger. Lorsque l'utilisateur clique sur l'icône, un tiroir glisse depuis la gauche avec notre menu. Ce tiroir restera au-dessus du site web jusqu'à ce que l'utilisateur le ferme.

Vuetify fournit deux outils pour afficher le menu pour différentes tailles d'écran. Pour les écrans moyens et grands, nous utiliserons le composant <v-toolbar> de Vuetify. Sur les petits écrans, nous afficherons le composant <v-navigation-drawer>.

Commençons par échafauder la configuration par défaut pour un nouveau composant Vue. Le fichier AppNavigation.vue doit contenir le code suivant :

```js
<template>

</template>

<script>
export default {
    name: 'AppNavigation'
};
</script>

<style scoped>
</style>
```

Nous allons commencer par créer le menu qui sera affiché sur les écrans de taille moyenne et grande. Pour cela, nous utiliserons le composant <v-toolbar>. Voici le code que vous mettrez pour la navigation :

```js
<template>
        <v-toolbar app color="brown darken-4" dark>
            <v-toolbar-side-icon></v-toolbar-side-icon>
            <v-toolbar-title>{{appTitle}}</v-toolbar-title>
            <v-btn flat>Menu</v-btn>
            <v-spacer></v-spacer>
            <v-btn flat>SIGN IN</v-btn>
            <v-btn color="brown lighten-3">JOIN</v-btn>
        </v-toolbar>
</template>

<script>
export default {
    name: 'AppNavigation'
};
</script>

<style scoped>
</style>
```

Ce code produira ce menu :

![Image](https://cdn-media-1.freecodecamp.org/images/GPxzsgB0VM63DnrYN6QTI3IbanOOy0hZ7rib)
_Barre d'outils du menu_

Permettez-moi d'expliquer les éléments que j'ai utilisés dans le menu. Pour le <v-toolbar>, j'ai ajouté la `pr`op app. Cette prop désigne le composant comme faisant partie de la mise en page de l'application. Elle est utilisée pour ajuster dynamiquement la taille du contenu. Lorsque le tiroir latéral glisse, le contenu à l'écran s'ajustera en conséquence.

Ensuite, j'ai ajouté une couleur à la navigation. Vuetify fournit l'accès à toutes les couleurs de la spécification Material Design. Ces valeurs peuvent être utilisées dans vos feuilles de style, vos fichiers de composants et sur les composants réels via le système de **classe de couleur**. J'ai choisi une couleur marron pour la navigation avec la variante darken-4. [Voici toutes les couleurs disponibles avec Vuetify](https://vuetifyjs.com/en/style/colors).

Il existe un certain nombre de composants d'aide disponibles pour utiliser avec la barre d'outils. Un composant d'aide est l'icône latérale de la barre d'outils. C'est le menu hamburger. Je l'ai positionné en premier dans la barre d'outils.

Un autre composant d'aide est le titre de la barre d'outils. Je l'ai ajouté après l'icône latérale de la barre d'outils. J'affiche le appTitle qui est défini dans les données.

Ensuite, j'ai une série de boutons. Les boutons Vuetify utilisent le composant <v-btn>. Pour les trois premiers boutons, je spécifie une pr`op o`f flat. Les boutons plats n'ont pas d'ombre de boîte et pas d'arrière-plan. Seulement au survol, le conteneur du bouton est affiché. Cela me permet de créer des boutons qui imitent l'apparence et la sensation d'un menu traditionnel.

Pour le bouton _JOIN_, je n'utilise pas la prop flat. J'ajoute une couleur au bouton.

La dernière chose que j'ai faite sur le <v-toolbar> est d'ajouter la `pro`p dark. Cette prop applique la variante de thème sombre à la barre d'outils. Cela inverse tout le texte pour qu'au lieu d'être noir, ils soient maintenant blancs.

#### Amélioration du style dans la navigation

La première implémentation de la navigation fournit toutes les fonctionnalités que je souhaite avoir. Mais je souhaite apporter quelques modifications. Tout d'abord, je ne veux pas que le menu hamburger soit affiché sauf si je suis sur un petit appareil. De même, je ne veux pas qu'un bouton du menu soit affiché lorsque je suis sur un petit appareil.

Vuetify fournit un helper d'affichage. Les helpers d'affichage vous permettent de contrôler l'affichage du contenu. Cela inclut le fait d'être conditionnellement visible en fonction de la fenêtre d'affichage actuelle ou du type d'affichage réel de l'élément.

Pour l'icône latérale de la barre d'outils, je veux qu'elle soit visible uniquement sur les appareils XS et SM. Pour les écrans MD et LG, je ne veux pas que l'icône latérale de la barre d'outils soit visible. De même, je veux que tous les boutons soient affichés sur les écrans MD et LG et masqués sur les petits écrans.

Je vais ajouter la classe `hidden-md-and-up` sur l'icône latérale de la barre d'outils. Je vais ajouter la classe `hidden-sm-and-down` à tous les boutons et à l'espaceur.

Maintenant, je vais être un peu pointilleux ici car je veux ajouter un autre changement de mise en page. Lorsque j'affiche l'application sur de petits appareils, je ne verrai que le menu hamburger et le titre de l'application. Actuellement, ils sont tous les deux du côté gauche de l'écran. Je veux changer cela pour que le titre de l'application apparaisse du côté droit de l'écran. Cela fournira un équilibre entre les deux éléments qui sont affichés.

Pour ce faire, je vais ajouter un nouvel <v-spacer> entre l'icône latérale de la barre d'outils et le titre de la barre d'outils. L'espaceur déplacera tout ce qui suit vers le côté droit de l'écran. Mais je veux que cet espaceur n'apparaisse que sur les petits écrans. Je lui ajoute donc la classe `hidden-md-and-up`.

Voici le code final :

```js
<v-toolbar app color="brown darken-4" dark>
    <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>
    <v-spacer class="hidden-md-and-up"></v-spacer>
    <v-toolbar-title>{{appTitle}}</v-toolbar-title>
    <v-btn flat class="hidden-sm-and-down">Menu</v-btn>
    <v-spacer class="hidden-sm-and-down"></v-spacer>
    <v-btn flat class="hidden-sm-and-down">SIGN IN</v-btn>
    <v-btn color="brown lighten-3" class="hidden-sm-and-down">JOIN</v-btn>
</v-toolbar>
```

Si vous voulez voir à quoi cela ressemble lorsque vous redimensionnez l'écran, voici le premier giphy que j'ai jamais créé. :-)

![Image](https://cdn-media-1.freecodecamp.org/images/zeJ5FhZpMNo0mRVXFmtpwNzohBk4G29TMnnP)
_Le redimensionnement de l'écran change ce qui est affiché._

#### Création de la navigation pour les petits écrans

Pour les petits écrans, nous utiliserons le composant <v-navigation-drawer> de Vuetify. Si nous ajoutons cela au template, nous obtiendrons immédiatement une erreur. Cela est dû au fait que chaque composant Vue est censé avoir une seule racine dans le template. En ayant à la fois un <v-navigation-drawer> et un <v-toolbar> dans notre template, nous avons deux racines. Pour éviter cela, créez une balise <span> pour envelopper les deux.

Voici le code pour le tiroir de navigation :

```js
<template>
    <span>
        <v-navigation-drawer app v-model="drawer" class="brown lighten-2" dark disable-resize-watcher>
            <v-list>
                <template v-for="(item, index) in items">
                    <v-list-tile :key="index">
                        <v-list-tile-content>
                            {{item.title}}
                        </v-list-tile-content>
                    </v-list-tile>
                    <v-divider :key="`divider-${index}`"></v-divider>
                </template>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar app color="brown darken-4" dark>
            <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>
            <v-spacer class="hidden-md-and-up"></v-spacer>
            <v-toolbar-title>{{appTitle}}</v-toolbar-title>
            <v-btn flat class="hidden-sm-and-down">Menu</v-btn>
            <v-spacer class="hidden-sm-and-down"></v-spacer>
            <v-btn flat class="hidden-sm-and-down">SIGN IN</v-btn>
            <v-btn color="brown lighten-3" class="hidden-sm-and-down">JOIN</v-btn>
        </v-toolbar>
    </span>
</template>

<script>
export default {
    name: 'AppNavigation',
    data() {
        return {
            appTitle: 'Meal Prep',
            drawer: false,
            items: [
                { title: 'Menu' },
                { title: 'Sign In' },
                { title: 'Join' }
            ]
        };
    }
};
</script>

<style scoped>
</style>
```

Permettez-moi d'expliquer ce que j'ai mis pour la navigation du tiroir. J'ai ajouté la prop `app`. C'est la même prop que nous avons ajoutée pour la barre d'outils. Ensuite, j'ai ajouté un v-model qui recherche l'élément de données appelé drawer. Dans les données, drawer sera initialement défini sur `false`. Cela signifie que le tiroir est fermé. Le tiroir s'ouvrira lorsqu'il sera vrai et se fermera lorsqu'il sera faux. J'ai ajouté une méthode de clic sur l'icône latérale de la barre d'outils. Lorsque vous cliquez sur le menu hamburger, il changera la valeur de drawer de vrai à faux ou vice versa.

Le dernier élément que j'ai ajouté est de lui donner une classe avec une couleur de `brown lighten-2`. J'ai décidé d'ajouter une couleur à mon tiroir puisque la couleur par défaut est blanche.

Ensuite, j'utilise le composant <v-list> de Vuetify. Dans les données, j'ai créé un tableau appelé items. Il s'agit d'un tableau d'objets. Chaque objet a une clé de texte et la valeur est ce qui est affiché dans le menu. J'utilise un élément de données au lieu de coder en dur les éléments du menu dans la liste car nous l'utiliserons dans les séries ultérieures lorsque nous ajouterons l'authentification.

Dans les données, j'ai ajouté drawer et items :

```js
export default {
    name: 'AppNavigation',
    data() {
        return {
            appTitle: 'Meal Prep',
            drawer: false,
            items: [
                { title: 'Menu' },
                { title: 'Sign In' },
                { title: 'Join' }
            ]
        };
    }
};
```

Lorsque nous cliquons sur le menu hamburger, voici à quoi ressemblera le tiroir :

![Image](https://cdn-media-1.freecodecamp.org/images/Bi0wsYflMENihqL5XUFuZDW7h-yIEvZgOBKl)
_Navigation du tiroir pour les petits appareils_

#### Ajout de la navigation à l'application

Maintenant que nous avons créé notre composant AppNavigation, nous devons l'ajouter à notre application. Ouvrez le fichier `App.vue`. Dans ce fichier, nous devrons importer notre composant AppNavigation. Ensuite, nous pouvons le placer dans notre application.

Voici le code que vous devriez avoir dans votre fichier App.vue :

```js
<template>
    <v-app>
        <app-navigation></app-navigation>

        <v-content transition="slide-x-transition">
            <router-view></router-view>
        </v-content>
    </v-app>
</template>

<script>
import AppNavigation from '@/components/AppNavigation';

export default {
    name: 'App',
    components: {
        AppNavigation
    }
};
</script>

<style>
</style>
```

Tout d'abord, vous devez importer AppNavigation. Lorsque je l'importe, je lui donne un nom de AppNavigation. Dans le script, j'ai ajouté un objet components qui contient AppNavigation. Le format du nom est important. Lorsque le composant est ajouté, il hyphénera le nom. Lorsque je place le composant dans le template html, j'utilise le nom hyphéné de <app-navigation>.

**NOTE :** _si vous regardez le code de près, vous remarquerez que j'ai supprimé la balise <transition> et l'ai placée directement sur la balise <v-content>. Je voulais juste vous faire savoir que j'ai apporté cette modification puisque je ne voulais vraiment pas revenir en arrière et mettre à jour toutes les images !_

#### Création du contenu de notre page d'accueil

Nous allons ajouter une image plein écran pour notre page d'accueil. Ensuite, nous allons ajouter du texte sur l'image. Au lieu de mettre notre code directement dans le fichier Home.vue situé dans le dossier views, je vais créer un nouveau composant Vue. Dans le dossier components, créez un nouveau fichier appelé HomeHero.vue.

Vuetify dispose d'un système de grille à 12 points. Construit en utilisant flex-box, la grille est utilisée pour disposer le contenu d'une application. Le `**v-container**` peut être utilisé pour une page centrée, ou donné la `**fluid**` prop pour étendre sa largeur complète. `**v-layout**` est utilisé pour séparer les sections. La structure de votre mise en page sera la suivante, **v-container**  **v-layout**  **v-flex**.

Nous allons utiliser ce système de grille dans la conception de notre composant HomeHero. Nous allons utiliser <v-container fluid> pour notre élément racine dans notre template. Nous allons ajouter la `prop fill-`height. Cette prop ajustera automatiquement le conteneur pour qu'il ait une hauteur de 100 % de l'écran. La dernière chose que je fais est d'ajouter une classe appelée hom`e-hero.

Dans mes styles, je vais ajouter une image de fond au conteneur. C'est l'image plein écran que les utilisateurs verront lors du chargement du site web. J'utilise une image de unsplash.com.

À l'intérieur du conteneur, j'aurai un <v-layout>. La mise en page enveloppera tout le texte affiché sur l'image. Vuetify fournit des paramètres de typographie que je vais utiliser pour styliser le texte. Pour le texte principal, je lui donne une

`class="display-4 font-weight-black white--text"`

Le display-4 produira un texte avec une taille de police de 112sp et un poids de police léger. Je vais remplacer ce font-weight en spécifiant un font-weight-black. Je veux que le texte soit blanc, donc je peux ajouter `white--text`. La dernière chose que j'ajoute est de spécifier que le texte doit être centré.

J'utiliserai le même style pour la deuxième ligne de texte. La seule addition est que j'ajoute un alignement de `mb-3`. Vuetify fournit 5 niveaux d'espacement. Le mb signifie appliquer une marge inférieure de 3. Cela fournira un certain espacement entre l'en-tête et le texte subHeader.

La dernière chose que j'ajoute est un bouton vers le bas de l'écran. Je l'ajoute parce que parfois les gens pourraient ne pas penser à faire défiler vers le bas pour voir plus de contenu puisque l'image est en plein écran. L'image est un indicateur visuel pour les utilisateurs qu'il y a plus de contenu en dessous.

J'utilise le composant <v-btn> de Vuetify. C'est le même composant que nous avons utilisé dans la navigation. Cette fois, j'applique la `pr`op fab au bouton. Les boutons flottants sont ronds et contiennent généralement une icône. Je vais ajouter une icône de flèche vers le bas. Le composant <v-icon> vous demande d'entrer le nom de l'icône à afficher. Voici une liste de toutes les icônes matérielles disponibles pour vous à utiliser avec Vuetify.

Pour le bouton, je vais ajouter une classe qui mettra une marge supérieure de 5 et définira la couleur pour qu'elle soit la même couleur marron que j'ai utilisée pour le menu. Pour l'icône, je définis sa couleur pour qu'elle soit blanche. J'ai également défini l'icône pour qu'elle soit grande.

Voici le code pour le fichier HomeHero :

```js
<template>
    <v-container fluid fill-height class="home-hero">
        <v-layout justify-center align-center column pa-5>
            <div class="display-4 font-weight-black white--text text-xs-center">REPAS SAINS</div>
            <div class="display-4 font-weight-black white--text text-xs-center mb-3">POUR VOTRE TABLE</div>
            <div class="display-1 font-weight-bold white--text text-xs-center">Enfin, soyez un foodie à la maison avec des repas frais, préparés par un chef, livrés quotidiennement à votre porte.</div>
            <v-btn fab class="mt-5 brown darken-4">
            <v-icon large color="white">expand_more</v-icon>
            </v-btn>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    name: 'HomeHero'
};
</script>

<style scoped>
.home-hero {
    background: url('http://source.unsplash.com/0BhSKStVtdM');
    background-size: cover;
    width: 100%;
    height: 100%;
}
</style>
```

#### Ajout du composant HomeHero à l'application

Maintenant que nous avons créé notre composant, nous devons l'ajouter à l'application. Ouvrez le fichier Home.vue dans le dossier views. Tout comme nous l'avons fait avec AppNavigation, vous devrez importer le composant et le placer dans le template. Voici à quoi devrait ressembler le fichier Home.vue :

```js
<template>
    <span>
        <home-hero></home-hero>
    </span>
</template>

<script>
import HomeHero from '@/components/HomeHero';

export default {
    name: 'home',
    components: {
        HomeHero
    }
};
</script>
```

#### Ajout de plus de contenu à la page d'accueil

Actuellement, nous avons une très belle page d'accueil. Mais nous devons ajouter plus de contenu pour expliquer ce que notre service de préparation de repas offre aux clients potentiels. Ajoutons cela maintenant.

Pour le contenu, nous allons créer un nouveau composant appelé HomeDetails.vue. Dans le dossier components, créez un nouveau fichier appelé HomeDetails.vue. Pour le contenu, je vais utiliser Lorem Ipsum pour le texte.

Je vais utiliser le schéma de mise en page Vuetify en créant l'élément racine avec le composant <v-container>. À l'intérieur, j'utiliserai le composant <v-layout>. Pour la mise en page, j'ajouterai `the pr`op de column. Comme la mise en page est basée sur Flexbox, elle alignera tout le contenu verticalement. Chaque élément de texte sera dans un composant <v-flex>.

L'en-tête utilisera la classe de typographie Vuetify `display-2`. Je veux que ce texte soit centré. Pour le centrer, j'ajoute `text-xs-center` à la classe. La dernière chose à ajouter est `my-5`. Cela ajoute une marge le long de l'axe y, ce qui signifie qu'il ajoute une marge supérieure et une marge inférieure.

Ensuite, je vais créer une autre entrée <v-flex>. Cette entrée aura un titre et un sous-titre de texte. Je veux ajouter un peu d'espace blanc autour du texte, donc j'ajoute une classe `mt-3`. Cela ajoutera une marge supérieure de 3 à tous les éléments de texte.

Voici mon fichier HomeDetails.vue :

```js
<template>
    <v-container>
        <v-layout column>
            <v-flex  class="display-2 text-xs-center my-5">Grand titre ici</v-flex>
            <v-flex>
                <div class="headline mt-3">Lorem ipsum</div>
                <p class="subheading mt-3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras pulvinar risus quis mauris interdum, in euismod nibh pretium. Etiam pulvinar tincidunt dapibus. Quisque sollicitudin, mauris a consequat consectetur, turpis nisl sollicitudin enim, id consectetur neque neque nec metus. Pellentesque dolor nisi, vulputate quis lobortis ac, tincidunt et quam. Mauris pulvinar blandit nisi nec mattis. Aliquam accumsan ut sem eget efficitur. Vivamus in tortor gravida eros laoreet condimentum nec vel dui. Nullam quam massa, ultrices eget tincidunt a, pulvinar ac libero.</p>
            </v-flex>
            <v-flex>
                <div class="headline mt-3">Lorem ipsum</div>
                <p class="subheading mt-3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras pulvinar risus quis mauris interdum, in euismod nibh pretium. Etiam pulvinar tincidunt dapibus. Quisque sollicitudin, mauris a consequat consectetur, turpis nisl sollicitudin enim, id consectetur neque neque nec metus. Pellentesque dolor nisi, vulputate quis lobortis ac, tincidunt et quam. Mauris pulvinar blandit nisi nec mattis. Aliquam accumsan ut sem eget efficitur. Vivamus in tortor gravida eros laoreet condimentum nec vel dui. Nullam quam massa, ultrices eget tincidunt a, pulvinar ac libero.</p>

                <p class="subheading mt-3">Nullam nec massa eu est fringilla lobortis. Praesent in enim in justo blandit varius. Cras placerat arcu in sapien rhoncus aliquet. Sed interdum tortor et tincidunt condimentum. Etiam consequat mi leo, in suscipit odio scelerisque molestie. Nam et purus consequat, iaculis augue vel, sagittis ligula. Vestibulum aliquet vulputate erat. Phasellus id mauris mauris. Nunc a maximus dolor. Curabitur ut vestibulum arcu. Curabitur non lacus justo. Cras varius a magna in semper. Nulla eros ante, consectetur faucibus sapien eu, rhoncus imperdiet dui. Sed viverra iaculis nunc, id pulvinar massa egestas vitae.</p>

                <p class="subheading mt-3">Aenean erat metus, imperdiet eget nisl laoreet, venenatis ultricies ante. In interdum ante vel dictum ullamcorper. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer sit amet gravida diam. Aliquam in tempor metus. Fusce pellentesque pharetra sem, et luctus justo tempor dictum. Ut feugiat est sed tristique egestas. Nullam posuere a nunc in blandit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Suspendisse laoreet ultrices eros, nec malesuada enim semper sit amet. Maecenas efficitur consectetur accumsan. Etiam in aliquam turpis, ut pharetra nulla. Vestibulum malesuada, nulla id elementum cursus, nibh dui rhoncus felis, suscipit mattis felis enim sed ex. Pellentesque scelerisque aliquam lorem, vel mattis nibh tincidunt ac. Suspendisse ac nibh sit amet lacus ullamcorper maximus.</p>
            </v-flex>
            <v-flex>
                <div class="headline mt-3">Lorem ipsum</div>
                <p class="subheading mt-3">Nullam nec massa eu est fringilla lobortis. Praesent in enim in justo blandit varius. Cras placerat arcu in sapien rhoncus aliquet. Sed interdum tortor et tincidunt condimentum. Etiam consequat mi leo, in suscipit odio scelerisque molestie. Nam et purus consequat, iaculis augue vel, sagittis ligula. Vestibulum aliquet vulputate erat. Phasellus id mauris mauris. Nunc a maximus dolor. Curabitur ut vestibulum arcu. Curabitur non lacus justo. Cras varius a magna in semper. Nulla eros ante, consectetur faucibus sapien eu, rhoncus imperdiet dui. Sed viverra iaculis nunc, id pulvinar massa egestas vitae.</p>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    name: 'HomeDetails'
};
</script>

<style scoped>
</style>
```

#### Ajout de HomeDetails à l'application

Nous allons ajouter HomeDetails à l'application comme nous l'avons fait pour HomeHero. Ouvrez le fichier Home.vue dans le dossier views. Vous devrez importer le composant HomeDetails. Ensuite, ajoutez-le au template en dessous de HomeHero.

Voici à quoi ressemble le fichier Home.vue :

```js
<template>
    <span>
        <home-hero></home-hero>
        <home-details></home-details>
    </span>
</template>

<script>
import HomeHero from '@/components/HomeHero';
import HomeDetails from '@/components/HomeDetails';

export default {
    name: 'home',
    components: {
        HomeHero,
        HomeDetails
    }
};
</script>
```

Lorsque nous ajoutons ce nouveau composant, cela pose un problème avec notre mise en page. Maintenant, le texte est centré en fonction de la hauteur totale de l'image ainsi que du nouveau contenu textuel. Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/miBJB8CzWKJA4L7-p9Xy8p6TzkBWS2jL5f0-)
_Problèmes avec notre mise en page._

Nous pouvons facilement corriger ce problème en spécifiant une hauteur maximale pour le conteneur qui contient notre image. Nous voulons que ce conteneur soit à 100 % de la hauteur de notre viewport.

Ouvrez le fichier HomeHero.vue. Sur le composant <v-container>, ajoutez un style qui définit la hauteur maximale. Voici cette ligne :

```js
<v-container fluid fill-height class="home-hero" style="max-height: 100vh;">
```

Maintenant, nous avons une image plein écran avec notre texte centré sur l'image. Nous pouvons ensuite faire défiler vers le bas pour voir les détails.

#### Création du composant des plans de repas

Après les détails, je veux ajouter des images des plans de repas que nous proposons sur notre site web de préparation de repas. Pour mon site web de préparation de repas, je proposerai des plans de repas Keto, Paléo et Vegan. N'hésitez pas à personnaliser votre application pour offrir les plans de repas que vous souhaitez proposer à vos clients.

Créons un nouveau composant. Dans le dossier components, créez un nouveau fichier appelé HomePlans.vue. Nous allons utiliser la mise en page de la grille Vuetify. Notre élément racine sera un `<v-container>`. Nous allons ajouter une nouvelle prop `grid-list-lg`. Nous aurons trois plans de repas côte à côte. Cette prop met de l'espace entre eux.

Ensuite, nous avons un `<v-layout>` pour notre texte d'en-tête annonçant nos plans de repas disponibles. Nous allons utiliser un nouveau composant Vuetify appelé `<v-card>`. Notre carte aura une image, le nom du plan de repas et un texte de détail. Je vais utiliser des images de unsplash pour chacun des plans de repas.

Voici le code pour le fichier `HomePlans.vue` :

```js
<template>
    <v-container grid-list-lg>
        <v-layout row>
            <v-flex xs12 class="text-xs-center display-1 font-weight-black my-5">Plans de repas disponibles</v-flex>
        </v-layout>
        <v-layout row wrap>
            <v-flex xs12 sm12 md4>
                <v-card>
                    <v-img src="http://source.unsplash.com/hjCA3ecCXAQ" height="500px">
                        <v-container fill-height fluid>
                            <v-layout fill-height>
                                <v-flex xs12 align-end flexbox>
                                    <span class="headline white--text">KETO</span>
                                </v-flex>
                            </v-layout>
                        </v-container>
                    </v-img>

                    <v-card-title primary-title>
                        <div>
                            <h3 class="headline mb-0">Keto</h3>
                            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam mauris felis, varius rutrum massa a, dignissim ornare dui. Cras eget velit eu dui tristique lobortis sit amet vel tellus.
                            </div>
                        </div>
                    </v-card-title>
                </v-card>
            </v-flex>

            <v-flex xs12 sm12 md4>
                <v-card>
                    <v-img src="http://source.unsplash.com/6S27S6pZ6o0" height="500px">
                        <v-container fill-height fluid>
                            <v-layout fill-height>
                                <v-flex xs12 align-end flexbox>
                                    <span class="headline white--text">PALEO</span>
                                </v-flex>
                            </v-layout>
                        </v-container>
                    </v-img>
                    <v-card-title primary-title>
                        <div>
                            <h3 class="headline mb-0">Paleo</h3>
                            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam mauris felis, varius rutrum massa a, dignissim ornare dui. Cras eget velit eu dui tristique lobortis sit amet vel tellus.
                            </div>
                        </div>
                    </v-card-title>
                </v-card>
            </v-flex>

            <v-flex xs12 sm12 md4>
                <v-card>
                    <v-img src="http://source.unsplash.com/1SPu0KT-Ejg" height="500px">
                        <v-container fill-height fluid>
                            <v-layout fill-height>
                                <v-flex xs12 align-end flexbox>
                                    <span class="headline white--text">VEGAN</span>
                                </v-flex>
                            </v-layout>
                        </v-container>
                    </v-img>
                    <v-card-title primary-title>
                        <div>
                            <h3 class="headline mb-0">Vegan</h3>
                            <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam mauris felis, varius rutrum massa a, dignissim ornare dui. Cras eget velit eu dui tristique lobortis sit amet vel tellus.
                            </div>
                        </div>
                    </v-card-title>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
export default {
    name: 'HomePlans'
};
</script>

<style scoped>
</style>
```

#### Ajout de HomePlans à l'application

Nous avons déjà fait cela plusieurs fois. Ouvrez le fichier Home.vue dans le dossier views. Importez le composant HomePlans.vue et placez-le dans le template en dessous de HomeDetails.

Voici le code pour Home.vue :

```js
<template>
    <span>
        <home-hero></home-hero>
        <home-details></home-details>
        <home-plans></home-plans>
    </span>
</template>

<script>
import HomeHero from '@/components/HomeHero';
import HomeDetails from '@/components/HomeDetails';
import HomePlans from '@/components/HomePlans';

export default {
    name: 'home',
    components: {
        HomeHero,
        HomeDetails,
        HomePlans
    }
};
</script>
```

Voici à quoi ressemble la section des plans de repas :

![Image](https://cdn-media-1.freecodecamp.org/images/Nt34q1yb5VIPQxNdZ3p3qpmwPyQQ4y1B6cTL)
_Plans de repas disponibles._

### Obtenez le code

Bien que ce soit une série en 4 parties, vous pouvez obtenir le [code final dans mon compte GitHub.](https://github.com/ratracegrad/meal-prep) Aidez-moi et **étoilez le dépôt** lorsque vous obtenez le code.

### Résumé

Dans la première partie de cette série, vous avez appris :

* comment installer Vue
* comment ajouter Vuetify à une application
* comment créer plusieurs composants
* comment styliser des composants en utilisant Vuetify

#### Qu'est-ce qui suit

Dans la prochaine partie de cette série, nous aborderons Vue Router. Vue Router vous permet de naviguer entre différentes pages de votre application. Par exemple, nous affichons une liste de menus disponibles. Lorsque l'utilisateur clique sur l'un d'eux, il doit voir les détails de ce menu. Vue Router est ce que nous utiliserons pour passer de la page de la liste des recettes à la page des détails. À la prochaine leçon.

Si vous avez aimé cet article, applaudissez-le. Si vous pensez que quelqu'un d'autre pourrait bénéficier de cet article, partagez-le avec lui.

Si vous avez des questions ou si vous trouvez quelque chose qui ne va pas avec le code, laissez un commentaire. Si vous avez d'autres sujets que vous aimeriez que j'aborde, laissez un commentaire.

#### Plus d'articles

Voici d'autres articles que j'ai écrits et que vous pourriez vouloir lire !

[**Il y a trois ans, j'ai participé à un bootcamp de codage. Aujourd'hui, je suis devenu un Google Developer Advocate.**  
_C'est l'histoire de mon parcours et comment j'y suis arrivé_](https://www.freecodecamp.org/news/three-years-ago-i-attended-a-coding-bootcamp-today-i-became-a-google-developer-advocate-b89fae03d476/)

[**Comment ajouter l'internationalisation à une application Vue**  
_Hola! Bonjour. Ciao. Vous êtes bien. Voici comment vous ajoutez l'internationalisation à Vue._](https://www.freecodecamp.org/news/how-to-add-internationalization-to-a-vue-application-d9cfdcabb03b/)

[**Comment programmer une calculatrice avec jQuery**  
_Auparavant, je vous ai montré comment utiliser la propriété CSS border-radius pour créer la calculatrice suivante. Maintenant, je vais vous montrer..._](https://www.freecodecamp.org/news/programming-a-calculator-8263966a8019/)

[**Suivez-moi sur Twitter !**](https://twitter.com/ratracegrad)