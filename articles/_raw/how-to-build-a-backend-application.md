---
title: How to Build and Deploy a Backend App with Express, Postgres, Github, and Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-03T20:46:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-backend-application
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-pixabay-417273.jpg
tags:
- name: 'Back end development '
  slug: back-end-development
- name: deployment
  slug: deployment
- name: Express
  slug: express
- name: GitHub
  slug: github
- name: Heroku
  slug: heroku
- name: postgres
  slug: postgres
seo_title: null
seo_desc: "By Njoku Samson Ebere\nIn this tutorial, we will be learning how to build\
  \ and deploy an image management application backend. \nIt will be able to store\
  \ a record of an image in the database, get the image's record back from the database,\
  \ update the rec..."
---

By Njoku Samson Ebere

In this tutorial, we will be learning how to build and deploy an image management application backend. 

It will be able to store a record of an image in the database, get the image's record back from the database, update the record, and even delete the record completely as the case may be.

To achieve all of this, we will be using Express (a Node.js framework), Postgres (a database), Cloudinary (a cloud based image storage), GitHub (for version control/storage) and Heroku (a hosting platform).

These tools are all free. So you don’t have to bother about how to go about paying for them. Thanks to these great innovators.

### Prerequisites

If you are new to most of these technologies, I would advise you go through my other tutorial on how to [create a server and upload images to Cloudinary](https://www.freecodecamp.org/news/build-a-secure-server-with-node-and-express/).

If you are totally to Postgres, then check out this [tutorial](https://dev.to/ogwurujohnson/-persisting-a-node-api-with-postgresql-without-the-help-of-orms-like-sequelize-5dc5).

Whenever you are ready, let’s get to work!

## How to Store and Retrieve an Image Record 

### Create Database and Table

So you'll want to start by cloning this [project](https://github.com/EBEREGIT/server-tutorial/tree/cloudinary-upload) if you don't already have it.

In your **pgAdmin**:

* Create a database and name it `tutorial`
* Create a table and name it `tutorial`
* Create a Login/Group Role and name it `tutorial`. **(Do not forget to give it all privileges.)**

Back in your project directory, install the [node-postgres](https://node-postgres.com/) (`npm i pg`) and [make-runnnable](https://www.npmjs.com/package/make-runnable) (`npm i make-runnable`) packages.

In your `package.json` file, replace the contents of the `"scripts"` with `"create": "node ./services/dbConnect createTables"`. We will use this to execute the `dbConnect` file we are about to create.

Create a `services/dbConnect` file to contain the following code:

```javascript

const pg = require("pg");

const config = {
  user: "tutorial",
  database: "tutorial",
  password: "tutorial",
  port: 5432,
  max: 10, // max number of clients in the pool
  idleTimeoutMillis: 30000,
};

const pool = new pg.Pool(config);

pool.on("connect", () => {
  console.log("connected to the Database");
});

const createTables = () => {
  const imageTable = `CREATE TABLE IF NOT EXISTS
    images(
      id SERIAL PRIMARY KEY,
      title VARCHAR(128) NOT NULL,
      cloudinary_id VARCHAR(128) NOT NULL,
      image_url VARCHAR(128) NOT NULL
    )`;
  pool
    .query(imageTable)
    .then((res) => {
      console.log(res);
      pool.end();
    })
    .catch((err) => {
      console.log(err);
      pool.end();
    });
};

pool.on("remove", () => {
  console.log("client removed");
  process.exit(0);
});

//export pool and createTables to be accessible from anywhere within the application
module.exports = {
  createTables,
  pool,
};

require("make-runnable");


```

Now we are all set to create the table in our database. If you are ready, let's rock and roll!

Execute the following code in your terminal:

```javascript

  npm run create


```

If the image below is your result, then you are good to go:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/fjk5ty113j5p7kaxveqc.JPG)

Check your **pgAdmin**, and you should have your table seated properly in your database like in the image below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/sj7gy6d86vm7ay3d8a74.JPG)

Alright, it's been a long road. It's time to unite Node, Postgres, and Cloudinary.

## How to Create Endpoints to Store and Retrieve Image Records

### Endpoint 1: Persist Image

First, require the `dbConnect.js` file on the top of the `app.js` file like so:

```javascript
  const db = require('services/dbConnect.js');

```

Then in the `app.js` file, make a new endpoint _(persist-image)_ with the following code:

```javascript

// persist image
app.post("/persist-image", (request, response) => {
  // collected image from a user
  const data = {
    title: request.body.title,
    image: request.body.image,
  }

  // upload image here
  cloudinary.uploader.upload(data.image)
  .then().catch((error) => {
    response.status(500).send({
      message: "failure",
      error,
    });
  });
})


```

Replace the `then` block with the following code:

```javascript

.then((image) => {
    db.pool.connect((err, client) => {
      // inset query to run if the upload to cloudinary is successful
      const insertQuery = 'INSERT INTO images (title, cloudinary_id, image_url) 
         VALUES($1,$2,$3) RETURNING *';
      const values = [data.title, image.public_id, image.secure_url];
    })
  })


```

The `image.public_id` and `image.secure_url` are gotten as part of the details returned for an image after the image has been successfully uploaded to Cloudinary. 

We are now keeping a record of the `image.public_id` and `image.secure_url` (as you can see in the code above) in order to use it to retrieve, update, or delete the image record when we see fit. 

Alright, let's move forward!

Still in the `then` block, add the following code under the query we created:

```javascript

// execute query
client.query(insertQuery, values)
      .then((result) => {
        result = result.rows[0];

        // send success response
        response.status(201).send({
          status: "success",
          data: {
            message: "Image Uploaded Successfully",
            title: result.title,
            cloudinary_id: result.cloudinary_id,
            image_url: result.image_url,
          },
        })
      }).catch((e) => {
        response.status(500).send({
          message: "failure",
          e,
        });
      })


```

So our `persist-image` endpoint now looks like this:

```javascript

// persist image
app.post("/persist-image", (request, response) => {
  // collected image from a user
  const data = {
    title: request.body.title,
    image: request.body.image
  }

  // upload image here
  cloudinary.uploader.upload(data.image)
  .then((image) => {
    db.pool.connect((err, client) => {
      // inset query to run if the upload to cloudinary is successful
      const insertQuery = 'INSERT INTO images (title, cloudinary_id, image_url) 
         VALUES($1,$2,$3) RETURNING *';
      const values = [data.title, image.public_id, image.secure_url];

      // execute query
      client.query(insertQuery, values)
      .then((result) => {
        result = result.rows[0];

        // send success response
        response.status(201).send({
          status: "success",
          data: {
            message: "Image Uploaded Successfully",
            title: result.title,
            cloudinary_id: result.cloudinary_id,
            image_url: result.image_url,
          },
        })
      }).catch((e) => {
        response.status(500).send({
          message: "failure",
          e,
        });
      })
    })  
  }).catch((error) => {
    response.status(500).send({
      message: "failure",
      error,
    });
  });
});


```

**Now let's test out all our hard work:**

Open your _postman_ and test out your endpoint like the image below. Mine was successful. Hope yours had no errors too?

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/euxsoyb821v85uv5rhml.JPG)

