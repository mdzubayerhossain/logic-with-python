import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands and drawing utils
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Function to count fingers
def count_fingers(hand_landmarks):
    tips = [8, 12, 16, 20]
    count = 0
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    return count

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame and find hands
        result = hands.process(rgb_frame)

        # Draw hand landmarks
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Count the number of fingers
                fingers_count = count_fingers(hand_landmarks)
                
                # If 2 fingers are detected, simulate a spacebar press
                if fingers_count == 2:
                    pyautogui.press('space')
                    print("V sign detected - Spacebar pressed")

        # Display the resulting frame
        cv2.imshow('Hand Gesture Recognition', frame)

        if cv2.waitKey(5) & 0xFF == 27:
            break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
           