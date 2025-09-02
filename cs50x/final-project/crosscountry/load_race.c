#include "configure_race.h"
#include "race_timing.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

void load_runners(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Error opening runners file");
        exit(1);
    }

    char line[256];
    while (fgets(line, sizeof(line), file)) {
        int bib;
        char name[NAME_LEN], team[TEAM_LEN];

        if (sscanf(line, "%d,%49[^,],%49[^\n]", &bib, name, team) != 3) {
            printf("Skipping invalid line: %s\n", line);
            continue;
        }

        // Check for duplicate bib
        for (int i = 0; i < runner_count; ++i) {
            if (runners[i].bib == bib) {
                printf("Duplicate bib %d found! Skipping.\n", bib);
                goto skip;
            }
        }

        Runner* r = &runners[runner_count];
        r->bib = bib;
        strncpy(r->name, name, NAME_LEN);
        strncpy(r->team, team, TEAM_LEN);
        r->finish_time = -1;
        r->finished = 0;
        runner_count++;

        // Add to team
        int found = 0;
        for (int i = 0; i < team_count; ++i) {
            if (strcmp(teams[i].name, team) == 0) {
                teams[i].runners[teams[i].runner_count++] = r;
                found = 1;
                break;
            }
        }
        if (!found) {
            strncpy(teams[team_count].name, team, TEAM_LEN);
            teams[team_count].runners[0] = r;
            teams[team_count].runner_count = 1;
            team_count++;
        }

        if (runner_count >= MAX_RUNNERS) break;
        skip:;
    }

    fclose(file);
}
