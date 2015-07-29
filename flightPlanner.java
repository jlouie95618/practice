import java.util.*;
import java.io.*;

public class flightPlanner {

	public static void main(String []args) {
       HashMap<String, ArrayList<String>> flights = loadFlights();

       ArrayList<String> flightPath = chooseFlightPath();

       printFlightPath(flightPath);
    }
	
    private static HashMap<String, ArrayList<String>> loadFlights() {
    	return null;
    }

    private static ArrayList<String> chooseFlightPath() {
    	return null;
    }

    private static void printFlightPath(ArrayList<String> flightPath) {
    	System.out.println("Yo motherfuckin face");
    }

}