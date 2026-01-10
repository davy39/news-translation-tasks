---
title: Comment créer une fonction de connexion avec Bootstrap Modal et jQuery AJAX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T21:44:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-login-feature-with-bootstrap-modal-and-jquery-ajax-53dc0d281609
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QQsDn3sXpsL06kzzS7a_oA.jpeg
tags:
- name: Bootstrap
  slug: bootstrap
- name: coding
  slug: coding
- name: jQuery
  slug: jquery
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer une fonction de connexion avec Bootstrap Modal et jQuery
  AJAX
seo_desc: 'By Yogi

  Bootstrap Modal is an excellent way to create a Login form on your website. In this
  tutorial, you will learn how to create a login feature using Bootstrap for an ASP.NET
  website. The login Check feature will be created using jQuery AJAX.

  I wi...'
---

Par Yogi

**Bootstrap Modal** est un excellent moyen de créer un **formulaire de connexion** sur votre site web. Dans ce tutoriel, vous apprendrez à créer une fonction de connexion en utilisant Bootstrap pour un site web ASP.NET. La fonction de vérification de connexion sera créée en utilisant jQuery AJAX.

**Je vais créer les fonctionnalités suivantes étape par étape :**

1. Une fenêtre modale Bootstrap qui contiendra un formulaire de connexion.

2. Le formulaire de connexion contiendra 2 champs, « Nom d'utilisateur » et « Mot de passe ». L'utilisateur doit entrer ses valeurs dans ces champs.

3. En cliquant sur le bouton de soumission du formulaire, les entrées de l'utilisateur (nom d'utilisateur et mot de passe) seront envoyées à la fonction C#.

4. Cette fonction C# vérifiera si le nom d'utilisateur et le mot de passe sont corrects ou non.

5. S'ils sont corrects, l'utilisateur est redirigé vers la page de profil.

#### [Vous pouvez consulter la démo fonctionnelle ici](http://www.demo.yogihosting.com/e/bootstrap-modal-login-form/).

#### **Création d'une fenêtre modale Bootstrap avec un formulaire de connexion**

Ajoutez la référence des fichiers « bootstrap CSS, jQuery et bootstrap js » dans l'en-tête de la page.

```
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
```

```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
```

```
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
```

Ensuite, créez une fenêtre modale Bootstrap qui contient le formulaire de connexion :

```
<div class="container"><div class="validCredential">
```

```
<h3>Essayez l'une des trois options suivantes :</h3><div><p>  1. Nom d'utilisateur : Ram</p><p>  Mot de passe : admin</p></div>
```

```
<div><p>  2. Nom d'utilisateur : Shiv</p><p>  Mot de passe : admin</p></div>
```

```
<div><p>  3. Nom d'utilisateur : Krishna</p>
```

```
<p>  Mot de passe : admin</p></div>
```

```
</div>
```

```
<!-- Le bouton qui déclenche la fenêtre modale --><button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal">Ouvrir la fenêtre modale</button>
```

```
<!-- Fenêtre modale Bootstrap --><div id="myModal" class="modal fade" role="dialog">  <div class="modal-dialog">
```

```
    <!-- Contenu de la fenêtre modale -->    <div class="modal-content">      <div class="modal-header">        <button type="button" class="close" data-dismiss="modal"></button>        <h4 class="modal-title">Connectez-vous avec votre nom d'utilisateur</h4>      </div>
```

```
      <div class="modal-body">        <table>          <tbody>            <tr>              <td>                <input type="text" id="userNameTextBox" placeholder="Nom d'utilisateur" />              </td>            </tr>            <tr>              <td>                <span id="userNamSpan"></span>              </td>            </tr>            <tr>              <td>                <input type="text" id="passwordTextBox" placeholder="Mot de passe" />              </td>            </tr>            <tr>              <td>                <span id="passwordSpan"></span>              </td>            </tr>            <tr>              <td>                <input type="button" id="submitButton" value="Connexion" />              </td>            </tr>            <tr>              <td>                <span id="messageSpan"></span>              </td>            </tr>            <tr>              <td>                <img id="loadingImg" src="loading.gif" />              </td>            </tr>          </tbody>        </table>      </div>
```

