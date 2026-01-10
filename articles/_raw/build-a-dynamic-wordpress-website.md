---
title: How to Build a Dynamic Wordpress Site with Advanced Custom Fields and Custom
  Post Types
subtitle: ''
author: Jim Campbell
co_authors: []
series: null
date: '2023-08-03T20:36:38.000Z'
originalURL: https://freecodecamp.org/news/build-a-dynamic-wordpress-website
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-03-at-3.50.46-AM.png
tags:
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: "Hello, fellow WordPress enthusiasts! Today, I want to share with you an\
  \ exciting journey I took while building Honeymoons.com. It's a dynamic website\
  \ that uses Advanced Custom Fields (ACF) and Custom Post Types. \nAs a travel company\
  \ specializing in d..."
---

Hello, fellow WordPress enthusiasts! Today, I want to share with you an exciting journey I took while building [Honeymoons.com](https://honeymoons.com). It's a dynamic website that uses [Advanced Custom Fields (ACF)](https://www.advancedcustomfields.com/) and [Custom Post Types](https://developer.wordpress.org/plugins/post-types/registering-custom-post-types/). 

As a travel company specializing in dreamy honeymoon destinations, it was crucial for us to showcase our hotels and destinations in a user-friendly and visually appealing way. 

ACF and CPTs proved to be the perfect solution for achieving our goal of providing an immersive and personalized experience for our users. 

Creating a custom post type for both Destinations and Hotels allowed us to easily categorize these specific types of content. Advanced Custom Fields allowed us to enrich the Custom Post Types with specific metadata that can be dynamically displayed throughout the website.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-12.png)
_Example of [Honeymoons.com](https://honeymoons.com) using a Custom Post Type, Custom Template, and ACF to display hotel information._

## What Are Custom Post Types?

WordPress [Custom Post Types](https://developer.wordpress.org/plugins/post-types/registering-custom-post-types/) are a powerful feature that allows you to extend the default functionality of WordPress beyond the standard posts and pages. They enable you to create and manage different types of content, each with its own set of attributes and functionalities. 

Custom Post Types are essential for organizing and presenting specific content types, such as products, portfolio items, testimonials, events, recipes, and more in a structured and efficient manner.

By default, WordPress comes with two main post types:

### Posts

These are standard blog posts that are typically displayed in reverse chronological order on the blog page.

### Pages

These are static pages that are typically used for static content like About Us, Contact Us, or a Privacy Policy page.

However, when you need to create content that doesn't fit into the default post or page structure, Custom Post Types come into play.

You can register your custom post types with their own set of attributes, taxonomies, and template files. This allows you to manage and present diverse content in a more organized and user-friendly manner.

For instance, on [honeymoons.com](https://honeymoons.com), we created a Custom Post Type called "Destinations" to showcase honeymoon destinations. 

To create Custom Post Types, you can either write custom code using the `register_post_type()` function or use plugins that make the process more user-friendly, like "[Custom Post Type UI](https://wordpress.org/plugins/custom-post-type-ui/)" or "[Toolset Types](https://toolset.com/home/types-manage-post-types-taxonomy-and-custom-fields/)." 

WordPress comes with functionality to easily configure the post types to your specific needs by updating the functions.php file within your theme.

The specific code we used to create the Destinations post type is here:

	//Destinations
    register_post_type('destination', // Register Custom Post Type
        array(
        'labels' => array(
            'name' => __('Destinations', 'destination'), // Rename these to suit
            'singular_name' => __('Destination', 'html5blank'),
        ),
        'public' => true,
        'hierarchical' => true, // Allows your posts to behave like Hierarchy Pages
        'has_archive' => false,
		'menu_icon' => 'dashicons-palmtree',
		'show_in_nav_menus'   => true,
        'supports' => array(
            'title',
            'editor',
            'excerpt',
			'revisions',
			'page-attributes',
            'thumbnail'
        ), // Go to Dashboard Custom HTML5 Blank post for supports
		'rewrite' => array (
			'slug' => '/destinations',
			'with_front' => false,
			'hierarchical' => true
		),
        'can_export' => true, // Allows export in Tools > Export
        'taxonomies' => array(
			'experiences',
			'regions'
        ) // Add Category and Post Tags support */
    ));

These Custom Post Types will appear in the wp-admin sidebar with your Posts and Pages:

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-11.png)

Custom Post Types have become an essential tool for developers and content creators, as they offer the flexibility to tailor WordPress websites to specific needs, making it a versatile and robust content management system.

## What are Advanced Custom Fields for WordPress?

[Advanced Custom Fields (ACF)](https://www.advancedcustomfields.com/) is a popular WordPress plugin that enhances the content creation and management experience by providing a user-friendly interface for adding custom fields to posts, pages, and custom post types. It allows website developers and content creators to easily extend the default WordPress post editor with additional input fields, enabling the creation of more structured and dynamic content.

With ACF, you can define various types of custom fields, such as text fields, image upload fields, select dropdowns, date pickers, repeater fields, and more. These custom fields can be used to add extra information to your content, making it more versatile and tailored to specific requirements.

Key features and benefits of Advanced Custom Fields (ACF) include:

1. **Custom Field Creation**: ACF allows you to create custom fields through an intuitive graphical interface within the WordPress admin area. You can choose from various field types and configure their settings to suit your needs.
2. **Field Groups**: You can group related fields together into sets called "Field Groups." These groups can then be assigned to specific post types or pages, providing a modular and organized approach to content management.
3. **Conditionals and Logic**: A powerful feature of ACF is the ability to set conditional logic for fields. You can show or hide specific fields based on the values of other fields, making content creation more efficient and user-friendly.
4. **Repeater Fields**: ACF's repeater field allows you to create sets of sub-fields that can be repeated as needed. This is especially useful for managing dynamic content like lists, galleries, and flexible content sections.
5. **Frontend Integration**: ACF makes it easy to display the custom field data on the frontend of your website. You can use simple template tags or ACF functions to retrieve and display the custom field values within your theme files.
6. **Extensibility**: ACF can be extended through third-party add-ons and custom code, allowing developers to create even more advanced and specialized custom fields and functionalities.
7. **User-Friendly Experience**: ACF simplifies the content creation process for non-technical users. It reduces the need for custom coding and makes it easier for content editors to add and manage content with structured fields.

ACF has gained popularity among WordPress developers and designers for its flexibility and ease of use. It enables the creation of dynamic and customized websites without the need for complex custom development, making it a valuable tool for both small-scale websites and large, complex projects.

## How to Create Custom Templates to Display ACF Content

To dynamically show data using Advanced Custom Fields (ACF) and custom templates in WordPress, we'll walk through the steps with an example from Honeymoons.com using a Custom Post Type of Hotels. 

We'll create custom fields for metadata such as the number of rooms, average price, and the hotel URL, and then display this data dynamically on the frontend using a custom template.

### Step 1: Install and Activate Advanced Custom Fields Plugin.

First, ensure that the Advanced Custom Fields plugin is installed and activated on your WordPress website. You can find the plugin in the WordPress Plugin Repository and install it from the admin dashboard.

### Step 2: Create Custom Fields for Hotel Post Type. 

Next, we'll create custom fields for the Hotel post type using ACF.

1. Go to "Custom Fields" in the WordPress admin sidebar and click on "Add New."

2. Create a new field group for Hotels and add the following custom fields:

* Hero Image (Image)
* TripAdvisor.com Link (URL)
* Number of Rooms (Number)
* Number of Rooms (Number)
* Price - Low (Number)
* Price - High (Number)
* Price - Average (Number)
* Guest Rating (Number with a maximum value of 10)
* Star Rating
* Website (URL)
* Display URL (Text)

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-9.png)

3. Assign Field Group to Hotel Post Type 

After creating the custom fields, we need to assign the field group to the Hotel post type.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-10.png)

### Step 3: Displaying the Custom Fields in the Custom Template 

Now, we'll create a custom template for the Hotel post type, where we can dynamically retrieve and display the metadata.

Create a new PHP file in your theme folder and name it "single-hotel.php" (assuming you have a custom post type template hierarchy in your theme). Replace "hotel" with whatever your custom post type is named. 

In "single-hotel.php," start with the regular template code for the header, footer, and post loop. You can start with a copy of single.php.

Use ACF functions to retrieve the custom field values and display them in the template. Use PHP, HTML and CSS to display the content.

You can retrieve the Advanced Custom Fields like this:

$number_of_rooms = get_field('number_of_rooms');
$average_price = get_field('average_price');
$hotel_url = get_field('hotel_url');

And display the content like this:

echo '<p>Number of Rooms: ' . $number_of_rooms . '</p>';
echo '<p>Average Price: $' . $average_price . '</p>';
echo '<p><a href="' . $hotel_url . '">Hotel Website</a></p>';

By  capturing metadata with Advanced Custom Fields and displaying that content with Custom Templates and Custom Post Types, you can organize and display data on your WordPress website in a much more dynamic and user-friendly way.

Your WordPress site will not look "out-of-the-box" and your site will provide much more helpful and organized information to the user.

## Conclusion

Thanks to ACF and Custom Post Types, Honeymoons.com now boasts a dynamic website that offers personalized experiences to our users. 

Our collaboration with ACF and CPTs has empowered us to create stunning hotel and destination pages that captivate visitors and help them plan their dream honeymoon effortlessly. 

I hope our case study has inspired you to explore the vast potential of ACF and CPTs for building dynamic WordPress websites tailored to your specific needs. Happy coding!

  