Open your Cloudinary console/dashboard and check your `media Library`. Your new image should be sitting there comfortably like mine below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/dxy5fl8fodqpn89oltzh.JPG)

And now to the main reason why we are here: check the `images` table in your **pgAdmin**. Mine is what you see below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ypv6vcrocsgp13owq5dv.JPG)

Oohlala! We made it this far. Please take a break if you need one. I will be here waiting when you return. :)

If you are ready, then let's retrieve the image we persisted a moment ago.

### Endpoint 2: Retrieve Image

Start with this code:

```javascript

app.get("/retrieve-image/:cloudinary_id", (request, response) => {

});


```

Next, we will need to collect a unique ID from the user to retrieve a particular image. So add `const { id } = request.params;` to the code above like so:

```javascript

app.get("/retrieve-image/:cloudinary_id", (request, response) => {
  // data from user
  const { cloudinary_id } = request.params;

});


```

Add the following code just below the code above:

```javascript

db.pool.connect((err, client) => {
      // query to find image
    const query = "SELECT * FROM images WHERE cloudinary_id = $1";
    const value = [cloudinary_id];
    });


```

Under the query, execute the query with the following code:

```javascript

// execute query
    client
      .query(query, value)
      .then((output) => {
        response.status(200).send({
          status: "success",
          data: {
            id: output.rows[0].cloudinary_id,
            title: output.rows[0].title,
            url: output.rows[0].image_url,
          },
        });
      })
      .catch((error) => {
        response.status(401).send({
          status: "failure",
          data: {
            message: "could not retrieve record!",
            error,
          },
        });
      });


```

