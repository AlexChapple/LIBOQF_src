#!/bin/bash

destination="N80"

send_up () {
    scp -r template/$1 mahuika:/nesi/project/uoa03404/work/$destination/$1
}

send_up_Little_Boxes_Large () {
    scp Little_Boxes_Large.f08 mahuika:/nesi/project/uoa03404/work/$destination/Little_Boxes_Large.f08
}

send_up python_scripts
send_up summarise.run 
send_up run_simulations.sh 
send_up LIBOQF_array.run 
send_up initialise.run 
send_up_Little_Boxes_Large
