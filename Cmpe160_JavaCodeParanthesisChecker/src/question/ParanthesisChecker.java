
package question;

/**
 * Checks whether the parentheses of the code are true or not
 * @author Bilge Kaan Güneyli
 * */
public class ParanthesisChecker {
	
	
	public boolean isCorrect(String javaCode) { 
		
		//DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
		MyStack myStack = new MyStack();
		// isString and isChar show whether we are in a string/char or not
		boolean isString = false;
		boolean isChar = false;
		int fullStack = 4;
		int charCount = 0;
		for (int i=0; i<javaCode.length(); i++) {
			char item = javaCode.charAt(i);
			// if we are in a string or char we don't check the inside, when we face " or ' we switch isString or isChar to false again
			if (!isChar & isString) {
				if (item == '"') {
					// when we face " there is a possibility that it might be a part of the string
					// to handle that we check the number of \'s before the "
					// if the number is even, " is not part of the string, if the number is odd " is in the string
					int slashCount = 0;
					int prevItemIndex = i-1;
					while (javaCode.charAt(prevItemIndex) == '\\') {
						slashCount += 1;
						prevItemIndex--;
					} if (slashCount % 2 == 1) {
					continue;
					} else {
					isString = false;
					}
				} 
				continue;
			} else if (!isString & isChar) {
				charCount++;
				// if we face a char, we stop searching for parentheses for 2 characters because this characters will be the the char and closing '
				if (charCount == 2) {
					charCount = 0;
					isChar = false;
					continue;
				}
			} else if (isString == false || isChar == false) {
				if (item == '"') {
					isString = true;
				} else if (item == '\'') {
					isChar = true;
					
					
				// when we face an opening bracket we push it to the stack, if the stack is full we resize it
				} else if (item == '{' || item == '(') {
					if (myStack.size() == fullStack) {
						fullStack *= 2;
						myStack.resize();
					}
					myStack.push(item);
					
					
					// if we face a closing bracket we check whether it matches the last bracket or not
					// if the brackets don't match, we return false
				} else if (item == '}') {
					if (myStack.pop() != '{') {
						return false;
					}
				} else if (item == ')') {
					if (myStack.pop() != '(') {
						return false;
					}
				}
			}
		}
		// if we reach the end, we check whether the stack is empty or not
		// if it's empty we return true, else we return false
		if (myStack.isEmpty()) {
			return true;
		} else {
			return false;
		}
		//DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
		
	}
	
}


