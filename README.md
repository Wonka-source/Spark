# Spark

[Spark live link](https://spark-project.herokuapp.com/)

Responsive:
![Am i responsive image](/static/images/readme_images/other_readme_images/responsive.jpg)


### Theme, Epic and User Stories

#### Theme
Spark is an Irish based platform for both event promoters to showcase their local events and for potential attendees to view the local upcoming events.

#### Epic
The site allows promoters to sign up for an account and the ability to create, review, edit and delete events they want to promote. The promoter has the ability to make drafts of events before posting to the main page. The site also allows potential attendees to view the upcoming events on the main page.

#### User stories

 - As a promoter I can securely sign up for an account so that I can create events
 - As a promoter I can create a draft event so that I can customize it before posting it to the main page
 - As a promoter I can edit my created events so that I can make changes as needed
 - As a promoter I can delete my created events so that I can delete them as needed
 - As a promoter I can post the individual events that I have created to the main page so that it is visible to potential attendees
 - As a promoter, I can toggle my events post status so that I can remove the event from the main page
 - As a promoter/viewer I can  navigate the website easily and intuitively.
 - As a viewer I can view the main page so that  I can browse all of the posted events
 - As a viewer, I can click on individual events listed on the main page so that I can view all of the posted events details
 - As a viewer I can view the posted events in the order of date happening so that so I can view the events listed starting from the most current






### Design and UX

I chose an RGB color scheme for the logo and a main color palette of white and off-white with a dark grey footer. My aim was to create a minimalist look for the site. The RGB logo adds a bit of color and the white and off white are easy on the eyes this also leaves room for the user to add custom images without any clashing color schemes. Links and navigation have a have a blue hover color.

### Wireframes

![Spark wireframes](/static/images/readme_images/other_readme_images/wireframes.jpg)

### Database model

![Database model](/static/images/readme_images/other_readme_images/data_model.jpg)


### Features
 - Navbar
 - Logo
 - Log in 
 - Log out
 - Profile
 - Sign up
 - About
 - Footer
 - Home page
 - Create an event page
 - Edit event page 
 - Delete event page
 - View event page 

Logo:
 
 ![Logo](/static/images/readme_images/features/logo.jpg)

Navbar: 

![Navbar](/static/images/readme_images/features/nav_bar.jpg)

Navbar logged in:

![Navbar logged in](/static/images/readme_images/features/navbar_loged_in.jpg)

Footer:

![Footer](/static/images/readme_images/features/footer.jpg)

Footer logged in:

![Footer logged in](/static/images/readme_images/features/footer_loged_in.jpg)

Home page:

![Home page](/static/images/readme_images/features/home_page.jpg)

Home page navigation:

![Home page nav](/static/images/readme_images/features/home_page_ev_nav_next.jpg)

![Home page nav](/static/images/readme_images/features/home_page_ev_nav_prev.jpg)

Profile page:

![Profile page:](/static/images/readme_images/features/profile_page.jpg)

Create Event:

![Create Event:](/static/images/readme_images/features/create_event.jpg)

Create Event Message:

![Create Event Message](/static/images/readme_images/features/create_event_message.jpg)

Form Error Message:

![Form Error Message](/static/images/readme_images/features/please_try_again.jpg)

Edit Event:

![Edit Event](/static/images/readme_images/features/edit_event.jpg)

Edit Event Message:

![Edit Event Message](/static/images/readme_images/features/edit_event_message.jpg)

Delete Event:

![Delete Event](/static/images/readme_images/features/delete_event.jpg)

Delete event Message:

![Delete event Message](/static/images/readme_images/features/delete_event_message.jpg)

Event Detail:

![Event Detail](/static/images/readme_images/features/event_detail.jpg)

Status draft or post to All Sparks:

![Status draft or post to All Sparks:](/static/images/readme_images/features/post_draft_status.jpg)

About:

![About](/static/images/readme_images/features/about_spark.jpg)

Sign up:

![Sign up](/static/images/readme_images/features/sign_up.jpg)

Sign in:

![Sign in](/static/images/readme_images/features/sign_in.jpg)

Sign in message:

![Sign in message](/static/images/readme_images/features/sign_in_message.jpg)



### Technologies

Python 3

HTML5

CSS

Javascript

Django

Django/allauth

Bootstrap

Cloudinary 

GitHub

Heroku 

Gitpod


### Testing
All python files were validated using [Code Institutes Pep8 validator](https://pep8ci.herokuapp.com) and passed with no errors.

HTML validator https://validator.w3.org/:

![HTML validator results](/static/images/readme_images/testing_screenshots/html.jpg)

CSS validator https://jigsaw.w3.org/css-validator/:

![CSS validator results](/static/images/readme_images/testing_screenshots/css.jpg)

Lighthouse test https://web.dev/measure/:

![Lighthouse test results desktop](/static/images/readme_images/testing_screenshots/desktop_lighthouse.jpg)

![Lighthouse test results desktop](/static/images/readme_images/testing_screenshots/mobile_lighthouse.jpg)

### Browser Compatibility
- **Firefox** - No issues
- **Chrome** - No issues
- **Opera** - No issues
- **Microsoft Edge** - No issues
- **Brave** - No issues
- **Waterfox** - No issues

### ### Manual Testing

![Manual testing table](/static/images/readme_images/testing_screenshots/manual_testing.jpg)

### Deployment

 - Create Heroku account  
 - Click "New" button on the top right of the dashboard
 - Choose a region and a name for the project, then click "Create app"
 - Create an ElephantSQL account and Log in
 - Click “Create New Instance”
 - Set up your plan
 - Give your plan a Name (this is commonly the name of the project)
 - Select the Tiny Turtle (Free) plan
 - Select “Select Region”
 - Select a data center near you
 - Then click “Review”
 - Check your details are correct and then click “Create instance”
 - Return to the ElephantSQL dashboard and click on the database instance name for this project
 - In the URL section, click the copy icon to copy the database URL
 - In your project workspace, create a file called env.py. It’s a good idea to check that this file is included in the .gitignore file too.
 - Add your database url and your secret key
 - save the file
 - Now import env.py to settings.py
 - Run the command "python manage.py migrate"
 - Add, commit and push your project to GitHub 
 - Go back to the Heroku dashboard open the Settings tab
 - Reveal the config vars and add Cloudinary and Postgres config vars and the secret key
 - Navigate to the "Deploy" tab and choose Github as deployment option
 - Connect Heroku to your Github repo you can choose automatic or manual deployment, I used automatic.
 - Then push your code to update the app.


### Credits
 - Thank you to Bran, my mentor, for the help during the project.

### Acknowledgements
- The home page was inspired by the Django blog walkthrough from the Code Institute.