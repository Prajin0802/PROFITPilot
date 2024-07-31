# tanX.fi Online Assessment Task - PROFITPilot
PROFITPilot is a data analytics tool for businesses to analyze and visualize revenue. It offers insights into monthly revenue, product contributions, customer revenue, and identifies top customers. Using Streamlit, it provides interactive charts for easy exploration and decision-making. Currently it uses a custom sample dataset 'orders.csv'.

- TABLE OF CONTENTS:
    - Features
    - Setup
    - Docker
    - Running the Project without docker
    - Running main.py
    - Running Tests with tests.py
    - Running the streamlit_app.py
    - Project Structure
    - Demo video

FEATURES:
  - Monthly Revenue Analysis: View and analyze revenue trends by month.
  - Product Revenue Breakdown: See which products generate the most revenue.
  - Customer Revenue Insights: Analyze revenue contributions from individual customers.
  - Top Customers Identification: Identify the top 10 customers based on revenue.
  - Interactive Visualization: Use Streamlit for dynamic data visualization.

STEPS:
  1. Clone the Repository:
  2. Create a Virtual Environment (optional but recommended)
  3. Activate the Virtual Environment:
  4. Install Dependencies:
       - pandas
       - streamlit

PREREQUISITES:
- Ensure you have the following installed on your system:
    - Docker
    - Docker Compose
    
STEPS TO RUN THE APPLICATION:
 - Clone the repository to your local machine:

       git clone https://github.com/Prajin0802/tanX.fi-Online-Assessment---PROFITPilot.git
 - Download the Orders Data
        - Ensure you have the orders.csv file in the root directory of the repository. If you don't have it, request the file from the project maintainer and place it in the root directory.
 - Pull the Docker Images
        - Pull the necessary Docker images from Docker Hub using the following commands:
   
            docker pull prajincmakam/profitpilot-main:latest
            docker pull prajincmakam/profitpilot-streamlit_app:latest
            docker pull prajincmakam/profitpilot-tests:latest
            
 - Run the Application with Docker Compose
 - Use Docker Compose to start all services:
   
        docker-compose up
   
THIS WILL START THE FOLLOWING SERVICES:
- main_app: Processes the revenue metrics.
- streamlit_app: Runs the Streamlit web application.
- tests_app: Runs the unit tests.

  
ACCESS THE STREAMLIT APPLICATION:
- Once the containers are running, you can access the Streamlit application by opening a web browser and navigating to:
    
        http://localhost:8501

STOPPING THE APPLICATION:
- To stop the application, press Ctrl+C in the terminal where Docker Compose is running. Alternatively, you can run:

        docker-compose down
    
ADDITIONAL NOTES:
- Ensure that the orders.csv file is up-to-date and placed in the root directory before starting the application.
- If you encounter any issues, check the container logs for more details:

        docker-compose logs

WITHOUT DOCKER:
- TERMINAL COMMANDS TO INSTALL pandas, streamlit:
  - type this command in the terminal -> "pip install pandas streamlit"
  - to check the installed packages -> "pip list"
  - to check the version and other properties of the installed packages -> "pip show pandas" and "pip show streamlit"

- TERMINAL COMMANDS TO RUN the project files:
  - to run 'main.py' script -> "python main.py"
  - to run 'tests.py' script -> "python tests.py"
  - to run 'streamlit_app.py' script -> "streamlit run streamlit_app.py"

- PROJECT STRUCTURE:
    - .dockerignore -> for ignoring pycache(pyc) files, just in case
    - Dockerfile -> for imaging and copying directory to docker
    - docker-compose.yml -> contains all the relevant services
    - main.py -> python script to compute the tasks from 'orders.csv'
    - orders.csv -> sample dataset for the task
    - streamlit_app.py -> A web view for visualising relevant graphs
    - tests.py -> to test the script with manually calculated expected values

- DEMO VIDEO:

      https://drive.google.com/file/d/1DU1v1IbtHAJcU5S0NjWQ3rI6nOgzBWwz/view?usp=sharing
