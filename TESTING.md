# Testing

## Manual Testing

Testing was done throughout site development, for each feature before it was merged into the master file.

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different devices and browsers to ensure issues were caught and where possible fixed during development.


|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Log In      |                        |                  |      |             |
| 1           | Click on Login button | Redirection to Login page | Y |          |
| 2           | Click on the SignUp link in the form | Redirection to SignUp page | Y |          |
| 3           | Enter valid email or username | Field will only accept email address format | Y |          |
| 4           | Enter valid password | Field will only accept secure passwords | Y |          |
| 5           | Click on the Login button | Takes user to profile page with pop-up confirming successful sign in. User navigation displayed | Y |          |
| 6           | Click "Logout" button | Redirects user to home page with pop-up confirming successful sign out| Y |          |
| Sign Up     |                        |                  |      |             |
| 1           | Click on the Sign Up button | Redirects to Sign up page | Y |          |
| 2           | Click on the Login link in the form | Redirection to Login page | Y |          |
| 3           | Enter valid email | Field will only accept email address format | Y |          |
| 4           | Enter valid username | Field will only accept non existing usernames | Y |          |
| 5           | Enter valid password | Field will only accept secure passwords | Y |          |
| 6           | Enter valid password confirmation | Field will only accept the same password from the previous field | Y |          |
| 7           | Click on the Submit button | creates user and takes user to profile page with pop-up confirming successful sign in | Y |          |
| 8           | Click "Logout" button | Redirects user to home page with pop-up confirming successful sign out| Y |          |
| User Nav    |                        |                  |      |             |
| 1           | Click on the "Group search" button | redirects to group list page | Y | Only displays participating groups or non private groups |
| 2           | Click on "Profile" | Redirection to My Profile page | Y |    |
| 3           | Click on "Group Detail" | Redirection to group search page if not viewing group associated views | Y |  |
| 4           | Click on "Session Detail" | Redirection to group search page if not viewing session associated views | Y |  |
| 5           | Click on "Session Invite" | Redirection to users session invite page | Y |  |
| 6           | Click on "Friend Search" | Redirection to friend search page | Y |   |
| 7           | Click on "Pending Invites" | Redirection to pending friend request page | Y |  |
| 8           | Click on "Logout" button in the center of the page | Takes user to log out page to confirm logout | Y |  |
| Profile     |            |                  |      |             |
| 1           |  Click "three vertical dots" button | cycles user stats | Y |   |
| 2           |  Click "edit" button | Redirect to edit profile page | Y |  Available only when the user opens his/her own profile  |
| 3           |  Click "friend avatar" in friend section | redirects to users profile | Y |   |
| 4           |  Click "invite" link in session invite section | redirects to session invites page | Y |  |
| 5           |  Click "user name" link in the pending section | redirects to pending friend request page | Y | Sent and received invites are different color |
| 6           |  Click '+' avatar in friends section  | display modal with all friends | Y | displayed when more than 7 friends |
| Edit Profile |            |                  |      |             |
| 1           |  Change the form data for the first name, last name | Date in the form will be updated | Y | Available only when the user opens his/her own profile  |
| 2           |  Click "cancel" button | Redirect back to user profile | Y |  Available only when the user opens his/her own profile |
| 3           |  Click "save" button | Redirect back to user profile+data will be updated in the database | Y |  Available only when the user opens his/her own profile |
| Group Search |     |      |     |    |
| 1                | click on 'Create Group' button | Redirect to the create group page | Y |  |
| 2                | pagination "next" | Redirect to the next page of groups | Y | Available when groups more than 12 |
| 3                | pagination "previous" | Redirect to the previous page of groups | Y | Available when groups more than 12 |
| 4                | Form Search | filters group list to match groups containing form input | Y |  |
| 5                | click group link | redirects to group detail page | Y |  |
| Group Detail |     |      |     |    |
| 1                | click button to create session | redirects to create session page | Y |  |
| 2                | click button to delete group | redirects to delete group page | Y |  |
| 3                | click button to edit group | redirect edit group page | Y |  |
| 4                | click button to edit group host | redirects to update group host page | Y |  |
| 5                | click session link | redirect session detail page | Y |  |
| 6                | click session users avatar | redirects to users profile | Y |  |
| Create Group |     |      |     |    |
| 1                | Enter valid details in form | Field will only accept unique input | Y |  |
| 2                | Select private option | notification stating group will only be visible to invited users | Y |  |
| 3                | click cancel button | redirect to previous page | Y |  |
| 4                | click submit button | Creates group with selected parameters and redirect to group search | Y |  |
| Group Delete |     |      |     |    |
| 1                | click cancel button | redirects to group detail page | Y |  |
| 2                | click submit button | Deleted from database and redirects to group list page | Y |  |
| Group Host Update |     |      |     |    |
| 1                | click cancel button | redirects to group detail page | Y |  |
| 2                | click submit button | updates host and redirects to group detail | Y |  |
| 3                | form select field | list of users participating in group as option | Y | required field can not be left blank  |
| Group Update |     |      |     |    |
| 1                | click cancel button | redirects to group detail page | Y |  |
| 2                | click submit button | updates table and redirects to group detail | Y |  |
| 3                | Enter valid name | name field required to be unique | Y |  |
| 4                | Private uncheck slider | Remove private info when unselected | Y |  |
| 5                | Private check slider | Displays private info when unselected | Y |  |
| Session Detail |     |      |     |    |
| 1                | click new game button | modal opens to create new game | Y | only displayed when minimum players are met |
| 2                | click invite button | redirects to send invite page | Y | changed to new game button when minimum players met |
| 3                | click edit session button | redirect edit session page | Y |  |
| 4                | click edit session admin button | redirects to update session admin page | Y |  |
| 5                | click invite players button | redirect session invite page | Y |  |
| 6                | click delete session button | redirects delete session page | Y |  |
| 7                | click game link | redirects to update game score | Y |  |
| Session Delete |     |      |     |    |
| 1                | click cancel button | redirects to session detail page | Y |  |
| 2                | click submit button | Deleted from database and redirects to group detail page | Y |  |
| Session admin Update |     |      |     |    |
| 1                | click cancel button | redirects to session detail page | Y |  |
| 2                | click submit button | updates host and redirects to session detail | Y |  |
| 3                | form select field | list of users participating in session as options | Y | required field can not be left blank  |
| Session Update |     |      |     |    |
| 1                | click cancel button | redirects to session detail page | Y |  |
| 2                | click submit button | updates table and redirects to session detail | Y |  |
| 3                | Enter valid location | required field is not unique | Y |  |
| 4                | Enter valid Time | required field is not unique | Y |  |
| 5                | Select Game type option | only doubles option available | Y |  |
| 6                | Select Team type option | only random option available | Y |  |
| Session Invite |     |      |     |    |
| 1                | click Send invite button | redirects to send session invite page | Y |  |
| 2                | click remove player button | redirects to remove player page | Y | the x after the player name in current roster |
| 3                | click delete invite button | redirects to delete session invite page | Y | the x after the session invite element |
| 4                | click approve invite button | redirects to update session invite page | Y | the tick after the session invite element |
| Session Join Request |     |      |     |    |
| 1                | click cancel button | redirects to session detail page | Y |  |
| 2                | click submit button | Sends join request for session admin to review and redirects to session details page | Y |  |
| Send Session Invite |     |      |     |    |
| 1                | click cancel button | redirects to session invite page | Y |  |
| 2                | click submit button | Sends invite to user selected | Y |  |
| 3                | Select user option | required fields | Y | will only provide option for users that are not already invited and are participating in group or admins friend |
| Remove Player |     |      |     |    |
| 1                | click cancel button | redirects to session invite page | Y |  |
| 2                | click submit button | removed player from roster and redirects to session invite page | Y |  |
| Delete session invite |     |      |     |    |
| 1                | click cancel button | redirects to session invite page | Y |  |
| 2                | click submit button | removed invite and redirects to session invite page | Y |  |
| Approve session invite |     |      |     |    |
| 1                | click cancel button | redirects to session invite page | Y |  |
| 2                | click submit button | Adds player to roster and redirects to session invite page | Y |  |
| 3                | Select field option | required field | Y |  |
| Game Detail |     |      |     |    |
| 1                | enter team 1 score | can be left blank or 0 | Y |  |
| 2                | enter team 2 score | can be left blank or 0 | Y |  |
| 3                | click submit button | save the score for each team redirects to session detail page | Y | winner is displayed on session detail page |
| User Session invites list |     |      |     |    |
| 1                | click invite link | redirects to update user session invite | Y |  |
| Update User Session invites |     |      |     |    |
| 1                | click cancel button | redirects to user session invite list page | Y |  |
| 2                | click submit button | Adds player to roster and redirects to profile page | Y |  |
| 3                | Select approved field option | need to manually select | Y |  |
| User Profiles list |     |      |     |    |
| 1                | click user profile | redirects to users profile | Y |  |
| Other User Profile |     |      |     |    |
| 1                | click button to add friend | refreshes user profile | Y | add friend button changed to friend request status |
| 2                | click status button | redirects to update friend request page | Y |  |
| 3                | click remove friend button | redirects to unfriend page  | Y | Displayed once user accepts friend request |
| Unfriend |     |      |     |    |
| 1                | click cancel button | redirects to users profile page | Y |  |
| 2                | click submit button | unfriends both users and redirect to user profile page | Y |  |
| Update Sent Friend request |     |      |     |    |
| 1                | click cancel button | redirects to user profile page | Y |  |
| 2                | click submit button | updates database and adds each user to respective friend list | Y | redirect back to user profile |
| 3                | click delete button | delete friend request from database | Y | request no longer visible on recipient profile |
| Update Received Friend request |     |      |     |    |
| 1                | click cancel button | redirects to user profile page | Y |  |
| 2                | click submit button | updates database and adds each user to respective friend list | Y | redirect back to user profile |
| 3                | Select accept option | Adds both users to each others respective friends list | Y |  |
| Pagination |     |      |     |    |
| 1                | click next button | redirects to next page in view | Y |  |
| 2                | click next page number | redirects to next page in view | Y |  |
| 3                | click previous button | redirects to previous page in view | Y |  |
| 4                | click previous page number | redirects to previous page in view | Y |  |
| List View Search |     |      |     |    |
| 1                | enter parameter to search | Displayed list reduced to match search parameter | Y |  |

