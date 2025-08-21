#include "configure_race.h"
#include "race_timing.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

void interactive_menu() {
    int choice;
    char input[20];
    while (1) {
        printf("\n--- Menu ---\n");
        printf("1. Record finish time\n");
        printf("2. Show individual results\n");
        printf("3. Show team results\n");
        printf("4. Save results (CSV)\n");
        printf("5. Save results (HTML)\n");
        printf("6. Exit\n");
        printf("Enter choice: ");
        if (!fgets(input, sizeof(input), stdin)) break;
        choice = atoi(input);

        switch (choice) {
            case 1:
                printf("Enter bib number: ");
                if (fgets(input, sizeof(input), stdin)) {
                    int bib = atoi(input);
                    record_finish(bib);
                }
                break;
            case 2:
                show_individual_results();
                break;
            case 3:
                show_team_results();
                break;
            case 4:
                save_results_csv("results.csv");
                printf("CSV results saved to results.csv\n");
                break;
            case 5:
                save_results_html("results.html");
                break;
            case 6:
                return;
            default:
                printf("Invalid choice.\n");
        }
    }
}

int main() {
    load_runners("runners.csv");
    start_race();
    interactive_menu();
    return 0;
}
