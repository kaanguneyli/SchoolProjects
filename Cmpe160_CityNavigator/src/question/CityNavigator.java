
package question;


import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

import javax.xml.transform.Templates;


public class CityNavigator
{  

	public static int pathFinder(String startCity, String targetCity) {
		
		//DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
		
		// in this part we read the file
		// in order to store every path and line separately we create 2 arrays
		String[] paths = new String[17];
		int[] lengths = new int[17];
		int arrayIndex = 0;
		try {
			// here we read the file line by line
			File file = new File("cities_and_distances.txt");
			Scanner scan = new Scanner(file);
			while (scan.hasNextLine()) {
				String data = scan.nextLine();
				// we split from : so we can differentiate paths and their lengths
				String[] dataArray = data.split(":");
				paths[arrayIndex] = dataArray[0];
				lengths[arrayIndex] = Integer.valueOf(dataArray[1]);
				arrayIndex++;
			}
			scan.close();
		} catch (FileNotFoundException e) {
			System.out.println("error");
			e.printStackTrace();
		}
		// we create these just to make our code easier to write
		char startCityChar = startCity.charAt(0);
		char targetCityChar = targetCity.charAt(0);
		// here we set our current point as the starting point
		char currentPoint = startCityChar;
		// we create the arraylist that represents points we have passed and we add the starting point
		ArrayList<Character> points = new ArrayList<Character>();
		points.add(currentPoint);
		// we create an arraylist for the indexes that we used
		ArrayList<Integer> indexes = new ArrayList<>();
		// we store the path we are working on in this arraylist
		ArrayList<String> currentPath = new ArrayList<>();
		// we create an arraylist that will store the shortest way, we will print this at the end
		ArrayList<String> minPath = new ArrayList<>();
		// we set a boolean to false, which will make our while loop work
		boolean done = false;
		// i stands for index, which will be used in our iterations through the array 'paths', we set it at 0 to make our iteration start from the beginning 
		int i = 0;
		int currentLength = 0;
		int minLength = Integer.MAX_VALUE;
		
		while (!done) {
			// this false boolean expression say we have not found a proper way to leave our current point 
			boolean foundOne = false;
			// we will use this for loop will iterate through 'paths' and 'lengths'
			for (; i<lengths.length; i++) {
				// if we face current point as the first point of path in the text file and the point it leads is not used we will rearrange our variables 
				if (paths[i].charAt(0) == currentPoint) {
					if (! points.contains(paths[i].charAt(2))) { 
						currentPoint = paths[i].charAt(2);
						currentLength += lengths[i];
						points.add(currentPoint);
						indexes.add(i);
						currentPath.add(paths[i]);
						foundOne = true;
						// we are setting i to 0 in order to check the points from the beginning
						i=0;
					}
				} 
				// here we are doing the same thing when the current point is given as the second city in text file
				else if (paths[i].charAt(2) == currentPoint) {
					if (! points.contains(paths[i].charAt(0))) {
						currentPoint = paths[i].charAt(0);
						currentLength += lengths[i];
						points.add(currentPoint);
						indexes.add(i);
						currentPath.add(paths[i]);
						foundOne = true;
						i=0;
					}
				}
			} 
			// if the point we arrived is the targetCity we have to look for new ways to find the optimum, so we have to set foundOne to false (this will be clarified in next block)
			if (currentPoint == targetCityChar) {
				foundOne = false;
				// if the path we found is the minimum until now, we have to arrange min variables
				if (currentLength < minLength) {
					// we clear the minPath and add the values one by one with this for loop
					// we cannot do assignment directly because arraylists are passed by reference
					minLength = currentLength;
					minPath.clear();
					for (int j=0; j<currentPath.size(); j++)
						minPath.add(currentPath.get(j));
				}
			}
			// if we couldn't find anywhere to go from a point or if it is the targetCity we have to go back and look for new options
			if (! foundOne) {
				// we remove the last point we have been from the arraylist
				points.remove(points.size()-1);
				// we set i to a value that is 1 bigger than its old value which led us to last way, thus we do not find the same way again
				// we also remove the last paths values from our variables
				if (indexes.size() > 0) {
					i = indexes.get(indexes.size()-1) + 1;
					indexes.remove(indexes.size()-1);
					currentPath.remove(currentPath.size()-1);
					currentLength -= lengths[i-1];
					currentPoint = points.get(points.size()-1);
				}
				// if there are no elements in the indexes arraylist, we understand that we have tried all the ways possible, so we exit the while loop
				else 
					done = true;
			}
		}
		// we return 0 if there is not an answer 
		if (minLength == Integer.MAX_VALUE) {
			return 0;
		} else {
			System.out.println(minPath);
			return minLength;
		}	
	}
		//DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
	public static void main(String[] args) {
		System.out.println(pathFinder("L", "B"));
	}  
}
