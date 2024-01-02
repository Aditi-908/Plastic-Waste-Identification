import cv2
import os
import getpass

def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        
        if key == ord('c'):
            print("Image captured")
            print(base_path)
            cv2.imwrite(f'{base_path}_{n}.{ext}', frame)
            n += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)

if __name__ == "__main__":
    username = getpass.getuser()
    test_dir = f'/Users/{username}/Downloads/major_project/test'  # Adjust the path as needed
    save_frame_camera_key(0, test_dir, 'camera_capture')
