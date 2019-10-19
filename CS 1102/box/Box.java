/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package box;

/**
 *
 * @author Dode22
 */
public class Box {

    /**
     * @param args the command line arguments
     */
   
    
    double width;
   double height;
   double depth;
 
   // This is an empty constructor
   Box() {
          ;
   }
 
   Box(double w, double h, double d) {
          width = w;
          height = h;
          depth = d;
   }
 
   void getVolume() {
          System.out.println("Volume is : " + width * height * depth);
   }
    
}
