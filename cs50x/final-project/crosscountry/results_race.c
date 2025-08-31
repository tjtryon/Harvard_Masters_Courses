#include "configure_race.h"
#include "race_timing.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

void show_individual_results() {
    Runner* finished[MAX_RUNNERS];
    int count = 0;
    for (int i = 0; i < runner_count; ++i) {
        if (runners[i].finished) {
            finished[count++] = &runners[i];
        }
    }

    qsort(finished, count, sizeof(Runner*), compare_runners_by_time);

    printf("\n--- Individual Results ---\n");
    for (int i = 0; i < count; ++i) {
        printf("%d: %s (%s) - %.3f s\n", finished[i]->bib, finished[i]->name, finished[i]->team, finished[i]->finish_time);
    }
    printf("--------------------------\n");
}

void show_team_results() {
    printf("\n--- Team Scores (Top 5 + 2 displacers) ---\n");
    for (int i = 0; i < team_count; ++i) {
        Team* t = &teams[i];
        qsort(t->runners, t->runner_count, sizeof(Runner*), compare_runners_by_time);

        double score = 0;
        int count = 0;
        for (int j = 0; j < t->runner_count && count < 5; ++j) {
            if (t->runners[j]->finished) {
                score += t->runners[j]->finish_time;
                count++;
            }
        }
        printf("Team %s: ", t->name);
        if (count == 5) {
            printf("%.3f (Top 5) | ", score);
        } else {
            printf("Incomplete | ");
        }

        // Displacers
        printf("Displacers: ");
        int displacers = 0;
        for (int j = 5; j < t->runner_count && displacers < 2; ++j) {
            if (t->runners[j]->finished) {
                printf("%s(%.3f) ", t->runners[j]->name, t->runners[j]->finish_time);
                displacers++;
            }
        }
        printf("\n");
    }
    printf("-----------------------------------------\n");
}

void save_results_csv(const char* filename) {
    FILE* file = fopen(filename, "w");
    if (!file) {
        perror("Error opening results file");
        exit(1);
    }
    fprintf(file, "bib,name,team,finish_time\n");
    for (int i = 0; i < runner_count; ++i) {
        if (runners[i].finished)
            fprintf(file, "%d,%s,%s,%.3f\n", runners[i].bib, runners[i].name, runners[i].team, runners[i].finish_time);
        else
            fprintf(file, "%d,%s,%s,DNF\n", runners[i].bib, runners[i].name, runners[i].team);
    }
    fclose(file);
}

void save_results_html(const char* filename) {
    FILE* file = fopen(filename, "w");
    if (!file) {
        perror("Error opening HTML file");
        exit(1);
    }
    fprintf(file, "<html><head><title>Race Results</title></head><body>\n");
    fprintf(file, "<h1>Individual Results</h1>\n<table border='1'><tr><th>Bib</th><th>Name</th><th>Team</th><th>Time</th></tr>\n");
    for (int i = 0; i < runner_count; ++i) {
        if (runners[i].finished)
            fprintf(file, "<tr><td>%d</td><td>%s</td><td>%s</td><td>%.3f</td></tr>\n",
                    runners[i].bib, runners[i].name, runners[i].team, runners[i].finish_time);
        else
            fprintf(file, "<tr><td>%d</td><td>%s</td><td>%s</td><td>DNF</td></tr>\n",
                    runners[i].bib, runners[i].name, runners[i].team);
    }
    fprintf(file, "</table></body></html>\n");
    fclose(file);
    printf("Results saved to %s\n", filename);
}
