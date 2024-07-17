# Budget Buddy
#### Video Demo: https://youtu.be/WJ7iS2375WU
#### Description:
With Budget Buddy you are able to plan projects more efficiently and plan within Budget. Budget Buddy is very userfriendly and easy to control. Create categories set maximum Budgets for those categories and allocate items to those categories.

![Start Page of Budget Buddy](https://i.ibb.co/0KJkbSs/main.png)

# How the System works
In Budget Buddy everything is connected to a big database, so that data is stored serverside and security is granted.

# Registering and Login
![Login Page](https://i.ibb.co/cbS7cph/Login.png)
![Register Page](https://i.ibb.co/wgQtL9j/register.png)

When a user logs in the database is going to get queried for the username and the input password is going to get hashed and compared to the hashed password in the database. This ensures, that database breaches do not show the password in plaintext.

When a user registrates he will be prompted for a budget aside from username password and confirmation of password. The budget sets the overall limit for the project. The budget can be changed once logged in.

# Items Page
![Items](https://i.ibb.co/ZhsLm7q/items.png)

On the item page you have an overview of all items in the database that are bound to your account. You can delete items if wanted and insert new items.
When inserting new items the name price and category are mandatory inputs. If wanted a link to a photo can be added.
The categories you can choose from are the categories you have created in the categories tab.

# Categories Page
![Categories](https://i.ibb.co/cTpQgmZ/categories.png)

On the Categories Page all custom categories are listed. Should the sum of the budgets of those categories exceed the overall budget a red warning will be displayed.
The user is also able to add new categories by inserting a name and a budget. All categories can be changed and renamed and will be stored in the database. If a category is being deleted, all corresponding items will be deleted as well.
After a category has been renamed, the new name will also be updated in the 'items' table within the database.

# Main Page
![Overview](https://i.ibb.co/7JpdDQf/over.png)

On the main page all categories and their corresponding items are listed. If a budget is exceeded it is going to be visible. At the bottom of the Page a small Conclusion sector is visible. In the conclusion the given and used budget are compared and the results are shown. This page should help to give an overview about the projects costs.

# Budget Page
![Budget](https://i.ibb.co/fQP2DsX/budget.png)

This page allows the user to change the project budget

# Database
The database follows this schema:

users

    'user_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'username' TEXT NOT NULL UNIQUE, 'password' NUMERIC NOT NULL,
    'budget' INTEGER NOT NULL


categories

    'category_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 'name' TEXT NOT NULL,
    'budget' INTEGER NOT NULL

items

    'item_id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    'user_id' INTEGER NOT NULL, 'image' TEXT,
    'name' TEXT NOT NULL,
    'price' INTEGER NOT NULL, 'category' TEXT NOT NULL

# Requirements
The app uses the following librarys:

    flask
    functools
    cs50
    flask_session
    werkzeug.security

# Security

As already mentioned earlier the passwords int the database are stored as hash values. Besides that, all users are required to log in in order to make changes to their project. this ensures that users are only able to change properties when they are logged in. Because of the used Cookies every user has a unique id that he himself cannot access. All operations only happen in the scope of this id. As a result it is not possible for a logged in user to make changes to another user's project.

The Insertion and changes on the database happens on industry level security. SQL-Injections are prevented by the systems known so far.

# Webpage Generation

The webpage is being dynamically generated. This happens on the basis of a template and Jinja functionalities. As a result, the webpage is very interactive and all projects can be scaled almost infinitely. There is no limit to the amount of items or the amount of categories.

# Notes

the flask_session folder can be deleted without issues as it will be regenerated upon use.

# Error Handling
![Error](https://i.ibb.co/tJFX58J/error.png)

Should an error occur an Error page will be rendered that explains what happened wrong. This page is being used if the error is client-side.
