import os 
def creation_carpet(name):
    try:
        os.mkdir(name)
        print(f"The directory {name} is created sucessfully")
    except FileExistsError:
        print(f"The directory {name} exists")
def creation_file(name,archive,extension):
    name_archive_extension = f"{archive}.{extension}"
    path = os.path.join(name,name_archive_extension)
    try:
        with open(path, "x") as f:
            f.write("")
        print(f"The archive {name_archive_extension} is created in {name}")
    except FileExistsError:
        print(f"Error the file exits")
def rename_carpet(new_name , old_carpet):
    try:
        os.rename(old_carpet,new_name)
        print(f"The directory {old_carpet} has rename ----> {new_name}")
    except FileNotFoundError:
        print("Error: The directory not exist")
    except FileExistsError:
        print("Error: The directory already exist")
def delete_carpet(name_carpet):
    try:
        os.rmdir(name_carpet)
        print(f"The directory {name_carpet} has deleted.")
    except FileNotFoundError:
        print(f"The directory {name_carpet} does not exist ")
    except OSError:
        print(f"The directory {name_carpet} is not empty or cannot be deleted")
def main():
    try:    
        while True:
            print("|--------------------|")
            print("|[1] Creation carpet |")
            print("|[2] Create file     |")
            print("|[3] Rename Carpet   |")
            print("|[4] Delete carpet   |")
            print("|[5] Exit            |")
            print("----------------------")
            option = int(input(">"))
            if option == 1:
                name = input("Enter the name of the carpet ->")
                creation_carpet(name)
            elif option == 2:
                name = input("Enter the name of the carpet ->")
                archive = input("Enter the name of the archive ->")
                extend = input("Enter the extend archive ->")
                decision = input("Deseas escribir algo ?")
                if(decision.lower=="si"):
                    pass
                else:
                    creation_file(name,archive,extend)
            elif option == 3:
                old_name = input("Enter the old name ->")
                new_name = input("Enter the new name ->")
                rename_carpet(new_name,old_name)
            elif option == 4:
                name_carpet = input("Enter the name of the carpet ->")
                if(delete_carpet(name_carpet)):
                    pass
                else:
                    pass
            elif option == 5:
                print("Exit........")
                break
    except ValueError:
        print("Error: You must be enter a number (1-5).")
    except Exception as e:
        print(f"Unexpected error : {e}")
if __name__ == "__main__":
    main()
