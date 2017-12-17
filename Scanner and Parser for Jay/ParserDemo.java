public class ParserDemo
{
	private static String file = "C:\\Users\\Aleeya\\workspace\\ParserScannerOriginal\\src\\prog2.jay";  //change this file path for each file run

	public static void main(String[] args)
	{
		
		TokenStream tStream = new TokenStream(file);
		System.out.println("test1");
		ConcreteSyntax cSyntax = new ConcreteSyntax(tStream);
		System.out.println("test2");
		Program p = cSyntax.program();
		System.out.println(p.display());
		System.out.println("test");
	}

}
