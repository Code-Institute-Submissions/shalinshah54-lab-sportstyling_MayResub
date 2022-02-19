![image](static/images/)

# SportStyling

## Aim/ Purpose

The Sport Styling is an E-commerce website for sports relating shopping where anybody can purchase any sports related items. The website allows users to shop through the different products, there details, rating  and price. They can just add the product they like and can added to the bag and purchase the item/items by safely checking out. This website is my Milestone Project 4 for the Full Stack Developer course at Code Institute. You can access this site by clicking [Sport Styling](https://shalinshah54-lab-sportstyling.herokuapp.com/)

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

- As an initial process of the project design, wireframes were created for desktop and mobile screen sizes using [Figma Wireframe](https://www.figma.com/file/n6mZuV9SiD2jDU99MBnSrx/sportstyling?node-id=0%3A1).

## Existing Features
- All the pages on this website are mainly divided into 4 section which are:
  - Navbar
  - Flash Message
  - Main content
  - Checkout
  - Order Confirmation
  - Profile
  - Footer

#### Navbar
- Navbar consist of company name which is a link to the home page.
- Navbar also has a search bar which can find the products your looking for.
- There is a my account which is drop down for a new user it has registration and login.
- Once you login the my account drop down changes to the profile and logout.
- There is a shopping bag which adds items into it once you select any product and on clicking on it will take you to the checkout page.
- Then there are links All Products, Activewear, Sports and Special Offers. All are a drop down where you can selet the categories and go to the selected products.

#### Flash message
- There are flashing message which appears under the shopping cart if the task was successfull, and error occured.
- All the messages are color coded so it gives a visual feedback.

#### Main content
- On the home page there is small message which has a link shop now, on clicking onto it will redirect you to the all product page and all the items will appear.
- All the items contains add to cart option select size if necessary, quantity. 
- All the items have a brief description on it which is obtained by clicking on the product image.
- Once you add the item to the cart you'll get a message that the item has been added to the cart and cart will display item and the subtotal.
- There is registration form and login form once you signup.
- On the checkout there is a brief form which requires the user to add the information and safely checkout.
- Once the user checks out the message and the order confirmation appears which shows all the details of the purchased items.
- The user can login and under the profile can review there history of purchases.
- For the product management there is a form where the admin can make changes to the product add product and delete the product.

#### Footer
- Small footer is created to hold the copyright information of the website which is final section of the page and sit at the bottom and each page of the website contain same footer with same copyright information.

#### Home Page
- The home page contains a logo which is link back to the home page from any pages being used. There are nav links on the right side which only contains three links prior to logging in. Once logged in the session users will see the profile, add services and logout links along with the home link still there. The page also contains the search which will search for the category name and the description for all the services being added. There is an image for show all the services being provided by the company. On the lower part there is services field which shows all the services being posted. The page also contains a basic footer which shows the copyrights.

#### Search field
- By inputing the text on the search line and clicking on the search, if the search text is there in the database the search will show a result under the services field. There is a reset button next to the search which will redirect you back the home page by reseting the field.

#### Services field
- In this field the posted services will be visible to all the users. There is a card which appears the category name, created by and the date the job needs to be performed. On clicking on the activator on the right side which will activate the next card by sliding upwards and the full description for the post job will be shown. There is a close button to close the card and if the text or description is too long then a scroll down is there to view properly. Bottom if the slide card there is an edit and delete buttons only functioning when the users is in session and can only deleted or upgraded by created users. 

#### Registration
- On the registration page there is a simple form which has two required fields. First is the username and the second is the password 
Both are required fields and by clicking on the button it is validated and message appears on the top. If the user successfully logs in then the information is stored in the database. Additionally this page utilize Werkzeuz security which is python library to hash the password and stored in database securley. Underneath the registration form small text with login option also provided which allow user to login directly if they are already registered however select register option by mistake. This allow user to peform registration and login task from the same page without having to navigate to the exact page.


#### Login page
- This page looks very identical to register page and contains similar options however only accessible to those user who is already registered to the page, user simply need to input their username and password to login to the page, once login successful flash message will display on screen to welcome the user and user will be redirected to their own profile. This page utilize some python functionality to check and verify the users input and only allow user to login if their details matched with what they have provided while registration. Additionally python will display the flash message to inform user if username or password they supplied is not found and redirect the user back to login page again. Underneath the login form small text with registration option also provided which allow user to register directly if they are not registered however select login option by mistake. This allow user to peform registration and login task from the same page without having to navigate to the exact page.

### Add Services page
- This option is visible to the user only once they are logged into the page, this page allow user to add their own job by completing the form provided and then hit submit button. input elements in the forms need to fullfll certain criteria and if supplied input do not match certain criteria or left empty then warning message will appear below input field and colour of the bottom border will change to red, also required attribute is utilize on this form to ensure user are not able to submit the form without completing, if any of the field left empty and hit submit button then required attribute trigger and let user knows that they must complete the field. Python funtionality also added to this page to conduct some check to ensure that only user are able to add the job. once user select the option to add new job then python function will excute and do some checks and only let user to add the job if user in the session and user who logged in are the same person, otherwise python will immediatley redirect user to login page and display flash message accordingly. Javascript in the form of jQuery is utilized to validate the form and display and hide error message accordingly while user completing the form. Once user added the information, python will then send the information to mongoDB using insertOne method and also render the information in the home page

### Profile page
- This option also only visible to the user once they are logged in. Python function will execute once user select this option and check to verify the user first and if person selecting the option is really a user then python will allow user to access the page and display welcome message to the user, if user is not verified then python will redirect user to the login page and display flash message accordingly. Once user verified and inside the page user able to see all the job added to the page by themself and also able to edit and delete if they wish to do by just clicking the buttons brovided below job images.

#### Edit/delete job
- User can edit or delete their own job once they are inside their own account, every job added by user will be shown in My account page with job images and job title, each job has two options for user which are edit and delete. Once user select edit job option then python function will trigger to check wether person trying to edit the job is really a user or not, if not then user will be redirected to login page aagin with correct flash messaeg and if the person is really the user then python will populate the form with pre-field data in the input field and allow user to update their job information. Similar to add new job form, edit job form also need to pass the input validation check which is done by utilizing Javascript in the form of jQuery. once inpt field validate and user select the update button then all the updated information will be store in the database which is done by using updateOne method.
  Additionally user can also delete their own job, once user select delete button python will trigger the delete function and run if/else statement to check user's details and let user to act accordingly. First python will check if user is in the session or not then second step python will check if user logged in is the similar user who add this job. if both condition is satisfied they only user will be able to delete the job otherwise python will redirect the user to login page and display flash message accordingly
  python use mongoDB remove() method to perform delete job once condition satisfied. Once user select the delete button, modal will trigger and display warning message on screen to allow user to confirm their delete request or cancel, purpose of this modal is to prevent deleting the job straightway if user select the delete button by mistake or in case user wants to change their mind once after delete button clicked. 

### Logout
- This option only visible to the user once they are logged into the page, user can simply select the logout option and they will be loggout from the page, python function will execute once user select logout option and redirect them to login page immediately and display flash message accordingly.

## Issues and Debugging



# Technologies Used

## Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://en.wikipedia.org/wiki/Jquery)
-   [Python3](https://en.wikipedia.org/wiki/Python_Programming_Language)

## Frameworks, Libraries & Programs Used

1. [Bootstrap 5.x:](https://getbootstrap.com/)
    - Bootstrap 5.x was used to assist with the responsiveness and styling of the website.
2. [Font Awesome 5:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
3. [jQuery:](https://jquery.com/)
    - jQuery came with bootstrap to make the navbar entire site responsive.
4. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
5. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git. 
6. [Figma:](https://figma.com/)
    - Figma was used to create the [Figma Wireframe](https://www.figma.com/file/n6mZuV9SiD2jDU99MBnSrx/sportstyling?node-id=0%3A1).
7. [Heroku:](https://heroku.com/)
    - Heroku was used to create  and deploy our app.    
8. [Django:](https://django.com/)
    - Django was used to create the framework.
9. [Postgresql:](https://postgresql.org/)
    - Mongodb was used to create database and to connect server to our site.
10. [Stripe:](https://stripe.com/)
    - Stripe was used to accept and authorise payment for any item purchased on the site.
11. [AWS:](https://s3.console.aws.amazon.com/)
    - Amazon S3 was used to manage and save media and collectstatic file in Its cloud service.
12. - [HTML Formatter](https://htmlformatter.com/) 
    - HTML formatter was used to format HTML code
13. - [W3.CSS](https://www.w3schools.com/w3css/defaulT.asp) 
    - General resources.
14. - [Stack Overflow](https://pt.stackoverflow.com/)
15. - [Youtube](https://www.youtube.com/)     
16. - General resources.
17. - Code Institute SLACK Community

## Code Validation

- [W3C Markup Validation](https://validator.w3.org/#validate_by_input) 
  - ![HTML validation](static/validation and issues/html-validator.png)
  - W3C Markup Validation was used throughout the process to validate HTML codes
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) 
  - ![Css validation](static/validation and issues/css-validator.png)
  - W3C CSS Validation was used to vaildate CSS codes
- [JSHINT](https://jshint.com/) 
  - JSHINT was used for JavaScript code warning & error check.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) 
  - ![Lighthouse](static/validation and issues/lighthouse.png) 
- [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
  - Python tutor was used to visualize the python code and identify any error.

    