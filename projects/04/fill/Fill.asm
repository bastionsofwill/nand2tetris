// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(LISTEN)
    @24576 
    D=M // Read keyboard input
    @WHITE
    D;JEQ // JMP to WHITE if keyboard input does not exists
    @BLACK
    D;JGT // JMP to BLACK if keyboard input exists
    @LISTEN
    0;JMP // (Not used) JMP to LISTEN if keyboard input is negative
(BLACK)
    @16384
    D=A // Screen memory map address(0x4000)
    @i
    M=D // M[i] = 0x4000
    (LOOPB)
        @24576
        D=M // Read keyboard input
        @WHITE
        D;JEQ // JMP to WHITE if keyboard input does not exists
        @i
        D=M // D = M[i]
        @24576
        D=D-A // D = M[i] - 0x6000
        @LISTEN
        D;JEQ // Break if M[i] = 0x6000
        @i
        A=M // A = M[i]        
        M=-1 // M[M[i]] = -1(Black)
        @i
        M=M+1 // M[i] += 1
        @LOOPB
        0;JMP
(WHITE)
    @16384
    D=A // Screen memory map address(0x4000) 
    @i
    M=D // M[i] = 0x4000
    (LOOPW)
        @24576
        D=M // Read keyboard input
        @BLACK
        D;JGT // JMP to BLACK if keyboard input exists
        @i
        D=M // D = M[i]
        @24576
        D=D-A // D = M[i] - 0x6000
        @LISTEN
        D;JEQ // Break if M[i] = 0x6000
        @i
        A=M // D = M[i]
        M=0 // M[M[i]] = 0(White)
        @i
        M=M+1 // M[i] += 1
        @LOOPW
        0;JMP
