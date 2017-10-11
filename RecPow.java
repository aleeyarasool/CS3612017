import java.util.Scanner;

public class RecPow
{
	public static int recPow(int n)
	{
		if(n == 0)
			return 1;
		else
			return 2 * recPow(n-1);
	}
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Enter a value: "); 
		int n = scan.nextInt();
		 
			System.out.println(recPow(n));
	}	
}
