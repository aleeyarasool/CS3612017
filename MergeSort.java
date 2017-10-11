import java.util.*;

public class MergeSort
{
	public static int[] mergeSort(int[] a, int[] b, int n)
	{
		int[] array = new int [8];
		int i = n/2;
		
		if(b.length >= a.length)
		{
			if(n%2 == 0)
			{
				if (i>a.length-1)
				{
					array[n] = b[i];
					mergeSort(a,b,n+1);
				}
				else
				{
					array[n] = a[i];
					mergeSort(a,b,n+1);
				}
			}
		}
		
		if(b.length<a.length)
		{
			if(n%2 ==0)
			{
				array[n] = a[i];
				mergeSort(a,b,n+1);
			}
			else
			{
				if(i>=b.length)
				{
					array[n] = a[i];
					mergeSort(a,b,n+1);
				}
				else
				{
					array[n] = b[i];
					mergeSort(a,b,n+1);
				}
			}
		}
		
		if(n > array.length-1)
		{
			return array;
		}
			return array;
	}
	
	public static void main(String[] args)
	{
		int[] a = {1,2,4,5};
		int[] b = {2,3,6,6};
		
		for(int i=0; i<7; i++)
		{
			mergeSort(a, b, i);
		}
		
		System.out.println(array);
	}
}
