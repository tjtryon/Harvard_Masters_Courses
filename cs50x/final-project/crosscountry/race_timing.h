#ifndef RACE_TIMING_H_
#define RACE_TIMING_H_

void start_race(void);
double get_elapsed_time(void);
void record_finish(int);
int compare_runners_by_time(const void*, const void*);
void start_race(void);
double get_elapsed_time(void);
void record_finish(int);
void load_runners(const char*);
void interactive_menu(void);
void show_individual_results(void);
void show_team_results(void);
void save_results_csv(const char*);
void save_results_html(const char*);

#endif
