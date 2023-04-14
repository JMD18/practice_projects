package classes.Types;
import java.util.ArrayList;

public class Types {

    // creating default private variables to be inherited by each type
    private int typeID;
    private String typeStr;
    ArrayList<Types> weaknesses = new ArrayList<Types>();
    ArrayList<Types> resistances = new ArrayList<Types>();
    ArrayList<Types> immunities = new ArrayList<Types>();
    
    
    // constructor
    public Types(int typeID, String typeStr, ArrayList<Types> weaknesses, ArrayList<Types> resistances, ArrayList<Types> immunities) {

        this.typeID = typeID;
        this.typeStr = typeStr;
        this.weaknesses = weaknesses;
        this.resistances = resistances;
        this.immunities = immunities;

    }

    // getters and setters
    public int getTypeID() {
        return typeID;
    }

    public void setTypeID(int typeID) {
        this.typeID = typeID;
    }

    public String getTypeStr() {
        return typeStr;
    }

    public void setTypeStr(String typeStr) {
        this.typeStr = typeStr;
    }

    public ArrayList<Types> getWeaknesses() {
        return weaknesses;
    }

    public void setWeaknesses(ArrayList<Types> weaknesses) {
        this.weaknesses = weaknesses;
    }

    public ArrayList<Types> getResistances() {
        return resistances;
    }

    public void setResistances(ArrayList<Types> resistances) {
        this.resistances = resistances;
    }

    public ArrayList<Types> getImmunities() {
        return immunities;
    }

    public void setImmunities(ArrayList<Types> immunities) {
        this.immunities = immunities;
    }

    // method to print out the weaknesses and resistances of a type
    public void printWeaknessesAndResistances() {
        System.out.println("Weaknesses: " + weaknesses);
        System.out.println("Resistances: " + resistances);
    }
}
