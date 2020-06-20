#tie together unrelated tuple and arbitrary argument list
#to perform file input adn output
import os as os
#write function write_to_file()
def write_to_file(*args):
    # accepts tuple to be added to the end of file
    # open student_info.txt for appending
    try:
        with open('student_info.txt', 'a') as f:
            f.write(str(args) + "\n") #write typle on one line
            f.close() #close file
    except IOError:
        print("Cannot openfile on file system")

#write function get_student_info()
def get_student_info():
    student_name = input("Enter student name: ")
    score_list = []
    score = 0
    #accepts kwarg for student name
    #prompts user to input as many test scores
    sentinel = -99
    while score != sentinel:
        try:
            score = int(input("Enter number between 0 and 100, or -99 to stop"))
            if 0 <= score <= 100 and score != -99:
                score_list.append(score)
            elif score < 0 or score > 100 and score != -99:
                print("Number not in range")
        except ValueError:
            print("input must be number")
            raise ValueError
    #stores name and ascore in tuple
    #call function write_to_file()
    write_to_file(student_name, score_list)
    #send typle to be written to the end of the file

#write function read_from_file()
def read_from_file():
    file_dir = os.path.dirname(__file__)
    file_name = "student_info.txt"
    f = open(os.path.join(file_dir, file_name), "r")
    line = f.read(300)
    print(line)
    f.close()
    #read file line by line
    #print each line to console

if __name__ == '__main__':
    #call get_student_info() for 4 different students
    #call read_from_file()
    #include input("Press any key to end")
    get_student_info()
    read_from_file()
    get_student_info()
    read_from_file()
    get_student_info()
    read_from_file()
    get_student_info()
    read_from_file()
    print("Press any key to end")
