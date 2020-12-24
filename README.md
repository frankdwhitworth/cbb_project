# College Basketball Betting Risk Project

### What is this?
This is called a GitHub repository. It is a tool that is essentially Google Drive for big programming projects. We will use this to share our progress and also to dump files and info for eachother. 

### Instructions for using this GitHub Repository
1) In order to use this GitHub repository, you will need to use Visual Studio Code (VSCode). Make sure you have downloaded VSCode and have it open. 
2) Next, you will need to clone the repository into your `Documents` folder for your computer. You can do this by clicking the third tab on the far left (the network looking button) and pressing "clone repository"
3) Select your Documents folder to clone it to and then click "Open workspace" with it
4) Now, open your command line again if it closed
5) Now, you can look inside of the repository and also dump your own files inside of it. However, whenever you want to save all of your changes so that I can see it, you have to do is press the GitHub tab on the left and write a commit message, press the check mark, wait, press the three dots, and then press Push 


### What to do now?
Try to run the `main.py` that is inside this repository. Enter this into your command prompt: (first make sure that you are in the cbb_project folder)
```sh
python3 main.py
```
You can now mess around inside of the repository and edit some of the code or just look at it. I will try to make comments in my code so you can understand it, but if you have any questions about any code, just shoot me a text. 

If you have any ideas or files you want me to look at, just put it in the `cbb_project/ideas_and_files` folder that I made. 

Text me when you have read over all of this and are ready to get to work and make some money 🤑


### How to run code
This is important so pay attention.

Whenever I make edits to the python script, I might be installing different libraries and tools. To make sure that you and I have the same libraries installed and everything is synced up, we will be working in a virtual environment (venv). What this venv will ensure is the fact that you and I (and whoever is on the project) will have the same libraries and nothing will be left out at compile and run time. 

Every time you want to run our program, you are going to have to go into the venv by doing the following command: 
```sh
source .gitignore/env/bin/active
```
you should see `(env)` to the left of the command line now. Now, do this command to ensure you are using the right python3
```sh
which python3
```
If you see `/cbb_project/.gitignore/env/bin/python` at the end of the file location, then you are successfully using the venv python and you are good to go
