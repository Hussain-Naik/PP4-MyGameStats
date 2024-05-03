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
| Create Group |     |      |     |    |
| 1                | Enter valid details in form | Field will only accept unique input | Y |  |
| 2                | Select private option | notification stating group will only be visible to invited users | Y |  |
| 3                | click cancel button | redirect to previous page | Y |  |
| 4                | click submit button | Creates group with selected parameters and redirect to group search | Y |  |



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

| Potential Client Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Potential client, I want to be contacted by sales managers, so that I can make a prudent decision about being a member. | Sales Manager will be able to get contact information from a potential client in new application page in order to contact new user | ![New Application. Data](documentation/features/application_detail_page/application_detail_data.png) |

| Bosses' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Boss, I want to be able to view new applications, so that I can control the flow of potential clients. | Available in new application page | ![New Applications. Data](documentation/features/new_applications_page/new_applications_data.png) |
| As a Boss, I want to be able to delete or approve membership, assign a role to a new member, so that I can keep data up to date. | Available in new application detail page | ![Assigning role to new application](documentation/features/application_detail_page/application_detail_role.png) |
| As a Boss, I want to be able to add, edit data on a kid, so that I can have a profile for each student. | Add student button is available on students page, students personal info is seen after clicking on a particular student. Edit button is located in student’s profile page. | ![Student Detail. Admin View](documentation/features/student_detail_page/student_detail_page_admin_view.png) |
| As a Boss, I want to be able to delete a member, so that I can control the access to the application. | Available in user’s profile only for bosses | ![Profile View. Deletion](documentation/features/profile_page/profile_page_other_user.png) |
| As a Boss I can see the info about kids provided by the company: name, contact info, classes visited, how many classes left, so that refresh the information about a client. | Available on students page, students personal info is seen after clicking on a particular student | ![Data about a student](documentation/features/student_detail_page/student_detail_page_admin_view.png) |
| As a Boss, I want to be able to search for a particular member, so that I can easily access information on this member. | Available in members page | ![Members search](documentation/features/members_page/members_page_search_input_results.png) |
| As a Boss, I want to be able to sort members according to a role, so that I can easily access particular group of members. | Available in members page | ![Members sorting bar](documentation/features/members_page/members_page_sorting_bar.png) |
| As a Boss, I want to be able to search for a particular student, so that I can easily access information on this student. | Available in students page | ![Students. Search input](documentation/features/students_page/students_page_search_input.png) |
| As a Boss, I want to be able to sort students by the urgent sale, so that I can control the sales in the company and preserve clients. | Available in students page | ![Students. Sort Bar](documentation/features/students_page/students_page_sort.png) |
| As a Boss, I want to be able to see lessons schedule, so that I can schedule time to talk to a teacher or a parent. | Available in schedule page | ![Schedule table](documentation/features/schedule_page/schedule_page_box.png) |
| As a Boss, I want to see see information on students for each lesson, so that I can control students’ attendance, learn clients preferences. | Available in schedule page, after clicking on a lesson | ![Lesson detail](documentation/features/lesson_detail_page/lesson_detail_personnel.png) |
| As a Boss, I want to be able to see sales' details, so that I can check which sales manager and which parent was involved in a deal. | Available in sales page | ![Menu](documentation/features/sales_page/sales_table_admin_view.png) |
| As a Boss, I want to be able to delete students from the application, so that I can control the flow of the present students. | Available on students page, student delete button is seen after clicking on a particular student. | ![Student deletion](documentation/features/student_detail_page/student_detail_page_data_box.png) |

