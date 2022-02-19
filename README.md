![image](static/images/)

# SportStyling

## Aim/ Purpose

The Sport Styling is an E-commerce website for sports relating shopping where anybody can purchase any sports related items. The website allows users to shop through the different products, there details, rating  and price. They can just add the product they like and can added to the bag and purchase the item/items by safely checking out. This website is my Milestone Project 4 for the Full Stack Developer course at Code Institute. You can access this site by clicking [Sport Styling]()

## Table of Contents

- [User Experiencess](#user-experiences)
  - [User Stories](#user-stories)
  - [UX Framework](#ux-framework)
  - [Wireframes](#wireframes)
- [Existing Features](#existing-features)
- [Features to be added in future](#features-to-be-added-in-future)
- [Issues and Resolutions](#issues-and-resolutions)
- [Technoligies Used](#technologies-used)
  - [Languages used](#languages-used)
  - [Frameworks, Libraries, Programme and Resources Used](#frameworks-libraries-programme-and-resources-used)
- [Code Validation](#code-validation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credit](#credit)
- [Media](#media)
- [Acknowledgements](#acknowledgements)


## User Experiences

The goal of this shopping site is to provide a satisfactory user experience and an accessible platform for users to find various available shopping items which is sports related. The website should allow users to easily register or login and search through the site for the best sports related products online. After finding the product you need to simply add the product to the chart and once finished shopping just checkout. The users are also able to easily add and edit their shopping card and delete the product anytime. Once the order is placed the confirmation is emailed to the user and allows them to see there ordered items.

### User Stories

#### First Time User Goals
- As a first time user, I would like to just see around the online shop for the right products before signining up.
- As a first time user, I would like to read description on the product I would like to buy.
- As a first time user, I would like to add products to my shopping bag. 
- As a first time user, I would like to see products in the bag before checking out so I can edit or remove the unwanted products from the cart.
- As a first time user, I would like to safely and securely enter my information to make the purchase.
- As a first time user, I would like to recieve a confirmation via email with the order number and details.
- As a first time user, as I have filled out the informaiton during checkout would like to use that to signup and register to the site. 

#### Frequent User Goals
- As a frequent user, I would love to see new products on the site with good deals, and sales.
- As a frequent user, I want to login to my existing account I would like to track my old order history.
- As a frequent user, I want to be able to recieve newsletters with deals and coupons online via email.
- As a frequent user, I would like to safely logout keep my information secured.

#### Return User Goals
- As a return user, I want to easily navigate accross all the products and shop without any problems.
- As a return user, I want to see more products with new and upcoming fashions.
- As a return user, I would like to recieve emails with coupons so I can return back for more shopping.
- As a return user, I want to be save my items in the cart so when I log back in I can see my added items in the cart.

## UX Framework

### Strategy

The Sport Styling is an online e-com site with products to shop from by using front-end and back-end functionality, created using HTML, JavaScript, CSS, Python and Django. The goal is to create a website that is user-friendly and allows users to easily search and buy so many products.

### Scope

The website is interactive and allows users to shop around see the products they like and easily add them to the cart. Once added to the cart if the shopper need to edit or delete the item from the cart they can easily do so.
Otherwise they can checkout and see there order confirmation. 

#### Functional Requirements

Functional requirements include: a user-friendly navigation menu, a search bar, properly display of products onclicking shop now button, working templates for registration, login. The product can be added to the card by choosing which product if it requires size then you can select that, you can select as much quantity you need. There is a add to cart buttton that can send your item to the shopping cart. On clicking on the cart buttton you can easily review your order make changes if needed otherwise safely click on checkout. Here you are redirected to the form page where the user has fill the information and the credit card info. And can place your order and see the confirmation on the next page with all your information added in the checkout form. 

#### Content Requirements

The content of the site should include a header and image, as well as a dropdown navigation menu. A search bar should allow users to search for prducts. There is my account link which allows to register and login. There is profile link which shows your history purchases. There is cart which redirects you to the checkout page. There is a checkout form where the user has to fill out and on checkout and order confirmation is given via email and the user can see it in the profile also. User can search the products by categories, by price, by alphabetical order or by Deals. The products are sorted accordingly. There is product management for the admin user where they can mannually enter the product to the site and remove the product if needed. They can change the price if there is a deal update images. 

### Structures

In this e-com site the main structure is to let the users come and shop for there sporting needs. They browse through the site and see all the different products and select them simply add them to the cart and checkout. Just add all the required info and checkout. The user can log back in and check there past history in the profile section. The super user is the only one who can add, edit and delete a product change its description and update the price.


### Skeleton

The skeleton of the website will utilise Bootstrap for the CSS layout of the pages, font awesome and google fonts are used. A dropdown navigation menu will allow users to go to their choose there category of items like to search for. The main landing page will function to allow users to select numerous products by click on shop now, and seeing the products and added them to your cart. Used the authall forms for registration and login. Stripe is used for the credit card varification and added the payment type. Webhook Handler are used if the user accidently closes the tab in the ordering process it still takes care of the order without any issues. Heroku is used for deployment and ASW for storing the static part of the site along with media. Crispy forms are used in the product management for adding, editing and updating data.

### Surface

The surface design of the website will also utilise bootstrap CSS to provide styling for the components of the website.
The first step for my research was visiting sites and knowing different layouts, elements in navigation bar, images, products there details and pricing which are stored in the product.json. Media folder holds all the needed images for the site.

### _Colors_ :

- Black
- White
- Grey
- Green
- Alert colors have been added like red, green, yellow and blue

### _Typography_ :

- Lato

 Google Fonts is used to style the text using the 'Lato' font used throughtout the site.

 ## Wireframes

- As an initial process of the project design, wireframes were created for desktop and mobile screen sizes using [Figma Wireframe](https://www.figma.com/file/WbKaj1kTqyEGyiKLDmUvlh/service-beyond).
