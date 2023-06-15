# Pollar.io

Pollario is a web application that allows users participate in daily polls. It provides an interactive and user-friendly interface for creating, answering, and viewing poll results.

## Features

- Answering Polls: Users have access to a poll question that changes every day and allows the user to vote on it.
- Real-time Results: Poll results are displayed in real-time, allowing users to see the current distribution of votes.
- Interactive US Map: The application includes an interactive US map that displays state-specific poll results when hovering over each state.
- Responsive Design: The application is designed to work seamlessly across different devices and screen sizes.

## Implementation

### Set Up

 - We utilized the starter code for py4web, specifically the version that already had Vue.js integrated. Our project consists of a server-side implemented in Python and a client-side developed using JavaScript. The HTML pages are responsible for rendering the content to the users.

### Databases

 - We employed four databases, each uniquely connected to others through a specific field. The first database is the user table, which stores essential user information such as their first name, last name, email, and password. This table is utilized for user authentication, making it mandatory for accessing our website.

 - The second database is the question and answer database. It is designed to store the questions along with their corresponding answers. This table comprises five fields, with four fields dedicated to storing the possible answers for each question. To simplify the process of identifying the user-selected answer, we arranged the answer fields before the question field. Consequently, answer1 is positioned at index 1, answer2 at index 2, and so forth, while answer4 is located at index 4 of the table. This arrangement facilitates the retrieval of the chosen answer and enables its storage in other databases.

 - The third database is the results database. It includes four fields: a reference to the question database, allowing us to determine which question the user responded to; the user's ID, aiding in identifying the user who answered the question; the answer ID, which corresponds to the position number of the selected answer in the question and answer database; and the user's residing state. The latter field is particularly useful for tailoring specific information to each user. 

 - Additionally, we use the userStates database, consisting of two fields: the user ID and the state name. This database serves to store user-related information for easy retrieval and transmission to the results database. Furthermore, it ensures that every user is assigned a state, as access to the remainder of the website is restricted until a user selects a state. 

 ### Structure

 - Our website begins with a user login page, where users must create an account before progressing to the subsequent pages. If a user has not yet selected their residing state, they will be redirected to an individual page, accompanied by its dedicated JavaScript file responsible for handling event listeners and client-side code. Afterward, the user is directed to the main page, where a question is presented, and they can select an answer. This page has its separate JavaScript file. By employing two distinct JavaScript files, we maintain clean code separation, avoiding interdependencies between the two functionalities. Similarly, adhering to the principle of separation of concerns, we utilize separate databases to store different types of information rather than relying on a single database for all data.

 - Lastly, upon answering a question, the user is directed to a server-generated page that displays information specifically relevant to the user's residing state. This personalized approach enhances the user experience. From this page, users have the option to navigate back to the main page to answer additional questions and view statistical information pertaining to the rest of the United States. To prevent misuse and manipulation of voting, we delete the user-selected answer, ensuring that users cannot spam responses.

### Functionality

 - Interactive US Map

    Pollar.io incorporates an interactive US map to display state-specific poll results when hovering over each state. The map integration was implemented using SVG.js, a JavaScript library for manipulating and animating SVG.

    The SVG map data is fetched from the server using an AJAX request and injected into the map container on the frontend. Event listeners are added to each state element, enabling the display of state-specific poll results when the user hovers over a state. The poll results are retrieved from the server via an AJAX request, and the data is dynamically rendered in a tooltip using HTML and CSS.

    For the get_state.html, the SVG map is displayed the same way except the event listeners enable only the display of the state name when hovered upon. When the user then clicks on a state, the state name is passed to the server where it is added to the database along with the user id.

 - Next Button For Questions

    For testing purposes, we included a button labeled “Next question” that allows us to cycle through the questions in the database beginning with the first one. Each time the button is pressed, the next question will be grabbed from the QA (Question and answer) database and a new set of arbitrary users and answers will be created to simulate a live user base.

 - Testing Users

    To facilitate testing, we implemented a function that generates arbitrary users and their corresponding answers for the current question. The number of testing users created can be adjusted through a variable within our code, allowing us to have any desired number of testing users and answers.

 - JavaScript

    Our JavaScript code comprises several actions, all of which are routed through the controller. The controller, in turn, interacts with the databases, retrieving the necessary information and returning it as a dictionary for easier accessibility.

- Server Generated Page

    As per the project requirements, we have a single server-generated page. Unlike the other pages that rely on JavaScript, this page does not interact with JavaScript functionalities. Instead, it sends the required databases to a separate HTML page. This communication is achieved through href calls, where we pass multiple variables to ensure that the necessary information is accessible on the page.
    


## Technologies Used

- Frontend: HTML, CSS, JavaScript, Vue.js
- Backend: Python, Flask
- Database: SQLite
- AJAX Requests: Axios
- Map Integration: SVG.js
- Styling: Bulma CSS framework

## Installation

1. Clone the repository:

https://github.com/RowdyRiley/pollar.io.git

2. Navigate to the py4web directory: 

cd py4web

3. Start the application:

./py4web.py run apps

## Usage

- Create an account or log in to an existing account.
- Select the state they currently reside in.
- See the poll of the day.
- Select an answer choice for the poll or scroll down to hover over the US map to see state-specific results.
- Once a answer is selected, user is taken to the next page and can see the statistics of the state they live in.

## Contributors

Beixi Zhang, Riley Kuo, Shafiq Nomair, John Chen


