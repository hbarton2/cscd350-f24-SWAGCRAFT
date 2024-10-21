# SWAGCRAFT UML Editor 
This project is a UML editor written in python, the current implementation is built for use in CLI and the team expects to expand functionality to include GUI features in the near future. 

## Installation
the first step to install the project is to navigate to the group github and preform a git clone on the main branch of the project (assuming you have access).
  
The project uses colorama to enhance the CLI user experience by added a multi-colored output in the command line. This makes the output stand out and easy to use. Before running the application, you will need to install a colorama dependency by typing `pip install colorama` in the command line

1) navigate to the github (https://github.com/hbarton2/cscd350-f24-SWAGCRAFT) and use the git clone feature by selecting the green "Code" tab and selecting the HTTPS option then selecting "Copy URL to Clipboard"

2) once the URL is copied you will go to your command line on your machine or in a VM, if issues occur installing Colorama dependency in step (??) using a VM is recommended. Navigate to the place you want to install the git clone. Once in the correct directory run the command `git clone https://github.com/hbarton2/cscd350-f24-SWAGCRAFT.git`
3) After the git clone is completed navigate to the folder then the application can be ran using the command `python3 main.py`.
4) the application is a CLI interface using text commands, each command will be listed when the program starts and additional information can be found by typing `help`