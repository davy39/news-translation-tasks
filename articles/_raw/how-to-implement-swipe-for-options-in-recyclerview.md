---
title: How to Implement 'Swipe for Options' in RecyclerView
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
seo_title: null
seo_desc: "By Gagandeep Singh\nLet's say a user of your site wants to edit a list\
  \ item without opening the item and looking for editing options. If you can enable\
  \ this functionality, it gives that user a good User Experience. \nPocket, a bookmarking\
  \ app owned by ..."
---

By Gagandeep Singh

Let's say a user of your site wants to edit a list item without opening the item and looking for editing options. If you can enable this functionality, it gives that user a **good User Experience**. 

[Pocket](https://play.google.com/store/apps/details?id=com.ideashower.readitlater.pro&hl=en_IN), a bookmarking app owned by Mozilla, does something similar. You can share/archive/delete your saved articles directly from the list without opening the article. Then you can click the menu button in the top-right corner and select your edit option.

So in this tutorial we'll try to code this one out.

**Here's what we want to achieve**:

![Image](https://www.freecodecamp.org/news/content/images/2024/08/recycler-view-example.jpg)

## First let’s create a normal RecyclerView list

RecyclerView is an advanced and flexible version of ListView and GridView. It's capable of holding large amounts of list data and has better performance than its predecessors. 

As the name suggests, RecyclerView 'recycles' the items of our list once it's out of view on scrolling and re-populates them when they come back to view. So the list container has to maintain only a limited number of views and not the entire list.

It's so flexible that the new [ViewPager2](https://developer.android.com/training/animation/vp2-migration#diffutil) class, used to create swipe-able tabs, is written over RecyclerView.

### Create a POJO (Plain Old Java Object) to hold the list data

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
    
    //... all the getters and setters
}
```

Notice we have a showMenu member here which will handle the visibility of the menu for that list item in our RecyclerView.

### Create a RecyclerView Adapter

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

Usually we put our ViewHolder sub class (MyViewHolder) in the super class template. This lets us directly return our defined ViewHolder subclass object from the onCreateViewHolder() method. Then we don't have to cast it again and again in onBindViewHolder() method. 

But here we can't do that, and we'll learn why in a minute. 

### Initialise the RecyclerView in the Activity

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
		//... rest of the list items
        
        adapter = new RecyclerAdapter(this, list);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(adapter);
    }
}
```

Now let's start making things a little more interesting.

## Create a layout resource for the menu 

And initialise it in Recycler Adapter:

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
        	//... same as above
        }
        
        if(holder instanceof MenuViewHolder){
            //Menu Actions
        }

    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder {
        //... same as above
    }
    //Our menu view
    public class MenuViewHolder extends RecyclerView.ViewHolder{
        public MenuViewHolder(View view){
            super(view);
        }
    }
}
```

Now we have two ViewHolder sub-classes in our adapter, MyViewHolder (the actual list item) and MenuViewHolder. Both inherit the same class so we return the parent class _RecyclerView.ViewHolder_ from onCreateViewHolder(). 

Our getItemViewType() method returns the int variable (viewType) which tells the kind of view we want to show in our RecyclerView for a particular position: that is, either MyViewHolder or MenuViewHolder. 

This viewType variable is then used by onCreateViewHolder() which actually returns the respective ViewHolder object.

## Add the functions to show/hide menu in RecyclerAdapter

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

Note that there are many ways to handle this. But for simplicity's sake we're keeping a boolean value in our POJO to maintain the menu's visibility.

After changing our data list, we call the notifyDataSetChanged() method to redraw the list. 

## Show the menu on long press of our list item in RecyclerAdapter

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
            //Set Menu Actions like:
            //((MenuViewHolder)holder).edit.setOnClickListener(null);
        }

    }
```

Again, setting events on our views can also be done in various ways. 

In our example, we have three actions in our menu. You can write your logic to handle those actions in the second if statement like shown in the comments.

## Show the menu on swipe 

To do this, we add a touch helper in our MainActivity.java:

```java
public class MainActivity extends AppCompatActivity {
    RecyclerView recyclerView;
    List<RecyclerEntity> list;
    RecyclerAdapter adapter;


    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //... same as above 
         
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

We call the showMenu() function inside our adapter when a list item is swiped.

The onChildDraw() function draws the background while we swipe. Otherwise there'll be a white background while swiping and our menu layout will show up with a pop.

## Hiding the menu

There are three ways to hide our menu.

1. Hiding the menu when another row is swiped:

This case is already handled in showMenu() method in our Adapter. Before showing the menu for any row, we first call _setShowMenu(false)_ for all the rows to hide the menu.

2.  Hiding the menu when the back button is pressed (in our Activity):

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

3.  Hiding the menu when a user scrolls the list:

```java
recyclerView.setOnScrollChangeListener(new View.OnScrollChangeListener() {
            @Override
            public void onScrollChange(View v, int scrollX, int scrollY, int oldScrollX, int oldScrollY) {
                adapter.closeMenu();
            }
        });
```

Though pocket only has a long-press action to show the menu, in this example we've added swipe to show the menu for added functionality. You can hide your menu item on swipe right/left again, but I think it might confuse the user. 

## Wrapping up

If your app has a very large dataset to show in a RecyclerView, this type of UX might not be the way to go. In that case you should have a bulk-edit sort of functionality. 

Also if your edit options are more than what you can adjust in a RecyclerView row but you still want to show some quick actions, you can show a Bottomsheet dialog on long press of your item and it can have all your edit options. The [Google Drive](https://play.google.com/store/apps/details?id=com.google.android.apps.docs&hl=en_IN) android app does exactly the same thing.  

If you want to implement a simple swipe to delete function, the code for that can be found here [on Github](https://github.com/iamtherealgd/RecyclerViewSwipeDelete).

You can also check the [source code for this project](https://github.com/iamtherealgd/RecyclerViewSwipeOptions) on Github.

Visit [22Boxes.com](https://22boxes.com/) for more Mobile & Web development resources.

