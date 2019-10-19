/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package firstsubroutines;
import java.util.Scanner;
/**
 *
 * @author Dode22
 */
public class Firstsubroutines {

    /**
     * @param args the command line arguments
     */
   
    public static void main(String[] args) {
        // TODO code application logic here
       
        Scanner stdin = new Scanner( System.in );  // Create the Scanner.
        String word,stripped;
        
        System.out.println("Please Enter words:  ");
        // store user input
        word = stdin.nextLine();
        //call convert_str or stripped word!!
        stripped= convert_str(word);
        // call palindrome take parameter stripped!!
        System.out.println(palindrome(stripped));
        
        
    }
    static String convert_str(String user_input){
        String copy;
        copy =user_input.replaceAll("[^a-zA-Z]", "").toLowerCase();
        System.out.println("stripped:"+" "+copy);
        return(copy);
        
        }
    static String palindrome(String str) {
        String copy;  // The reversed copy.
        int i;        // One of the positions in str, 
                 //       from str.length() - 1 down to 0.
        copy = "";    // Start with an empty string.
        for ( i = str.length() - 1;  i >= 0;  i-- ) {
            // Append i-th char of str to copy.
              copy = copy + str.charAt(i);  
            }
        System.out.println("reversed:"+"  "+copy);
        if (str.equals(copy)){
            return("This IS a palindrome.");
        }
        else {
            
            return("This is NOT a palindrome.");    
        }
         //return copy;
    }
   
}
