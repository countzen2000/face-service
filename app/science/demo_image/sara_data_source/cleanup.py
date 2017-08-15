from __future__ import division, print_function, absolute_import

import cv2
import os


# Loading each image is very slow, but lets try one run

face_cascade = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('classifier/haarcascade_eye.xml')


# # Make sure the data is normalized
# img_prep = ImagePreprocessing()
# img_prep.add_featurewise_zero_center()
# img_prep.add_featurewise_stdnorm()
#
# # Create extra synthetic training data by flipping, rotating and blurring the
# # images on our data set.
# img_aug = ImageAugmentation()
# img_aug.add_random_flip_leftright()
# img_aug.add_random_rotation(max_angle=25.)
# img_aug.add_random_blur(sigma_max=3.)


for i in range(1,7377): #1-7377
    count_name = str(i)
    while len(count_name) < 4:
        count_name = "0"+count_name
    try:
        gray = cv2.imread("demo_image/sara_data_source/output-{0}.jpg".format(count_name), cv2.IMREAD_GRAYSCALE)
    except:
        continue
    # print ("loaded: {0}".format(count_name))

    # detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # print ("face count: {0}".format(len(faces)))

    # draw squares around faces and output
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # If the faces match use that to train on.
    if len(faces) <= 0:
        print ("noFaces")
        print(count_name)
        # cv2.imshow("Output", gray)
        try:
            os.rename("demo_image/sara_data_source/output-{0}.jpg".format(count_name), "demo_image/sara_data_source/noface/output-{0}.jpg".format(count_name))
        except:
            print ("couldn't move")
            print(count_name)


    # cv2.imshow("Output", gray)
    # cv2.waitKey()