! ------------------------------------------------------------------------------------------------
!
!   Emission tracking 
!
! ------------------------------------------------------------------------------------------------

program main 

    implicit none
    
    integer (kind=16), parameter :: file_length = 3000 !791425 ! Needs to be manually specified 
    real (kind=16), dimension(file_length) :: emission_data 
    integer (kind=16), dimension(30) :: emission_count_list 

    ! Simulation parameters 
    real (kind=16), parameter :: tau = 0.2d0 
    real (kind=16), parameter :: end_time = 100.0d0

    ! temporary parameters 
    integer (kind=16) :: session_count, index 
    real (kind=16) :: session_start_time, waiting_time 

    !!! ----- Program starts here -------------------------

    ! Read the data in 
    open(1, file="results/N80_phi_pi/emission_tracking_total.txt", status="old")

    do index = 1,file_length
        read(1,*) emission_data(index)
        
        if (mod(index, 10000) == 0) then 
            print *, "index ", index, " has been read."
        end if 

    end do 

    session_count = 0d0 
    session_start_time = 0.0d0 

    emission_count_list = 0d0 

    do index = 1, file_length

        if (session_start_time == 0.0d0) then 

            session_start_time = emission_data(index)
            session_count = session_count + 1d0 

        else

            if (emission_data(index) == (end_time + 50.0d0)) then 

                emission_count_list(session_count) = emission_count_list(session_count) + 1
                session_count = 0d0 
                session_start_time = 0.0d0 

            else 

                waiting_time = emission_data(index) - session_start_time

                if (waiting_time <= tau) then 

                    session_count = session_count + 1 

                else 

                    emission_count_list(session_count) = emission_count_list(session_count) + 1

                    session_count = 0 
                    session_start_time = emission_data(index)

                end if 

            end if


        end if 

        
        ! Makes sure the last data point gets stored 
        if (index == file_length) then 
            emission_count_list(session_count) = emission_count_list(session_count) + 1
        end if 

        ! Prints out progress 
        ! if (mod(index, 1000) == 0) then 
        !     print *, "index ", index, " has been processed."
        ! end if 
        print *, index

    end do 

    ! Writes data to a textfile to be plotted with python later 
    open(2, file="results/N80_phi_pi/emission_tracking_processed.txt", status="replace")

    do index = 1, size(emission_count_list)

        write(2,*) emission_count_list(index)

    end do 
























end program main 