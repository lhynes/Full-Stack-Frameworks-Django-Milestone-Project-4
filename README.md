# [Explore More Adventure Agency](https://explore-more-adventures-ms4.herokuapp.com/)

 Code Institute - Full Stack Frameworks with Django Milestone Project 4

<h1 align="center">
  <a href="https://explore-more-adventures-ms4.herokuapp.com/" target="_blank"><img src="https://explore-more-adventures-ms4.s3-eu-west-1.amazonaws.com/media/EM_home_logo.png" alt="Explore More Adventure Agency"/></a>
</h1>

<h2 align="center">
Explore More Adventure Agency <br> 
</h2>
<div> 

A site to explore a wide range of adventure packages and book your trip of a lifetime. Explore More aims to emulate a holiday package 
site which provides adventure seekers a variety of locations to visit and participate in a range of activities. 
The Explore More app was designed, developed and deployed but Louise Hynes for 
educational purposes as part of her final preject for the Code Institute Software Development diploma.
<br>
In Phase one we are focusing on pre-made packages with the intention to build on this 
and allow users to create their own custom adventure packages.  
<br>
[Click here to view the page now!](https://explore-more-adventures-ms4.herokuapp.com/)

</div>


## Table of Contents

1. [**UX**](#ux)
    - [Project Goals](#project-goals)
        - [User Stories](#user-stories)
        - [Site Owner User Stories](#site-owner-user-stories)
        - [Developer and Business Goals](#developer-and-Business-Goals)
    - [Design choices](#design-choices)
    - [Wireframes](#wireframes)

2. [**Features**](#features)
    - [Current Features](#current-features)
    - [Future Features](#future-features)

3. [**Database**](#database)
    - [Database choice](#db-choice)
    - [Database Relationship](#database-relationship)
    - [Database structure](#db-structure)

4. [**Technologies Used**](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs](#frameworks,-libraries-and-programs)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#depl-heroku)
    - [Local Deployment (GitPod)](#depl-gitpod)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#ack)


# UX

## Project Goals

The primary goal of *Explore More(EM)* is to provide a clean, intuitive and engaging web app is to provide customers with an online platform to book their next big adventure. 

EM has two key target audiences: New Adventure Seekers/explorers and returning customers.
 People who want to make a relax or spiritual trip.
- People who are looking for the best locations.

**Project stakeholders**
- Adventure Seekers (Customers) – the agency offers recreational activty based adventures to individuals.
- Agency (Site Owners) – Explore More Adventure Agency the agency offers CHANGE travels for businesses and scientists for research purposes.

## User Stories

**New/Unregistered User**

The first impression of a site for any new potential customer is very important. With that in mind new visitros to the EM site want to: 
* Learn more about the EM Agency to know more about the team and the services provided via an about page
* Easily at first glance get an overview of the type of adventure packages avaialbe from the agency 
* Read more information and view  details of any particular adventure t better understand whats included in the package.
* Easily register for an account to update personal profile for quicker ordering in the future


**Registered User**

Additional permissions and features will be provided to registered users. A registered user will want to: 
* Easily log in and out of their account to access personal information and order history
* Edit profile information to update personal details
* View past orders to keep track of history with the site
* Save my billing details to autopopulate the form on checkout

**All Users**

All customers and visitors of the Explore More site - new, returning or registered users want to: 
* Discover more about the adventure packages based on activity caegory
* Easy access to all the adventure packages the EM agency offers
* A visually and operationally appealing site that makes if simple to learn more about various adventures
* Easily view the details of a specific adventure.
* Search for an adventure or activity category by its keyword and receive a feedback by the website if it isn't available.
* View the top 3 adventures at the time of browsing
* Contact the EM site owner to ask them a question
* Learn more about different adventures through blog articles, reviews and comments. 
* Sort the packages available on the site by category so that I can view just the products in that category.
* Wnen selecting an adventure package choose the number of people to be added and update the cart accordingly 
* Add a package to my cart to order chosen adventure package
* Update the number of items in my cart to order more or less of the chosen item
* Delete products from my cart to empty it or update the price total where relevenat
* Checkout with credid card using a secure payment method to complete order
* Get updated interactive messages so their is clear feedback on any action i.e. form completion,cart updated, payment processed etc. 
* Checkout in a simple and easy way with confirmation the process has been successful or other. 
* Receive an order confirmation


## Site Owner User Stories

EM adventure agency wants a site that will: 
* Excellently display their adventure packages and  help sell as many via an easy and simple process.  
* Make sure the customers are aware of the different advnetures available to them.
* Be easy to manage and have the ability to simply add, update and delete items. 


**Site owner/Admin goals:**

A site owner or admin wants to: 
* Easily list all adventures for sale and view all adventure package listings
* Create, edit, update adventure pacakages and categories - ensuring all information is correct
* Delete and packages or categories from the site
* Educate customers about the different options of adventures avialable and encourage them to engage via the site. 
* View and update all blog posts via the admin panel and update from draft to published when ready to share on the site
* Send email confirmations to users to them of successful registration and order confirmation.



## Developer Goals

- A well designed directory of adventure holiday pacakges that strives to engange new costomers to and envourage them to book a package with the company thus increasing revenue. 
- Good and clean programming that is robust and scaleable with the increase of adventure categories and locations. 
- A professional looking first attempt of building a full stack application with Django which the developer is excited to make a part of her portfolio and continue to develop in the future



## Design Choices

The goal with the look and feel of the site was to have a design that was simple, clean and engangeing. 
Where tuhe imagery of the adventures jumped out to the visitor. 
I reviewed some bootstrsp themes for inspiration 
- [Agency](https://startbootstrap.com/previews/agency)
- [Clean Blog](https://startbootstrap.com/previews/clean-blog)
- [Grayscale](https://startbootstrap.com/themes/grayscale/). I found it absolutely wonderful and I tried my best to stick to the theme while building my website.
The following design choices were made with this in mind:

**Fonts**

- The primary font **Roboto** was chosen because it is a crisp, sharp and easy to read font. It was inspired by the logo created on [Canva.com](https://www.canva.com/design/DAEZS9oLjqo/ORIPu67YhJCYB8cCxHwt_Q/view?utm_campaign=designshare&utm_source=sharebutton) 


**Colours**

- The primary colour choices for this site is navy and tourqupise. Inspired but the sea and also my brothers old scounts uniform of blue and navy. 


**Styling**

- On the listing page cards have a minimalist design
- Design and styting consistency was important on this site to help linking and combining the related areas together. 


**Adventure Tile Images**

- At present these have been kept simple and their layout will be considered again in the future. 


**Header and home Banner images**

- A strong header was chosen to make the logo and heading memorable 
- The homepage image was chosen to envoke a sense of the wild. 




### Wireframes

During the early part of the project wireframes were created using pen and paper and on [Pages](https://www.apple.com/pages/). 

- [Link](https://drive.google.com/drive/folders/1E-GPI5uT55XETPIjipmbFOIiUjZFPJ0j?usp=sharing)


# Features


## Current Features

###### Features on every page
- Fixed navigation bar with:
    - the logo on the left 
    - centered in the middle links to the different pages
    - links for account pages and cart planced on the rights
- Footer with the name of the company and representative social media links

###### Feature 1 - Home page
Home page with:
- Insights to Explore more 
    - Top adventures available to cusotmerts
    - reviews from customers
    - Feature story
    - contact information for the main office


###### Feature 2 - About page
- A simple page with information about the company.

###### Feature 3 - Contact page
- A simple page with contact form and the google map location of the company.

###### Feature 4 - Blog page
- List page overview of all adventure blogs
- Detail page for each blog and option for visitor to leave a comment


###### Feature 5 - Adventures Page
Presentation of all the adventures available. 
For each package, the following information is provided:
- The dates of the adventure
- the cost 
- the activity category
- CTA button to access the aadventure details

###### Feature 6 - Adventure details
Description page for a specific destination. The page should display:
- 4 high-quality pictures of the destination
- trip information (duration, distance, price)
- a form to look for upcoming trips to this destination
- trip description, requirements and safety guidelines

###### Feature 7 - Search all (trips) page / trips results page
Page with the list of all the trips available. The user has the option to refine his search by submitting a form to search for a specific trip (form fields: destination, departure site and departure date). For each trip the following information should be displayed:
- departure site
- departure date and time
- destination
- return date and time
- CHANGEship number
- small picture of the destination
- available slots
- price for 1 passenger
- select input for passengers
- button to book the trip

###### Feature 8 - Cart page
The shopping cart is available anywhere in the site. The cart page should display all the trips in the user's cart. For each item in the cart, the following information should be available:
- trip destination
- departure and return dates
- CHANGEship number
- recap of the trip with departure site (departure date and time) and destination site (return date and time)
- number of passengers and price
- total price of the cart
- button to checkout

###### Feature 9 - Checkout
Checkout process step by step with the following pages:
- (log in / sign up if the user is not logged in yet)
- contact details form
- forms to register passengers
- payment form
- confirmation of order booked4
- for each step of the checkout process, a recap of the cart is available as well as a return button to get back to the previous step. 

###### Feature 10 - FAQs page
Page with all the most frequently asked questions about our trips.

###### Feature 10 - Sign up page
Sign up form to register to an account.

###### Feature 11 - Login page
Form to log in to your account.

###### Feature 12 - Password reset page
Option to reset password by email in case users forgot it.

###### Feature 13 - Profile page
Profile page for users with an account that should display their:
- passenger details
- contact details
- option to change their password

###### Feature 14 - Order Summary page
Page with all upcoming and/or past trips that were booked by the user.

###### Feature 16 - Log out confirmation



## Future Features 

###### Waiting list

To provide the user with the option to register to a waiting list if a trip is sold out.

###### Activity dashboard for admin

To have a custom dashboard for the administrator of the website so they can monitor the activity of the travel agency.
- statistics: number of bookings, revenues, new users...
- edit/delete/add new trips

###### Option to add testimonials

Create a testimonial form where passengers could share their experience after completing a trip with us.







# Database



## Database choice

- Development: I used sqlite3 database which is the default database provided by Django. 
- Production: I used PostgreSQL for my deployed application hosted on Heroku. 


## Database Relationship

- The relation of the models are displayed in the image below
    <img src="./readme_docs/data-schema.png" height="500px" />

## Database structure

- The data consists of 10 models accross 7 apps
    - **Home app** - Displays the home page of the website.
    - **Checkout app** - Handles the checkout pages and the checkout view for product purchase, including payments.

        - DeliveryType Model - holds different delivery type information such as rate of cost for delivery, dispatch time, delivery_speed, constant deliver charge, limit at which delivery charge changes from constant to a rate

                name = models.CharField('Delivery Type', max_length=20)
                dispatch_speed = models.IntegerField('days to dispatch order')
                delivery_speed = models.IntegerField('days to deliver order')
                limit = models.DecimalField('order amount limit for set delivery cost', max_digits=5, decimal_places=2, default=0)
                const = models.DecimalField('set delivey cost', max_digits=5, decimal_places=2, default=0)
                rate = models.DecimalField('delivery rate', max_digits=5, decimal_places=2, default=0)

        - Order Model - Holds information on each order. This is populated when user completes the checkout. The details entered in the checkout will populate this model as well as custom calculations for total amount and discount and delivery charge

                order_number = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
                user_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_orders')
                first_name = models.CharField(max_length=30)
                last_name = models.CharField(max_length=30)
                full_name = models.CharField(max_length=70, editable=False, default='')
                phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Enter phone number in a format: '+111111111' and no longer that 15 digits.")
                phone_number = models.CharField(validators=[phone_regex], max_length=16, default=0)
                email = models.EmailField(max_length=254)
                address_line_1 = models.CharField(max_length=100,)
                address_line_2 = models.CharField(max_length=100, null=True, blank=True)
                city = models.CharField('city or town', max_length=85)
                region = models.CharField('region or county', max_length=85, null=True, blank=True)
                country = CountryField(blank_label='Country *')
                postcode = models.CharField('post/zip code', max_length=10)
                order_date = models.DateTimeField(auto_now_add=True)
                dispatch_date = models.DateTimeField('order dispatched on', null=True, blank=True)
                est_dispatch_dte = models.DateTimeField('estimated order dispatch date', ditable=False, null=True, blank=True)
                delivery_date = models.DateTimeField('order delivered on', null=True, blank=True)
                est_deliery_dte = models.DateTimeField('estimated order delivery date', editable=False, null=True, blank=True)
                delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE)
                delivery_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
                subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=0)
                total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
                original_cart = models.TextField(default='')
                stripe_pid = models.CharField(max_length=254, default='')

        - OrderLine Model that captures each item added to the cart and are used for calucations in the Order Model

                order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_line')
                product = models.ForeignKey(Product, on_delete=models.CASCADE)
                color = models.CharField(max_length=20, null=True, blank=True)
                quantity = models.IntegerField(default=0)
                line_total = models.DecimalField(max_digits=7, decimal_places=2, default=0, editable=False)

    - Memberships app - Displays different kinds of memebrship plans, handles user subscription to membership plans

        - Membership Model - contains memebrship plans

                name = models.CharField(max_length=50)
                pic = models.ImageField('Membership Picture', null=True, blank=True)
                free_delivery = models.CharField(max_length=1, hoices=FREE_DELIVERY, default='N')
                first_order_disc = models.IntegerField('First Order Discount', default=0)
                overall_discount = models.IntegerField(default=0)
                priority = models.CharField(max_length=10, choices=PRIORITY, help_text=('Priority of announcements'))
                q_gift = models.CharField('Quarterly Gift', max_length=50, null=True, blank=True)
                price = models.DecimalField(max_digits=4, decimal_places=2)

        - StripCustomer Model - stores information used to identify a user in Stripe payment system for subscriptions

                user = models.OneToOneField(to=User, on_delete=models.CASCADE)
                stripeCustomerId = models.CharField(max_length=255)
                stripeSubscriptionId = models.CharField(max_length=255)

    - Products app - Handles Product Display and Individual Item Detil view
        - Category Model - Stores Item categories

                name = models.CharField(max_length=20)
        
        - Product Model - stores Individual Item information

                product_code = models.CharField(max_length=36, default=uuid.uuid4, editable=False)
                category = models.ForeignKey(Category, on_delete=models.CASCADE)
                name = models.CharField(max_length=50)
                description = models.TextField()
                avg_rating = models.DecimalField('average product rating', max_digits=2, decimal_places=1, default=0, null=True, blank=True)
                price = models.DecimalField(max_digits=5, decimal_places=2)
                many_colors = models.CharField(max_length=1, choices=MANY_COLORS, help_text=('Will the product come in multiple colors?'))
                main_pic = models.ImageField('thumbnail picture', null=True, blank=True)
                pic2 = models.ImageField('additional picture 2', null=True, blank=True)
                pic3 = models.ImageField('additional picture 3', null=True, blank=True)
                pic4 = models.ImageField('additional picture 4', null=True, blank=True)
                added_date = models.DateTimeField(auto_now_add=True)
                release_date = models.DateTimeField('product release date', help_text=('Select today/now as the input if the product is being published now.'))

        - Color Model - handles they colors of an item if the item hsa mutliple colors

                name = models.CharField(max_length=20)
                color_hex = ColorField(default='#FFFFFF')
                product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    - Profiles app - Handles Profile view and creating a profile whenever a user registers. It also handles Order History view.
        - Profile Model - holds data on each user, this can be used in checkout to prefill the checkout form.

                user = models.OneToOneField(User, on_delete=models.CASCADE)
                membership = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True, blank=True)
                user_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter phone number in a format: '+111111111' and no longer that 15 digits.")
                user_phone_number = models.CharField(validators=[user_phone_regex], max_length=16, null=True, blank=True)
                user_address_line_1 = models.CharField(max_length=100, null=True, blank=True)
                user_address_line_2 = models.CharField(max_length=100, null=True,  blank=True)
                user_city = models.CharField('city or town', max_length=85, null=True, blank=True)
                user_region = models.CharField('region or county', max_length=85, null=True, blank=True)
                user_country = CountryField(blank_label='Country',  null=True, blank=True)
                user_postcode = models.CharField('post/zip code', max_length=10, null=True, blank=True)


    - Reviews app  - Handles CRUD operations for Reviews
        - Review Model

                user = models.ForeignKey(Profile, on_delete=models.CASCADE)
                product = models.ForeignKey(Product, on_delete=models.CASCADE)
                title = models.CharField(max_length=50)
                description = models.TextField()
                rating = models.IntegerField(choices=RATE)
                upvotes = models.IntegerField(default=0)
                downvotes = models.IntegerField(default=0)
                date_posted = models.DateTimeField(auto_now_add=True)

    - Shpping Cart app - Handles CRUD operations with order items in cart
        - No models



</br>

# Technologies Used


## Languages

##### [HTML5](https://www.w3.org/TR/html/)
- I used HTML to create the static content of my website.
- The following [code validator](https://validator.w3.org/) was used to test my HTML code.

##### [CSS3](https://www.w3.org/Style/CSS/)
- I used CSS to style my website and personalize it.  
- The following [code validator](https://jigsaw.w3.org/css-validator/) was used to test my CSS code.

##### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- I used core JS in coordination with Sweet Alert library.
- [JSHint](https://jshint.com/) was used to check my JS code quality.

##### [Python 3](https://www.python.org/downloads/release/python-374/)
- I used Python 3 as the back-end programming language for my application.


- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://www.javascript.com/)
- [Python 3.8.5](https://www.python.org/) (Python 3.9 was not compatible with cryptography==3.3.1)




## Frameworks & Libraries

### Frameworks, Libraries and Programs Used
- Front-End
    - [Bootstrap 5.0](https://getbootstrap.com/) - Used for the responsive layout as well as the navigation, header, footer, forms, dropdowns, item cards, modals.
    - [Font Awesome](https://fontawesome.com/) - Font Awesome was used to add social media icons at the bottom of the page and icons throughout the pages.
    - [Google Fonts](https://fonts.google.com/) - Google Fonts was used to import 'Montserrat' font in the style.css file.
    - [Notyf](https://github.com/caroso1222/notyf) - Used to display messages
    - [jQuery 3.5.1](https://jquery.com/) - Used in stripe javascript logic
- Back-End
- [Django](https://www.djangoproject.com/) - used as the main framework to build the project.
- [Stripe](https://stripe.com) - used to facilitate single payments and subscription plans
- [Psycopg2](https://pypi.org/project/psycopg2/)  - used to allow postgresSQL to be used with python
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - used to display forms
- [Gunicorn](https://pypi.org/project/gunicorn/)  - deployment tool
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  - aid the deployment of AWS S3
- [Pillow](https://pillow.readthedocs.io/en/stable/) - image proccessing tool in python
- [Whitenoise](http://whitenoise.evans.io/en/stable/)  - aids static file management and serving
- [pip3](https://pip.pypa.io/en/stable//)  - used to install all packages in python
- [SQlite3](https://www.sqlite.org/index.html) - used as a database in development
- [PostgreSQL](https://www.postgresql.org/) - used as a database in deployment
- [AWS S3](https://aws.amazon.com/)  - used to store images and static files displayed in the deployed site
- General
    - [Git](https://git-scm.com/) - Git was used to allowing for tracking of any changes in the code and version control.
    - [Github](https://github.com/) - GitHub is used to host the project files.
    - [Visual Studio Code](https://code.visualstudio.com/) - IDE used to compile the code as well as facilitate a virtual environment.
    - [TinyJPG](https://tinypng.com/) - Used to minify and compress images.
    - [Heroku](https://dashboard.heroku.com/apps) - A cloud platform used to deploy the web application.
    - [Lightroom](https://www.adobe.com/ie/products/photoshop-lightroom.html?gclid=CjwKCAjwwYP2BRBGEiwAkoBpAqomS77OrQwQggC9QPnPACrkLBs-2AcrW9ZUvxbUJnFOgbRGKNeNEhoC95IQAvD_BwE&sdid=88X75SKS&mv=search&ef_id=CjwKCAjwwYP2BRBGEiwAkoBpAqomS77OrQwQggC9QPnPACrkLBs-2AcrW9ZUvxbUJnFOgbRGKNeNEhoC95IQAvD_BwE:G:s&s_kwcid=AL!3085!3!394412108599!e!!g!!lightroom) - Lightroom was used to edit and resize all images.
    - [Adobe Xd](https://www.adobe.com/ie/products/xd.html) - Adobe Xd was used to create mockups.
    - [Balsamiq](https://balsamiq.com/wireframes/desktop/#) - Used for wireframes

# Testing 

All the documentation regarding the testing of this project can be found in this [TESTING.md](testing/TESTING.md) file.


## Testing

For this project, I put the website through some vigorous testing. This included testing manually myself, by a friend, by my Mentor and also by the slack community in the peer-code review page.

**User Story Testing**

Due to the length of the user story testing, I have saved all of this on a separate document which you can view [here](static/readme_docs/user_story_tesitng.pdf), as well as added some of the new user stories below.


*As a new user, I want to be able to learn more about Magnetic Eyes lashes so that I can get to know the brand* 
* When a user lands on the website, they are met with a couple of options to find out more about Magnetic Eyes Lashes:
* Navigation item ‘About’: This navigation item links the user further down the homepage so they can read more about the products.
* Intro text: Beneath the Jumbotron is a short introduction which explains what Magnetic Eyes are about.
* Additionally, a user can head to the blog to read articles on Magnetic Eyes and its products.
 

*As a new user, I want to be able to understand how Magnetic Lashes work so that I can learn what the product is about and how to use them*
* A user can quickly and easily learn more about how Magnetic Lashes work by clicking on one of two main navigation options which are both immediately available when the user lands on the site:
* Application: This link takes the user to a page which explains how to apply magnetic eyelashes.
* About: This link takes the user down to an anchor on the homepage which explains more information about magnetic eyelashes and how they work.
 

*As a new user, I want to be able to easily view all eyelashes available so that I can decide which product I might like to learn more about*
* In the main navigation, the first item a user can see is ‘Shop’ – this link takes the user to the main shop page which displays all the products there are for sale. By clicking on one of those products, the user is taken to a product detail page to read more about that item.
* Additionally, on the homepage, there are 3 CTA’s to take the user to the shop.


*As a new user, I want to be able to view the details of a product so that I can learn more about that particular product* 
* When a user clicks to view an item, either by clicking the item image or item name, they are taken to a product details page.
* On this page, they will be able to learn more about the product as well as add their desired quantity of that item to the bag.


*As a new user, I want to be able to easily register for an account so that I can see and save my personal details for quicker ordering in the future*
* In the main navigation (or in the mobile toggler menu) a user can easily find the ‘My Account’ name and icon. This link provides a dropdown prompting a user to log in or register for an account.
* Upon clicking Register, the user is taken to a page to register for an account by filling in their email, username and choosing a password.
* The rest of the process to confirm their email is clearly guided. The user is told they will receive an email to confirm their email address. Once this is link is clicked, they will be taken to the homepage and be informed via a notification that they have successfully signed up to Magnetic Eyes.
* In order to save their details for faster purchasing, when they make their first order they can choose to save those details to their account using the check box provided.
* If a user is at the checkout point without having registered for an account thus far, they will be prompted that they can do so at this point, where the checkbox is replaced with a login/register link.

To view the Registered User Story testing, website shopper user story testing and site owner user story testing, please view the full document [here.](static/readme_docs/user_story_tesitng.pdf)

**Manual Testing**

I manually tested the entire website across 3 desktop browsers (Chrome, Safari and Firefox) on tablet on 2 browsers (Chrome and Safari) and an iPhone on two browsers (Chrome and Safari).

The results of this testing can be found in the following document [here](static/readme_docs/testing.pdf),


**Automated Testing**

In addition to the full manual testing, I also decided to add some automated testing, as advised in the short testing section of the course.

I created 20 automated tests in total. These include:
* Blog>tests.py: Comment form testing and blog view testing
* Checkout>tests.py: Order form testing
* Products>tests.py: Product form testing and Product page view test
* Sendemail>tests.py: Contact form testing and view test



**W3C CSS Validator**

I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to check the validity of my CSS code.
* Two Bootstrap errors did occur, which I was advised to ignore. 
* All of my code otherwise passes without any errors



**W3C HTML Validator**

I used the [W3C HTML Validator](https://validator.w3.org) to check the validity of my HTML code

The Shop page and Bag page issued a warning to consider adding H2-H6 headers but I didn’t feel this was necessary on these pages as it did not add anything to the page and there are headers in the section above.
 
All other code passed with no errors.



**JSHint**

All JS code has been run through JS hint to check for errors. Whilst there were no errors with my code, two errors were appearing in the checker:

Undefined variable: $ : According to a Tutor, the reason for this error is that JSHint isn’t designed to pick up a jQuery syntax

Undefined variable: Stripe : This is a value being pulled in from the settings which I am advised cannot be checked by JSHint.



**PEP8 Compliant Testing**

Each and every .py file has been check over to make sure it complies with PEP8 formatting rules, both manually in the Gitpod window, as well as running the code through POP8online.com.

There are no errors through the PEP8 check. However, there are a couple of highlighted rows of code where I have decided not to make the suggested corrections:

*‘Avoid using null=True on string based fields.’*
Pages with error: Blog>models.py & products>models.py
I have left this error as it is a string path to a source file.

*‘Avoid using null=True on string based fields.’*
Pages with error: checkout>models.py, profiles>models.py, product>models.py

*‘Line too long’*
Pages with error: settings.py, checkout>webhooks.py, checkout>webhook_handler.py, checkout>models.py
These have been left as is as these lines should not be broken.

*'checkout.signals' imported but unused*
Page with error: checkout>apps.py
This ‘error’ has been left. This code is needed, and if removed the order total and grand totals appear as £0. 










# Deployment

<a name="depl-heroku"/>

## Heroku

My application was deployed through [heroku](https://dashboard.heroku.com) using the master branch of my github repository for this project. The following steps were implemented to deploy this project:

1. Install **gunicorn** package to run the application on Heroku.
    - `sudo pip3 install gunicorn`
2. Install **pycopg2** to connect to PostgreSQL
    - `sudo pip3 install psycopg2`
3. Create a **requirements.txt** file
    - `sudo pip3 freeze --local > requirements.txt`
4. Create a new Heroku application
    - Sign up to a new account if you do not already have one.
    - Create a new application by clicking on `new` then `create new app`.
    - Set the name of your application and select your region and click on `create app` to finalize the creation of your app. 
5. Install PostgreSQL add-on
    - `heroku addons:create heroku-postgresql:hobby-dev`
6. Create a **Procfile** in the root directory
    - content: `web: gunicorn CHANGEx.wsgi:application`
7. Set the following config variables as environment variables:

Config Vars | Value
----------- | -------------
AWS_ACCESS_KEY_ID | `<AWS_ACCESS_KEY_ID>`
AWS_SECRET_ACCESS_KEY | `<AWS_SECRET_ACCESS_KEY>`
DATABASE_URL | `<DATABASE_URL>`
EMAIL_HOST_PASSWORD | `<EMAIL_HOST_PASSWORD>`
EMAIL_HOST_USER | `<EMAIL_HOST_USER>`
EMAILJS_USER | `<EMAILJS_USER>`
GOOGLE_API_KEY | `<GOOGLE_API_KEY>`
HOSTNAME | `<HOSTNAME>`
SECRET_KEY | `<SECRET_KEY>`
STRIPE_PUBLISHABLE | `<STRIPE_PUBLISHABLE>`
STRIPE_SECRET | `<STRIPE_SECRET>`
USE_AWS | `<TRUE>`

5. In the `Deploy` tab, choose `Connect Github` as **Deployment Method** and *Enable Automatic Deployment* from the Github master branch so that any new commit will be automatically deployed through your heroku app. 

<a name="depl-gitpod"/>

## Local Deployment (GitPod)

To deploy this project locally using gitpod you will have to create a gitpod account and use a web browser with a stable internet connection as gitpod is an online IDE. I suggest you use Chrome as web browser so that you can use gitpod chrome extension to speed up the deployment process. 

1. Create a Gitpod account (if not already)
    - Go to [GitPod](https://www.gitpod.io)
    - Click on `Go to App` and click on the green `Authorize gitpod.io`
    - Agree to the terms and then create your free account
2. Add gitpod browser extension for Chrome:
    - Go to [GitPod Chrome Browser Extension](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki)
    - Search for "gitpod" in chrome web store search bar
    - Click on `Add to Chrome` then click on `Add to extension`
3. Clone this project repository from github
    - Go to my [repository](https://github.com/CHANGEiaDelorme/project-CHANGEx) for this project.
    - If you successfully installed the gitpod browser extension you should view a green `Gitpod` button in the top right corner of the repository (next to `Clone or download` button). Click the `Gitpod` button. 
    - This will allow you to open this repository directly in gitpod for editing.
4. Set the following environment variables for the project:

Env Vars | Value
----------- | -------------
AWS_ACCESS_KEY_ID | `<AWS_ACCESS_KEY_ID>`
AWS_SECRET_ACCESS_KEY | `<AWS_SECRET_ACCESS_KEY>`
EMAIL_HOST_PASSWORD | `<EMAIL_HOST_PASSWORD>`
EMAIL_HOST_USER | `<EMAIL_HOST_USER>`
EMAILJS_USER | `<EMAILJS_USER>`
GOOGLE_API_KEY | `<GOOGLE_API_KEY>`
HOSTNAME | `<HOSTNAME>`
SECRET_KEY | `<SECRET_KEY>`
STRIPE_PUBLISHABLE | `<STRIPE_PUBLISHABLE>`
STRIPE_SECRET | `<STRIPE_SECRET>`

5. The default local database for django projects is SQLite 3.
6. Download all the dependencies necessary to run this project and listed in the **requirements.txt** file. 
    - Run the following command `pip3 install -r requirements.txt`
7. Create a local development server:
    - In the workCHANGE run the following command `Python3 manage.py runserver`.
    - You should now have a gitpod link to the deployed app. 



# Credits



### Content

- For the concept of this web app, (as you could guess) I got inspired by [CHANGEX](https://www.CHANGEx.com/). I decided to keep the same name to make it more realistic, I don't think it would be an issue as it is a project for educational purposes only.
- For content related to microgravity, scientific experiments, general terms & conditions, and safety guidelines, I have used information from [AirZeroG](https://www.airzerog.com/). This company organizes parabolic flights in Europe for the general public.
- For content specifically related to the trips, I looked online to get the distance from earth, moon etc... I researched a list of launch sites. I have set the price and duration of each trip myself - even though for some trips it's not that realistic (Mars).

<a name="media"/>

### Media

- I created the logo of this website thanks to [Hatchful](https://hatchful.shopify.com).
- All the images used for this project were found on [Pexels](https://www.pexels.com).
- I used [Font Awesome](https://fontawesome.com/v4.7.0/icons/) for my icons.
- Demo picture of my app used in this README file: [Am I Responsive](http://ami.responsivedesign.is/#)

**Images:** 
* Banner images: These images were from free stocksites [Pexels](https://www.pexels.com/discover/) and [Unsplash](https://unsplash.com/) and overlaid with a purple gradient design.
* Product images: All product images were taken by myself and are of my own products I used to sell.
* Homepage & Application page photos and video: All images and videos were taken and created by myself. The photo of the eye is my eye.
* No Image: [No Image Icon](https://www.freeiconspng.com/) provided the image for when a product does not have an image associated with it.


### Code
- [Datepicker](https://jsbin.com/culagonula/edit?html,js,output)
- [Timeline](https://bootsnipp.com/tags/timeline/4)
- [Collapsable](http://jsfiddle.net/hungerpain/eK8X5/7/)
- [Login Success View](https://stackoverflow.com/questions/16824004/django-conditional-login-redirect/16824337#16824337)
- [Django Email](https://stackoverflow.com/questions/2809547/creating-email-templates-with-django)
- [Corey Schafer's Django Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

**Blog Implementation Tutorial**

In order to implement my brand new modules, I followed the following tutorials, with some additions of my own (such as adding images)

[Blog App](https://djangocentral.com/building-a-blog-application-with-django/)

[Blog Comments](https://djangocentral.com/creating-comments-system-with-django/)

[Blog Pagination](https://djangocentral.com/adding-pagination-with-django/)

[Sign In With Google](https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5)

**SendEmail (Contact Us) App Tutorial**

In order to add a contact app (or sendemail) I used the following tutorial to do so. I made some small amends, such as using Crispy Form instead of the suggested.
[Django Email Contact Form](https://learndjango.com/tutorials/django-email-contact-form)







### Acknowledgements
- I would like to greatly thank my Code Institute mentor, Reuben Ferrante, for his guidance, advice and support over the course of this project. 
- A huge thanks to all the tutors at Code Institute for their great support and patience.
- Finally my partner Michael and family for keeping my spirits high and supporting me along the way with tea and site testing.