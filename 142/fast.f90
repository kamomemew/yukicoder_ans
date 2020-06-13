

program main
    implicit none
    integer N,S,X,Y,Z,Q
    integer i,j
    integer :: int_arr
    logical,allocatable :: arr(:)

    read *,N,S,X,Y,Z
    call mk_int_arr
    read *,Q
    do i = 1, Q
        call modify_arr
    end do

    do i = 1, N
        if ( arr(i) .eqv. .true. ) then
            write (*,fmt='(a)', advance='no'),"O"
        else
            write (*,fmt='(a)', advance='no'),"E"
        end if
    end do
    write (*,fmt='(a)') ""

contains
subroutine mk_int_arr
    implicit none
    integer i,prev
    logical mod2
    allocate(arr(N))
    prev = S
    arr(1) = mod(prev, 2) == 1
    do i = 1, N-1
        !write(*,*) prev
        prev = mod(X * prev + Y,Z)
        mod2 = mod(prev, 2) == 1
        arr(i+1) = mod2
    end do
    
end subroutine

subroutine modify_arr
    implicit none
    integer CPin1,CPin2,CPout1,CPout2
    integer i,j,length
    logical,allocatable :: mini_arr(:)
    read *,CPin1,CPin2,CPout1,CPout2
    length=CPin2-CPin1+1
    allocate(mini_arr(length))
    do i = 1, length
        mini_arr(i)=arr(CPin1+i-1)
    end do
    do j = 1, length
        arr(j+CPout1-1)=xor(arr(j+CPout1-1),mini_arr(j))
    end do
    !write (*,*) arr
end subroutine


end program  main
