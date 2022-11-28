package starWar;

public class Padawan extends Jedi{
	
    Knight knight;
    final String nameForce;
    
	public Padawan(String nameString, int countBattles, double health, double attackPower, String lsColorJedi, int credits, Knight knight){
		super(nameString, countBattles, health, attackPower, lsColorJedi, credits);
		this.knight = knight;
		this.nameForce = "Jedi Mind Trick";
	}

	public Knight getKnight() {
		return knight;
	}

	public void setKnight(Knight knight) {
		this.knight = knight;
	}

	public String getNameForce() {
		return nameForce;
	}
    
	public void confuseSith(Sith s) {
		if (s.getHealth() != 0) {
			s.setAttackPower(s.getAttackPower()*0.8);
		}
	}
	
	public void healKnight() {
		if(knight.getHealth() != 0) {
			knight.healPadawan();
		}
	}
	
	@Override
    public String getTypeString() { 
		return "Padawan Jedi";
	}
    
    
}
