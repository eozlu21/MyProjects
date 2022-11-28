package simulation;

public class Intern {

    private String name;
    private String id;
    private int maxScore = 0;
    private Training maxTraining;
    private int rowNum;

    public Intern(){ 
    }

    public Intern(String idString){
        this.id = idString;
    } 

    public Intern(String idString, String name){
        this.id = idString;
        this.name = name;
    }

    public int getRowNum() {
        return this.rowNum;
    }

    public void setRowNum(int rowNum) {
        this.rowNum = rowNum;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getId() {
        return this.id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setMaxScore(int score, Training training){
        if (score > this.maxScore){
            this.maxScore = score;
            this.maxTraining = training;
        }
    }

    public int getMaxScore() {
        return this.maxScore;
    }


    public Training getMaxTraining() {
        return this.maxTraining;
    }

    public void setMaxTraining(Training maxTraining) {
        this.maxTraining = maxTraining;
    }

    public void overrideMaxScore(int score){
        this.maxScore = score;
    }

}
