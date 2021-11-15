#!/bin/bash

source="Omega_10_tau_01_phi_0"
mkdir results/$source

send_down () {
    scp mahuika:/nesi/project/uoa03404/work/$source/summary/$1 results/$source/$1
}

send_down spin_up_total.txt
send_down spin_down_total.txt 
send_down photon_counting_total.txt 
send_down emission_tracking_total.txt
send_down input.txt