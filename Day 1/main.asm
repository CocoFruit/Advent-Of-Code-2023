.386
.model flat, stdcall
option casemap :none

include \masm32\include\masm32rt.inc

includelib \masm32\lib\fileio.lib ; Include file I/O library

.data
    total dd 0
    lastNum dd 0
    FileName db "input.txt",0
    BufferSize equ 24576  ; size of input file
    Buffer db BufferSize dup(?)
    bytesRead dd ?
    errorMessage dd 1
    freq dd ?
.code

start:
    invoke CreateFile, addr FileName, GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL
    mov ebx, eax ; Save the file handle in ebx

    ; Check if the file was successfully opened
    cmp ebx, INVALID_HANDLE_VALUE
    je errorExit

    ; Read from the file
    invoke ReadFile, ebx, addr Buffer, BufferSize, addr bytesRead, NULL
    test eax, eax
    jz errorExit ; Check for errors during reading

    ; Process the contents of the file (in Buffer)
    lea esi, Buffer 

repeatLoop:
    movzx eax, byte ptr [esi] ; Load the current character into eax
    cmp eax, 10 ; if newline character            
    je newLine
    cmp eax, 26 ; end of file
    je endLoop             
    cmp eax, 0 ; end of file
    je endLoop    
    ; Test if the character is numeric
    cmp eax, '0'
    jl notNumeric
    cmp eax, '9'
    jg notNumeric

    sub eax, '0' ; go to regular decimal        

    ; if first number, mulitply it by 10 and add it to the total
    mov ecx, lastNum
    test ecx,ecx
    jnz notFirst
    mov lastNum, eax
    imul eax, 10
    add total, eax
    inc esi
    jmp repeatLoop

notFirst:
    mov lastNum, eax
    inc esi
    jmp repeatLoop

notNumeric:
    inc esi
    jmp repeatLoop

newLine:
    mov eax, lastNum
    add total, eax
    mov lastNum, 0 ; reset for next line
    inc esi
    jmp repeatLoop

endLoop:
    print str$(total),13,10,0
    invoke CloseHandle, ebx    ; Close the file
    invoke ExitProcess, 0

errorExit:
    print str$(errorMessage)
    invoke ExitProcess, 1

end start