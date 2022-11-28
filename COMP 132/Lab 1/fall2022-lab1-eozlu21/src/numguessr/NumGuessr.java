package numguessr;

public class NumGuessr {

    private User user1;
    private User user2;
    private int sumOfDivableBy3 = 0;

    public int getSumOfDivableBy3(){
        return this.sumOfDivableBy3;
    }
    public void addSumOfDivableBy3(int numberToAdd){
        this.sumOfDivableBy3 += numberToAdd;
    }

    public NumGuessr(User user1, User user2) {

        this.user1 = user1;
        this.user2 = user2;

    }
    
    public int distanceCalculator(int currentUserGuess, int numberToGuess) {
            
        int userDist;
        
        if (numberToGuess > currentUserGuess) {
            userDist = numberToGuess - currentUserGuess;
        }
        else if (currentUserGuess > numberToGuess) {
            
            userDist = currentUserGuess - numberToGuess;
        }
        else {
            userDist = 0;
        }

        return userDist;
    }

    public void play(int numberToGuess) {

        int guessUser1;
        int guessUser2;
        int distUser1;
        int distUser2;
        int pointUser1;
        int pointUser2;

        guessUser1 = user1.getGuessedNumber();
        if (guessUser1 > numberToGuess){
            user1.incrementNumExceeds(user1.getNumExceeds());
        }
        guessUser2 = user2.getGuessedNumber();
        if (guessUser2 > numberToGuess){
            user2.incrementNumExceeds(user2.getNumExceeds());
        }
        if ((guessUser1 + guessUser2) % 3 == 0){
            this.addSumOfDivableBy3(guessUser1 + guessUser2);
        }

        distUser1 = distanceCalculator(guessUser1, numberToGuess);
        distUser2 = distanceCalculator(guessUser2, numberToGuess);

        if ((distUser1 == distUser2) && (distUser1 == 0)) {
            pointUser1 = 202;
            pointUser2 = 202;
        }
        else if (distUser1 == distUser2) {
            pointUser1 = 101;
            pointUser2 = 101;
        }
        else if (distUser1 == 0) {
            pointUser1 = 101;
            pointUser2 = 0;
        }
        else if (distUser2 == 0) {
            pointUser2 = 101;
            pointUser1 = 0;
        }
        else if (distUser1 > distUser2) {
            pointUser2 = distUser1;
            pointUser1 = 0;
        }
        else {
            pointUser1 = distUser2;
            pointUser2 = 0;
        }

        System.out.println("Number to guess was: " + Integer.toString(numberToGuess));

        if (pointUser1 == 202) {
         System.out.println("Both " + user1.toString() + " and" + user2.toString() + " guessed the number correctly!");
        }

        else if ((pointUser1 == 101 && pointUser2 == 101)) {
            System.out.println(user1.toString() + " and "+ user2.toString()+ " were the same distance to " + Integer.toString(numberToGuess) + "!");
        }
        else if (pointUser1 > pointUser2) {
            System.out.println(user1.toString() + " won.");
        }
        else if (pointUser2 > pointUser1) {
            System.out.println(user2.toString() + " won.");
        }

        System.out.println(" ");

        user1.incrementTotalScore(pointUser1);
        user2.incrementTotalScore(pointUser2);
    }    
    
    public void whoWon() {
        if (user1.getTotalScore() > user2.getTotalScore()) {
            System.out.println(user1.toString() + " has won 3 rounds of NumGuessr with a total " + user1.getTotalScore() + " points.");
        }
        else if (user2.getTotalScore() > user1.getTotalScore()) {
            System.out.println(user2.toString() + " has won 3 rounds of NumGuessr with a total " + user2.getTotalScore() + " points.");
        }
        else {
            System.out.println("3 rounds of NumGuessr between " + user1.toString() + " and " + user2.toString() + " were resulted with a tie with both scoring " + user1.getTotalScore() + "points.");
        }
        System.out.println("Number of exceeds for " + user1.toString() + ": " + user1.getNumExceeds());
        System.out.println("Number of exceeds for " + user2.toString() + ": " + user2.getNumExceeds());
        System.out.println("The total difference on the rounds with total guesses is divisible by three: " + this.getSumOfDivableBy3());
    }
}
