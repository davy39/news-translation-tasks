---
title: Comment déployer un modèle de Machine Learning en tant qu'application Web en
  utilisant Gradio
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-06-01T15:14:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-machine-learning-model-as-a-web-app-using-gradio
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/deploy-ml-models-article.jpeg
tags:
- name: deployment
  slug: deployment
- name: Machine Learning
  slug: machine-learning
- name: Web Applications
  slug: web-applications
seo_title: Comment déployer un modèle de Machine Learning en tant qu'application Web
  en utilisant Gradio
seo_desc: 'You''ve built your Machine Learning model with 99% accuracy and now you
  are ecstatic. You are like yaaaaaaaaay! My model performed well.

  Then you paused and you were like – now what?

  Well first, you might have thought of uploading your code to GitHub ...'
---

Vous avez construit votre modèle de Machine Learning avec une précision de 99 % et maintenant vous êtes ravi. Vous êtes comme yaaaaaaaaay ! Mon modèle a bien performé.

Puis vous vous êtes arrêté et vous vous êtes dit – et maintenant ?

Eh bien, d'abord, vous avez peut-être pensé à télécharger votre code sur GitHub et à montrer aux gens votre fichier Jupyter notebook. Il comprend ces visualisations magnifiques que vous avez créées avec Seaborn, ces modèles d'ensemble extrêmement puissants, et comment ils sont capables de passer leurs métriques d'évaluation, etc.

Mais ensuite, vous avez remarqué que personne n'interagit avec.

Eh bien, mon ami, pourquoi ne pas essayer de déployer le modèle en tant qu'application web afin que les non-techniciens puissent également interagir avec le modèle ? Parce que seuls les programmeurs comme vous comprendront probablement cette première approche.

Il existe plusieurs méthodes pour déployer votre modèle, mais nous allons nous concentrer sur l'une d'entre elles dans cet article : l'utilisation de Gradio. Je peux vous dire que vous êtes excité. Eh bien, détendez-vous et profitez, car cela va être un voyage passionnant.

# Prérequis

Avant de commencer ce voyage, je suppose que vous avez les connaissances suivantes :

1. Vous savez comment créer une fonction définie par l'utilisateur en Python
   
2. Vous pouvez construire et ajuster un modèle de ML
   
3. Votre environnement est prêt
   

# Qu'est-ce que Gradio ?

