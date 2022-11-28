package numguessr;

public class User {

    private String name;
    private int guessedNumber;
    private int totalScore;
    private int numExceeds;

    public User(String userName) {

        totalScore = 0;
        numExceeds = 0;
        this.name = userName;

    }

    public String toString() {
        return this.name;
    }

    public int getGuessedNumber() {
        return this.guessedNumber;
    }

    public void setGuessedNumber(int guessedNumber) {
        this.guessedNumber = guessedNumber;
    }

    public int getTotalScore() {
        return this.totalScore;
    }

    public void setTotalScore(int totalScore) {
        this.totalScore = totalScore;
    }
    
    public void incrementTotalScore(int points) {
        this.totalScore += points;
    }

    public int getNumExceeds() {
        return this.numExceeds;
    }

    public void setNumExceeds(int numExceeds) {
        this.numExceeds = numExceeds;
    }

    public void incrementNumExceeds(int numExceeds){
        this.numExceeds += 1;
    }
    
}
