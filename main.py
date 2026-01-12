import cv2
import mediapipe as mp
import pyautogui
import time
import math
import sys

# --- SENIOR DEV SAFETY FIRST ---
# 1. If you slam your mouse to the top-left corner, the script crashes.
# This is your "Emergency Brake."
pyautogui.FAILSAFE = True 

def map_range(x, in_min, in_max, out_min, out_max):
    x = max(min(x, in_max), in_min)
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
screen_w, screen_h = pyautogui.size()

cloc_x, cloc_y = 0, 0 
ploc_x, ploc_y = 0, 0 
smooth = 4 
scroll_speed_multiplier = 40 

clicked = False 
right_clicked = False
stealth_active = False
screenshot_taken = False
last_zoom_time = 0 

# Use index 0 for default camera
cap = cv2.VideoCapture(0)

# Check if camera opened (Critical for .exe troubleshooting)
if not cap.isOpened():
    sys.exit()

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success: break

        frame = cv2.flip(frame, 1)
        f_h, f_w, _ = frame.shape
        center_y = f_h // 2
        margin = 30 

        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                lm = hand_landmarks.landmark
                itip, iknuckle = lm[8], lm[6]   
                mtip, mknuckle = lm[12], lm[10] 
                rtip, rknuckle = lm[16], lm[14] 
                ptip, pknuckle = lm[20], lm[18] 
                ttip = lm[4]                    

                index_up = itip.y < iknuckle.y
                middle_up = mtip.y < mknuckle.y
                ring_up = rtip.y < rknuckle.y
                pinky_up = ptip.y < pknuckle.y

                finger_gap = ((itip.x - mtip.x)**2 + (itip.y - mtip.y)**2)**0.5
                zoom_gap = ((ttip.x - ptip.x)**2 + (ttip.y - ptip.y)**2)**0.5
                palm_spread = ((itip.x - ptip.x)**2 + (itip.y - ptip.y)**2)**0.5

                # --- MODE 1: STEALTH ---
                if index_up and middle_up and ring_up and pinky_up and palm_spread > 0.15:
                    if not stealth_active:
                        pyautogui.hotkey('win', 'd'); stealth_active = True; time.sleep(0.7)
                    continue

                # --- MODE 2: ZOOM ---
                elif index_up and pinky_up and not middle_up and not ring_up:
                    current_time = time.time()
                    if current_time - last_zoom_time > 0.3:
                        if zoom_gap > 0.15: pyautogui.hotkey('ctrl', '+'); last_zoom_time = current_time
                        elif zoom_gap < 0.08: pyautogui.hotkey('ctrl', '-'); last_zoom_time = current_time

                # --- MODE 3: JOYSTICK SCROLL ---
                elif index_up and middle_up and finger_gap < 0.08:
                    offset = center_y - (itip.y * f_h)
                    if abs(offset) > 40:
                        speed = int((offset / 10) * scroll_speed_multiplier)
                        pyautogui.scroll(speed)

                # --- MODE 4: SCREENSHOT ---
                elif index_up and middle_up and finger_gap > 0.08:
                    if not screenshot_taken:
                        pyautogui.hotkey('win', 'shift', 's'); screenshot_taken = True; time.sleep(0.5)

                # --- MODE 5: MOUSE ---
                elif index_up:
                    target_x = map_range(itip.x * f_w, margin, f_w - margin, 0, screen_w)
                    target_y = map_range(itip.y * f_h, margin, f_h - margin, 0, screen_h)
                    cloc_x = ploc_x + (target_x - ploc_x) / smooth
                    cloc_y = ploc_y + (target_y - ploc_y) / smooth
                    pyautogui.moveTo(cloc_x, cloc_y, _pause=False)
                    ploc_x, ploc_y = cloc_x, cloc_y 
                    
                    l_pinch = ((itip.x - ttip.x)**2 + (itip.y - ttip.y)**2)**0.5
                    r_pinch = ((mtip.x - ttip.x)**2 + (mtip.y - ttip.y)**2)**0.5
                    
                    if l_pinch < 0.04:
                        if not clicked: pyautogui.click(button='left'); clicked = True
                    elif r_pinch < 0.04:
                        if not right_clicked: pyautogui.click(button='right'); right_clicked = True
                    else:
                        clicked = False; right_clicked = False
                
                else:
                    stealth_active = False; screenshot_taken = False

        # If running as .exe, you can comment out the imshow to make it truly "background"
        cv2.imshow('Gesture Pro', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()