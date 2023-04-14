package classes.Types;
import java.util.ArrayList;

public class Water extends Types {
    
    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();
    
    public Water() {
        
        super(2, "Water", weaknesses, resistances);
        weaknesses.add(new Grass());
        weaknesses.add(new Electric());

        resistances.add(new Fire());
        resistances.add(new Water());
        resistances.add(new Ice());
        resistances.add(new Steel());

    }
}