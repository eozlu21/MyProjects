package starWar;

public class Knight extends Jedi{
	
    Padawan padawan;
    final String nameForce;
    
	public Knight(String nameString, int countBattles, double health, double attackPower, String lsColorJedi, int credits,
			Padawan padawan) {
		super(nameString, countBattles, health, attackPower, lsColorJedi, credits);
		this.padawan = padawan;
		this.nameForce = "Force Heal";
	}

	public Padawan getPadawan() {
		return padawan;
	}

	public void setPadawan(Padawan padawan) {
		this.padawan = padawan;
	}

	public String getNameForce() {
		return nameForce;
	}
    
    public void healPadawan() {
    	if (padawan.getHealth() != 0) {
    		padawan.setHealth(padawan.getHealth() + getForceHealAmount());
    	}
    }
    
    @Override
    public String getTypeString() {
    	return "Knight Jedi";
    }
	
}
