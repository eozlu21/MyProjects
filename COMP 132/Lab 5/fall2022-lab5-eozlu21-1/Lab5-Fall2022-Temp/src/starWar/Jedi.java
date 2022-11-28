package starWar;

public class Jedi extends ForceWielder implements IHealthBoostable{
	
	String lsColorJedi;
	double forceHealAmount = 2 * this.attackPower;
	int credits;

	public Jedi(String nameString, int countBattles, double health, double attackPower, String lsColorJedi, int credits) {
		
		super(nameString, countBattles, health, attackPower);
		this.lsColorJedi = lsColorJedi;
		this.healAmount = 150;
		this.credits = credits;
	}
	
	

	public int getCredits() {
		return credits;
	}



	public void setCredits(int credits) {
		this.credits = credits;
	}



	public void totalCredits() {
		System.out.printf("%.1f", 310 - 15* this.getCountBattles());
	}

	public void saberFight (Sith s) {
		this.countBattles++;
		
		if (s.getHealth() > 0) {
			System.out.printf("The Jedi %s produced a damage worth of %s against the Sith %s.\n", this.getNameString(),this.getAttackPower() ,s.getNameString());
			s.setAttackPower(s.getAttackPower() - 10);
			s.setHealth(s.getHealth() - attackPower);
			this.setAttackPower(this.getAttackPower() + 10);
		}
		
		else if (this.getHealth() <= 0) {
			System.out.printf("The Jedi %s has been defeated by the Sith %s.\n", this.getNameString(), s.getNameString());
		}
		
		else {
			System.out.printf("The Jedi %s defeated the Sith %s.\n", this.getNameString(), s.getNameString());
		}
	}
	
	public void revealLightsaber () {
		
		if (this.getLsColorJedi() == "blue") {
			System.out.println("Color generated from the lightsaber is blue.");
		}
		
		else if (this.getLsColorJedi() == "green") {
			System.out.println("Color generated from the lightsaber is green.");
		}
		
		else if (this.getLsColorJedi() == "purple") {
			System.out.println("Color generated from the lightsaber is purple.");
		}
		else {
			System.out.println("An Unknown color has been generated from the lightsaber.");
		}
	}
		
	public String getLsColorJedi() {
		return lsColorJedi;
	}

	public void setLsColorJedi(String lsColorJedi) {
		this.lsColorJedi = lsColorJedi;
	}

	

	public double getForceHealAmount() {
		return forceHealAmount;
	}

	public void setForceHealAmount(double forceHealAmount) {
		this.forceHealAmount = forceHealAmount;
	}

	

	@Override
	public String getTypeString() {
		
		return "Jedi";
	}



	@Override
	public void healthBoost() {
		setHealth(getHealth() * 5);
		
	}

	
	
	
}
