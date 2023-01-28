#include "validator.h"

void run() {
    int n = Int(1, 100000);
    Endl();
    set<string> seen;
    for (int i = 0; i < n; ++i) {
        string pubname;
        cin >> pubname;
        if (pubname.length() > 10) die("Pub name " + pubname + " too long!");
        if (pubname.length() < 1) die("Pub name " + pubname + " too short!");
        for(char c : pubname){
            if(!(c>='a' && c<='z') && !(c>='A' && c<='Z')) die("bad char");
        }
        if(seen.count(pubname)) die("duplicate name");
        seen.insert(pubname);
        Space();
        int k = Int(0, 10000);
        Space();
        int t = Int(1, 10000);
        Endl();
    }
    Eof();
}
