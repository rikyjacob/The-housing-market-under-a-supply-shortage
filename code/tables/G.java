public class G extends F {
String m = "G.m";
final static String s = "G.s";
String m() { return "G.m()" + super.s(); }
String m(F f) { return "G.m(F)"; }
String m(G g) { return "G.m(G)"; }
String k(F f) { return "G.k(F)" + this.m((G)f); } 
static String s() { return "G.s()"; }
}