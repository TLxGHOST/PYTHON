import cv2
import mediapipe as mp
import numpy as np


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def draw_on_frame(frame, points):
    for i in range(1, len(points)):
        if points[i-1] is None or points[i] is None:
            continue
        cv2.line(frame, points[i-1], points[i], (0, 0, 255), thickness=5)


def erase_drawing(points, frame, threshold=50):
    for i, (x, y) in enumerate(points):
        if x is None or y is None:
            continue
        for j in range(len(points)):
            if points[j] is None:
                continue
            dist = np.sqrt((x - points[j][0])**2 + (y - points[j][1])**2)
            if dist < threshold:
                cv2.circle(frame, (x, y), 10, (255, 255, 255), -1)
                points[i] = None


def track_and_draw():
   
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

   
    frame_width = 1280
    frame_height = 720
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
    
    with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        
        points_history = []
        drawing = False

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame from webcam.")
                break
            
           
            frame = cv2.flip(frame, 1)
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
           
            rgb_frame.flags.writeable = False
            results = hands.process(rgb_frame)

            
            rgb_frame.flags.writeable = True
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    
                   
                    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    index_finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
                    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                    
                    height, width, _ = frame.shape
                    finger_tip_x = int(index_finger_tip.x * width)
                    finger_tip_y = int(index_finger_tip.y * height)
                    finger_pip_y = int(index_finger_pip.y * height)
                    middle_finger_tip_x = int(middle_finger_tip.x * width)
                    middle_finger_tip_y = int(middle_finger_tip.y * height)

                    
                    if finger_tip_y < finger_pip_y:
                       
                        points_history.append((finger_tip_x, finger_tip_y))
                        drawing = True
                    else:
                       
                        points_history.append(None)
                        drawing = False

                    # Determine if the middle finger is near the index finger for erasing
                    # distance = np.sqrt((finger_tip_x - middle_finger_tip_x) ** 2 + (finger_tip_y - middle_finger_tip_y) ** 2)
                    # if distance < 50:
                    #     erase_drawing(points_history, frame, threshold=50)

            # Draw on frame using points history
            draw_on_frame(frame, points_history)

           
            cv2.imshow('MediaPipe Hands with Drawing and Erasing', frame)

  
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    track_and_draw()
