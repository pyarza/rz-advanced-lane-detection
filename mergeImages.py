import cv2
from os.path import basename, join

camera_cal_dir = 'camera_cal'
calibration_outputs_dir = 'output_images/camera_cal'

fName = 'calibration_grid10.jpg'
fName = 'calibration_grid20.jpg'
fName = 'calibration_grid40.jpg'
fName = 'calibration_grid80.jpg'
fName = 'calibration2.jpg'
fName = 'calibration3.jpg'

i1 = cv2.imread(calibration_outputs_dir + "/Undist_" + fName)
print(calibration_outputs_dir + "/Undist_" + fName)

print(camera_cal_dir + "/" + fName)
i2 = cv2.imread(camera_cal_dir + "/" + fName)

dst = cv2.addWeighted(i2, 0.5, i1, 0.5, 0)
cv2.imshow('Differences: ' + basename(fName), dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

write_name = join(calibration_outputs_dir, 'merge_' + basename(fName))
cv2.imwrite(write_name, dst)
