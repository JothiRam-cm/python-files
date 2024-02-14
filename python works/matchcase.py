while True:
    x=int(input("Enter a number to Match || 0 t0 exit : "))
    match x :
        case 0 :
            print("code-exited") 
            exit()
        case 1 :
            print("matches 1")
        case 2 :
            print("matches 2")
        case 3 :
            print("matches 3")
        case 4 :
            print("matches 4")    
        case 5 :
            print("matches 5")     
        case _:
            print("matches DEFAULT")    
    