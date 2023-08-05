import cv2
import tkinter as tk
import function_module as fm


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.handRecognizer = fm.HandGestureRecognizer()
        self.poseRecognizer = fm.PoseGestureRecognizer()
        self.create_widgets()

    def stream_window(self):
        if (self.url_inp.get() == ""):
            cap = cv2.VideoCapture(0)
        else:
            cap = cv2.VideoCapture("http://"+self.url_inp.get()+"/video")

        framePrev = cv2.flip(cap.read()[1], 1)
        while True:
            ret, frame = cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                # frame = self.poseRecognizer.findPosition(frame)
                self.poseRecognizer.slideControl(framePrev, frame)
                self.poseRecognizer.volumeControl(framePrev, frame)
                # self.handRecognizer.gestureControl()
                cv2.imshow('Frame', frame)
                framePrev = frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        return None

    def initialize(self):
        cap = cv2.VideoCapture(0)
        frame = cv2.flip(cap.read()[1], 1)
        self.handRecognizer.initialize(frame)
        self.poseRecognizer.initialize(frame)
        return None

    def create_widgets(self):
        self.url_inp_label = tk.Label(self, text="Enter stream URL:")
        self.url_inp_label.grid(row=1, column=0, padx=10, pady=10)
        self.url_inp = tk.Entry(self)
        self.url_inp.grid(row=1, column=1, padx=10, pady=10)

        self.stream_button = tk.Button(
            self, text="Stream", command=lambda: self.stream_window())
        self.stream_button.grid(row=2, column=0, padx=5, pady=10)

        self.initialize_button = tk.Button(
            self, text="Initialize", command=lambda: self.initialize())
        self.initialize_button.grid(row=2, column=1, padx=5, pady=10)

        return None

    def stop(self):
        self.status = 0
        return None


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(master=root)
    app.mainloop()
