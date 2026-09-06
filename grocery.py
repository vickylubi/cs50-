def main():
    grocery_list = {}
    

    while True: 
        try: 
            item = input("What do you want to buy? ").upper()
            if item not in grocery_list: 
                grocery_list[item] = 1
            else:  
                grocery_list[item] += 1
        except EOFError:
            print()
            break 
  
    sorted_list = sorted(grocery_list)  
    for key in sorted_list:
        print (f"{grocery_list[key]} {key} ")
        
if __name__ == "__main__":
    main()
    