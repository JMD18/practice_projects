package classes.Types;
import java.util.ArrayList;

public class Ground extends Types {

    static ArrayList<int> weaknesses = [Water.typeID, new Grass(), new Ice()];
    static ArrayList<int> resistances = new ArrayList<Types>();
    static ArrayList<int> immunities = new ArrayList<Types>();

    public Ground() {
        
        super(12, "Ground", weaknesses, resistances,immunities);
        weaknesses.add(new Water());
        weaknesses.add(new Grass());
        weaknesses.add(new Ice());
        resistances.add(new Poison());
        resistances.add(new Rock());
        resistances.add(new Steel());
        resistances.add(new Fire());
        immunities.add(new Electric());

    }

}