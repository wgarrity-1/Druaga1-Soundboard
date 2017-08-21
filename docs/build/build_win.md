# Building For Windows
This is how to build Druaga1 Soundboard for Windows
## Requirements
* Python 3.6 or later
* Pygame
* Guizero
* Pyinstaller Development Versions
* NSIS (only if you are planning on building the installer)  <br>
  <br>
To find instructions on how to install these programs, see /doc/requirements-win.md for more information.
## Instructions for Regular Build
1. Fork this repository with either git or download the zip file.
1. Open Command Prompt or Powershell in the code's folder and type `pyinstaller main.py`
  1. **NOTE: There might be some errors appearing on screen, but it should be fine**
1. When finsihed, close Powershell or CMD and open the main repository folder
1. Move all audio files and the License file to the main folder in the dist folder
1. Open that main folder and run main.exe
## Instructions for Building the Installer
1. Go to the main respository folder and move the installer.nsi file to the dist folder
1. Open the dist folder and right click on the installer.nsi file
1. Click on the "Compile NSIS Script" option
1. When done, close the window and the install file should appear