---

## Testing User Story

| First Time Visitor Goals | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a First Time Visitor, I want to be able to easily understand the main purpose of the app, so that I can learn more about this app. | Welcome text on the top of the homepage explaining the main purpose of the website and describing the the services offered | ![Home page](documentation/features/home_page/home_page.png) |
| As a First Time Visitor, I want to be able to easily navigate through the app, so that I can find the content. | The website for the fist time visitors made out of one page. The user can read all benefits of the school and learn briefly about its services. The page has also several buttons, which lead to the registration page. At the end of the page, the user may find additional contact information and location of the school. | ![Menu](documentation/features/navbar/menu_admin_view.png) |
| As a First Time Visitor, I want to be able to register my account, so that I can learn the benefits of the app as a user. | Top navigation GET STARTED button + GET STARTED button in the hero section | ![Navbar Logout](documentation/features/navbar/navbar_logout.png) |
| As a First Time Visitor, I want to be able to find the app useful, so that I can use it according to my needs. | The website cover benefits of becoming a member and engages new visitors to become a member of a school | go to features section in the [README.md](README.md) |


| Frequent Visitor Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Frequent User, I want to be able to log in to my account, so that I can have a personal account. | Log in from the top right navigation | ![Get Started Button](documentation/features/navbar/get_started_button.png) |
| As a Frequent User, I want to be able to easily log in and log out, so that I can access my personal account information. | Logout button in the main menu in the top of navbar | ![Navbar limited access](documentation/features/navbar/navbar_limited_access.png) |
| As a Frequent User, I want to be able to easily recover my password in case I forget it, so that I can recover access to my account. | Available on login page | ![Login](documentation/features/login_page/login_page.png) |
| As a Frequent User, I can be able to change my password, so that I can be sure that nobody else can access my account. | Available in user’s profile | ![Profile. Admin view](documentation/features/profile_page/profile_page_admin_box.png) |





