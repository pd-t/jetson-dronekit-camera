import jetson.utils


class JetsonCamera:
    def __init__(
            self,
            camera_device: str
    ):
        self.video_input = jetson.utils.videoSource(camera_device)

    def capture(
            self,
            filename: str
    ):
        print(filename)
        img = self.video_input.Capture()
        #video_output = jetson.utils.videoOutput('file://' + filename)
        #video_output.Render(img)
