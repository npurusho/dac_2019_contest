# DAC 2019 Design Contest

For general questions regarding this contest, please contact Jeff Goeders <jgoeders@byu.edu>.

## Setup PYNQ on your Ultra96 board

  * Download the board image from http://www.pynq.io/board.html
  * Follow the instructions to image the SD card at https://pynq.readthedocs.io/en/latest/getting_started/pynq_image.html.  
  * Follow the instructions to setup and connect to the board at https://ultra96-pynq.readthedocs.io/en/latest/getting_started.html.

## Quick Start

Open a terminal on your PYNQ board and run:

```
sudo pip3 install --upgrade git+https://github.com/npurusho/dac_2019_contest.git
```

Currently this repository is compatible with [PYNQ image v2.3](http://www.pynq.io/board).

## Usage
The get started, users have to run the following command on the Ultra96 board:

```shell
cd /home/xilinx/jupyter_notebooks
sudo git clone https://github.com/jgoeders/dac_2019_contest.git
```
Remember the user name and password are both `xilinx` for super user.

After the above step is completed successfully, you will see a folder `dac_2019_contest` under your 
jupyter notebook dashboard.  Open the `pynquser/dac_contest.ipynb` notebook for directions on where to begin.

## Folder Structure

1. overlay: This folder stores the overlay needed for the design. Usually it includes <teamname>.bit and <teamname>.tcl.

2. images: All the test images are stored in this folder.

3. python: This folder contains the python classes needed for the design, as well as the example notebook(s).

4. result: The results includes the coordinates of the resized pictures and the frame rate of each picture.


