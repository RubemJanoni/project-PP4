# Coffee Blog

Coffee blog is a website aimed at coffee lovers, a place where they can share information about the world of coffee.
Users can create posts containing title, author, content and image, they can also update and delete their posts.

![responsive-site](static/responsive-coffeeblog.jpg)

## Features

- Design

The design was planned to offer a clean, minimalist layout, with a white background and black navigation bar, highlighting the colors of the coffee images, the different shades of brown, harmoniously interacting with black and white.

- Navigation

Navigation is quite simple, basically we have a menu on the left with the main features, containing three buttons (Home, All Posts, Create Post)

**Home** - It always takes you to the home page, where the posts are displayed.

**All Posts** - Displays a list of posts, where it is possible to update or delete each post.

**Create Post** - Through this button, the user has access to the post form, with basically the author, text and upload image fields.


![menu-site](static/menu-coffeeblog.jpg)


The **All post** and **Create Post** buttons take the user to the list of posts and the creation form respectively, as shown in the images below.


![menu-site](static/post01-coffeeblog.jpg)

![menu-site](static/post02-coffeeblog.jpg)



  On the right we have a hamburger menu, where user login and registration features are presented.
  The user will only be able to create, change and delete a post after registering and logging in.



![menu-site](static/menu2-coffeeblog.jpg)


## The Header

A nav-brand was used in the header, showing the name of the site "Coffee Blog" and a logo, represented by a fontawosome icon.

![menu-site](static/menu-coffeeblog.jpg)


## The Main Section

In the body of the website, posts are inserted, built within a bootstrap card structure, with all the required responsiveness and planned according to the must-have requirements of the agile model.

![menu-site](static/menu-coffeeblog.jpg)



## The Footer

Following the same design pattern, the footer is presented, containing links to the main social networks, with their respective fontawesome icons.

![footer-site](static/footer-coffeeblog.jpg)

## Testing

- I tested that this page works in different browsers: Chrome, Firefox, Safari.
- I confirmed that this project is responsive, looks good and functions on all standard screen sizes using the devtools device toolbar.
- I confirmed that the navigation, header, footer, forms are readable and easy to understand.
- I have confirmed that the form works

## Validator Testing

- HTML
  - No errors were returned when passing through the official W3C validator.
  
- CSS
  - No errors were found when passing through the official (Jigsaw) validator.

   
    
- ACCESSIBILITY
  - I confirmed that the colors and fonts chosen are easy to read and accessible by running it through lighthouse in devtools.

  ![validation-site](static/lighthouse-coffeeblog.jpg)         
         
    


## Deployment

This epic is the deployment of the application to Heroku - application parameters and configuration of heroku

USER-STORY: - As a developer, I must deploy to heroku to allow public access

Deployment to Heroku
Navigate to the heroku website and create an account if you dont have one.

Create a new app
Give it a name and select your region - create app
Goto resources, and add Heroku postgres as an add-on, select the price plan that you desire
Click on settings, and reveal config vars
The following vars must be defined...


DATABASE_URL should have been populated by heroku

EMAIL_HOST_USER - is the sendng email address for user email verification (from signup).

EMAIL_HOST_PASS - is the sendng email address password for user email verification (from signup).

HEROKU_HOSTNAME - is the url which the app is deleivered by.

SECRET_KEY - is a string that the django application needs to run.

Go to the Deploy tab.
Connect to GitHub, sign in and connect to the required repository.
Scroll down to manual Deploy, select the main branch, and click deploy.
  
  
The live link can be found here - [Coffee Blog](https://mytodolist-b19dd36961bb.herokuapp.com/)

## Credits

### Content

- The code to make the social media links was taken from the CI [Love Running](https://code-institute-org.github.io/love-running-2.0/index.html) project.

### Media

- The background image was taken from [Pexels](https://www.pexels.com/pt-br/).

- The video in the gallery was taken from Youtube.

- The audio in the Home was taken from [Bensound](https://www.bensound.com/)




    
 
    
    

         

