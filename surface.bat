@echo off
cd export/
for /L %%i in (0,1,9) do (
    setlocal enabledelayedexpansion
    set "id=000%%i"
    if %%i GEQ 10 set "id=00%%i"
    if %%i GEQ 100 set "id=0%%i"
    if %%i GEQ 1000 set "id=%%i"

    echo Processing sim_!id!
    cd sim_!id!
    mkdir surface
    splashsurf reconstruct vtk/ParticleData_Fluid_{}.vtk -r=0.025 -l=2.0 -c=0.5 -t=0.6 -o=surface/surfaceData_{}.obj --mesh-smoothing-weights=on --mesh-smoothing-iters=15 --normals=on --normals-smoothing-iters=10
    cd ..
    endlocal
)
cd ..