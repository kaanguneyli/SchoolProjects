
package question;


public class Main
{
	// Main method is for you to test your code
	// You will not get any points here
	public static void main(String[] args) {
		
		// Example:
		// Code that displays Fibonacci Series:
		String javaCode1 = "class Main {\r\n"
				+ "  public static void main(String[] args) {\r\n"
				+ "\r\n"
				+ "    int n = 10, firstTerm = 0, secondTerm = 1;\r\n"
				+ "    System.out.println(\"Fibonacci Series till \" + n + \" terms:\");\r\n"
				+ "\r\n"
				+ "    for (int i = 1; i <= n; ++i) {\r\n"
				+ "      System.out.print(firstTerm + \", \");\r\n"
				+ "\r\n"
				+ "      // compute the next term\r\n"
				+ "      int nextTerm = firstTerm + secondTerm;\r\n"
				+ "      firstTerm = secondTerm;\r\n"
				+ "      secondTerm = nextTerm;\r\n"
				+ "    }\r\n"
				+ "  }\r\n"
				+ "}";
		
		String javaCode2 = "print(\"Num (((even or odd): \")"
				+ "int num = reader.nextInt();"
				+ "if(num % 2 == 0)"
				+ "    println(num + \" {is even\");"
				+ "else"
				+ "    println(num + \" {is odd\");";
		
		String javaCode3 ="private static void waitForNextFrame() {\r\n"
				+ "			do {\r\n"
				+ "			{\r\n"
				+ "				deltaTime += System.currentTimeMillis() - previousTime;\r\n"
				+ "				previousTime = System.currentTimeMillis();\r\n"
				+ "				StdDraw.pause(1);\r\n"
				+ "			} while (deltaTime <= MS_PER_FRAME);\r\n"
				+ "\r\n"
				+ "			deltaTime -= MS_PER_FRAME;\r\n"
				+ "				}";
		
		String javaCode4 = "c='\u0030';"
				+ "a='(';"
				+ "s(\"'\")";
		
		String testCase1 = "c{\r\n"
				+ "  p(S[]s) {\r\n"
				+ "    i, f, s;\r\n"
				+ "    S(\"F\" + n + \"t\");\r\n"
				+ "    f(i) {\r\n"
				+ "      S(f + \", \");\r\n"
				+ "    }\r\n"
				+ "  }\r\n"
				+ "}";
						
		ParanthesisChecker checker = new ParanthesisChecker();
		System.out.println(checker.isCorrect(javaCode4));
		
	}

}

