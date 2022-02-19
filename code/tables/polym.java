public class F {
String m = "F.m";
String m() { return "F.m()" + this.s(); } String m(F f) { return "F.m(F)" + s(); } private String m(G g) { return "F.m(G)"; } String k() { return "F.k()" + this.m(this); } String k(G g) { return "F.k(G)"; }
static String s() { return "F.s()"; }
static String t() { return "F.t()"; }
}
public class G extends F {
String m = "G.m";
final static String s = "G.s";
String m() { return "G.m()" + super.s(); }
String m(F f) { return "G.m(F)"; }
String m(G g) { return "G.m(G)"; }
String k(F f) { return "G.k(F)" + this.m((G)f); } static String s() { return "G.s()"; }
}
public class H extends G {
private String m = "H.m";
String k(F f) { return "H.k(F)"; }
String k(G g) { return "H.k(G)" + super.m((F)g); }
}