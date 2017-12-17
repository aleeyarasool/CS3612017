/**
 * @author Christelle
 * 
 */
import java.io.*;
import java.util.*;
public class ScannerDemo {

	private static String file = "prog2.jay";  //change this file path for each file run
	private static int counter = 1;

	public static void main(String args[]) throws Exception {

		TokenStream ts = new TokenStream(file);

		Token t;

		while (!ts.isEndofFile()) {
			t = ts.nextToken();
			t.toString();
			System.out.println("Token " + counter + " - " + t);
			counter  = counter+1;
		}
	}
}
