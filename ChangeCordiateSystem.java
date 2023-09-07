import java.util.*;
import java.lang.Math;

class ChangeCordiateSystem {
    public static void main(String[] arg) {
        Scanner cin = new Scanner(System.in);
        System.out.println("In which cordinate system, you want to provide 3-dimetional points? ");
        System.out.println("1= Rectangular, 2= Circular cylinderical, 3=Spherical");
        int choice = cin.nextInt();

        System.out.print("Input value of x: ");
        double x = cin.nextDouble();
        System.out.print("Input value of y: ");
        double y = cin.nextDouble();
        System.out.print("Input value of z: ");
        double z = cin.nextDouble();

        switch (choice) {
            case 1: {
                System.out.println("Points in Rectangular coordinate system is: ");
                System.out.println("value of x: " + x);
                System.out.println("value of y: " + y);
                System.out.println("value of z: " + z);
                break;
            }
            case 2: {
                System.out.println("Points in Circular cylindrical coordinate system is: ");
                System.out.println("value of rho: " + Math.pow((x * x + y * y), 0.5));
                System.out.println("value of phi in radian: " + Math.atan(x / y));
                System.out.println("value of z: " + z);
                break;
            }
            case 3: {
                System.out.println("Points in Spherical coordinate system is: ");
                System.out.println("value of r: " + Math.pow((x * x + y * y + z * z), 0.5));
                System.out.println("value of theta in radians: " + Math.atan((Math.pow((x * x + y * y), 0.5)) / z));
                System.out.println("value of phi in radian: " + Math.atan(x / y));
                break;
            }
        }

    }
}