package codes.teaching.testing.student;

import org.junit.FixMethodOrder;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TestName;
import org.junit.runners.MethodSorters;

import question.CityNavigator;

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
	public void test1_findPath1() {
		String inputForReport = "ShortestPathFinder.pathFinder('A', 'Z');";
		String expectedAnswer = "6";

		ExamJUnit.testInitialization(1, name.getMethodName(), inputForReport, expectedAnswer);
		try {
			int answerStudent = CityNavigator.pathFinder("A", "Z");
			ExamJUnit.testCheck(String.valueOf(answerStudent));
		} catch (Exception e) {
			testFailedExecution(e);
		}
	}
	
	@Test
	public void test2_findPath2() {
		String inputForReport = "ShortestPathFinder.pathFinder('A', 'J');";
		String expectedAnswer = "0";

		ExamJUnit.testInitialization(1, name.getMethodName(), inputForReport, expectedAnswer);
		try {
			int answerStudent = CityNavigator.pathFinder("A", "J");
			ExamJUnit.testCheck(String.valueOf(answerStudent));
		} catch (Exception e) {
			testFailedExecution(e);
		}
	}
	
	@Test
	public void test3_findPath3() {
		String inputForReport = "ShortestPathFinder.pathFinder('B', 'L');";
		String expectedAnswer = "9";

		ExamJUnit.testInitialization(1, name.getMethodName(), inputForReport, expectedAnswer);
		try {
			int answerStudent = CityNavigator.pathFinder("B", "L");
			ExamJUnit.testCheck(String.valueOf(answerStudent));
		} catch (Exception e) {
			testFailedExecution(e);
		}
	}
}
