
public class H extends G {
private String m = "H.m";
String k(F f) { return "H.k(F)"; }
String k(G g) { return "H.k(G)" + super.m((F)g); }
public static void main(String[] args){
    F a = new F();
    G b = new G();
    F c = b;
    H h = new H();
    String j = 5 + "5";
    String k = new String("5");
    System.out.print(j);

    }
}