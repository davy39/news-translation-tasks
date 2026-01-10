---
title: Ajoutez un blog à votre site web avec React et l'API WordPress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-26T11:01:05.000Z'
originalURL: https://freecodecamp.org/news/get-a-blog-on-your-website-with-react-and-wordpress-api-c63ff81b388e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ElZM2hjwYLDE29GCAmYxoA.jpeg
tags:
- name: blog
  slug: blog
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: WordPress
  slug: wordpress
seo_title: Ajoutez un blog à votre site web avec React et l'API WordPress
seo_desc: 'By Sam Williams

  I’ve read a lot of articles in the last few months, and have noticed that many had
  disclaimers saying that the post was originally posted on a personal blog. I’ve
  written a few articles and wanted to increase my exposure, so I decided...'
---

Par Sam Williams

J'ai lu beaucoup d'articles au cours des derniers mois et j'ai remarqué que beaucoup avaient des avertissements disant que l'article avait été initialement publié sur un blog personnel. J'ai écrit quelques articles et je voulais augmenter ma visibilité, alors j'ai décidé que je voulais aussi avoir un blog sur mon site. Mais comment faire ?

### Options

Il y avait quelques options pour incorporer un blog à mon site. Les deux principales étaient un système de gestion de contenu (CMS) personnalisé ou WordPress. Je voulais le mettre en place rapidement, alors j'ai choisi WordPress.

### API WordPress

J'avais entendu parler de l'API WordPress au cours des dernières semaines, alors j'ai commencé à chercher sur Google. J'ai créé un blog gratuit sur [WordPress.com](http://wordpress.com) et j'ai importé mes articles depuis Medium. Cela a été très simple grâce à la fonction d'exportation de Medium et à la fonction "importer depuis Medium" de WordPress.

Maintenant que mes articles étaient sur WordPress, je devais trouver comment y accéder. J'ai trouvé [cette page](https://developer.wordpress.com/docs/api/) dans la documentation et j'ai construit une page web très basique pour tester.

```html
<h1>vérificateur wordpress</h1>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>

<script src="getWordpress.js"></script>
```

```js
console.log("ceci est une preuve de concept");

$.get(
  "https://public-api.wordpress.com/rest/v1/sites/VotreSite.wordpress.com/posts",
  function(response) {
    console.log(response);
  }
);
```

Cela effectue la tâche très simple d'appeler l'API WordPress et de demander tous les articles de "VotreSite.wordpress.com". À partir de cela, j'ai obtenu un objet de réponse contenant le nombre d'articles et un tableau de chacun des articles.

### Routage

Maintenant que j'allais ajouter une section blog à mon site, je devais passer de la seule page que j'avais. J'ai installé react-router-dom et importé `BrowserRouter` et `Route` dans mon fichier de mise en page.

```html
<BrowserRouter>
    <div id="center-stripe">
        <Nav />
        <Route exact path="/" component={main} />
        <Route exact path="/blog" component={Blog} />
    </div>
</BrowserRouter>
```

### Création du Blog en React

Mon site web personnel est construit en utilisant create-react-app et a une structure très basique. La prochaine chose que je devais faire était d'ajouter une nouvelle page "blog" qui afficherait les aperçus de tous les articles.

```js
export default class Blog extends Component {
  constructor(props) {
    super(props);
    this.state = {
      posts: []
    };
  }
  componentDidMount() {
    axios
      .get(
        "http://public-api.wordpress.com/rest/v1/sites/samwcoding.wordpress.com/posts"
      )
      .then(res => {
        this.setState({ posts: res.data.posts });
        console.log(this.state.posts);
      })
      .catch(error => console.log(error));
  }

  render() {
    return (
      <div className="blog">
        <h1 className="sectionTitle">Articles</h1>
        {this.state.posts.map(post => <ArticlePreview post={post} />)}
      </div>
    );
  }
}
```

Je vais vous expliquer ce code. La section supérieure définit l'état du composant avec un tableau vide de posts. Ensuite, j'utilise la fonction `componentDidMount` pour exécuter l'appel à l'API WordPress avec axios. Lorsque l'appel à l'API retourne, je définis this.state.posts pour qu'il soit le tableau des posts. Cela provoque ensuite la ligne 24 pour rendre un composant `ArticlePreview` pour chacun des posts.

```js
render() {
    if (this.props.post) {
      return (
        <div className="article">
          <a href={"/blog/" + this.props.post.ID} className="blackLink">
            {this.props.post.featured_image ? (
              <img
                className="img-responsive webpic"
                alt="en-tête de l'article"
                src={this.props.post.featured_image}
              />
            ) : (
              ""
            )}
            <h1 className="text-center">{this.props.post.title}</h1>
            <div className="content">{excerpt}</div>
          </a>
          <Link to={"/blog/" + this.props.post.ID}>
            <button className="btn">Lire la suite</button>
          </Link>
        </div>
      );
    } else {
      return null;
    }
  }
```

ArticlePreview prend chaque post et rend l'aperçu avec un titre et un extrait, tous deux fournis par l'API WordPress. Si le post a également une image à la une, il l'inclut également.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zygv4F72-f7w_6fiepGFvA.png)
_Aperçus de l'API WordPress_

J'ai réutilisé beaucoup de CSS du reste du site web pour styliser les aperçus des articles, et cela a l'air assez bien. Une erreur majeure est le "<p>I&#8217;" et des morceaux similaires disséminés dans l'extrait. Pour résoudre cela, j'ai défini l'extrait pour qu'il passe par une fonction `removeUnicode()` avant d'être rendu à l'écran. Elle a simplement remplacé tous les `&#8217` par une simple virgule et a supprimé les balises `<p> et [&hellip;]`. Ce n'est pas élégant, mais cela fonctionne.

J'ai ensuite dû créer un composant pour les articles complets. J'ai ajouté une autre route pour `/blog/:id` et j'ai commencé le nouveau composant. Il était presque identique au composant `ArticlePreview`, sauf qu'au lieu de rendre uniquement l'extrait, il rendait un article. Obtenir l'article de WordPress était très simple, il suffisait d'ajouter l'ID de l'article à la fin de l'appel précédent à l'API.

```js
axios.get(
    "http://public-api.wordpress.com/rest/v1/sites/samwcoding.wordpress.com/posts/" +
    this.props.match.params.id
)
```

Obtenir la réponse de l'article est là que j'ai rencontré mon premier obstacle. Le corps de l'article était au format HTML stringifié. J'ai trouvé une solution avec la fonction `dangerouslySetInnerHTML`. _(Si quelqu'un a des suggestions sur la façon de mieux implémenter cela, faites-le moi savoir.)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*cePHka90ljGiCw4Sfsp2qw.png)
_Article fonctionnel_

J'avais quelques autres changements à faire. Les boutons de navigation en haut étaient simplement connectés à des balises d'ancrage. Cela fonctionnait bien sur un site web à page unique, mais maintenant ils envoyaient les utilisateurs à `/blog#about`, ce qui ne fonctionne pas. Cela a été résolu en définissant le lien spécifiquement comme `/#about` et `/#projects`.

Le blog fonctionne bien avec le nombre d'articles que j'ai actuellement écrits, mais comment va-t-il gérer 50 ou 100 articles ? À l'avenir, je devrai peut-être rendre quelques aperçus d'articles à la fois, en rendant plus si l'utilisateur fait défiler jusqu'en bas. Une autre fonctionnalité que je pourrais ajouter est la recherche.

Consultez le blog à l'adresse [SamWSoftware blog](https://samwsoftware.herokuapp.com/blog) et voyez mon code entier [ici](https://github.com/SamWSoftware/NodePortfolio).