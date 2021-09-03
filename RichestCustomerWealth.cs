public class Solution {
    public int MaximumWealth(int[][] accounts) {

        var richestCustomer = 0;
        var temp = 0;

        //loop through inputted accounts array
         //add up each customers wealth [inner array]
        for(int i = 0; i < accounts.Length; i++){
            for(int j = 0; j < accounts[i].Length; j++){
                temp += accounts[i][j];
            }
            Console.WriteLine($"Temp {temp}");
            if(temp > richestCustomer){
                richestCustomer = temp;
                temp = 0;
            }else{
                temp = 0;
            }
            Console.WriteLine($"Rich Customer {richestCustomer}");
        }

       //return sum of wealthiest customer

        return richestCustomer;
    }
}