// race_timing_gui.c
#include <gtk/gtk.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>

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
struct timeval start_time;

GtkWidget *text_view;

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
        if (sscanf(line, "%d,%49[^,],%49[^\n]", &bib, name, team) != 3) continue;
        // check duplicate
        for (int i = 0; i < runner_count; ++i)
            if (runners[i].bib == bib) goto skip;
        Runner* r = &runners[runner_count];
        r->bib = bib;
        strncpy(r->name, name, NAME_LEN);
        strncpy(r->team, team, TEAM_LEN);
        r->finish_time = -1;
        r->finished = 0;
        runner_count++;
        // team
        int found = 0;
        for (int i = 0; i < team_count; ++i)
            if (strcmp(teams[i].name, team) == 0) {
                teams[i].runners[teams[i].runner_count++] = r;
                found = 1;
                break;
            }
        if (!found) {
            strncpy(teams[team_count].name, team, TEAM_LEN);
            teams[team_count].runners[0] = r;
            teams[team_count].runner_count = 1;
            team_count++;
        }
        skip:;
    }
    fclose(file);
}

void start_race() {
    gettimeofday(&start_time, NULL);
    gtk_text_buffer_set_text(gtk_text_view_get_buffer(GTK_TEXT_VIEW(text_view)),
                             "Race started!\n", -1);
}

double get_elapsed_time() {
    struct timeval now;
    gettimeofday(&now, NULL);
    return (now.tv_sec - start_time.tv_sec) + (now.tv_usec - start_time.tv_usec) / 1e6;
}

void record_finish(int bib) {
    for (int i = 0; i < runner_count; ++i) {
        if (runners[i].bib == bib) {
            if (runners[i].finished) return;
            double elapsed = get_elapsed_time();
            if (elapsed < 0) return;
            runners[i].finish_time = elapsed;
            runners[i].finished = 1;
            char msg[128];
            snprintf(msg, sizeof(msg), "Bib %d finished at %.3f s\n", bib, elapsed);
            GtkTextBuffer* buffer = gtk_text_view_get_buffer(GTK_TEXT_VIEW(text_view));
            GtkTextIter end;
            gtk_text_buffer_get_end_iter(buffer, &end);
            gtk_text_buffer_insert(buffer, &end, msg, -1);
            return;
        }
    }
}

int compare_runners(const void* a, const void* b) {
    const Runner* r1 = *(const Runner**)a;
    const Runner* r2 = *(const Runner**)b;
    if (!r1->finished) return 1;
    if (!r2->finished) return -1;
    return (r1->finish_time > r2->finish_time) - (r1->finish_time < r2->finish_time);
}

void show_individual_results() {
    Runner* finished[MAX_RUNNERS];
    int count = 0;
    for (int i = 0; i < runner_count; ++i)
        if (runners[i].finished)
            finished[count++] = &runners[i];
    qsort(finished, count, sizeof(Runner*), compare_runners);
    char buffer[8192] = "\n--- Individual Results ---\n";
    char line[128];
    for (int i = 0; i < count; ++i) {
        snprintf(line, sizeof(line), "%d: %s (%s) - %.3f s\n",
                 finished[i]->bib, finished[i]->name, finished[i]->team, finished[i]->finish_time);
        strncat(buffer, line, sizeof(buffer) - strlen(buffer) - 1);
    }
    GtkTextBuffer* textbuf = gtk_text_view_get_buffer(GTK_TEXT_VIEW(text_view));
    gtk_text_buffer_set_text(textbuf, buffer, -1);
}