Now our `retrieve-image` API looks like this:

```javascript

app.get("/retrieve-image/:cloudinary_id", (request, response) => {
  // data from user
  const { cloudinary_id } = request.params;
  
  db.pool.connect((err, client) => {
    // query to find image
    const query = "SELECT * FROM images WHERE cloudinary_id = $1";
    const value = [cloudinary_id];

    // execute query
    client
      .query(query, value)
      .then((output) => {
        response.status(200).send({
          status: "success",
          data: {
            id: output.rows[0].cloudinary_id,
            title: output.rows[0].title,
            url: output.rows[0].image_url,
          },
        });
      })
      .catch((error) => {
        response.status(401).send({
          status: "failure",
          data: {
            message: "could not retrieve record!",
            error,
          },
        });
      });
  });
});


```

**Let's see how well we did:**

In your postman, copy the `cloudinary_id` and add it to the URL like in the image below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/9bmutxbmitgznqnnwmny.JPG)

YEEESSS! We can also retrieve our image.

If you are here, then you deserve a round of applause and a standing ovation for your industriousness.

Congratulations! You just reached a great milestone.

The code for storing and retrieving image records is [here](https://github.com/EBEREGIT/server-tutorial/tree/create-APIs).

## How to Update and Delete an Image Record

We will now see how to delete and update an image record as the case maybe. Let's begin with the delete endpoint.

### Delete Endpoint

In the app.js file, start with the following code:

```javascript

// delete image
app.delete("delete-image/:cloudinary_id", (request, response) => {

});


```

Next, we want to get the unique ID of the image we want to delete from the URL, that is `cloudinary_id`. So inside the code above add:

```javascript

const { cloudinary_id } = request.params;


```

We now start the deleting process.

First, we delete from Cloudinary. Add the following code to delete the image from Cloudinary:

```javascript

cloudinary.uploader
    .destroy(cloudinary_id)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    })
    .catch((error) => {
      response.status(500).send({
        message: "Failure",
        error,
      });
    });


```

At this point, our API can delete the image from Cloudinary only (you can check it out in postman). But we also want to get rid of the record we have in our Postgres database.

Second, we delete from our Postgres database. To do so, replace the code in the `then` block with the following `query`:

```javascript

db.pool.connect((err, client) => {
     
      // delete query
      const deleteQuery = "DELETE FROM images WHERE cloudinary_id = $1";
      const deleteValue = [cloudinary_id];

})

```

Execute the query with the following code underneath it:

```javascript

// execute delete query
      client.query(deleteQuery, deleteValue)
      .then((deleteResult) => {
        response.status(200).send({
          message: "Image Deleted Successfully!",
          deleteResult
        });
      }).catch((e) => {
        response.status(500).send({
          message: "Image Couldn't be Deleted!",
          e
        });
      });


```

So our Endpoint should look like this:

```javascript

// delete image
app.delete("/delete-image/:cloudinary_id", (request, response) => {
  // unique ID
  const { cloudinary_id } = request.params;

  // delete image from cloudinary first
  cloudinary.uploader
    .destroy(cloudinary_id)

    // delete image record from postgres also
    .then(() => {
      db.pool.connect((err, client) => {
     
      // delete query
      const deleteQuery = "DELETE FROM images WHERE cloudinary_id = $1";
      const deleteValue = [cloudinary_id];

      // execute delete query
      client
        .query(deleteQuery, deleteValue)
        .then((deleteResult) => {
          response.status(200).send({
            message: "Image Deleted Successfully!",
            deleteResult,
          });
        })
        .catch((e) => {
          response.status(500).send({
            message: "Image Couldn't be Deleted!",
            e,
          });
        });
      })
    })
    .catch((error) => {
      response.status(500).send({
        message: "Failure",
        error,
      });
    });
});


```

The time has arrived for us to put our Endpoint to the test.

The following is my Cloudinary `media library` with two images I uploaded already. Take note of their unique ID (`public_id`). 

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/sjir185on5pqrlzrc1hl.JPG)

