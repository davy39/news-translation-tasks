---
title: Comment faciliter le téléchargement d'images avec Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T15:07:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-image-upload-easy-with-angular-1ed14cb2773b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dxawCwfllIh8ljUcRtwnXg.png
tags:
- name: Angular
  slug: angularjs
- name: image
  slug: image
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment faciliter le téléchargement d'images avec Angular
seo_desc: 'By Filip Jerga

  This is the second part of the tutorial on how to upload an image to Amazon S3.
  You can find the first part here. In this article, we will take a look at the Angular
  Part.

  You can also watch my step by step video tutorial of an image u...'
---

Par Filip Jerga

Il s'agit de la deuxième partie du tutoriel sur la façon de télécharger une image vers Amazon S3. Vous pouvez trouver la première partie [ici](https://medium.freecodecamp.org/how-to-set-up-simple-image-upload-with-node-and-aws-s3-84e609248792). Dans cet article, nous allons examiner la partie Angular.

**Vous pouvez également regarder mon tutoriel vidéo étape par étape sur le téléchargement d'images. Le lien est fourni à la fin de cet article.**

### 1. Créez d'abord un template

Tout d'abord, nous voulons créer un composant réutilisable qui pourra être facilement intégré dans d'autres composants.

Commençons par un simple template HTML pour notre input. N'oubliez pas d'appliquer les styles de votre choix, ou vous pouvez les obtenir depuis mon [dépôt GitHub](https://gist.github.com/Jerga99/7fe7b1942c6e5bbe4723f2369c760649).

```ts
<label class="image-upload-container btn btn-bwm">
  <span>Sélectionner une image</span>
  <input #imageInput
         type="file"
         accept="image/*"
         (change)="processFile(imageInput)">
</label>
```

L'élément important ici est le **type** de l'input, qui est défini sur **file**. L'attribut **Accept** définit les fichiers acceptés pour l'input. **Image/*** spécifie que nous pouvons choisir des images de n'importe quel type avec cet input. **#imageInput** est une référence à l'input sur lequel nous pouvons accéder aux fichiers téléchargés.

Un événement **Change** est déclenché lorsque nous sélectionnons un fichier. Alors, examinons le code de la classe.

### 2. N'oubliez pas le code du composant

```ts
class ImageSnippet {
  constructor(public src: string, public file: File) {}
}

@Component({
  selector: 'bwm-image-upload',
  templateUrl: 'image-upload.component.html',
  styleUrls: ['image-upload.component.scss']
})
export class ImageUploadComponent {

  selectedFile: ImageSnippet;

  constructor(private imageService: ImageService){}

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', (event: any) => {

      this.selectedFile = new ImageSnippet(event.target.result, file);

      this.imageService.uploadImage(this.selectedFile.file).subscribe(
        (res) => {
        
        },
        (err) => {
        
        })
    });

    reader.readAsDataURL(file);
  }
}
```

Analysons ce code. Vous pouvez voir dans **processFile** que nous obtenons un input d'image envoyé depuis l'événement **change**. En écrivant **imageInput.files[0]**, nous accédons au premier **fichier**. Nous avons besoin d'un **reader** pour accéder aux propriétés supplémentaires d'un fichier. En appelant **readAsDataURL**, nous pouvons obtenir une représentation base64 d'une image dans la fonction de rappel de l'**addEventListener** auquel nous nous sommes abonnés auparavant.

Dans une fonction de rappel, nous créons une instance de **ImageSnippet**. La première valeur est une représentation base64 d'une image que nous afficherons plus tard à l'écran. La deuxième valeur est le fichier lui-même, que nous enverrons au serveur pour le télécharger vers Amazon S3.

Maintenant, nous devons simplement fournir ce fichier et envoyer une requête via un service.

### 3. Nous avons également besoin d'un service

Ce ne serait pas une application Angular sans un service. Le service sera responsable de l'envoi d'une requête à notre serveur Node.

```ts
export class ImageService {

  constructor(private http: Http) {}


  public uploadImage(image: File): Observable<Response> {
    const formData = new FormData();

    formData.append('image', image);

    return this.http.post('/api/v1/image-upload', formData);
  }
}
```

Comme je vous l'ai dit dans la conférence précédente, nous devons envoyer une image dans le cadre des **données de formulaire**. Nous allons ajouter l'image sous la clé **image** aux données de formulaire (même clé que nous avons configurée auparavant dans Node). Enfin, nous devons simplement envoyer une requête au serveur avec **formData** dans une charge utile.

**Maintenant, nous pouvons célébrer. C'est tout ! L'image est envoyée pour être téléchargée !**

Dans les lignes suivantes, je vais fournir un code supplémentaire pour une meilleure expérience utilisateur.

### 4. Mises à jour supplémentaires de l'UX

```ts
class ImageSnippet {
  pending: boolean = false;
  status: string = 'init';

  constructor(public src: string, public file: File) {}
}

@Component({
  selector: 'bwm-image-upload',
  templateUrl: 'image-upload.component.html',
  styleUrls: ['image-upload.component.scss']
})
export class ImageUploadComponent {

  selectedFile: ImageSnippet;

  constructor(private imageService: ImageService){}

  private onSuccess() {
    this.selectedFile.pending = false;
    this.selectedFile.status = 'ok';
  }

  private onError() {
    this.selectedFile.pending = false;
    this.selectedFile.status = 'fail';
    this.selectedFile.src = '';
  }

  processFile(imageInput: any) {
    const file: File = imageInput.files[0];
    const reader = new FileReader();

    reader.addEventListener('load', (event: any) => {

      this.selectedFile = new ImageSnippet(event.target.result, file);

      this.selectedFile.pending = true;
      this.imageService.uploadImage(this.selectedFile.file).subscribe(
        (res) => {
          this.onSuccess();
        },
        (err) => {
          this.onError();
        })
    });

    reader.readAsDataURL(file);
  }
}
```

Nous avons ajouté de nouvelles propriétés à **ImageSnippet** : **Pending** et **Status**. **Pending** peut être faux ou vrai, selon si une image est actuellement en cours de téléchargement. **Status** est le résultat du processus de téléchargement. Il peut être **OK** ou **FAILED**.

**OnSuccess** et **onError** sont appelés après le téléchargement de l'image et ils définissent le statut de l'image.

D'accord, maintenant examinons le fichier de template mis à jour :

```ts
<label class="image-upload-container btn btn-bwm">
  <span>Sélectionner une image</span>
  <input #imageInput
         type="file"
         accept="image/*"
         (change)="processFile(imageInput)">
</label>


<div *ngIf="selectedFile" class="img-preview-container">

  <div class="img-preview{{selectedFile.status === 'fail' ? '-error' : ''}}"
       [ngStyle]="{'background-image': 'url('+ selectedFile.src + ')'}">
  </div>

  <div *ngIf="selectedFile.pending" class="img-loading-overlay">
    <div class="img-spinning-circle"></div>
  </div>

  <div *ngIf="selectedFile.status === 'ok'" class="alert alert-success"> Image téléchargée avec succès !</div>
  <div *ngIf="selectedFile.status === 'fail'" class="alert alert-danger"> Échec du téléchargement de l'image !</div>
</div>
```

Ici, nous affichons notre image téléchargée et les erreurs à l'écran en fonction de l'**état** de l'**image**. Lorsque l'image est en attente, nous affichons également une belle image tournante pour notifier l'utilisateur de l'activité de téléchargement.

### 5. Ajoutez un peu de style

Les styles ne sont pas le sujet principal de ce tutoriel, vous pouvez donc obtenir tous les styles SCSS dans ce [lien](https://gist.github.com/Jerga99/7fe7b1942c6e5bbe4723f2369c760649).

**Travail terminé ! :) Cela devrait suffire pour un téléchargement d'image simple. Si quelque chose n'est pas clair, assurez-vous d'avoir regardé la première partie de ce tutoriel.**

Si vous aimez ce tutoriel, n'hésitez pas à consulter mon cours complet sur Udemy **— [Le guide complet Angular, React & Node | Application style Airbnb](http://bit.ly/2NeWna4).**

**Projet terminé :** [Mon dépôt GitHub](https://github.com/Jerga99/bwm-ng)

**Conférence vidéo :** [Tutoriel YouTube](https://www.youtube.com/watch?v=wNqwExw-ECw)

À bientôt,

Filip