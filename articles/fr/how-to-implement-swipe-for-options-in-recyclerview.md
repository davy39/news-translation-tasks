---
title: Comment implémenter 'Glisser pour les options' dans RecyclerView
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-18T23:09:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-swipe-for-options-in-recyclerview
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aef740569d1a4ca28ba.jpg
tags:
- name: Java
  slug: java
- name: 'RecyclerView  '
  slug: recyclerview
- name: user experience
  slug: user-experience
seo_title: Comment implémenter 'Glisser pour les options' dans RecyclerView
seo_desc: "By Gagandeep Singh\nLet's say a user of your site wants to edit a list\
  \ item without opening the item and looking for editing options. If you can enable\
  \ this functionality, it gives that user a good User Experience. \nPocket, a bookmarking\
  \ app owned by ..."
---

Par Gagandeep Singh

Supposons qu'un utilisateur de votre site souhaite modifier un élément de liste sans ouvrir l'élément et rechercher les options de modification. Si vous pouvez activer cette fonctionnalité, cela offre à cet utilisateur une **bonne expérience utilisateur**. 

[Pocket](https://play.google.com/store/apps/details?id=com.ideashower.readitlater.pro&hl=en_IN), une application de marque-pages appartenant à Mozilla, fait quelque chose de similaire. Vous pouvez partager/archiver/supprimer vos articles sauvegardés directement depuis la liste sans ouvrir l'article. Ensuite, vous pouvez cliquer sur le bouton de menu dans le coin supérieur droit et sélectionner votre option de modification.

Donc, dans ce tutoriel, nous allons essayer de coder cela.

**Voici ce que nous voulons réaliser** :

![Image](https://www.freecodecamp.org/news/content/images/2024/08/recycler-view-example.jpg)

## Commençons par créer une liste RecyclerView normale

RecyclerView est une version avancée et flexible de ListView et GridView. Il est capable de contenir de grandes quantités de données de liste et a de meilleures performances que ses prédécesseurs. 

Comme son nom l'indique, RecyclerView "recycle" les éléments de notre liste une fois qu'ils sont hors de vue lors du défilement et les réutilise lorsqu'ils reviennent à la vue. Ainsi, le conteneur de liste n'a à maintenir qu'un nombre limité de vues et non la liste entière.

Il est si flexible que la nouvelle classe [ViewPager2](https://developer.android.com/training/animation/vp2-migration#diffutil), utilisée pour créer des onglets balayables, est écrite sur RecyclerView.

### Créer un POJO (Plain Old Java Object) pour contenir les données de la liste

```java
public class RecyclerEntity {
    private String title;
    private boolean showMenu = false;
    private int image;

    public RecyclerEntity() {
    }

    public RecyclerEntity(String title, int image, boolean showMenu) {
        this.title = title;
        this.showMenu = showMenu;
        this.image = image;
    }

    public int getImage() {
        return image;
    }

    public void setImage(int image) {
        this.image = image;
    }
    
    //... tous les getters et setters
}
```

Remarquez que nous avons un membre showMenu ici qui gérera la visibilité du menu pour cet élément de liste dans notre RecyclerView.

### Créer un adaptateur RecyclerView

```java
public class RecyclerAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {
    List<RecyclerEntity> list;
    Context context;

    public RecyclerAdapter(Context context, List<RecyclerEntity> articlesList) {
        this.list = articlesList;
        this.context = context;
    }

    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View v;
            v= LayoutInflater.from(parent.getContext()).inflate(R.layout.recycler_list, parent, false);
            return new MyViewHolder(v);
    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder holder, final int position) {
        RecyclerEntity entity = list.get(position);
        if(holder instanceof MyViewHolder){
            ((MyViewHolder)holder).title.setText(entity.getTitle());
            ((MyViewHolder)holder).imageView.setImageDrawable(context.getResources().getDrawable(entity.getImage()));
        }
    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder {
        TextView title;
        ImageView imageView;
        ConstraintLayout container;

        public MyViewHolder(View itemView) {
            super(itemView);
            title = itemView.findViewById(R.id.title);
            imageView = itemView.findViewById(R.id.imageView);
            container = itemView.findViewById(R.id.container);
        }
    }
}
```

Habituellement, nous plaçons notre sous-classe ViewHolder (MyViewHolder) dans le modèle de la super classe. Cela nous permet de retourner directement notre objet de sous-classe ViewHolder défini à partir de la méthode onCreateViewHolder(). Ensuite, nous n'avons pas à le caster à nouveau dans la méthode onBindViewHolder(). 

Mais ici, nous ne pouvons pas faire cela, et nous allons apprendre pourquoi dans un instant. 

### Initialiser le RecyclerView dans l'activité

```java
public class MainActivity extends AppCompatActivity {
    RecyclerView recyclerView;
    List<RecyclerEntity> list;
    RecyclerAdapter adapter;


    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerview);
        list = new ArrayList<>();

        list.add(new RecyclerEntity("This is the best title", R.drawable.one, false));
        list.add(new RecyclerEntity("This is the second-best title", R.drawable.two, false));
		//... reste des éléments de la liste
        
        adapter = new RecyclerAdapter(this, list);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(adapter);
    }
}
```

Maintenant, commençons à rendre les choses un peu plus intéressantes.

## Créer une ressource de mise en page pour le menu 

Et l'initialiser dans l'adaptateur Recycler :

```java
public class RecyclerAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {
    List<RecyclerEntity> list;
    Context context;
    private final int SHOW_MENU = 1;
    private final int HIDE_MENU = 2;

    public RecyclerAdapter(Context context, List<RecyclerEntity> articlesList) {
        this.list = articlesList;
        this.context = context;
    }

    @Override
    public int getItemViewType(int position) {
        if(list.get(position).isShowMenu()){
            return SHOW_MENU;
        }else{
            return HIDE_MENU;
        }
    }

    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View v;
        if(viewType==SHOW_MENU){
            v= LayoutInflater.from(parent.getContext()).inflate(R.layout.recycler_menu, parent, false);
            return new MenuViewHolder(v);
        }else{
            v= LayoutInflater.from(parent.getContext()).inflate(R.layout.recycler_list, parent, false);
            return new MyViewHolder(v);
        }

    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder holder, final int position) {
        RecyclerEntity entity = list.get(position);
        if(holder instanceof MyViewHolder){
        	//... même chose que ci-dessus
        }
        
        if(holder instanceof MenuViewHolder){
            //Actions du menu
        }

    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder {
        //... même chose que ci-dessus
    }
    //Notre vue de menu
    public class MenuViewHolder extends RecyclerView.ViewHolder{
        public MenuViewHolder(View view){
            super(view);
        }
    }
}
```

Maintenant, nous avons deux sous-classes ViewHolder dans notre adaptateur, MyViewHolder (l'élément réel de la liste) et MenuViewHolder. Les deux héritent de la même classe, donc nous retournons la classe parente _RecyclerView.ViewHolder_ à partir de onCreateViewHolder(). 

Notre méthode getItemViewType() retourne la variable int (viewType) qui indique le type de vue que nous voulons afficher dans notre RecyclerView pour une position particulière : c'est-à-dire, soit MyViewHolder soit MenuViewHolder. 

Cette variable viewType est ensuite utilisée par onCreateViewHolder() qui retourne effectivement l'objet ViewHolder respectif.

## Ajouter les fonctions pour afficher/masquer le menu dans RecyclerAdapter

```java
public void showMenu(int position) {
        for(int i=0; i<list.size(); i++){
            list.get(i).setShowMenu(false);
        }
        list.get(position).setShowMenu(true);
        notifyDataSetChanged();
    }


    public boolean isMenuShown() {
        for(int i=0; i<list.size(); i++){
            if(list.get(i).isShowMenu()){
                return true;
            }
        }
        return false;
    }

    public void closeMenu() {
        for(int i=0; i<list.size(); i++){
            list.get(i).setShowMenu(false);
        }
        notifyDataSetChanged();
    }
```

Notez qu'il existe de nombreuses façons de gérer cela. Mais pour des raisons de simplicité, nous conservons une valeur booléenne dans notre POJO pour maintenir la visibilité du menu.

Après avoir modifié notre liste de données, nous appelons la méthode notifyDataSetChanged() pour redessiner la liste. 

## Afficher le menu lors d'un appui long sur notre élément de liste dans RecyclerAdapter

```java
@Override
    public void onBindViewHolder(RecyclerView.ViewHolder holder, final int position) {
        RecyclerEntity entity = list.get(position);
        if(holder instanceof MyViewHolder){
            ((MyViewHolder)holder).title.setText(entity.getTitle());
            ((MyViewHolder)holder).imageView.setImageDrawable(context.getResources().getDrawable(entity.getImage()));

            ((MyViewHolder)holder).container.setOnLongClickListener(new View.OnLongClickListener() {
                @Override
                public boolean onLongClick(View v) {
                    showMenu(position);
                    return true;
                }
            });
        }
        if(holder instanceof MenuViewHolder){
            //Définir les actions du menu comme :
            //((MenuViewHolder)holder).edit.setOnClickListener(null);
        }

    }
```

Encore une fois, la définition des événements sur nos vues peut également être faite de diverses manières. 

Dans notre exemple, nous avons trois actions dans notre menu. Vous pouvez écrire votre logique pour gérer ces actions dans la deuxième instruction if comme montré dans les commentaires.

## Afficher le menu lors d'un balayage 

Pour ce faire, nous ajoutons un helper de toucher dans notre MainActivity.java :

```java
public class MainActivity extends AppCompatActivity {
    RecyclerView recyclerView;
    List<RecyclerEntity> list;
    RecyclerAdapter adapter;


    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //... même chose que ci-dessus 
         
        adapter = new RecyclerAdapter(this, list);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(adapter);

        ItemTouchHelper.SimpleCallback touchHelperCallback = new ItemTouchHelper.SimpleCallback(0, ItemTouchHelper.LEFT) {
            private final ColorDrawable background = new ColorDrawable(getResources().getColor(R.color.background));

            @Override
            public boolean onMove(RecyclerView recyclerView, RecyclerView.ViewHolder viewHolder, RecyclerView.ViewHolder target) {
                return false;
            }

            @Override
            public void onSwiped(RecyclerView.ViewHolder viewHolder, int direction) {
                adapter.showMenu(viewHolder.getAdapterPosition());
            }

            @Override
            public void onChildDraw(Canvas c, RecyclerView recyclerView, RecyclerView.ViewHolder viewHolder, float dX, float dY, int actionState, boolean isCurrentlyActive) {
                super.onChildDraw(c, recyclerView, viewHolder, dX, dY, actionState, isCurrentlyActive);

                View itemView = viewHolder.itemView;

                if (dX > 0) {
                    background.setBounds(itemView.getLeft(), itemView.getTop(), itemView.getLeft() + ((int) dX), itemView.getBottom());
                } else if (dX < 0) {
                    background.setBounds(itemView.getRight() + ((int) dX), itemView.getTop(), itemView.getRight(), itemView.getBottom());
                } else {
                    background.setBounds(0, 0, 0, 0);
                }

                background.draw(c);
            }
        };
        ItemTouchHelper itemTouchHelper = new ItemTouchHelper(touchHelperCallback);
        itemTouchHelper.attachToRecyclerView(recyclerView);

    }
```

Nous appelons la fonction showMenu() à l'intérieur de notre adaptateur lorsqu'un élément de liste est balayé.

La fonction onChildDraw() dessine l'arrière-plan pendant que nous balayons. Sinon, il y aura un fond blanc pendant le balayage et notre mise en page de menu apparaîtra avec un pop.

## Masquer le menu

Il y a trois façons de masquer notre menu.

1. Masquer le menu lorsqu'une autre ligne est balayée :

Ce cas est déjà géré dans la méthode showMenu() de notre adaptateur. Avant d'afficher le menu pour une ligne, nous appelons d'abord _setShowMenu(false)_ pour toutes les lignes afin de masquer le menu.

2. Masquer le menu lorsque le bouton retour est pressé (dans notre activité) :

```java
@Override
    public void onBackPressed() {
        if (adapter.isMenuShown()) {
            adapter.closeMenu();
        } else {
            super.onBackPressed();
        }
    }
```

3. Masquer le menu lorsqu'un utilisateur fait défiler la liste :

```java
recyclerView.setOnScrollChangeListener(new View.OnScrollChangeListener() {
            @Override
            public void onScrollChange(View v, int scrollX, int scrollY, int oldScrollX, int oldScrollY) {
                adapter.closeMenu();
            }
        });
```

Bien que Pocket n'ait qu'une action de pression longue pour afficher le menu, dans cet exemple, nous avons ajouté un balayage pour afficher le menu pour une fonctionnalité ajoutée. Vous pouvez masquer votre élément de menu lors d'un balayage à droite/gauche à nouveau, mais je pense que cela pourrait confondre l'utilisateur. 

## Conclusion

Si votre application a un très grand ensemble de données à afficher dans un RecyclerView, ce type d'UX pourrait ne pas être la solution à adopter. Dans ce cas, vous devriez avoir une fonctionnalité de type édition en masse. 

De plus, si vos options de modification sont plus nombreuses que ce que vous pouvez ajuster dans une ligne de RecyclerView, mais que vous souhaitez toujours afficher quelques actions rapides, vous pouvez afficher une boîte de dialogue Bottomsheet lors d'un appui long sur votre élément et elle peut contenir toutes vos options de modification. L'application android [Google Drive](https://play.google.com/store/apps/details?id=com.google.android.apps.docs&hl=en_IN) fait exactement la même chose.  

Si vous souhaitez implémenter une simple fonction de balayage pour supprimer, le code pour cela peut être trouvé ici [sur Github](https://github.com/iamtherealgd/RecyclerViewSwipeDelete).

Vous pouvez également consulter le [code source de ce projet](https://github.com/iamtherealgd/RecyclerViewSwipeOptions) sur Github.

Visitez [22Boxes.com](https://22boxes.com/) pour plus de ressources sur le développement mobile et web.