[Gradio](https://gradio.app/) est une bibliothèque Python gratuite et open-source qui vous permet de développer une démonstration de composant personnalisable facile à utiliser pour votre modèle de machine learning que n'importe qui peut utiliser n'importe où.

Gradio s'intègre avec les bibliothèques Python les plus populaires, y compris Scikit-learn, PyTorch, NumPy, seaborn, pandas, Tensor Flow, et d'autres.

L'un de ses avantages est qu'il vous permet d'interagir avec l'application web que vous développez actuellement dans votre Jupyter ou Colab notebook. Il possède de nombreuses fonctionnalités uniques qui peuvent vous aider à construire une application web avec laquelle les utilisateurs peuvent interagir.

# Comment installer Gradio

Pour utiliser Gradio, nous devons d'abord installer sa bibliothèque sur notre PC local. Alors, allez dans votre Conda PowerShell ou terminal et exécutez la commande suivante. Si vous utilisez Google Colab, vous pouvez également taper ce qui suit :

```javascript
pip install gradio
```

Nous avons maintenant Gradio installé sur notre PC local. Passons en revue quelques-unes des bases de Gradio pour que nous puissions nous familiariser avec la bibliothèque.

Pour commencer, nous devons importer la bibliothèque dans notre notebook ou IDE, selon ce que vous utilisez. Nous pouvons le faire en tapant la commande suivante :

```javascript
import gradio as gr
```

# Comment créer votre première application Web

Dans ce tutoriel, nous allons créer une application de salutation exemple pour nous familiariser avec les bases de Gradio.

Pour ce faire, nous devons écrire une fonction de salutation car Gradio fonctionne avec des fonctions définies par l'utilisateur en Python. En conséquence, notre fonction de salutation ressemble à ceci :

```py
def greet_user(name):
	return "Bonjour " + name + " Bienvenue sur Gradio !😎"
```

Nous devons maintenant déployer la fonction Python sur Gradio afin qu'elle puisse agir comme une application web. Pour ce faire, nous tapons :

```py
app =  gr.Interface(fn = greet_user, inputs="text", outputs="text")
app.launch()
```

Analysons et comprenons ce qui se passe dans le code ci-dessus avant de l'exécuter.

`gr.Interface` : Cet attribut sert de fondement à tout dans Gradio. C'est l'interface utilisateur qui affiche tous les composants qui seront montrés sur le web.

Le paramètre `fn` : Il s'agit de la fonction Python que vous avez créée et que vous souhaitez fournir à Gradio.

Le paramètre `inputs` : Ce sont les composants que vous souhaitez passer dans la fonction que vous avez créée, tels que des mots, des images, des nombres, de l'audio, etc. Dans notre cas, la fonction que nous avons créée nécessitait du texte, nous l'avons donc entré dans les paramètres d'entrée.

Le paramètre `output` : Il s'agit d'un paramètre qui vous permet d'afficher le composant sur l'interface que vous souhaitez voir. Parce que la fonction que nous avons créée dans cet exemple doit afficher du texte, nous fournissons le composant texte au paramètre de sortie.

`app.launch` est utilisé pour lancer l'application. Vous devriez avoir quelque chose comme ceci lorsque vous exécutez le code ci-dessus :

![alt_text](https://www.freecodecamp.org/news/content/images/2022/05/Gradio-pro.png align="left")

Une fois que l'interface Gradio apparaît, tapez simplement votre nom et cliquez sur soumettre. Ensuite, il affiche le résultat dans la fonction que nous avons créée ci-dessus. Maintenant que nous avons terminé cela, passons en revue une autre chose dans Gradio avant d'apprendre comment déployer notre modèle.

Nous allons créer une application Gradio qui peut accepter deux entrées et fournir une sortie. Cette application demande simplement votre nom et une valeur, puis affiche vos noms ainsi que les multiples de la valeur que vous avez entrée. Pour ce faire, tapez simplement le code ci-dessous :

```py
def return_multiple(name, number):
    result = "Salut {} ! 😎. Le multiple de {} est {}".format(name, number, round(number**2, 2))
    return result

app = gr.Interface(fn = return_multiple, inputs=["text", gr.Slider(0, 50)], outputs="text")
app.launch()
```

![alt_text](https://www.freecodecamp.org/news/content/images/2022/05/gradio-2.png align="left")

Maintenant que nous avons fait cela, passons rapidement en revue certaines des choses que nous avons faites ici et que vous ne connaissez peut-être pas.

Paramètre d'entrée : Dans le paramètre d'entrée, nous avons créé une liste qui implique deux composants, le texte et le curseur. Le curseur est également l'un des attributs de Gradio qui retourne une valeur flottante lorsque vous glissez sur une plage donnée. Nous avons utilisé cela parce que dans la fonction que nous avons créée, nous attendons un texte et une valeur.

Nous devons ordonner le composant dans le paramètre d'entrée de la manière dont nos attributs sont ordonnés dans la fonction que nous avons créée ci-dessus. C'est-à-dire, le texte d'abord avant le nombre. Donc ce que nous attendons pour la sortie est en fait une chaîne. Nous avons simplement fait un peu de formatage dans la fonction ci-dessus.

Maintenant que nous nous sommes familiarisés avec certaines des bases de Gradio, créons un modèle que nous allons déployer.

# Comment déployer un modèle de Machine Learning sur Gradio

Dans cette section, j'utiliserai un modèle de classification que j'ai précédemment entraîné et sauvegardé dans un fichier pickle.

Lorsque vous créez un modèle qui prend beaucoup de temps à entraîner, la méthode la plus efficace pour le gérer est de le sauvegarder dans un fichier pickle une fois l'entraînement terminé afin de ne pas avoir à subir le stress de l'entraînement du modèle à nouveau.

Si vous souhaitez sauvegarder un modèle en tant que fichier pickle, laissez-moi vous montrer comment vous pouvez faire cela. D'abord, importez la bibliothèque pickle, puis tapez le code ci-dessous. Supposons que je veux simplement ajuster un modèle comme ceci :

```python
import pickle
```

```javascript
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train) 

# Si vous avez ajusté le modèle, tapez simplement ceci pour le sauvegarder : N'oubliez pas de changer le nom du fichier
with open("filename.pkl", "wb") as f:
pickle.dump(clf, f)
```

Maintenant, si vous souhaitez le charger, vous pouvez taper le code suivant également :

```py
with open("filename.pkl", "rb") as f:
	clf  = pickle.load(f)
```

Maintenant que nous avons compris cela, créons une fonction que nous pourrons passer à Gradio afin qu'elle puisse faire les prédictions.

```python
def make_prediction(age, employment_status, bank_name, account_balance):
    with open("filename.pkl", "rb") as f:
        clf  = pickle.load(f)
        preds = clf.predict([[age, employment_status, bank_name, account_balance]])
    if preds == 1:
            return "Vous êtes éligible pour le prêt"
    return "Vous n'êtes pas éligible pour le prêt"

#Créer le composant d'entrée pour Gradio puisque nous attendons 4 entrées

age_input = gr.Number(label = "Entrez l'âge de l'individu")
employment_input = gr.Number(label= "Entrez le statut d'emploi {1:Pour employé, 2: Pour sans emploi}")
bank_input = gr.Textbox(label = "Entrez le nom de la banque")
account_input = gr.Number(label = "Entrez votre solde de compte :")
# Nous créons la sortie
output = gr.Textbox()


app = gr.Interface(fn = make_prediction, inputs=[age_input, employment_input, bank_input, account_input], outputs=output)
app.launch()
```

![alt_text](https://www.freecodecamp.org/news/content/images/2022/05/bank2.png align="left")

Alors, déballons ce que nous avons ci-dessus :

Nous commencerons au point où nous avons créé le composant d'entrée. Vous pouvez choisir de créer le composant dans `gr.Interface`, mais dans le code suivant, je l'ai construit directement à l'extérieur de `gr.Interface` puis j'ai fourni la variable dans `gr.Interface`.

Donc, si vous voulez faire un composant qui reçoit des nombres, utilisez `gr.Number`, puis à partir de la variable de sortie que j'ai créée, vous pouvez passer du texte comme nous l'avons fait précédemment dans notre première application (la chaîne "text" est un raccourci pour textbox si vous ne voulez pas déclarer l'attribut explicitement).

J'ai également utilisé le paramètre label dans chaque composant afin que l'utilisateur sache quoi faire. Nous sommes déjà familiers avec le reste du code mentionné ci-dessus. Et maintenant que nous avons fait cela, notre modèle est déployé. 🎉🎉😎🤗🤗.

# Conclusion

Merci d'avoir lu ce tutoriel. Nous avons couvert beaucoup de choses dans cet article. Rappelez-vous simplement que l'apprentissage de Gradio ne s'arrête pas ici – vous pouvez consulter plus d'informations sur leur [site web](https://gradio.app/). Ils ont une documentation assez intuitive sur la façon dont vous pouvez créer votre application web.

Merci encore une fois pour la lecture. Si vous avez aimé cet article, vous pouvez me soutenir en me suivant sur [LinkedIn](https://www.linkedin.com/in/ibrahimogunbiyi/) ou [Twitter](https://twitter.com/Comejoinfolks). Gracias, et bon déploiement😀