If you don't already have that, please use the persist-image endpoint to upload some images.

Now let's proceed to postman:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/beu5lleymnffa5vyzj97.JPG)

Notice, the unique ID as it matches one of the image in my Cloudinary media library.

From the output, we executed the DELETE command and that deleted one ROW from our image TABLE in our database.

Now this is my media library with one of the images remaining:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/8d7rs33580c4ewpcipbr.JPG)

Walahhhh... We are now able to get rid of an image.

Do take a break if you need one. ✌🏾

If you are ready, I am ready to update images.

### Update Image API

Below the `delete-image` API, let's start creating the `update-image` API with the following code:

```javascript

// update image
app.put("/update-image/:cloudinary_id", (request, response) => {

});

All codes will live in there.


```

Collect the unique Cloudinary ID and new image details from the user with the following code:

```javascript

// unique ID
  const { cloudinary_id } = request.params;

// collected image from a user
  const data = {
    title: request.body.title,
    image: request.body.image,
  };


```

Delete the image from Cloudinary with the following code:

```javascript

// delete image from cloudinary first
  cloudinary.uploader
    .destroy(cloudinary_id)
      // upload image here
    .then()
    .catch((error) => {
      response.status(500).send({
        message: "failed",
        error,
      });
    });


```

Next, upload another image to Cloudinary. To do that, enter the following code into the `then` block:

```javascript

() => {
      cloudinary.uploader
        .upload(data.image)
        .then()
        .catch((err) => {
          response.status(500).send({
            message: "failed",
            err,
          });
        });
    }


```

Now let's replace our initial record with the new image details. Replace the content of the `then` block with the following:

```javascript

(result) => {
          db.pool.connect((err, client) => {
            
            // update query
            const updateQuery =
              "UPDATE images SET title = $1, cloudinary_id = $2, image_url = $3 WHERE cloudinary_id = $4";
            const value = [
              data.title,
              result.public_id,
              result.secure_url,
              cloudinary_id,
            ];
          });
        }


```

We execute the query using the following code just beneath the query declaration:

```javascript

// execute query
            client
              .query(updateQuery, value)
              .then(() => {

                // send success response
                response.status(201).send({
                  status: "success",
                  data: {
                    message: "Image Updated Successfully"
                  },
                });
              })
              .catch((e) => {
                response.status(500).send({
                  message: "Update Failed",
                  e,
                });
              });


```

At this point, this is what I have:

```javascript

// update image
app.put("/update-image/:cloudinary_id", (request, response) => {
  // unique ID
  const { cloudinary_id } = request.params;

  // collected image from a user
  const data = {
    title: request.body.title,
    image: request.body.image,
  };

    // delete image from cloudinary first
    cloudinary.uploader
      .destroy(cloudinary_id)

      // upload image here
      .then(() => {
        cloudinary.uploader
          .upload(data.image)

          // update the database here
          .then((result) => {
            db.pool.connect((err, client) => {
            // update query
            const updateQuery =
              "UPDATE images SET title = $1, cloudinary_id = $2, image_url = $3 WHERE cloudinary_id = $4";
            const value = [
              data.title,
              result.public_id,
              result.secure_url,
              cloudinary_id,
            ];

            // execute query
            client
              .query(updateQuery, value)
              .then(() => {

                // send success response
                response.status(201).send({
                  status: "success",
                  data: {
                    message: "Image Updated Successfully"
                  },
                });
              })
              .catch((e) => {
                response.status(500).send({
                  message: "Update Failed",
                  e,
                });
              });
            });
          })
          .catch((err) => {
            response.status(500).send({
              message: "failed",
              err,
            });
          });
      })
      .catch((error) => {
        response.status(500).send({
          message: "failed",
          error,
        });
      });
  
});


```

