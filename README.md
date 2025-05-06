#FlapJacks the game!

#There was a bit of a process to get my code uploaded to github. This is the steps that were taken. \\
#Installed and configured Git with. \\
<sudo apt install git>  
<git config --global user.name "Username">  
<git config --global user.email "email@email.com">  

#I had already created a github account but added the repository "FlapJacks"
#Initialized the Directory (~/Documents/network/python): <br>
<git init>

#linked project with the repository: <br>
<git remote add origin https://github.com/lkboisa/FlapJacks.git>

#Staged files for entire folder: <br>
<git add.>
#For individual files: <br>
<git add file>
#commit files: <br>
<git commit -m "first commit">

#In order to commit files that have been modified you can skip the "git add" and just use the -a flag so: <br>
<git commit -a -m "commit comment">
#(-m is for the message)

#created a keypair: <br>
<ssh-keygen -t ed25519 -C "lkboisa@yahoo.com">

#Grabbed the public key from ~/.ssh/id_ed25519.pub and pasted (contaent of entire file) to Github.com/lkboisa/FlapJacks/Settings/Deploy Keys/Add deploy keys

#push code: <br>
<git push -u origin main>

#Note you only need to push use the entire above push code once, as after that git knows you want to push the code and you can just use: <br>
<git push>
_______________________________________________________________________________________

#Note to stage the file you either stage file:  <br>
<git add <file_name> 
#or stage directory: <br>
<git add .>

#Then commit:
<git commit -m "comment">

#To upload to the server:
<git push>


