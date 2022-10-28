
import java.awt.Font;
import java.util.ArrayList;
import java.util.Arrays;

import javax.print.attribute.SupportedValuesAttribute;

public class Main
{
	public static void main(String[] args) {
		
		Polynomial p1 = new Polynomial("-7x^4+5x-10+3x^2+6x^3");
		double deltaX = 0.0001;
		p1.setDeltaX(deltaX);
		int min = 4;
		int max = 7;
		int result = p1.computeIntegral(min, max);
		System.out.println(result);
		
		StdDraw.setCanvasSize(600, 500);
		StdDraw.setXscale(-10, 10);
		StdDraw.setYscale(-12, 50);

		StdDraw.setPenColor(StdDraw.BLACK);
		StdDraw.setPenRadius(0.01);
		StdDraw.line(-9, 0, 9, 0); // x axis
		StdDraw.line(8.5, 0.75, 9, 0);
		StdDraw.line(8.5, -0.75, 9, 0);
		StdDraw.line(0, -11, 0, 49); // y axis
		StdDraw.line(0.25, 48, 0, 49);
		StdDraw.line(-0.25, 48, 0, 49);
		
		
		double deltaX2 = 1000*deltaX;		
		
		StdDraw.setPenColor(StdDraw.GRAY);
		for (double i = -10; i<10; i+=deltaX2) {
			StdDraw.line(i, p1.valueAt(i), i+deltaX2, p1.valueAt(i+deltaX2));
		}
		int red = 170;
		int green = 200;
		int blue = 90;
		
		for (double i = min; i<max; i += deltaX) {
			StdDraw.setPenColor(red, green, blue);
			double valueAti = p1.valueAt(i);
			if (valueAti > 0) {
				StdDraw.filledRectangle(i+deltaX/2, valueAti/2, deltaX/2, valueAti/2);
			} else {
				StdDraw.filledRectangle(i+deltaX/2, valueAti/2, deltaX/2, (-1)*valueAti/2);
			}
//			if (red < 30)
//				red +=20;
//			else
//				red -= 30;
//			if (green < 20)  
//				green += 35;
//			else
//				green -= 20;
//			if (blue < 5)
//				blue += 17;
//			else
//				blue -= 5;
		}
		StdDraw.setPenColor(StdDraw.BLACK);
//		StdDraw.line(i, 0.5, i, -0.5);
		StdDraw.setFont(new Font("Comic Sans", Font.PLAIN, 12));
//		StdDraw.text(i, -2, Double.toString(i));
		StdDraw.textLeft(-9, -8, "Delta x =" + deltaX);
		StdDraw.textLeft(-9, -10, "Integral:" + result);
		StdDraw.textLeft(9.25, 0, "x");
		StdDraw.textLeft(0.5, 49, "y");
		StdDraw.textRight(min, 1, Integer.toString(min));
		StdDraw.textRight(max, 1, Integer.toString(max));
		StdDraw.line(min, 0.75, min, -0.75);
		StdDraw.line(max, 0.75, max, -0.75);
		StdDraw.show();
	}

}

