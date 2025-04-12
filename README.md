#FlapJacks the game

#There was a bit of a process to get my code uploaded to github. This is the steps that were taken:
#Installed and configured Git with:
<sudo apt install git>
<git config --global user.name "Username">
<git config --global user.email "email@email.com">

#I had already created a github account but added the repository "FlapJacks"
#Initialized the Directory (~/Documents/network/python):
<git init>

#linked project with the repository:
<git remote add orgin https://github.com/lkboisa/FlapJacks.git>

#Staged Files:
<git add .>

#commit files:
<git commit -m "first commit">

#created a keypair:
<ssh-keygen -t ed25519 -C "lkboisa@yahoo.com">

#Grabbed the public key from ~/.ssh/id_ed25519.pub and pasted (contaent of entire file) to Github.com/lkboisa/FlapJacks/Settings/Deploy Keys/Add deploy keys

#push code:
<git push -u orgin main>

#Note you only need to push use the entire above push code once, as after that git knows you want to push the code and you can just use:
<git push>
_______________________________________________________________________________________

#Note to stage the file you either stage file:
<git add <file_name> 
#or stage directory:
<git add .>

#Then commit:
<git commit -m "comment">

#To upload to the server:
<git push>

