Conda
=====
 
SCALT is written in python, R and bash programming language. To ensure the versatility accross different operating systems, SCALT requires the installation of a **Conda** environment. Conda is a powerful command line tool for package and environment management that runs on Windows, macOS, and Linux.

To install Conda and set up the SCALT envirnoment, follow the following steps.

Conda Installer download
========================

Open your favorite brwoser and visit the `Anaconda distribution page <https://www.anaconda.com/download>`_ and download the appropiate version of Conda depending on your operating system and version. 

Alternativelly, you can dowload the installer directly from the command line using the **wget** command and inserting the link to the installer script from the Anaconda distribution page as follows:

::

  wget https://repo.anaconda.com/archive/[installer script]

In the following example, the download of the Conda installer for MacOS is reported.

::

  wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-MacOSX-x86_64.sh
  
Conda installation
==================

After having downloaded the installer, open the terminal and navigate towards the directory where the installer was downloaded using the **cd** command as follows:

::

  cd path/to/the/directory

Then, run the installer using the following command specifying the name of the installer:

::

  bash [installer script]

In the following commnda, the installation of the installer for MacOS is proposed as example:


::

  bash Anaconda3-2023.09-0-MacOSX-x86_64.sh


During the installation, follow the instructions on the terminal and agree to the terms and conditions. After accepting the *terms and conditions*, select the directory to install Anaconda or press **Enter** to accept the default location and allow the installer to initialize Conda by appending the installation location to your system PATH.

At this point, the installation should be concluded. However, you may need to restart the terminal or use the **source** command to update your settings:

::

  source ~/.bashrc

Additionallly, to verify that Conda was properly installed, type the following command:

::

  conda list

This command should display a list of installed packages if Conda is set up correctly.

SCALT download
==============

Subsequent to the installation of Conda, make sure that conda is activated with the following command:

::

  conda activate

THEN, SCALT can be downloaded from the following `Github repository <https://github.com/danitrave/SCALT>`_ as a zipped file or directly using the following command:

::

  git clone https://github.com/danitrave/SCALT.git


Move to the SCALT directory making use of **cd** command as follows:

::

  cd path/to/directory/SCALT

Inside the directory the configuartion file **SCALT_conda_envSetup.yml** enables the installation of the proper SCALT environment in which all the packages and programs required by the tool are provided. To properly install the envirnoment, run the following command:

::

  conda env create -f SCALT_conda_envSetup.yml

Finally, make sure to activate the environment if not already activated using the following commad:

::

  conda activate SCALT

Now, you are ready to play with SCALT.

