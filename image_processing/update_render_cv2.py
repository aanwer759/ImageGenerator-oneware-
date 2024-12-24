import cv2
import numpy as np

def get_image(img1, img2, y, x ):
# Load the base image and overlay image
    #img1 = cv2.imread("base_image.jpg")  # Replace with your base image path
    #img2 = cv2.imread("overlay_image.jpg")  # Replace with your overlay image path

# Resize img2 to a desired size (optional)
    #img2 = cv2.resize(img2, (150, 150))  # Resize to 150x150 pixels

# Define the position where img2 will be placed on img1
    x_offset, y_offset = x,y

# Create a mask for img2 by identifying black pixels
# Convert to grayscale
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create the mask: Non-black pixels in img2 are white (foreground)
    _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

# Invert the mask: Black pixels in img2 become white (background)
    mask_inv = cv2.bitwise_not(mask)

# Extract the region of interest (ROI) from img1 where img2 will be placed
    roi = img1[y_offset:y_offset+img2.shape[0], x_offset:x_offset+img2.shape[1]]

# Use the mask to blend img2 with the ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  # Background from img1
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)    # Foreground from img2

# Combine the background and the foreground
    dst = cv2.add(img1_bg, img2_fg)

# Place the combined result back into img1
    img1[y_offset:y_offset+img2.shape[0], x_offset:x_offset+img2.shape[1]] = dst

# Display the final image
    cv2.imshow("Result", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img1


def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result


def get_updated_render_cv2(img1, img2, x_offset, y_offset, rotation, scale):

    img1 = np.array(img1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
    img2 = np.array(img2)

    scale = int(scale)
    rotation = int(rotation)
    
    img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
    width = int(img2.shape[1] * scale / 100)
    height = int(img2.shape[0] * scale / 100)
    img2= cv2.resize(img2,(width, height))

    img2 = rotate_image(img2, (rotation))
    

# Create a mask for img2 by identifying black pixels
# Convert to grayscale
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create the mask: Non-black pixels in img2 are white (foreground)
    _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
   
   
    non_zero_indices = np.argwhere(mask > 0)
      # First row and column where mask > 0 
    #print("First non-zero value found at:", non_zero_indices[0][0])

    #print("First non-zero value found at:", non_zero_indices[0])
    #first_non_zero_x = non_zero_indices[0][0]
    #first_non_zero_y = non_zero_indices[0][1]
    x_bound, y_bound, w_bound, h_bound = cv2.boundingRect(non_zero_indices)
    #print("x_bound:",x_bound)
    img2 = img2[y_bound:y_bound+h_bound,x_bound:x_bound+w_bound]
    mask = mask[y_bound:y_bound+h_bound,x_bound:x_bound+w_bound]
# Invert the mask: Black pixels in img2 become white (background)
    
    mask_inv = cv2.bitwise_not(mask)
    
# Extract the region of interest (ROI) from img1 where img2 will be placed
    roi = img1[y_offset:y_offset+img2.shape[0], x_offset:x_offset+img2.shape[1]]
    

# Use the mask to blend img2 with the ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  # Background from img1
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)    # Foreground from img2

# Combine the background and the foreground
    dst = cv2.add(img1_bg, img2_fg)
    #cv2.imshow("dst", dst)
    
# Place the combined result back into img1
    img1[y_offset:y_offset+img2.shape[0], x_offset:x_offset+img2.shape[1]] = dst
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    return img1



#img1  =cv2.imread("images/background/0.jpg")
#img2 = cv2.imread("images/objects/obj1/sample1.jpg")
#img2 = process_image(img2)
#test = get_updated_render_cv2(img1,img2,10 ,10 , 0, 100)

#cv2.imshow("check", test)
#cv2.waitKey(0)