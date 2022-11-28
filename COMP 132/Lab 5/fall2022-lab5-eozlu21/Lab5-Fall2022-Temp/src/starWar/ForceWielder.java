package starWar;

public abstract class ForceWielder implements IHealable{
	

	String nameString;
	int countBattles;
	double health;
	double attackPower;
	double healAmount;
	
	public ForceWielder(String nameString, int countBattles, double health, double attackPower) {
		this.nameString = nameString;
		this.countBattles = countBattles;
		this.health = health;
		this.attackPower = attackPower;
	}
	
	public abstract void totalCredits();
	
	public abstract String getTypeString();
	
	public String toString() {
		var output = String.format
				(	"%s Name: %s\n"
				+ 	"   Number of battles engaged: %s \n"
				+ 	"   Health: %.1f \n"
				+ 	"   Damage of Lightsaber: %.1f\n", getTypeString(), this.nameString, this.countBattles, this.health, this.attackPower);
		return output;
	}

	public String getNameString() {
		return nameString;
	}

	public void setNameString(String nameString) {
		this.nameString = nameString;
	}

	public int getCountBattles() {
		return countBattles;
	}

	public void setCountBattles(int countBattles) {
		this.countBattles = countBattles;
	}

	public double getHealth() {
		return health;
	}

	public void setHealth(double health) {
		this.health = health;
	}

	public double getAttackPower() {
		return attackPower;
	}

	public void setAttackPower(double attackPower) {
		this.attackPower = attackPower;
	}
	
	public void heal() {
		setHealth(getHealth() + healAmount);
		
	}
	
}
