import cv2



def extract_frames_per_second(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Get the FPS of the video
    frame_count = 0
    extracted_count = 0
    frames = []
    while True:
        success, frame = cap.read()
        if not success:
            break
        if frame_count % fps == 0:
            frames.append(frame)
            cv2.imwrite(f'{output_folder}/frame_{extracted_count:04d}.png', frame)
            extracted_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {extracted_count} frames (1 frame per second).")
    return frames