It's testing time!

This is my postman in the image below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/jowr0guiazmqkhx1mmls.JPG)

Take note of the unique cloudinary ID which matches the image left in my Cloudinary media library.

Now take a look at my Cloudinary media library in the image that follows:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/td9rpqovhh2kl6ytc2u4.JPG)

Take note of the new image replacing the initial one in my media library above.

Also, see that the unique Cloudinary ID matches that in my database with the new title. See image below:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/wu3mydrn71x3azyd75ee.JPG)

Yayeh! You did awesomely great! 💪

We just completed an image management application with Node.js, Cloudinary and Postgres.

## Code Optimisation With Express Routing

Express Routing enables us to make our Node.js code more optimized or give it a more modular structure by separating the business logic from the controllers. We want to use that to clean up our code so far. 

We'll begin by creating a new folder with the name `routes` in the root directory:

```javascript

mk dir routes


```

In the routes folder, create a file with the name: `routes.js`.

For Windows:

```javascript

echo . > routes.js


```

For Mac:

```javascript

touch routes.js


```

Empty the `routes.js` file if anything is there and enter the following code:

```javascript

const express = require('express');

const router = express.Router();



module.exports = router;


```

Add the following code above the last line:

```javascript

const cloudinary = require("cloudinary").v2;
require("dotenv").config();
const db = require("../services/dbConnect.js");

// cloudinary configuration
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET,
});


```

Back in the App.js file, delete the following code:

```javascript

const cloudinary = require("cloudinary").v2;
require("dotenv").config();
const db = require("./services/dbConnect.js");

// cloudinary configuration
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET,
});


```

Move all the APIs to `routes.js`.

Change all occurence of `app` to `router` carefully.

