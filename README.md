#FlapJacks the game

#There was a bit of a process to get my code uploaded to github. This is the steps that were taken:  <br>
#Installed and configured Git with: <br>
<sudo apt install git> <br>
<git config --global user.name "Username"> <br>
<git config --global user.email "email@email.com"> <br>

#I had already created a github account but added the repository "FlapJacks"
#Initialized the Directory (~/Documents/network/python): <br>
<git init>

#linked project with the repository: <br>
<git remote add orgin https://github.com/lkboisa/FlapJacks.git>

#Staged Files: <br>
<git add.>
#commit files: <br>
<git commit -m "first commit">

#created a keypair: <br>
<ssh-keygen -t ed25519 -C "lkboisa@yahoo.com">

#Grabbed the public key from ~/.ssh/id_ed25519.pub and pasted (contaent of entire file) to Github.com/lkboisa/FlapJacks/Settings/Deploy Keys/Add deploy keys

#push code: <br>
<git push -u orgin main>

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

