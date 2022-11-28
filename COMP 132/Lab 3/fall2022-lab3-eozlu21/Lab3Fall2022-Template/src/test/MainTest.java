package test;

import simulation.Intern;
import simulation.Simulation;
import simulation.Training;

public class MainTest {
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
	public static void main(String[] args) {
		
		/* TODO 1: create seven Intern objects with the names surnames:
		Eda Yilmaz, Ali Korkmaz, Burak Hasan, Can Kuyucu, Ege Argun,
		Burcu Celebi, and Seyma Ece
		
		While creating the objects, you should demonstrate the use all the constructors that are defined in the Intern class. 
		*/
		Intern intern1 = new Intern();
		intern1.setId("1");
		intern1.setName("Eda Yılmaz");
		Intern intern2 = new Intern("2");
		intern2.setName("Ali Korkmaz");
		Intern intern3 = new Intern("3", "Burak Hasan");
		Intern intern4 = new Intern("4", "Can Kuyucu");
		Intern intern5 = new Intern("5", "Ege Argun");
		Intern intern6 = new Intern("6", "Burcu Celebi");
		Intern intern7 = new Intern("7", "Seyma Ece");
		
		/*
		 * TODO 2: create five objects of type Training class, named as Math, Java, Python, ML, and DS
		 * */
		Training t1 = new Training("Math", "1");
		Training t2 = new Training("Java", "2");
		Training t3 = new Training("Python", "3");
		Training t4 = new Training("ML", "4");
		Training t5 = new Training("DS", "5");
		
		/*
		 * TODO 3: add all the interns to all the trainings
		 * */
		Training[] trainings = {t1, t2, t3, t4, t5};
		Intern[] interns = {intern1, intern2, intern3, intern4, intern5, intern6, intern7};
		for (int i = 0; i < trainings.length; i++){
			for (int j = 0; j < interns.length; j++){
				trainings[i].appendIntern(interns[j]);
			}
		}
		
		/*
		 * TODO 4: create an object of Simulation class with the size of a x b, 
		 * where a is the number of interns (the number of rows) 
		 * and b is the number of trainings (the number of columns).
		 * */
		Simulation testSimulation = new Simulation(interns.length, trainings.length);
		
		/*
		 * TODO 5: Add all the trainings to the simulation object.
		 * */
		for (int i = 0; i < trainings.length; i++){
		 	testSimulation.appendTraining(trainings[i]);
		}
		/*
		 * TODO 6: Call the simulateTable() method that fills in and displays the table.
		 * */
		
		testSimulation.simulateTable();
		/*
		 * TODO 7: Call showInternPerformance() method that finds and displays the performance of interns as shown in the sample output.
		 * */

		testSimulation.updateTrainingPerformance("Math","Burcu Celebi", 92);
		testSimulation.updateTrainingPerformance("ML", "Burak Hasan", 35);

		

		testSimulation.showInternPerformance();
		/*
		 * TODO 8: Call showTrainingLevel() that finds and displays the level of each training as shown in the sample output.
		 * */
		testSimulation.showTrainingLevel();

		testSimulation.findMax();

	}

}