My `routes.js` file now looks like [this](https://github.com/EBEREGIT/server-tutorial/blob/routing/routes/routes.js).

Back in the `app.js` file, import the `routes.js` file like so:

```javascript

// import the routes file
const routes = require("./routes/routes")


```

Now register the routes like so:

```javascript

// register the routes 
app.use('/', routes);


```

This is my `app.js` file at the moment:

```javascript

const express = require("express");
const app = express();

// import the routes file
const routes = require("./routes/routes")

// body parser configuration
const bodyParser = require("body-parser");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// register the routes 
app.use('/', routes);

module.exports = app;


```

It's time to test and see if our routes are still working like before.

Make sure yours are working like mine below:

#### persist-image

![persist image](https://dev-to-uploads.s3.amazonaws.com/i/r2uz54xix054li4lgw6i.JPG)

#### retrieve-image

![retrieve image](https://dev-to-uploads.s3.amazonaws.com/i/o44a1dnfgvz3r9sv3a1j.JPG)

#### update-image

![update image](https://dev-to-uploads.s3.amazonaws.com/i/6t9k5m079rwx4p6ouax3.JPG)

#### delete-image

![delete image](https://dev-to-uploads.s3.amazonaws.com/i/nkkydplioi68la4eynhp.JPG)

Wow! We have been able to separate our routes from our `app.js` file.

The code for this is [here](https://github.com/EBEREGIT/server-tutorial/tree/routing).

Even though our `routes.js` file is still lengthy, we have a good basis to separate our business logic from our controllers. The time has arrived to do just that.

## How to Move Each Endpoint to a Different File

Begin by creating a new folder in the `routes` folder and name it `controllers`.

In the controllers folder, create 5 files and name them after the 5 endpoints.

Our folder and files should be structured as follows:

![folder and files structure](https://dev-to-uploads.s3.amazonaws.com/i/dmren2r2w2801lf28wjy.JPG)

Back in the routes.js file, let's work on the `image-upload` API. Cut the following code:

```javascript

(request, response) => {
  // collected image from a user
  const data = {
    image: request.body.image,
  };

  // upload image here
  cloudinary.uploader
    .upload(data.image)
    .then((result) => {
      response.status(200).send({
        message: "success",
        result,
      });
    })
    .catch((error) => {
      response.status(500).send({
        message: "failure",
        error,
      });
    });
}


```

In the `imageUpload` file, equate the code you already cut from the `image-upload` endpoint to `exports.imageUpload` like so:

```javascript

exports.imageUpload = (request, response) => {
    // collected image from a user
    const data = {
      image: request.body.image,
    };
  
    // upload image here
    cloudinary.uploader
      .upload(data.image)
      .then((result) => {
        response.status(200).send({
          message: "success",
          result,
        });
      })
      .catch((error) => {
        response.status(500).send({
          message: "failure",
          error,
        });
      });
  }


```

Now let's import what is necessary for this code to work. So this is my `imageUpload` file right now:

```javascript

const cloudinary = require("cloudinary").v2;
require("dotenv").config();

// cloudinary configuration
cloudinary.config({
  cloud_name: process.env.CLOUD_NAME,
  api_key: process.env.API_KEY,
  api_secret: process.env.API_SECRET,
});

exports.imageUpload = (request, response) => {
    // collected image from a user
    const data = {
      image: request.body.image,
    };
  
    // upload image here
    cloudinary.uploader
      .upload(data.image)
      .then((result) => {
        response.status(200).send({
          message: "success",
          result,
        });
      })
      .catch((error) => {
        response.status(500).send({
          message: "failure",
          error,
        });
      });
  }


```

Let's import and register the `imageUpload` API in the `routes.js` file like so:

```javascript

const imageUpload = require("./controllers/imageUpload");

// image upload API
router.post("image-upload", imageUpload.imageUpload);


```

Now we have this line of code pointing to the `imageUpload` API in the `imageUpload.js` file from the `routes.js` file.

How awesome! Our code is more readable.

Make sure to test the API to be sure it's working properly. Mine works perfectly. See image below:

![image upload test result](https://dev-to-uploads.s3.amazonaws.com/i/t456z1fz1537nja0huyr.JPG)

Now, it's your turn!

Apply what you have learnt to the other APIs. Let's see what you have got.

I will be waiting on the other side...

If you are here, then I believe you have done yours and they're working perfectly – or at least, you already gave it your best shot. Kudos!

Checkout mine [here](https://github.com/EBEREGIT/server-tutorial/tree/controller-setup/routes).

Congratulations. You are awesome :)

The code optimisation code is [here](https://github.com/EBEREGIT/server-tutorial/tree/controller-setup).

Alright, on to the next step.

## How to Deploy to GitHub And Heroku

Now that we've completed our application, let's deploy it on Heroku so that we can access it even without being on our laptop where the code was written.

I will be walking you through uploading our application to [GitHub](https://github.com/) and deploying it to [Heroku](https://heroku.com/).

Without further ado, let's get our hands dirty.

## How to Upload the Code to GitHub

Uploading or pushing to GitHub is as easy as eating your favorite meal. Check out [this resource](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line) to learn how to push your project from you local machine to GitHub.

## How to Deploy to Heroku

Let's begin by creating an account on [Heroku](https://heroku.com/).

If you have created an account, you may have been prompted to create an app (that is a folder where your app will be housed). You can do that, but I will do mine using my terminal since the terminal comes with a few added functionalities that we will need later.

Open your project in a terminal if you have not done so already. I will be using the VS Code integrated terminal.

Install Heroku CLI:

```javascript
npm install heroku

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/716g1v0nnea93rdrhmk5.JPG)

Login to Heroku CLI. This will open a browser window, which you can use to log in.

```javascript
heroku login

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/bky4mywipzua8cj6d0kf.JPG)

Create an app. It can have any name. I am using `node-postgres-cloudinary`.

```javascript
heroku create node-postgres-cloudinary

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ibofc7xcyqgi165f5dz1.JPG)

Go to your [Heroku dashboard](https://dashboard.heroku.com/apps) and you will find the newly created app.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/d84emoge8pi9qt0a2qrb.JPG)

Waalaah!

That is how mine looks in the image above. I have some apps there already but you can see the one I just created.

Let's now add the PostgreSQL database to the app.

### How to Add Heroku Postgres

Click on the app you just created. It will take you to the app's dashboard.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/g48iadulci1evt6j8ftf.JPG)

Click on the `Resources` tab/menu.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/e6bvzsv7cn6ebgwi0y65.JPG)

In the `Add-ons` Section, search and select `Heroku Postgres`.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/91nwppclfdkvitp56rrj.JPG)

Make sure you select the `Hobby Dev - Free` plan in the pop-up window that follows:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/hd7zj1qa2t4e051zn654.JPG)

Click on the `provision` button to add it to the app like so:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/8w2z6tok8plmp154ovuj.JPG)

Click on the `Heroku Postgres` to take you to the `Heroku Postgres` dashboard.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/nvrdf902ypuz2frqiu1q.JPG)

Click on the `settings` tab:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/6k81alizfc5yzgtbzlcv.JPG)

Click on `View Credentials`:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/33p2ceyfkbmr590s1r6b.JPG)

In the Credentials, we are interested in the Heroku CLI. We will be using it in a bit.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/xzmtjtqrg8a5vqrfjkg3.JPG)

Back to the terminal.

Let's confirm if the `Heroku Postgres` was added successfully. Enter the following in the terminal:

```javascript
heroku addons

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/7hhl70mw99b2mrji9i35.JPG)

Yeeeeaaaah! It was added successfully.

Before we proceed, **make sure that your PostgreSQL `path` is set correctly if you are on Windows**. Follow this [link](https://www.computerhope.com/issues/ch000549.htm) to learn how to set a `path`. The path should be like this: `C:\Program Files\PostgreSQL\<VERSION>\bin`. 

The version will depend on the one installed on you machine. Mine is: `C:\Program Files\PostgreSQL\12\bin` since I am using the `version 12`.

The following image might be helpful:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/dl3wv0z1dtvyjvvusx26.JPG)

You may have to navigate to the folder where PostgreSQL is installed on your machine to find out your own path.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/bzf04c5827d4tri3ngrg.JPG)

Login into the `Heroku Postgres` using the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) from our `Heroku Postgres` [credentials](https://devcenter.heroku.com/articles/heroku-postgresql-credentials). This is mine – yours will be different:

```javascript
heroku pg:psql postgresql-slippery-19135 --app node-postgres-cloudinary

```

If you got an error, it is most likely because your path is not set properly.

### How to Prepare our Database Connection to Match Heroku's

At the moment, my database looks like this:

```javascript

const pg = require("pg");

const config = {
  user: "tutorial",
  database: "tutorial",
  password: "tutorial",
  port: 5432,
  max: 10, // max number of clients in the pool
  idleTimeoutMillis: 30000,
};

const pool = new pg.Pool(config);

pool.on("connect", () => {
  console.log("connected to the Database");
});


```

If you try connecting Heroku to this, you are going to get an error. This is because Heroku has a `connection string` setup already. So we have to setup our connection such that Heroku can easily connect. 

I am going to refactor my database connection file (`dbConnect.js`) and `.env` file to make this happen.

* dbConnect.js

```javascript

const pg = require('pg');
require('dotenv').config();

// set production variable. This will be called when deployed to a live host
const isProduction = process.env.NODE_ENV === 'production';

// configuration details
const connectionString = `postgresql://${process.env.DB_USER}:${process.env.DB_PASSWORD}@${process.env.DB_HOST}:${process.env.DB_PORT}/${process.env.DB_DATABASE}`;

// if project has been deployed, connect with the host's DATABASE_URL
// else connect with the local DATABASE_URL
const pool = new pg.Pool({
  connectionString: isProduction ? process.env.DATABASE_URL : connectionString,
  ssl: isProduction,
});

// display message on success if successful
pool.on('connect', () => {
  console.log('Teamwork Database connected successfully!');
});


```

* .env file

```javascript

DB_USER="tutorial"
DB_PASSWORD="tutorial"
DB_HOST="localhost"
DB_PORT="5432"
DB_DATABASE="tutorial"


```

With the setup of the `dbconnect` and `.env` file, we are ready to export our database and tables from our local machine to `heroku postgres`.

### How to Export Database and Tables

Go to your `pgAdmin` and locate the database for this tutorial. Mine is tutorial.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/m454dij54j7dghsxqa25.JPG)

Right-Click on it and select `Backup`. This will bring up a new window.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/u57h6kpw5gtbhublc1la.JPG)

Enter a name for the SQL file like I did. Select the `plain` format. Then click Backup. This will save the file to your documents folder.

Locate the file and move it into the project directory. It can be anywhere in the directory but I choose to move mine into the `services` directory because it holds the database related files.

Back in the terminal, navigate to the folder containing the SQL file and run the following code to add the tables we just exported to the `heroku postgres` database:

```html
cat <your-SQL-file> | <heroku-CLI-from-the-heroku-posgres-credentials>

```

This is what mine looks like:

```javascript
cat tutorial.sql | heroku pg:psql postgresql-slippery-19135 --app node-postgres-cloudinary

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/67x0f9521g5savkrafpc.JPG)

Did you notice that I changed directory to services (`cd services`)? That is where my `sql` file is located.

Wow! We have just successfully exported our database and tables to Heroku.

It is almost over...

### How to Tell GitHub that We Made Changes

Add the files we have made changes to:

```javascript
$ git add .

```

The period (`.`) adds all files.

Commit your latest changes:

```javascript
$ git commit -m "refactored the dbConnect and .env file to fit in to heroku; Added the database SQL file"

```

Push the committed files:

```javascript
$ git push origin -u master

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/u8kogsya1gt3uxnujz35.JPG)

### Finally deploying our App

Go to you app's dashboard:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4j4bi64n0f0bp65j7pb7.JPG)

Select the GitHub Deployment method:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/5edwt90cpy75b3uyqgvy.JPG)

Search and select a repo, and click on `connect`:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ifg4zh7jzab3edpaxvnf.JPG)

Select the branch you want to deploy (in my own case, it is the `master` branch):

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4ka9c6781vft1gio7p0k.JPG)

Enable automatic deployment by clicking the `Enable automatic deployment` button as in the image above.

Click on the `Deploy` button in the manual deploy

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/7ksrclnfyjzzvn2nr4gc.JPG)

We will not have to do all this for subsequent deployments.

Now you have a button telling you to "view site" after build is completed. Click it. This will open your app in a new tab.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/9xi5vx6lx99z49uscre6.JPG)

**Oh no! A bug? Application error??**

Don't worry, it just a small issue. Something you should never forget to do while making deployments. Most hosting service will require it.

### How to Fix the Heroku Application Error

Get back to the root directory of your project.

Create a file and name it `Procfile` (it has no extension).

In the file, enter the following code:

```javascript
web: node index.js

```

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/k3jb0rof1g6bs1zs2eh6.JPG)

This directs Heroku to the server file (`index.js`) which is the entry point of the application. If your server is in a different file, please modify as required.

Save the file and push the new changes to GitHub.

Wait 2 to 5 minutes for Heroku to automatically detect changes in your GitHub repo and render the changes on the app.

You can now refresh that error page and see your hard work paying off:

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/n4t9yp4598wc5i7v8p82.JPG)

You can also test the `retrieve image` route and see it working.

Congratulations! What a feat you have attained.

Other routes **(persist-image, update-image, and delete-image)** will not be working because we have not provisioned or added `cloudinary` add-on. It is as simple as the `PostgreSQL` one we just did. So you can give it a shot.

## Conclusion 

We started this tutorial with the aim of learning how to build a backend application using Express, Postgres, Cloudinary, Github and Heroku. 

We learned how to store, retrieve, delete, and update an image record. We then organised our code with Express Routing, pushed it to GitHub, and deployed it on Heroku. That was a lot.

I hope you will agree that it was worth it because we learnt a lot. You should try adding the Cloudinary add-on yourself to sharpen your knowledge even more.

Thanks for reading!

