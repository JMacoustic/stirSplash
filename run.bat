@echo off

REM ====== Setup ======
pip install pandas pysplishsplash meshio pysplashsurf trimesh vessl pillow

REM Download Blender
REM curl -L -o blender.zip https://download.blender.org/release/Blender4.3/blender-4.3.2-windows-x64.zip
REM tar -xf blender.zip

REM Install Python packages using Blender’s Python
REM cd blender-4.3.2-windows-x64\4.3\python\bin
REM python.exe -m ensurepip --upgrade
REM python.exe -m pip install meshio numpy fileseq
REM cd ..\..\..\..

REM DOWNLOAD ADDONS
REM curl -L -o sequence_loader.zip https://github.com/InteractiveComputerGraphics/blender-sequence-loader/archive/refs/tags/v0.3.4.zip
REM tar -xf sequence_loader.zip
REM move blender-sequence-loader-0.3.4 blender-4.3.2-windows-x64\4.3\scripts\addons_core\sequence_loader

REM Cleanup
REM del blender.zip
REM del sequence_loader.zip

REM ====== VTK Builder (80 sec per file) ======
REM python jeeljil.py --start 1 --interval 0
REM python jeeljil.py --start 5 --interval 3

REM python jeeljil.py --start 9 --interval 3
REM python jeeljil.py --start 13 --interval 3
REM python jeeljil.py --start 17 --interval 3
REM python jeeljil.py --start 21 --interval 3
REM python jeeljil.py --start 25 --interval 3
REM python jeeljil.py --start 29 --interval 3
REM python jeeljil.py --start 33 --interval 3
REM python jeeljil.py --start 37 --interval 3
REM python jeeljil.py --start 41 --interval 4
REM python jeeljil.py --start 45 --interval 4

REM ====== Mesh Builder ======
REM python surface.py

REM ====== Headless Render ======
REM conda create -y -n py37_env python=3.7
REM call conda activate py37_env
REM python --version
REM pip install bpy 

REM Loop through all folders in obj
for /D %%F in ("%~dp0final_mesh\*") do (
    echo [JOB] %%F -> videos\%%~nxF.mp4
    call blender-4.3.2-windows-x64\blender.exe -b --python renderbase.py -- "%%F" "%~dp0videos" "%%~nxF.mp4"
)
@REM vessl configure
@REM vessl storage copy-file .\videos volume://vessl-storage/sph-videos
@REM vessl storage copy-file .\configs volume://vessl-storage/sph-configs