void show_team_results() {
    char buffer[8192] = "\n--- Team Results ---\n";
    char line[256];
    for (int i = 0; i < team_count; ++i) {
        Team* t = &teams[i];
        qsort(t->runners, t->runner_count, sizeof(Runner*), compare_runners);
        double score = 0;
        int count = 0;
        for (int j = 0; j < t->runner_count && count < 5; ++j) {
            if (t->runners[j]->finished) {
                score += t->runners[j]->finish_time;
                count++;
            }
        }
        snprintf(line, sizeof(line), "Team %s: %s %.3f\n",
                 t->name, (count==5)?"Total":"Incomplete", score);
        strncat(buffer, line, sizeof(buffer) - strlen(buffer) - 1);
    }
    GtkTextBuffer* textbuf = gtk_text_view_get_buffer(GTK_TEXT_VIEW(text_view));
    gtk_text_buffer_set_text(textbuf, buffer, -1);
}

void save_html(const char* filename) {
    FILE* file = fopen(filename, "w");
    fprintf(file, "<html><body><h1>Race Results</h1><table border=1><tr><th>Bib</th><th>Name</th><th>Team</th><th>Time</th></tr>\n");
    for (int i = 0; i < runner_count; ++i) {
        if (runners[i].finished)
            fprintf(file, "<tr><td>%d</td><td>%s</td><td>%s</td><td>%.3f</td></tr>\n",
                    runners[i].bib, runners[i].name, runners[i].team, runners[i].finish_time);
    }
    fprintf(file, "</table></body></html>");
    fclose(file);
}

void on_start_clicked(GtkButton *button, gpointer user_data) {
    start_race();
}

void on_enter_bib(GtkButton *button, gpointer entry) {
    const char* bib_str = gtk_entry_buffer_get_text(gtk_entry_get_buffer(GTK_ENTRY(entry)));
    int bib = atoi(bib_str);
    if (bib > 0) record_finish(bib);
}

void on_show_indiv(GtkButton *button, gpointer user_data) {
    show_individual_results();
}

void on_show_team(GtkButton *button, gpointer user_data) {
    show_team_results();
}

void on_export(GtkButton *button, gpointer user_data) {
    save_html("results.html");
}

int main(int argc, char* argv[]) {
    gtk_init();
    load_runners("runners.csv");

    GtkWidget *window = gtk_window_new();
    gtk_window_set_title(GTK_WINDOW(window), "Race Timing System");
    gtk_window_set_default_size(GTK_WINDOW(window), 600, 400);

    GtkWidget *grid = gtk_grid_new();
    gtk_window_set_child(GTK_WINDOW(window), grid);

    GtkWidget *start_btn = gtk_button_new_with_label("Start Race");
    GtkWidget *entry = gtk_entry_new();
    GtkWidget *enter_btn = gtk_button_new_with_label("Enter Bib");
    GtkWidget *indiv_btn = gtk_button_new_with_label("Show Individual");
    GtkWidget *team_btn = gtk_button_new_with_label("Show Teams");
    GtkWidget *export_btn = gtk_button_new_with_label("Export HTML");
    text_view = gtk_text_view_new();

    gtk_grid_attach(GTK_GRID(grid), start_btn, 0, 0, 1, 1);
    gtk_grid_attach(GTK_GRID(grid), entry, 1, 0, 1, 1);
    gtk_grid_attach(GTK_GRID(grid), enter_btn, 2, 0, 1, 1);
    gtk_grid_attach(GTK_GRID(grid), indiv_btn, 0, 1, 1, 1);
    gtk_grid_attach(GTK_GRID(grid), team_btn, 1, 1, 1, 1);
    gtk_grid_attach(GTK_GRID(grid), export_btn, 2, 1, 1, 1);
    gtk_grid_attach(GTK_GRID(grid), text_view, 0, 2, 3, 1);

    g_signal_connect(start_btn, "clicked", G_CALLBACK(on_start_clicked), NULL);
    g_signal_connect(enter_btn, "clicked", G_CALLBACK(on_enter_bib), entry);
    g_signal_connect(indiv_btn, "clicked", G_CALLBACK(on_show_indiv), NULL);
    g_signal_connect(team_btn, "clicked", G_CALLBACK(on_show_team), NULL);
    g_signal_connect(export_btn, "clicked", G_CALLBACK(on_export), NULL);

    gtk_widget_show(window);
    gtk_main();
    return 0;
}
