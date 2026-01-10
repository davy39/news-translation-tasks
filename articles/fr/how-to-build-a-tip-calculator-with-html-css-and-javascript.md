---
title: Comment créer une calculatrice de pourboire avec HTML, CSS et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T17:51:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-tip-calculator-with-html-css-and-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dfa740569d1a4ca3aaf.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
seo_title: Comment créer une calculatrice de pourboire avec HTML, CSS et JavaScript
seo_desc: "A Tip Calculator is a calculator that calculates a tip based on the percentage\
  \ of the total bill.\nLet's build one now.\nStep 1 - HTML:\nWe create a form in\
  \ order to enter the preferred amount:\n<!doctype html>\n<html lang=\"en\">\n  <head>\n\
  \    <title>Tip Ca..."
---

Une calculatrice de pourboire est un outil qui calcule un pourboire en fonction du pourcentage du total de la facture.

Créons-en une maintenant.

## **Étape 1 - HTML :**

Nous créons un formulaire afin de saisir le montant souhaité :

```html
<!doctype html>
<html lang="fr">
  <head>
    <title>Calculatrice de pourboire</title>
    <!-- Balises meta requises -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- CSS Bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">


   
  </head>
  <body class="bg-dark">
    <div class="container">
      <div class="row">
        <div class="col-md-6 mx-auto">
          <div class="card card-body text-center mt-5">
            <h1 class="heading display-5 pb-3">Calculatrice de pourboire</h1>
            <form id="tip-form">
              <div class="form-group">
                <div class="input-group">
                  <span class="input-group-addon">$</span>
                  <input type="number" class="form-control" id="billTotal" placeholder="Total de la facture">
                </div>
              </div>
              <div class="form-group tipPersent">
                <div class="input-group">
                  <label for="">Pourboire :</label>


                  <input type="range" class="form-control" id="tipInput" value="0">
                  <span class="input-group-addon" id="tipOutput"></span>
                </div>
              </div>



            </form>
            <hr>

            <!-- RÉSULTATS -->
            <div id="results" class="pt-4">
              <h5>Résultats</h5>
              <div class="form-group">
                <div class="input-group">
                  <span class="input-group-addon">Montant du pourboire</span>
                  <input type="number" class="form-control" id="tipAmount" disabled>
                </div>
              </div>

              <div class="form-group">
                <div class="input-group">
                  <span class="input-group-addon">Total de la facture avec pourboire</span>
                  <input type="number" class="form-control" id="totalBillWithTip" disabled>
                </div>
              </div>


            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- JavaScript optionnel -->
    <!-- jQuery d'abord, puis Popper.js, puis Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>

  </body>
</html>
```

## **Étape 2 - CSS :**

Vous concevez le style comme vous le souhaitez. Vous pouvez également utiliser CSS pour masquer les résultats et les afficher via JavaScript après que l'utilisateur ait rempli le formulaire :

```css
  #results {
         display:none;
       }
```

## **Étape 3 : JavaScript :**

Nous ajoutons un événement onchange. L'événement onchange se produit lorsque l'utilisateur interagit avec le formulaire.

Cette action exécutera une fonction qui calcule le montant final de la facture en fonction du pourcentage de pourboire, puis retourne les résultats.

```javascript
document.querySelector('#tip-form').onchange = function(){

  var bill = Number(document.getElementById('billTotal').value);
  var tip = document.getElementById('tipInput').value;
  document.getElementById('tipOutput').innerHTML = `${tip}%`;
  var tipValue = bill * (tip/100)
  var finalBill = bill + tipValue
console.log(finalBill)
var tipAmount = document.querySelector('#tipAmount')
var totalBillWithTip = document.querySelector('#totalBillWithTip')

tipAmount.value = tipValue.toFixed(2);
 totalBillWithTip.value =finalBill.toFixed(2);

 //Afficher les résultats

  document.getElementById('results').style.display='block'
}
```

Vous pouvez voir un exemple fonctionnel et son code sur [Codepen.io](https://codepen.io/voula12/pen/djrZGw).