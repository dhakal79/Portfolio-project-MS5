# Dhakal Consultancy 
Welcome! 
## Introduction
The global water crisis is a major concern today and will become more severe in the coming years. The availability of freshwater becomes more challenging in the semi-arid regions. However, in other areas where freshwater is available(surface and groundwater),contamiantion and degradation of the water quality is a major issue risking the health of millions of people. As per the SDG 6, availability of fresh and safe water for all is a basic necessity for overall human development. Therefore, there is a need of experts in this filed who can provide the solutions/ideas instantly/remotely so the action on site can be taken immediately. 

The overall aim of Dhakal Consultancy is a full-stack ecommerce web application to sell its services in the field of water treatment, desaliantion, water and sanitation as well as frontend and backend coding applications to customer from entire world.  This project is created as a part of Code Institute's Full Stack Software Development course.
The admin of the website will have the ability to use all CRUD functionality (Create, Read, Update, Delete).

A live website can be found [here](https://dhakalconsultancy.herokuapp.com/).

![consultancy website preview](media/readme/media/preview.jpg)

# Table of Contents
 [1. About the Dhakal Consultancy](#dhakal-consultancy)

 [2. User Expereince (UX) design](#ux)
  - [Project Goals:](#project-goals)
  - [User Goals:](#user-goals)
  - [Site Skeleten(Wireframe):](#wireframe)

  [3. Features](#features)
 - [Existing features](#exist-feature)
 - [future features](#future-feature)

 [4.Technologies used](#technologies-used)

 [5.Testing](#testing)

 [6.Bugs](#bugs)

 [7. Deployment](#deployment)

 [8. SEO](#seo)
 [9. Marketing](#marketing)
 [10. Social Media](#social-media)

[8. Acknowledgement](#acknowledgement)

  <a name="dhakal-consultancy"></a>

# 1. About the Dhakal Consultancy website
  [Go to the top](#table-of-contents)

This consultancy website is desinged as a a platform to sell the expertise in the field of water and full-stack software.  
   <a name="ux"></a>
# 2. User Expereince (UX) design
  [Go to the top](#table-of-contents)

  Water crisis is now a global issue which can be addressed by the joint efforts from professional working in this field. Therefore, sharing of knowledge and expereience among professional is important mainly to i)to save the available resources and time and ii) solve the global water issue. This project is thus aimed to design the user friendly water channel blog which allows all water professional to register and participate in sharing their knowledge and experience in water related issues.  

The following users types can be benifitted from the blog:

- Water professionals
- Students in field of water.
- University/institution who can consider the platform for thier educational activities.

   <a name="project-goals"></a>
## 2.1 Project Goals
  [Go to the top](#table-of-contents)

The main goal of this project is to develop a full-stack ecommerce web application to sell consultancy services in the field of water treatment, desaliantion, water and sanitation as well as frontend and backend coding applications to customer from entire world.  

   <a name="user-goals"></a>
## 2.2 User Goals
  [Go to the top](#table-of-contents)

First Time Visitor Goals

-  Be able to see some information about the consultancy so that he/she knows the background and history of the company.
- Be able to view the list of available services so that he/she can select the service that they are interested for
- Be able to easily view the details about the service so that he/she can can decide whether to take the service or not.

- Option to search for a service available by name or description so that he/she can find a specific service that I am interested on.
- Be able to easily add service items to my purchase basket so that he/she can view all the services that are interested for 

- Be able to easily remove items and update quantities of service from my purchase service list so that he/she can remove any services that is not of interest from the list.
- Be able to select the the number of service hours of a service when selecting the particular service so that he/she can select the service with actual hours interested in.
- Be able to easily enter my payment information at the checkout page so that he/she can checkout with no hassles.
- Be able to receive an email confirmation after completing the checkout process so that he/she can have the proof of payment for the service requested.
- Be able to see a contact page where i can write my details and questions so that I can send any query and make an appointment to discuss about the service.

Returning Visitor Goals
- Be able to easily register an account so that he/she can have a personal account and be able to view profile.
- Be able to receive an email confirmation after registering so that I can verify that my account registration is successful.
- Be able to easily login or logout so that he/she can access his/her personal account information.
- Be able to easily reset my password in case I forget it so that I can have an access to my account.

Frequent User Goals
-   Be able to subscribe for newsletter so that I can follow the update of the organization.
- Be able to unsubscribe for newsletter so that I can stop to follow the update of the organization anytime i wish.

Three step processes were followed as below:
- Set the user requirements and added to the user stories within the github project
![User Stories](media/readme/media/userstories.jpg)

- After the gradual fullfilment of the requirements, the stories were moved to in progress column.
![User Stories](media/readme/media/userstories_progress.jpg)

- And finally when requirement was fully met, it was moved to the complete column.
![User Stories](media/readme/media/userstories_complete.jpg)

  <a name="wireframe"></a>
## 2.2 Site Skeleten (wireframe)
  [Go to the top](#table-of-contents)

[Balsamiq](https://balsamiq.com/) was used to create wireframes of the website. This was very useful as it gives the template of the UI. Wireframes were designed for  mobile browser format. The concept design (wireframes) of webpages of the water channel prepared is presented below.

### Home page (MY Water Channel)
![wireframe](media/image/wireframe-home.jpg)

### About us 
![wireframe](media/image/wireframe-detail.jpg)

### Our service 
![wireframe](media/image/wireframe-pagination.jpg)

### Latest News 
![wireframe](media/image/wireframe-post.jpg)

### Contact us 
![wireframe](media/image/wireframe-category.jpg)

 <a name="features"></a>

# 3. Features
  [Go to the top](#table-of-contents)

<a name="exist-feature"></a>

## 3.1 Existing Feature

### 3.1.1 Navigation bar:
Dhakal consultancy has naviagation bar that includes; 
- Home page
- About us
- Our services 
- Latest news
- contact us 
- My account 
- Purchase bag 

Any users have an ability to view the home page, page detail view, register in the webpage and login as registered user.
![Nav bar](media/readme/media/nav-bar.jpg)

- Link for Social media(facebook) and newsletter subscription are placed at the bottom of the each page in the footer. 
![footer](media/readme/media/footer.jpg)


### 3.1.2 Django admistration page

The admin page is created where the admin has the ability right to the all CRUD functionality of the website. 

![Nav bar](media/image/django-admin.jpg)

### 3.1.3 Home Page 

The website has homepage with the image and a button for the services. The users can click on the button to explore the possible service provided by the consultancy.The page also contains the footer with facebook business page link , newsletter subscription and contact us as well as option to login and logout.

![Home Page](media/readme/media/home-page.jpg)

Home page is design with functionality of pagination. Each page shows maximum of 6 recent posts. In order to view other older posts  there is NEXT button at the bottom of page, which will redirect to the next page.  The next page also has the button " PREVIOUS" which will redirect to the previous page of the blog.
At the bottom of the page there is a link to the social media where the users can connect to the admin social media page.

![Home Page](media/image/home-page-2.jpg)

### 3.1.4 Login and Register

The user is able to register, login and logout. The blog has a new view or form to allow the user to login, logout or register. The users have an full access to post/edit/update/delate the post once they register and login.


### 3.1.5 Comment the post

The registered Users is allowed to make comemnt on the blog post detail view page and is only possible when they logged in the blog site. 

![Comment Page](media/image/comment.jpg)

The user can write a comment about the blog by clicking on "please provide comments". The name, date and time of comments will appear on the comment box.

![Home Page](media/image/add-comment.jpg)

## 3.1.6 Like the post

Registered users are able to like post of theirs and other user's post but only when they are logged in. The total number of likes will be recorded on the post. This provides an opportuntiy to know how popular is the blog post. 

![Like Page](media/image/like-post.jpg)

### 3.1.7 Add Post in webbrowser

Registered Users are able to create their own posts within the app but only when logged in. They can do this from the Add Post button within the navbar

Each post is automatically stamped with the date of when the posts were uploaded.

Once the new post is added in the blog channel, a flash message "The new blog post has been added" will appear in the Home page.
![Flash message](media/image/flash.jpg)

### 3.1.8 Edit and Delete Post

Registered users are able to edit their own posts within the blog but only when they are logged in.

![Edit Page](media/image/edit.jpg)

They can also delete their own post

![Delete Page](media/image/delete.jpg)
When a user is not registered or logged in they are not shown the "Edit Post" or "Delete Post" buttons.

Here is an example when registered as differnt user, one can view the post but the option of edit and delete is disappear as these post is of admin.

![edit/delete Page](media/image/edit-post.jpg)

### 3.1.9 Add Categories of the post

Each post is given a category by choosing from the scroll down menu when creating a post. Each post is then added to the corresponding category list enabling the user to choose a category and view all posts within.

There is also a dropdown menu within the navbar to allow the user to choose a category to view from the homepage.
Here is one example of post under category "drinking water"
![Category Page](media/image/category.jpg)

### 3.1.10 Error page 404 and 500
The page not found (404) error and server error (500) has been addressed. For both cases, a pop up message and asked to redirect to home page appears. 

![404 error](media/image/error_404.jpg)

<a name="future-feature"></a>
## Future Features

- Profile page to be included that describes the bio and profile picture or the post author.
- Automatically populate the username instead of adding name to comment form.
- Add forget user name and password
- Add search button on nav bar 
- Add text editor in the add page content like what we have in admin add post page.

<a name="technologies-used"></a>

# 4. Technologies-used
  [Go to the top](#table-of-contents)
* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language)) was used as a scripting language for the app development in this project.
* [HTML5](https://en.wikipedia.org/wiki/HTML5) (markup language) was used for structuring and presenting content of the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) (Cascading Style Sheets) was used to provide the style to the content written in a HTML.
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) was used to for a rapid development and clean, pragmatic design as well as to provide the style to the content written in a HTML.
* [Github](https://github.com/) was used to create the repository and to store the cproject's code after pushed from Git.
* [Gitpod](https://www.gitpod.io/) was used as the Code Editor for the site to allow me to add, commit and push to GitHub
* [PEP8 online](http://pep8online.com/) tool was used for manual testing procedures for code validation.
* [W3C Markup](https://validator.w3.org/) and [Jigsaw validation](https://jigsaw.w3.org/) tools were used to validate the HTML code and CSS style used in the proejct.
* [Ami](http://ami.responsivedesign.is/) was used to develop a Mockup screenshot generator
* [Heroku](heroku.com) was used to deploy a final version of the Python Essentials application code.
* [Bootstrap](https://getbootstrap.com/) to make responsive design much easier due to their "mobile first" design.
* [PostgreSQL](https://www.postgresql.org/) was used 
    as a database.
* [AWS](https://aws.amazon.com/) was used to host all static and media files.
* [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.
* [Google Fonts](https://fonts.google.com/) was used to import the font style into the style.css file which is used on all pages throughout the project.


<a name="testing"></a>

# 5. Testing
  [Go to the top](#table-of-contents)
## 5.1 General
- Throughout the development process zI have tested each View, Model and URL together after each one had been written. 
- Any changes made in the models, I performed makemigrations and migrate. In the sametime, code for view.py and urls were also written and run the server to check if there are any issues or not. I checked if the url written directed to the right page that i am expecting or not. 
- All the pages of the website were manullay tested 
- All the code written were also validated using W3C validator (for Html), PEP8 online (Python),Jigsaw (CSS) and JS Hint(Javascript). the details of each testing are summarized below.
## 5.2 W3C, Jigsaw, JS Hint and PEP8 online validation
  I have tested manually (for each page of the website) by passing the code through W3C, JigSaw and PEP8 online validation tool and confirmed there are no errors. The screenshot is as shown below:
  for W3C validation (sample example for home page)
  ![W3C validation](media/image/w3c.jpg)
  for CSS validation
 ![JigSaw validation](media/image/css.jpg)

  for PEP8 validation
 ![PEP8online validation](media/image/pep8online.jpg)
   forJS Hint validation
 ![JS Hint validation](media/image/pep8online.jpg)
 
## 5.3 Mannual testing 

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Water Channel(Home page) | checked if on click to "Water Channel", the browser redirects me to the Water Channel "home page".| PASS
Water Channel(Home page) | checked if recent posted blog appear on the the front page of home page or not.| PASS
Pagination | checked if there appears 6 blog posts in "Water Channel" home page or not. And after clicking to the button NEXT goes to the other pages where other additional blog posts appears and vice versa.| PASS
Detail page | checked if by clicking "more...." on home page of each blog post redirect to the detail page or not.| PASS
Detail page| checked if button "back" in detail page redirect to home page or not.| PASS
Post like| checked if registered user can like to blog post or not and count the number of likes.| PASS
Comment | checked if registered user after clicking on "please provide comment" redirect to comment form page or not.| PASS
Comment | checked if after clicking to add comment, the page redirect to the correcting detail blog page with name of blog user who commented and date when he/she made the comment.| PASS
Register/login|checked if users can register and login in the blog or not".| PASS
Edit/Delete post |checked if the post can be edited and deleted by the authorized resitered user only or not.The users can edit and delete their own post only| PASS
Catergory | checked if on click to each "Category", the browser redirects me to the the respective category page.| PASS
Add category| checked if register user can add additional new category to the blog post and after addition new category appears as new category in the nav bar.|PASS 
Social media links|checked if social media links provided in the footer open in the separate page.|PASS
Responsive design|Checked if the design is responsive to differnt media size or  not.|PASS
Error page 404/500|Check if the issue of error page 404/500 is solved or not.| PASS
Flash message notification|check if once the user post in the blog an automatic flash message " the new blog post has been added" will appear on the home page or not.|PASS
Draft post|check if any blog post as draft visible to other users or not.|PASS


<a name="bugs"></a>

# 6. Bugs
  [Go to the top](#table-of-contents)

## 6.1 Solved bugs
- The update on static css did not show up in webpage after heroku deployment. This was solved by changing below;

    In setting.py

      1. debug = "DEVELOPMENT" in os.environ

    In, env.py add,

      2. os.environ["DEVELOPMENT"] = "true"  and 

    In Heroku setting remove:

      3. DISABLE_COLLECTSTATIC          1  

- The update in static CSS also did not change in gitpod environment as well. This was solved by adding missing '/' in STATIC URL = 'static/'

- The detail page edit did not work and it says the page cannot be reached. this was solved by adding missing '%' before url in the link below:
<a href="{ url 'edit_post' post.pk %}">(Edit)</a>

- Received an HTML validation error in the add post page. The Error was: Attribute maxlength not allowed on element select at this point.This issue was solved by switching CharField to TextField in the Post Model 

- In edit page, the new image selection (repalcement of old image) did not work. This was solved by adding 
  enctype="multipart/form-data as;
  <form method="POST" enctype="multipart/form-data">
  
## 6.2 Unsolved bugs
Following PEP8 online validation for env.py files is kept as it is. It is related to long character...
![PEP8online validation](media/image/pep8-unsolved-bug.jpg)

 <a name="deployment"></a>

# 7. Deployment
  [Go to the top](#table-of-contents)

  The project was deployed to GitHub and pushed throughout the devlopment process. The project was also deployed to Heroku in the early stages of development to ensure that there weren't any issues later on in the project. Mannual deploy was selected within Heroku and has been deployed the latest versio/update in the project.

## 7.1 Method of Deployment
### 7.1.1 Installing Django and supporting libraries
- In gitpod terminal, install Django and supporting libraries and create requirement files
- Create a project "waterchanel" and app "blog" 
- Add installed app in the setting.py and migrate the chnages 
### 7.1.1 GitHub Repository
- Set up project GitHub repository and user stories correctly 
- Ensure all requirements for the project are added to the requirements.txt file prior to deployment. The command **pip3 freeze --local > requirements.txt** was used to run in the terminal to do this.
- All installed apps are added within setting.py under INSTALLED_APPS

### 7.1.2 Deploying to Heroku app
- Create new Heroku app 
    
- Added database 

Steps for this were;

i) Navigate to the resources tab for the app that has just been created.
ii) In the Add-Ons section, search for the Heroku Postgres add on and submit an order form. iii)Select the Settings tab for the app. iv)Reveal Config Vars and copy the DATABASE_URL string provided. v) Create a env.py file within the project and use the copied string to create a DATABASE_URL environment variable. The Python OS module will be required for this.

- Create a SECRET_KEY

  i) Create a SECRET_KEY environment variable Within the env.py file ii) Add the SECRET_KEY variable in the settings tab of the Heroku app, reveal config vars and add the along with the corresponding string.
  
- Update setting.py file 

Import dj_database_url and env.py into the settings.py file within the project as.
import dj_database_url
if os.path.isfile("env.py"):
    import env
- Update the default SECRET_KEY variable provided by Django to the SECRET_KEY environment variable.
 SECRET_KEY = os.environ.get('SECRET_KEY')

- Copy DATABASE_URL to Settings.py
- Copy SECRET_KEY to Settings.py
- Migrate Changes
- Connect app to Cloudinary
- Tell Django where the templates are stored
- Update ALLOWED_HOSTS
- Create a Procfile
- Connect the GitHub repository to the Heroku App

Note: I followed all the steps mentioned in the Django Blog Cheat Sheet provided by Code Institute.

<a name="seo"></a>
# 9. SEO
 [Go to the top](#table-of-contents)

To improve the search engine optimisation (SEO) of the site following actions were taken:
- Added keywords in a meta tag to my base.html. The keywords were researched using [WordTracker](https://www.wordtracker.com/), there are a number of short-tail and long-tail keywords.

- This is a list of all the keywords I came up with, desalianmtion, ultrafiltration, memebrane, water treatemnt, WASH, frontend developemnt, backend development.

<a name="marketing"></a>
# 10. Marketing
 [Go to the top](#table-of-contents)

 For my marketing strategies, I decided to go with content marketing, Social media and email marketing root. As these are free options and very effective for an E-commerce store.

- Content marketing - Posting content that contains blog posts and video tutorials will be my primary source to display content.

- Social media - Using these platforms will help build and interact with customers to build relationships and loyalty. This also helps build the brand. Followers will help share the business posts and in result gain more traction with other people. The same content can be across all social media platforms.

- Email marketing - Using email marking via a newsletter will be beneficial as it is a free source of marketing. Those who are subscribed are more likely to convert into paying customers. This will increase sales and returning customers as I can provide discount codes and other special offers. A good pro is that the business has total control over the design of the emails.


<a name="social-media"></a>
# 11. Social Media
 [Go to the top](#table-of-contents)
 A facebook business page was created and is planned to use this platform to promote the business.

![facebook_business_page](media/readme/media/facebook%20business%20page.jpg)


 <a name="acknowledgement"></a>

# 12. Acknowledgement
  [Go to the top](#table-of-contents)

* Inspired from Project Boutique Adoand from the code institute course
* Thanks to my mentor Marcel Mulders for his constructive feedback
* Thanks to the Code Institute tutor support team, who helped me develop my understanding throughout this project.
* Text in the blog post were taken from various sources in the internet