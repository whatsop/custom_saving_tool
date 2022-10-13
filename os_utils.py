import os

def make_txt_file(path, file_name, content_file):
    # check if file does not already exits
    new_file = path + "/" + file_name + "_saving_logs.txt"
    
    if not os.path.exists(new_file):
        try:
            with open(new_file, 'a') as f:
                f.write(content_file)
        except:
            print("please check again your arguments!")
        finally:
            print("File has been created!")
    else:
        print("File already exists!")
        
# make_txt_file("D:/", "temP-test1.txt", "hello test")
    
    

