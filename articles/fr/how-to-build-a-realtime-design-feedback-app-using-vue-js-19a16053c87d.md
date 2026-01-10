---
title: Comment créer une application de feedback de design en temps réel avec Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-28T23:41:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-realtime-design-feedback-app-using-vue-js-19a16053c87d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VIqC81gGioRMRpnoi5_bLw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de feedback de design en temps réel avec
  Vue.js
seo_desc: 'By Neo Ighodaro

  A basic understanding of Laravel and Vue.js is needed to follow this tutorial.

  Companies like Invision have built applications that designers use to get feedback
  from other people. A designer can simply load the application, upload th...'
---

Par Neo Ighodaro

Une compréhension de base de Laravel et Vue.js est nécessaire pour suivre ce tutoriel.

Des entreprises comme [Invision](https://www.invisionapp.com/lp/signup-1?utm_source=google&utm_medium=paid_search&utm_campaign=DG_SS_G_NAM_Search_Brand_BMM&utm_content=InVision_BMM&utm_term=%2Binvision_b&_bk=%2Binvision&_bt=253209933326&_bm=b&_bn=g&gclid=EAIaIQobChMI_Kq1p5He2gIVj1mGCh2eJgaSEAAYASAAEgL7BPD_BwE) ont créé des applications que les designers utilisent pour obtenir des feedbacks de la part d'autres personnes. Un designer peut simplement charger l'application, téléverser ses designs et envoyer le lien aux personnes qui laisseront des feedbacks. Ensuite, ces personnes peuvent laisser leurs feedbacks sur différentes parties du design. C'est bien pour le designer, car il peut voir ces feedbacks et agir en conséquence immédiatement.

Dans cet article, nous allons créer une application similaire de feedback de design. Cela vous permettra de téléverser des images, d'envoyer le lien à quelqu'un d'autre et de recevoir ses feedbacks sur votre design en temps réel.

Voici un enregistrement d'écran de ce que notre application sera capable de faire :

![Image](https://cdn-media-1.freecodecamp.org/images/wPZLpxfcpOXa9Cm8u7ZUSRQYngaXLxgaUSbU)

### Exigences pour construire notre application

Avant de commencer, nous devons avoir quelques éléments en place. Les exigences sont les suivantes :

* Connaissance de PHP et du framework [Laravel](https://laravel.com).
* Connaissance de JavaScript (ES6).
* Connaissance de Vue.js.
* PHP 7.0+ installé localement sur votre machine.
* [Laravel CLI](https://laravel.com/docs/5.5/installation#installing-laravel) installé localement.
* [Composer](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-osx) installé localement.
* [NPM](https://docs.npmjs.com/cli/install) et Node.js installés localement.
* Une application Pusher. Créez-en une sur [pusher.com](https://pusher.com).

Une fois que vous avez vérifié que vous avez les exigences ci-dessus, nous pouvons commencer à créer notre application.

### Configuration de notre application prototype de feedback

Commençons par configurer notre application. Créez une nouvelle application Laravel en utilisant la commande ci-dessous :

```
$ laravel new votre_nom_d_application
```

Lorsque l'installation est terminée, `cd` dans le répertoire de l'application. Ouvrez le fichier `.env` afin que nous puissions apporter quelques modifications au fichier.

#### Configuration de notre base de données et des migrations

La première chose à faire est de configurer notre base de données et de créer ses migrations. Commençons par configurer la base de données. Remplacez les éléments de configuration ci-dessous :

```
DB_CONNECTION=mysqlDB_HOST=127.0.0.1DB_PORT=3306DB_DATABASE=homesteadDB_USERNAME=homesteadDB_PASSWORD=secret
```

par :

```
DB_CONNECTION=sqlite
```

Cela fera maintenant en sorte que l'application utilise SQLite comme choix de base de données. Dans votre terminal, exécutez la commande ci-dessous pour créer une nouvelle base de données SQLite :

```
$ touch database/database.sqlite
```

Maintenant, nous allons créer quelques migrations qui créeront les tables requises dans la base de données. Dans votre terminal, exécutez la commande suivante pour créer les migrations dont nous aurons besoin :

```
$ php artisan make:model Photo --migration --controller$ php artisan make:model PhotoComment --migration
```

La commande ci-dessus créera un modèle, puis les indicateurs `--migration` et `--controller` lui indiqueront de créer une migration et un contrôleur en même temps que le modèle.

Pour l'instant, nous nous intéressons au Modèle et à la migration. Ouvrez les deux fichiers de migration créés dans le répertoire `./database/migrations`. Modifiez d'abord la classe `CreatePhotosTable`. Remplacez le contenu de la méthode `up` par ce qui suit :

```
public function up(){    Schema::create('photos', function (Blueprint $table) {        $table->increments('id');        $table->string('url')->unique();        $table->string('image')->unique();        $table->timestamps();    });}
```

Cela créera la table `photos` lorsque les migrations seront exécutées à l'aide de la commande artisan. Cela créera également de nouvelles colonnes à l'intérieur de la table comme spécifié ci-dessus.

Ouvrez la deuxième classe de migration, `CreatePhotoCommentsTable`, et remplacez la méthode `up` par le contenu ci-dessous :

```
public function up(){    Schema::create('photo_comments', function (Blueprint $table) {        $table->increments('id');        $table->unsignedInteger('photo_id');        $table->text('comment');        $table->integer('top')->default(0);        $table->integer('left')->default(0);        $table->timestamps();
```

```
        $table->foreign('photo_id')->references('id')->on('photos');    });}
```

Cela créera la table `photo_comments` lorsque la migration sera exécutée, et créera également une clé étrangère vers la table `photos`.

Maintenant, allez dans votre terminal et exécutez la commande ci-dessous pour exécuter les migrations :

```
$ php artisan migrate
```

Cela devrait maintenant créer les tables de la base de données.

#### Configuration des modèles

Maintenant que nous avons exécuté nos migrations, nous devons apporter quelques modifications à notre fichier de modèle afin qu'il puisse mieux fonctionner avec la table.

Ouvrez le modèle `Photo` et remplacez le contenu par ce qui suit :

```
<?php
```

```
namespace App;
```

```
use Illuminate\Database\Eloquent\Model;
```

```
class Photo extends Model{    protected $with = ['comments'];
```

```
    protected $fillable = ['url', 'image'];
```

```
    public function comments()    {        return $this->hasMany(PhotoComment::class);    }}
```

Dans ce qui précède, nous avons ajouté la propriété `fillable`. Cela nous empêche d'avoir des exceptions d'assignation de masse lorsque nous essayons de mettre à jour ces colonnes en utilisant `Photo::create`. Nous avons également défini la propriété `with`, qui charge simplement les relations `comments`.

Nous avons défini une relation Eloquent, `comments`, qui dit simplement que `Photo` a plusieurs `PhotoComments`.

Ouvrez le modèle `PhotoComment` et remplacez le contenu par ce qui suit :

```
<?php
```

```
namespace App;
```

```
use Illuminate\Database\Eloquent\Model;
```

```
class PhotoComment extends Model{    protected $fillable = ['photo_id', 'comment', 'top', 'left'];
```

```
    protected $appends = ['position'];
```

```
    public function getPositionAttribute()    {        return [            'top' => $this->attributes['top'],             'left' => $this->attributes['left']        ];    }}
```

Tout comme le modèle `Photo`, nous avons défini la propriété `fillable`. Nous utilisons également [Eloquent accessors](https://laravel.com/docs/5.5/eloquent-mutators#accessors-and-mutators) pour configurer une nouvelle propriété appelée `position`. Celle-ci est ensuite ajoutée, car nous l'avons spécifié dans la propriété `appends`.

#### Configuration du frontend pour notre application

La prochaine chose que nous voulons faire est de configurer le frontend de notre application. Commençons par installer quelques packages NPM dont nous aurons besoin dans l'application. Dans votre application Terminal, exécutez la commande ci-dessous pour installer les packages nécessaires :

```
$ npm install --save laravel-echo pusher-js vue2-dropzone@^2.0.0$ npm install
```

Cela installera [Laravel Echo](https://laravel.com/docs/5.5/broadcasting#installing-laravel-echo), le [Pusher JS SDK](https://github.com/pusher/pusher-js), et [vue-dropzone](https://github.com/rowanwins/vue-dropzone). Nous aurons besoin de ces packages pour gérer les événements en temps réel plus tard.

Lorsque les packages ont été installés avec succès, nous pouvons maintenant commencer à ajouter du HTML et du JavaScript.

Ouvrez le fichier `./routes/web.php`, et ajoutons quelques routes. Remplacez le contenu du fichier par le contenu ci-dessous :

```
<?php
```

```
Route::post('/feedback/{image_url}/comment', 'PhotoController@comment');Route::get('/feedback/{image_url}', 'PhotoController@show');Route::post('/upload', 'PhotoController@upload');Route::view('/', 'welcome');
```

Dans le code ci-dessus, nous avons défini quelques routes. La première gérera les feedbacks `POST`. La deuxième route affichera l'image qui doit recevoir des feedbacks. La troisième route gérera les téléversements, et la dernière route affichera la page d'accueil.

Maintenant, ouvrez le fichier `./resources/views/welcome.blade.php`, et remplacez le contenu par le code HTML suivant :

```
<!doctype html><html lang="{{ app()->getLocale() }}"><head>    <meta charset="utf-8">    <meta http-equiv="X-UA-Compatible" content="IE=edge">    <meta name="viewport" content="width=device-width, initial-scale=1">    <meta name="csrf-token" content="{{csrf_token()}}">    <title>Téléverser pour obtenir des feedbacks</title>    <link href="https://fonts.googleapis.com/css?family=Roboto:400,600" rel="stylesheet" type="text/css">    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">    <link rel="stylesheet" href="{{ asset('css/app.css') }}"></head><body>    <div id="app">        <div class="flex-center position-ref full-height">            <div class="content">                <uploadarea></uploadarea>            </div>        </div>    </div>    <script src="js/app.js"></script></body></html>
```

Ceci est un document HTML simple. Si vous regardez de près, vous verrez une référence à une balise `uploadarea` qui n'existe pas en HTML mais est un composant Vue.

Ouvrez le fichier `./resources/assets/sass/app.scss` et collez le code suivant sous les instructions d'importation :

```
html, body {    background-color: #fff;    color: #636b6f;    font-family: 'Roboto', sans-serif;    font-weight: 100;    height: 100vh;    margin: 0;}.full-height {    height: 100vh;}.flex-center {    align-items: center;    display: flex;    justify-content: center;}.position-ref {    position: relative;}.content {    text-align: center;}.m-b-md {    margin-bottom: 30px;}.dropzone.dz-clickable {    width: 100vw;    height: 100vh;    .dz-message {        span {            font-size: 19px;            font-weight: 600;        }    }}#canvas {    width: 90%;    margin: 0 auto;    img {        width: 100%;    }}.modal {    text-align: center;    padding: 0!important;    z-index: 9999;}.modal-backdrop.in {    opacity: 0.8;    filter: alpha(opacity=80);}.modal:before {    content: '';    display: inline-block;    height: 100%;    vertical-align: middle;    margin-right: -4px;}.modal-dialog {    display: inline-block;    text-align: left;    vertical-align: middle;}.image-hotspot {    position: relative;    > img {        display: block;        height: auto;        transition: all .5s;    }}.hotspot-point {    z-index: 2;    position: absolute;    display: block;    span {        position: relative;        display: flex;        justify-content: center;        align-items: center;        width: 1.8em;        height: 1.8em;        background: #cf00f1;        border-radius: 50%;        animation: pulse 3s ease infinite;        transition: background .3s;        box-shadow: 0 2px 10px rgba(#000, .2);        &:after {            content: attr(data-price);            position: absolute;            bottom: 130%;            left: 50%;            color: white;            text-shadow: 0 1px black;            font-weight: 600;            font-size: 1.2em;            opacity: 0;            transform: translate(-50%, 10%) scale(.5);            transition: all .25s;        }    }    svg {        opacity: 0;        color: #cf00f1;        font-size: 1.4em;        transition: opacity .2s;    }    &:before,    &:after  {        content: '';        position: absolute;        top: 0;        left: 0;        width: 100%;        height: 100%;        border-radius: 50%;        pointer-events: none;    }    &:before {        z-index: -1;        border: .15em solid rgba(#fff, .9);        opacity: 0;        transform: scale(2);        transition: transform .25s, opacity .2s;    }    &:after {        z-index: -2;        background:#fff;        animation: wave 3s linear infinite;    }    &:hover{        span {            animation: none;            background: #fff;            &:after {                opacity: 1;                transform: translate(-50%, 0) scale(1);            }        }        svg {            opacity: 1;        }        &:before {            opacity: 1;            transform: scale(1.5);            animation: borderColor 2s linear infinite;        }        &:after {            animation: none;            opacity: 0;        }    }}@-webkit-keyframes pulse{    0%, 100% { transform: scale(1); }    50% { transform: scale(1.1); }}@keyframes pulse{    0%, 100% { transform: scale(1); }    50% { transform: scale(1.1); }}.popover {    min-width: 250px;}
```

Enregistrez le fichier et quittez. Maintenant, passons à la création de nos composants Vue.

### Utilisation de Vue pour créer les fonctionnalités de notre application prototype de feedback

Ouvrez le fichier `./resources/assets/js/app.js`, et créez le composant Vue. Dans ce fichier, trouvez la ligne ci-dessous :

```
Vue.component('example', require('./components/Example.vue'));
```

et remplacez-la par :

```
Vue.component('uploadarea', require('./components/UploadArea.vue'));Vue.component('feedback',require('./components/FeedbackCanvas.vue'));
```

Maintenant, créons notre premier composant Vue. Dans le répertoire `./resources/assets/js/components`, créez un fichier appelé `UploadArea.vue`. Dans le nouveau fichier, collez ce qui suit :

```
<template>    <dropzone ref="dropzone" id="dropzone"            url="/upload"            accepted-file-types="image/*"            v-on:vdropzone-success="showImagePage"            :headers="csrfHeader"            class="flex-center position-ref full-height">        <input type="hidden" name="csrf-token" :value="csrfToken">    </dropzone></template><script>import Dropzone from 'vue2-dropzone';const LARAVEL_TOKEN = document.head.querySelector('meta[name="csrf-token"]').contentexport default {    components: { Dropzone },    data() {        return {            csrfToken: LARAVEL_TOKEN,            csrfHeader: { 'X-CSRF-TOKEN': LARAVEL_TOKEN }        }    },    methods: {        showImagePage: (file, response) => {            if (response.url) {                return window.location = `/feedback/${response.url}`;            }        }    },    mounted () {        this.$refs.dropzone.dropzone.on('addedfile', function (file) {            if (this.files.length > 1) {                this.removeFile(this.files[0])            }        })    }}</script>
```

Dans la section `template`, nous utilisons simplement le package Vue dropzone pour définir une zone à travers laquelle les fichiers peuvent être téléversés. Vous pouvez consulter la documentation [ici](https://github.com/rowanwins/vue-dropzone).

Dans la section `script`, nous obtenons le jeton CSRF Laravel de l'en-tête de la page et importons le composant `Dropzone` dans notre composant Vue actuel.

Dans la propriété `methods`, nous définissons une méthode `showImagePage` qui redirige simplement l'utilisateur vers la page de l'image après que l'image a été téléversée avec succès. Dans la méthode `mounted`, nous limitons le fichier dropzone à permettre un téléversement de fichier à la fois.

Créons maintenant notre prochain composant Vue. Dans le répertoire `./resources/assets/js/components`, créez un nouveau fichier appelé `FeedbackCanvas.vue` et collez ce qui suit :

```
<template>    <div class="feedback-area">        <div class="content">            <div id="canvas">                <div class="image-hotspot" id="imghotspot">                    <transition-group name="hotspots">                        <a                        href="#"                        class="hotspot-point"                        v-for="(comment, index) in image.comments"                        v-bind:style="{ left: comment.position.left+'%', top: comment.position.top+'%' }"                        :key="index"                        @click.prevent                        data-placement="top"                        data-toggle="popover"                        :data-content="comment.comment"                        >                            <span>                                <svg class="icon icon-close" viewBox="0 0 24 24">                                    <path d="M18.984 12.984h-6v6h-1.969v-6h-6v-1.969h6v-6h1.969v6h6v1.969z"></path>                                </svg>                            </span>                        </a>                    </transition-group>                    <img ref="img" :src="'/storage/'+image.image" id="loaded-img"  @click="addCommentPoint">                </div>            </div>        </div>        <add-comment-modal :image="image"></add-comment-modal>    </div></template>
```

Nous avons défini le `template` pour notre composant Vue. C'est la zone où l'image sera affichée et où les feedbacks seront donnés.

Maintenant, nous allons décomposer certaines parties un peu.

La balise `a` a un ensemble d'attributs définis.

Le `v-for` parcourt chaque commentaire/feedback de l'image.

Le `v-bind:style` applique un attribut `style` à la balise `a` en utilisant les propriétés `left` et `top` du commentaire/feedback.

Nous avons également `:data-content`, `data-toggle` et `data-placement` dont Bootstrap a besoin pour ses [Popovers](https://www.w3schools.com/bootstrap/bootstrap_popover.asp).

La balise `img` a l'événement `@click` qui déclenche la fonction `addCommentPoint` lorsqu'une zone de l'image est cliquée.

Et enfin, il y a un composant Vue `add-comment-modal` qui accepte une propriété `image`. Ce composant affichera un formulaire pour que n'importe qui puisse laisser un commentaire.

Dans ce même fichier, après la balise de fermeture `template`, collez le code suivant :

```
<script>    let AddCommentModal = require('./AddCommentModal.vue')    export default {        props: ['photo'],        components: { AddCommentModal },        data() {            return { image: this.photo }        },        mounted() {            let vm = this            Echo.channel(`feedback-${this.photo.id}`)                .listen('.added', (e) => {                    // Parcourir les commentaires et si aucun commentaire ne correspond aux                     // commentaires existants, l'ajouter                    if (vm.image.comments.filter((comment) => comment.id === e.comment.id).length === 0) {                        vm.image.comments.push(e.comment)                        $(document).ready(() => $('[data-toggle="popover"]').popover())                    }                })        },        created() {            /** Activer les popovers */            $(document).ready(() => $('[data-toggle="popover"]').popover());            /** Calcule les coordonnées du point de clic */            this.calculateClickCordinates = function (evt) {                let rect = evt.target.getBoundingClientRect()                return {                    left: Math.floor((evt.clientX - rect.left - 7) * 100 / this.$refs.img.width),                    top: Math.floor((evt.clientY - rect.top - 7) * 100 / this.$refs.img.height)                }            }            /** Supprime les commentaires qui n'ont pas été enregistrés */            this.removeUnsavedComments = function () {                var i = this.image.comments.length                while (i--) {                    if ( ! this.image.comments[i]['id']) {                        this.image.comments.splice(i, 1)                    }                }            }        },        methods: {            addCommentPoint: function(evt) {                let vm       = this                let position = vm.calculateClickCordinates(evt)                let count    = this.image.comments.push({ position })                // Afficher le modal et ajouter un callback pour lorsque le modal est fermé                let modalElem = $("#add-modal")                modalElem.data({"comment-index": count-1, "comment-position": position})                modalElem.modal("show").on("hide.bs.modal", () => vm.removeUnsavedComments())            }        },    }</script>
```

> _? Les méthodes c`reated` et m`ounted` sont des hooks qui sont appelés automatiquement pendant la création du composant Vue. Vous pouvez en apprendre davantage sur le cycle de vie de Vue [ici](https://alligator.io/vuejs/component-lifecycle)._

Dans la méthode `mounted`, nous utilisons Laravel Echo pour écouter un canal Pusher. Le nom du canal dépend de l'ID de l'image actuellement visualisée. Chaque image aura des diffusions sur un canal différent en fonction de l'ID de l'image.

Lorsque l'événement `added` est déclenché sur le canal `feedback-$id`, il parcourt les `image.comments` disponibles et, si le commentaire diffusé n'existe pas, il l'ajoute au tableau des commentaires.

Dans la méthode `create`, nous activons les popovers Bootstrap, définissons une fonction qui calcule les coordonnées du point de clic, et nous définissons une fonction qui supprime les commentaires qui n'ont pas été enregistrés du tableau `image.comments`.

Sous `methods`, nous définissons la méthode `addCommentPoint` qui calcule les coordonnées du clic et lance ensuite un nouveau modal Bootstrap. Cela sera créé dans le composant Vue `add-comment-modal`.

Pour que Laravel Echo fonctionne, nous devons ouvrir le fichier `./resources/assets/js/bootstrap.js` et ajouter le code ci-dessous en bas du fichier :

```
import Echo from 'laravel-echo'
```

```
window.Pusher = require('pusher-js');
```

```
window.Echo = new Echo({    broadcaster: 'pusher',    key: 'PUSHER_KEY',    encrypted: true,    cluster: 'PUSHER_CLUSTER'});
```

Vous devez remplacer `PUSHER_KEY` et `PUSHER_CLUSTER` par la clé et le cluster de votre application Pusher.

Maintenant, créons notre prochain composant Vue, `AddCommentModal.vue`. Il est déjà référencé dans notre composant Vue `FeedbackCanvas.vue`.

```
<template>    <div id="add-modal" class="modal fade" role="dialog" data-backdrop="static" data-keyboard="false">        <div class="modal-dialog">            <div class="modal-content">                <form method="post" :action="'/feedback/'+photo.url+'post'" @submit.prevent="submitFeedback()">                    <div class="modal-header">                        <h4 class="modal-title">Ajouter un feedback</h4>                    </div>                    <div class="modal-body">                        <textarea name="feedback" id="feedback-provided" cols="10" rows="5" class="form-control" v-model="feedback" placeholder="Entrez un feedback..." required minlength="2" maxlength="2000"></textarea>                    </div>                    <div class="modal-footer">                        <button type="submit" class="btn btn-primary pull-right">Soumettre</button>                        <button type="button" class="btn btn-default pull-left" data-dismiss="modal">Annuler</button>                    </div>                </form>            </div>    </div>    </div></template>
```

```
<script>export default {    props: ['image'],    data() {        return { photo: this.image, feedback: null }    },    methods: {        submitFeedback: function () {            let vm = this            let modal = $('#add-modal')            let position = modal.data("comment-position")
```

```
// Créer l'URL et la charge utile            let url = `/feedback/${this.photo.url}/comment`;            let payload = {comment: this.feedback, left: position.left, top: position.top}            axios.post(url, payload).then(response => {                this.feedback = null                modal.modal('hide')                vm.photo.comments[modal.data('comment-index')] = response.data                $(document).ready(() => $('[data-toggle="popover"]').popover())            })        }    }}</script>
```

Dans la section `template`, nous avons défini un modal Bootstrap typique. Dans le formulaire modal, nous avons attaché un appel à `submitFeedback()` qui est déclenché lorsque le formulaire est soumis.

Dans la section `script`, nous avons défini la méthode `submitFeedback()` dans la propriété `methods` du composant Vue. Cette fonction envoie simplement un commentaire au backend pour stockage. Si une réponse favorable est reçue de l'API, le modal Bootstrap est masqué et le commentaire est ajouté au tableau `image.comments`. Le popover Bootstrap est ensuite rechargé pour qu'il prenne en compte les modifications.

Avec ce dernier changement, nous avons défini tous nos composants Vue. Ouvrez votre terminal et exécutez la commande ci-dessous pour construire vos actifs JS et CSS :

```
$ npm run dev
```

Super ! Maintenant, construisons le backend.

### Création des endpoints pour notre application prototype de feedback

Dans votre terminal, entrez la commande ci-dessous :

```
php artisan make:event FeedbackAdded
```

Cela créera une classe d'événement appelée `FeedbackAdded`. Nous utiliserons ce fichier pour déclencher des événements vers Pusher lorsque nous ajouterons des feedbacks. Cela fera apparaître les feedbacks en temps réel à toute personne regardant l'image.

Ouvrez la classe `PhotoController` et remplacez le contenu par le code ci-dessous :

```
<?phpnamespace App\Http\Controllers;
```

```
use App\Events\FeedbackAdded;use App\{Photo, PhotoComment};
```

```
class PhotoController extends Controller{    public function show($url)    {        $photo = Photo::whereUrl($url)->firstOrFail();
```

```
        return view('image', compact('photo'));    }
```

```
    public function comment(string $url)    {        $photo = Photo::whereUrl($url)->firstOrFail();
```

```
        $data = request()->validate([            "comment" => "required|between:2,2000",            "left" => "required|numeric|between:0,100",            "top"  => "required|numeric|between:0,100",        ]);
```

```
        $comment = $photo->comments()->save(new PhotoComment($data));
```

```
        event(new FeedbackAdded($photo->id, $comment->toArray()));
```

```
        return response()->json($comment);    }
```

```
    public function upload()    {        request()->validate(['file' => 'required|image']);
```

```
        $gibberish = md5(str_random().time());
```

```
        $imgName = "{$gibberish}.".request('file')->getClientOriginalExtension();
```

```
        request('file')->move(public_path('storage'), $imgName);
```

```
        $photo = Photo::create(['image' => $imgName, 'url' => $gibberish]);
```

```
        return response()->json($photo->toArray());    }}
```

Dans ce qui précède, nous avons une méthode `show` qui affiche une image afin que les gens puissent laisser des feedbacks dessus. Ensuite, il y a la méthode `comment` qui enregistre un nouveau commentaire sur une image. La méthode finale est la méthode `upload` qui téléverse simplement une image sur le serveur et l'enregistre dans la base de données.

Créons la vue pour la méthode `show`. Créez un nouveau fichier dans le répertoire `./resources/views` appelé `image.blade.php`. Dans ce fichier, collez le code ci-dessous :

```
<!doctype html><html lang="{{ app()->getLocale() }}"><head>    <meta charset="utf-8">    <meta http-equiv="X-UA-Compatible" content="IE=edge">    <meta name="viewport" content="width=device-width, initial-scale=1">    <meta name="csrf-token" content="{{csrf_token()}}">;    <title>Laravel</title>    <link href="https://fonts.googleapis.com/css?family=Roboto:400,600" rel="stylesheet" type="text/css">    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">    <link rel="stylesheet" href="{{ asset('css/app.css') }}"></head><body>    <div id="app">        <feedback :photo='@json($photo)'></feedback>    </div>    <script src="{{asset('js/app.js')}}"></script></body></html>
```

Dans ce qui précède, la seule chose qui se distingue est la balise `feedback`. Elle fait essentiellement référence au composant Vue feedback que nous avons construit plus tôt dans l'article. Tout le reste est simplement du Blade et du HTML de base.

Maintenant que nous avons créé la vue, nous devons ajouter le répertoire pour les téléversements défini dans la méthode `upload`. Dans votre terminal, exécutez la commande ci-dessous :

```
$ php artisan storage:link
```

Cette commande créera un lien symbolique du répertoire `./storage` vers le répertoire `./public/storage`. Si vous regardez dans le répertoire `./public`, vous devriez voir le lien symbolique.

Maintenant que nous avons créé le backend pour supporter notre application web, nous devons ajouter Pusher au backend afin que les commentaires soient diffusés et puissent être récupérés par d'autres personnes navigant sur l'image.

### Ajout de fonctionnalités en temps réel à l'application prototype de feedback en utilisant Pusher

Ouvrez votre terminal et entrez la commande ci-dessous pour installer le [Pusher PHP SDK](https://github.com/pusher/pusher-http-php) :

```
$ composer require pusher/pusher-php-server "~3.0"
```

Ouvrez le fichier `.env` et faites défiler jusqu'en bas et configurez les clés Pusher comme indiqué ci-dessous :

```
PUSHER_APP_ID="PUSHER_ID"PUSHER_APP_KEY="PUSHER_KEY"PUSHER_APP_SECRET="PUSHER_SECRET"
```

Également dans le même fichier, recherchez le `BROADCAST_DRIVER` et changez-le de `log` à `pusher`.

Ensuite, ouvrez le fichier `./config/broadcasting.php` et faites défiler jusqu'à la clé `pusher`. Remplacez la clé `options` de cette configuration par le code ci-dessous :

```
// ...
```

```
    'options' => [        'cluster' => 'PUSHER_CLUSTER',        'encrypted' => true    ], 
```

```
// ...
```

> _? N'oubliez pas de remplacer P`USHER_ID,` P`USHER_KEY,` P`USHER_SECRET` et P`USHER_CLUSTER` par les valeurs de votre application Pusher._

Maintenant, ouvrez la classe `FeedbackAdded` et remplacez le contenu par le code ci-dessous :

```
<?phpnamespace App\Events;
```

```
use Illuminate\Broadcasting\Channel;use Illuminate\Queue\SerializesModels;use Illuminate\Foundation\Events\Dispatchable;use Illuminate\Broadcasting\InteractsWithSockets;use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
```

```
class FeedbackAdded implements ShouldBroadcast{    use Dispatchable, InteractsWithSockets, SerializesModels;
```

```
    public $comment;
```

```
    public $photo_id;
```

```
    public function __construct(int $photo_id, array $comment)    {        $this->comment = $comment;        $this->photo_id = $photo_id;    }
```

```
    public function broadcastOn()    {        return new Channel("feedback-{$this->photo_id}");    }
```

```
    public function broadcastAs()    {        return 'added';    }}
```

Dans la classe ci-dessus, nous définissons l'objet `comment` et l'`photo_id` qui seront utilisés pour composer le nom du canal dans la méthode `broadcastOn`. Nous définissons également la méthode `broadcastAs`, qui nous permettra de personnaliser le nom de l'événement envoyé à Pusher.

C'est tout. Maintenant, exécutons notre application. Dans votre terminal, exécutez le code ci-dessous :

```
$ php artisan serve
```

![Image](https://cdn-media-1.freecodecamp.org/images/XSzmKqsOpg4JYAfw2a6QJ7Rt2Ng7ZvHMuHEx)

Cela devrait démarrer un nouveau serveur PHP. Vous pouvez ensuite l'utiliser pour tester votre application. Allez à l'URL donnée et vous devriez voir votre application.

### Conclusion

Dans cet article, nous avons réussi à créer une fonctionnalité de feedback d'application prototype qui permettra aux designers de partager leurs designs avec d'autres et de recevoir des feedbacks sur ceux-ci.

Cet article a été publié pour la première fois sur [Pusher](https://pusher.com/tutorials/design-feedback-vuejs/).