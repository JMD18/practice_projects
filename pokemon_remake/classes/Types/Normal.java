package classes.Types;
import java.util.ArrayList;

public class Normal extends Types {

    static ArrayList<Types> weaknesses = new ArrayList<Types>();
    static ArrayList<Types> resistances = new ArrayList<Types>();

    public Normal() {
        
        super(0, "Normal", weaknesses, resistances);
        weaknesses.add(new Fighting());
        resistances.add(new Ghost());

    }

}