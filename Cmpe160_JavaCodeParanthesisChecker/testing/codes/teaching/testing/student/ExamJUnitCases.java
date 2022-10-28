package codes.teaching.testing.student;

import java.io.File;
import java.time.LocalDateTime;

import org.junit.FixMethodOrder;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TestName;
import org.junit.runners.MethodSorters;

import question.ParanthesisChecker;

/* TODO: Import the classes you need for testing */

// Tests will be sorted in lexicographical order. Therefore start the names as "test1_TestName" 
@FixMethodOrder(MethodSorters.NAME_ASCENDING)

//@RunWith(JUnit4.class)
public final class ExamJUnitCases extends ExamJUnit {

	//	private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
	//	private final ByteArrayOutputStream errContent = new ByteArrayOutputStream();
	//	private final PrintStream originalOut = System.out;
	//	private final PrintStream originalErr = System.err;

	public static String lineSeperator = System.lineSeparator();

	@Rule
	public TestName name = new TestName();

	@Test
	public void test1() {
		String inputForReport = "First Java Code";
		String expectedAnswer = "true";

		ExamJUnit.testInitialization(1, name.getMethodName(), inputForReport, expectedAnswer);
		try {
			String answerStudent = "";
			
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
			
			ParanthesisChecker checker = new ParanthesisChecker();
			boolean result = checker.isCorrect(javaCode1);
			
			answerStudent = Boolean.toString(result);
			ExamJUnit.testCheck(answerStudent);
		} catch (Exception e) {
			testFailedExecution(e);
		}
	}
	
	@Test
	public void test2() {
		String inputForReport = "Second Java Code";
		String expectedAnswer = "false";

		ExamJUnit.testInitialization(2, name.getMethodName(), inputForReport, expectedAnswer);
		try {
			String answerStudent = "";
			
			String javaCode2 = "public static void main(String[] args) {\r\n"
					+ "    \r\n"
					+ "    System.out.println(\"Enter two numbers\");\r\n"
					+ "    int first = 10;\r\n"
					+ "    int second = 20;\r\n"
					+ "    \r\n"
					+ "    System.out.println(first + \" \" + second));\r\n"
					+ "\r\n"
					+ "    // add two numbers\r\n"
					+ "    int sum = first + second;\r\n"
					+ "    System.out.println(\"The sum is: \" + sum);\r\n";
					
			
			ParanthesisChecker checker = new ParanthesisChecker();
			boolean result = checker.isCorrect(javaCode2);
			
			answerStudent = Boolean.toString(result);
			ExamJUnit.testCheck(answerStudent);
		} catch (Exception e) {
			testFailedExecution(e);
		}
	}
}
