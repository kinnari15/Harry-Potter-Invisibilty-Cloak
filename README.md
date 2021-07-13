# Harry Potter Invisibility Cloak.

In this mini project, I tried to create a replica of the famous harry potter invisibility cloak that harry potter used to escape from difficult situations. I referred a few videos on Youtube to understand the working behind this project and have tried creating one.


# Steps : 

- import cv2 and numpy.
- Capture a picture of your background and save the image.
- Read every frame from video till the camera is open.
- Convert the frame/image to HSV.
- Next, we need to generate masks to detect a colour (in our case, it's red colour). 
- Finally, we add two masks. One which finds all the red coloured points present. Second mask ignores the red colour so that it can show us the background thus masking all the red coloured points or in our case a cloth making our body invisible.

# Conclusion

This project was fun as well was able to apply a bit of openCV knowledge.

##  Additional changes to be made :

The project when run contains a bit of impurities i.e. noise. I will be working on the dilation and morphology part soon.
 






