// return pairs of x and y next to each other in array
public class Solution {
    public int[] Shuffle(int[] nums, int n) {
        // List<int> xArray = new List<int>();
        // List<int> yArray = new List<int>();
        int[] xArray = new int[2*n];
        int[] yArray = new int[2*n];

        //split array based on n value
        xArray = nums.Take(nums.Length/2).ToArray();
        yArray = nums.Skip(nums.Length/2).ToArray();

        var tempX = xArray.ToList();
        var tempY = yArray.ToList();

        //create new array
        int[] finalArray = new int[0];
        var tempFinal = finalArray.ToList();

        //add in one from each array to new array
        for(int i=0; i < (n); i++){
            tempFinal.Add(xArray[i]);
            tempFinal.Add(yArray[i]);
        }

        finalArray = tempFinal.ToArray();
        return finalArray;
    }
}