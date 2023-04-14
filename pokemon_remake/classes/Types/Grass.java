package classes.Types;
import java.util.ArrayList;

public class Grass extends Types {

    ArrayList<Types> weaknesses = new ArrayList<Types>(new Fire(), new Ice(), new Poison(), new Flying(), new Bug());

    public Grass() {
        
        super(3, "Grass", weaknesses, resistances);
        weaknesses.add(new Fire());
        weaknesses.add(new Ice());
        weaknesses.add(new Poison());
        weaknesses.add(new Flying());
        weaknesses.add(new Bug());

        resistances.add(new Water());

        
        



    }

}