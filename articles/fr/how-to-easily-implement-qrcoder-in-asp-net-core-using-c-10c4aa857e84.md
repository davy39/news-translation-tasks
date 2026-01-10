---
title: Comment implémenter facilement QRCoder dans ASP.NET Core en utilisant C#
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-23T15:58:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-implement-qrcoder-in-asp-net-core-using-c-10c4aa857e84
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qL5RAfsdeIw875myQ3f9Ag.png
tags:
- name: Aspnetcore
  slug: aspnetcore
- name: C#
  slug: csharp
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment implémenter facilement QRCoder dans ASP.NET Core en utilisant C#
seo_desc: 'By Yogi

  QRCoder is a very popular QR Code implementation library written in C#. It is available
  in GitHub. Here I am going to implement the QRCoder library to generate QR Codes
  in my ASP.NET Core application. I will also be using C#.

  I will implement...'
---

Par Yogi

QRCoder est une bibliothèque très populaire d'implémentation de codes QR écrite en C#. Elle est disponible sur [**GitHub**](https://github.com/codebude/QRCoder). Ici, je vais implémenter la bibliothèque QRCoder pour générer des codes QR dans mon application ASP.NET Core. J'utiliserai également C#.

Je vais implémenter QRCoder de 3 manières, qui sont :

1. Créer une image Bitmap de code QR pour n'importe quel texte.

2. Créer un fichier de code QR (.qrr) pour n'importe quel texte et ensuite sauvegarder ces fichiers dans l'application.

3. Lire et afficher tous les fichiers de code QR (.qrr).

Commençons par l'installation de QRCoder dans le Framework [**ASP.NET Core**](https://www.yogihosting.com/category/aspnet-core/).

