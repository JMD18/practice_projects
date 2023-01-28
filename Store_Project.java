package practice_projects;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;



/*	Practice creating a class to go along with
 * 	YT coding interview found at the link below:
 * 
 * 	https://youtu.be/46dZH7LDbf8
 * 
 */

class Store {

	ArrayList<Integer> values = new ArrayList<Integer>();
    HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();

    public static void main(String[] args) {
        

		Store s = new Store();

		s.insert(3);
		s.insert(6);
		s.insert(7);
		s.insert(9);
		s.insert(12);
		s.insert(51);

		s.remove(s.getRandom());
        
    }


	// insert value into list of values + insert value into map as key, with index as 'value'
	public void insert(int value) {

		if(values.contains(value)) return;

		this.values.add(value);
		this.map.put(value,this.values.size() - 1);

		this.printValues();

	}


	// remove value from list and also fix affected indices in map
	public void remove(int value) {

		if(!(values.contains(value))) {
			System.out.println("\n" + value + " not found in values.");
			return;
		}

		// init elements to be swapped (swapping to lastIndex and then popping as to make shifting unnecessary)
		int lastIndex = this.values.size()-1;
		int index = this.map.get(value);
		int temp_val = this.values.get(lastIndex);

		// replacing values
		this.values.set(lastIndex, value);
		this.values.set(index, temp_val);
		this.map.replace(temp_val, index);

		// removing values
		this.values.remove(lastIndex);
		this.map.remove(value);

		this.printValues();
	}


	// gets random element from Values
	public int getRandom() {
		Random rn = new Random();
		int randomIndex = rn.nextInt(this.values.size());

		return this.values.get(randomIndex);
	}


	// c'mon...you know what it does
	public void printValues() {
		System.out.println("Values: " + this.values.toString());
	}	

}