! Simulation of the quantum system using quantum trajectories and the SDW model. 
! This is the HEAD file. 
! 
! Author: Alex Chapple 

program main

    ! ----------------------------------------------------------------------------------
    ! 
    ! This runs the simulation, and writes to separate files the spin statistics,
    ! photon counting distribution, and more. 
    ! 
    ! Waiting time distribution has been removed, and emission tracking has been added. 
    ! Waiting time distribution will be calculated in post. 
    !
    ! ----------------------------------------------------------------------------------

    implicit none 

    ! Declare general variables and parameters
    real (kind=8) :: start_time = 0.0d0 
    integer (kind=8), parameter :: N = 20d0 
    integer (kind=8), parameter :: end_time = 100d0 
    integer (kind=8), parameter :: time_steps = 50000d0  
    integer (kind=8), parameter :: num_of_simulations = 100d0
    real (kind=8), parameter :: pi = 3.14159265358979323846d0
    real (kind=8), parameter :: phase = 0  
    real (kind=8), parameter :: gammaL = 0.5d0 
    real (kind=8), parameter :: gammaR = 0.5d0
    real (kind=8), parameter :: Omega = 10.0d0 * pi 
    real (kind=8), parameter :: dt = 0.002d0 
    integer (kind=8), parameter :: period = 1d0 
    real (kind=8), parameter :: tau = 0.2d0 
    real (kind=8) :: total
    integer (kind=8) :: sim, index, q, j, k, beginning, end, rate, log_line, index1, index2
    real (kind=8), dimension(time_steps) :: time_list, rand_list
    complex (kind=8) :: lambdaL, lambdaR
    complex (kind=8), parameter :: i = cmplx(0.0d0,1.0d0) 
    
    ! The coefficients (g for ground, u for up)
    complex (kind=8) :: g_0, g_0_new, e_0 ,e_0_new
    complex (kind=8), dimension(N) :: g_1, g_1_new, e_1, e_1_new 
    complex (kind=8), dimension(N,N) :: g_2, g_2_new, e_2 ,e_2_new 
    real (kind=8) :: psi_0, psi_1, prob, rand_num, spin_up_prob, spin_down_prob, spin_total ! spin_total is just the total probability of spin up and down for normalisation purposes 

    ! g2 plots 
    real (kind=8), dimension(time_steps) :: g2, avg_e 
    complex (kind=8) :: p_up_now, p_up_0


    ! -------------------------------------------------------------------
    !
    ! START PROGRAM
    !
    ! -------------------------------------------------------------------

    ! Print initial stuff into console 
    call print_info(tau, period, dt, num_of_simulations, Omega, end_time, &
                            time_steps, phase, gammaL, gammaR, N)

    ! Program execution time tracking 
    call system_clock(beginning, rate)

    ! Construct time_list
    call linspace(start=start_time, end=end_time, list=time_list) ! This makes the time list 

    ! Initialise lambdaL and lambdaR
    lambdaL = exp(cmplx(0, phase / 2)) * sqrt(gammaL) * sqrt(N/tau)
    lambdaR = exp(cmplx(0, -phase / 2)) * sqrt(gammaR) * sqrt(N/tau)

    ! Initialise g2 
    g2 = 0.0d0 ; avg_e = 0.0d0 

    call initialise_arrays(N, g_0, g_0_new, e_0 , e_0_new, g_1, g_1_new,&
                                 e_1 ,e_1_new, g_2, g_2_new, e_2, e_2_new)

    ! A do loop will go through and do the simulations here
    do sim = 1, num_of_simulations

        total = modulo_func(g_0)**2 + modulo_func(e_0)**2 
        do j = 1,N 
            total = total + modulo_func(g_1(j))**2 + modulo_func(e_1(j))**2 
        end do 
        do j = 1,N 
            do k = 1,N 
                total = total + modulo_func(g_2(j,k))**2 + modulo_func(g_2(j,k))**2 
            end do
        end do 

        g_0 = g_0 / total; e_0 = e_0 / total
        g_1= g_1 / total; e_1 = e_1 / total
        g_2 = g_2 / total; e_2 = e_2 / total

        p_up_0 = modulo_func(e_0)**2 
        do j = 1,N
            p_up_0 = p_up_0 + modulo_func(e_1(j))**2 
        end do 

        do j = 1,N
            do k = 1,N 
                p_up_0 = p_up_0 + modulo_func(e_2(j,k))**2 
            end do 
        end do 

        ! Initialise arrays
        call initialise_arrays(N, g_0, g_0_new, e_0 , e_0_new, g_1, g_1_new,&
                                 e_1 ,e_1_new, g_2, g_2_new, e_2, e_2_new)

        ! Construct random number list 
        call random_number(rand_list)

        do index = 1, size(time_list)

            psi_0 = 0.0d0; psi_1 = 0.0d0; prob = 0.0d0; rand_num = 0.0d0; spin_up_prob = 0.0d0; 
            spin_down_prob = 0.0d0; spin_total = 0.0d0; total = 0.0d0

            ! -------------------------------------------------------------------
            !
            ! Performs Euler's method
            !
            ! -------------------------------------------------------------------

            ! Initialises the new variables
            g_0_new = 0.0d0; e_0_new = 0.0d0; g_1_new = 0.0d0; 
            e_1_new = 0.0d0; g_2_new = 0.0d0; e_2_new = 0.0d0

            ! Calculates new values using Euler's method 
            g_0_new = g_0_new + ((-i) * (Omega/2) * e_0)

            e_0_new = e_0_new + ((-i)*(((Omega/2)*g_0))) + ((-i)*lambdaL*g_1(1)) + ((-i)*lambdaR*g_1(N))

            g_1_new(1) = g_1_new(1) + ((-i) * (lambdaL * e_0))

            g_1_new(N) = g_1_new(N) + ((-i) * (lambdaR * e_0))

            do j = 1,N 
                g_1_new(j) = g_1_new(j) + ((-i)*(Omega/2)*e_1(j))
            end do 

            do j = 1,N 
                e_1_new(j) = e_1_new(j) + ((-i)*(Omega/2)*g_1(j))
            end do 

            do k = 2,N 
                e_1_new(k) = e_1_new(k) + ((-i)*lambdaL*g_2(1,k))
            end do 

            do j = 1,N-1 
                e_1_new(j) = e_1_new(j) + ((-i)*lambdaR*g_2(j,N))
            end do 

            do j = 1,N-1 
                do k = j+1,N 
                    g_2_new(j,k) = g_2_new(j,k) + ((-i)*(Omega/2)*e_2(j,k))
                end do 
            end do 

            do j = 2,N 
                g_2_new(1,j) = g_2_new(1,j) + ((-i)*lambdaL*e_1(j))
            end do 

            do j = 1,N-1 
                g_2_new(j,N) = g_2_new(j,N) + ((-i)*lambdaR*e_1(j))
            end do 

            do j = 1, N-1 
                do k = j+1, N 
                    e_2_new(j,k) = e_2_new(j,k) + ((-i)*(Omega/2)*g_2(j,k))
                end do 
            end do 

            ! Changed to euler method for now 
            g_0_new = g_0 + (dt*g_0_new)
            e_0_new = e_0 + (dt*e_0_new)
            g_1_new = g_1 + (dt*g_1_new)
            e_1_new = e_1 + (dt*e_1_new) 
            g_2_new = g_2 + (dt*g_2_new) 
            e_2_new = e_2 + (dt*e_2_new)

            ! Check photon 
            if (mod(index, period) == 0) then 

                ! Do statistics here 
                psi_0 = (modulo_func(g_0_new)**2) + (modulo_func(e_0_new)**2)

                do j = 1,(N-1) 
                    psi_0 = psi_0 + (modulo_func(g_1_new(j))**2) + (modulo_func(e_1_new(j))**2)
                end do 

                do j = 1,(N-2)
                    do k = (j+1),(N-1) 
                        psi_0 = psi_0 + (modulo_func(g_2_new(j,k))**2) + (modulo_func(e_2_new(j,k))**2)
                    end do 
                end do 

                psi_1 = (modulo_func(g_1_new(N))**2) + (modulo_func(e_1_new(N))**2)

                do j = 1,(N-1)
                    psi_1 = psi_1 + (modulo_func(g_2_new(j,N))**2) + (modulo_func(e_2_new(j,N))**2)
                end do 

                prob = psi_1 / (psi_1 + psi_0)
                
                ! Grab a random number from a pre existing list of random numbers
                rand_num = rand_list(index)

                ! Check if photon is in the Nth box
                if (rand_num <= prob) then ! Photon found

                    g_0 = g_1_new(N) 
                    e_0 = e_1_new(N)

                    g_1(1) = 0.0d0 
                    e_1(1) = 0.0d0 

                    do j = 2,N 
                        g_1(j) = g_2_new(j-1,N)
                        e_1(j) = e_2_new(j-1,N)
                    end do 

                    do j = 1, N-1 
                        do k = j+1, N 
                            g_2(j,k) = 0.0d0 
                            e_2(j,k) = 0.0d0
                        end do 
                    end do 


                
                else ! Photon not found 
                    
                    g_0 = g_0_new
                    e_0 = e_0_new 

                    g_1(1) = 0.0d0 
                    e_1(1) = 0.0d0 

                    do j = 2,N 
                        g_1(j) = g_1_new(j-1)
                        e_1(j) = e_1_new(j-1)
                    end do 

                    do k = 2,N 
                        g_2(1,k) = 0.0d0  
                        e_2(1,k) = 0.0d0 
                    end do  

                    do j = 2,(N-1)
                        do k = (j+1),N 
                            g_2(j,k) = g_2_new(j-1, k-1)
                            e_2(j,k) = e_2_new(j-1, k-1)
                        end do 
                    end do 



                end if 

            else ! It's not a multiple of the period
                ! In this case we just update it with Runge-Kutta 

                g_0 = g_0_new 
                e_0 = e_0_new
                g_1 = g_1_new 
                e_1 = e_1_new
                g_2 = g_2_new 
                e_2 = e_2_new 

            end if 

            total = modulo_func(g_0)**2 + modulo_func(e_0)**2 
            do j = 1,N 
                total = total + modulo_func(g_1(j))**2 + modulo_func(e_1(j))**2 
            end do 
            do j = 1,N 
                do k = 1,N 
                    total = total + modulo_func(g_2(j,k))**2 + modulo_func(g_2(j,k))**2 
                end do
            end do 

            g_0 = g_0 / total; e_0 = e_0 / total
            g_1= g_1 / total; e_1 = e_1 / total
            g_2 = g_2 / total; e_2 = e_2 / total


            total = modulo_func(g_0)**2 + modulo_func(e_0)**2 
            do j = 1,N 
                total = total + modulo_func(g_1(j))**2 + modulo_func(e_1(j))**2 
            end do 
            do j = 1,N-1 
                do k = j+1,N 
                    total = total + modulo_func(g_2(j,k))**2 + modulo_func(g_2(j,k))**2 
                end do
            end do 

            if (sim == 1) then 
                print *, total 
            end if 

            p_up_now = modulo_func(e_0)**2 
            do j = 1,N
                p_up_now = p_up_now + modulo_func(e_1(j))**2 
            end do 
            do j = 1,N
                do k = 1,N 
                    p_up_now = p_up_now + modulo_func(e_2(j,k))**2 
                end do 
            end do 

            g2(index) = g2(index) + (p_up_0 * p_up_now)
            avg_e(index) = avg_e(index) + p_up_now


        end do 

        ! Prints simulation completeion to terminal 
        if (end_time >= 15) then 
            ! print *, "photon count: ", photon_number
            print *, sim ,' simulations completed.'
        else
            if (mod(sim, 10) == 0) then 
                print *, sim ,' simulations completed.'
            end if     
        end if 

    end do 

    g2 = g2 / num_of_simulations
    avg_e = avg_e / num_of_simulations

    !!! Write out final result to a txt file
    open(1, file="results_g2/g2.txt", status="replace")
    open(2, file="results_g2/avg_e.txt", status="replace")

    do index = 1,size(time_list)
        write(1, *) time_list(index), g2(index)
        write(2, *) time_list(index), avg_e(index)
    end do 

    
    
    call system_clock(end)

    print *, "All simulations completed. Execution time: ", real(end - beginning) / real(rate), " seconds."

    ! -------------------------------------------------------------------------------------------
    ! 
    !   Functions and Subroutines 
    !
    !-------------------------------------------------------------------------------------------
    
    contains

    subroutine linspace(start, end, list) 

        real (kind=8), intent(in) :: start
        integer (kind=8), intent(in) :: end 
        real (kind=8), intent(out) :: list(:)
        real (kind=8) :: range
        integer (kind=8) :: p, q

        p = size(list)
        range = end - start
        
        do q = 1,p
            list(q) = start + (range * (q - 1) / (p - 1))
        end do

    end subroutine

    function modulo_func(z) result(c)

        ! Takes in a complex number z and returns its modulus

        implicit none

        ! Declare var types
        real (kind=8) :: a, b, c
        complex (kind=8), intent(in) :: z

        a = real(z)
        b = aimag(z)

        c = sqrt(a**2 + b**2)

    end function 

    subroutine initialise_arrays(N, g_0, g_0_new, e_0 , e_0_new, g_1, &
                                 g_1_new, e_1 ,e_1_new, g_2, g_2_new, e_2, &
                                e_2_new)

        ! This stores the initial condition of the simulations

        ! Declare types 
        integer (kind=8) :: N
        complex (kind=8) :: g_0, g_0_new, e_0 ,e_0_new
        complex (kind=8), dimension(N) :: g_1, g_1_new, e_1 ,e_1_new 
        complex (kind=8), dimension(N,N) :: g_2, g_2_new, e_2 , e_2_new 

        g_0 = 1.0d0; g_0_new = 0.0d0
        e_0 = 0.0d0; e_0_new = 0.0d0

        g_1 = 0.0d0; g_1_new = 0.0d0
        e_1 = 0.0d0; e_1_new = 0.0d0

        g_2 = 0.0d0; g_2_new = 0.0d0
        e_2 = 0.0d0; e_2_new = 0.0d0

    end subroutine

    subroutine print_info(tau, period, dt, num_of_simulations, Omega, end_time, &
                            time_steps, phase, gammaL, gammaR, N)

        integer (kind=8) :: N, end_time, time_steps, num_of_simulations, period
        real (kind=8) :: phase, gammaL, gammaR, dt, tau, Omega

        print *, "Number of Boxes: ", N 
        print *, "simulation duration: ", end_time 
        print *, "time steps: ", time_steps
        print *, "number of simulations: ", num_of_simulations
        print *, "phase: ", phase 
        print *, "gammaL: ", gammaL 
        print *, "gammaR: ", gammaR 
        print *, "Omega: ", real(Omega)
        print *, "dt: ", dt 
        print *, "tau: ", tau 
        print *, "period: ", period 
        print *, "Delta t: ", tau / N 

        ! Also will write this to an input.txt file 
        open(5, file="input.txt", status="replace")

        write (5,*) "Number of Boxes: ", N 
        write (5,*) "simulation duration: ", end_time 
        write (5,*) "time steps: ", time_steps
        write (5,*) "number of simulations: ", num_of_simulations
        write (5,*) "phase: ", phase 
        write (5,*) "gammaL: ", gammaL 
        write (5,*) "gammaR: ", gammaR 
        write (5,*) "Omega: ", real(Omega)
        write (5,*) "dt: ", dt 
        write (5,*) "tau: ", tau 
        write (5,*) "period: ", period 
        write (5,*) "Delta t: ", tau / N 

        close(5)

    end subroutine

end program main 



