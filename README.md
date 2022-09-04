# A Battleship Game



# Deployment

- Add newline (/n) to all input methods
- Save the file
- Create a list of dependencies and add them to a requirements.txt file 
- In the terminal: "pip3 freeze > requirements.txt"
- Push the changes up to Github
- Go to Heroku's website and login
- On the Heroku dashboard click the create new app button
- Name the app a unique name 
- Select region
- Click create app
- Select the setting tab
-  Scroll to the Config Var section and add:
   - Config Var: PORT. _______ Set it to:8000
- add two buildpacks in this order:
  1. `heroku/python`
  1.  `heroku/nodejs`
- Select the Deploy tab
- Then select Github and confirm connect to Github
- Search for the repository name
- Then click connect
- Select either manual or automatic deploy
- Click view to view  

**Test Label**  

**Test Action** 

**Expected Outcome**