---


## Bugs

### Known bugs

Due to the user navbar including a session detail and group detail button the code app would display error when viewing different pages which did not contain the relevant model objects. All page view included a session object with the context name of 'object_detail' to match and a method called get_group_id on the session and group model to fix the error

Due to the removal of singles badminton the game creation button on the session detail page would be removed. Upon investigating and testing the application the condition for the button display was calculated based on the session status integer multiplied by 4, which once a session was in session would require 8 players in session to display button. This was fixed by adding the correct variable 'game_type' to multiplied by 4.

### Solved bugs

There were plenty of bugs during the development process since this project was a learning platform for me and allowed me to improve my skills and knowledge significantly.

One of the bugs was due to a zero division as the win percentage to be calculated would cause an error for new users when viewing their profile page which did not contain any statistics

Due to changes to fontawesome mid way the project the application stopped displaying the icons or the fontawesome icon resizing which was used. Viewing the application with chrome dev tools it identified the broken link and i changed the fontawesome icons to bootstrap 5 native icons.


---

## Validation:
### HTML Validation:

- [Full HTML Validation Report](documentation/validation/html_validation.pdf)

- No errors or warnings were found when passing through the official [W3C](https://validator.w3.org/) validator. This checking was done manually by copying the view page source code (Ctrl+U) and pasting it into the validator.

### CSS Validation:

- All application CSS using Bootstrap 5 library, no other external CSS used

### JS Validation:

- All application JavaScript using Bootstrap 5 library, no other Javascript code used

### Python Validation:

- [Full Python Validation Report](documentation/validation/python_validation.pdf)

- No errors were found when the code was passed through [CI Python Linter](https://pep8ci.herokuapp.com/#). According to the reports, the code is [Pep 8-compliant](https://legacy.python.org/dev/peps/pep-0008/). This checking was done manually by copying python code and pasting it into the validator.

---
## Lighthouse Report

- [Full Lighthouse Report](documentation/validation/lighthouse_report.pdf)


---

## Compatibility

Testing was conducted on the following browsers;

- Safari;
- Chrome;
- Firefox;

- [Compatibility Report](documentation/responsive_report.pdf)

---

# Responsiveness

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.

Bootstrap 5 library used to handle responsive mobile first approach.

- [Responsive Report](documentation/responsive_report.pdf)
---