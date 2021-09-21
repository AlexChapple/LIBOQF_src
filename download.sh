#!/bin/bash

source="N80"
mkdir results/$source

send_down () {
    scp mahuika:/nesi/project/uoa03404/work/$source/summary/$1 results/$source/$1
}

send_down spin_up_total.txt
send_down spin_down_total.txt 
send_down photon_counting_total.txt 
send_down waiting_time_total.txt
send_down input.txt