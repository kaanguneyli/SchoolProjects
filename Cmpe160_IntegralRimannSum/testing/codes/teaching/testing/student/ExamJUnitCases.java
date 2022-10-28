package codes.teaching.testing.student;

import java.io.File;
import java.time.LocalDateTime;

import org.junit.FixMethodOrder;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TestName;
import org.junit.runners.MethodSorters;

import question.Polynomial;

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
		String inputForReport = "-x^2+x^3-3x+5, deltaX = 0.0001, range = 5,10";
		String expectedAnswer = "1964";

		ExamJUnit.testInitialization(1, name.getMethodName(), inputForReport, expectedAnswer);
		try {
			String answerStudent = "";
			
			Polynomial poly = new Polynomial("x^3-x^2-3x+5");
			poly.setDeltaX(0.0001);
			int result = poly.computeIntegral(5, 10);
			
			
			answerStudent = Integer.toString(result);
			ExamJUnit.testCheck(answerStudent);
		} catch (Exception e) {
			testFailedExecution(e);
		}
	}
	
	@Test
	public void test2() {
		String inputForReport = "0, deltaX = 0.0001, range = 5,10";
		String expectedAnswer = "0";

		ExamJUnit.testInitialization(1, name.getMethodName(), inputForReport, expectedAnswer);
		try {
			String answerStudent = "";
			
			Polynomial poly = new Polynomial("0");
			poly.setDeltaX(0.0001);
			int result = poly.computeIntegral(5, 10);
			
			
			answerStudent = Integer.toString(result);
			ExamJUnit.testCheck(answerStudent);
		} catch (Exception e) {
			testFailedExecution(e);
		}
	}
}
