#include "configure_race.h"
#include "race_timing.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

int compare_runners_by_time(const void* a, const void* b) {
    const Runner* r1 = *(const Runner**)a;
    const Runner* r2 = *(const Runner**)b;
    if (!r1->finished && !r2->finished) return 0;
    if (!r1->finished) return 1;
    if (!r2->finished) return -1;
    return (r1->finish_time > r2->finish_time) - (r1->finish_time < r2->finish_time);
}
