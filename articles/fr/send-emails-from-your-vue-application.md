---
title: Comment envoyer des emails depuis votre application Vue.js avec EmailJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T18:23:37.000Z'
originalURL: https://freecodecamp.org/news/send-emails-from-your-vue-application
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/EMAIL-JS.png
tags:
- name: automation
  slug: automation
- name: email
  slug: email
- name: Vue.js
  slug: vuejs
seo_title: Comment envoyer des emails depuis votre application Vue.js avec EmailJS
seo_desc: "By Oluwaseyi Bello\nA few days ago I decided to work on a simple Vue project\
  \ and needed to send emails through a contact from I had just created. I wanted\
  \ to receive an automated email every time someone filled out my contact form. \n\
  So I got to search..."
---

Par Oluwaseyi Bello

Il y a quelques jours, j'ai décidé de travailler sur un projet Vue simple et j'avais besoin d'envoyer des emails via un formulaire de contact que je venais de créer. Je voulais recevoir un email automatisé chaque fois que quelqu'un remplissait mon formulaire de contact. 

J'ai donc fait des recherches et je suis tombé sur [EmailJs](https://www.emailjs.com/). J'ai décidé d'écrire cet article parce que j'ai trouvé leur documentation excellente et qu'il était vraiment facile à utiliser. J'espère aussi que cela aidera quelqu'un là-bas :)

## Commençons !

Dans cet article, je vais vous montrer comment utiliser EmailJS pour envoyer des emails depuis votre application Vuejs. 

Avant de continuer, je suppose que vous avez Vue CLI installé sur votre ordinateur car je vais créer un mini projet de démonstration avec. Si ce n'est pas le cas, vous pouvez vérifier comment l'installer [ici](https://cli.vuejs.org/guide/installation.html).

Nous allons créer le projet en utilisant cette commande :

```
vue create vue-emailjs-demo
```

Nous serons alors invités à choisir une option pour sélectionner une configuration par défaut ou pour sélectionner manuellement des fonctionnalités. Sélectionnez `**default**`.

Un nouveau répertoire de projet sera créé, et vous pouvez y naviguer en utilisant cette commande :

```
cd vue-emailjs-demo
```

## Comment installer EmailJS

EmailJS vous aide à envoyer des emails en utilisant uniquement des technologies côté client. Aucun serveur n'est requis – il suffit de connecter EmailJS à l'un des services de messagerie pris en charge, de créer un modèle d'email et d'utiliser leur bibliothèque JavaScript pour déclencher un email.

Avant de commencer à écrire notre code, vous voudrez [créer un compte EmailJS](https://dashboard.emailjs.com/sign-in). Avec votre compte, vous pourrez créer des modèles d'email et choisir l'email auquel vous souhaitez que vos emails automatisés soient envoyés.

Une fois connecté à votre nouveau compte, vous serez redirigé vers le [tableau de bord](https://dashboard.emailjs.com/admin).

## Comment créer le modèle d'email

Les modèles d'email peuvent optionnellement contenir des variables dynamiques dans presque tous les champs (par exemple, sujet, contenu, email du destinataire, nom de l'expéditeur, etc.). Ils sont remplis à partir de l'appel JavaScript. Nous allons aborder cela sous peu. 

Tout d'abord, ajoutons un service d'email. J'ai sélectionné Gmail, mais vous êtes libre de choisir le service qui convient le mieux à vos besoins. 

De plus, si vous ne voulez pas commencer à réfléchir à un nom pour votre `Service ID`, appuyez sur l'icône de recherche et il sera généré automatiquement pour vous.

Ensuite, nous allons créer notre modèle d'email. Accédez à la page des modèles. Créez un nouveau modèle. Notre modèle d'email définira le sujet de notre email, le contenu qu'il contiendra, où il doit être envoyé, etc.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/emailjdeafault.PNG)

Les ensembles de doubles accolades comme `{{from_name}}` sont des variables. Lorsque l'utilisateur remplit notre formulaire, nous transmettons ces informations à EmailJS en utilisant ces variables.

Voici une petite explication des champs disponibles dans notre modèle :

* **Sujet** : Le sujet de l'email.
* **Contenu** : Le corps de l'email. Nous allons transmettre le message de l'utilisateur, son nom et son adresse de retour ici.
* **Email du destinataire** : Contient la destination de cet email.
* **Nom de l'expéditeur** : Ce champ est facultatif. Mais vous pouvez écrire votre nom ici.
* **Email de l'expéditeur** : L'adresse email de l'expéditeur telle qu'elle apparaîtra pour le destinataire. Si la case à cocher de l'adresse email par défaut est activée, EmailJS utilisera l'adresse email associée au service d'email utilisé.
* **Répondre à** : Définit l'adresse email à laquelle les réponses doivent être envoyées.
* **CCI et CC** : Ces deux champs sont généralement utilisés pour envoyer une copie du message à toutes les personnes que vous avez listées. `**Répondre à**`, `**CCI et CC**` ne seront pas utilisés dans ce guide car nous voulons le garder aussi simple que possible. Si vous avez besoin de plus d'informations, vous pouvez consulter la documentation d'EmailJS [ici](https://www.emailjs.com/docs/tutorial/creating-email-template/).

Note : À un moment donné dans cet article, nous utiliserons le `Service ID` et le `Template ID`. Nous aurons également besoin d'un `User ID`. Vous pouvez trouver votre `User ID` dans la partie **intégration** du tableau de bord. Vous pouvez copier les détails dans votre presse-papiers et les coller lorsqu'ils sont nécessaires.

## Comment installer EmailJS dans votre application

Passons maintenant au code :) Pour installer EmailJS dans votre application, utilisez cette commande :

```
npm install emailjs-com --save
```

Nous allons envoyer un email à partir d'un formulaire de contact très simple. Il collectera des données incluant : le nom (de l'expéditeur), l'email (de l'expéditeur) et le contenu du message. Simple !

