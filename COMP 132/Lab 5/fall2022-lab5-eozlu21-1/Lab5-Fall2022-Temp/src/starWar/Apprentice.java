package starWar;

public class Apprentice extends Sith {

	Master master;
	final String forceName;
	
	public Apprentice(String nameString, int countBattles, double health, double attackPower, int credits, Master master) {
		super(nameString, countBattles, health, attackPower, credits);
		this.master = master;
		this.forceName = "Force Choke";
	}

	public Master getMaster() {
		return master;
	}

	public void setMaster(Master master) {
		this.master = master;
	}

	public String getForceName() {
		return forceName;
	}
	
	@Override
	public String getTypeString() {
		return "Apprentice";
	}
	
	public void chokeJedi(Jedi j) {
		if(j.health != 0) {
			j.setHealth(j.getHealth()*0.5 - getAttackPower());
		}
	}
	
	public void betrayMaster() {
		if (master.getHealth()*10 < master.getInitHP()){
			master.setHealth(0);
			setHealth(100);
		}
	}
	
}
