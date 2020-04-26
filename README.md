# Facial-recognition-linux
Train facial recognition software on your images, then use it to unlock your device or for any other purpose
Step 1) take a 10 sec video of yours through the webcam
Step 2) split it to get hundreds of pictures (preferably different angles)
Step 3) use encdings.py on these to get an (almost) perfect encodings of yours
Step 4) use facial_recog.py to start webcam and identify you

This repository uses ageitgey's facial recognition system (https://github.com/ageitgey/face_recognition). So be sure to install all the necessary files

Warning: Don't configure PAM if you don't know enough about it. It can temporarily or permanently block your access to device
Finally, configure PAM (Linux authentication system) to use facial recognition instead of password to unlock device (this is not done in the project, yet)

Have fun!
