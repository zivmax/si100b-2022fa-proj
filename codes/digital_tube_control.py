import RPi.GPIO as GPIO
import time


def main():

    check()

    display0()

    display1()

    display2()

    display3()

    display4()

    display5()

    display6()

    display7()

    display8()

    display9()


def setup():

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(VCC, GPIO.OUT)
    GPIO.setup(A, GPIO.OUT)
    GPIO.setup(B, GPIO.OUT)
    GPIO.setup(C, GPIO.OUT)
    GPIO.setup(D, GPIO.OUT)
    GPIO.setup(E, GPIO.OUT)
    GPIO.setup(F, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)
    GPIO.setup(DP, GPIO.OUT)


def refresh(t = 0):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, False)
    GPIO.output(A, True)
    GPIO.output(B, True)
    GPIO.output(C, True)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    



def check(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, False)

    time.sleep(t)

    GPIO.cleanup()
    



def display0(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, True)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    


def display1(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    


def display2(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, True)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, True)
    GPIO.output(G, False)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    



def display3(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, False)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    



def display4(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, True)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    



def display5(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    



def display6(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, False)
    GPIO.output(B, True)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    



def display7(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, True)
    GPIO.output(E, True)
    GPIO.output(F, True)
    GPIO.output(G, True)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    



def display8(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, False)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()
    



def display9(t = 1):

    VCC = 32
    A = 11
    B = 12
    C = 13
    D = 15
    E = 16
    F = 18
    G = 29
    DP = 22

    setup()

    GPIO.output(VCC, True)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)
    GPIO.output(E, True)
    GPIO.output(F, False)
    GPIO.output(G, False)
    GPIO.output(DP, True)

    time.sleep(t)

    GPIO.cleanup()


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()