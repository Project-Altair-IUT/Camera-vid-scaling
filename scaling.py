import cv2

# Function to display video from a wide-angle camera with a specified aspect ratio
def display_wide_angle_video(camera_index=0, target_width=640, target_height=480):
    # Open the camera
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Set up window
    window_name = "Wide Angle Video"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    try:
        while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read frame.")
                break

            # Resize the frame to the target width and height
            frame = cv2.resize(frame, (target_width, target_height))

            # Apply wide-angle transformation (you need to implement this based on your camera's characteristics)

            # Display the frame
            cv2.imshow(window_name, frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()

# Specify the camera index (you may need to change this based on your system)
camera_index = 1

# Specify the target width and height for the displayed video
target_width = 1200
target_height = 400

# Call the function to display wide-angle video with the specified aspect ratio
display_wide_angle_video(camera_index, target_width, target_height)
