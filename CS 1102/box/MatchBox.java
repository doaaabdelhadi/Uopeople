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
public class MatchBox extends Box {
    double weight;
    //@SuppressWarnings("empty-statement")
    MatchBox() {
        ;
      }
    MatchBox(double w,double h, double d,double wt) {
        super(w ,h ,d);
        weight = wt;
          
   }

    
    @Override
    void getVolume() {
                
        System.out.println("width of MatchBox is  "+ width);
        System.out.println("height of MatchBox is  "+ height);
        System.out.println("depth of MatchBox is  "+ depth);
        System.out.println("weight of MatchBox is  " + weight);
        System.out.println("Volume is : " + width * height * depth);
   }
    
    void calculateWeight(){
        //wight = getVolume() /.03611  ;
        weight = (width * height * depth) * 0.03611;

        System.out.println("weight of MatchBox is  " +weight);
    }
}