```
    <div class="modal-footer">      <button type="button" class="btn btn-default" data-dismiss="modal">Fermer</button>    </div>  </div><!-- FIN Contenu de la fenêtre modale --></div>
```

```
</div>
```

```
<!-- FIN Fenêtre modale Bootstrap --></div>
```

Voici à quoi ressemblera le formulaire de connexion de la fenêtre modale Bootstrap.

![Image](https://cdn-media-1.freecodecamp.org/images/DNem9yh40WOT2fNUPM33t9YynO7yWzqoiFsC)
_**Formulaire de connexion de la fenêtre modale Bootstrap**_

#### **Ajout du code jQuery sur l'événement de clic du bouton**

Dans le clic du bouton, je vais forcer les utilisateurs à entrer une valeur dans les champs de nom d'utilisateur et de mot de passe, avant qu'ils ne soumettent le formulaire.

Lorsque les deux zones de texte contiennent une valeur, je vais alors appeler la fonction C# en utilisant la [méthode jQuery AJAX](http://www.yogihosting.com/jquery-ajax/). Avec cette méthode, je pourrai passer les valeurs des 2 zones de texte (nom d'utilisateur et mot de passe) à ma fonction C#.

Ajoutez le code jQuery suivant à votre page :

```
$("#submitButton").click(function (e) {
```

```
if ($("#userNameTextBox").val() == "")
```

```
$("#userNamSpan").text("Entrez le nom d'utilisateur");
```

```
else
```

```
$("#userNamSpan").text("");
```

```
if ($("#passwordTextBox").val() == "")
```

```
$("#passwordSpan").text("Entrez le mot de passe");
```

```
else
```

```
$("#passwordSpan").text("");
```

```
if (($("#userNameTextBox").val() != "") && ($("#passwordTextBox").val() != ""))
```

```
$.ajax({  type: "POST",  url: "index.aspx/login",  contentType: "application/json; charset=utf-8",  data: '{"username":"' + $("#userNameTextBox").val() + '","password":"' + $("#passwordTextBox").val() + '"}',  dataType: "json",  success: function (result, status, xhr) {    if (result.d == "Success") {      $("#messageSpan").text("Connexion réussie, redirection vers votre page de profil.");      setTimeout(function () { window.location = "profile.aspx"; }, 2000);    }    else      $("#messageSpan").text("Échec de la connexion, veuillez réessayer.");    },   error: function (xhr, status, error) {     $("#dbData").html("Résultat : " + status + " " + error + " " + xhr.status + " " + xhr.statusText)   }});
```

```
});
```

```
$(document).ajaxStart(function () {  $("#loadingImg").show();});
```

```
$(document).ajaxStop(function () {  $("#loadingImg").hide();});
```

Dans la méthode de rappel de succès, vous pouvez voir que je redirige l'utilisateur vers la page **profile.aspx** si et seulement si je reçois le message « **Success** ».

La fonction **setTimeout()** est une fonction JavaScript qui redirigera vers la page de profil en 2 secondes.

**Les 2 images suivantes expliqueront la fonction de connexion :**

> _1. Lorsque la connexion échoue._

![Image](https://cdn-media-1.freecodecamp.org/images/pEzx51hKTGLE3OTi76TdDiLQQKCiHN4VS8EZ)
_**Échec de la connexion pour un nom d'utilisateur et un mot de passe incorrects**_

> _2. Lorsque la connexion est réussie._

![Image](https://cdn-media-1.freecodecamp.org/images/bttqLY1d9BT7-UNRPN-lrYCIxgXHCqVmVV0H)
_**Connexion réussie lorsque le nom d'utilisateur et le mot de passe sont corrects**_

#### **Le code C# :**

Maintenant, dans votre page **.aspx.cs**, ajoutez le code suivant :

```
[System.Web.Services.WebMethod]
```

```
public static string login(string username, string password)
```

```
{
```

```
var cred = LoadCredential();
```

```
var count = (from t in cred
```

```
where t.username == username && t.password == password
```

```
select t).Count();
```

```
if (count == 1)
```

```
{
```

```
HttpContext.Current.Session["User"] = username;
```

```
return "Success";
```

```
}
```

```
else
```

```
return "Failed";
```

```
}
```

```
class Credential
```

```
{
```

```
public string username { get; set; }
```

```
public string password { get; set; }
```

```
}
```

```
static List<Credential> LoadCredential()
```

```
{
```

```
List<Credential> credList = new List<Credential>();
```

```
Credential cred = new Credential();
```

```
cred.username = "Ram";
```

```
cred.password = "admin";
```

```
credList.Add(cred);
```

```
cred = new Credential();
```

```
cred.username = "Shiv";
```

```
cred.password = "admin";
```

```
credList.Add(cred);
```

```
cred = new Credential();
```

```
cred.username = "Krishna";
```

```
cred.password = "admin";
```

```
credList.Add(cred);
```

```
return credList;
```

```
}
```

La fonction login() est celle qui est appelée par la méthode **jQuery**. Elle vérifie si le _nom d'utilisateur et le mot de passe sont corrects_ et retourne ensuite le message approprié.

#### **CSS**

Pour styliser le formulaire de connexion et la fenêtre modale Bootstrap afin qu'ils aient une apparence parfaite, ajoutez le CSS suivant à votre page :

```
.btn {
```

```
margin: 15px 0;
```

```
}
```

```
#loadingImg {
```

```
display: none;
```

```
position: absolute;
```

```
margin: auto;
```

```
top: 0;
```

```
left: 0;
```

```
right: 0;
```

```
bottom: 0;
```

```
}
```

```
.validCredential h3 {
```

```
float: left;
```

```
text-decoration: underline;
```

```
}
```

```
.validCredential div {
```

```
clear: both;
```

```
}
```

```
.validCredential p {
```

```
float: left;
```

```
padding-right: 10px;
```

```
}
```

```
::-webkit-input-placeholder {
```

```
color: #ccc;
```

```
}
```

```
#myModal {
```

```
color: #1fa67b;
```

```
}
```

```
#myModal table {
```

```
position: relative;
```

```
margin: auto;
```

```
}
```

```
#myModal table input {
```

```
border-radius: 5px;
```

```
border: solid 1px #CCC;
```

```
margin: 10px;
```

```
padding: 3px 10px;
```

```
color: #000;
```

```
}
```

```
#myModal table input[type="button"] {
```

```
width: 94%;
```

```
background: #1fa67b;
```

```
color: #FFF;
```

```
}
```

```
#myModal table span {
```

```
float: left;
```

```
font-size: 12px;
```

```
color: #f00;
```

```
padding-left: 23px;
```

```
}
```

#### **Page de profil**

![Image](https://cdn-media-1.freecodecamp.org/images/DnAL6MlCl08x4PU4NDj9YKcfGhsYAoJnnsra)
_**Message de bienvenue sur la page de profil**_

Sur la page de profil, l'utilisateur recevra le message de bienvenue. Le code de la page de profil est le suivant :

```
<h1 id="welcomeMessage" runat="server"></h1>
```

```
if (!IsPostBack){  welcomeMessage.InnerHtml = "Bienvenue " + Session["User"] + " sur la page de profil.";}
```

> **Consultez la démo fonctionnelle en cliquant sur le lien ci-dessous :**

#### [Démo fonctionnelle](http://www.demo.yogihosting.com/e/bootstrap-modal-login-form/)

### **Conclusion**

J'espère que vous avez aimé ce tutoriel. N'hésitez pas à me contacter pour toute question. Je serai là pour vous aider si vous en avez besoin. Si vous avez aimé ce tutoriel, alors partagez-le sur vos réseaux sociaux.

**J'ai également publié un autre tutoriel sur freeCodeCamp, que vous pourriez aimer consulter — [Maîtrisez l'art des boucles en JavaScript avec ces incroyables astuces](https://medium.freecodecamp.org/master-the-art-of-looping-in-javascript-with-these-incredible-tricks-a5da1aa1d6c5)**