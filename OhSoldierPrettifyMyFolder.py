import os
lst = []
def leavewords(filename):
    """
    this function is used for taking out all the words that will not be changed in the data you will modify
    """
    global lst
    lst = []
    with open(filename) as f:
        for a in f.readlines():
            if "\n" in a:
                a = a.split('\n')[0]
            else:
                pass
            lst.append(a)
#     return lst

def soldier(pathname, filen, *ext):
    """
    This function is to modify files in a directory. It can capitalise the first letters of you files. It
     can modify the data of a file by capitalising the first letters of words in a file.
     It can also rename your files of a specific format(extension)
    """
    try:
        # this a is storing a list of the words which you don not want to change and leave it as it is. It should be in your current directory in which you are running the python file.
        a = leavewords(filen)
        # this function is changing the directory where you want to modify your files and data.
        os.chdir(pathname)
        # this function is used to make a list of all folder and file names in a directory.
        all_things = os.listdir()
        # this loop is to create rename the first letter of all folders and files with first letter.
        for i in all_things:
            
            os.rename(i, f'{i[0].upper()}{i[1:len(i)]}')
        # print(all_things)
        # this loop is to rename the files with file extension of user input in a numerical order. 
        k = 1
        for j in all_things:
            filename, file_ext = os.path.splitext(j)
            if file_ext == ext[0]:
                filename = k
                os.rename(j, f"{filename}{file_ext}")
                k +=1
            else:
                pass
        # this loop is to modify the data of a text file. it capitalises the first letter of every word except of those refered by the user in a text file. 
        list1 = []
        for l in all_things:
            FileName,FileExt = os.path.splitext(l)
            if l == filen:
                pass
            elif FileExt == ".txt" and j != filen:
                f = open(l, "r+")
        
                text = f.read().split(" ")
                # print(text)
                for c in text:
                    if c not in a and c != "":
                        # this is the format to make the first letter capital. you can change this as you want.
                        c = f'{c[0].upper()}{c[1:len(c)]}'
            
                    else:
                        pass
                    # print(c)
                    list1.append(c)
                f.seek(0)
                f.truncate(0)
                for item in list1:
                    f.write(f'{item} ')
                list1.clear()
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    print("\t\t\t\t\t\t\tOH SOLDIER PRETTIFY MY FOLDER")
    user_path = input("Pls enter the path: ")
    user_refer = input("Pls enter the filename with which you want to modify the data of you rest text files.\nThe file you will input should have one word per line. This file should be in your current directory in which you are running program: ")
    user_format = input("Pls enter the format(extension) of the file of which you want to rename it in numerical order:  ")
    # there are print statements in the soldier function which are commented. you can un comment them for knowing how the function is working
    soldier(user_path, user_refer, user_format)
