from gaze_tracking import GazeTracking

gaze = GazeTracking()


class TrackEyes:
    frames_check = 2

    def __init__(self):
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

        print(self.prev_states)

        self.prev_states[self.frame_pos] = curr_state
        print(self.frame_pos)
        self.frame_pos = (self.frame_pos + 1) % self.frames_check

        if "center" not in self.prev_states:
            # Snooping for more than a certain period of time - reset the object and return
            self.frame_pos = 0
            self.prev_states = ["center"] * self.frames_check

            return True

        return False
