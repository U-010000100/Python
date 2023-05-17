import time
FILE = input("Enter the main file name (*.html) = ")
PLAYLIST = input("Enter the playlist from URLi.e. links=<Playlist ID Here> : ")
OUT_FILE = input("Enter the name of the output file : ")
time.sleep(1)
with open(f"./{FILE}.html", "r") as file:
    content = "good"
    initial = 1
    line_number = 1
    while content!="":
        try:
            content = file.readline()
        except UnicodeDecodeError as error:
            print(f"Error in Decoding at line {line_number}")
            print("Detail :-")
            print(error)
        line_number += 1
        initial_number = content.find("https://music.youtube.com/watch?v=")
        if initial_number==-1:
            continue
        else:
            final_number = content.find(f"list={PLAYLIST}")
            if final_number==-1:
                continue
            else:
                if initial==1:
                    initial = 0
                    with open(F"./{OUT_FILE}.txt", "w") as link_file:
                        write_content = content[initial_number:final_number+len(PLAYLIST)+5]+"\n"
                        link_file.write(write_content)
                else:
                    with open(F"./{OUT_FILE}.txt", "a") as link_file:
                        write_content = content[initial_number:final_number+len(PLAYLIST)+5]+"\n"
                        link_file.write(write_content)
    else:
        print("Done Finding Links")
time.sleep(1)
print("Modifying Links.")
time.sleep(1)
content = "good"
with open(f"./{OUT_FILE}.txt", "r") as file:
    content = file.read()
    while (True):
        content = content.replace("&amp;", "&")
        if "&amp;" in content:
            continue
        else:
            break
with open(f"./{OUT_FILE}.txt", "w") as file:
    file.write(content)
print("Done")
time.sleep(1)
