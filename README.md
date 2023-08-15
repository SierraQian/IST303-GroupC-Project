# Instructions to run the App:

1. First, start with creating the project directory: mkdir <App_Name>
2. Next, navigate to the project directory: cd <App_Name>
3. Pull request from git@github.com:SierraQian/IST303-GroupC-Project.git via SSH to get latest version or https://github.com/SierraQian/IST303-GroupC-Project.git via HTTPS
4. OPTIONAL: Create a Python environment if you don’t have one: `python3 -m venv venv`
5. OPTIONAL: Next, run the following command: source venv/bin/activate This command will activate the virtual environment.
6. Run the following command from the project directory to install the needed packages: pip3 install -r requirements.txt
7. In a terminal, you can set the FLASK_APP and FLASK_DEBUG values as follows: `export FLASK_APP=project && export FLASK_DEBUG=1` (**_ If you encounter an error with the following command, type first: `export PATH="/venv/bin:$PATH"` _**)
8. Run in a terminal: flask run
9. You should be able to type in a Internet browser of your choice the following to see the web application: http://localhost:5000 or alternatively http://127.0.0.1:5000
10. Run the unittest to see whether the script is bug-free by typing python3 test.py in your terminal.

# IST303-GroupC-Project

# Team members:

Xu Chen, Shengjie Qian, Josue Carames, Nicholas Colletta, Norah Aldaghmi

# PART A

# App Title: Economic Calendar

# Concept:

A website that shows an economic calendar that updates on a weekly basis. In the background, it would take the most popular time series indicators from the website FRED and show various features of the most popular indicators. Some of the various factors it would list:

1. Day of the week an indicator is going to be published
2. Frequency of the indicator in question (Daily, Weekly, Monthly, Quarterly, Annual)
3. Expected Value (if we can gather that data since that data is not from FRED)
4. Previous Value
5. Change in Value from previous publish
6. Category the series resides in

# Project Requirements (expressed as user stories, have the estimated time):

1. As an admin user, I want to have an account to login to the admin system. (frontend: 1 week, backend: 1 week)
2. As an admin user, I want to choose the indicators show on the page and the method of calculate the expected value. (frontend: 1 week, backend 1 week)
3. As a trader, I want to have an account to login, and could edit my username and password.
4. As a trader, I want to manipulate and save my own dashboard to see the indicators I am interested in.
5. As a trader, I want to view a list of upcoming economic releases and their expected impact on the market, so I can plan my trading strategies accordingly.
6. As a trader without an account, I want to view the default indicators and upcoming releases.

# Stakeholders:

1. Senior Management
2. Operations Team
3. Traders and Analysts
4. Compliance and Risk Management
5. IT Department
6. Clients

# PART B

# Decompose your user stories into tasks

# Milestone 1

1. As an admin user, I want to have an account to log in to the admin system. (Frontend: 1 week, Backend: 1 week)

   Tasks:

   - Frontend:
   - Design and implement a login page (2 days)
   - Create a form for user authentication (2 days)
   - Implement user interface for account creation (2 days)

   - Backend:
   - Set up user authentication system (2 days)
   - Implement user registration and login functionality (3 days)
   - Store user account information securely (2 days)

2. As a trader, I want to have an account to log in and be able to edit my username and password, so that I can manage my account information securely.

   Tasks:

   - Frontend:
   - Create a user interface for account management (2 days)
   - Design and implement a form for editing username and password (2 days)

   - Backend:
   - Implement backend system for user account management (3 days)
   - Validate and update user account information (2 days)

3. As a trader without an account, I want to view the default indicators and upcoming releases, enabling me to access basic information about the economic calendar even without a registered account.

   Tasks:

   - Frontend:
   - Design and implement a landing page with default indicators (2 days)
   - Display upcoming releases on the landing page (1 day)

   - Backend:
   - Set up default indicator configuration (1 day)
   - Provide APIs to fetch default indicators and upcoming releases (2 days)

# Milestone 2

4. As a trader, I want to be able to manipulate and save my own dashboard to see the indicators I am interested in, allowing me to personalize my trading experience.

   Tasks:

   - Frontend:
   - Design and implement a customizable dashboard interface (3 days)
   - Allow users to select indicators on the dashboard (2 days)

   - Backend:
   - Develop backend APIs for saving and retrieving user-specific dashboard configurations (3 days)
   - Store and retrieve user dashboard configurations from the database (2 days)

