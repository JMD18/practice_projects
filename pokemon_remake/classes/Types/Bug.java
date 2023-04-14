package classes.Types;
import java.util.ArrayList;

public class Bug extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();
    static ArrayList<Types> immunities = new ArrayList<Types>();

    public Bug() {
        
        super(14, "Bug", weaknesses, resistances, immunities);
        weaknesses.add(new Fire());
        weaknesses.add(new Flying());
        resistances.add(new Fighting());
        resistances.add(new Ground());
        resistances.add(new Grass());

    }

}