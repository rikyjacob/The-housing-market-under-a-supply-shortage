public class F {
String m = "F.m";
String m() { return "F.m()" + this.s(); } 
String m(F f) { return "F.m(F)" + s(); } 
private String m(G g) { return "F.m(G)"; } 
String k() { return "F.k()" + this.m(this); } 
String k(G g) { return "F.k(G)"; }
static String s() { return "F.s()"; }
static String t() { return "F.t()"; }
}