| Teachers' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Teacher, I want to be able to search for a particular student, so that I can easily access information on this student. | Available in students page | ![Students. Search Input](documentation/features/students_page/students_page_search_input.png) |
| As a Teacher, I want to be able to see personal information on a kid, so that I can know student’s personal data. |  students personal info is seen after clicking on a particular student. | ![Student. Data](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Teacher, I want to be able to see lessons schedule, so that I can manage my time. | Available in schedule page | ![Schedule](documentation/features/teacher_schedule_page/schedule_look_compare2.png) |
| As a Teacher, I want to be able to see information on students for each lesson, so that I can be prepared for each student. | Available in schedule page, after clicking on a lesson | ![Lesson detail](documentation/features/lesson_detail_page/lesson_detail_personnel.png) |

| Receptionists' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Receptionist, I want to be able to search for a particular student, so that I can easily access information on this student. | Available in students page | ![Student. Search input](documentation/features/students_page/students_page_search_input.png) |
| As a Receptionist, I want to be able to see personal information on a kid, so that I can know student’s personal data. |  students personal info is seen after clicking on a particular student. | ![Menu](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Receptionist, I want to be able to see lessons schedule and student attending lessons, so that I can arrange the flow of the students. | Available in schedule page | ![Schedule](documentation/features/schedule_page/schedule_page_box.png) |
| As a Receptionist, I want to be able to create lessons for a day (day, time, subject, teachers, students), so that I can provide a precise schedule for school members. | Add lesson button is available in schedule page | ![Add lesson button](documentation/features/schedule_page/add_lesson_button.png) |
| As a Receptionist, I want to be able to render lessons for a day (day, time, subject, teachers, students), so that I can provide up to date schedule. | Edit and delete lesson buttons are available after clicking on a lesson in schedule page | ![Lesson Detail. Editing and Deletion](documentation/features/lesson_detail_page/lesson_detail_receptionist.png) |

| Sales Managers' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Sales Manager, I want to be able to search for a particular student, so that I can easily access information on this student. | Available in students page | ![Student. Search Input](documentation/features/students_page/students_page_search_input.png) |
| As a Sales Manager, I want to be able to see personal information on a kid, so that I can know student’s personal data. |  students personal info is seen after clicking on a particular student. | ![Menu](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Sales Manager, I want to be able to sort students by the urgent sale, so that I can control the sales in the company and preserve clients. | Available in students page | ![Student. Search Input](documentation/features/students_page/students_page_sort.png) |
| As a Sales Manager, I want to be able to view new applications, so that I can contact a potential client and make profits for a company. | Available in the new applications page | ![New Application Data](documentation/features/new_applications_page/new_applications_data.png) |
| As a Sales Manager, I want to be able to add personal notes on each student that I’m in charge of, so that I can increase the company’s sales. | Available in the students page | ![Add student Page](documentation/features/add_student_page/add_student_page.png) |
| As a Sales Manager, I want to be able to add or edit information on students, so that I can keep up to date students’ profiles. | Available in the students page | ![Student Detail. Data](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Sales Manager, I want to be able to review my sales, so that I can control my performance. | Available in the sales manager personal profile | ![Sales for sales manager in Profile](documentation/features/profile_page/profile_page_sales_sales.png) |
| As a Sales Manager, I want to be able to add new classes to a child when parents buy classes, so that I can maintain relationships with clients. | Available in the sales page | ![Add sale button](documentation/features/sales_page/sales_page_add_sale_button.png) |
| As a Sales Manager, I want to be able to delete students from the application, so that I can control the flow of the present students. | Available on students page, student delete button is seen after clicking on a particular student. | ![Student Detail. Data](documentation/features/student_detail_page/student_detail_page_data_box.png) |
| As a Sales Manager I can edit information on about a sale so that change the data on a sale if a mistake was made or a parent changed his or her mind. | Available on sales page | ![Sales deletion and edition](documentation/features/sales_page/sales_page_edit_delete_limitations.png) |
| As a Sales Manager I can delete information on about a sale so that render sales data if a mistake was made or a parent changed his or her mind. | Available on sales page | ![Delete sale page](documentation/features/delete_sale_page/delete_sale_page.png) |

| Parents' Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Parent, I want to be able to see personal information on my child/children, so that I can check the personal data. | Available in student detail page | ![Student Detail. Other members view](documentation/features/student_detail_page/student_detail_page_others_view.png) |
| As a Parent, I want to be able to see my child’s attendance (subject, teacher, date), so that I can control my child’s education and my spending. | Available in student detail page | ![Menu](documentation/features/student_detail_page/student_detail_attendance.png) |
| As a Parent, I want to be able to see lessons schedule, so that I can manage my time and control child’s attendance. | Available in schedule page | ![Schedule](documentation/features/schedule_page/schedule_page_box.png) |
| As a Parent, I want to be able to see information on students for each lesson, so that I can prepare my child for a lesson. | Available in schedule page, after clicking on a lesson | ![Lesson detail for parents](documentation/features/lesson_detail_page/lesson_detail_parent.png) |
| As a Parent, I want to be able to see names of teachers for each lesson, so that I can know who is/are teaching a lesson. | Available in schedule page, after clicking on a lesson | ![Lesson Detail Parent](documentation/features/lesson_detail_page/lesson_detail_parent.png) |




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

- Not applicable, as all application CSS using Bootstrap 5 library

### JS Validation:

- Not applicable, as all application JavaScript using Bootstrap 5 library

### Python Validation:

- [Full Python Validation Report](documentation/validation/python_validation.pdf)

- No errors were found when the code was passed through [CI Python Linter](https://pep8ci.herokuapp.com/#). According to the reports, the code is [Pep 8-compliant](https://legacy.python.org/dev/peps/pep-0008/). This checking was done manually by copying python code and pasting it into the validator.

---
## Lighthouse Report

- [Full Lighthouse Report](documentation/validation/lighthouse_report.pdf)


---

## Compatibility

Testing was conducted on the following browsers;

- Brave;
- Chrome;
- Firefox;

[Compatibility Report](documentation/compatibility/compatibility.pdf)


---

# Responsiveness

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.

[Responsiveness Report](documentation/responsiveness/responsiveness.pdf)



---