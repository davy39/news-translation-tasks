---
title: How to Build a Tip Calculator with HTML, CSS, and JavaScript
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
seo_title: null
seo_desc: "A Tip Calculator is a calculator that calculates a tip based on the percentage\
  \ of the total bill.\nLet's build one now.\nStep 1 - HTML:\nWe create a form in\
  \ order to enter the preferred amount:\n<!doctype html>\n<html lang=\"en\">\n  <head>\n\
  \    <title>Tip Ca..."
---

A Tip Calculator is a calculator that calculates a tip based on the percentage of the total bill.

Let's build one now.

## **Step 1 - HTML:**

We create a form in order to enter the preferred amount:

```html
<!doctype html>
<html lang="en">
  <head>
    <title>Tip Calculator</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">


   
  </head>
  <body class="bg-dark">
    <div class="container">
      <div class="row">
        <div class="col-md-6 mx-auto">
          <div class="card card-body text-center mt-5">
            <h1 class="heading display-5 pb-3">Tip Calculator</h1>
            <form id="tip-form">
              <div class="form-group">
                <div class="input-group">
                  <span class="input-group-addon">$</span>
                  <input type="number" class="form-control" id="billTotal" placeholder="Total Bill">
                </div>
              </div>
              <div class="form-group tipPersent">
                <div class="input-group">
                  <label for="">Tip:</label>


                  <input type="range" class="form-control" id="tipInput" value="0">
                  <span class="input-group-addon" id="tipOutput"></span>
                </div>
              </div>



            </form>
            <hr>

            <!-- RESULTS -->
            <div id="results" class="pt-4">
              <h5>Results</h5>
              <div class="form-group">
                <div class="input-group">
                  <span class="input-group-addon">Tip amount</span>
                  <input type="number" class="form-control" id="tipAmount" disabled>
                </div>
              </div>

              <div class="form-group">
                <div class="input-group">
                  <span class="input-group-addon">Total Bill with Tip</span>
                  <input type="number" class="form-control" id="totalBillWithTip" disabled>
                </div>
              </div>


            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>

  </body>
</html>
```

## **Step 2 - CSS:**

You design the style however you want. You can also use CSS to hide the results and show them through JavaScript after the user fills in the form:

```css
  #results {
         display:none;
       }
```

## **Step 3: JavaScript:**

We add an onchange event. The onchange event occurs when the user interacts with the form.

This action will execute a function that computes the final bill amount based on the percentage tip, then returns the results.

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

 //Show Results

  document.getElementById('results').style.display='block'
}
```

You can see a working example and its code on [Codepen.io](https://codepen.io/voula12/pen/djrZGw).

