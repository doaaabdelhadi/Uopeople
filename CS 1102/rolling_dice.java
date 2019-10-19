/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rolling_dice;

/**
 *
 * @author Dode22
 */
public class Rolling_dice {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int die1;
        int die2 ;
        //snake eyes
        int i;
        int count;
        count=0;
        for(i =1;i < 1000;i++){

            die1 = (int)(Math.random()*6)+1;
            die2 = (int)(Math.random()*6)+1;
            
            if (die1==1 && die2 ==1){                
                count++;       
            }

        }
        float average;
        average =(float)count/1000;

        System.out.println("The precent of snake eyes from 1000 rollingis : "+ average);


       // TextIO.putln("snake"+Rolling_dice+"");
    }
    
}
