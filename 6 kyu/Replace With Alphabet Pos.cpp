#include <string>

using namespace std;

string alphabet_position(const string &text) {
    string s;
    for (size_t i = 0; i < text.length(); i++) {
        if (text[i] > 64 && text[i] < 91) { s += to_string(text[i] - 65 + 1) + ' '; }
        if (text[i] > 96 && text[i] < 123) { s += to_string(text[i] - 97 + 1) + ' '; }
    }
    if (!s.empty()) s.pop_back();
    return s;
}
