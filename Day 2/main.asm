.386
.model flat, stdcall
option casemap :none

include \masm32\include\windows.inc
include \masm32\include\kernel32.inc 
include \masm32\include\msvcrt.inc
include \masm32\include\masm32.inc 
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\masm32.lib

.data

red db 12
green db 13
blue db 14
lineInput db "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",0
curChar db ?,13,10,0

.code

start:
    lea esi, lineInput
    mov ecx, 0 ; counter for loop

loop_through_line:
    ; al = current char in line
    mov al, [esi+ecx]
    cmp al,0
    je end_loop

    mov curChar, al

    inc ecx
    jmp loop_through_line

end_loop:
    invoke StdOut, offset curChar
    invoke ExitProcess, 0

end start
