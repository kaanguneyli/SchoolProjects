
package question;

import java.util.Arrays;

/*
 * creates a stack from an array
 * @author Bilge Kaan Güneyli
 */

public class MyStack{
	
	private Character[] a; // array of items
	
	//DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
	public MyStack() {
		a = new Character[4];
	}
	
	/*
	 * returns a boolean showing that whether the stack is empty or not
	 */
	public boolean isEmpty() {
		if (a[0] == null)
			return true;
		return false;
	}
	
	/*
	 * @return the size of the stack
	 */
	public int size() {
		int count = 0;
		for (int i=0; i<a.length; i++) {
			if (a[i] != null) {
				count++;
			} else {
				break;
			}
		}
		return count;
	}
	
	/*
	 * doubles the size of the stack
	 */
	public void resize() {
		int size = a.length;
		// we put the old items in a temporary array, then we transfer them to new stack
		Character[] temp = new Character[size];
		for (int i=0; i<size; i++)
			temp[i] = a[i];
		a = new Character [size*2];
		for (int i=0; i<size; i++)
			a[i] = temp[i];
	}
	
	/*
	 * pushes the item to the stack
	 * @param item
	 */
	public void push(char item) {
		for (int i=0; i<a.length; i++) {
			if (a[i] == null) {
				a[i] = item;
				break;
			}
		}
	}
	
	/*
	 * returns the last item in the stack and removes it
	 * @return the last item in the stack (if the stack is empty, returns empty character)
	 */
	public Character pop() {
		for(int i=a.length-1; i>-1; i--) {
			if (a[i] != null) {
				Character item = a[i];
				a[i] = null;
				return item;
			}
		}
		return ' ';
	}
	
	/*
	 * @return the last item in the stack (if the stack is empty, returns empty character)
	 */
	public Character peek() {
		for(int i= a.length-1; i>-1; i--) {
			if (a[0] != null) {	
				if (a[i] != null) { 
					return a[i];
				}
			} else
				break;
		}
		return ' ';
	}
	//DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
	
}

