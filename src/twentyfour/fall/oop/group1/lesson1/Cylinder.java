package twentyfour.fall.oop.group1.lesson1;

public class Cylinder {
    public static void main(String[] arg){
        float radius = 16;
        System.out.println("Radius is : " + radius);
        float height = 10;
        System.out.println("Height is : " + height);
        //Constant variable use final
        final float NUMBER_PI = 3.141592f;
        System.out.println("Our constant have a value : " + NUMBER_PI);

        float volume = NUMBER_PI * (radius*radius) * height;
        System.out.println("The volume of the cylinder is : " + volume);
    }
}