Vous pouvez modifier le composant `HelloWorld.Vue` qui a été créé automatiquement pour nous lorsque nous avons utilisé Vue CLI ou vous pouvez créer un nouveau composant appelé `ContactForm.vue`. Je vais faire ce dernier.

Ci-dessous, nous allons construire le composant de formulaire de contact, `ContactForm.vue`.

Commençons par le `template` :

```
<template>
    <div class="container">
        <form @submit.prevent="sendEmail">
          <label>Nom</label>
          <input 
            type="text" 
            v-model="name"
            name="name"
            placeholder="Votre Nom"
          >
          <label>Email</label>
          <input 
            type="email" 
            v-model="email"
            name="email"
            placeholder="Votre Email"
            >
          <label>Message</label>
          <textarea 
            name="message"
            v-model="message"
            cols="30" rows="5"
            placeholder="Message">
          </textarea>
          
          <input type="submit" value="Envoyer">
        </form>
    </div>
</template>
```

### Explication de notre balisage

Comme je l'ai mentionné précédemment, nous allons envoyer un email à partir d'un formulaire de contact très simple. Créez donc un élément `div` qui contiendra le contenu de notre formulaire. Nous allons ajouter du style à notre formulaire, alors ajoutez une classe `container` à l'élément `div`.

```
<style scoped>
* {box-sizing: border-box;}

.container {
  display: block;
  margin:auto;
  text-align: center;
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
  width: 50%;
}

label {
  float: left;
}

input[type=text], [type=email], textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}
</style>
```

Vous pouvez démarrer votre serveur avec la commande :

```
npm run serve
```

Ouvrez maintenant votre navigateur à l'adresse localhost:8080 et vous devriez voir votre formulaire :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/vue-form-1.PNG)

Nous allons également créer une méthode appelée `sendEmail` qui gère la soumission de nos données. Mais avant cela, nous devons importer `emailjs` dans notre fichier. 

Ajoutez la ligne suivante juste sous `script` :

```
import emailjs from 'emailjs-com';
```

Voici le reste du code nécessaire dans notre `script` :

```
<script>
export default {
  name: 'ContactUs',
  data() {
    return {
      name: '',
      email: '',
      message: ''
    }
  },
  methods: {
    sendEmail(e) {
      try {
        emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', e.target,
        'YOUR_USER_ID', {
          name: this.name,
          email: this.email,
          message: this.message
        })
        .then((result) => {
          console.log('SUCCESS!', result.text);
        }, (error) => {
          console.log('FAILED...', error.text);
        });
      } catch(error) {
          console.log({error})
      }
      // Réinitialiser les champs du formulaire
      this.name = ''
      this.email = ''
      this.message = ''
    },
  }
}
</script>
```

### Ce que fait ce code

J'ai utilisé un `try...catch` ci-dessus, mais vous n'êtes pas obligé de l'utiliser. Vous souvenez-vous quand je vous ai demandé de copier les détails de votre Service ID, Template ID et User ID dans votre presse-papiers et de les coller lorsqu'ils sont nécessaires ? Eh bien, vous en avez absolument besoin maintenant ! Remplacez donc cette partie du code par vos détails réels.

`emailjs.sendForm()` est la manière dont nous envoyons des données à EmailJS après avoir passé le Service ID, le Template ID, le User ID et les données du formulaire qui ont été passées dans `sendEmail()`. Nous utilisons console.log() pour afficher toute erreur rencontrée avec le bloc `catch()`. 

Il est important de noter que `sendForm()` envoie un email en fonction du modèle d'email spécifié et des données du formulaire passées. Assurez-vous donc que le nom de l'entrée de votre formulaire est le même que la variable dans votre modèle EmailJS.

Voici mon modèle EmailJS modifié avec le nom (de l'expéditeur), l'email (de l'expéditeur) et le contenu du message.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/emailjscontactform-1.PNG)

C'est tout !

Vérifiez l'adresse `Email du destinataire` incluse dans votre modèle et vous devriez avoir votre email envoyé là-bas. Vous pouvez également jouer avec la fonction **Test it** ou **playground** dans le coin supérieur droit du modèle si vous le souhaitez.

### Dépôt GitHub

Vous pouvez trouver le code de cet article dans mon [compte GitHub](https://github.com/Seybel/vue-emailjs-demo).	

N'hésitez pas à partager cet article si vous l'avez trouvé utile. Merci pour la lecture !