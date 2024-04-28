# B657 Project: Object Detection in Historical Television Advertisements

## Project Idea

The Indiana University Libraries Moving Image Archive (IULMIA) has a collection of award-winning digitized television ads from the 1960s and 1970s. This collection is popular with researchers, historians, and filmmakers looking for historical footage, but it can be difficult to locate requested materials. One challenging use case is requests for footage containing a specific object, such as footage containing rings or jewelry or footage containing a TV. It would be very useful for IULMIA staff to be able to query this collection for footage based on object detection. Currently, there are about 1700 video items publicly available, many of them very brief clips of about 1 minute. Initial experimentation with current commercially-available models, presumably trained on contemporary imagery, such as provided through Google, AWS, and Azure, found that they were not very reliable at object detection for several sample items in this historical collection.

## Instructions to Run

1. Place the video files in the `data/videos` directory.
2. Run the `dataset.ipybn` notebook to extract frames from the videos. This will create a `data/frames` directory with the extracted frames.
3. Outputs from the object detection models will be saved in the `data/results` directory.
4. `yolo5_365.ipybn` notebook requires yolov5 model to be cloned from the official repository.
