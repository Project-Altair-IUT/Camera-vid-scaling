import cv2
import numpy as np

dim = (512, 384)
# Load images
img1 = cv2.imread('photos/one.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('photos/two.jpg', cv2.IMREAD_COLOR)

l = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
r = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

imgs = []

imgs.append(l)
imgs.append(r)

stitcher = cv2.Stitcher_create()
stitcher.setPanoConfidenceThresh(0.1)
status, pano = stitcher.stitch(imgs)

if status == cv2.Stitcher_OK:
    print("Panorama")
    cv2.imshow("Panorama", pano)

    # Save the panorama as 'pan.jpg'
    cv2.imwrite('pan.jpg', pano)

    cv2.waitKey()
    cv2.destroyAllWindows()
elif status == cv2.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL:
    print("Error STITCHER_ERR_CAMERA_PARAMS_ADJUST_FAIL")
elif status == cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
    print("Error STITCHER_ERR_HOMOGRAPHY_EST_FAIL")
elif status == cv2.Stitcher_ERR_NEED_MORE_IMGS:
    print("Error STITCHER_ERR_NEED_MORE_IMGS")
elif status == cv2.Stitcher_PANORAMA:
    print("Error STITCHER_PANORAMA")
elif status == cv2.Stitcher_SCANS:
    print("Error STITCHER_SCANS")
