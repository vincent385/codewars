#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool alphanumeric(const char* string) {
    if (strlen(string) < 1)
        return false;
    for (size_t i = 0; i < strlen(string); i++) {
        if (isalpha(string[i]) == 0 && isdigit(string[i]) == 0)
            return false;
    }
    return true;
}
