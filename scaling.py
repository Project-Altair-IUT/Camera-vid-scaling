import cv2

def display_wide_angle_video(camera_index, target_width, target_height, output_file):
    # Open the camera
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Get the frames per second (fps) and frame size from the camera
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_size = (target_width, target_height)

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Use avc1 codec
    out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

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

            # Write the frame to the output file
            out.write(frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Release the camera, close the window, and release the VideoWriter
        cap.release()
        out.release()
        cv2.destroyAllWindows()

# Specify the camera index (you may need to change this based on your system)
camera_index = 0

# Specify the target width and height for the displayed video
target_width = 1500
target_height = 500

# Specify the output file name with ".mp4" extension
output_file = "output_video.mp4"

# Call the function to display wide-angle video and save it to the specified output file
display_wide_angle_video(camera_index, target_width, target_height, output_file)
