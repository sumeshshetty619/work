import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        //String a="";
        StringBuilder a = new StringBuilder(""); 
        int f=k;
        //String n="";
        // Complete the function
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        // 'largest' must be the lexicographically largest substring of length 'k'
        for (int i=0;i<=s.length();i++)
        {
            if((i+f)!=s.length())
            {
            for(int m=i;m<k;m++)
            {
                char n=s.charAt(m);
                //String r=Character.toString(n);
                 a=a.append(n);
            }
             a=a.append("\t");
            k=k+1;
            }
            else{
                break;
            }
        }
        String g=a.toString();
        System.out.println(a);
        //System.out.println(a);
        //smallest=g;
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}