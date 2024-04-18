.386
.model flat, stdcall
option casemap :none

include \masm32\include\kernel32.inc 
include \masm32\include\masm32.inc 
includelib \masm32\lib\kernel32.lib
includelib \masm32\lib\masm32.lib

; label instruction operands [;comment]

; BYTE = 1 byte = 8 bits
; WORD = 2 bytes = 16 bits
; DWORD = 4 bytes = 32 bits

; MOV a, b = move value of b to a

; LEA reg, mem = place address of mem in reg (pointer)
; example:  lea eax, var1 ; eax = address of var1

; Jump instructions:
;   JMP = unconditional jump
;   JZ = jump if zero
;   ...

; Declare variables
; db = declare byte
; dw = declare word
; dd = declare dword
; example: 
; var db "Hello, World!", 0 ; declare string with null terminator
; arr dd 1, 2, 3, 4, 5 ; declare array of dwords
; unarr dd 5 DUP(?) ; declare uninitialized array of 5 dwords

.data
    message db "Hello, World!", 0

.code

start:
    push offset message
    call StdOut

end start
