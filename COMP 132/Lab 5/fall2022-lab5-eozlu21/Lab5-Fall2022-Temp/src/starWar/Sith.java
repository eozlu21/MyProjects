package starWar;

public class Sith extends ForceWielder{
	
	final String lsColorSith;
	int credits;


	public Sith(String nameString, int countBattles, double health, double attackPower, int credits) {
		super(nameString, countBattles, health, attackPower);
		this.lsColorSith = "red";
		this.healAmount = 100;
		this.credits = credits;
	}
	

	public void totalCredits() {
		System.out.printf("%.1f", 310 - 15* this.getCountBattles());
	}
	
	public void saberFight(Jedi j) {
		this.countBattles++;
		if (j.getHealth() > 0) {
			System.out.printf("The Sith %s produced a damage worth of %s against the Jedi %s.\n", this.getNameString(),this.getAttackPower() ,j.getNameString());
			j.setAttackPower(j.getAttackPower() - 10);
			j.setHealth(j.getHealth() - attackPower);
			this.setAttackPower(this.getAttackPower() + 10);
		}
		
		else if (this.getHealth() <= 0) {
			System.out.printf("The Sith %s has been defeated by the Jedi %s.\n", this.getNameString(), j.getNameString());
		}
		
		else {
			System.out.printf("The Sith %s defeated the Jedi %s.\n", this.getNameString(), j.getNameString());
		}
	}


	@Override
	public String getTypeString() {
		return "";
	}


}
