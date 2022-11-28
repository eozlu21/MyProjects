package starWar;

public class Master extends Sith {

	Apprentice apprentice;
	final String forceName;
	final double initHP;
	
	public Master(String nameString, int countBattles, double health, double attackPower, int credits, Apprentice apprentice) {
		super(nameString, countBattles, health, attackPower, credits);
		this.apprentice = apprentice;
		this.forceName = "Force Lightning";
		this.initHP = getHealth();
	}

	public Apprentice getApprentice() {
		return apprentice;
	}

	public void setApprentice(Apprentice apprentice) {
		this.apprentice = apprentice;
	}

	public String getForceName() {
		return forceName;
	}
	
	@Override
	public String getTypeString() {
		return "Master";
	}
	
	public double getInitHP() {
		return this.initHP;
	}
	public void shockJedi(Jedi j) {
		if (j.getHealth() != 0) {
			j.setHealth(j.getHealth()*0.8 - getAttackPower() * 0.5);
		}
	}
	
}
