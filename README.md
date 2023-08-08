# 🙋🏻PPT Gesture Control

#### 📑Tasks
* Come up with some natural non-awkward hand movement to control the interface ✅
* Code it (MediaPipe Solution by Google)
  * Gesture to key mapping for: up, down, right, left, enter... ✅
  * Volume control ✅
* Setup a stream to the code through IP Webcam ✅
  * On the stage, a smartphone camera would stream on IP Webcam. The host PC would be on same network and would get the stream data thereby.
* Test and optimize sensitivity and feasibility on stage.
  * We need the API to be low latency and to suppress false moves.
* Integrate simple tkinter gui ✅
* Multithreading for various actions to boost performance

#### 🛠️Setup
```
Windows
1. python -m venv ppt_control_env
2. ppt_control_env\Scripts\activate
3. pip install -r requirements.txt
4. python app.py
5. deactivate
```
```
Linux
1. python3 -m venv ppt_control_env
2. source ppt_control_env/bin/activate
3. pip install -r requirements.txt
4. python3 app.py
5. deactivate
```

#### 📦Final Packaging
```
$> pip freeze > requirements.txt
$> pyinstaller --onefile --windowed <i>filename</i>.py
```

#### 📚Resources
> [MediaPipe Solutions](https://developers.google.com/mediapipe/solutions/guide)<br>
> [PyAutoGui](https://pypi.org/project/PyAutoGUI/#:~:text=PyAutoGUI%20is%20a%20cross%2Dplatform,https%3A%2F%2Fpyautogui.readthedocs.org)<br>
> [Tkinter](https://docs.python.org/3/library/tkinter.html)<br>
> [Threading](https://docs.python.org/3/library/threading.html)

#### 🧑🏻‍🎓Contributors
* U Skanda Aithal<br>
* Swaminathan S K

#### 🛂Contribution Guidelines
1. Standard linting and formatting practices to be followed
2. Implement good object oriented programming

```
File Structure
~/ ----> ppt-control/
          |----> venv/
          |        |----> ...  
          |
          |----> Script/
                   |----> __init__.py
                   |----> function_module.py
                   |----> GUI.py
                   |----> app.py
```

#### 🎶Notes
* Some initial unstructured, not so well designed files have been dumped into the repository which work (They are of TRS itself and not from internet). They are for shear understanding of the general implementation logic and not a development model for us. Refrain from following similar structuring.  
* Communicate any concerns and enhancements with the maintainers.

***
## Technology Robotix Society | Indian Institute of Technology Kharagpur | 2023
