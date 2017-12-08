import java.util.Scanner;
import java.util.*;

public class TailRecursion 
{
	public static int gcd(int a, int b)
	{
		if(b == 0)
			return a;
		else
			return gcd(b, a%b);
	}
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Enter a value: "); 
		int a = scan.nextInt();
		
		System.out.print("Enter a value: "); 
		int b = scan.nextInt();
	}
}
