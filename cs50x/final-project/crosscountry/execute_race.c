#include "configure_race.h"
#include "race_timing.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

struct timeval start_time;

void start_race() {
    gettimeofday(&start_time, NULL);
    printf("Race started at %ld.%03ld seconds\n", start_time.tv_sec, start_time.tv_usec / 1000);
}

double get_elapsed_time() {
    struct timeval now;
    gettimeofday(&now, NULL);
    double seconds = (now.tv_sec - start_time.tv_sec) + (now.tv_usec - start_time.tv_usec) / 1e6;
    return seconds;
}

void record_finish(int bib) {
    for (int i = 0; i < runner_count; ++i) {
        if (runners[i].bib == bib) {
            if (runners[i].finished) {
                printf("Runner %d already finished!\n", bib);
                return;
            }
            double elapsed = get_elapsed_time();
            if (elapsed < 0) {
                printf("Negative finish time detected for bib %d!\n", bib);
                return;
            }
            runners[i].finish_time = elapsed;
            runners[i].finished = 1;
            printf("Bib %d finished at %.3f seconds\n", bib, elapsed);
            return;
        }
    }
    printf("Bib %d not found!\n", bib);
}
