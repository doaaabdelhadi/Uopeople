/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package statcalc;

/**
 *
 * @author Dode22
 */
public class StatCalc {

    /**
     * @param args the command line arguments
     */
    private int count;   // Number of numbers that have been entered.
   private double sum;  // The sum of all the items that have been entered.
   private double squareSum;  // The sum of the squares of all the items.
 
   /**
    * Add a number to the dataset.  The statistics will be computed for all
    * the numbers that have been added to the dataset using this method.
    */
   public void enter(double num) {
          count++;
          sum += num;
          squareSum += num*num;
   }
      /**
    * Return the number of items that have been entered into the dataset.
    */
   public int getCount() {
          return count;
   }
 
   /**
    * Return the sum of all the numbers that have been entered.
    */
   public double getSum() {
          return sum;
   }
 
   /**
    * Return the average of all the items that have been entered.
    * The return value is Double.NaN if no numbers have been entered.
   */
   public double getMean() {
          return sum / count;
   }
 
   /**
    * Return the standard deviation of all the items that have been entered.
    * The return value is Double.NaN if no numbers have been entered.
    */
   public double getStandardDeviation() {
          double mean = getMean();
          return Math.sqrt( squareSum/count - mean*mean );
   }         

    public static void main(String[] args) {
        // TODO code application logic here
        StatCalc myStatCalc;
        myStatCalc = new StatCalc();
        int[] numbers ={5, 7, 12, 23, 3, 2, 8, 14, 10, 5, 9, 13};
        for (int i : numbers) {
          myStatCalc.enter(i);  
          
        }
        System.out.println("Count: "+" "+myStatCalc.getCount());
        System.out.println("Mean: "+" "+myStatCalc.getMean());
        //double SD;
        //SD =;
        System.out.println("SD: "+" "+myStatCalc.getStandardDeviation());
        
        

    }
    
}
