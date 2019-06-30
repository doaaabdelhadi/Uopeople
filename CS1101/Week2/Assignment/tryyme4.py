#define new_line function to print one line.
def new_line():
    print('.')
    
#define three_lines function to print three lines from the new line function.
def three_lines():
    #call the new_line function
    new_line()
    new_line()
    new_line()
    
#define nine_lines function to print nine lines from the three_lines function.
          
def nine_lines():
    #call the three_lines function
    three_lines()
    three_lines()
    three_lines()
#define clear_screen function to print twenty-five lines from the three_lines function and nine_lines.

def clear_screen():
    #call the nine_lines function
    nine_lines()
    nine_lines()
    #call the three_lines function
    three_lines()
    three_lines()
    #call the new_line function
    new_line()
          
#call clear_screen to display.          
clear_screen()          

