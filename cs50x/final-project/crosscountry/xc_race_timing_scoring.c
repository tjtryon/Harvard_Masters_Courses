#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_RUNNERS 200
#define MAX_TEAMS 20
#define MAX_NAME_LEN 50
#define SCORING_RUNNERS 5

typedef struct {
    char name[MAX_NAME_LEN];
    char team[MAX_NAME_LEN];
    int finishTime;  // in seconds
    int place;
} Runner;

typedef struct {
    char teamName[MAX_NAME_LEN];
    int score;
    int runnersCount;
} TeamScore;

// Utility Functions
void clearBuffer() {
    while (getchar() != '\n');
}

int isDuplicateName(Runner runners[], int count, const char *name) {
    for (int i = 0; i < count; i++) {
        if (strcmp(runners[i].name, name) == 0)
            return 1;
    }
    return 0;
}

// CSV File Input
int readRunnersFromCSV(const char *filename, Runner runners[]) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Error opening file %s\n", filename);
        return 0;
    }

    int count = 0;
    while (fscanf(file, "%49[^,],%49[^,],%d\n", runners[count].name, runners[count].team, &runners[count].finishTime) == 3) {
        if (runners[count].finishTime < 0) {
            printf("Invalid time for runner %s. Skipping.\n", runners[count].name);
            continue;
        }
        if (isDuplicateName(runners, count, runners[count].name)) {
            printf("Duplicate name detected: %s. Skipping.\n", runners[count].name);
            continue;
        }
        count++;
        if (count >= MAX_RUNNERS) break;
    }

    fclose(file);
    return count;
}

// Save Results
void writeResultsToFile(const char *filename, Runner runners[], int runnerCount, TeamScore teams[], int teamCount) {
    FILE *file = fopen(filename, "w");
    if (!file) {
        printf("Error opening file %s\n", filename);
        return;
    }

    fprintf(file, "--- Individual Results ---\n");
    for (int i = 0; i < runnerCount; i++) {
        fprintf(file, "%d. %-20s %-15s %d seconds\n", runners[i].place, runners[i].name, runners[i].team, runners[i].finishTime);
    }

    fprintf(file, "\n--- Team Scores (Top %d finishers) ---\n", SCORING_RUNNERS);
    for (int i = 0; i < teamCount; i++) {
        if (teams[i].runnersCount >= SCORING_RUNNERS) {
            fprintf(file, "%d. %-20s %d points\n", i + 1, teams[i].teamName, teams[i].score);
        }
    }

    fclose(file);
}

// Manual Input
void inputRunners(Runner runners[], int *count) {
    printf("Enter number of runners: ");
    scanf("%d", count);
    clearBuffer();

    for (int i = 0; i < *count; i++) {
        printf("\nRunner #%d\n", i + 1);

        do {
            printf("Enter name: ");
            fgets(runners[i].name, MAX_NAME_LEN, stdin);
            runners[i].name[strcspn(runners[i].name, "\n")] = '\0';
            if (isDuplicateName(runners, i, runners[i].name))
                printf("Duplicate name. Please enter a unique name.\n");
        } while (isDuplicateName(runners, i, runners[i].name));

        printf("Enter team name: ");
        fgets(runners[i].team, MAX_NAME_LEN, stdin);
        runners[i].team[strcspn(runners[i].team, "\n")] = '\0';

        do {
            printf("Enter finish time in seconds: ");
            scanf("%d", &runners[i].finishTime);
            clearBuffer();
            if (runners[i].finishTime < 0)
                printf("Time cannot be negative.\n");
        } while (runners[i].finishTime < 0);
    }
}

// Live Timing Input
void startLiveRace(Runner runners[], int *runnerCount) {
    printf("Enter number of runners: ");
    scanf("%d", runnerCount);
    clearBuffer();

    for (int i = 0; i < *runnerCount; i++) {
        printf("\nRunner #%d\n", i + 1);

        do {
            printf("Enter name: ");
            fgets(runners[i].name, MAX_NAME_LEN, stdin);
            runners[i].name[strcspn(runners[i].name, "\n")] = '\0';
            if (isDuplicateName(runners, i, runners[i].name))
                printf("Duplicate name. Please enter a unique name.\n");
        } while (isDuplicateName(runners, i, runners[i].name));

        printf("Enter team name: ");
        fgets(runners[i].team, MAX_NAME_LEN, stdin);
        runners[i].team[strcspn(runners[i].team, "\n")] = '\0';

        printf("Press Enter to START timing for %s...", runners[i].name);
        getchar();
        time_t start = time(NULL);

        printf("Timing started... Press Enter to STOP timing for %s.", runners[i].name);
        getchar();
        time_t end = time(NULL);

        runners[i].finishTime = (int)(end - start);
        printf("Recorded time: %d seconds\n", runners[i].finishTime);
    }
}

