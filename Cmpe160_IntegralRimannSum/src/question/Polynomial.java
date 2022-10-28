
package question;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.IllegalFormatFlagsException;
import java.util.spi.LocaleNameProvider;

import javax.sql.rowset.JoinRowSet;

public class Polynomial {
	
	private double deltaX = 0.0001;

	//Example solution:
	//Index 0: Coef. of x^0
	//Index 1: Coef. of x^1
	//Index 2: Coef. of x^2
	//Index 3: Coef. of x^3
	//Index 4: Coef. of x^4
	//If there is no x^n, that coefficient should be 0.

	private ArrayList<Integer> coefficients = new ArrayList<Integer>();

	//Fill in coefficients inside the constructor
	public Polynomial(String polynomial) {
		
		//DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
// WE ARE MAKING SURE THAT THE POLYNOMIAL HAS A SIGN AT THE BEGINNING AND AT THE END
		if (polynomial.charAt(0) == '-') 
			polynomial = polynomial + '+';
		else
			polynomial = '+' + polynomial + '+';
// WE ARE DECLARING THE POWER AS 0 AND AS WE INCREASE IT WE TAKE ITS COEFFICIENT WITH THE FUNCTION WE CREATE
// WE ARE USING SPECIFIED WAYS FOR 0TH AND 1ST POWERS
		int power = 0;
		for (int i=1; i<polynomial.length(); i++) {
			if (polynomial.charAt(i) == '+' || polynomial.charAt(i) == '-') {  
				if (polynomial.charAt(i-2) != '^' && polynomial.charAt(i-1) != 'x') {
					coefficients.add(coefficientOf(polynomial, i, power));
					power++;
					break;
				}
			}
		}
		for (int i=1; i<polynomial.length(); i++) {
			if (polynomial.charAt(i) == '+' || polynomial.charAt(i) == '-') {
				if (i != 0) {
					if (polynomial.charAt(i-2) == '^') {
						int currentPower = Character.getNumericValue(polynomial.charAt(i-1));
						if (currentPower == power) {
							coefficients.add(coefficientOf(polynomial, i, power));
							power++;
							i = 1;
						} 
					} else if (polynomial.charAt(i-1) == 'x' && power == 1) {
						coefficients.add(coefficientOf(polynomial, i, power));
						power++;
						i = 1;
					} else if (i == polynomial.length()-1) {
						coefficients.add(0);
						power++;
						i = 1;
					}
				if (coefficients.size() == 5)
					break;
				}
			}
		}
		//DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
	}

	public double valueAt(double point) {
		
		//DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
		return coefficients.get(4)*Math.pow(point, 4) + coefficients.get(3)*Math.pow(point, 3) + coefficients.get(2)*Math.pow(point, 2) + coefficients.get(1)*Math.pow(point, 1) + coefficients.get(0);
		//DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
	}

	public void setDeltaX(double deltaX) {
		
		//DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
		this.deltaX = deltaX;
		//DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
	}


	public int computeIntegral(int min, int max) {
		
		double integration = 0;
		
		//DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
// WE CALCULATE THE NUMBER OF INTERVALS AND THEN WE CALCULATE THE AREAS
		int n = (int) ((max - min) / deltaX);
		for (int k=0; k<n; k++)
			integration += valueAt(min + k*deltaX) * deltaX;
		//DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
		
		return (int) integration;
	}
	/*
	 * Takes the coefficient from an item
	 * @param polynomial The polynomial as a string
	 * @param i Has to be the i value in the for loop above.
	 * 			Helps us to keep track of indexes
	 * @param power The power of the item we are working on.
	 * 				We need this as parameter because there 
	 * 				are separate ways for each power.
	 */
	public int coefficientOf(String polynomial, int i, int power) {
		int coefficient = 0;
		if (power != 0 && power != 1) {
// IF THERE IS NO NUMBER BEFORE X WE DIRECTLY ASSIGN 1
			if (polynomial.charAt(i-4) == '+')
				coefficient = 1;
			else if (polynomial.charAt(i-4) == '-')
				coefficient = -1;
			else {
				int digit = 0;
				int index = i-4;
// WE TAKE THE VALUES AND MULTIPLY THEM WITH INCREASING POWERS OF 10 UNTIL WE SEE A SIGN
				while (!(polynomial.charAt(index) == '-') && !(polynomial.charAt(index) == '+')) {
					int num = Character.getNumericValue(polynomial.charAt(index));
					int pow = (int) Math.pow(10, digit);
					coefficient += num * pow;
					digit++;
					index--;
					if (polynomial.charAt(index) == '-')
						coefficient *= -1;
				}
			}
		} else {
// IF THE POWER IS 1 OR 0 WE DO SAME THING BUT WE USE DIFFERENT INDEXES
			int digit = 0;
			int index;
			if (power == 0)
				index = i-1;
			else
				index = i-2;
			while (!(polynomial.charAt(index) == '-') && !(polynomial.charAt(index) == '+')) {
				int num = Character.getNumericValue(polynomial.charAt(index));
				int pow = (int) Math.pow(10, digit);
				coefficient += num * pow;
				digit++;
				index--;
				if (polynomial.charAt(index) == '-')
					coefficient *= -1;
			}
			if (power == 1 && coefficient == 0)
				coefficient = 1;
		}
		return coefficient;
		}
}



