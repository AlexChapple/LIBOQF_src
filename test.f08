! program main 

!     implicit none 

!     real, dimension(5) :: list_of_emissions 
!     real, dimension(20) :: waiting_list 
!     real, parameter :: bin_width = 0.5 
!     real :: current_time, last_time
!     integer :: i, value 

!     waiting_list = 0

!     list_of_emissions(1) = 0.3
!     list_of_emissions(2) = 0.4
!     list_of_emissions(3) = 5.2
!     list_of_emissions(4) = 6.4
!     list_of_emissions(5) = 6.5

!     do i = 1,5

!         if (i == 1) then 
!             last_time = list_of_emissions(1)
!         else
        
!             current_time = list_of_emissions(i) - last_time

!             value = floor(current_time / bin_width)

!             waiting_list(value + 1) = waiting_list(value + 1) + 1

!             last_time = current_time

!             print *, value, current_time

!         end if 

!     end do 

!     do i = 1,20
!         print *, i, waiting_list(i)
!     end do 


! end program main 

program main 

    implicit none
    
    real (kind=8), dimension(2) :: a 

    a = 0 

    print *, a 

    if (a(1) == 0d0) then 
        print *, "same"
    end if 

end program 