5. As a trader, I want to view a list of upcoming economic releases and their expected impact on the market, so that I can make informed decisions and plan my trading strategies accordingly.

   Tasks:

   - Frontend:
   - Design and implement a calendar view to display current and previous releases (3 days)
   - Fetch and display release data from the backend (2 days)

   - Backend:
   - Set up data source integration for retrieving economic release information (2 days)
   - Implement APIs to fetch upcoming releases and their impact (3 days)

6. As an admin user, I want to be able to choose the indicators shown on the page and define the method used to calculate the different values, so that I can customize the economic calendar according to specific requirements. (Frontend: 1 week, Backend: 1 week)

   Tasks:

   - Frontend:
   - Design and implement a settings page for indicators (3 days)
   - Create a user interface for selecting indicators (2 days)
   - Develop a chart to compare previous vs current releases (2 days)

   - Backend:
   - Develop a data model to store indicator settings (2 days)
   - Implement backend APIs for fetching available indicators (3 days)
   - Store and retrieve indicator settings from the database (2 days)

# Outline what features will be in Milestone 1.0 of your project

Milestone 1.0 of the economic calendar website project will focus on delivering essential features for users to view upcoming economic releases and manage their accounts. Here's an outline of the features that will be included in Milestone 1.0:

1. User Registration and Authentication:

   - User registration functionality to allow traders and admin users to create accounts.
   - User authentication system to enable secure login and session management (including login and logout function).

2. Account Management:

   - User profile page where traders can view and edit their account information, such as username and password.

3. Default Indicators and releases:

   - Landing page displaying a list of default indicators and upcoming economic releases.
   - Integration with a data source to retrieve and display the latest release data.

4. Upcoming releases Calendar:

   - Calendar view to present a comprehensive list of upcoming economic releases.
   - release details page providing additional information about each release, including its expected impact on the market.

5. Admin Account:

   - Admin user login functionality to access administrative privileges.
   - Basic admin dashboard to perform administrative tasks, such as managing user accounts and configuring indicators.

6. Responsive Design:
   - Ensuring the website is responsive and optimized for various devices and screen sizes, providing a seamless user experience on desktop and mobile platforms.

This Milestone 1.0 will establish the foundation of the economic calendar website, allowing traders to view upcoming releases, manage their accounts, and provide essential administrative capabilities for admin users.

# Build the iterations (at most 2) that will compose your Milestone 1.0. Record the total days of work and the time it will take for your team to complete that work

Iteration 1: User Registration, Authentication, and Account Management

Features:

- User registration and authentication
- User profile page for account management

Estimated Time:

- User registration and authentication: 5 days
- User profile page: 3 days

Total Days of Work: 8 days

Iteration 2: Default Indicators, Upcoming releases, and Admin Account

Features:

- Landing page with default indicators and upcoming releases
- Calendar view of upcoming releases
- Admin user login and basic admin dashboard

Estimated Time:

- Landing page with default indicators and releases: 4 days
- Calendar view of upcoming releases: 5 days
- Admin user login and dashboard: 5 days

Total Days of Work: 14 days

Overall, Milestone 1.0 will take approximately 8 days for Iteration 1 and 14 days for Iteration 2, resulting in a total of 22 days of work for the team to complete the outlined features. Please note that these estimates are approximate and can vary depending on the complexity of the project, team size, and available resources. It's essential to conduct proper project planning and allocate resources accordingly to ensure a successful and timely delivery of the milestone.

# Allocate tasks to each team member and record the allocation

Team Members:

1. Team Member 1 (Frontend Developer)
2. Team Member 2 (Backend Developer)
3. Team Member 3 (UI/UX Designer)
4. Team Member 4 (QA Tester)

Iteration 1: User Registration, Authentication, and Account Management

1. Team Member 1:

   - User registration and authentication (5 days)
   - Integration of frontend login and registration forms (2 days)

2. Team Member 2:

   - Backend implementation of user registration and authentication (5 days)
   - Backend APIs for user account management (3 days)

3. Team Member 3:

   - Design and implement the user profile page (3 days)
   - Create UI components for account management (1 day)

4. Team Member 4:
   - Create test cases for user registration and authentication (2 days)
   - Perform functional and security testing on the login and registration functionality (2 days)

Iteration 2: Default Indicators, Upcoming releases, and Admin Account