[**Vous pouvez télécharger le code complet depuis mon dépôt GitHub**](https://github.com/yogyogi/QRCoder-implemented-in-ASP.NET-Core).

### **Installation**

Installez QRCoder via le gestionnaire de packages NuGet. Si vous souhaitez utiliser NuGet, recherchez simplement « QRCoder » ou exécutez la commande suivante dans la console du gestionnaire de packages NuGet :

`PM> Install-Package QRCoder`

QRCoder s'installera en 1 minute et sera prêt à l'emploi.

Maintenant, commençons avec l'implémentation de QRCoder des 3 manières mentionnées ci-dessus.

### **Créer une image Bitmap de code QR pour n'importe quel texte**

Créez un nouveau contrôleur appelé `QRCoderController` dans le dossier Controllers. Le contrôleur sera créé et contiendra une seule méthode d'action appelée `Index` :

```
public IActionResult Index()
{
    return View();
}
```

Importez les espaces de noms suivants dans le contrôleur :

```
using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using Microsoft.AspNetCore.Mvc;
using QRCoder;
```

Ensuite, ajoutez l'action Index de type `[HttpPost]` au contrôleur :

```
[HttpPost]
public IActionResult Index(string qrText)
{
    QRCodeGenerator qrGenerator = new QRCodeGenerator();
    QRCodeData qrCodeData = qrGenerator.CreateQrCode(qrText,
    QRCodeGenerator.ECCLevel.Q);
    QRCode qrCode = new QRCode(qrCodeData);
    Bitmap qrCodeImage = qrCode.GetGraphic(20);
    return View(BitmapToBytes(qrCodeImage));
}
```

> Cette action Index reçoit un paramètre de chaîne appelé 'qrText'. Il contient le texte fourni par un contrôle d'entrée défini dans la vue. Ce texte sera converti en image Bitmap de code QR. Les lignes de code suivantes effectuent ce travail :

```
QRCodeGenerator qrGenerator = new QRCodeGenerator();

QRCodeData qrCodeData = qrGenerator.CreateQrCode(qrText, QRCodeGenerator.ECCLevel.Q);

QRCode qrCode = new QRCode(qrCodeData);
Bitmap qrCodeImage = qrCode.GetGraphic(20);
```

L'objet QRCode ('qrCode') défini appelle une fonction statique appelée 'BitmapToBytes()'. Le rôle de cette fonction est de convertir l'image Bitmap en 'Byte[]'.

Ajoutez cette fonction à votre contrôleur :

```
private static Byte[] BitmapToBytes(Bitmap img)
{
    using (MemoryStream stream = new MemoryStream())
    {
        img.Save(stream, System.Drawing.Imaging.ImageFormat.Png);
        return stream.ToArray();
    }
}
```

Enfin, créez la vue Index dans le dossier 'Views/QRCoder' avec le code suivant :

```
@model Byte[]
@{
    Layout = null;
}

<!DOCTYPE html>
<html>

<head>
  <meta name="viewport" content="width=device-width" />
  <title>Implémentation de QRCoder dans ASP.NET Core - Créer un code QR</title>
  <style>
    body {
      background: #111 no-repeat;
      background-image: -webkit-gradient(radial, 50% 0, 150, 50% 0, 300, from(#444), to(#111));
    }

    h1,
    h2,
    h3 {
      text-align: center;
      color: #FFF;
      margin: 5px 0;
    }

    h1 {
      font-size: 30px;
    }

    h2 a {
      font-size: 25px;
      color: #0184e3;
      text-decoration: none;
    }

    h3 {
      font-size: 23px;
      border-bottom: solid 3px #CCC;
      padding-bottom: 10px;
    }

    h3 a {
      color: #00e8ff;
      text-decoration: none;
    }

    h3 a:hover,
    h2 a:hover {
      text-decoration: underline;
    }

    .container {
      width: 800px;
      margin: auto;
      color: #FFF;
      font-size: 25px;
    }

    .container #content {
      border: dashed 2px #CCC;
      padding: 10px;
    }

    #reset {
      padding: 5px 10px;
      background: #4CAF50;
      border: none;
      color: #FFF;
      cursor: pointer;
    }

    #reset:hover {
      color: #4CAF50;
      background: #FFF;
    }

    #viewContent table {
      width: 100%;
    }

    #viewContent table tr {
      height: 80px;
      background: darkcyan;
    }

    #viewContent table tr td {
      width: 50%;
      padding-left: 5px;
    }
  </style>
</head>

<body>
  <div class="container">
    <div id="content">
      <h1>Implémentation de QRCoder dans ASP.NET Core - Créer un code QR</h1>
      <h2>
        <a href="http://www.yogihosting.com/category/aspnet-core/">Lire le tutoriel sur YogiHosting  </a>
        <button id="reset" onclick="location=''">Réinitialiser </button>
      </h2>
      <div id="viewContent">
        @using (Html.BeginForm(null, null, FormMethod.Post)) {
        <table>
          <tbody>
            <tr>
              <td>
                <label>Entrez le texte pour créer un code QR</label
                </td>
                <td>
                  <input type="text" name="qrText" />
                </td>
              </tr>
              <tr>
                <td colspan="2">
                  <button>Soumettre</button>
                </td>
              </tr>
            </tbody>
          </table>
        }
      </div>
      
      @{
        if (Model != null)
        {
          <h3>Code QR généré avec succès</h3>
          <img src="@String.Format("data:image/png;base64,{0}", Convert.ToBase64String(Model))" />
        }
      }
    </div>
  </div>
</body>
</html>
```

La vue Index contient un contrôle 'input'. L'utilisateur entre son texte dans ce contrôle pour créer le code QR :

`<input type="text" name="qrText"` />

Une fois le code QR généré par la méthode d'action Index, son tableau de 'byte' est retourné à la vue en tant que modèle, puis l'image bitmap est affichée par le code ci-dessous :

```
@{
  if (Model != null)
  {
    <h3>Code QR généré avec succès</h3>
    <img src="@String.Format("data:image/png;base64,{0}", Convert.ToBase64String(Model))" />
  }
}
```

#### **Test du code**

Exécutez votre application et allez à l'URL — 'http://localhost:50755/QRCoder' pour invoquer la méthode d'action Index.

Dans la zone de texte, ajoutez votre texte et cliquez sur le bouton de soumission pour créer l'image Bitmap du code QR.

Voir cette image qui l'illustre en fonctionnement :

![Image](https://cdn-media-1.freecodecamp.org/images/RZJScQFTxL1upNaGcmdXmOWaJR3u10Zq1RjJ)
_**créer une image Bitmap de code QR**_

### **Créer un fichier de code QR (.qrr) pour n'importe quel texte et ensuite sauvegarder ces fichiers dans l'application**

Vous pouvez également générer des fichiers de code QR pour un texte et les sauvegarder dans votre site web. Ces fichiers ont l'extension ._qrr_.

Ajoutez les méthodes d'action suivantes appelées 'GenerateFile' à votre contrôleur :

```
public IActionResult GenerateFile()
{
  return View();
}

[HttpPost]
public IActionResult GenerateFile(string qrText)
{
  QRCodeGenerator qrGenerator = new QRCodeGenerator();
  QRCodeData qrCodeData = qrGenerator.CreateQrCode(qrText,   QRCodeGenerator.ECCLevel.Q);
  
  string fileGuid = Guid.NewGuid().ToString().Substring(0, 4);
  
  qrCodeData.SaveRawData("wwwroot/qrr/file-" + fileGuid + ".qrr", QRCodeData.Compression.Uncompressed);
  
  QRCodeData qrCodeData1 = new QRCodeData("wwwroot/qrr/file-" + fileGuid + ".qrr", QRCodeData.Compression.Uncompressed);
  
  QRCode qrCode = new QRCode(qrCodeData1);
  Bitmap qrCodeImage = qrCode.GetGraphic(20);
  return View(BitmapToBytes(qrCodeImage));
}
```

La version `[HttpPost]` de cette méthode d'action génère les fichiers de code QR dans le dossier 'wwwroot/qrr'. Le code qui effectue ce travail est le suivant :

```
QRCodeGenerator qrGenerator = new QRCodeGenerator();

QRCodeData qrCodeData = qrGenerator.CreateQrCode(qrText, QRCodeGenerator.ECCLevel.Q);

string fileGuid = Guid.NewGuid().ToString().Substring(0, 4);

qrCodeData.SaveRawData("wwwroot/qrr/file-" + fileGuid + ".qrr", QRCodeData.Compression.Uncompressed);
```

Une fois le fichier .qrr créé, je le lis simplement à partir de son emplacement sauvegardé dans le site web. Ensuite, je le convertis en type Bitmap et enfin j'envoie les octets de l'image à la vue. Le code correspondant est :

```
QRCodeData qrCodeData1 = new QRCodeData("wwwroot/qrr/file-" + fileGuid + ".qrr", QRCodeData.Compression.Uncompressed);

QRCode qrCode = new QRCode(qrCodeData1);
Bitmap qrCodeImage = qrCode.GetGraphic(20);

return View(BitmapToBytes(qrCodeImage));
```

Ensuite, ajoutez la vue GenerateFile dans le dossier 'Views/QRCoder' et ajoutez le code suivant :

```
@model Byte[]
@{
    Layout = null;
}

<!DOCTYPE html>
<html>

<head>
  <meta name="viewport" content="width=device-width" />
  <title>Implémentation de QRCoder dans ASP.NET Core - Créer un fichier de code QR</title>
  <style>
    body {
      background: #111 no-repeat;
      background-image: -webkit-gradient(radial, 50% 0, 150, 50% 0, 300, from(#444), to(#111));
    }

    h1,
    h2,
    h3 {
      text-align: center;
      color: #FFF;
      margin: 5px 0;
    }

    h1 {
      font-size: 30px;
    }

    h2 a {
      font-size: 25px;
      color: #0184e3;
      text-decoration: none;
    }

    h3 {
      font-size: 23px;
      border-bottom: solid 3px #CCC;
      padding-bottom: 10px;
    }

    h3 a {
      color: #00e8ff;
      text-decoration: none;
    }

    h3 a:hover,
    h2 a:hover {
      text-decoration: underline;
    }

    .container {
      width: 800px;
      margin: auto;
      color: #FFF;
      font-size: 25px;
    }

    .container #content {
      border: dashed 2px #CCC;
      padding: 10px;
    }

    #reset {
      padding: 5px 10px;
      background: #4CAF50;
      border: none;
      color: #FFF;
      cursor: pointer;
    }

    #reset:hover {
      color: #4CAF50;
      background: #FFF;
    }

    #viewContent table {
      width: 100%;
    }

    #viewContent table tr {
      height: 80px;
      background: darkcyan;
    }

    #viewContent table tr td {
      width: 50%;
      padding-left: 5px;
    }
  </style>
</head>

<body>
  <div class="container">
    <div id="content">
      <h1>Implémentation de QRCoder dans ASP.NET Core - Créer un fichier de code QR</h1>
      <h2>
        <a href="http://www.yogihosting.com/category/aspnet-core/">Lire le tutoriel sur YogiHosting  </a>
        <button id="reset" onclick="location=''">Réinitialiser </button>
      </h2>
      <div id="viewContent">
        @using (Html.BeginForm(null, null, FormMethod.Post)) {
        <table>
          <tbody>
            <tr>
              <td>
                <label>Entrez le texte pour créer un fichier QR</label>
              </td>
              <td>
                <input type="text" name="qrText" />
              </td>
            </tr>
            <tr>
              <td colspan="2">
                <button>Soumettre</button>
              </td>
            </tr>
          </tbody>
        </table>
        }
      </div>
      @{ if (Model != null) {
      <h3>Fichier de code QR généré avec succès</h3>
      <img src="@String.Format(" data:image/png;base64,{0} ", Convert.ToBase64String(Model))" /> } }
    </div>
  </div>
</body>

</html>
```

Le code de cette vue est exactement similaire à la vue 'Index' et fonctionne exactement comme elle.

L'URL pour invoquer cette vue est 'http://localhost:50755/QRCoder/GenerateFile'.

### **Lire et afficher tous les fichiers de code QR (.qrr)**

Vous pouvez également lire tous les fichiers .qrr sauvegardés dans le site web. Allez dans votre contrôleur et ajoutez une nouvelle action appelée 'ViewFile' :

```
public IActionResult ViewFile()
{
  List<KeyValuePair<string, Byte[]>> fileData=new List<KeyValuePair<string, byte[]>>();
  
  KeyValuePair<string, Byte[]> data;
  string[] files = Directory.GetFiles("wwwroot/qrr");
  foreach (string file in files)
  {
    QRCodeData qrCodeData = new QRCodeData(file, QRCodeData.Compression.Uncompressed);
    
    QRCode qrCode = new QRCode(qrCodeData);
    Bitmap qrCodeImage = qrCode.GetGraphic(20);
    
    Byte[] byteData = BitmapToBytes(qrCodeImage);
    data = new KeyValuePair<string, Byte[]>(Path.GetFileName(file), byteData);
    fileData.Add(data);
  }
  return View(fileData);
}
```

Dans cette méthode d'action, je lis les fichiers situés dans le dossier 'qrr' en utilisant le code :

```
Directory.GetFiles("wwwroot/qrr")
```

Ensuite, j'ajoute les octets et le nom de chaque fichier qrr dans un objet `List<KeyValuePair<string, Byte[]>>`.

Cet objet est retourné à la vue à la fin :

```
return View(fileData);
```

Enfin, créez la vue 'ViewFile' dans le dossier 'Views/QRCoder' avec le code suivant :

```
@model List
<KeyValuePair<string, Byte[]>>
@{
    Layout = null;
}

  <!DOCTYPE html>
  <html>

  <head>
    <meta name="viewport" content="width=device-width" />
    <title>Implémentation de QRCoder dans ASP.NET Core - Voir les fichiers de code QR</title>
    <style>
      body {
        background: #111 no-repeat;
        background-image: -webkit-gradient(radial, 50% 0, 150, 50% 0, 300, from(#444), to(#111));
      }

      h1,
      h2,
      h3 {
        text-align: center;
        color: #FFF;
        margin: 5px 0;
      }

      h1 {
        font-size: 30px;
      }

      h2 a {
        font-size: 25px;
        color: #0184e3;
        text-decoration: none;
      }

      h3 {
        font-size: 23px;
        border-bottom: solid 3px #CCC;
        padding-bottom: 10px;
      }

      h3 a {
        color: #00e8ff;
        text-decoration: none;
      }

      h3 a:hover,
      h2 a:hover {
        text-decoration: underline;
      }

      .container {
        width: 800px;
        margin: auto;
        color: #FFF;
        font-size: 25px;
      }

      .container #content {
        border: dashed 2px #CCC;
        padding: 10px;
      }

      #reset {
        padding: 5px 10px;
        background: #4CAF50;
        border: none;
        color: #FFF;
        cursor: pointer;
      }

      #reset:hover {
        color: #4CAF50;
        background: #FFF;
      }

      #viewContent table {
        width: 100%;
      }

      #viewContent table tr {
        height: 80px;
        background: darkcyan;
      }

      #viewContent table tr td {
        width: 50%;
        padding-left: 5px;
      }

      #viewContent table tr td img {
        width: 150px;
      }

      #viewContent table tr td span {
        display: block;
      }
    </style>
  </head>

  <body>
    <div class="container">
      <div id="content">
        <h1>Implémentation de QRCoder dans ASP.NET Core - Voir les fichiers de code QR</h1>
        <h2>
          <a href="http://www.yogihosting.com/category/aspnet-core/">Lire le tutoriel sur YogiHosting  </a>
          <button id="reset" onclick="location=''">Réinitialiser </button>
        </h2>
        <div id="viewContent">
          <table>
            <tbody>
              @foreach (KeyValuePair
              <string, Byte[]> k in Model) {
                <tr>
                  <td>
                    <img src="@String.Format(" data:image/png;base64,{0} ", Convert.ToBase64String(k.Value))" />
                    <span>@k.Key</span>
                  </td>
                </tr>
                }
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </body>

  </html>
```

Cette vue affiche tous les fichiers qrr sous forme d'images bitmap dans un tableau HTML. Le code ci-dessous crée le tableau HTML :

```
<table>
  <tbody>
    @foreach (KeyValuePair<string, Byte[]> k in Model)
    {
      <tr>
        <td>
          <img src="@String.Format("data:image/png;base64,{0}", Convert.ToBase64String(k.Value))" />
         <span>@k.Key</span>
        </td>
      </tr>
    }
  </tbody>
</table>
```

#### **Test du code**

Exécutez votre application et allez à l'URL — 'http://localhost:50755/QRCoder/ViewFile' pour invoquer la méthode d'action ViewFile. Vous verrez tous les fichiers .qrr sauvegardés dans votre site web.

Voir l'image ci-dessous qui l'illustre en fonctionnement :

![Image](https://cdn-media-1.freecodecamp.org/images/S3jNmNaLIW0QuUy5qo9GV36lgPia8-qEgB2s)
_**Voir tous les fichiers QRR**_

[**Vous pouvez télécharger le code complet depuis mon dépôt GitHub**](https://github.com/yogyogi/QRCoder-implemented-in-ASP.NET-Core).

### **Conclusion**

J'espère que vous aimez ce dépôt qui vous aidera à utiliser QRCoder dans votre projet ASP.NET Core. Assurez-vous de liker ce dépôt pour montrer votre amour pour lui.

Si vous avez besoin d'aide en ASP.NET Core, faites-le moi savoir dans la section des commentaires ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/hHGcaGHoUc9cjgZiK5W7uBls4YgSY5wPewfR)

_Je publie 2 articles de développement web par semaine. Envisagez de me suivre et recevez une notification par email chaque fois que je publie un nouveau tutoriel sur Medium. Si cet article vous a été utile, veuillez cliquer sur le bouton d'applaudissements plusieurs fois pour montrer votre soutien ! Cela mettra un sourire sur mon visage et me motivera à écrire davantage pour les lecteurs comme vous._

J'ai également publié un autre tutoriel sur freeCodeCamp, si vous souhaitez le voir aussi — [Comment créer une fonctionnalité de connexion avec Bootstrap Modal et jQuery AJAX](https://medium.freecodecamp.org/how-to-create-a-login-feature-with-bootstrap-modal-and-jquery-ajax-53dc0d281609)

Merci et bon codage !