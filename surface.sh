#!/bin/bash

cd export/
for i in $(seq 0 9); do
    id=$(printf "%04d" $i)

    echo "Processing sim_$id"
    cd sim_$id || continue
    mkdir -p surface
    splashsurf reconstruct vtk/ParticleData_Fluid_$id.vtk -r=0.025 -l=2.0 -c=0.5 -t=0.6 -o=surface/surfaceData_$id.obj --mesh-smoothing-weights=on --mesh-smoothing-iters=15 --normals=on --normals-smoothing-iters=10
    cd ..
done
cd ..