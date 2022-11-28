package simulation;

import java.util.ArrayList;
import java.util.Random;

public class Simulation {

    private int[][] performanceTable;
    private ArrayList<Training> trainings = new ArrayList<Training>();
    
    public Simulation(int a, int b){
        this.performanceTable = new int[a][b];
    }

    public int[][] getPerformanceTable() {
        return this.performanceTable;
    }

    public void setPerformanceTable(int[][] performanceTable) {
        this.performanceTable = performanceTable;
    }

    public ArrayList<Training> getTrainings() {
        return this.trainings;
    }

    public void setTrainings(ArrayList<Training> trainings) {
        this.trainings = trainings;
    }

    public void appendTraining(Training trn){
        trainings.add(trn);
    }

    public void simulateTable(){
        // first, create the table data
        Random generator = new Random(1500);
        for(int i = 0; i < this.performanceTable.length; i++){
            ArrayList<Intern> interns = trainings.get(0).getInterns();
            for(int j = 0; j < performanceTable[i].length; j++){
                int currentScore = generator.nextInt(90) + 10;
                performanceTable[i][j] = currentScore;
                interns.get(i).setMaxScore(currentScore, trainings.get(j));
            }
        }
        // then, create the row and columns
        String[] topRow = new String[trainings.size()];
        for (int i = 0; i < topRow.length; i++){
            topRow[i] = trainings.get(i).getTitle();
        }
        ArrayList<String> nameColumn = trainings.get(0).getInternList();
        String outputString = "Name           ";
        for (int i = 0; i < topRow.length; i++){
            outputString += topRow[i] + "  ";
        }
        outputString += " \n";
        outputString += "---------------------------------------------";
        outputString += "\n";
        for (int i = 0; i < nameColumn.size(); i++){
            outputString += nameColumn.get(i);
            for (int n = 0; n < (14 - nameColumn.get(i).length()); n++){
                outputString += " ";
            }
            for (int rowIndex = 0; rowIndex < this.performanceTable[i].length; rowIndex++){
            outputString += "| ";
            outputString += this.performanceTable[i][rowIndex];
            if (rowIndex + 1 == this.performanceTable[i].length){
                outputString += " ";
            }
            else {
                outputString += "  ";
            }
            }
            outputString += "|";
            outputString += "\n"; 
        }
        System.out.println(outputString);
    }

    public void showInternPerformance(){
        System.out.println("------------------------ Interns performance ---------------------------------");
        System.out.println("");
        for(int i = 0; i < this.performanceTable.length; i++){
            ArrayList<String> nameColumn = trainings.get(0).getInternList();
            int sum = 0;
            for(int j = 0; j < performanceTable[i].length; j++){
                sum += performanceTable[i][j];
            }
            float average = (float)sum / (float)this.performanceTable[i].length;
            System.out.printf("%s  has the Average score of %.1f", nameColumn.get(i), Math.floor(average));
            System.out.println("");
            System.out.println("");
        }
    }

    public void showTrainingLevel(){
        System.out.println("------------------------ Trainings performance ---------------------------------");
        System.out.println("");
        String[] topRow = new String[trainings.size()];
        for (int i = 0; i < topRow.length; i++){
            topRow[i] = trainings.get(i).getTitle();
        }
        for (int j = 0; j < this.performanceTable[0].length; j++){
            int sum = 0;
            for (int i = 0; i < this.performanceTable.length; i ++){
                sum += performanceTable[i][j];
            }
            float average = (float)sum / (float)this.performanceTable.length;
            String currentTraining = topRow[j];
            String result;
            if (average > 65) {
                result = "above";
            }
            else {
                result = "below";
            }
            System.out.printf("The average of  %s  is %.1f, then, its level is %s the threshold.", currentTraining, Math.floor(average), result);
            System.out.println("");
        }
    }

    public void findMax(){
        System.out.println("");
        Intern refIntern = new Intern();
        refIntern.overrideMaxScore(0);
        for(int i = 0; i < trainings.get(0).getInterns().size(); i++){
            if (trainings.get(0).getInterns().get(i).getMaxScore() > refIntern.getMaxScore()){
                refIntern = trainings.get(0).getInterns().get(i);
            }
        }
        System.out.println("Maximum performance: " + Integer.toString(refIntern.getMaxScore()));
        System.out.println("Intern: " + refIntern.getName() + ", ID: " + refIntern.getId());
        System.out.println("Training: " + refIntern.getMaxTraining().getTitle() + ", CODE: " + refIntern.getMaxTraining().getCode());
    }
    
    public void updateTrainingPerformance(String trainingName, String
    internName, int newPerformance){
        int internIndex = 0;
        int trainingIndex = 0;
        for (Training iteTraining : this.trainings){
            if(iteTraining.getTitle() == trainingName){
                break;
            }
            trainingIndex++;
        }
        for (Intern intern : this.trainings.get(0).getInterns()){
            if(intern.getName() == internName){
                break;
            }
            internIndex++;
        }
        performanceTable[internIndex][trainingIndex] = newPerformance;

    }
}

