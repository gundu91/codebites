# Python Helper
Note: This is primarily a self-serving document written for my environment. It is not a general resource. 

## Creating a Virtual Environment on Windows
1. Enter your project directory: <code>$ cd my_project_folder</code>
2. Create the virtual enviroment: <code>$ virtualenv my_project_env</code>
   
   For a specific python version: <code>$ virtualenv --python=C:\Python27\python.exe my_project_env </code>, replacing "C:\..." with the path to the python executable you want to use
3. Activate the virtual environment: <code>$ my_project_env\Scripts\activate</code>
4. Install the packages you need for your project
5. Save a list of the packages you've installed: <code>pip freeze > requirements.txt</code>
6. Deactivate the virtual enviroment: <code>$ deactivate</code>

Here's a <a href="http://docs.python-guide.org/en/latest/dev/virtualenvs/">more detailed and more general tutorial</a>.