// Sorting and Scoring
void sortByTime(Runner runners[], int count) {
    for (int i = 0; i < count - 1; i++) {
        for (int j = i + 1; j < count; j++) {
            if (runners[j].finishTime < runners[i].finishTime) {
                Runner temp = runners[i];
                runners[i] = runners[j];
                runners[j] = temp;
            }
        }
    }

    for (int i = 0; i < count; i++) {
        runners[i].place = i + 1;
    }
}

int findTeamIndex(TeamScore teams[], int teamCount, const char *teamName) {
    for (int i = 0; i < teamCount; i++) {
        if (strcmp(teams[i].teamName, teamName) == 0)
            return i;
    }
    return -1;
}

void calculateTeamScores(Runner runners[], int count, TeamScore teams[], int *teamCount) {
    *teamCount = 0;
    for (int i = 0; i < count; i++) {
        int idx = findTeamIndex(teams, *teamCount, runners[i].team);
        if (idx == -1) {
            strcpy(teams[*teamCount].teamName, runners[i].team);
            teams[*teamCount].score = 0;
            teams[*teamCount].runnersCount = 0;
            idx = (*teamCount)++;
        }

        if (teams[idx].runnersCount < SCORING_RUNNERS) {
            teams[idx].score += runners[i].place;
            teams[idx].runnersCount++;
        }
    }
}

// Display Functions
void displayIndividualResults(Runner runners[], int count) {
    printf("\n--- Individual Results ---\n");
    printf("%-4s %-20s %-15s %-10s\n", "PLC", "Name", "Team", "Time(s)");
    for (int i = 0; i < count; i++) {
        printf("%-4d %-20s %-15s %-10d\n", runners[i].place, runners[i].name, runners[i].team, runners[i].finishTime);
    }
}

void displayTeamScores(TeamScore teams[], int teamCount) {
    for (int i = 0; i < teamCount - 1; i++) {
        for (int j = i + 1; j < teamCount; j++) {
            if (teams[j].score < teams[i].score) {
                TeamScore temp = teams[i];
                teams[i] = teams[j];
                teams[j] = temp;
            }
        }
    }

    printf("\n--- Team Scores (Top %d finishers) ---\n", SCORING_RUNNERS);
    printf("%-4s %-20s %-10s\n", "PLC", "Team", "Score");
    for (int i = 0; i < teamCount; i++) {
        if (teams[i].runnersCount >= SCORING_RUNNERS) {
            printf("%-4d %-20s %-10d\n", i + 1, teams[i].teamName, teams[i].score);
        } else {
            printf(" -   %-20s (Not enough finishers)\n", teams[i].teamName);
        }
    }
}

// Menu
void displayMenu() {
    printf("\n--- Cross Country Race Timing and Scoring ---\n");
    printf("1. Input runners manually (no timing)\n");
    printf("2. Time runners live using system clock\n");
    printf("3. Read runners from CSV file\n");
    printf("4. Display individual results\n");
    printf("5. Display team scores\n");
    printf("6. Save results to file\n");
    printf("7. Exit\n");
    printf("Choose an option: ");
}

// Main
int main() {
    Runner runners[MAX_RUNNERS];
    TeamScore teams[MAX_TEAMS];
    int runnerCount = 0, teamCount = 0;
    int dataLoaded = 0;
    int choice;

    while (1) {
        displayMenu();
        if (scanf("%d", &choice) != 1) {
            clearBuffer();
            printf("Invalid input. Please enter a number.\n");
            continue;
        }

        clearBuffer();

        switch (choice) {
            case 1:
                inputRunners(runners, &runnerCount);
                sortByTime(runners, runnerCount);
                calculateTeamScores(runners, runnerCount, teams, &teamCount);
                dataLoaded = 1;
                break;

            case 2:
                startLiveRace(runners, &runnerCount);
                sortByTime(runners, runnerCount);
                calculateTeamScores(runners, runnerCount, teams, &teamCount);
                dataLoaded = 1;
                break;

            case 3: {
                char filename[100];
                printf("Enter CSV filename (name,team,time): ");
                fgets(filename, sizeof(filename), stdin);
                filename[strcspn(filename, "\n")] = '\0';

                runnerCount = readRunnersFromCSV(filename, runners);
                sortByTime(runners, runnerCount);
                calculateTeamScores(runners, runnerCount, teams, &teamCount);
                dataLoaded = 1;
                break;
            }

            case 4:
                if (dataLoaded)
                    displayIndividualResults(runners, runnerCount);
                else
                    printf("No data loaded.\n");
                break;

            case 5:
                if (dataLoaded)
                    displayTeamScores(teams, teamCount);
                else
                    printf("No data loaded.\n");
                break;

            case 6: {
                if (!dataLoaded) {
                    printf("No data to save.\n");
                    break;
                }
                char outFile[100];
                printf("Enter output filename: ");
                fgets(outFile, sizeof(outFile), stdin);
                outFile[strcspn(outFile, "\n")] = '\0';
                writeResultsToFile(outFile, runners, runnerCount, teams, teamCount);
                printf("Results saved.\n");
                break;
            }

            case 7:
                printf("Goodbye!\n");
                return 0;

            default:
                printf("Invalid choice. Try again.\n");
        }
    }
    return 0;
}
