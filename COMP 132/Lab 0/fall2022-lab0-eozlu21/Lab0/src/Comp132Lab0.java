import java.util.Scanner;

// add your pledge of honor statement here
/* *********** Pledge of Honor ************************************************ *

I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted at the course website and (3) any study notes handwritten by myself.
I have not used, accessed or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.
READ AND SIGN BY WRITING YOUR NAME SURNAME AND STUDENT ID
SIGNATURE: Ege Erdem Özlü, 80481
********************************************************************************/

public class Comp132Lab0 {


	public static void main(String[] args) {

		// Question 1:
			Scanner input = new Scanner(System.in);
			System.out.print("Please enter the number of seconds: ");
			int secondsInput = input.nextInt();
			final int secondsInHour = 3600;
			final int secondsInMinute = 60;
			int hours = secondsInput / secondsInHour;
			int newSecondsInput = secondsInput % secondsInHour;
			int minutes = newSecondsInput / secondsInMinute;
			int seconds = newSecondsInput %  secondsInMinute;
			System.out.println(
				Integer.toString(secondsInput) + " seconds = " 
				+ Integer.toString(hours) + " hours, " + 
				Integer.toString(minutes) + " minutes, " + 
				Integer.toString(seconds) + " seconds.");
		// Question 2 & 3 & 4:
			String myName = "Ege Erdem Özlü";
			int myID = 80481;
			System.out.println(myName + ", " + myID);
		// Question 5:
			for (int i = 0; i < myName.length(); i++){
				char currentChar = myName.charAt(i);
				if (currentChar != (" ".charAt(0))) {
					int currentNumericVal = (int)currentChar;
					System.out.println(currentNumericVal);
				}
			
			}
	}
}
