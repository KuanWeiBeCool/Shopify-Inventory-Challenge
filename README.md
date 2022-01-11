# Shopify-Inventory-Challenge

Here is the link of my app, feel free to test it out: https://kw-inventory-app.herokuapp.com/

***Please note that the app might be sleeping, so you might need to wait for a moment for it to wake up :)***


Please check the YouTube video for detailed instruction of how to use my app: https://youtu.be/hy3H0PPgqOY


# Download The Repository and Run Locally

If you got any issue running the deployed version of my app, or if you simply prefer running locally, you can do the following steps:

1. Download and install [Visual Studio Code](https://code.visualstudio.com/)

2. Install the Python extension on Visual Studio Code. You can either go to the [link](https://marketplace.visualstudio.com/items?itemName=ms-python.python) or directly add in your VS code:
![image](https://user-images.githubusercontent.com/64152297/148977219-df0cd4e8-4bdf-4825-aff8-d03ad9edbc22.png)

3. Install a version of Python 3. Options include: 
  - (All operating systems) A download from python.org;
  - (Linux) The built-in Python 3 installation works well, but to install other Python packages you must run sudo apt install python3-pip in the terminal.
  - (macOS) An installation through [Homebrew](https://brew.sh/) on macOS using brew install python3 (the system install of Python on macOS is not supported).

4. On Windows, make sure the location of your Python interpreter is included in your PATH environment variable. You can check the location by running path at the command prompt. If the Python interpreter's folder isn't included, open Windows Settings, search for "environment", select **Edit environment variables for your account**, then edit the **Path** variable to include that folder.

5. Download the repository and unzip the folder
6. Open the folder in VS Code using the **Open Folder** option under **File** on the top left of VS Code and select the folder.
7. Open a new terminal using the **New Terminal** option under **Terminal** on the top left of VS Code.
8. Run the following command to create a virtual environment named .venv:

**Linux**

sudo apt-get install python3-venv    # If needed

python3 -m venv .venv

source .venv/bin/activate


**macOS**

python3 -m venv .venv

source .venv/bin/activate

**Windows**

py -3 -m venv .venv

.venv\scripts\activate

9. In VS Code, open the Command Palette (**View** > **Command Palette** or (Ctrl+Shift+P)). Then select the **Python: Select Interpreter** command:
![image](https://user-images.githubusercontent.com/64152297/148978774-54ce5129-afea-4a2f-a098-b6d026caa3fd.png)

10. The command presents a list of available interpreters that VS Code can locate automatically (your list will vary; if you don't see the desired interpreter, see [Configuring Python environments](https://code.visualstudio.com/docs/python/environments)). From the list, select the virtual environment in your project folder that starts with ./.venv or .\.venv:
![image](https://user-images.githubusercontent.com/64152297/148978901-8198329f-ffaf-4f8b-9787-01f6872c3473.png)

11. Run Terminal: Create New Terminal (Ctrl+Shift+`) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script. The selected environment appears on the left side of the VS Code status bar, and notices the ('.venv': venv) indicator that tells you that you're using a virtual environment:

![image](https://user-images.githubusercontent.com/64152297/148979011-f3e6b631-9896-4649-aa06-6fbec3f7c94c.png)


12. Update pip in the virtual environment by running the following command in the VS Code Terminal:

python -m pip install --upgrade pip

13. Install all the required packages;

pip install -r requirements.txt

14. Open the app and copy the server url to your browser to start exploring!

python manage.py runserver

![image](https://user-images.githubusercontent.com/64152297/148980312-e3dc1dbf-960b-4429-8a30-b2d1c35b760b.png)