1. Team Member 1:

   - Design and implement the landing page with default indicators and releases (4 days)
   - Integrate frontend components for the calendar view (3 days)

2. Team Member 2:

   - Backend integration with the data source to retrieve release information (3 days)
   - Implement backend APIs for retrieving default indicators and releases (4 days)

3. Team Member 3:

   - Design and develop the calendar view of upcoming releases (5 days)
   - Create UI components for displaying release details (2 days)

4. Team Member 4:
   - Create test cases for the landing page and calendar view (3 days)
   - Perform functional and usability testing on the landing page and calendar functionality (2 days)

# Create a burn down chart for monitoring your team’s progress

Assuming the following estimates for the tasks in Milestone 1.0:

Iteration 1: User Registration, Authentication, and Account Management

- Estimated Effort: 8 days

Iteration 2: Default Indicators, Upcoming releases, and Admin Account

- Estimated Effort: 14 days

Here's a potential burn down chart to monitor the team's progress:
![Picture1](https://github.com/SierraQian/IST303-GroupC-Project/assets/133469784/48341b33-bbfd-47c9-ba22-ceb74488d6c7)

The vertical axis represents the remaining effort in days, while the horizontal axis represents the number of days elapsed. The line indicates the planned effort burn down over time.

As the team completes tasks, the remaining effort decreases. The actual progress is tracked by comparing the remaining effort against the planned effort. Ideally, the actual line should be below the planned line, indicating that the team is ahead of schedule. If the actual line is above the planned line, it suggests the team is behind schedule.

# Include evidence that you are meeting for periodic stand up meetings with your teammates

Based on Agile principles:

1. Schedule regular stand-up meetings: Set a recurring time for your team to meet daily or at a frequency that suits your project's needs. This could be in person, via video conference, or using collaboration tools.

2. Define the purpose and agenda: Start each stand-up meeting by reiterating the purpose, which is to provide brief updates on progress, identify any obstacles, and align on priorities. Keep the meeting focused and time-bound.

3. Share progress updates: Each team member should briefly share what they worked on since the last meeting, what they plan to work on next, and if there are any blockers or challenges.

4. Discuss impediments and provide support: If any team member mentions obstacles or issues, the team can collectively brainstorm solutions or offer assistance to help overcome them.

5. Update the task board or project management tool: Capture the progress made and any changes to the task board or project management tool to reflect the current state of tasks and user stories.

6. Foster open communication: Encourage team members to raise questions, concerns, or dependencies during the stand-up meetings. This promotes collaboration and helps address any issues early on.

The primary purpose of stand-up meetings is to foster transparency, collaboration, and alignment within the team. While I cannot provide evidence of actual stand-up meetings taking place, implementing these practices can help your team stay on track and maintain effective communication.

# Ensure that your development and testing environment is set up. Be sure to have some working functional (however rudimentary) and test code in your repository

General steps:

1. Choose a Version Control System (VCS): GitHub --> https://github.com/SierraQian/IST303-GroupC-Project

2. Set Up Development Environment:

   - Install the necessary software and tools for development, including the programming language, frameworks, libraries, and IDEs or text editors.
   - Configure your development environment to ensure proper integration and compatibility with the chosen technologies.

3. Create Project Structure:

   - Organize your project files and directories based on best practices and the specific requirements of your programming language or framework.
   - Set up the necessary configuration files for your project, such as package.json, pom.xml, or requirements.txt.

4. Write Initial Functional Code:

   - Start by implementing basic functionality to demonstrate the core features of your application.
   - Build a simple working prototype or Minimum Viable Product (MVP) to test the basic functionality.

5. Set Up Testing Environment:

   - Choose a testing framework that aligns with your project requirements and programming language.
   - Install the testing framework and any necessary testing dependencies.
   - Set up test directories and create test files to write test cases for your code.

6. Write Initial Test Code:

   - Begin by writing basic test cases to cover the critical functionality of your application.
   - Use the testing framework to execute the test cases and verify that the code is functioning correctly.

7. Commit and Push:
   - Use the VCS to commit and push your code to the repository, ensuring that your functional and test code is safely stored and version controlled.

# Part C

<a href="https://docs.google.com/presentation/d/1ni1wBBxDgJWjzWgd-ISLGnQGoXP8ufWI1rC_jBP3ebY/edit?usp=sharing">Presentation</a>

# Part D

<a href="#">Presentation 2</a>
