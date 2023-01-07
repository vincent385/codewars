#include <stdbool.h>
#include <string.h>

typedef struct mini_win_t
{
    char    *letters;
    unsigned code;
} MiniWin;

typedef struct ticket_t
{
    MiniWin *mini_wins;
    unsigned count;
} Ticket;

const char *bingo(const Ticket *ticket, unsigned win)
{
    unsigned mini_wins = 0;
    bool bracket_win = false;
    for (unsigned i = 0; i < ticket->count; i++) {
        for (unsigned j = 0; j < strlen(ticket->mini_wins[i].letters); j++) {
            if ((unsigned) ticket->mini_wins[i].letters[j] == ticket->mini_wins[i].code && !bracket_win) {
                mini_wins += 1;
                bracket_win = true;
            }
        }
        bracket_win = false;
    }
    if (mini_wins >= win)
        return "Winner!";
    return "Loser!";
}
