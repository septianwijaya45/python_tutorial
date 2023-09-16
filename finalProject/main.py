import os
import Controller as Controller

if __name__ == "__main__":
    sistemOperasi = os.name
    
    match sistemOperasi:
        case "posix": os.system("clear") # linux, mac
        case "nt": os.system("cls") # windows

    
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERUSAHAAN")
    print(30*"=")

    #check database ada atau Tidak
    Controller.init_console()

    #######################################################
    while True:

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")

        userInput = input("Masukkan Menu:\t")

        match userInput:
            case "1":
                print("READ DATA")
                Controller.readConsole()
            case "2":
                print("CREATE DATA")
                Controller.createConsole()
            case "3":
                print("UPDATE DATA")
                Controller.updateConsole()
            case "4":
                print("DELETE DATA")
                Controller.deleteConsole()

        isDone = input("Apakah Anda Ingin Menyelesaikan program (Y/N)? ")
        if isDone == "y" or isDone == "Y" or isDone == "yes" or isDone == "Yes":
            break
    print("Program Berakhir")