import java.util.*;
import java.lang.Math;

class CalculateResistance {
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        System.out.println("Enter Number of bands: ");
        int band = cin.nextInt();
        int a, b, c, d, e, f;
        double resistance1 = 0, resistance2 = 0;
        switch (band) {
            case 3: {
                System.out.println("Enter three number of band: ");
                a = cin.nextInt();
                b = cin.nextInt();
                c = cin.nextInt();
                resistance1 = ((a * 10 + b) * Math.pow(10.0, c)) + 0.2;
                resistance2 = ((a * 10 + b) * Math.pow(10.0, c)) - 0.2;
                System.out.println("Resistance of bands are: " + resistance1 + " " + resistance2);
                break;
            }
            case 4: {
                System.out.println("Enter four number of band: ");
                a = cin.nextInt();
                b = cin.nextInt();
                c = cin.nextInt();
                d = cin.nextInt();
                resistance1 = ((a * 10 + b) * Math.pow(10.0, c)) + d / 100;
                resistance2 = ((a * 10 + b) * Math.pow(10.0, c)) - d / 100;
                System.out.println("Resistance of bands are: " + resistance1 + " " + resistance2);
                break;
            }
            case 5: {
                System.out.println("Enter four number of band: ");
                a = cin.nextInt();
                b = cin.nextInt();
                c = cin.nextInt();
                d = cin.nextInt();

                resistance1 = ((a * 100 + b * 10 + c) * Math.pow(10.0, d)) + 0.01;
                resistance2 = ((a * 100 + b * 10 + c) * Math.pow(10.0, d)) - 0.01;
                System.out.println("Resistance of bands are: " + resistance1 + " " + resistance2);
                break;
            }
            case 6: {
                System.out.println("Enter six number of band: ");
                a = cin.nextInt();
                b = cin.nextInt();
                c = cin.nextInt();
                d = cin.nextInt();
                e = cin.nextInt();
                f = cin.nextInt();
                resistance1 = ((a * 100 + b * 10 + c) * Math.pow(10.0, d)) + e / 100;
                resistance2 = ((a * 100 + b * 10 + c) * Math.pow(10.0, d)) - e / 100;
                System.out.println("Resistance of bands are: " + resistance1 + " " + resistance2);
                System.out.println("temperature coefficient is: " + f);
                break;
            }
        }
    }
}