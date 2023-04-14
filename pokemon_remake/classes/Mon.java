package classes;
import java.io.*;

public class Mon {

    private int MonID;
    private String MonTypeStr;
    private int MonTypeID;

    public Mon(int MonID, String MonTypeStr, int MonTypeID) {

        this.MonID = MonID;
        this.MonTypeStr = MonTypeStr;
        this.MonTypeID = MonTypeID;

    }

    public int getMonID() {
        return MonID;
    }

    public void setMonID(int monID) {
        MonID = monID;
    }

    public String getMonTypeStr() {
        return MonTypeStr;
    }

    public void setMonTypeStr(String monTypeStr) {
        MonTypeStr = monTypeStr;
    }

    public int getMonTypeID() {
        return MonTypeID;
    }

    public void setMonTypeID(int monTypeID) {
        MonTypeID = monTypeID;
    }

    public void addWeakness(int weakness) {
        weaknesses.add(weakness);
    }

    public void addResistance(int resistance) {
        resistances.add(resistance);
    }

    public void printWeaknesses() {
        System.out.println("Weaknesses: ");
        for(int i = 0; i < weaknesses.size(); i++) {
            System.out.println(weaknesses.get(i));
        }
    }

    public void printResistances() {
        System.out.println("Resistances: ");
        for(int i = 0; i < resistances.size(); i++) {
            System.out.println(resistances.get(i));
        }
    }

    public void printWeaknessesAndResistances() {
        System.out.println("Weaknesses: " + weaknesses);
        System.out.println("Resistances: " + resistances);
    }
    
}