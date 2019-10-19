/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package icecream;

/**
 *
 * @author Dode22
 */
public class Icecream {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
       // check open the file frist
        try{
            TextIO.readFile("icecream.dat");
            System.out.println("Opened!!");
        }
        // if the file don't exit
        
        catch(IllegalArgumentException e){
            System.out.println("Can't open file \"icecream.dat\" for reading!");
            System.out.println("Please make sure the file is present before");
            System.out.println("running the program.");
            System.exit(1);  // Terminates the program.

        
        }
        // lines in files
        String flavor;
        // count the strawberry
        double count_Stra;
        count_Stra =0;
        // count all lines or cones;
        double count_all;
        count_all =0;
        // percentage of strawberry;
        double perc_Stra;
        while(TextIO.eof()== false){
            // read the lines in the file;
            flavor = TextIO.getlnString();
            // check value of Strawberry in each lines;
            if (flavor.equals("Strawberry")) {
                // count the Strawberry in the files by increase 1
                count_Stra++;
            
            }
            // count all lines;
            count_all++;
            
        
        }
        perc_Stra = (count_Stra*100)/count_all;
        System.out.println("The total number of cones: "+" "+count_Stra);
        System.out.println("The number of Strawberry cones "+" "+count_all);
        System.out.println("The percentage of cones that were Strawberry "+" "+perc_Stra+"%");
    }
    
}
