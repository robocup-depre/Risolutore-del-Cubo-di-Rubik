# Rubik's Cube Solver

An automated, hardware-accelerated Rubik's Cube solver powered by a Python computer vision pipeline and an ATmega2560 microcontroller driving a 3D-printed, 6-axis stepper motor chassis. 

The machine interfaces directly with each face of the cube via a dedicated stepper motor attached to the center caps. It executes 180° rotations, as well as 90° clockwise and counterclockwise turns.

---

# Hardware Architecture & Electronics

The `Arduino/` folder contains the C++ firmware required for the microcontroller. While an Arduino Mega was used for this build, the footprint is small enough to run on an Arduino Uno as well. The system relies on **9 logical pins**:

* **Relay Control (1 Pin):** Engages or disengages the main 12V battery line. This isolates the stepper drivers when idling to eliminate motor humming and vibration.
* **Direction Line - DIR (1 Pin):** Sets the rotational direction (clockwise/counterclockwise). This line is shared globally across all stepper drivers.
* **Step Line - STEP (1 Pin):** Sends the pulse train to drive the motor steps. This line is also shared globally.
* **Enable Lines - EN1 to EN6 (6 Pins):** Individual driver enables. Because `STEP` and `DIR` are wired in parallel to all six drivers, the firmware pulls only one `EN` line low at any given instant to ensure that exactly one target motor executes the move.

The firmware listens continuously to the serial bus for instruction sets sent by the PC. Upon receiving a move command, it instantly pulses the active motor and relays an execution feedback signal back to the Python script.

> [!IMPORTANT]
> Before flashing the firmware, review the pin configuration constants at the top of the sketch file and adjust them to match your physical hardware mapping.

---

# Software & Computer Vision Pipeline

The `Python/` directory contains four modular scripts. The execution pipeline is handled through `main.py`, which initializes a Graphical User Interface (GUI) via `tkinter`.

### 1. Optical Scanning & AprilTags
Instead of using easily skewed raw color histograms, this system tracks **AprilTags** to robustly locate and identify faces under changing lighting conditions. 
* Click the first GUI button to begin scanning. 
* Follow the orientation sequence specified in `scanning_order.gif`. 
* The script triggers an audible tone upon every successful capture, signaling you to rotate the cube to the next designated position.
* **Caution:** Maintain the exact face orientations shown in the guide; scanning a face upside-down will invalidate the internal virtual cube mapping.

### 2. Move Sequence Calculation
Once the scan concludes, a 2D projection of the cube will render on-screen for validation. If correct, clicking the second button calculates the optimized algorithm sequence. 
* *Note:* The GUI will temporarily hang/freeze during the solving computation. Do not interact with the window until it completes.

### 3. Execution
Mount the cube inside the chassis mechanism as demonstrated in `insertion.gif`. Click the final button to open the serial pipe, flashing the move sequence directly to the microcontroller array.

---

# Dependencies & Prerequisites

### 3D Printing & Assembly
* The `3D Print/` folder contains the `.stl` assets. The original chassis components were drafted in Autodesk Fusion 360 and fabricated on a Sisma Everes Uno DLP system.
* Print **9 copies of each AprilTag** provided in the `AprilTag/` directory. Glue them cleanly to their corresponding color tiles on the cube.
* Mounting the rig onto a hollow wooden base is highly recommended to cleanly route wire looms and isolate the relay.

### Core Software Requirements
| Dependency | Purpose | Notes |
| :--- | :--- | :--- |
| **Python 3.8+** | Core runtime environment | Ensure it is added to your system PATH. |
| **OpenCV** | Hardware video capture pipeline  |
| **pupil_apriltags**| Tag localization and ID extraction | Required for the computer vision tracking loop. |
| **NumPy** | Array manipulations & mapping | Handles matrix transforms of the virtual cube space. |
| **Tkinter** | Native GUI framework | Standard library component. |
| **Winsound** | Audio capture queues | Windows native (requires alternative library on Linux/macOS). |
| **CH340/ATmega Driver** | USB-to-Serial communications bridge | Necessary if your OS fails to discover the COM port mapping. |

---

# Power Delivery Specifications

The electronics run on an isolated dual-rail configuration:
* **Logic Rail:** The Arduino board is bus-powered directly through the USB host serial cable. No external step-downs or buck converters are needed.
* **Motor Rail:** A high-discharge **12V Battery** is required to drive the stepper array. 

> [!WARNING]
> Ensure all heavy-gauge power distribution lines originating from the battery terminal are properly sized. Each active stepper motor can pull a peak current of **2A** under load.
