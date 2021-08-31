public class Solution {
    public string DefangIPaddr(string address) {
        address = address.Replace(".", "[.]");

        return address;
    }
}