/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int RangeSumBST(TreeNode root, int low, int high) {
        int sum = 0;

        if(root == null){
            return sum += 0;
        }

        //check root
        if(root.val >= low && root.val <= high){
            sum += root.val;
        }

        //loop through tree
        //search through left branch
        sum += RangeSumBST(root.left, low, high);

        //search through right branch
        sum += RangeSumBST(root.right, low, high);


        return sum;
    }
}