#ifndef CONFIGURE_RACE_H_
#define CONFIGURE_RACE_H_

#define MAX_RUNNERS 1000
#define MAX_TEAMS 50
#define NAME_LEN 50
#define TEAM_LEN 50

typedef struct {
    int bib;
    char name[NAME_LEN];
    char team[TEAM_LEN];
    double finish_time;
    int finished;
} Runner;

typedef struct {
    char name[TEAM_LEN];
    Runner* runners[MAX_RUNNERS];
    int runner_count;
} Team;

Runner runners[MAX_RUNNERS];
int runner_count = 0;
Team teams[MAX_TEAMS];
int team_count = 0;

#endif
