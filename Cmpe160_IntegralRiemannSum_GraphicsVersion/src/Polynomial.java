
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.IllegalFormatFlagsException;
import java.util.spi.LocaleNameProvider;

import javax.sql.rowset.JoinRowSet;

public class Polynomial {
	
	private double deltaX = 0.0001;
	private ArrayList<Integer> coefficients = new ArrayList<Integer>();

	public Polynomial(String polynomial) {
		
		if (polynomial.charAt(0) == '-') 
			polynomial = polynomial + '+';
		else
			polynomial = '+' + polynomial + '+';
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
	}

	public double valueAt(double point) {
		return coefficients.get(4)*Math.pow(point, 4) + coefficients.get(3)*Math.pow(point, 3) + coefficients.get(2)*Math.pow(point, 2) + coefficients.get(1)*Math.pow(point, 1) + coefficients.get(0);
	}

	public void setDeltaX(double deltaX) {
		this.deltaX = deltaX;
	}


	public int computeIntegral(int min, int max) {
		double integration = 0;
		int n = (int) ((max - min) / deltaX);
		for (int k=0; k<n; k++)
			integration += valueAt(min + k*deltaX) * deltaX;
		return (int) integration;
	}
	
	public int coefficientOf(String polynomial, int i, int power) {
		int coefficient = 0;
		if (power != 0 && power != 1) {
			if (polynomial.charAt(i-4) == '+')
				coefficient = 1;
			else if (polynomial.charAt(i-4) == '-')
				coefficient = -1;
			else {
				int digit = 0;
				int index = i-4;
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



