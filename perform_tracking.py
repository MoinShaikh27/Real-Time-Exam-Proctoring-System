import cv2
from gaze_tracking import GazeTracking


class TrackEyes:
    frames_check = 5

    def __int__(self):
        self.frame_pos = 0
        self.prev_states = ["center"] * self.frames_check

    def eye_based_snooping_detect(self, human_frame):
        gaze.refresh(human_frame)
        new_frame = gaze.annotated_frame()

        if gaze.is_right():
            curr_state = "right"
        elif gaze.is_left():
            curr_state = "left"
        else:
            curr_state = "center"

        self.prev_states[self.frame_pos] = curr_state
        self.frame_pos = (self.frame_pos + 1) % self.frames_check

        unique_ele = set(self.prev_states)
        if len(unique_ele) == 1 and (unique_ele[0] in ["right", "left"]):
            # Snooping for more than a certain period of time - reset the object and return
            self.frame_pos = 0
            self.prev_states = ["center"] * self.frames_check

            return True

        return False
