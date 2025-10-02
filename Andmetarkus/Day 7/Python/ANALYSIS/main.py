
def main():
    file_path = r"C:\Users\opilane\Desktop\Andmetarkus,git\Andmetarkus\Python\ANALYSIS\request-log.txt"

    # filecontent = ""

    # with open(file_path, "a") as f:
    #     f.write("4. Neljas")

    # with open(file_path) as f:
    #     filecontent = f.read()

    # request_log_entries = filecontent.split('\n')   

    for line in request_log_entries:
        print(line + '\n')

   
    
    row_count = len(request_log_entries)

    print(f"Logifailis on  {row_count} rida.")
    

if __name__ == "__main__":
    main()