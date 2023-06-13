# Pollar.io

Pollario is a web application that allows users participate in daily polls. It provides an interactive and user-friendly interface for creating, answering, and viewing poll results.

## Features

- Answering Polls: Users have access to a poll question that changes every day and allows the user to vote on it.
- Real-time Results: Poll results are displayed in real-time, allowing users to see the current distribution of votes.
- Interactive US Map: The application includes an interactive US map that displays state-specific poll results when hovering over each state.
- Responsive Design: The application is designed to work seamlessly across different devices and screen sizes.

## Implementation

### Interactive US Map

Pollar.io incorporates an interactive US map to display state-specific poll results when hovering over each state. The map integration was implemented using SVG.js, a JavaScript library for manipulating and animating SVG.

The SVG map data is fetched from the server using an AJAX request and injected into the map container on the frontend. Event listeners are added to each state element, enabling the display of state-specific poll results when the user hovers over a state. The poll results are retrieved from the server via an AJAX request, and the data is dynamically rendered in a tooltip using HTML and CSS.

For the get_state.html, the SVG map is displayed the same way except the event listeners enable only the display of the state name when hovered upon. When the user then clicks on a state, the state name is passed to the server where it is added to the database along with the user id.

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


